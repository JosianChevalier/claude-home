"""Integration checks for shared harness state storage."""

import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest
import uuid


ROOT = Path(__file__).resolve().parents[2]
NOTEBOOK = ROOT / "tools/grab-notebook"
EXPLORE = ROOT / "philosophy/navigation/navigation.sh"


class TempStorageTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.base = Path(self.tmp.name)
        self.session = "test_" + uuid.uuid4().hex

    def call(self, script, *args, root=None):
        env = os.environ.copy()
        env.pop("CLAUDE_CODE_SESSION_ID", None)
        env.pop("TMPDIR", None)
        env["OPENCODE_SESSION_ID"] = self.session
        if root is not None:
            env["TMPDIR"] = str(root)
        return subprocess.run([str(script), *args], env=env, text=True, capture_output=True)

    def test_roots_and_reuse(self):
        for root in (self.base / "one", self.base / "two"):
            if root.name == "two":
                root.mkdir(mode=0o755)
            first = self.call(NOTEBOOK, root=root)
            self.assertEqual(first.returncode, 0, first.stderr)
            notebook = Path(first.stdout.strip())
            self.assertEqual(notebook.parent, root)
            self.assertEqual(root.stat().st_mode & 0o777, 0o700)
            notebook.write_text("keep me")
            again = self.call(NOTEBOOK, root=root)
            self.assertEqual(again.stdout, first.stdout)
            self.assertEqual(notebook.read_text(), "keep me")

            start = self.call(EXPLORE, "explore", "start", root=root)
            self.assertEqual(start.returncode, 0, start.stderr)
            run = re.search(r"^run ([0-9a-f]{4})", start.stdout).group(1)
            state = root / f"philosophy-explore-{self.session}-{run}.json"
            self.assertTrue(state.exists())
            served = self.call(EXPLORE, "explore", run, "conversation-as-interface", root=root)
            self.assertEqual(served.returncode, 0, served.stderr)
            self.assertIn('file name="philosophy/conversation-as-interface.md"', served.stdout)
            self.assertIn("conversation-as-interface", state.read_text())
            repeat = self.call(EXPLORE, "explore", run, "conversation-as-interface", root=root)
            self.assertEqual(repeat.returncode, 0, repeat.stderr)
            self.assertNotIn('file name="philosophy/conversation-as-interface.md"', repeat.stdout)

    def test_unset_keeps_legacy_session_state(self):
        notebook = Path("/tmp") / f"notebook-{self.session}.md"
        self.addCleanup(notebook.unlink, missing_ok=True)
        first = self.call(NOTEBOOK)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout.strip(), str(notebook))
        notebook.write_text("legacy")
        self.assertEqual(self.call(NOTEBOOK).stdout, first.stdout)
        self.assertEqual(self.call(NOTEBOOK, root=Path("/tmp")).stdout, first.stdout)
        self.assertEqual(notebook.read_text(), "legacy")
        start = self.call(EXPLORE, "explore", "start")
        self.assertEqual(start.returncode, 0, start.stderr)
        run = re.search(r"^run ([0-9a-f]{4})", start.stdout).group(1)
        state = Path("/tmp") / f"philosophy-explore-{self.session}-{run}.json"
        self.addCleanup(state.unlink, missing_ok=True)
        self.assertEqual(self.call(EXPLORE, "explore", run, "conversation-as-interface").returncode, 0)

    @unittest.skipUnless(Path("/tmp").is_symlink(), "/tmp is a system link only on macOS")
    def test_accepts_root_owned_link_as_parent(self):
        root = Path("/tmp") / self.session
        self.addCleanup(lambda: subprocess.run(["rm", "-rf", str(root)]))
        result = self.call(NOTEBOOK, root=root)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(Path(result.stdout.strip()).parent, root)

    def test_rejects_unsafe_directory_and_identifiers(self):
        link = self.base / "link"
        link.symlink_to(self.base, target_is_directory=True)
        for root in (link, link / "child", Path("relative"), self.base / ".." / "other"):
            for script, args in ((NOTEBOOK, ()), (EXPLORE, ("explore", "start"))):
                result = self.call(script, *args, root=root)
                self.assertNotEqual(result.returncode, 0, (root, result.stdout))
        self.session = "../escape"
        self.assertNotEqual(self.call(NOTEBOOK).returncode, 0)
        self.assertNotEqual(self.call(EXPLORE, "explore", "start").returncode, 0)

    def test_rejects_symlinked_state(self):
        root = self.base / "private"
        root.mkdir(mode=0o700)
        notebook = root / f"notebook-{self.session}.md"
        notebook.symlink_to(self.base / "target")
        self.assertNotEqual(self.call(NOTEBOOK, root=root).returncode, 0)
        state = root / f"philosophy-explore-{self.session}-abcd.json"
        state.symlink_to(self.base / "target")
        result = self.call(EXPLORE, "explore", "abcd", "conversation-as-interface", root=root)
        self.assertIn("unsafe exploration state", result.stderr)


if __name__ == "__main__":
    unittest.main()
