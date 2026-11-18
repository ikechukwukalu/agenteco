# Optional Local-Only User-Level Loader

Install this **outside every company repository** only in a local agent surface that supports user-level instructions. It is a generic pointer, not a product registration. Replace the registry path with a company-approved local location. Do not put company identities, context content, or personal-account credentials in a user-level file that may sync to another machine or account without permission.

```text
At the start of a new local coding session, check whether the approved local Agent Eco registry exists at <ABSOLUTE_LOCAL_REGISTRY_PATH>. If it does not, do not activate Agent Eco. If it does, compare the current workspace's canonical Git remote and path with the registered project identity. Activate Local-Only Agent Eco Space only on an exact approved match, after verifying that the local context and governance source are readable and appropriate for this tool and audience. If the match, access, or instruction loading is uncertain, tell the human and use the manual Local-Only Startup Prompt or stop affected work.

In Local-Only Mode, never create or repair Agent Eco files inside the company project worktree. Keep context updates in the approved external local root, subject to ordinary implementation authorization, review, security, and retention rules. A local update is not shared or remotely synchronized. Never send company context to a personal or external destination unless the local registration records explicit approval.
```

This is a **candidate instruction**, not proof that a tool loads it. For example, Codex supports a user-level `AGENTS.md` in its Codex home, Claude Code supports user-level `CLAUDE.md`, and Copilot support depends on its client or harness. Verify the active tool's documented instruction location and inspect the current session's loaded instructions. Hosted GitHub reviews and cloud agents cannot be assumed to access this PC-only registry. The [manual startup prompt](call-agent-eco-space-local-only.md) is the portable fallback.

Official references: [Codex instruction discovery](https://developers.openai.com/cookbook/examples/gpt-5/codex_prompting_guide), [VS Code/Copilot instruction locations](https://code.visualstudio.com/docs/agents/reference/custom-instructions-reference), and [Copilot support by environment](https://docs.github.com/en/copilot/reference/custom-instructions-support).
