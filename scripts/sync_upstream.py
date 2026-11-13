"""Vendor pinned upstream files as non-discoverable methods and refresh the index."""

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "pm-perspective"


def git(repo, *args):
    return subprocess.check_output([
        "git", "-c", "core.autocrlf=false", "-c", "core.eol=lf", "-C", str(repo), *args
    ])


def export_source(repo, commit, target):
    files = {}
    archive_bytes = git(repo, "archive", "--format=tar", commit)
    with tarfile.open(fileobj=io.BytesIO(archive_bytes)) as archive:
        for member in archive.getmembers():
            if member.isdir():
                continue
            if not member.isfile():
                raise ValueError(f"Unsupported upstream archive entry: {member.name}")
            relative = Path(member.name)
            if relative.name.lower() == "skill.md":
                relative = relative.with_name("METHOD.md")
            if relative.name in (".gitattributes", ".gitignore"):
                relative = relative.with_name("UPSTREAM" + relative.name)
            destination = (target / relative).resolve()
            if not destination.is_relative_to(target.resolve()):
                raise ValueError(f"Unsafe archive path: {member.name}")
            if destination.exists():
                raise ValueError(f"Upstream filename collision: {relative}")
            content = archive.extractfile(member).read()
            if relative.suffix.lower() == ".md":
                content = re.sub(
                    r"(?i)skill\.md", "METHOD.md", content.decode("utf-8-sig")
                ).encode("utf-8")
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(content)
            files[relative.as_posix()] = hashlib.sha256(content).hexdigest()
    return files


def read_metadata(path):
    frontmatter = path.read_text(encoding="utf-8").split("---", 2)[1]
    try:
        metadata = yaml.safe_load(frontmatter)
        return metadata, False
    except yaml.YAMLError:
        # Some upstream descriptions contain unquoted colons. Keep their original text.
        metadata = {}
        for field in ("name", "description"):
            match = re.search(
                r"^" + field + r":\s*(.*(?:\n[ \t]+[^\n]*)*)", frontmatter, re.M
            )
            if not match:
                raise ValueError(f"Missing {field} in {path}")
            metadata[field] = match.group(1)
        return metadata, True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, help="Export existing clean local checkouts")
    args = parser.parse_args()
    manifest_path = SKILL / "references/library.json"
    old_manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    with tempfile.TemporaryDirectory(prefix=".pm-upstream-", dir=ROOT) as temp:
        staging = Path(temp)
        staged_skill = staging / "pm-perspective"
        shutil.copytree(SKILL, staged_skill, ignore=shutil.ignore_patterns("library", "__pycache__"))
        staged_library = staged_skill / "library"
        sources, rows, warnings, snapshots = [], [], [], {}
        for source in old_manifest["sources"]:
            source_id = source["id"]
            if not re.fullmatch(r"[a-z0-9-]+", source_id):
                raise ValueError(f"Invalid source ID: {source_id}")
            if args.source_root:
                repo = args.source_root.resolve() / source_id
                if git(repo, "status", "--porcelain").strip():
                    raise ValueError(f"Local upstream is modified: {source_id}")
            else:
                if not re.fullmatch(r"https://github\.com/[\w.-]+/[\w.-]+", source["url"]):
                    raise ValueError(f"Invalid upstream URL: {source['url']}")
                repo = staging / "checkouts" / source_id
                subprocess.run(
                    ["git", "clone", "--depth", "1", source["url"] + ".git", str(repo)],
                    check=True,
                )
            commit = git(repo, "rev-parse", "HEAD").decode().strip()
            target = staged_library / source_id
            snapshots[source_id] = export_source(repo, commit, target)
            skills = sorted(target.glob("skills/*/METHOD.md"))
            if not skills:
                raise ValueError(f"No skills found in {source_id}")
            for path in skills:
                metadata, warning = read_metadata(path)
                relative = path.relative_to(staged_library).as_posix()
                if warning:
                    warnings.append(relative)
                rows.append({
                    "source": source_id,
                    "name": metadata["name"],
                    "path": relative,
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
                    "description": " ".join(metadata["description"].split()),
                })
            sources.append({**source, "commit": commit, "skill_count": len(skills)})

        changed = sources != old_manifest["sources"] or old_manifest.get("root") != "../library"
        manifest = {
            "checked_on": datetime.now(timezone.utc).date().isoformat() if changed else old_manifest["checked_on"],
            "root": "../library",
            "sources": sources,
            "upstream_frontmatter_parse_warnings": warnings,
            "transform": "Rename skill.md manifests to METHOD.md and update Markdown references; rename .gitattributes and .gitignore to UPSTREAM.gitattributes and UPSTREAM.gitignore to isolate upstream Git settings; preserve other file bytes.",
        }
        references = staged_skill / "references"
        for filename, value in (("library.json", manifest), ("snapshots.json", snapshots)):
            (references / filename).write_text(
                json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )
        with (references / "catalog.tsv").open("w", encoding="utf-8", newline="") as stream:
            writer = csv.DictWriter(
                stream, fieldnames=["source", "name", "path", "sha256", "description"], delimiter="\t"
            )
            writer.writeheader()
            writer.writerows(rows)
        subprocess.run([sys.executable, "-X", "utf8", str(staged_skill / "scripts/check_library.py")], check=True)

        previous = staging / "previous"
        SKILL.rename(previous)
        try:
            staged_skill.rename(SKILL)
        except OSError:
            previous.rename(SKILL)
            raise
    print(f"Synced {len(rows)} methods from {len(sources)} sources")


if __name__ == "__main__":
    main()
