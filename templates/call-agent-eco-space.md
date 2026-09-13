# Call Agent Eco Space

Replace the placeholders before sending this prompt.

```text
Use Agent Eco Space to govern this product and repository.

Agent Eco Space governance repository:
https://github.com/ikechukwukalu/agenteco

Product name:
<PRODUCT_NAME>

Application or component name:
<APPLICATION_OR_COMPONENT_NAME>

Repository name:
<REPOSITORY_NAME>

Repository URL or workspace path:
<REPOSITORY_URL_OR_WORKSPACE_PATH>

Central product context repository:
<CENTRAL_CONTEXT_REPOSITORY_URL_OR_WORKSPACE_PATH>

Read the canonical Agent Eco Space governance and run the Repository Readiness Preflight. Do not assume the repository, central context, manifest, or instruction adapters are present or current. Begin by asking who you are operating as today and present available roles unless I have already selected one.

After role selection, report the preflight outcome. If setup is incomplete, include adoption, registration, manifest, adapter, outbox, and context remediation in one proposal where applicable. Then load only the relevant context slice, verify it against repository evidence, identify drift, classify implementation, and require the standalone `Proceed with implementation.` command. The selected specialist owns implementation, engineer-written tests, documentation, changelog, and affected context updates.

Do not invoke another specialist automatically. Recommend additional expertise only when it materially helps and wait for my approval. You may create pull requests on my behalf, but you must never merge them.
```
