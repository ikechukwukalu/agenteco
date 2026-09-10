# Agent Eco Space Local Outbox

Install this directory convention at the common local product-workspace root. When only one repository is available, it may live at that codebase's root:

```text
.agenteco/
  outbox/
    context/
```

Add `.agenteco/outbox/` to the product repository's `.gitignore` unless the human explicitly selects an encrypted, access-controlled shared mechanism.

Each pending file uses the [Context Update Package](../context-update-package.md) template. Use a collision-resistant descriptive filename such as:

```text
2026-09-10-core-backend-quote-contract.md
```

At session startup, report pending packages. A specialist with authorized central-context access may verify and submit any package, regardless of who created it.

Before submission, search the online context and synchronization ledger by package identifier, content fingerprint, repository, and source commit. Do not submit a duplicate. Reconcile any partial or conflicting online record.

Do not delete a local package merely because a branch was pushed or a PR was opened. Delete it only after a human has merged the context PR and both the remote commit and synchronization-ledger entry have been verified. If an equivalent merged record already exists, record that verification before deleting the duplicate local copy. If rejected, retain it with status `Rejected` until the human decides whether to revise or remove it.
