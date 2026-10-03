# Enroll a Product in Production-Context Reconciliation

Use this complete prompt in a new or existing product session. It starts discovery and a bounded proposal, not activation. Replace the placeholders with the actual product registration or known repositories.

```text
Use Agent Eco Space to propose production-to-central-context reconciliation for this product.

Canonical Agent Eco Space repository:
https://github.com/ikechukwukalu/agenteco

Product name:
<PRODUCT_NAME>

Central product-context repository or workspace path:
<CONTEXT_REPOSITORY>

Known source repositories, if available:
<SOURCE_REPOSITORIES_OR_DISCOVER_FROM_PRODUCT_REGISTRATION>

Operate as the Engineering Manager for this product-wide intake unless I have already selected a different specialist. Read the current canonical Production-to-Central-Context Reconciliation policy and the product's existing registration, source manifests, production branches, notification workflows, central receiver and scheduled fallback, reconciliation state, open tasks and PRs, and approval records. Do not assume this is a new product or that a workflow or credential is absent.

Verify required secret names by metadata only: CPI_DISPATCH_TOKEN, CPI_COPILOT_TOKEN, and CPI_SOURCE_READ_TOKEN. Never retrieve or expose their values. Distinguish scanner source access from the executing agent's separate source and governance access. Preserve compatible credentials and workflow references. Determine the smallest missing setup, including any failed runs or blocked agent tasks.

Present a product-specific registration and a migration or onboarding plan. Separate the human's bounded authority to prepare workflow and registration repair PRs from the standing authority for automatic central documentation PRs. Identify approved source repositories, their production branches, central destination, allowed paths, executing agent, effective period, and revocation. Do not infer either grant from a production merge, existing token, or generated task.

Explain how the process will retain one active reconciliation per source, keep newer revisions queued, stop repeated launches when access is blocked, and update the synchronized revision only after a substantive documentation PR is human-merged. Distinguish production-source merge from deployment and customer availability.

Do not change a repository or activate the workflow now. Present exact proposed files, tests, access checks, PRs, and remaining human decisions. Wait for the standalone Proceed with implementation. authorization for changes not already covered by an approved, bounded setup grant. Never merge a PR.
```
