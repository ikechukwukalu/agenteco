# Agent Eco Space

Agent Eco Space is a lean, product-wide governance system for AI-assisted software delivery. It preserves AgentHQ's specialist expertise and engineering safeguards while removing mandatory orchestration, automatic multi-agent work, and repeated loading of irrelevant context.

## Operating model

1. A fresh session asks: **Who am I operating as today?**
2. The human selects one specialist. That role remains fixed for the session.
3. The specialist loads only shared rules, its repository context, and relevant cross-repository contracts.
4. The specialist owns implementation, engineer-written tests, documentation, changelog, and context updates.
5. The specialist may recommend an independent review, but never starts another specialist without human approval.
6. Specialists may create pull requests but must never merge them.

One specialist normally performs the work. Armstrong may be added as an independent QA specialist when the human approves it. Other specialists are invoked sequentially when their expertise is genuinely required.

## The central product brain

Each product has one central context repository covering every application, service, package, SDK, and infrastructure repository. It records product meaning, business rules and history, architecture, repository relationships, contracts, decisions, handoffs, risks, delivery evidence, and per-repository context.

Git repositories remain the authority for implemented code. When context and code disagree, the specialist reports and resolves **context drift** rather than guessing.

## Core documents

- [Operating Constitution](governance/operating-constitution.md)
- [Session and Role Selection](governance/session-and-role-selection.md)
- [Central Context Standard](governance/central-context-standard.md)
- [Delivery and Pull Request Governance](governance/delivery-and-pr-governance.md)
- [AgentHQ Inheritance Matrix](governance/agenthq-inheritance-matrix.md)
- [AgentHQ Transfer Ledger](governance/transfer-ledger.md)
- [Access-Degraded and Offline Mode](governance/access-degraded-mode.md)
- [Repository Readiness Preflight](governance/repository-readiness-preflight.md)
- [Instruction Adapter Integrity](governance/instruction-adapter-integrity.md)
- [Implementation Authorization Integrity](governance/implementation-authorization-integrity.md)
- [Governance Suspension and Recovery](governance/governance-suspension-and-recovery.md)
- [Specialist Catalogue](agents/README.md)
- [Product Context Template](templates/product-context/README.md)
- [Tool Instruction Adapters](templates/tool-instructions/README.md)

## Non-negotiable boundaries

- No hidden or automatic delegation.
- No specialist merges a pull request.
- No completion claim without proportionate tests and evidence.
- No silent divergence between implementation and shared context.
- No production release inferred from implementation approval.
- No invented business requirement, technical fact, or source authority.
- No repository mutation inferred from task wording, urgency, conversational momentum, prior approval, or absent objections.
- No silent fallback to ordinary implementation when governance is missing, disabled, contradictory, or uncertain.

Agent Eco Space is a sibling of AgentHQ, not a replacement. AgentHQ remains suitable for formally orchestrated delivery; Agent Eco Space is optimized for direct specialist execution, cross-repository continuity, and controlled cost.

## Licence and authorized use

Agent Eco Space is proprietary and confidential. It is not open-source software and is not licensed under MIT or another permissive licence. Access to this private repository does not itself grant permission to use, copy, modify, redistribute, publish, or commercialize its contents.

Use requires prior written authorization from Ikechukwu Kalu and is limited to the people, projects, purposes, and period covered by that authorization. See the [Proprietary and Confidential License](LICENSE.md).

## Commands

Commands that change Agent Eco Space state or enter a governed workflow must be sent as standalone messages.

### First-time bootstrap

A completely new AI session cannot understand the short commands until Agent Eco Space is discoverable. Start an unconfigured session with the [First-Time Bootstrap Prompt](templates/bootstrap-agent-eco-space.md). It identifies the Agent Eco Space repository, the product or current repository, and the central context repository when one exists.

After repository instruction adapters have been installed, the shorter commands below become reliable entry points.

### Adopt a product

```text
Adopt this product into Agent Eco Space.
```

Starts the Engineering Manager onboarding workflow for a new or existing product only after Agent Eco Space is discoverable in the current session. It authorizes discovery and an adoption proposal, not repository changes.

### Authorize implementation

```text
Proceed with implementation.
```

Authorizes implementation of the most recently presented, unchanged, approved scope. It does not authorize merge, deployment, publication, or production release.

It is single-use and scope-bound. A request to write, build, fix, or implement is not a substitute, and the absence of `Do not code yet` never grants permission.

### Suspend governance for one task

```text
Suspend Agent Eco Space governance for this task.
```

Deliberately suspends Agent Eco Space only for an already-established task. Similar wording, including generic statements that earlier instructions no longer apply, instead triggers Governance-Uncertain Mode. Suspension does not itself authorize merge, deployment, publication, destructive work, access expansion, or unrelated changes. Restored governance requires a new proposal and fresh `Proceed with implementation.` authorization.

