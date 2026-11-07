# Feature FARS Record

Store this record in the affected repository directory of the product's central context. Link shared contracts, business rules, and affected consumers rather than duplicating them. Use one record per meaningful feature or integration; adapt the depth to its risk.

| Field | Verified or proposed detail |
| --- | --- |
| Feature, success objective, audience, and user journey | `<GOAL_AND_AUDIENCE>` |
| Relevant generic FARS capabilities and product-specific additions | `<CAPABILITIES_AND_EXTRA_RISKS>` |
| Owning repository and specialist | `<REPOSITORY_AND_OWNER>` |
| Source revision and environment | `<COMMIT_AND_VERIFIED_ENVIRONMENT>` |
| Dependencies and affected consumers | `<PROVIDERS_PACKAGES_APIS_AND_APPS>` |
| Status | `Proposed / Implemented / Verified / Released` |

## Success path

| Preconditions and valid input | Steps and state changes | Expected output | Verification evidence |
| --- | --- | --- | --- |
| `<PRECONDITIONS>` | `<STEPS>` | `<OUTCOME>` | `<TEST_OR_OBSERVATION>` |

## Actor, state, and next-action map

Use the **2A system (Actors and Actions)**: list every real actor and every approved business-required action in the process, then distinguish the actions indispensable to the stated success point from actions available after it. Design a guided flow where the next required step is obvious at the right moment, without unnecessary detours. A pending action owned by someone else should show an honest waiting state, not a dead button. Test primary-action visibility on mobile web, desktop web, and native mobile where supported. Every mapped action needs proportionate implementation and verification, including post-success actions; key actions deserve extra success-path scrutiny.

| Current state | Responsible actor | Action and classification: key / other pre-success / post-success | Prerequisite or business condition | Visible next action or waiting status | Interface, test evidence, and gap |
| --- | --- | --- | --- | --- | --- |
| `<STATE>` | `<VERIFIED_ACTOR>` | `<BUSINESS_REQUIRED_ACTION_AND_CLASS>` | `<VERIFIED_RULE_AND_SOURCE>` | `<ACTION_OR_WAITING_EXPLANATION>` | `<WEB_MOBILE_WEB_NATIVE_AND_TEST>` |

Specify whether the success point is an intermediate state (for example, a shipment draft) or the completed business outcome (for example, a paid booking). For each actor, confirm that all mapped actions—including viewing or downloading documents after booking—remain discoverable, permitted, and tested without misclassifying them as booking prerequisites.

## Conditional validation and customer guidance

| Producer rule and revision | Triggering condition | Affected consumer and step | Early customer-safe requirement | Server error ID and field key | Clear message, locale, and recovery | Contract test or gap |
| --- | --- | --- | --- | --- | --- | --- |
| `<BUSINESS_RULE_AND_API_REVISION>` | `<WHEN_REQUIRED>` | `<APP_AND_STEP>` | `<WHAT_IS_SHOWN_BEFORE_SUBMIT>` | `<STABLE_CODE_AND_FIELD>` | `<MESSAGE_AND_NEXT_ACTION>` | `<EVIDENCE_OR_GAP>` |

The backend remains authoritative. Do not copy secret or privileged conditions to a client. For nested fields, verify that the customer-facing one-based box/item labels match the form; keep raw array paths internal. Separate corrections from service failures and show whether the operation completed, is pending, or remains uncertain.

## Failure, avoidance, and recovery paths

| Stable failure ID, source, and failure/frustration point | Avoidance and responsible component | Actual failure behaviour and preserved state | Safe recovery or escalation | User guidance | Test or observation | Status, owner, and next action |
| --- | --- | --- | --- | --- | --- | --- |
| `<FARS-ID; USER_PROVIDER_PACKAGE_INFRASTRUCTURE; CREDIBLE_FAILURE>` | `<PREVENTION_OR_INFEASIBLE; COMPONENT>` | `<ERROR_AND_STATE>` | `<RETRY_FALLBACK_OR_MANUAL_PATH>` | `<ACTIONABLE_SAFE_MESSAGE>` | `<TEST_OR_GAP>` | `<VERIFIED_PRESENT_UNVERIFIED_MISSING_PLANNED_UNSUPPORTED; OWNER; ACTION>` |

For an API or third-party contract risk, link the product's API–Consumer Compatibility Map and any Consumer Impact Alert. Record the producer and consumer, request and response fields or schema versions affected, old versus new behaviour, dependency version or upgrade, source revisions, affected journeys, compatibility tests, and rollback or migration. Do not copy private payloads or secrets into this record.

For existing journeys, record whether each relevant avoidance and recovery is `Verified`, `Present but unverified`, `Missing`, or `Not applicable`. Link an approved follow-up for missing controls; do not imply an audit authorized implementation. Note mobile viewport, keyboard, network, browser, accessibility, and affected API/third-party evidence where relevant.

## Usability review and score

| Samuel review stage | Decision to approve or decline | Journeys and representative users tested | Score, coverage, confidence, and blockers | Evidence or follow-up |
| --- | --- | --- | --- | --- |
| Before implementation / after implementation / retrospective | `<HUMAN_DECISION>` | `<JOURNEYS_USERS_DEVICES>` | `<SCORE_OR_NOT_YET_SCOREABLE; COVERAGE; CONFIDENCE; BLOCKERS>` | `<OBSERVATIONS_AND_ACTIONS>` |

If a score describes only part of the application, label it a journey or coverage-limited score rather than an overall application score. Do not average untested journeys into a claimed whole-application result. For a valid application-wide score, record the overall score, lowest assessed section score, all sections below 90, journey/section weights, tested coverage, confidence, and every unresolved blocker. Keep an accepted low-score risk in the calculation and visible until retested; an acceptance to continue QA is not a usability pass or release approval.

| Accepted low-score risk | Affected score and section | Reason and customer impact | Mitigation and owner | Reassessment date and evidence | QA continuation decision | Release decision |
| --- | --- | --- | --- | --- | --- | --- |
| `<RISK_ID>` | `<SCORE_AND_SECTION>` | `<WHY_AND_IMPACT>` | `<MITIGATION_AND_OWNER>` | `<DATE_AND_RECORD>` | `<APPROVED_OR_NOT>` | `<SEPARATE_RELEASE_STATUS>` |

## Operational and continuity notes

- Monitoring or alert and responsible operator: `<SIGNAL_AND_OWNER_OR_NOT_APPLICABLE>`
- Duplicate/partial-work protection and retry limits: `<EVIDENCE_OR_NOT_APPLICABLE>`
- Affected contracts, documents, and `CHANGELOG.md`: `<LINKS_OR_REASON_NOT_APPLICABLE>`
- Accepted gaps, impact, mitigation, decision owner, and next action: `<DETAILS_OR_NONE>`
- Last checked repository revision and context PR: `<REVISION_AND_PR_STATUS>`

Never put protected environment values, credentials, private customer data, or raw third-party responses in this record. Separate verified behaviour from intended behaviour and retain decision history when a recovery design changes.

## Linked business planning record

Reference the PRD and agreed 2A IDs and versions, plus the [simple planning FARS](../planning/fars.md). This record holds engineering evidence; it does not replace the business form. Use identical finding IDs, link approval/provenance and 2A conflict decisions, and distinguish proposed recovery from implemented and verified controls.
