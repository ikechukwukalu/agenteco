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

## Future commands

New commands must be added here before they are treated as workflow triggers. Each entry must define exact text, purpose, preconditions, effects, exclusions, and whether it changes authorization state.
