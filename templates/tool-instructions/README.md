# Tool Instruction Adapters

Every governed repository should contain thin instruction adapters for the AI tools approved for that repository. Codex, Claude, GitHub Copilot, and Gemini have defined repository adapters. DeepSeek support is resolved through its host coding client because DeepSeek is a model provider, not one universal workspace application. All adapters point to the same canonical rules and product context rather than duplicating them.

Each adapter requires the AI to:

1. identify Agent Eco Space as the governing system;
2. run the Repository Readiness Preflight without assuming setup is complete;
3. ask **Who am I operating as today?** unless the role is explicit;
4. lock the selected role for the session;
5. load compact governance and the relevant context slice;
6. confirm feature or hotfix before branching;
7. follow the branch and pull-request rules;
8. implement tests and synchronize documentation and context;
9. never merge a pull request;
10. require a recorded human decision on Armstrong's independent QA after testable implementation and before creating implementation PRs, while never invoking Armstrong automatically;
11. never infer implementation authorization from task wording, urgency, prior approval, conversation flow, or absent objections;
12. enter Governance-Uncertain Mode rather than silently falling back when governance is missing, disabled, superseded, contradictory, inaccessible, or uncertain.
13. complete one recorded ecosystem intake, then use a fast repository-scoped path on later tasks;
14. always refresh active business rules and decisions;
15. request human approval before a periodic full ecosystem refresh and keep the reminder non-blocking when scoped work is safe;
16. identify and maintain actual feature/API documentation tooling and `CHANGELOG.md`;
17. write context updates for detailed cross-agent continuity.
18. verify and automatically reconcile the complete manifest-required adapter set, restoring another tool's deleted adapter even when it is not the active tool;
19. treat Agent Eco Space itself as read-only except for a request verified through GitHub as coming from repository owner `ikechukwukalu`, followed by the normal proposal and authorization gate.
20. check relevant API–consumer mappings and alerts, initialize the backend baseline when assigned, and record new consumer usage or breaking producer impact with source and revision evidence.
21. treat `.env` and every `.env.*` file except exact `.env.example` as value-confidential, never disclose those values, and allow only explicitly authorized non-disclosing secret insertion.

The adapters must also recognize only commands listed in the canonical [Command Catalogue](../../commands/README.md) as protected workflow triggers.

Defined locations are root `AGENTS.md` for Codex, root `CLAUDE.md` for Claude, `.github/copilot-instructions.md` for GitHub Copilot, and root `GEMINI.md` for Gemini CLI.

For DeepSeek, first identify the host client. If that client natively loads one of the governed adapters, reuse it and record the client and path in `.agenteco/manifest.yml`. Otherwise use the [DeepSeek Bootstrap](deepseek-bootstrap.md) at session start and record the adapter as `manual-bootstrap`. Never create or trust a fictional universal `DEEPSEEK.md` auto-discovery contract.

| AI model or tool | Agent Eco mechanism | Discovery classification |
|---|---|---|
| Codex | Root `AGENTS.md` | Native when supported by the active Codex surface |
| Claude | Root `CLAUDE.md` | Native when supported by the active Claude surface |
| GitHub Copilot | `.github/copilot-instructions.md` | Native GitHub Copilot repository instructions |
| Gemini CLI | Root `GEMINI.md` | Native hierarchical Gemini context |
| DeepSeek | Host-client adapter or portable bootstrap prompt | Client-managed or manual until verified |

Tool-specific syntax may differ, but behaviour and canonical sources remain consistent.

## Integrity and human edits

Each adapter separates its canonical and repository-specific content using the managed markers defined in [Instruction Adapter Integrity](../../governance/instruction-adapter-integrity.md). The readiness preflight compares recorded template versions and fingerprints, preserves valid local instructions, and reports accidental or conflicting edits instead of silently overwriting them.

Repositories may install the dependency-free [adapter integrity checker](../check-agenteco-adapters.py) in CI. It detects total adapter loss, malformed managed sections, and fingerprint drift but never repairs or commits; a surviving governed agent or a human-started bootstrap performs remediation.
