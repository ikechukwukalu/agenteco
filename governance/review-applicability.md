# Review Applicability by Work Impact

Determine review applicability from the **changed behaviour and affected audience**, not the selected specialist's name. Record the decision in the task and PR handoff before asking the human to approve or decline an optional review. Never invoke Samuel or Armstrong automatically. This rule does not waive a separately mandatory design, security, localization, UAT, CI, or release gate.

| Work impact | Samuel FARS usability decision | Armstrong independent QA decision |
| --- | --- | --- |
| Materially changes a customer, partner, staff, or operator journey, including error guidance, forms, or essential next actions | Offer before- and after-implementation review; record each approval or decline | Offer when code or behaviour is testable; record approval or decline before implementation PR |
| Backend, SDK, workflow, or API change with no direct UI but a credible effect on a user journey | Offer a scoped Samuel review of the affected journey or explain why no user-facing impact exists | Offer for testable behaviour, including API contracts, recovery, and deployment automation |
| Testable code or operational behaviour without a user-facing journey | Record why Samuel is not applicable; do not invent a usability score | Offer and record the human decision before implementation PR |
| Documentation-only analysis, context reconciliation, planning, or advice with no testable behaviour | Record both reviews as not applicable with a brief reason; follow any separately required editorial or approval gate | No Armstrong checkpoint merely because an Engineering Manager or other specialist handled the task |

An agent must not disguise a code, workflow, or customer-journey change as documentation-only to avoid review. When impact is uncertain, inspect the affected contracts, consumers, and journey, then ask only the necessary clarification. An approved specialist review may reveal a wider impact; if scope changes materially, return to the implementation authorization gate. The implementing specialist still runs proportionate checks for the work it owns; those checks are not Armstrong's independent QA.

If Samuel's review is approved and reports an unsuitable or unscoreable critical journey, follow [FARS scoring](../rules/fars-usability-scoring.md). A human may accept a recorded risk to continue diagnostic QA but cannot turn an unsuitable score into a pass or bypass a separate release gate. If Armstrong is declined, report the lack of independent QA accurately. If either review is not applicable, do not present the absence as a decline or as completed review.
