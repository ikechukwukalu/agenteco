# Agent Eco Space Command Catalogue

This catalogue documents commands that trigger a defined Agent Eco Space workflow or state transition. Commands are deliberately short, visible, and unambiguous.

## Bootstrap versus command

The [First-Time Bootstrap Prompt](../templates/bootstrap-agent-eco-space.md) is required when a session has no repository instruction pointing to Agent Eco Space. It supplies the governance location and product scope. The commands below are shortcuts used after that bootstrap or after instruction adapters are installed.

## Command rules

- Send a command as a standalone message, without commentary or additional scope.
- A command applies only to the currently established scope and repository context.
- Quoting a command in documentation or conversation does not execute it.
- Similar wording does not trigger a protected state transition.
- No command authorizes a specialist to merge a pull request.
- Every entry command runs the canonical Repository Readiness Preflight before assuming setup exists.
- Repository-based complete prompts identify the product, application or component, repository name and location, and central-context location; a repository URL alone is not a complete product identity. The Business Context Mode prompt intentionally identifies only governance, product, central context, and the business objective because no code repository is assigned.

## Adopt a product

```text
Adopt this product into Agent Eco Space.
```

**Purpose:** Begin onboarding an existing or new product.

**Discovery precondition:** The session has loaded Agent Eco Space through the first-time bootstrap prompt or a repository instruction adapter. Otherwise, the AI must request the governance location rather than pretending to recognize the command.

**Selected role:** Engineering Manager is recommended and may be selected for the onboarding session.

**Effect:** Inspect current repositories and instructions, determine whether the product is new or already registered, build a repository and contract inventory, identify context drift, and present an adoption plan.

**Does not authorize:** Creating or changing product files, installing instruction adapters, merging PRs, or implementing application features.

## Authorize implementation

```text
Proceed with implementation.
```

**Purpose:** Authorize the selected specialist to implement the most recently presented and unchanged scope.

**Preconditions:** The specialist identity, work classification, scope, repositories, branch source, material risks, and intended outputs have been established.

**Effect:** Implementation authorization becomes active only for that scope.

**Does not authorize:** Scope expansion, automatic specialists, merging, production deployment, package publication, destructive operations, or unrelated repository changes.

Material scope changes invalidate the authorization and require a refreshed proposal followed by a new standalone command.

## Start a business context session

```text
Start an Agent Eco Space business context session.
```

**Purpose:** Start a business-facing, context-only Agent Eco Space session without assigning a code repository.

**Discovery precondition:** The session already knows the canonical Agent Eco Space governance repository, product name, central product-context repository, presenter ID, and presenter or stage name. In a new or ambiguous session, use the complete [Business Context Mode Prompt](../templates/call-agent-eco-space-business-context.md), which pre-fills presenter ID `africanies-support-assistant` for AfricanIES.

**Selected role:** Ada is selected and locked internally by default. The session confirms Ada instead of asking who it is operating as, unless the human explicitly requests another specialist. Ada presents herself using the supplied human-approved stage name while retaining the presenter ID for traceability.

**Effect:** Run the Business Context Readiness Check and answer from central context in clear language suitable for non-technical business users. Distinguish released behaviour, unreleased implementation records, approved plans, proposals, superseded rules, uncertainty, and matters requiring code or specialist verification.

**Read-only default:** Business explanations, summaries, comparisons, and communication drafts do not require implementation authorization.

**Does not authorize:** Code inspection or implementation, repository registration, adapter installation, context mutation, publication, another specialist, merge, deployment, release, or access expansion. A proposed central-context change still requires the standalone `Proceed with implementation.` command; publication requires its separate applicable approval.

Task verbs, urgency, conversation flow, previous approval, and the absence of `Do not code yet` never substitute for this command. Authorization is single-use, scope-bound, non-retroactive, and revocable.

## Suspend governance for one task

```text
Suspend Agent Eco Space governance for this task.
```

**Purpose:** Deliberately suspend Agent Eco Space governance for one already-established task.

**Preconditions:** A human sends the exact text as a standalone message after the task scope is established. The specialist must acknowledge the scope and explain which Agent Eco Space protections will no longer govern it before acting.

**Effect:** Suspends Agent Eco Space only for that task. Higher-priority platform, safety, permission, and legal requirements remain active.

**Does not authorize:** Merge, deployment, publication, destructive operations, access expansion, unrelated work, or a later task.

