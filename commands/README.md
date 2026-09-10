# Agent Eco Space Command Catalogue

This catalogue documents commands that trigger a defined Agent Eco Space workflow or state transition. Commands are deliberately short, visible, and unambiguous.

## Command rules

- Send a command as a standalone message, without commentary or additional scope.
- A command applies only to the currently established scope and repository context.
- Quoting a command in documentation or conversation does not execute it.
- Similar wording does not trigger a protected state transition.
- No command authorizes a specialist to merge a pull request.

## Adopt a product

```text
Adopt this product into Agent Eco Space.
```

**Purpose:** Begin onboarding an existing or new product.

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

## Future commands

New commands must be added here before they are treated as workflow triggers. Each entry must define exact text, purpose, preconditions, effects, exclusions, and whether it changes authorization state.