### Add another repository

```text
Add this repository to Agent Eco Space.
```

Registers a repository with an existing governed product. In a new or ambiguous session, use the complete [Add Repository Prompt](templates/add-repository-to-agent-eco-space.md) so the AI knows the product, central context, and repository being added.

### Synchronize work from an existing session

```text
Synchronize this work with Agent Eco Space.
```

Backfills verified implementation and decision history from an existing code session into central context. Use the complete [Synchronization Prompt](templates/synchronize-existing-work.md) when the repositories and scope are not already established.

### Refresh Agent Eco Space understanding

```text
Refresh this repository's Agent Eco Space understanding.
```

Refreshes the agent's verified knowledge of current Agent Eco governance, installed adapters and manifest, central product context, and repository implementation. It reports drift and proposes reconciliation without changing anything until `Proceed with implementation.` is sent.

See the [Command Catalogue](commands/README.md) for exact meanings and preconditions.

## Copyable prompt library

The complete prompts are displayed here so a human can start or recover an Agent Eco Space session without searching through the repository. Replace every value enclosed in angle brackets before sending a prompt. The linked template files remain the canonical copies and must be updated together with this section.

### 1. First-time bootstrap prompt

Use this when a new AI session does not yet know what Agent Eco Space is or when the current repository has no working instruction adapters. Canonical template: [First-Time Bootstrap Prompt](templates/bootstrap-agent-eco-space.md).

```text
Use Agent Eco Space as the governance system for this work.

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
<CONTEXT_REPOSITORY_URL_OR_NONE_YET>

Read the Agent Eco Space README, command catalogue, operating constitution, specialist catalogue, and applicable rules. Then begin the "Adopt this product into Agent Eco Space." workflow.

Do not assume the repository is already configured. Run the canonical Repository Readiness Preflight first. Confirm what sources you can access, recommend the Engineering Manager for onboarding, ask who you are operating as today, inspect current product evidence, and present one combined adoption and remediation plan. Wait for the standalone "Proceed with implementation." command before creating approved changes. You may create pull requests after authorization, but you must never merge them.
```

### 2. Call Agent Eco Space prompt

Use this in a repository that is already governed by Agent Eco Space, or when you want the preflight to determine its actual readiness. Canonical template: [Call Agent Eco Space](templates/call-agent-eco-space.md).

```text
Use Agent Eco Space to govern this product and repository.

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

Read the canonical Agent Eco Space governance and run the Repository Readiness Preflight. Do not assume the repository, central context, manifest, or instruction adapters are present or current. Begin by asking who you are operating as today and present available roles unless I have already selected one.

After role selection, report the preflight outcome. If setup is incomplete, include adoption, registration, manifest, adapter, outbox, and context remediation in one proposal where applicable. Then load only the relevant context slice, verify it against repository evidence, identify drift, classify implementation, and require the standalone "Proceed with implementation." command. The selected specialist owns implementation, engineer-written tests, documentation, changelog, and affected context updates.

Do not invoke another specialist automatically. Recommend additional expertise only when it materially helps and wait for my approval. You may create pull requests on my behalf, but you must never merge them.
```

### 3. Add a repository prompt

Use this when a product is already governed and another repository must join its central context. Canonical template: [Add Repository to Agent Eco Space](templates/add-repository-to-agent-eco-space.md).

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

Do not modify any repository yet. Inspect the repository and classify its readiness as Ready, Partially Configured, Unconfigured, Access Degraded, or Blocked. Verify whether it is already registered and whether its manifest and adapters are current. Determine its type, purpose, audience, technology, runtime, visibility, current revision, owners, default specialist, operating profile, delivery mode, protected branches, deployment or publication lifecycle, and documentation state.

Identify the APIs, events, data, packages, authentication, queues, files, or other contracts it produces and consumes. Map every known relationship with existing product repositories. Compare its implementation with the existing central context and report duplication, conflicts, missing contracts, security or access concerns, and context drift.

Present a repository-registration proposal containing:
1. the proposed central-context repository record and destination directory;
2. repository-map and architecture changes;
3. contract, consumer, business-rule, decision, risk, roadmap, and handoff updates;
4. the proposed Codex, Claude, and Copilot instruction adapters for the new repository;
5. the temporary branches and pull requests required;
6. tests or verification required for any executable adapter or automation changes;
7. unresolved questions and access blockers.

