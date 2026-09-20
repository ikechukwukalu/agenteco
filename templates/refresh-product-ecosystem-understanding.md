# Refresh Product Ecosystem Understanding

Use this prompt when the recorded complete ecosystem intake is stale, incomplete, or explicitly due for review. It authorizes read-only study, not repository mutation. Replace every placeholder before sending it.

```text
Refresh this product's Agent Eco Space ecosystem understanding.

Agent Eco Space governance repository:
https://github.com/ikechukwukalu/agenteco

Product name:
<PRODUCT_NAME>

Central product context repository:
<CENTRAL_CONTEXT_REPOSITORY_URL_OR_WORKSPACE_PATH>

Current repository name and location:
<REPOSITORY_NAME_AND_URL_OR_WORKSPACE_PATH>

Recorded ecosystem-intake revision and date:
<CONTEXT_REVISION_AND_DATE_OR_UNKNOWN>

Read the current active business rules and decisions, product overview, architecture, repository map, contracts, handoffs, risks, releases, synchronization records, and every registered repository context directory. Identify every registered application, backend, frontend, mobile app, microservice, package, SDK, and infrastructure repository.

Where access exists, verify each repository's purpose, current revision, produced and consumed contracts, documentation systems, changelog, consumers, producers, and material changes against repository evidence. For every applicable backend, refresh its route inventory, route-to-consumer relationships, recorded consumer revisions, confidence states, compatibility risks, and unresolved Consumer Impact Alerts. Ask consumer specialists to confirm only their own observed integrations; do not invent consumption from route existence alone. Record inaccessible repositories and uncertainty rather than guessing.

Compare the current ecosystem with the previous intake. Report new, removed, renamed, split, archived, stale, or conflicting repositories, relationships, APIs, events, packages, data contracts, business rules, decisions, handoffs, risks, documentation systems, and releases. Identify the current repository's updated connections and task-relevant implications, including API changes that may break a mapped web, mobile, SDK, service, or third-party consumer.

Return a compact ecosystem receipt containing the context revision, repositories reviewed, revisions verified, relationships added or changed, unresolved Consumer Impact Alerts, access gaps, material drift, and recommended next reminder date. Do not dump the full context back to me.

Present the exact central-context, manifest, contract, documentation-inventory, handoff, risk, and repository-context updates required. Do not modify any repository until I send the standalone "Proceed with implementation." command. You may prepare pull requests after authorization, but you must never merge them.
```
