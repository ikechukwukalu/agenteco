# FARS Mobile-First Web Capability Library

FARS means **Failure and frustration, Avoidance, Recovery, Success**. Success is the intended user outcome; identify credible failures first, then design avoidance for each failure and a truthful recovery when avoidance fails. This catalogue is reusable across products, not a claim that every product has every capability. Select applicable entries and add product-specific risks. Use it during new-product intake, existing-product adoption, new-feature design, and retrospective review. The [FARS workflow](feature-paths-and-recovery.md) and [product-context template](../templates/product-context/feature-paths-and-recovery.md) govern application and evidence.

Mobile web is the default starting context: test narrow viewports, touch, keyboard-open states, zoom, assistive technology, slow devices, intermittent networks, and supported browsers. This also affects backend and provider contracts, not only page layout. Desktop remains in scope. Avoidance and recovery below are candidate patterns; a specialist must verify feasibility, business rules, security, and actual implementation before claiming one exists. An unimplemented fallback must not be promised to users.

## Forms and multi-step journeys

Success: valid information is entered and the intended task completes.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Unclear field, unit, format, or required status | Visible labels, examples, and instructions before entry | Identify the exact field and correction without erasing valid entries |
| Validation arrives only after several steps | Validate known constraints early and again on the server | Return to the affected step with values and focus preserved |
| Refresh, timeout, or navigation loses a long form | Preserve safe, non-sensitive drafts and warn before abandonment | Restore the permissible draft or explain what must be re-entered |
| Mobile keyboard hides fields or controls | Test keyboard-open layouts and reachable actions | Bring the affected field and error into view without resetting the step |
| Repeated submit creates duplicate work | Immediate pending state and server-side duplicate protection | Check the existing operation before offering another attempt |
| Frontend and backend validation disagree | Contract tests and compatible rules | Preserve entered data, show a safe field error, and report contract drift |

## Registration, sign-in, and social sign-in

Success: the rightful person creates or enters the intended account securely.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Password requirements appear only after submission | State requirements beforehand; allow password managers and paste | State the unmet requirement without restarting registration |
| Existing account uses another sign-in method | Provide clear options without exposing account existence to strangers | Offer a safe account-recovery or support path |
| Social sign-in popup is blocked, cancelled, or loses destination | Test mobile browser redirect and return flows | Retry or choose another approved method with journey state retained |
| Verification code is delayed, expired, or mistyped | Explain delivery, expiry, and resend limits | Resend or restart safely; make old-code state clear |
| Repeated failures lock the account unexpectedly | Explain limits in non-revealing terms | Provide a verified unlock or support path |

## Password recovery and session expiry

Success: the rightful account holder regains access without account disclosure.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Reset link expires, is reused, or fails on mobile | Single-use, time-limited links tested on supported devices | Request a fresh link without exposing tokens |
| Recovery message does not arrive | Neutral confirmation and clear delivery expectations | Bounded resend and support route without account enumeration |
| New password fails after reset token is consumed | Explain requirements and token lifecycle before submit | Provide safe restart of recovery rather than a dead end |
| Session expires during a long task | Warn where appropriate and preserve non-sensitive progress | Re-authenticate and restore only permissible state |
| Action looks complete after session loss | Check authentication and actual operation status | Verify whether the action occurred before retrying |

## Navigation and responsive layout

Success: users find and complete tasks without losing their place.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Primary action is hidden in a mobile menu | Prioritize common tasks and test with real content | Provide a clear route back with state preserved |
| Modal or side panel hides its own close control | Test narrow, tall, zoomed, and keyboard-open states | Reachable close/back action with focus restored |
| SPA deep link or refresh fails | Configure server fallback and test direct routes | Useful not-found route and safe path home |
| Login or redirect loses the intended destination | Preserve destination and location cues | Resume at the last safe step |
| Page or element overflows both axes unexpectedly | Reflow ordinary content; contain necessary two-axis scrolling locally | Alternative view or explicit scroll cues without losing context |

## Search, filters, sorting, and pagination

Success: users find the correct item and understand the result set.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Empty results provide no explanation | Show query, active filters, and useful empty state | Edit query, clear filters, or browse all |
| Dynamic requests race or overload a slow connection | Debounce where appropriate and ignore stale responses | Retain usable results with freshness notice and retry |
| Mobile filter panel silently applies or loses selections | Show selections, counts, Apply, and Reset | Reopen with selections retained and one-action reset |
| Sort changes unexpectedly across pages | Show active sort and persist it | Restore previous position and ordering |
| Pagination loses query or selected record | Keep URL/state consistent where appropriate | Return to previous results and selection |

## Tables, lists, and row actions

