"""Keep the FARS library and scoring contract complete across documentation edits."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class FarsGovernanceTests(unittest.TestCase):
    def test_capability_rows_have_failure_avoidance_and_recovery(self):
        library = (ROOT / "rules/fars-mobile-web-library.md").read_text(encoding="utf-8")
        sections = re.findall(r"^## (.+)$", library, flags=re.MULTILINE)

        # A broad reusable library must cover more than one example journey.
        self.assertGreaterEqual(len(sections), 10)
        self.assertIn("Forms and multi-step journeys", sections)
        self.assertIn("Tables, lists, and row actions", sections)
        self.assertIn("Notifications, alerts, and progress", sections)

        for section in library.split("\n## ")[1:]:
            if section.startswith("Source standards"):
                continue
            heading = section.splitlines()[0]
            self.assertIn("Success:", section, heading)
            self.assertIn("| Failure or frustration | Candidate avoidance | Candidate recovery |", section, heading)
            rows = [line for line in section.splitlines() if line.startswith("| ")]
            self.assertGreaterEqual(len(rows), 4, heading)
            for row in rows:
                self.assertEqual(row.count("|"), 4, f"Incomplete FARS row in {heading}: {row}")

    def test_score_has_hundred_points_and_no_unearned_claim(self):
        scoring = (ROOT / "rules/fars-usability-scoring.md").read_text(encoding="utf-8")
        points = [int(value) for value in re.findall(r"^\| [^|]+ \| (\d+) \|", scoring, re.MULTILINE)]

        self.assertEqual(sum(points), 100)
        self.assertIn("Not yet scoreable", scoring)
        self.assertIn("not an industry-wide numeric standard", scoring)
        self.assertIn("before", scoring)
        self.assertIn("after", scoring)


if __name__ == "__main__":
    unittest.main()
