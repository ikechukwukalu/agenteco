# Tool Instruction Adapters

Every governed repository should contain thin instruction adapters for Codex, Claude, and GitHub Copilot. They point to the same canonical rules and product context rather than duplicating them.

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
10. recommend, but never automatically invoke, independent QA or another specialist.

The adapters must also recognize only commands listed in the canonical [Command Catalogue](../../commands/README.md) as protected workflow triggers.

Suggested locations are root `AGENTS.md` for Codex, root `CLAUDE.md` for Claude, and `.github/copilot-instructions.md` for GitHub Copilot.

Tool-specific syntax may differ, but behaviour and canonical sources remain consistent.
