"""Protect validation comparisons and unresolved API-impact follow-through."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(relative_path):
    return (ROOT / relative_path).read_text(encoding="utf-8")


class ApiImpactFollowupTests(unittest.TestCase):
    def test_form_validation_comparison_is_recorded(self):
        policy = read("rules/api-consumer-compatibility.md")
        template = read("templates/product-context/api-consumer-compatibility.md")

        self.assertIn("## Form-to-API validation comparison", policy)
        self.assertIn("## Form-to-API validation comparison", template)
        for detail in (
            "current backend validation contract",
            "conditionally required fields",
            "server rejects a value",
            "producer and consumer revisions",
            "backend validation remains authoritative",
        ):
            self.assertIn(detail.lower(), policy.lower())
        self.assertIn("Gap open", template)
        self.assertIn("Linked alert", template)

    def test_alert_remains_open_until_all_consumers_are_verified(self):
        policy = read("rules/api-consumer-compatibility.md")
        template = read("templates/product-context/api-consumer-compatibility.md")

        self.assertIn("At **each task preflight", policy)
        self.assertIn("PR handoff", policy)
        self.assertIn("release-readiness check", policy)
        self.assertIn("**every** affected consumer", policy)
        self.assertIn("does **not** assert compatibility or remove the alert", policy)
        self.assertIn("human-reviewed context PR", policy)
        self.assertIn("Open with exception", template)

    def test_producer_and_consumers_own_the_followup(self):
        chinedu = read("agents/chinedu.backend-architect.md")
        dotun = read("agents/dotun.frontend-architect.md")
        joseph = read("agents/joseph.mobile-architect.md")

        self.assertIn("form-to-API comparison", chinedu)
        self.assertIn("form-to-API connection", dotun)
        self.assertIn("mobile input flows", joseph)
        for role in (chinedu, dotun, joseph):
            self.assertIn("release checks", role)


if __name__ == "__main__":
    unittest.main()
