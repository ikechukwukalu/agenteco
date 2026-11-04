# FARS evidence for an implementation PR

Use this section in the body of every material feature, integration, or behaviour-change PR. Keep it proportional to risk, but do not omit a credible failure merely because a control is missing. Link the full feature-specific record in the product's central context or identify a pending Context Update Package when access is unavailable. Do not paste secrets, protected payloads, or private customer data.

**Success outcome and audience:** `<GOAL_AND_USER>`

| Failure ID and credible failure/frustration | Implemented avoidance or explicit gap | Implemented recovery or explicit gap | Engineer-owned test or observation | Status and affected component |
| --- | --- | --- | --- | --- |
| `<FARS-ID; FAILURE>` | `<CONTROL_AND_EVIDENCE_OR_MISSING>` | `<CONTROL_AND_EVIDENCE_OR_MISSING>` | `<TEST_LINK_OR_GAP>` | `<VERIFIED_PLANNED_UNSUPPORTED; COMPONENT>` |

**Contract/dependency impact:** `<API_CONSUMER_ALERTS; PROVIDER_UPGRADES; REQUEST_RESPONSE_CHANGES; OR_NONE_WITH_REASON>`

**Samuel FARS review:** `<APPROVED_OR_DECLINED; PROVISIONAL_OR_VERIFIED_SCORE_OR_NOT_YET_SCOREABLE; OVERALL; LOWEST_SECTION; ALL_SUB_90_SECTIONS; BLOCKERS; CONTEXT_LINK>`

**Armstrong decision and evidence:** `<APPROVED_OR_DECLINED; INDEPENDENT_FINDINGS_OR_NOT_RUN; DIAGNOSTIC_QA_OVERRIDE_IF_ANY>`

**Accepted usability risk, if any:** `<HUMAN_DECISION; AFFECTED_SCORE; IMPACT; MITIGATION; OWNER; REASSESSMENT_DATE; CONTEXT_LINK>`

**Release boundary:** A low score accepted for continued work or diagnostic QA is not a usability pass, production approval, or merge authorization.
