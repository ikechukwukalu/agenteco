# Local-Only Agent Eco Space Startup Prompt

Use this at the start of a session when the company project must not gain tracked Agent Eco files. Replace the placeholders; the company-approved context location is required, while a personal or remote copy is optional and **disabled by default**. This prompt does not authorize repository or context mutation.

```text
Use Agent Eco Space in Local-Only Mode for this product.

Agent Eco governance source: https://github.com/ikechukwukalu/agenteco
Product: <PRODUCT_NAME>
Application or component: <APPLICATION_OR_COMPONENT_NAME>
Company repository remote: <EXACT_REPOSITORY_REMOTE>
Project workspace: <ABSOLUTE_PROJECT_PATH>
Approved local context root, outside the project worktree: <ABSOLUTE_APPROVED_CONTEXT_PATH>
Local registration: <ABSOLUTE_APPROVED_REGISTRATION_PATH>
Optional personal or external context destination: none unless separately authorized and recorded in the local registration.

First verify that the project remote and path match the local registration, that this local context is authorized for this machine and audience, and that you can actually read the applicable Agent Eco governance and product context. Report any missing access, stale version, conflicting repository instructions, or unverified activation. Use the local context and the current role-specific rules only after verification. Ask who you are operating as today unless the role was already selected.

Do not create, edit, restore, stage, or commit Agent Eco adapters, manifest, outbox, or context inside the company code repository. Do not add an Agent Eco entry to its .gitignore. Keep local pending updates and review history in the approved external context. Never claim that a local update was shared, pushed, or merged.

Follow the ordinary scope rules and wait for the standalone "Proceed with implementation." command before code or context changes. Respect company AI and information-handling rules. Do not copy company context to a personal account or remote destination without explicit permission. Continue with the requested task only after this Local-Only Readiness Preflight.
```
