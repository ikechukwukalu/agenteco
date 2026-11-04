# FARS Laravel/PHP Backend Capability Library

FARS means **Failure and frustration, Avoidance, Recovery, Success**. This is a generic discovery library for Laravel/PHP backends, including JSON APIs and server-rendered web applications. It is not an implementation checklist to copy blindly: select relevant capabilities, establish the product's actual success outcome, inspect its deployment topology and consumers, then record feature-specific failures and evidence in the [product-context FARS record](../templates/product-context/feature-paths-and-recovery.md). Each row below proposes controls; none proves a control exists in a product.

The backend owns a truthful operation state and response contract. The consuming web or mobile application owns presentation when a response reaches it. If DNS, TLS, a proxy, or the network fails before the backend can answer, the client or edge must provide the visible fallback; the backend must still make outcome lookup and consequential retries safe. For every customer-visible failure, distinguish **what happened**, **whether the operation completed or remains uncertain**, and **what to do next**. Use plain, professional language understandable to a young teenager without talking down to the customer. Keep detailed diagnostics internal and sanitized. Never leak stack traces, raw database errors, provider payloads, secrets, or another customer's data.

First identify the interface: JSON API, server-rendered HTML, background job, webhook, or a combination. Preserve the repository's existing compatible contract unless a separately approved migration changes it. Define stable machine-readable error codes, appropriate HTTP status, customer-safe message, field-level corrections when applicable, operation status or lookup reference for uncertain outcomes, and a non-sensitive support reference. Do not claim that a queued, accepted, or partially completed operation succeeded. Test the same failure through each supported consumer. Laravel can customize [validation](https://laravel.com/docs/12.x/validation), [exception reporting and HTML/JSON rendering](https://laravel.com/docs/12.x/errors), and [localization](https://laravel.com/docs/12.x/localization); verify the actual framework version and application conventions before implementation.

## Validation, nested inputs, and translations

Success: the backend accepts valid input or directs the customer to the exact correction needed.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Raw paths such as `boxes.0.items.2.weight` or zero-based indexes appear in messages | Map nested attributes to the labels and one-based numbering shown by the consumer; test arrays with multiple boxes and items | Return a stable field identifier for the client and a human message such as “Enter a weight for item 3 in box 1”; preserve valid entries |
| Validation wording is vague, harsh, untranslated, or disagrees with business rules | Review locale strings and examples with the actual form, API contract, and business-rule owner | Explain what to correct and acceptable format or range without exposing implementation details |
| Client checks pass but server validation rejects the payload | Keep server rules authoritative and contract-test the submitted shape across consumers | Return field-specific corrections; notify affected consumer owners when a request contract changed |

## JSON APIs, web pages, and response contracts

Success: each supported consumer receives a consistent, truthful outcome it can present clearly.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| The same failure alternates between JSON, HTML, or an unstructured exception | Define response negotiation and test API versus web routes, `Accept` headers, and expected error envelopes | Return the agreed format with an appropriate status and action, not a stack trace or a false success body |
| Changed error codes, field names, or response payloads break web/mobile clients | Maintain the API–Consumer Compatibility Map, contract tests, versioning or compatibility windows, and staged rollout | Preserve a supported old contract or coordinate consumer repair; issue a Consumer Impact Alert |
| A request times out after the operation actually succeeded | Give consequential actions an operation identity and status lookup; design idempotency where applicable | Ask the client to check authoritative status before retrying; state uncertainty honestly |

## Exception handling, logs, and diagnostics

Success: operators can diagnose a failure while customers see safe guidance.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Customer sees a trace, SQL exception, filesystem path, provider response, or secret | Keep production debug output off; centralize safe exception rendering; test error paths | Give a plain message and safe support reference while retaining sanitized diagnostics internally |
| Errors are swallowed, logged twice, or lack a way to connect a report to a request | Define reporting ownership, severity, correlation IDs, and redaction rules | Alert the right owner; use the reference to investigate and correct the customer-facing state |
| Logs or central context contain credentials or private customer information | Minimize and redact data; restrict access and retention; never read `.env` or `.env.*` values except permitted `.env.example` placeholders | Contain exposure through the security process, rotate affected credentials where required, and remove improper copies |

