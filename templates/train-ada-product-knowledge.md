# Train Ada with New Product Knowledge

Use this prompt to add, correct, supersede, or clarify product knowledge in central context. It does not update Agent Eco Space itself.

```text
Train Ada with new product knowledge.

Agent Eco Space governance repository:
https://github.com/ikechukwukalu/agenteco

Product name:
<PRODUCT_NAME>

Central product context repository:
<CENTRAL_CONTEXT_REPOSITORY_URL_OR_WORKSPACE_PATH>

Knowledge owner:
<KNOWLEDGE_OWNER>

Approver:
<APPROVER_OR_APPROVAL_PROCESS>

Proposed new, corrected, or superseding information:
<PRODUCT_KNOWLEDGE>

Authoritative evidence or source:
<EVIDENCE_OR_SOURCE>

Effective date and review date, if applicable:
<EFFECTIVE_AND_REVIEW_DATES>

Authorized audience or information classification:
<AUDIENCE_OR_CLASSIFICATION>

Customer-safe wording, if applicable:
<APPROVED_CUSTOMER_SAFE_WORDING_OR_TO_BE_DRAFTED>

Treat this as a proposed central product-context update, not as immediately authoritative knowledge. Do not modify Agent Eco Space or any application repository.

Read the relevant existing central context and compare the proposal with current, historical, superseded, and conflicting records. Ask only the material questions needed to establish ownership, approval, evidence, effective date, scope, audience, confidentiality, customer-safe wording, exceptions, expiry, affected workflows, and whether the information replaces, corrects, or supplements an existing rule.

Preserve history. Never silently overwrite a prior directive. Mark replaced information as superseded and link the correction or replacement with its reason, date, evidence, and approver.

Separate internal-only detail from customer-safe knowledge. Never place secrets, credentials, protected `.env` or `.env.*` values, unauthorized customer data, or improperly classified information in central context or a Context Update Package.

For an indicative or basic rate card, record its owner and approver, effective and review dates, currency, units, lanes or service scope, authorized audience, exclusions, verified pricing factors, required final-quotation inputs, approved customer-safe explanation, escalation route, and superseded rate history. Require Ada to say that the basic rate is not the final cost, explain only the product-verified reasons, and guide the user toward an accurate quotation. Do not invent generic pricing factors as product facts.

Present a concise reconciliation proposal containing the exact central-context destinations, additions, corrections, superseded records, downstream documentation or support effects, risks, and verification plan. Do not change any repository until I send the standalone "Proceed with implementation." command.

After authorization, create a central-context branch and pull request but never merge it. If write access is unavailable, create a Context Update Package in the assigned governed repository's version-controlled `.agenteco/outbox/context/` when available. If no governed repository is assigned, return a clearly labelled copyable pending package and state that it has not been synchronized.
```
