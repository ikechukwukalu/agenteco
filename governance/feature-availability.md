# Product Feature Availability

## One shared record per customer capability

DTAP products keep a central feature availability catalogue that every specialist can read. Each feature has a stable ID, business name, intended audiences and journey, accountable owner, required repositories or components, related contracts, flags or entitlements, and a row for each relevant environment. Package-only products may use their package release evidence instead.

For every component and environment, record the source branch and commit or artifact, merge state, deployment evidence, test or UAT result, flag state, and last verified time. Distinguish **implemented**, **merged**, **deployed**, **validated**, **enabled for audience**, and **approved for communication**. A branch name or merged pull request proves none of the later states. Test, staging, and production claims require evidence from the actual environment.

The customer availability decision is product-wide: all required producer and consumer components must be deployed and compatible in production, the necessary flag or entitlement must be enabled for the intended audience, the customer journey must be verified, and communication must be approved where required. A production backend API alone does not make a dashboard or mobile feature available. A direct third-party API has its own documented audience, access, contract, SDK or integration dependencies, and release gate.

## Maintenance and communication

- The implementing specialist updates the rows for components they changed and identifies downstream components and consumers. Backend/API changes link the API–Consumer Compatibility Map and unresolved Consumer Impact Alerts. Frontend, mobile, SDK, and partner specialists confirm their own implementation and verification evidence.
- The release or DevOps owner confirms actual deployment, environment, artifact, and rollout state. QA records independent validation. No specialist infers another team's deployment or signs off on its behalf.
- Before describing a feature as available, every specialist checks the shared record and material recent context changes. If evidence is incomplete or contradictory, report the uncertainty to an authorized internal user and request targeted verification. A product-context record is not proof that a currently deployed service still behaves as recorded.
- Ada may discuss test, staging, dependencies, and release readiness with authorized internal staff. In customer-facing mode she describes a capability as available only for an audience whose full production journey is verified and approved for communication. Otherwise she uses approved current-product language and never exposes unreleased plans, internal branches, or repository details.

Corrections preserve the prior state, effective period, evidence, reason, and owner. Never rewrite a feature's history to make a later release look earlier. Use the [catalogue template](../templates/product-context/feature-availability.md) for the shared table.
