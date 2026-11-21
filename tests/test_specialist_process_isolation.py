"""Protect genuine host-independent specialist-process isolation across canonical governance and adapters."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ADAPTERS = (
    "templates/tool-instructions/AGENTS.md",
    "templates/tool-instructions/CLAUDE.md",
    "templates/tool-instructions/copilot-instructions.md",
    "templates/tool-instructions/GEMINI.md",
    "templates/tool-instructions/deepseek-bootstrap.md",
)


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class SpecialistProcessIsolationTests(unittest.TestCase):
    def test_constitution_requires_distinct_task_and_fresh_context(self):
        content = read("governance/operating-constitution.md")
        self.assertIn("## Specialist process isolation (mandatory)", content)
        for phrase in (
            "equivalent isolated agent executions",
            "no inherited implementing-agent tool history",
            "Explicit specialist brief",
            "verifiable execution reference",
            "automatic/default or balanced routing",
            "same-session \"Armstrong PASS\"",
            "report the review or handoff as blocked and stop",
        ):
            self.assertIn(phrase.lower(), content.lower())

    def test_capp_requires_actual_armstrong_subagent_before_pr(self):
        delivery = read("governance/delivery-and-pr-governance.md")
        self.assertIn("Under CAPP, the implementing specialist MUST invoke Armstrong", delivery)
        self.assertIn("verifiable independent execution reference", delivery)
        self.assertIn("Inline role-play is not Armstrong QA", delivery)
        self.assertIn("stop the PR handoff under CAPP", delivery)
        self.assertIn("never merge", delivery.lower())

    def test_managed_adapters_carry_exact_process_boundary(self):
        for path in ADAPTERS:
            with self.subTest(adapter=path):
                content = read(path)
                self.assertIn("### Mandatory specialist process isolation", content)
                self.assertIn("separate host-native Task/subagent", content)
                self.assertIn("must not inherit", content)
                self.assertIn("automatic/default or balanced model routing", content)
                self.assertIn("actual independent execution verdict before implementation PR creation", content)
                self.assertIn("same-session \"Armstrong PASS\" is invalid", content)
                self.assertIn("report blocked and stop", content)

    def test_samuel_fars_scores_are_independent(self):
        content = read("rules/fars-usability-scoring.md")
        self.assertIn("### Independent Samuel process", content)
        self.assertIn("provisional or verified score", content)
        self.assertIn("`Not yet scoreable`", content)
        self.assertIn("Same-chat Samuel impersonation", content)
        self.assertIn("report blocked and stop", content)

    def test_evidence_and_versioning(self):
        evidence = read("rules/output-format.md")
        global_rules = read("rules/global-engineering-rules.md")
        self.assertIn("## Independent specialist review evidence", evidence)
        self.assertIn("Missing subagent evidence is a blocked review", evidence)
        self.assertIn("60. Enforce [mandatory specialist process isolation]", global_rules)
        self.assertEqual("0.10.2", read("VERSION").strip())
        self.assertIn("host-neutral independent specialist process isolation", read("CHANGELOG.md"))


if __name__ == "__main__":
    unittest.main()
