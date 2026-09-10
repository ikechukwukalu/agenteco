# Access-Degraded and Offline Mode

This mode applies when a repository contains an Agent Eco Space adapter but the active AI cannot access canonical governance or the central product-context repository.

## Required disclosure

The specialist reports whether it can access the current repository, local Agent Eco Space instructions and version, canonical Agent Eco Space, a local or remote central-context repository, and connected repositories required by the task.

Never claim that inaccessible context was reviewed, synchronized, committed, pushed, or submitted.

## Operating boundary

The local adapter supplies only the compact non-negotiable contract. Continue only when that contract and verified local evidence are sufficient. If missing business rules, contracts, security requirements, or repository relationships could materially change implementation, stop affected work and request access or approved context.

## Context update outbox

When work can safely continue but remote context cannot be updated, create a **Context Update Package** using the canonical template. It records identity, available governance and context versions, implementation evidence, verified changes, affected rules and contracts, intended context destinations, consumers, risks, and status `Pending Context Sync`.

Store it under the governed product workspace's standard local outbox:

```text
.agenteco/outbox/context/
```

This directory may sit inside the local codebase when that is the only available workspace, or preferably at the common local product-workspace root when several repositories are checked out together. It is an offline context registry, not an authoritative online context repository.

The outbox is local operational state and should normally be excluded from the product repository through `.gitignore`. Never place secrets, customer data, or confidential context in a public repository or an unsafe workstation.

Every new Agent Eco Space session checks the outbox after role selection. Finding a pending package does not automatically change the current task, but the specialist reports it and, when remote context access is available, offers to synchronize it.

## Synchronization

An authorized human or later specialist with access must first search the online central context and synchronization ledger using the package identifier, source repository, source commit, and content fingerprint. If the same update is already present, verify that it is equivalent and do not create a duplicate. If it differs or is only partially present, reconcile the records rather than overwriting either one.

When the update is not already online, verify the package against code, reconcile newer context changes, apply it through a context branch and PR, and record its status. The synchronizing specialist does not need to be the specialist who created the package.

Creating or pushing the context PR changes the package to `Submitted`; it is not yet safe to delete. Because specialists cannot merge PRs, the package becomes `Synchronized` only after a human merges the context PR and the specialist verifies the remote commit and synchronization-ledger entry. The local pending package may then be deleted. The central context retains the durable change history and synchronization evidence.

The original specialist must not report full context synchronization while the package remains pending or merely submitted.

## Local context clone

If an authorized local context clone exists without network access, the specialist may prepare a local branch and commit after implementation authorization. It remains `Pending Push` until an authorized user restores access and pushes it.