Similar wording and generic statements that previous instructions no longer apply do not trigger this command. They place the session in Governance-Uncertain Mode. After suspension ends or governance is restored, further repository mutation requires a refreshed proposal and a new standalone `Proceed with implementation.` command.

## Add a repository

```text
Add this repository to Agent Eco Space.
```

**Purpose:** Register another repository with an existing Agent Eco Space product and its central context.

**Required input:** Existing product name, central-context location, and the repository URL or workspace path being added. Use the complete [Add Repository Prompt](../templates/add-repository-to-agent-eco-space.md) in a new or ambiguous session.

**Effect:** Inspect and classify the repository, verify it is not already registered, map relationships and contracts, identify drift and risks, and present the central-context and instruction-adapter changes required.

**Does not authorize:** Modifying either repository, automatically selecting the Engineering Manager, activating other specialists, creating or merging PRs, deployment, or publication.

## Synchronize existing work

```text
Synchronize this work with Agent Eco Space.
```

**Purpose:** Backfill verified work from an existing AI session and code repository into the product's central context.

**Required input:** Current repository, central-context repository, product name, and optionally a commit, PR, version, or date range. Use the complete [Synchronization Prompt](../templates/synchronize-existing-work.md) when Agent Eco Space locations are not already established.

**Effect:** Verify implementation against repository evidence, compare it with existing context, avoid duplicates, reconstruct relevant history with confidence labels, and present exact context changes and a PR plan.

**Does not authorize:** Changing application code, inventing undocumented history, modifying context before `Proceed with implementation.`, merging a PR, deployment, or publication.

## Refresh Agent Eco Space understanding

```text
Refresh this repository's Agent Eco Space understanding.
```

**Purpose:** Refresh the selected agent's verified understanding of current Agent Eco Space governance, repository adapters and manifest, and relevant central product context.

**Required input:** Product name, application or component name, repository name and location, central-context location, and the governance repository. Use the complete [Refresh Understanding Prompt](../templates/refresh-agent-eco-space-understanding.md).

**Effect:** Run the readiness preflight, compare installed governance and context with their canonical sources and repository evidence, classify drift and valid local customizations, and present one reconciliation proposal.

**Does not authorize:** Changes beyond the narrow automatic adapter-compliance exception; modifying context, product code, or ordinary documentation; invoking another specialist; merging a pull request; deployment; or publication.

## Upgrade installed Agent Eco Space governance

```text
Upgrade this repository to the latest Agent Eco Space governance.
```

**Purpose:** Bring an already-governed repository and active session into compliance with a newer canonical Agent Eco Space revision.

**Required state:** Agent Eco Space is already installed. The session has an existing product, component, repository, manifest, context registration, and usually an established specialist. Use the complete [Governance Upgrade Prompt](../templates/upgrade-agent-eco-space-governance.md) when locations or versions are not already known.

**Effect:** Compare the recorded and current governance revisions, verify every manifest-required adapter, automatically restore deleted required adapters, reconcile managed content and manifest metadata, recover compliant local sections from Git history when safe, retire conflicts with history, verify adapter loading, and return a Governance Upgrade Report.

**Does not repeat:** Product adoption, repository registration, initial ecosystem intake, general context reconciliation, or full sibling-repository study unless evidence proves existing setup is invalid.

**Standing authorization:** Canonical local adapter compliance repair is automatic and does not require `Proceed with implementation.` It is limited to governed adapters, manifest metadata, and compatibility support files. It never authorizes product changes or a write to Agent Eco Space itself.

## Refresh complete product ecosystem understanding

```text
Refresh this product's Agent Eco Space ecosystem understanding.
```

**Purpose:** Perform a human-approved, read-only restudy of the complete registered product ecosystem when the recorded intake is stale, incomplete, materially changed, or explicitly requested.

**Required input:** Product name, central-context location, current repository, and the previous intake revision and date when known. Use the complete [Product Ecosystem Refresh Prompt](../templates/refresh-product-ecosystem-understanding.md).

**Effect:** Refresh active business rules and decisions, inspect every registered repository context directory, verify accessible repository revisions and relationships, detect new or changed contracts and drift, and return a compact ecosystem receipt plus a precise reconciliation proposal.

**Does not authorize:** Changing central context, manifests, adapters, code, documentation, or changelogs; invoking another specialist; merging; deployment; or publication. Changes still require the standalone `Proceed with implementation.` command.

## Future commands

New commands must be added here before they are treated as workflow triggers. Each entry must define exact text, purpose, preconditions, effects, exclusions, and whether it changes authorization state.
