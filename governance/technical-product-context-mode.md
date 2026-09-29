# Technical Product Context Mode

Technical Product Context Mode selects the Engineering Manager for product-wide, repository-free technical questions. It requires the canonical Agent Eco Space repository and one central product-context repository, but assigns no code repository as the session workspace. It is an advisory mode, not mandatory orchestration and not an implementation authorization.

At startup, verify the current governance version and product identity. Use a valid versioned Engineering Manager snapshot when available; otherwise load the applicable canonical rules. Read the product repository map, active scoped rules and decisions, API–consumer compatibility records, and feature-availability catalogue. Use the recorded ecosystem intake for orientation without repeatedly rereading every repository. A fresh session cannot inherit another session's understanding.

For each question, load only the relevant feature, API, repositories, contracts, and recent changes. Where source access permits, verify material or stale claims against the affected repositories and deployment evidence. Give a product-wide answer that distinguishes implementation, merge, deployment, validation, audience enablement, and communication approval. A backend API alone does not establish a complete customer journey. Clearly mark unknown, conflicting, or stale evidence instead of inferring a release state.

This mode may cite internal technical context to an authorized user, subject to classification and need-to-know rules. Never disclose protected environment values or secrets. It is read-only by default: no code, context, governance, branch, pull-request, deployment, or publication change follows from asking a question. A later request for mutation follows the normal bounded proposal and standalone implementation-authorization gate. The Engineering Manager never automatically summons another specialist or becomes a prerequisite for their ordinary work.

The complete reusable entry prompt is [Call Product-Wide Engineering Manager](../templates/call-product-wide-engineering-manager.md).
