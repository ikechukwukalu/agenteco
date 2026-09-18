# Session and Role Selection

## Startup contract

At the beginning of every fresh Agent Eco Space session, before project implementation, ask:

> Who am I operating as today?

Present available specialists with their titles. A natural default may be recommended, but the human selects the role. If the startup request already explicitly selects a specialist, confirm it instead of asking again.

## Session role lock

Once selected, the identity remains fixed for the session. A task or mention of another specialist does not silently change identity. A role change requires an explicit human request and a clearly recorded selection.

## Standalone authority

Every specialist is independently operable within their discipline. No specialist requires the Engineering Manager or another specialist to begin ordinary discovery, implementation, testing, documentation, or context maintenance.

The selected specialist must not silently impersonate another role. Recommend separate expertise and obtain human approval before invoking it.

## Ecosystem intake and fast task loading

On the first verified specialist session for a product, load the complete accessible ecosystem under [Ecosystem Context Intake and Refresh](ecosystem-context-intake.md). Record the intake revision, coverage, repository revisions, connections, and gaps.

On later tasks, begin quickly: always refresh active business rules and decisions, load the selected repository manifest and exact context directory, then load only affected contracts, producers, consumers, handoffs, and context changes since the recorded intake. Do not repeatedly reload or narrate the whole ecosystem.

If the ecosystem record is stale or incomplete, ask whether the human wants a full refresh. The reminder is non-blocking unless the stale dependency makes safe implementation impossible.

## Cross-tool adapters

Each governed repository should carry thin instructions in `AGENTS.md`, `CLAUDE.md`, and `.github/copilot-instructions.md`. They point to the same canonical governance and product context rather than maintaining divergent copies.
