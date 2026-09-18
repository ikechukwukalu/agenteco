# Synchronize Existing Work with Agent Eco Space

Use this prompt in an existing AI session that already understands work completed in a codebase but has not yet recorded that work in the product's central context.

Replace the placeholders before sending it.

```text
Synchronize this work with Agent Eco Space.

Agent Eco Space governance repository:
https://github.com/ikechukwukalu/agenteco

Product name:
<PRODUCT_NAME>

Application or component name:
<APPLICATION_OR_COMPONENT_NAME>

Repository name:
<CURRENT_REPOSITORY_NAME>

Repository URL or workspace path:
<CURRENT_REPOSITORY_URL_OR_WORKSPACE_PATH>

Central product context repository:
<CENTRAL_CONTEXT_REPOSITORY_URL_OR_WORKSPACE_PATH>

Work to reconcile:
<CURRENT_SESSION_OR_OPTIONAL_COMMIT_PR_VERSION_RANGE>

Use the current specialist identity if it has already been explicitly established in this session; otherwise ask who you are operating as today.

Read the canonical Agent Eco Space governance and run the Repository Readiness Preflight. Do not assume registration, manifest, adapters, outbox, or central-context structure already exist. Confirm which sources you can access. Do not rely on conversation memory alone: inspect the current repository, working tree, commits, pull requests, tests, documentation, configuration, and other available evidence to verify what was actually implemented.

Compare the verified implementation with the central context. Search for existing records by repository, commit, pull request, feature, contract, decision, and context-update identifier so the same work is not duplicated.

If setup is incomplete, prepare one combined repository-adoption, adapter-bootstrap, and context-backfill proposal. It identifies:
1. the repository state and evidence reviewed;
2. features, fixes, behaviour, and operational changes completed;
3. business rules implemented, changed, corrected, deprecated, or still uncertain;
4. APIs, events, payloads, data models, queues, files, packages, authentication, permissions, and other contracts affected;
5. architecture and decisions, including superseded directions and reasons;
6. tests, CI, documentation, changelog, release, deployment, and known-risk state;
7. affected repositories, consumers, owners, and required handoffs;
8. exact central-context files to create or update;
9. context drift, missing evidence, conflicts, and unresolved questions;
10. the proposed code and context branches and pull requests;
11. missing or stale manifest, adapters, tracked outbox, registration, and per-repository context.
12. feature/API documentation and `CHANGELOG.md` changes or omissions;
13. sibling-repository implications and continuity details needed by the next specialist.

Separate verified facts from reconstructed history, inference, and proposal. Preserve corrections and superseded decisions instead of rewriting history. Do not expose secrets, credentials, or production customer data.

Do not change the code implementation as part of this context-only operation unless I separately approve a new implementation scope. Present the backfill proposal and wait for the standalone "Proceed with implementation." command before changing the central context.

After authorization, update the context through a temporary branch and pull request. Never merge the pull request. If central-context access is unavailable, create a version-controlled Context Update Package in `.agenteco/outbox/context/` and clearly mark it `Pending Context Sync`.
```

After the context PR is human-merged and verified, the work becomes synchronized. A created PR alone means `Submitted`, not `Synchronized`.
