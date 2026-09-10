# Agent Eco Space

This repository uses Agent Eco Space as its canonical AI governance system.

Begin each fresh session by loading the canonical rules and relevant central product context. Ask **Who am I operating as today?** unless the user already selected a specialist, then keep that identity fixed.

Use selective context, verify cross-repository facts, report context drift, clarify feature versus hotfix before branching, and keep code, tests, documentation, changelog, and context synchronized. Require the standalone `Proceed with implementation.` command before changing repositories.

The standalone `Adopt this product into Agent Eco Space.` command begins product onboarding and discovery, not implementation.

Additional specialists require human approval. Pull requests may be created but never merged by the AI specialist.

If canonical governance or central context is inaccessible, disclose it, apply Access-Degraded Mode, and create a Context Update Package rather than claiming synchronization.

Check `.agenteco/outbox/context/` after role selection. Offer to synchronize pending packages when access exists, and delete them only after verified human merge.
