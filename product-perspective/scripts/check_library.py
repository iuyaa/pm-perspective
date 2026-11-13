"""Check the single entry point, pinned upstream trees, and all routing targets."""

import csv
import hashlib
import json
from pathlib import Path
import re


def main():
    skill_dir = Path(__file__).resolve().parents[1]
    references = skill_dir / "references"
    manifest = json.loads((references / "library.json").read_text(encoding="utf-8"))
    library_root = (references / manifest["root"]).resolve(strict=True)
    errors = []

    manifests = [p for p in skill_dir.rglob("*") if p.name.lower() == "skill.md"]
    if manifests != [skill_dir / "SKILL.md"]:
        errors.append("The registered directory must contain exactly one SKILL.md")

    with (references / "catalog.tsv").open(encoding="utf-8", newline="") as stream:
        catalog = list(csv.DictReader(stream, delimiter="\t"))

    expected_paths = set()
    for source in manifest["sources"]:
        repo = library_root / source["id"]
        skills = list(repo.glob("skills/*/METHOD.md"))
        if len(skills) != source["skill_count"]:
            errors.append(f"{source['id']}: skill count differs from manifest")
        expected_paths.update(p.relative_to(library_root).as_posix() for p in skills)
        if not (repo / "LICENSE").is_file():
            errors.append(f"{source['id']}: LICENSE is missing")

    snapshots = json.loads((references / "snapshots.json").read_text(encoding="utf-8"))
    for source in manifest["sources"]:
        repo = library_root / source["id"]
        actual_files = {p.relative_to(repo).as_posix() for p in repo.rglob("*") if p.is_file()}
        expected_files = snapshots[source["id"]]
        if actual_files != set(expected_files):
            errors.append(f"{source['id']}: snapshot file set differs")
        for relative, expected_digest in expected_files.items():
            path = (repo / relative).resolve()
            if not path.is_relative_to(repo.resolve()) or not path.is_file():
                errors.append(f"Invalid snapshot path: {relative}")
                continue
            if hashlib.sha256(path.read_bytes()).hexdigest() != expected_digest:
                errors.append(f"Snapshot file changed: {source['id']}/{relative}")

    catalog_paths = [row["path"] for row in catalog]
    if len(catalog_paths) != len(set(catalog_paths)):
        errors.append("Catalog contains duplicate paths")
    if set(catalog_paths) != expected_paths:
        errors.append("Catalog does not cover exactly the original skill directories")
    for row in catalog:
        path = (library_root / row["path"]).resolve()
        if not path.is_relative_to(library_root) or not path.is_file():
            errors.append(f"Invalid catalog target: {row['path']}")
            continue
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != row["sha256"]:
            errors.append(f"Skill content changed: {row['path']}")

    route_paths = set()
    for document in [skill_dir / "SKILL.md", *references.glob("*.md")]:
        content = document.read_text(encoding="utf-8")
        route_paths.update(re.findall(r"[\w-]+/skills/[\w-]+/METHOD\.md", content))
        for target in re.findall(r"\]\(([^)]+)\)", content):
            if "://" not in target and not target.startswith("#"):
                if not (document.parent / target.split("#")[0]).is_file():
                    errors.append(f"Broken reference in {document.name}: {target}")
    for path in sorted(route_paths):
        if path not in expected_paths:
            errors.append(f"Routing target is absent from catalog: {path}")

    if errors:
        raise SystemExit("\n".join(errors))
    print(
        f"PASS: 1 exposed SKILL.md, {len(manifest['sources'])} pinned source snapshots, "
        f"{len(catalog)} indexed skills, {len(route_paths)} direct routing targets, "
        "all local reference links valid."
    )


if __name__ == "__main__":
    main()