Success: users understand records and act on the intended one.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Mobile view hides decision-critical columns | Prioritize fields; use tested cards, detail view, or local scrolling | Full record details with identity preserved |
| Icon-only row action is ambiguous | Accessible action names and clear row association | Confirm affected record before consequential changes |
| Row moves or disappears after action | Stable pending state and explicit outcome | Activity/status record, safe refresh, or undo where possible |
| Bulk action includes hidden or stale selection | Show count, scope, and affected records | Confirm before action; report partial results for targeted correction |
| Stale record makes an action invalid | Show freshness; recheck state and permission server-side | Explain change and refresh row while preserving location |
| Assistive users lose header/row relationships | Semantic tables or equivalent labelled card structure | Accessible alternate view without relying on proximity |

## Uploads, downloads, camera, and KYC

Success: acceptable evidence or documents transfer safely and their status is understood.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Type, size, or count rejected after a long upload | State limits early and enforce them server-side | Replace only affected file while retaining journey state |
| Upload stalls or connection drops | Visible progress and truthful resumability claims | Resume if supported; otherwise safe retry without duplicates |
| File received but processing or scanning fails | Separate received from ready; validate and scan before use | Replace or escalate with clear processing status |
| Download is blank, expired, or hard to find on mobile | Clear filename, format, availability, and download action | Regenerate or re-request; explain save location if known |
| Camera permission denied, unavailable, or unsupported | Explain need before prompt and check secure-context/device support | File-selection or another approved route, plus permission guidance |
| Captured image is blurred, cropped, or dark | Capture guidance and review before submit | Retake without restarting KYC |
| Camera fails after permission is granted | Handle hardware and browser errors separately | Retry, switch device, or upload alternative |
| KYC status is silent or generic | Distinguish received, pending, accepted, rejected, action needed | State the next approved step and retain case reference |
| Sensitive evidence leaks into drafts, URLs, or logs | Minimize retention, secure storage, and access | Follow incident process and safe resubmission guidance |

## Notifications, alerts, and progress

Success: users understand the outcome and what action, if any, is needed.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Meaning depends only on color or icon | Text labels such as Information, Correction needed, or Unable to complete; accessible announcement | Restate in persistent accessible page context |
| Toast disappears before it can be read | Use brief toasts only for low-stakes confirmation; keep important guidance visible | Message history, error summary, or persistent page notice |
| Form error exists only in a top-right toast | Field-level message and summary for long forms | Focus or link the affected field; preserve entries |
| User correction is mistaken for service failure, or vice versa | Classify by cause and required action, not color or status code alone | State whether to correct, retry, check status, or contact support |
| Repeated alerts compete or interrupt | Prioritize, group, and deduplicate announcements | Review history and dismiss non-critical messages |
| Progress claims done before background work completes | Distinguish submitted, processing, completed, and failed | Status lookup and truthful next step |

## Networks, offline operation, and retries

Success: the journey remains understandable and data-safe on unreliable connections.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Indefinite spinner on a slow network | Bounded waits and visible state | Explain delay, preserve work, retry or check status |
| Connectivity drops during entry or submission | Save permissible drafts; never imply success before confirmation | Restore draft; verify whether submission succeeded before retry |
| Cached content appears current | Show freshness and last verified update | Refresh when online; warn before high-stakes action on stale data |
| Retry duplicates shipment, order, or payment | Server-side operation identity and safe retry design | Find original outcome before a new transaction |
| Work is assumed to continue after browser closes | Promise background completion only when actually supported | Server-side status or explicit manual resume |

## Email, SMS, push, and in-app communications

Success: the intended person receives an understandable message and can act on it safely.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Message is delayed, blocked, or sent to an outdated address | Verify contact route where appropriate and show delivery expectations | Bounded resend, contact correction, or alternate approved channel |
| Message links expire before use | State validity and provide a clear path to request a new link | Regenerate safely without exposing private account status |
| In-app and external messages disagree about status | Use one authoritative state and event mapping | Correct the stale message and provide status lookup |
| Push notification is disabled or unsupported | Do not rely on push as the sole route for essential information | In-app status/history and another consented channel |
| Sensitive details appear on a lock screen or shared device | Minimize notification content and honor privacy preferences | Direct users to a secure authenticated view |

## Real-time updates and long-running work

Success: users see a truthful state for work that changes after an initial request.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Live connection disconnects and status freezes | Detect disconnect and show last-update time | Reconnect or fetch authoritative current status |
| Background job fails after the page reports success | Separate accepted from completed states and monitor jobs | Explain failure and retry/escalate without duplicating the original action |
| Two tabs or users edit the same record | Version or conflict detection where appropriate | Show the conflicting changes and require informed resolution |
| Progress indicator advances without real progress | Derive progress from meaningful work stages | Switch to honest indeterminate or delayed state with status lookup |

## Help, onboarding, and account support

Success: users understand how to proceed without needing technical knowledge.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| First-use terms or steps assume prior technical knowledge | Plain-language task guidance at the point of need | Contextual help, examples, or a human support route |
| Help content is outdated or contradicts the current interface | Link help updates to feature/release changes | Surface current instructions and report content drift |
| A user is trapped in a support loop with no case state | Provide a reference and expected response path | Escalate to a person or alternate channel with context preserved |

## APIs, third parties, and generated documents