## Customer notifications and state guidance

Success: the customer receives timely, accessible, accurate next-step information.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| “Completed” is sent while work is only queued, paid but unreconciled, or awaiting a document | Derive notification wording from authoritative state transitions, not job dispatch | Correct the visible status and tell the customer what is pending and how to check it |
| Email, SMS, push, or in-app notification is delayed, undelivered, duplicated, or misleading | Track attempt versus delivery evidence; use consented channels and deduplication; keep essential status available in-app | Retry only when safe, offer an alternate status channel, and correct materially wrong messages |
| A message names an error but gives no useful action | Pair each customer-safe error class with a specific correction, safe retry, wait, or support route | Keep the explanation available beyond a transient toast; give a reference when support is needed |

## Authentication, authorization, and abuse controls

Success: the rightful actor can complete an allowed action without exposing another person's data.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Session or token expires mid-task | Test expiry and refresh policies; keep non-sensitive resumable state where permitted | Re-authenticate and resume only after checking whether the original action completed |
| Incorrect role, tenant, or object access leaks data or blocks legitimate users | Enforce policy per action and resource; test positive and negative access paths | Deny safely without revealing protected details; provide approved access or support route |
| Rate limit or lockout traps a legitimate customer | Apply proportionate throttling and clear, non-enumerating messages | Explain when and how to retry or use an approved recovery channel |

## Database availability, transactions, and migrations

Success: reads and writes reflect one authoritative, durable business state.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Database connection fails, times out, or reaches capacity | Monitor connectivity and saturation; bound waits; avoid unnecessary queries | Do not claim data was saved; preserve permissible client input and verify the earlier outcome before retry |
| A multi-step write partially succeeds or concurrent requests overwrite each other | Use transactions, constraints, locks or optimistic versions where justified; test races | Roll back local incomplete work or reconcile committed external effects before reporting status |
| Deployment migration leaves old workers or clients incompatible | Plan backward-compatible schema stages and worker lifecycle; test rollback limitations | Restore compatible service and reconcile records affected during the transition |

## Queues, jobs, events, and scheduled work

Success: accepted background work reaches a verified terminal state once per intended operation.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Worker stops, backlog grows, or job fails without visibility | Monitor queue age and failed jobs; set timeouts and alert thresholds | Mark work pending or failed accurately; retry or escalate with the original operation reference |
| Retried job repeats a charge, shipment, or notification | Use durable idempotency or deduplication and appropriate transaction boundaries | Reconcile the original side effect before another attempt; repair duplicates through an approved process |
| Scheduler runs twice, not at all, or at the wrong time | Verify scheduler deployment, locks where applicable, timezone, and missed-run monitoring | Run a controlled catch-up or manual process without duplicating effects |

## Cache, search, pagination, and stale reads

Success: customers and consumers see appropriately fresh, correctly scoped information.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Stale cache shows an old price, permission, balance, or shipment state | Define freshness limits and invalidation by business impact; do not trust cache for critical final decisions | Read authoritative data or explain that current information is temporarily unavailable |
| Search or pagination loses, duplicates, or misorders records | Use stable ordering, bounded pages, filters, and representative data tests | Restore query context and give a safe refresh path without acting on the wrong record |
| Cache or search service is down | Define whether a bounded database fallback is safe under load | Degrade honestly, or return a retryable unavailable state with operational alerting |

## Files, uploads, storage, and document generation

Success: a file is safely accepted or a document becomes available without misreporting the underlying transaction.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Upload is too large, malformed, interrupted, or stored without its record | State limits and formats, validate before use, and verify durable storage and record linkage | Explain the correction, retain the wider task, and retry only the file step where safe |
| Storage or PDF provider fails after a shipment or payment succeeded | Separate core transaction state from document readiness and monitor generation | Keep the transaction reference; say the document is pending; retry generation without recreating the transaction |
| Download is missing, expired, unauthorized, or exposes private data | Check access on each request; define expiry and document availability | Offer a fresh authorized link or support route without leaking the file or its location |

## Third-party APIs, SDKs, and webhooks

