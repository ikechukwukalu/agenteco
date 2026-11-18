"""Keep the explicit CAPP shortcut consistent across governed entry points."""

import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class CappCommandTests(unittest.TestCase):
    def test_command_is_standalone_and_scope_bound(self):
        commands = read("commands/README.md")
        authorization = read("governance/implementation-authorization-integrity.md")

        self.assertIn("```text\nCAPP\n```", commands)
        self.assertIn("**C**opilot review, **A**rmstrong review, **P**Rs presented, **P**roceed", commands)
        self.assertIn("entire standalone message", commands)
        self.assertIn("most recently presented, unchanged scope", commands)
        self.assertIn("does not authorize a merge", authorization)

    def test_review_and_pr_handoff_are_not_claimed_without_evidence(self):
        delivery = read("governance/delivery-and-pr-governance.md")
        constitution = read("governance/operating-constitution.md")

        self.assertIn("standalone `CAPP`", delivery)
        self.assertIn("His review must actually occur", delivery)
        self.assertIn("Armstrong reports the applicable evidence and limits", constitution)
        self.assertIn("Awaiting Copilot", delivery)
        self.assertIn("never merge", delivery.lower())

    def test_all_native_adapters_recognize_the_shortcut(self):
        adapters = [
            "templates/tool-instructions/AGENTS.md",
            "templates/tool-instructions/CLAUDE.md",
            "templates/tool-instructions/copilot-instructions.md",
            "templates/tool-instructions/GEMINI.md",
            "templates/tool-instructions/deepseek-bootstrap.md",
        ]

        for adapter in adapters:
            with self.subTest(adapter=adapter):
                content = read(adapter)
                self.assertIn("standalone `Proceed with implementation.` or `CAPP`", content)
                self.assertIn("both Ps are deliberate", content)
                self.assertIn("even documentation-only work", content)


if __name__ == "__main__":
    unittest.main()
