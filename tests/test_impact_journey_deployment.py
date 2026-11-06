"""Keep the new governance handoffs discoverable and internally consistent."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ImpactJourneyDeploymentTests(unittest.TestCase):
    def read(self, path):
        return (ROOT / path).read_text(encoding="utf-8")

    def test_snapshot_loads_impact_and_journey_rules(self):
        builder = self.read("tools/build_governance_snapshot.py")
        self.assertIn('"governance/review-applicability.md"', builder)
        self.assertIn('"rules/journey-actions-and-customer-feedback.md"', builder)

    def test_journey_template_records_actions_and_conditional_requirements(self):
        template = self.read("templates/product-context/feature-paths-and-recovery.md")
        self.assertIn("Visible primary next action", template)
        self.assertIn("Conditional", template)

    def test_copilot_review_requires_follow_through(self):
        delivery = self.read("governance/delivery-and-pr-governance.md")
        self.assertIn("Awaiting Copilot", delivery)
        self.assertIn("request a fresh Copilot review", delivery)
        self.assertIn("pending review", delivery)

    def test_deployment_registration_is_product_scoped(self):
        registration = json.loads(self.read("templates/product-context/production-reconciliation-registration.json"))
        self.assertEqual(registration["schema_version"], 2)
        self.assertEqual(registration["central_context_repository"], "<OWNER/REPOSITORY>")
        self.assertEqual(
            registration["credentials"],
            {
                "source_dispatch_secret_name": "CPI_DISPATCH_TOKEN",
                "central_assignment_secret_name": "CPI_COPILOT_TOKEN",
                "central_source_read_secret_name": "CPI_SOURCE_READ_TOKEN",
            },
        )
        evidence = registration["source_repositories"][0]["production_deployment_evidence"]
        self.assertEqual(evidence["status"], "unconfigured")
        self.assertIn("workflow_identity", evidence)
        self.assertIn("deployed_revision_source", evidence)
        policy = self.read("governance/production-context-reconciliation.md")
        self.assertIn("do not infer the deployed SHA", policy)
        self.assertIn("human reviews and merges", policy)


if __name__ == "__main__":
    unittest.main()
