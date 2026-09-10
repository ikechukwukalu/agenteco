# Agent Eco Space repository instructions

Follow the canonical Agent Eco Space governance and this product's central context.

At the first project interaction, run the Repository Readiness Preflight and never assume registration, manifest, adapters, outbox, or central context are current. Ask **Who am I operating as today?** unless the role is explicit. Keep the selected specialist identity for the session.

Load only relevant business rules, repository context, contracts, and decisions. Verify implementation facts in connected repositories and report drift. Confirm feature versus hotfix before branching. Require the standalone `Proceed with implementation.` command before repository changes. The implementer owns tests, documentation, changelog, and context updates.

The standalone `Adopt this product into Agent Eco Space.` command begins product onboarding and discovery, not implementation.

Never start another specialist automatically and never merge a pull request.

If canonical governance or central context is inaccessible, disclose it, apply Access-Degraded Mode, and create a Context Update Package rather than claiming synchronization.

Check the version-controlled `.agenteco/outbox/context/` after role selection. Offer to synchronize pending packages when access exists, and remove them through codebase PRs only after verified human merge.
