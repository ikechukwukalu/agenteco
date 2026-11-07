"""Check that Samuel's cross-platform FARS guidance stays complete and selective."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LIBRARY = "rules/fars-uiux-library.md"


class UiuxFarsLibraryTests(unittest.TestCase):
    def test_capabilities_keep_success_failure_avoidance_and_recovery(self):
        library = (ROOT / LIBRARY).read_text(encoding="utf-8")
        sections = re.findall(r"^## (.+)$", library, flags=re.MULTILINE)

        self.assertGreaterEqual(len(sections), 10)
        self.assertIn("Success-point and 2A journey clarity", sections)
        self.assertIn("Feedback, notifications, and operation state", sections)
        self.assertIn("Accessibility and inclusive understanding", sections)

        for section in library.split("\n## ")[1:]:
            heading = section.splitlines()[0]
            if heading == "Verification and continuity":
                continue
            self.assertIn("Success:", section, heading)
            self.assertIn(
                "| Failure or frustration | Candidate avoidance | Candidate recovery |",
                section,
                heading,
            )
            rows = [line for line in section.splitlines() if line.startswith("| ")]
            self.assertGreaterEqual(len(rows), 4, heading)
            for row in rows:
                self.assertEqual(row.count("|"), 4, f"Incomplete UI/UX FARS row in {heading}: {row}")

    def test_samuel_loads_library_without_making_it_global(self):
        builder = (ROOT / "tools/build_governance_snapshot.py").read_text(encoding="utf-8")
        samuel = (ROOT / "agents/samuel.uiux-lead.md").read_text(encoding="utf-8")
        core = builder.split("CORE = [", 1)[1].split("\n]", 1)[0]

        self.assertNotIn(LIBRARY, core)
        self.assertIn('if key == "samuel":', builder)
        self.assertIn(f'paths.append("{LIBRARY}")', builder)
        self.assertIn("UI/UX FARS capability library", samuel)

    def test_library_respects_evidence_and_review_approval(self):
        library = (ROOT / LIBRARY).read_text(encoding="utf-8")
        self.assertIn("when his review is approved", library)
        self.assertIn("Not yet scoreable", library)
        self.assertIn("product-specific risks", library)
        self.assertIn("2A actor/action", library)


if __name__ == "__main__":
    unittest.main()
