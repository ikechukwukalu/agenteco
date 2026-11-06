# Feature FARS: Failure, Avoidance, Recovery, Success

## Purpose and scope

For every meaningful feature, integration, or behaviour change, the implementing specialist must apply **FARS: Failure and frustration, Avoidance, Recovery, Success**. The requested outcome defines Success. Before implementation, identify credible failure and frustration points, propose an avoidance measure and a recovery path for each, and show this map to the human. Apply it in proportion to user impact and system risk across applications, services, SDKs, packages, and operational features. A small low-risk change may have a short record; a payment, shipment, document, identity, or third-party integration needs deeper treatment. Do not invent every imaginable failure or claim a fallback exists when it has not been implemented and verified.

When a journey has several actors or conditional steps, apply [Journey Actions and Customer Feedback](journey-actions-and-customer-feedback.md): map the actor and visible next action for each state, surface verified backend requirements early on every affected consumer, and make failure guidance clear across channels. Record the map in product context, not just a screen mockup.

For a web product, start from the [mobile-first web capability library](fars-mobile-web-library.md). During product adoption or feature work, select applicable patterns and discover missing product-specific risks. The generic library is guidance, never a substitute for inspecting the real journey, business rules, affected consumers, devices, and dependencies. Backend and provider specialists must account for the mobile customer's experience of their error, latency, and recovery contracts, even when they do not build UI.

For a native mobile product, start from the [native mobile capability library](fars-native-mobile-library.md). Verify platform-specific permissions, lifecycle, background execution, connectivity, device variation, and recovery on supported iOS and Android versions. Flutter implementations must still test actual platform behaviour. Read the applicable library selectively; a web-only task need not load the native-mobile catalogue, and neither catalogue replaces product-specific context.

For a Laravel/PHP backend, start from the [backend capability library](fars-laravel-php-backend-library.md). Identify whether each affected interface returns JSON, renders HTML, processes a job, or receives a webhook. Establish plain-language validation and customer feedback, a consistent response contract, safe internal diagnostics, and the boundary between backend recovery and a client's network-failure experience. Select only applicable backend patterns and verify them against the installed framework version, hosting topology, business rules, and affected consumers. The backend library is not a claim that a recovery is already implemented.

For an internal or external API, include outgoing request changes, incoming response changes, provider/SDK upgrades, outages, partial success, and changed error semantics where credible. Link the FARS failure to the shared [API–Consumer Compatibility Map](api-consumer-compatibility.md) and Consumer Impact Alert when a producer or consumer may break. Frontend specialists must handle an unexpected response without crashing or falsely claiming success, preserve safe user state, and report contract drift. Backend and integration specialists record affected consumers, compatibility tests, and a safe rollout or rollback path; do not assume a schema-valid response is a correct business result.

## Required analysis

Record:

1. **Objective and success path:** the user or system goal, valid input and prerequisites, expected state transitions, external dependencies, successful output, and how success is verified.
2. **Failure and frustration points:** material ways the path can fail or confuse the user, including invalid or incomplete input; permissions or business-rule rejection; unavailable, slow, malformed, or changing third-party responses; package or internal component errors; network, queue, storage, database, and hosting disruptions; and duplicate or partial execution. Identify verified risks separately from plausible scenarios needing validation.
3. **Avoidance points:** for each failure, state the prevention or reduction measure, the responsible component, and what remains possible despite it. If avoidance is infeasible, say so and prioritize a safe recovery; never label an unimplemented control as active.
4. **Recovery paths:** for each failure, state what code does, what state is preserved, whether retry is safe and bounded, how duplicate effects are prevented, whether fallback or manual escalation exists, what the user sees or can do next, and who owns unresolved recovery. If no safe automatic recovery exists, fail clearly and safely rather than pretending success.
5. **Evidence:** engineer-owned tests for important success, avoidance, failure, and recovery paths; monitoring or operational signals where applicable; documentation and customer-facing guidance; known gaps; and exact repository revision. Never claim a path is supported merely because it is documented.

Do not expose secrets, protected environment values, private provider details, or sensitive user data in errors, logs, documentation, or central context. Retries, fallbacks, and user messaging must respect existing business, security, compatibility, and release rules. A successful backend action is not proof that every consumer journey succeeds.

## Implementation and completion gate

Use the analysis to shape validation, error handling, timeouts, idempotency, state cleanup, observability, and user guidance as applicable. Add or update tests that demonstrate the important outcomes. Record what is **implemented and verified**, what is **planned**, and what remains **unsupported**; do not collapse these statuses. A material risk with no credible avoidance or recovery must be raised before readiness is claimed.

Update the assigned repository's central-context directory and affected shared contracts or operational records using the [Feature FARS template](../templates/product-context/feature-paths-and-recovery.md). Keep the record concise enough to scan but detailed enough for another specialist to implement or debug without relying on conversation memory. Update feature/API documentation and `CHANGELOG.md` when behaviour, avoidance, or recovery changes. If a credible material failure lacks an approved recovery design, flag it to the human before claiming the feature is ready; an explicitly accepted residual risk must record owner, impact, and mitigation.

At completion, report the covered success, failure, avoidance, and recovery paths, tested behaviour, gaps, and context destination. The specialist's own tests are not independent QA; retain the separate human decision about Armstrong before an implementation PR.

## Existing-feature audit

When adopting an existing product or changing an established journey, inspect the current implementation and evidence. Mark each applicable FARS control as `Verified`, `Present but unverified`, `Missing`, or `Not applicable`. Document verified controls in the product's central context. Present missing avoidance or recovery as a scoped proposal, with risk, owner, and priority; an audit does not authorize a code rewrite. Preserve prior decisions and do not describe a newly drafted control as already working.
