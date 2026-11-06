# FARS Native Mobile Capability Library

FARS means **Failure and frustration, Avoidance, Recovery, Success**. This is a generic discovery library for native mobile applications. Flutter is a useful implementation context, but specialists must verify iOS and Android behaviour separately. The success point comes from the product's actual user journey; each credible failure needs a feasible avoidance measure, a truthful recovery path, an owner, and evidence in the [feature FARS record](../templates/product-context/feature-paths-and-recovery.md). Select applicable capabilities and add product-specific risks. A candidate below is not an implemented control.

Test on representative devices and OS versions, including interruption, low storage, poor connectivity, accessibility settings, and app upgrades. Operating systems may pause or terminate background work and users may deny permissions. Never promise completion, delivery, or recovery that has not been verified for the supported platforms.

## Launch, update, and app lifecycle

Success: the app opens and returns to a usable, accurate state.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Startup hangs or crashes on older devices | Test supported devices, initialization, and startup time | Safe failure screen, restart guidance, and diagnosable operator signal |
| Upgrade changes local data format or loses a draft | Test migrations and backward-compatible state restoration | Restore last safe state or explain data requiring re-entry |
| App is terminated while backgrounded | Persist only permissible state at lifecycle boundaries | Resume from server truth and safe local draft, never assume unfinished work completed |

## Navigation, deep links, and external intents

Success: the person reaches the intended screen and can resume their task.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Deep link opens wrong or missing screen | Validate routes, authentication, and destination state | Useful fallback destination with intended action retained |
| External payment, maps, share, or browser app is unavailable or cancelled | Check availability and define handoff/return states | Re-enter the original task with operation status verified |
| Back action leaves an unfinished transaction or loses form state | Design platform-appropriate back behaviour and draft policy | Confirm exit where needed; restore permissible draft |
| The next required action is buried in a menu or inaccessible after a state change | Map actor and journey state; present a reachable primary action or clear waiting status | Reopen the correct stage with the task and permissible inputs retained |

## Forms, wizards, and keyboards

Success: valid information is entered and submitted without losing progress.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Keyboard, safe area, or orientation hides field or action | Test small screens, keyboard-open state, rotation, and text scaling | Focus and reveal the exact field without clearing other inputs |
| Validation arrives too late or differs from backend rules | Clear constraints and contract tests; server validation remains authoritative | Preserve entries and show field-specific correction |
| A destination, role, or service choice creates an undisclosed business-rule requirement | Inspect active producer rules and expose customer-safe conditions when known | Retain safe draft, return to the exact step, and explain the required evidence or correction |
| Interruption or process death loses a long wizard | Save safe non-sensitive drafts with lifecycle tests | Restore permissible steps or explain what must be re-entered |
| Repeated submit creates duplicate work | Pending state and server-side operation identity | Check authoritative result before another attempt |

## Registration, sign-in, recovery, and biometrics

Success: the rightful person can access the intended account securely.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Verification code or reset link expires or is not delivered | Explain validity, delivery, and resend limits without account disclosure | Safe resend or alternate approved account-recovery route |
| Session expires during a task | Refresh only where authorised; preserve non-sensitive progress | Re-authenticate then verify action state before retry |
| Biometric check is denied, unavailable, or changed after enrolment | Check device support; retain another approved authentication method | Fall back to that method without locking out the rightful user |
| Login redirects lose the original task | Preserve intended destination safely | Resume at the last valid step after authentication |

## Connectivity, APIs, offline data, and sync

Success: the app communicates and makes local versus server state understandable.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Network drops or request times out | Truthful loading, bounded waits, and safe retry design | Preserve work; determine whether the first request succeeded before repeating |
| Server request or response contract changes | Consumer map, version-aware contract tests, and compatible rollout | Bounded UI fallback, retained safe state, and Consumer Impact Alert |
| Cached data is mistaken for current data | Mark local/offline state and last update | Refresh when connected; block unsafe decisions on stale facts |
| Offline edits conflict with newer server changes | Detect versions and define conflict policy | Present both versions and support informed resolution |
| Retry duplicates a consequential write | Server-side idempotency or status lookup | Reconcile original operation before new transaction |

## Background work and long-running operations

Success: work completes where platform support permits, with truthful progress.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| OS suspends or kills upload, sync, or job | Use supported background mechanisms and durable server-side state | Resume where supported or show pending/failed with next step |
| User closes app during processing | Separate accepted from completed state and persist operation reference | Restore authoritative status on return |
| Background retry runs twice | Bounded retry and operation identity | Reconcile duplicate attempts and preserve one authoritative result |

## Files, media capture, KYC, and downloads