Success: external effects are verified, compatible, and correctly represented to consumers.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Provider outage, maintenance, slow response, or rate limit | Set bounded timeouts and safe retry policy; monitor dependency health; separate pending from failed | Defer or escalate when supported, give a truthful status, and reconcile before repeating an effect |
| SDK upgrade changes sent payloads, received fields, status meanings, or error semantics | Contract-test old/new behavior and affected consumers; stage upgrades and map dependencies | Roll back or adapt compatibly; alert producer and consumer owners; preserve affected operation IDs |
| Webhook arrives late, twice, out of order, or never arrives | Verify authenticity, deduplicate events, and reconcile against provider truth | Repair state through a controlled reconciliation path, not an unverified “success” message |

## Payments and other high-stakes operations

Success: exactly the intended operation and amount are recorded and communicated.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Provider charges but acknowledgement is lost | Use stable references, idempotency, and authoritative provider verification | Check whether payment completed before asking for another payment; show pending when uncertain |
| Duplicate submit, callback, or retry produces a second effect | Protect at client, API, job, and provider boundaries; test concurrency | Reconcile duplicates and follow an approved refund or correction process |
| Currency, amount, tax, or fee differs between quote and final charge | Preserve pricing version and confirm total before commitment | Stop unsafe completion, explain changed amount, and require renewed confirmation |

## Hosting, network edge, and service capacity

Success: the hosted service remains reachable or its failure is detected and handled honestly.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| DNS, TLS, proxy, load balancer, or network failure prevents a request reaching Laravel | Monitor the full path and test edge health, certificates, and failover where available | Client or edge shows the fallback; preserve work and check operation status before retry |
| PHP process, web server, or dependency exhausts capacity | Set resource budgets, health checks, autoscaling or capacity plans as applicable | Return service-unavailable guidance when possible; alert operators and restore capacity |
| Slow backend causes mobile timeouts and repeated taps | Profile slow routes, paginate, offload long work, and define pending responses | Provide status lookup and safe retry rather than starting duplicate work |

## Deployment, configuration, and production rollback

Success: compatible code, configuration, schema, and workers serve the intended release.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Missing configuration, stale config cache, or mismatched worker code breaks a release | Validate required setting presence without reading secret values; check cache and worker lifecycle | Restore compatible configuration or prior service, then reconcile operations during the incident |
| New backend contract is live before web/mobile consumers are ready | Track feature availability per environment and consumer; require compatibility checks | Keep old contract or controlled feature gate; alert consumers and delay customer-ready claims |
| Rollback leaves changed data or external side effects behind | Test rollback boundaries and forward-repair plans | Restore service, repair data deliberately, and record what was actually deployed and recovered |

## Privacy, security, localization, and accessibility of feedback

Success: guidance is understandable and safe across supported audiences and locales.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Message uses internal jargon, color-only meaning, or a translation that changes the action | Review copy in every supported locale and device flow, including error and pending states | Give a plain-language next step with a text label the client can present accessibly |
| Customer receives another person's status or sensitive detail through an error or notification | Minimize response data; enforce recipient, tenant, and channel access checks | Contain the incident and follow the security response; do not disclose more in the correction |
| Date, time, unit, or currency is misunderstood | Use explicit locale-aware formatting and units in business-critical messages | Clarify the value before commitment and provide a safe correction route |

## Verification and continuity

For each applicable feature, test the success path and credible failures through the real API/web contract and affected consumers. Include wrong input, no response, partial success, duplicate execution, provider changes, and recovery after interruption where material. Record exact customer-facing copy, machine-readable code or field key, operation status, logs/alerts, safe retry rule, test evidence, owner, and remaining gap in product context. Mark controls `Verified`, `Present but unverified`, `Missing`, or `Not applicable`; never infer implementation from this library. A backend-only test does not prove a web or mobile customer journey works. Keep feature/API documentation and `CHANGELOG.md` aligned with verified behavior.

Laravel's [database transaction](https://laravel.com/docs/12.x/database), [queue](https://laravel.com/docs/12.x/queues), [HTTP client](https://laravel.com/docs/12.x/http-client), and [notification](https://laravel.com/docs/12.x/notifications) facilities can support some candidate controls. Confirm the product's installed Laravel/PHP versions and deployment configuration before choosing a mechanism.
