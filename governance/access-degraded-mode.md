# Access-Degraded and Offline Mode

This mode applies when a repository contains an Agent Eco Space adapter but the active AI cannot access canonical governance or the central product-context repository.

## Required disclosure

The specialist reports whether it can access the current repository, local Agent Eco Space instructions and version, canonical Agent Eco Space, a local or remote central-context repository, and connected repositories required by the task.

Never claim that inaccessible context was reviewed, synchronized, committed, pushed, or submitted.

## Operating boundary

The local adapter supplies only the compact non-negotiable contract. Continue only when that contract and verified local evidence are sufficient. If missing business rules, contracts, security requirements, or repository relationships could materially change implementation, stop affected work and request access or approved context.

## Context update outbox

When work can safely continue but remote context cannot be updated, create a **Context Update Package** using the canonical template. It records identity, available governance and context versions, implementation evidence, verified changes, affected rules and contracts, intended context destinations, consumers, risks, and status `Pending Context Sync`.

Store it inside the active codebase's version-controlled Agent Eco Space outbox:

```text
.agenteco/outbox/context/
```

This is the repository's offline context registry, not the authoritative central context repository. Add the package to the active feature or hotfix branch and include it in the applicable code PR so Git preserves it for other machines and specialists.

Do not add this outbox to `.gitignore`. It must be tracked. Before committing, verify repository visibility and information classification. Never place secrets, credentials, production customer data, or central-context material in a repository whose authorized audience must not see it. For a public or insufficiently restricted codebase, use a separate approved private recovery repository instead.

Every new Agent Eco Space session checks the outbox after role selection. Finding a pending package does not automatically change the current task, but the specialist reports it and, when remote context access is available, offers to synchronize it.

## Synchronization

An authorized human or later specialist with access must first search the online central context and synchronization ledger using the package identifier, source repository, source commit, and content fingerprint. If the same update is already present, verify that it is equivalent and do not create a duplicate. If it differs or is only partially present, reconcile the records rather than overwriting either one.

When the update is not already online, verify the package against code, reconcile newer context changes, apply it through a context branch and PR, and record its status. The synchronizing specialist does not need to be the specialist who created the package.

Creating or pushing the context PR changes the package to `Submitted`; it is not yet safe to delete. Because specialists cannot merge PRs, the package becomes `Synchronized` only after a human merges the context PR and the specialist verifies the remote commit and synchronization-ledger entry.

The specialist may then remove the live outbox file through the appropriate codebase branch and PR. The removal must never be committed directly to a protected branch or merged by the specialist. Git history preserves the original package, while the central context retains the authoritative record and synchronization evidence.

The original specialist must not report full context synchronization while the package remains pending or merely submitted.

## Local central-context clone

If an authorized local context clone exists without network access, the specialist may prepare a local branch and commit after implementation authorization. It remains `Pending Push` until an authorized user restores access and pushes it.
