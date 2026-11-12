import io
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

from scripts.sync_upstream import export_source, read_metadata


def archive_bytes(entries):
    stream = io.BytesIO()
    with tarfile.open(fileobj=stream, mode="w") as archive:
        for name, content in entries:
            member = tarfile.TarInfo(name)
            member.size = len(content)
            archive.addfile(member, io.BytesIO(content))
    return stream.getvalue()


class ExportTests(unittest.TestCase):
    def test_preserves_resources_and_rewrites_method_links(self):
        entries = [
            ("skills/demo/SKILL.md", b"[next](../other/SKILL.md)"),
            ("skills/other/skill.md", b"# Other"),
            ("assets/example.bin", bytes(range(256))),
            ("LICENSE", b"original license"),
        ]
        with tempfile.TemporaryDirectory() as temp, patch(
            "scripts.sync_upstream.git", return_value=archive_bytes(entries)
        ):
            root = Path(temp)
            files = export_source(root, "commit", root)
            self.assertEqual((root / "skills/demo/METHOD.md").read_bytes(), b"[next](../other/METHOD.md)")
            self.assertEqual((root / "assets/example.bin").read_bytes(), bytes(range(256)))
            self.assertEqual((root / "LICENSE").read_bytes(), b"original license")
            self.assertEqual(len(files), 4)
            self.assertFalse(any(p.name.lower() == "skill.md" for p in root.rglob("*")))

    def test_rejects_path_traversal(self):
        with tempfile.TemporaryDirectory() as temp, patch(
            "scripts.sync_upstream.git", return_value=archive_bytes([("../escape.txt", b"bad")])
        ):
            with self.assertRaisesRegex(ValueError, "Unsafe archive path"):
                export_source(Path(temp), "commit", Path(temp))

    def test_rejects_transformation_collision(self):
        entries = [("skills/demo/METHOD.md", b"a"), ("skills/demo/SKILL.md", b"b")]
        with tempfile.TemporaryDirectory() as temp, patch(
            "scripts.sync_upstream.git", return_value=archive_bytes(entries)
        ):
            with self.assertRaisesRegex(ValueError, "filename collision"):
                export_source(Path(temp), "commit", Path(temp))

    def test_reads_upstream_unquoted_description(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "METHOD.md"
            path.write_text("---\nname: demo\ndescription: Work: use this method\n---\n", encoding="utf-8")
            metadata, warning = read_metadata(path)
            self.assertTrue(warning)
            self.assertEqual(metadata["description"], "Work: use this method")


if __name__ == "__main__":
    unittest.main()
