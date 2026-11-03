# Feature Success, Failure, and Recovery Paths

## Purpose and scope

For every meaningful feature, integration, or behaviour change, the implementing specialist must reason about more than the ideal outcome. Before implementation, describe the expected **success path**, credible **failure points**, and safe **recovery paths** in proportion to user impact and system risk. This applies to applications, services, SDKs, packages, and operational features. A small low-risk change may have a short record; a payment, shipment, document, identity, or third-party integration needs deeper treatment. Do not invent every imaginable failure or claim a fallback exists when it has not been implemented and verified.

## Required analysis

Record:

1. **Objective and success path:** the user or system goal, valid input and prerequisites, expected state transitions, external dependencies, successful output, and how success is verified.
2. **Failure points:** material ways the path can fail, including invalid or incomplete user input; permissions or business-rule rejection; unavailable, slow, malformed, or changing third-party responses; package or internal component errors; network, queue, storage, database, and hosting disruptions; and duplicate or partial execution where relevant. Identify which are verified risks versus plausible scenarios needing validation.
3. **Recovery paths:** what the code does, what state is preserved, whether retry is safe and bounded, how duplicate effects are prevented, whether a fallback or manual escalation exists, what the user sees or can do next, and who owns unresolved recovery. If no safe automatic recovery exists, fail clearly and safely rather than pretending success.
4. **Evidence:** engineer-owned tests for important success and failure paths, monitoring or operational signals where applicable, documentation and customer-facing guidance, known gaps, and the exact repository revision. Never claim a recovery path is supported merely because it is documented.

Do not expose secrets, protected environment values, private provider details, or sensitive user data in errors, logs, documentation, or central context. Retries, fallbacks, and user messaging must respect existing business, security, compatibility, and release rules. A successful backend action is not proof that every consumer journey succeeds.

## Implementation and completion gate

Use the analysis to shape validation, error handling, timeouts, idempotency, state cleanup, observability, and user guidance as applicable. Add or update tests that demonstrate the important outcomes. Record what is **implemented and verified**, what is **planned**, and what remains **unsupported**; do not collapse these statuses.

Update the assigned repository's central-context directory and affected shared contracts or operational records using the [Feature Paths and Recovery template](../templates/product-context/feature-paths-and-recovery.md). Keep the record concise enough to scan but detailed enough for another specialist to implement or debug without relying on conversation memory. Update feature/API documentation and `CHANGELOG.md` when behaviour or recovery changes. If a credible material failure lacks an approved recovery design, flag it to the human before claiming the feature is ready; an explicitly accepted residual risk must record owner, impact, and mitigation.

At completion, report the covered success and failure paths, tested recovery behaviour, gaps, and context destination. The specialist's own tests are not independent QA; retain the separate human decision about Armstrong before an implementation PR.
