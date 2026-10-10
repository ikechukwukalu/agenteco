"""End-to-end checks for the versioned, complete governance mirror."""

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / "tools" / "build_governance_mirror.py"
VERIFY = ROOT / "tools" / "verify_governance_mirror.py"


class GovernanceMirrorTests(unittest.TestCase):
    def test_complete_copy_and_tamper_detection(self):
        with tempfile.TemporaryDirectory(prefix="agenteco-mirror-") as temporary:
            mirror = Path(temporary) / "mirror"
            build = subprocess.run(
                [
                    sys.executable,
                    str(BUILD),
                    "--product",
                    "Verification",
                    "--classification",
                    "internal",
                    "--output",
                    str(mirror),
                ],
                cwd=ROOT,
                capture_output=True,
                text=True,
            )
            self.assertEqual(build.returncode, 0, build.stderr)
            manifest = json.loads((mirror / "manifest.json").read_text(encoding="utf-8"))
            tracked = subprocess.check_output(
                ["git", "ls-tree", "-r", "--name-only", "HEAD"], cwd=ROOT, text=True
            ).splitlines()
            self.assertEqual(set(manifest["files"]), set(tracked))

            valid = subprocess.run(
                [sys.executable, str(VERIFY), str(mirror)], capture_output=True, text=True
            )
            self.assertEqual(valid.returncode, 0, valid.stderr)

            # A modified file or an extra file must invalidate the exact copy.
            readme = mirror / "repository" / "README.md"
            original = readme.read_bytes()
            readme.write_bytes(original + b"\nmodified\n")
            modified = subprocess.run(
                [sys.executable, str(VERIFY), str(mirror)], capture_output=True, text=True
            )
            self.assertNotEqual(modified.returncode, 0)

            readme.write_bytes(original)
            (mirror / "repository" / "unexpected.md").write_text("unexpected", encoding="utf-8")
            extra = subprocess.run(
                [sys.executable, str(VERIFY), str(mirror)], capture_output=True, text=True
            )
            self.assertNotEqual(extra.returncode, 0)


if __name__ == "__main__":
    unittest.main()