Success: connected systems agree on contracts and complete the user journey, or expose a truthful recoverable state.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Frontend payload no longer meets backend contract | Contract tests, consumer map, compatible evolution | Retain user data, show safe correction, and raise drift alert |
| Response field changes and a page crashes | Validate expected structure and handle optional data deliberately | Bounded fallback state and retry/support route; alert owners |
| Backend request fields, validation, or response shape change without consumer rollout | Versioned contract checks and consumer-impact review across every affected app | Preserve work, show a truthful bounded state, and coordinate compatible rollout or rollback |
| Third-party SDK or API upgrade changes outgoing fields, response shape, semantics, or error codes | Review release changes, pin/test upgrades, and verify request/response contracts in staging | Roll back or adapt the integration; keep affected journeys in an honest pending or unavailable state |
| Third-party response is syntactically valid but semantically different | Check required invariants and business outcome, not just HTTP status or schema | Quarantine uncertain result, reconcile with provider, and notify operators before repeating effects |
| Business failure is returned as HTTP success | Explicit outcome semantics and end-to-end tests | Display actual outcome, never false success |
| Auth, permission, validation, and outage all become generic error | Stable error categories and safe user messages | Correct next action: sign in, fix input, request access, retry, or support |
| Provider is slow, offline, or in maintenance | Timeouts, monitoring, bounded safe retries, and realistic status | Queue/defer only if supported; show pending and escalation |
| Provider succeeds but app loses confirmation | Operation IDs and reconciliation | Check authoritative result before retry or charge |
| PDF generation fails after a shipment is created | Separate shipment state from document readiness; retryable job | Keep shipment/tracking ID; show document pending and retry/escalate |
| Multi-step provider operation partly succeeds | Define boundaries and compensation | Reconcile partial state and explain what remains |
| Provider changes format or credential expires | Monitor contracts and credential health without reading values | Fail safely, alert operators, and offer approved delayed/alternate path |

## Payments and high-stakes actions

Success: exactly the intended transaction occurs with a trustworthy result.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Payment succeeds but page says it failed | Verify authoritative transaction state, not browser return alone | Reconcile before asking for another payment; status/receipt lookup |
| Duplicate tap or retry causes duplicate charge | UI pending state and server-side transaction identity | Identify duplicates and follow documented refund/correction process |
| Amount, currency, fee, or terms change unexpectedly | Clear final review with explicit currency and total | Stop and allow renewed review before commitment |
| Browser closes during processing | Durable server-side state and return path | Show verified pending, success, or failure on return |
| Destructive action looks harmless | Clear action labels and affected-record confirmation | Undo where safe; otherwise honest restoration/support route |

## Dates, money, locations, and language

Success: users and system interpret the same facts.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Date or time uses ambiguous format or timezone | Unambiguous display, timezone, and conversion tests | Review/correct before deadline or booking commitment |
| Decimal separator or unit is misread | Explicit units and locale-aware examples/parsing | Identify ambiguity and ask for confirmation |
| Indicative price is presented as final | Label estimate, currency, effective time, and exclusions | Recalculate or obtain verified quote before payment |
| Address autocomplete selects wrong location | Show full selected address and review for consequential deliveries | Manual entry and correction without restarting |
| Translation is clipped or changes action meaning | Test real localized copy and long text on mobile | Safe fallback language and defect report |

## Accessibility, browser support, security, and trust

Success: the essential journey works for supported users, devices, and assistive methods without unsafe disclosure.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Zoom or large text hides action or forces page-wide two-axis scroll | Reflow and enlargement testing | Usable alternate presentation without losing function |
| Touch targets are too small or adjacent | Test tap size and spacing on devices | Distinguishable actions and correction for mistaken tap |
| Keyboard or screen reader cannot operate panel, modal, or table action | Focus management, labels, reading order, assistive testing | Restore focus and alternate accessible route |
| Supported browser lacks needed feature | Feature detection and actual browser matrix | Alternative path or precise compatibility explanation |
| Motion, color, or contrast obscures feedback | Text with color, readable contrast, reduced-motion support | Static readable equivalent |
| Sensitive information appears in logs, URLs, or notices | Minimize collection and exposure by design | Incident process and safe remediation |
| Shared-device session remains open | Clear sign-out and suitable session controls | Authorized session revocation |
| Suspicious support link or impersonation confuses user | Consistent verified channels and in-product guidance | Known official route and fraud escalation |
| Permission prompt appears without context | Request only when needed and explain purpose | Respect denial and provide alternate route |

## Source standards and review boundary

Use [W3C form validation](https://www.w3.org/WAI/tutorials/forms/validation/), [reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html), [status messages](https://www.w3.org/WAI/WCAG21/Understanding/status-messages), and [data-table guidance](https://www.w3.org/WAI/tutorials/tables/) for relevant accessibility checks. Use [OWASP authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [password recovery](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html), and [file upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) guidance for relevant security constraints. These are references, not automatic proof of conformance. Browser support, offline capability, and safe retries require product-specific verification.
