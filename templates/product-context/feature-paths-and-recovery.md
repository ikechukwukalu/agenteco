# Feature Paths and Recovery Record

Store this record in the affected repository directory of the product's central context. Link shared contracts, business rules, and affected consumers rather than duplicating them. Use one record per meaningful feature or integration; adapt the depth to its risk.

| Field | Verified or proposed detail |
| --- | --- |
| Feature, objective, and user journey | `<GOAL_AND_AUDIENCE>` |
| Owning repository and specialist | `<REPOSITORY_AND_OWNER>` |
| Source revision and environment | `<COMMIT_AND_VERIFIED_ENVIRONMENT>` |
| Dependencies and affected consumers | `<PROVIDERS_PACKAGES_APIS_AND_APPS>` |
| Status | `Proposed / Implemented / Verified / Released` |

## Success path

| Preconditions and valid input | Steps and state changes | Expected output | Verification evidence |
| --- | --- | --- | --- |
| `<PRECONDITIONS>` | `<STEPS>` | `<OUTCOME>` | `<TEST_OR_OBSERVATION>` |

## Failure and recovery paths

| Source | Trigger or failure | System behaviour and preserved state | Safe recovery or escalation | User guidance | Test or evidence | Status and owner |
| --- | --- | --- | --- | --- | --- | --- |
| User / business rule / third party / package / infrastructure | `<CREDIBLE_FAILURE>` | `<ERROR_AND_STATE>` | `<RETRY_FALLBACK_OR_MANUAL_PATH>` | `<ACTIONABLE_SAFE_MESSAGE>` | `<TEST_OR_GAP>` | `<IMPLEMENTED_VERIFIED_PLANNED_UNSUPPORTED; OWNER>` |

## Operational and continuity notes

- Monitoring or alert and responsible operator: `<SIGNAL_AND_OWNER_OR_NOT_APPLICABLE>`
- Duplicate/partial-work protection and retry limits: `<EVIDENCE_OR_NOT_APPLICABLE>`
- Affected contracts, documents, and `CHANGELOG.md`: `<LINKS_OR_REASON_NOT_APPLICABLE>`
- Accepted gaps, impact, mitigation, decision owner, and next action: `<DETAILS_OR_NONE>`
- Last checked repository revision and context PR: `<REVISION_AND_PR_STATUS>`

Never put protected environment values, credentials, private customer data, or raw third-party responses in this record. Separate verified behaviour from intended behaviour and retain decision history when a recovery design changes.
