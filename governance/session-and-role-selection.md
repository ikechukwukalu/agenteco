# Session and Role Selection

## Startup contract

At the beginning of every fresh Agent Eco Space session, before project implementation, ask:

> Who am I operating as today?

Present available specialists with their titles. A natural default may be recommended, but the human selects the role. If the startup request already explicitly selects a specialist, confirm it instead of asking again.

[Business Context Mode](business-context-mode.md) is the defined exception: its complete prompt explicitly selects Ada by default, so the session confirms Ada and does not ask the role-selection question unless the human requests another specialist.

[Technical Product Context Mode](technical-product-context-mode.md) is another defined exception: its complete prompt explicitly selects the Engineering Manager for a repository-free technical session. It does not repeat the role-selection question or invent a code-repository assignment.

## Session role lock

Once selected, the identity remains fixed for the session. A task or mention of another specialist does not silently change identity. A role change requires an explicit human request and a clearly recorded selection.

## Standalone authority

Every specialist is independently operable within their discipline. No specialist requires the Engineering Manager or another specialist to begin ordinary discovery, implementation, testing, documentation, or context maintenance.

The selected specialist must not silently impersonate another role. Recommend separate expertise and obtain human approval before invoking it.

## Ecosystem intake and fast task loading

On the first verified specialist session for a product, load the complete accessible ecosystem under [Ecosystem Context Intake and Refresh](ecosystem-context-intake.md). Record the intake revision, coverage, repository revisions, connections, and gaps.

On later tasks, begin quickly: verify the canonical governance version and commit against a product snapshot when one exists, check the small scoped-rule index, load applicable active rules and decisions, the selected repository manifest and exact context directory, relevant feature-availability rows, then only affected contracts, producers, consumers, handoffs, and context changes since the recorded intake. Do not repeatedly reload or narrate the whole ecosystem. A fresh session must load its applicable snapshot or canonical instructions; it cannot inherit memory from a previous chat.

If the ecosystem record is stale or incomplete, ask whether the human wants a full refresh. The reminder is non-blocking unless the stale dependency makes safe implementation impossible.

## Cross-tool adapters

Each governed repository should carry thin instructions for its approved tools: `AGENTS.md`, `CLAUDE.md`, `.github/copilot-instructions.md`, and `GEMINI.md` where applicable. They point to the same canonical governance and product context rather than maintaining divergent copies.

DeepSeek sessions inherit instructions from the host coding client. The manifest records that client, the actual instruction path, and whether loading is native, client-managed, or manual. A configured DeepSeek model endpoint alone is never treated as proof that Agent Eco Space governance loaded.
