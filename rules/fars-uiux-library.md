# FARS UI/UX Capability Library

FARS means **Failure and frustration, Avoidance, Recovery, Success**. This is a reusable design and usability review library for Samuel across web, mobile web, and native mobile. It complements the [2A Actors and Actions map](journey-actions-and-customer-feedback.md), the [platform-specific FARS libraries](README.md), and the [evidence-based scoring rule](fars-usability-scoring.md); it does not replace them. Select relevant entries and add product-specific risks. Do not claim a proposed control is implemented or effective without evidence.

Start from the approved success point and the real actors, actions, permissions, and process states. For each applicable failure, identify a feasible avoidance, a truthful recovery, the responsible component or person, and how a representative user will test it. Design mobile-first for web without treating native mobile and desktop as afterthoughts. A design file or attractive screen alone is not usability evidence.

## Success-point and 2A journey clarity

Success: each actor understands the outcome, the current state, and the next required action at the right moment, without unnecessary detours.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| A key action is hidden behind details, settings, or an unexplained menu | Map all actors and actions; show the state-appropriate primary action where the actor is already working | Return to the same task with a clear action and preserved safe progress |
| The user cannot tell whether they or another actor must act next | Show the responsible actor, waiting state, and expected handoff in plain language | Provide a status check, reminder, or escalation route appropriate to the actor |
| A post-success action is mistaken for a prerequisite or becomes undiscoverable | Separate success-point prerequisites from post-success actions; give the latter a findable home | Link back to the completed record and its available actions |
| The flow assumes an actor has a permission they do not have | Verify roles and conditions against the approved product register | Explain who can act and provide an authorized handoff without exposing private data |

## Information architecture and wayfinding

Success: people can find the right task and know where they are and how to return.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Labels follow internal organization rather than user language | Test task names and grouping with representative users | Offer search, cross-links, and an understandable route from the wrong place |
| Navigation loses the user's location, filters, or task state | Preserve safe state and show location and progress consistently | Restore the prior view and any permissible draft |
| Important information is buried behind competing panels or actions | Prioritize by the current actor's task and progressive disclosure | Provide a clear detail view without hiding the primary task |

## Forms, decisions, and cognitive load

Success: users can provide required information and make informed choices without guessing or restarting.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Required information or a conditional business rule appears only at submission | Explain known requirements when the condition becomes known; align with the authoritative backend rule | Preserve entries, identify the exact field or document, and return to that step |
| Too many choices or technical terms obscure the decision | Group related choices; explain consequences, units, costs, and defaults in plain language | Let the user revise the choice without duplicating or losing work |
| A long wizard gives no progress or safe back path | Show stages and what remains; preserve permissible values | Resume at the last safe stage and explain any unavoidable re-entry |

## Feedback, notifications, and operation state

Success: users know what happened, what is pending, and what to do next.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| A toast vanishes before a consequential message is understood | Keep important guidance near the task, persistent until addressed, and available to assistive technology | Show the same guidance in the record or field summary |
| Color or an icon alone distinguishes correction from a system fault | Use text labels, cause-aware wording, and specific next steps | Restate the issue in accessible plain language and link to the action |
| The interface claims completion while payment, processing, or another actor is still pending | Model submitted, pending, completed, failed, and uncertain states separately | Offer a safe status check and escalation without encouraging duplicate action |

## Error prevention and safe recovery

Success: credible mistakes are prevented where possible and people can recover without avoidable loss.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| A destructive or costly action is easy to trigger by mistake | Clarify consequences and scope; confirm high-impact actions without adding needless friction | Offer undo where safe, or a clear support and remediation path |
| An error message explains a technical cause but not the customer's next step | Translate stable error categories into respectful, actionable guidance | Preserve permissible progress and return to the affected action |
| A retry could duplicate a booking, payment, or upload | Show the existing operation's status before offering another attempt | Check the original outcome and provide only a safe retry or escalation |

## Trust, transparency, and consent

Success: users understand consequential choices and can trust the displayed status and information.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Price, eligibility, delivery promise, or document readiness is implied without evidence | Distinguish estimate from final price, eligibility from approval, and created from ready | Correct the status, explain the gap, and provide a verified next step |
| A permission request or data collection has no clear purpose | Explain need, timing, alternatives, and relevant privacy boundaries before prompting | Offer an approved alternate path or clear permission guidance |
| Design nudges users toward a choice they did not intend | Present material alternatives and consequences fairly | Allow review and correction before commitment where feasible |

## Accessibility and inclusive understanding

Success: supported users can perceive, operate, and understand the journey with their devices and assistive settings.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Text scaling, zoom, or small screens hide a key control or meaning | Check reflow, hierarchy, spacing, and touch targets on representative devices | Provide an equivalent accessible route without losing progress |
| Keyboard or screen-reader users cannot follow focus or status changes | Use semantic controls, visible focus, meaningful names, and announced state | Restore focus to a meaningful location and provide persistent guidance |
| Instructions depend on color, literacy, prior product knowledge, or a single language | Use clear terms, text plus visual cues, examples, and supported localization | Offer understandable help or a supported alternate channel |

## Localization and content consistency

Success: people receive the same truthful meaning across supported languages and channels.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| A translation changes the business meaning or action required | Review terminology and message intent with the approved localization specialists | Correct the wording and point the user to the right action |
| Backend, web, and native apps give contradictory status or correction messages | Use shared error meaning and verify each consumer's rendered text | Show the authoritative current state and fix the inconsistent channel |
| Nested field errors expose array indexes or technical paths | Use the user's one-based labels and visible item or box names | Take the user to the matching field with clear correction guidance |

## Cross-actor handoffs and awareness

Success: a process involving several people continues without silent stalls or unauthorized disclosure.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| One actor completes a step but the next actor is not aware | Define the handoff, recipient, channel, and expected timing in the 2A flow | Make status visible and provide a bounded reminder or escalation |
| An actor sees another person's action but cannot tell whether it is complete | Show trustworthy state, ownership, and last verified update where appropriate | Refresh or check the record and explain what remains uncertain |
| A notification exposes private information to the wrong actor | Apply audience and permission checks before composing or sending | Follow the product's incident process and provide safe corrected guidance |

## Slow, interrupted, and cross-device journeys

Success: the journey remains understandable when network, device, or attention is interrupted.

| Failure or frustration | Candidate avoidance | Candidate recovery |
| --- | --- | --- |
| Indefinite loading leaves users unsure whether an action happened | Show bounded progress and distinguish slow from failed or pending | Preserve work and provide a status check before retry |
| A user leaves and returns on another device or browser | Save only permissible progress and communicate whether it is synced | Restore the last safe state or explain why re-entry is required |
| A third-party step returns the user to the wrong place | Define return states and confirm the provider result before showing success | Re-enter at the correct stage and verify outcome without double submission |

## Verification and continuity

Samuel applies this library before and after implementation **when his review is approved**, without auto-invoking another specialist or weakening mandatory design gates. For each selected risk, link the 2A actor/action and success-point IDs, intended interface and platform, avoidance and recovery design, observed user behavior, evidence, unresolved gap, and owner in the product's FARS record. Include representative users with low technical familiarity, mobile conditions, accessibility needs, and real content where relevant. Distinguish a design hypothesis, implemented control, and observed effective control. Use [FARS usability scoring](fars-usability-scoring.md) only with sufficient evidence; otherwise report `Not yet scoreable`. Armstrong's approved QA verifies mapped actions and risk controls independently; Samuel's score does not substitute for functional tests.
