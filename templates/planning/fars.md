# FARS review template

Failure and frustration, avoidance, recovery and success

Review each action in the 2A document. Identify what could go wrong, how to prevent it and how people can recover. Keep entries short and practical.

| Document details | Entry | Document details | Entry |
| --- | --- | --- | --- |
| Document name |  | FARS document reference |  |
| Related 2A document reference |  | Related 2A document link |  |
| Document owner |  | Last reviewed |  |
| Version |  | Status | Draft |
| Related PRD name |  | Related PRD reference |  |
| PRD version |  | PRD link |  |


The related 2A document reference is its main document ID. Keep it unchanged across both documents. Each action retains its 2A reference; each FARS finding receives a unique reference.

## Action review

Repeat this section for every action, including optional actions. If no meaningful risk is identified, write “Reviewed — no material risk identified.”

| Actor name and reference | Action name and reference | Related success point references |
| --- | --- | --- |
|  |  |  |


| No. | FARS reference | Possible failure or frustration | Avoidance | Recovery | How to verify |
| --- | --- | --- | --- | --- | --- |
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |


### What to enter

Failure or frustration: What could go wrong, confuse someone or stop progress?
Avoidance: What can prevent or reduce the problem?
Recovery: How can the person continue, and what should they be told?
How to verify: What should QA test and expect? Add the result or evidence when tested.

Treat proposed measures as proposals until agreed. Keep references stable when names or row order change.


## Contribution and review notes

Related 2A version:

Date created:

For each finding reference, record its source (human-provided, agent-proposed or joint), approval reference/date, control status (proposed, implemented or verified) and any linked 2A conflict or recovery-feature requirement. Display agent proposals for approval before adding them to the agreed review. Link engineering test evidence when available; a proposed check is not a passed test.

# Example action review

Illustrative example only. The proposed behaviour below must be agreed for the actual product.

| Actor | Action | Connection to 2A |
| --- | --- | --- |
| Customer | Create receiver’s address | Use the actor, action and success-point references from the related 2A document. |


| No. | FARS reference | Possible failure or frustration | Avoidance | Recovery | How to verify |
| --- | --- | --- | --- | --- | --- |
| 1 | FARS-001 | Address suggestions are unavailable, blocking entry. | Offer manual entry alongside suggestions, if agreed. | Keep entered details and explain how to continue manually. | Make suggestions unavailable. Confirm the customer can save a valid address without losing entered details. |
| 2 | FARS-002 | The customer misses a required field and does not understand why saving failed. | Clearly identify required fields before submission. | Highlight the missing field, explain what is needed and retain other entries. | Leave a required field empty. Confirm the message is clear and the customer can correct it and continue. |


These entries describe proposed prevention, recovery and checks. They do not claim that controls are implemented or tests have passed.
