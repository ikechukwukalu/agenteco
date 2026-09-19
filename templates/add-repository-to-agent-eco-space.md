# Add a Repository to Agent Eco Space

Use this prompt when a product is already governed by Agent Eco Space and another repository must join the same central product context.

Replace the placeholders before sending it.

```text
Add this repository to Agent Eco Space.

Agent Eco Space governance repository:
https://github.com/ikechukwukalu/agenteco

Existing product name:
<PRODUCT_NAME>

Application or component name:
<APPLICATION_OR_COMPONENT_NAME>

Central product context repository:
<CENTRAL_CONTEXT_REPOSITORY_URL_OR_WORKSPACE_PATH>

Repository name:
<NEW_REPOSITORY_NAME>

Repository URL or workspace path:
<NEW_REPOSITORY_URL_OR_WORKSPACE_PATH>

Known purpose, if any:
<OPTIONAL_HUMAN_DESCRIPTION>

Read the canonical Agent Eco Space governance and run the Repository Readiness Preflight. Do not assume the repository is unregistered or configured correctly. Confirm which sources you can access. Ask who you are operating as today and recommend the Engineering Manager for repository registration, but let me choose the specialist.

Do not modify any repository yet. Inspect the repository and classify its readiness as Ready, Partially Configured, Unconfigured, Access Degraded, or Blocked. Verify whether it is already registered and whether its manifest and adapters are current. Determine its type, purpose, audience, technology, runtime, visibility, current revision, owners, default specialist, operating profile, delivery mode, protected branches, deployment or publication lifecycle, feature/API documentation tooling, and `CHANGELOG.md` state.

Identify the APIs, events, data, packages, authentication, queues, files, or other contracts it produces and consumes. Map every known relationship with existing product repositories. Compare its implementation with the existing central context and report duplication, conflicts, missing contracts, security or access concerns, and context drift.

Treat registration as a material ecosystem change. Mark the complete ecosystem intake for refresh and include the new repository, its verified revision, relationships, documentation system, and any coverage gaps in that proposal.

Present a repository-registration proposal containing:
1. the proposed central-context repository record and destination directory;
2. repository-map and architecture changes;
3. contract, consumer, business-rule, decision, risk, roadmap, and handoff updates;
4. the proposed Codex, Claude, Copilot, and Gemini instruction adapters for the new repository, plus the verified DeepSeek host-client or manual-bootstrap configuration when DeepSeek is used;
5. the temporary branches and pull requests required;
6. tests or verification required for any executable adapter or automation changes;
7. unresolved questions and access blockers.

Wait for the standalone "Proceed with implementation." command before creating approved changes. If central-context access is unavailable but the code repository is writable, create a version-controlled Context Update Package in `.agenteco/outbox/context/` after authorization. You may prepare pull requests, but you must never merge them.
```

This prompt registers one repository with an existing product. Use the first-time bootstrap prompt when Agent Eco Space itself is not yet known to the session, and use the product-adoption prompt when the product does not yet have a central context.
