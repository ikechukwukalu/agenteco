"""Keep Local-Only Mode separate from tracked repository adoption."""

import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


class LocalOnlyModeTests(unittest.TestCase):
    def test_mode_never_requires_project_git_files_or_personal_sync(self):
        policy = read("governance/local-only-mode.md")
        registration = read("templates/local-only-registration.yml")
        registry = read("templates/local-only-project-registry.yml")

        self.assertIn("outside the project worktree", policy)
        self.assertIn("does not wish to commit Agent Eco adapters", policy)
        self.assertIn("personal account or personal remote copy", policy)
        self.assertIn("Never say it is", policy)
        self.assertIn("enabled: false", registration)
        self.assertIn("destination: null", registration)
        self.assertIn("<COMPANY_OR_APPROVED_OWNER>", registration)
        self.assertIn("enabled: false", registry)
        self.assertIn("registration_path:", registry)

    def test_manual_prompt_is_complete_and_mirrored_in_readme(self):
        template = read("templates/call-agent-eco-space-local-only.md")
        readme = read("README.md")
        prompt = re.search(r"```text\n(.*?)\n```", template, re.DOTALL)

        self.assertIsNotNone(prompt)
        self.assertIn(prompt.group(1), readme)
        self.assertIn("<ABSOLUTE_APPROVED_CONTEXT_PATH>", prompt.group(1))
        self.assertIn('standalone "Proceed with implementation."', prompt.group(1))
        self.assertIn("Do not create, edit, restore, stage, or commit", prompt.group(1))

    def test_preflight_and_auto_repair_have_local_only_exception(self):
        self.assertIn("local-only-mode.md", read("governance/repository-readiness-preflight.md"))
        self.assertIn("local-only-mode.md", read("governance/instruction-adapter-integrity.md"))
        self.assertIn("local-only-mode.md", read("governance/access-degraded-mode.md"))
        self.assertIn('"governance/local-only-mode.md"', read("tools/build_governance_snapshot.py"))

    def test_optional_loader_never_claims_cloud_or_personal_access(self):
        loader = read("templates/local-only-user-loader.md")
        self.assertIn("<ABSOLUTE_LOCAL_REGISTRY_PATH>", loader)
        self.assertIn("exact approved match", loader)
        self.assertIn("do not activate Agent Eco", loader)
        self.assertIn("Hosted GitHub reviews and cloud agents cannot be assumed", loader)

    def test_document_links_resolve(self):
        paths = [
            "governance/local-only-mode.md",
            "templates/call-agent-eco-space-local-only.md",
            "commands/README.md",
            "templates/local-only-user-loader.md",
            "templates/local-only-project-registry.yml",
        ]
        for path in paths:
            source = ROOT / path
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", source.read_text(encoding="utf-8")):
                if "://" in target or target.startswith("#"):
                    continue
                with self.subTest(source=path, target=target):
                    self.assertTrue((source.parent / target.split("#", 1)[0]).exists())


if __name__ == "__main__":
    unittest.main()