Success: an acceptable file or identity record is transferred and its status is clear.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Large upload stalls, repeats, or exceeds size limits | State limits and progress; validate before and after transfer | Resume if supported or retry safely without losing task state |
| Camera permission is denied or device lacks a camera | Explain purpose at point of use; check capability | Offer approved file selection or alternate verification route |
| Image is blurry, cropped, or in unsupported format | Preview and quality guidance before submission | Retake or replace only affected media |
| KYC processing fails after upload | Distinguish received, pending, accepted, rejected, action required | Preserve case reference and explain correction or escalation |
| PDF download is unavailable or cannot open on device | Verify format, readiness, and compatible viewer path | Re-request document or offer approved alternate access |

## Location, maps, and device permissions

Success: the user supplies an accurate location or grants only the capability needed.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Location permission denied, limited, or inaccurate | Ask only when relevant; confirm selected result | Manual address or map-pin correction |
| Permission was granted before but later revoked | Check current permission when using feature | Explain settings route and offer non-permission alternative |
| Map or geocoding service is unavailable | Do not rely on a single unverified service for essential input | Manual entry and later verification if business rules allow |

## Push, in-app, email, and SMS messages

Success: the user receives a timely, understandable message through an approved channel.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Push permission denied, delivery delayed, or token expired | Never make push the sole source of essential state; maintain token lifecycle | In-app status and another consented route |
| Sensitive notification appears on lock screen | Minimize preview content and respect privacy preference | Open an authenticated detail view instead |
| Message says complete while server still processes | Derive message from authoritative state | Correct status and show next expected step |
| Multiple alerts overwhelm or use color alone | Prioritize and label meaning in words | Accessible notification history and clear action |

## Payments and high-stakes actions

Success: exactly the intended transaction is recorded and confirmed.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Provider charges but app loses confirmation | Durable transaction identity and server-side reconciliation | Verify payment before asking to pay again; show receipt/status |
| App switch to provider is cancelled or return link fails | Test handoff and return on both platforms | Restore original journey and authoritative pending/failure state |
| Duplicate tap or retry charges twice | UI pending state and backend duplicate protection | Identify duplicate and follow refund/correction procedure |
| Amount or currency differs from review screen | Final confirmation with explicit units and total | Stop and require renewed review before payment |

## Search, filters, lists, and record actions

Success: users find and act on the intended record.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Results arrive out of order or filters vanish after app switch | Ignore stale responses and preserve query state | Restore selection, filters, and result position |
| Touch action targets the wrong record | Clear row identity and accessible action labels | Confirm consequential action and offer safe undo or correction |
| Empty or stale list gives no explanation | Show loading, empty, error, and last-updated states distinctly | Refresh or change filters without losing context |

## Accessibility, localization, and device diversity

Success: supported users complete essential journeys on supported devices.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Large text or screen reader hides controls or context | Test text scaling, semantics, reading order, and contrast | Accessible alternate presentation; report unsupported barrier |
| Small touch target or gesture-only action blocks use | Reachable targets and non-gesture alternative | Clear correction path for accidental action |
| Older OS, low memory, or low storage breaks feature | Support matrix and representative device tests | Explain limitation without data loss; offer supported path |
| Translation or locale changes meaning, dates, or currency | Test localized copy, units, and layout | Clarify value and provide safe correction before commitment |

## Privacy, local storage, and account trust

Success: user data remains protected throughout normal and disrupted journeys.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Sensitive data persists on a shared or lost device | Minimize local storage and protect session/data appropriately | Revoke sessions and follow security recovery process |
| Secrets or personal data appear in logs or crash reports | Redaction and access review | Incident handling and data removal/rotation as appropriate |
| User cannot distinguish genuine from suspicious account message | Consistent official channels and in-app guidance | Direct to known official support route and escalate suspected fraud |

## Third-party integrations and generated documents

Success: dependencies complete the user journey or leave a truthful recoverable state.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Provider outage or maintenance interrupts operation | Monitor health, bound timeouts, and design safe pending state | Retry/defer only when supported; explain delay and escalation |
| SDK upgrade changes request, response, or error semantics | Test upgrades against old and new contracts and affected app versions | Roll back, adapt, or stage rollout; report consumer impact |
| Provider succeeds but app loses acknowledgement | Use operation IDs and authoritative reconciliation | Check provider/backend state before repeating effects |
| Document generation fails after core action succeeds | Separate core action from document readiness | Retain reference, show document pending, retry or escalate |

## Source and verification boundary

Mobile background execution and permission delivery differ by platform and version. Verify against [Android background work](https://developer.android.com/develop/background-work), [Apple background execution](https://developer.apple.com/documentation/uikit/preparing-your-ui-to-run-in-the-background), and [Apple notification permission guidance](https://developer.apple.com/documentation/usernotifications/asking-permission-to-use-notifications) as applicable. Apply [Flutter accessibility guidance](https://docs.flutter.dev/ui/accessibility) where Flutter is used. Platform documentation informs candidate controls; product tests establish what is actually supported.
