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

Agent Eco Space is a sibling of AgentHQ, not a replacement. AgentHQ remains suitable for formally orchestrated delivery; Agent Eco Space is optimized for direct specialist execution, cross-repository continuity, and controlled cost.

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

See the [Command Catalogue](commands/README.md) for exact meanings and preconditions.
