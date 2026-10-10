# Refresh Agent Eco Space Understanding

Use this prompt when an existing agent or repository may have stale Agent Eco Space governance, adapters, manifest data, or central-context understanding. Replace every placeholder before sending it.

```text
Refresh this repository's Agent Eco Space understanding.

Agent Eco Space governance repository:
https://github.com/ikechukwukalu/agenteco

Product name:
<PRODUCT_NAME>

Application or component name:
<APPLICATION_OR_COMPONENT_NAME>

Repository name:
<REPOSITORY_NAME>

Repository URL or workspace path:
<REPOSITORY_URL_OR_WORKSPACE_PATH>

Central product context repository:
<CENTRAL_CONTEXT_REPOSITORY_URL_OR_WORKSPACE_PATH>

Optional governance version or revision expected:
<VERSION_COMMIT_OR_LATEST>

Optional work or context range to review:
<CURRENT_STATE_OR_COMMIT_PR_VERSION_RANGE>

Use the current specialist identity if it has already been explicitly established in this session; otherwise ask who you are operating as today.

Run the Repository Readiness Preflight. Verify the last approved full Agent Eco mirror in central context. When canonical Agent Eco is accessible, compare its VERSION and exact merged commit with the mirror; read a matching mirror rather than downloading unchanged governance. Without canonical access, state the mirror's recorded version and that freshness is unknown. Compare the applicable verified governance with the local manifest, AGENTS.md, CLAUDE.md, Copilot instructions, GEMINI.md, any recorded DeepSeek host-client instructions, and other installed Agent Eco files. Separately read the central product context relevant to this product, application or component, repository, its producers, and its consumers.

Verify both sources of understanding against the current repository and any accessible connected repositories. Do not assume that governance, adapters, central context, conversation memory, or implementation is current. Detect and report:
1. governance-version and inherited-rule changes;
2. missing, stale, accidentally edited, or conflicting instruction adapters;
3. manifest identity or configuration errors;
4. central-context records that are missing, stale, duplicated, or inconsistent;
5. implementation and contract drift between repositories and central context;
6. superseded decisions, business rules, and corrections that must remain in history;
7. access limitations and pending outbox packages;
8. authorization ambiguity, governance suspension or uncertainty, and implementation that may have proceeded without valid scope-bound approval.
9. missing, partial, stale, or materially outdated ecosystem-intake coverage and sibling-repository relationships;
10. missing or stale feature/API documentation-tool records and `CHANGELOG.md` status.

Classify each finding as a verified fact, drift, authorized repository-specific customization, unresolved conflict, or proposal. Preserve valid local instructions and history. Never allow a local adapter to weaken Agent Eco Space's non-negotiable safeguards.

If governance was disabled, superseded, contradictory, or uncertain, identify the exact affected period and changes. Do not treat restored governance as retroactive authorization. Enter Governance-Uncertain Mode, preserve incident history, restate the scope, and require a fresh standalone `Proceed with implementation.` command before further mutation.

Automatically repair proven canonical local adapter and manifest compliance differences under Instruction Adapter Integrity, and report them. Then present one reconciliation proposal identifying every remaining central-context file, repository document, branch, test, and pull request that should change. Do not make changes outside the automatic adapter-compliance exception until I send the standalone "Proceed with implementation." command.

After authorization, implement only the approved reconciliation. If canonical governance is newer, only an agent with approved canonical read and central-context write access may prepare the full-mirror refresh PR; never silently overwrite the approved copy. Create pull requests where appropriate but never merge them. After PR creation, remind the human of other relevant open context and code PRs. If the central context cannot be written, create a version-controlled Context Update Package in `.agenteco/outbox/context/` and report its pending status.
```

This refresh updates an agent's verified understanding; it does not authorize product-feature work, merge, deployment, publication, or production release.
