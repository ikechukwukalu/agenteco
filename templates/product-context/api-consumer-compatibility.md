# API–Consumer Compatibility Map

This product-wide record is initialized by the backend specialist and progressively maintained by every producer and consumer specialist. Replace placeholders with repository evidence and retain historical rows by changing status rather than erasing context.

## Baseline evidence

| Backend/component | Baseline owner | Status | Backend revision | Consumer repositories inspected | Access/coverage gaps | Generated or source evidence | Last verified |
|---|---|---|---|---|---|---|---|
| `<BACKEND>` | `<SPECIALIST>` | `Complete / Partial / Stale` | `<COMMIT>` | `<REPOSITORIES>` | `<GAPS>` | `<ROUTE_LIST_OR_SOURCE>` | `<DATE>` |

## Backend route inventory

| Method | URI | Route name | Controller/handler | Authentication | Middleware | API version | Purpose | Documentation source | Lifecycle | Backend revision |
|---|---|---|---|---|---|---|---|---|---|---|
| `<METHOD>` | `<URI>` | `<NAME>` | `<HANDLER>` | `<AUTH>` | `<MIDDLEWARE>` | `<VERSION>` | `<PURPOSE>` | `<SOURCE>` | `Active / Deprecated / Internal` | `<COMMIT>` |

## Route-to-consumer map

| API route | Consumer application | Repository | Platform | Module/feature | Calling source file | Relationship status | Confidence | Backend revision | Consumer revision | Last verified |
|---|---|---|---|---|---|---|---|---|---|---|
| `<METHOD URI>` | `<APPLICATION>` | `<REPOSITORY>` | `Web / Mobile / SDK / Service / Partner / Third-party` | `<MODULE>` | `<PATH>` | `<STATUS>` | `<CONFIDENCE>` | `<BACKEND_COMMIT>` | `<CONSUMER_COMMIT>` | `<DATE>` |

## Consumer contract expectations

| Consumer | API route | Path/query parameters | Request fields sent | Response fields used | Authentication | Error handling | Pagination/state assumptions | Tests/evidence |
|---|---|---|---|---|---|---|---|---|
| `<CONSUMER>` | `<METHOD URI>` | `<PARAMETERS>` | `<REQUEST>` | `<RESPONSE_DEPENDENCIES>` | `<AUTH>` | `<ERRORS>` | `<ASSUMPTIONS>` | `<TEST_OR_SOURCE>` |

## Form-to-API validation comparison

Record only customer-safe producer requirements; link the authoritative backend rule instead of copying private server logic. Use one row per material requirement or gap, and update affected rows when either revision changes.

| API route and backend revision | Consumer form/module and revision | Backend requirement and condition | Frontend collection, guidance, validation, and rejection handling | Gap and customer impact | Status and owner | Test/evidence | Linked alert |
|---|---|---|---|---|---|---|---|
| `<METHOD_URI_AND_BACKEND_COMMIT>` | `<APP_FORM_SOURCE_AND_COMMIT>` | `<SAFE_REQUIREMENT_AND_TRIGGER>` | `<VISIBLE_INPUT_GUIDANCE_CLIENT_CHECK_SERVER_ERROR_PATH>` | `<MISMATCH_OR_NONE>` | `Verified aligned / Gap open / Correction proposed / Correction in PR / Unverified; <OWNER>` | `<CONTRACT_FORM_AND_ERROR_TEST>` | `<CIA_ID_OR_NONE>` |

## Compatibility and risk register

| Risk ID | API route | Affected consumer | Risk or mismatch | Possible failure | Severity | Evidence | Recommended correction | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|
| `<RISK_ID>` | `<METHOD URI>` | `<CONSUMER>` | `<RISK>` | `<FAILURE>` | `Low / Medium / High / Critical` | `<EVIDENCE>` | `<REMEDIATION>` | `<OWNER>` | `Open / Accepted / Mitigated / Resolved` |

## Consumer Impact Alerts

| Alert ID | Changed API | Previous contract | New contract | Breaking difference or validation gap | Affected consumers and forms | Required updates and owner | Producer state | Per-consumer state and evidence | Target environment/date | Severity | Status and last reminder |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `<CIA_ID>` | `<METHOD URI>` | `<PREVIOUS>` | `<NEW>` | `<DIFFERENCE_OR_GAP>` | `<CONSUMERS_AND_FORMS>` | `<UPDATES_AND_OWNERS>` | `<BRANCH_COMMIT_PR>` | `<PER_CONSUMER_STATUS_REVISION_TEST>` | `<TARGET>` | `<SEVERITY>` | `Open / Open with exception / Resolved; <LAST_CHECKPOINT>` |

## Approved exceptions

| Alert ID | Approved by | Reason | Impact accepted | Duration/expiry | Mitigation | Rollback or recovery | Decision record |
|---|---|---|---|---|---|---|---|
| `<CIA_ID>` | `<HUMAN>` | `<REASON>` | `<IMPACT>` | `<EXPIRY>` | `<MITIGATION>` | `<RECOVERY>` | `<DECISION_LINK>` |
