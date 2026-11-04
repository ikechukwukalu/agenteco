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

## Failure, avoidance, and recovery paths

| Source and failure/frustration point | Avoidance and responsible component | Actual failure behaviour and preserved state | Safe recovery or escalation | User guidance | Test or observation | Status, owner, and next action |
| --- | --- | --- | --- | --- | --- | --- |
| `<USER_PROVIDER_PACKAGE_INFRASTRUCTURE; CREDIBLE_FAILURE>` | `<PREVENTION_OR_INFEASIBLE; COMPONENT>` | `<ERROR_AND_STATE>` | `<RETRY_FALLBACK_OR_MANUAL_PATH>` | `<ACTIONABLE_SAFE_MESSAGE>` | `<TEST_OR_GAP>` | `<VERIFIED_PRESENT_UNVERIFIED_MISSING_PLANNED_UNSUPPORTED; OWNER; ACTION>` |

For existing journeys, record whether each relevant avoidance and recovery is `Verified`, `Present but unverified`, `Missing`, or `Not applicable`. Link an approved follow-up for missing controls; do not imply an audit authorized implementation. Note mobile viewport, keyboard, network, browser, accessibility, and affected API/third-party evidence where relevant.

## Usability review and score

| Samuel review stage | Decision to approve or decline | Journeys and representative users tested | Score, coverage, confidence, and blockers | Evidence or follow-up |
| --- | --- | --- | --- | --- |
| Before implementation / after implementation / retrospective | `<HUMAN_DECISION>` | `<JOURNEYS_USERS_DEVICES>` | `<SCORE_OR_NOT_YET_SCOREABLE; COVERAGE; CONFIDENCE; BLOCKERS>` | `<OBSERVATIONS_AND_ACTIONS>` |

If a score describes only part of the application, label it a journey or coverage-limited score rather than an overall application score. Do not average untested journeys into a claimed whole-application result.

## Operational and continuity notes

- Monitoring or alert and responsible operator: `<SIGNAL_AND_OWNER_OR_NOT_APPLICABLE>`
- Duplicate/partial-work protection and retry limits: `<EVIDENCE_OR_NOT_APPLICABLE>`
- Affected contracts, documents, and `CHANGELOG.md`: `<LINKS_OR_REASON_NOT_APPLICABLE>`
- Accepted gaps, impact, mitigation, decision owner, and next action: `<DETAILS_OR_NONE>`
- Last checked repository revision and context PR: `<REVISION_AND_PR_STATUS>`

Never put protected environment values, credentials, private customer data, or raw third-party responses in this record. Separate verified behaviour from intended behaviour and retain decision history when a recovery design changes.
