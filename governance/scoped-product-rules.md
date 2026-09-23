# Scoped Product Rules

## Catalogue and applicability

Every product context keeps a short rule index with stable IDs and links to the authoritative rule text. A rule records its owner and approver, effective period, state, audience and information classification, and applicability by product, repository/component, specialist role, channel, feature or workflow, and environment when relevant. Scope fields may be `all` or an explicit list. Missing scope is unresolved, not permission to apply a rule globally.

At session startup, every specialist reads the small index, filters active rules for its role, product, repository, audience, and task, and loads only those rule bodies plus directly affected decisions. The first product intake may review the whole catalogue once. A customer-facing Ada session loads only customer-safe presentation rules and the active product facts she is permitted to use; internal-only rules remain internal. The index records its context revision and content fingerprint so a snapshot can verify that it is current.

Existing business rules are registered progressively. The migration records their original paths, owners, current or superseded status, effective dates, and any unresolved scope or approval. Do not silently promote an old note into active policy.

## Authority and conflicts

Agent Eco Space safeguards govern every product. Product rules may specialize behavior but cannot weaken confidentiality, explicit authorization, test and QA gates, human-only merging, source verification, or release restrictions. More specific product rules apply only within their stated scope; they do not silently override a global safeguard or an unrelated rule. If two applicable active product rules conflict, the specialist records both IDs and the impact, asks the authorized owner to resolve it, and does not guess. Preserve the superseded rule with replacement, reason, effective date, and decision evidence.

The specialist that changes a rule updates its index row, affected contracts, feature availability, repository directories, customer-safe knowledge and handoffs where applicable. All other specialists see the new index revision at their next session or task. Use the [rule index template](../templates/product-context/scoped-rules.md).
