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

    def test_low_sections_and_accepted_risk_remain_visible(self):
        scoring = (ROOT / "rules/fars-usability-scoring.md").read_text(encoding="utf-8")
        context = (ROOT / "templates/product-context/feature-paths-and-recovery.md").read_text(
            encoding="utf-8"
        )

        self.assertIn("lowest assessed section score", scoring)
        self.assertIn("every", scoring)
        self.assertIn("sub-90", scoring)
        self.assertIn("diagnostic QA", scoring)
        self.assertIn("not production approval", scoring)
        self.assertIn("lowest assessed section score", context)
        self.assertIn("all sections below 90", context)
        self.assertIn("Reassessment date", context)

    def test_pr_evidence_and_contract_changes_are_explicit(self):
        handoff = (ROOT / "governance/delivery-and-pr-governance.md").read_text(encoding="utf-8")
        template = (ROOT / "templates/fars-pr-evidence.md").read_text(encoding="utf-8")
        library = (ROOT / "rules/fars-mobile-web-library.md").read_text(encoding="utf-8")

        self.assertIn("FARS evidence section", handoff)
        self.assertIn("Failure ID", template)
        self.assertIn("Implemented avoidance", template)
        self.assertIn("Implemented recovery", template)
        self.assertIn("Third-party SDK or API upgrade", library)
        self.assertIn("Backend request fields", library)


if __name__ == "__main__":
    unittest.main()
