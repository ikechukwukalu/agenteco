"""Keep resource-efficient Cursor subagents mandatory across governed entry points."""

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADAPTERS = [
    "AGENTS.md", "CLAUDE.md", "GEMINI.md",
    "copilot-instructions.md", "deepseek-bootstrap.md",
]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class ResourceEfficiencyTests(unittest.TestCase):
    def test_canonical_safeguards(self):
        rule = read("governance/subagent-model-and-resource-efficiency.md")
        for term in (
            "Auto", "Balance", "model: inherit",
            "Inheritance is not Auto routing", "smallest relevant context",
            "MUST NOT weaken", "same-chat role-play", "LOCAL",
        ):
            with self.subTest(term=term):
                self.assertIn(term, rule)

    def test_all_managed_adapters(self):
        for adapter in ADAPTERS:
            with self.subTest(adapter=adapter):
                content = read("templates/tool-instructions/" + adapter)
                for term in (
                    "### Mandatory subagent model and resource efficiency",
                    "model: inherit", "Auto with Balance optimization",
                    "does not guarantee Auto routing",
                    "Preserve independent Armstrong/Samuel review",
                    "report blocked and stop",
                ):
                    self.assertIn(term, content)

    def test_governance_version_and_entry(self):
        self.assertIn("Subagent Model and Resource Efficiency", read("governance/operating-constitution.md"))
        self.assertIn("60. Follow mandatory [Subagent Model and Resource Efficiency]", read("rules/global-engineering-rules.md"))
        self.assertIn("mandatory canonical Subagent Model and Resource Efficiency", read("templates/call-agent-eco-space.md"))
        self.assertEqual("0.10.3", read("VERSION").strip())
        self.assertIn("Mandated provider-neutral Cursor subagent resource efficiency", read("CHANGELOG.md"))


if __name__ == "__main__":
    unittest.main()