Wait for the standalone "Proceed with implementation." command before creating approved changes. If central-context access is unavailable but the code repository is writable, create a version-controlled Context Update Package in `.agenteco/outbox/context/` after authorization. You may prepare pull requests, but you must never merge them.
```

### 4. Synchronize existing work prompt

Use this in an existing AI session when work has already been completed but has not been reliably recorded in the central context. Canonical template: [Synchronize Existing Work](templates/synchronize-existing-work.md).

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

Separate verified facts from reconstructed history, inference, and proposal. Preserve corrections and superseded decisions instead of rewriting history. Do not expose secrets, credentials, or production customer data.

Do not change the code implementation as part of this context-only operation unless I separately approve a new implementation scope. Present the backfill proposal and wait for the standalone "Proceed with implementation." command before changing the central context.

After authorization, update the context through a temporary branch and pull request. Never merge the pull request. If central-context access is unavailable, create a version-controlled Context Update Package in `.agenteco/outbox/context/` and clearly mark it `Pending Context Sync`.
```

### 5. Refresh Agent Eco Space understanding prompt

Use this when the agent's governance or product-context understanding may be outdated, or after Agent Eco Space, repository adapters, implementation, or central context has changed. Canonical template: [Refresh Understanding](templates/refresh-agent-eco-space-understanding.md).

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

Run the Repository Readiness Preflight. Read the latest accessible Agent Eco Space governance and compare it with the governance version, manifest, AGENTS.md, CLAUDE.md, Copilot instructions, and other Agent Eco files currently installed in this repository. Separately read the central product context relevant to this product, application or component, repository, its producers, and its consumers.

Verify both sources of understanding against the current repository and any accessible connected repositories. Do not assume that governance, adapters, central context, conversation memory, or implementation is current. Detect and report:
1. governance-version and inherited-rule changes;
2. missing, stale, accidentally edited, or conflicting instruction adapters;
3. manifest identity or configuration errors;
4. central-context records that are missing, stale, duplicated, or inconsistent;
5. implementation and contract drift between repositories and central context;
6. superseded decisions, business rules, and corrections that must remain in history;
7. access limitations and pending outbox packages;
8. authorization ambiguity, governance suspension or uncertainty, and implementation that may have proceeded without valid scope-bound approval.

Classify each finding as a verified fact, drift, authorized repository-specific customization, unresolved conflict, or proposal. Preserve valid local instructions and history. Never allow a local adapter to weaken Agent Eco Space's non-negotiable safeguards.

If governance was disabled, superseded, contradictory, or uncertain, identify the exact affected period and changes. Do not treat restored governance as retroactive authorization. Enter Governance-Uncertain Mode, preserve incident history, restate the scope, and require a fresh standalone `Proceed with implementation.` command before further mutation.

Present one reconciliation proposal identifying the exact governance adapters, manifest fields, central-context files, repository documentation, branches, tests, and pull requests that should change. Do not modify anything until I send the standalone "Proceed with implementation." command.

After authorization, implement only the approved reconciliation. Create pull requests where appropriate but never merge them. If the central context cannot be written, create a version-controlled Context Update Package in `.agenteco/outbox/context/` and report its pending status.
```

### 6. Context update package

This is the offline fallback used when a specialist must update central context but cannot write to that repository. It is stored in the codebase at `.agenteco/outbox/context/<package-identifier>.md`, committed for safekeeping, and removed only after the corresponding context pull request has been human-merged and verified. Canonical template: [Context Update Package](templates/context-update-package.md).

```text
# Context Update Package

## Identity

- Product:
- Application or component:
- Source repository name:
- Source repository:
- Selected specialist:
- Created at:
- Status: Pending Context Sync
- Package identifier:
- Content fingerprint:
- Version-controlled outbox path: .agenteco/outbox/context/<package-identifier>.md
- Source repository visibility and authorized audience:

## Available authority

- Agent Eco Space version or commit available:
- Central-context version or commit available:
- Canonical governance access: Available / Unavailable
- Remote context access: Read-write / Read-only / Unavailable

## Implementation evidence

- Work classification: Feature / Hotfix / Package / Other
- Branch:
- Commit or working-tree reference:
- Pull request, if available:
- Tests and verification:

## Proposed context updates

### Verified facts and implementation changes

### Business rules affected

### API, event, or data contracts affected

### Decisions created or superseded

### Repositories and consumers affected

### Documentation and release notes affected

## Intended central-context destinations

- Proposed files or directories:

## Risks and unresolved questions

## Sensitive-data handling

Confirm that this package contains no secret, credential, production customer data, or confidential content inappropriate for its storage or transfer location.

## Synchronization record

- Verified by:
- Context branch:
- Context commit:
- Context pull request:
- Online duplicate check: Not checked / Not found / Equivalent found / Reconciliation required
- Central synchronization-ledger entry:
- Human merge status:
- Final status: Pending Context Sync / Submitted / Synchronized / Rejected
- Remote merge verified by:
- Remote merge commit:
- Codebase outbox removal PR:
- Live outbox removal: Pending / Completed
```
