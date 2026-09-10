# Agent Eco Space Local Outbox

Install this directory in every governed codebase that may need to preserve a context update while central-context access is unavailable:

```text
.agenteco/
  outbox/
    context/
```

Do not add `.agenteco/outbox/` to `.gitignore`. Commit pending packages on the active temporary branch and include them in the code PR so Git preserves them across devices and handoffs.

Before committing a package, verify that everyone who can read the code repository is authorized to read its contents. Never store secrets, credentials, production customer data, or improperly classified information. If the code repository is public or has a broader audience than the context update, store the package in an approved private recovery repository instead.

Each pending file uses the [Context Update Package](../context-update-package.md) template. Use a collision-resistant descriptive filename such as:

```text
2026-09-10-core-backend-quote-contract.md
```

At session startup, report pending packages. A specialist with authorized central-context access may verify and submit any package, regardless of who created it.

Before submission, search the online context and synchronization ledger by package identifier, content fingerprint, repository, and source commit. Do not submit a duplicate. Reconcile any partial or conflicting online record.

Do not delete a package merely because a branch was pushed or a PR was opened. Remove it from the live codebase only after a human has merged the context PR and both the remote commit and synchronization-ledger entry have been verified. Perform removal through the applicable codebase branch and PR; the specialist never merges it. Git history continues to preserve the original package. If rejected, retain it with status `Rejected` until the human decides whether to revise or remove it.
