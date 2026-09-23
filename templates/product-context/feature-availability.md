# Feature Availability Catalogue

Evidence is per environment and component. `Merged`, `deployed`, `validated`, `enabled`, and `announced` are separate facts; leave a cell `Unverified` when evidence is missing.

| Feature ID and customer capability | Audience/journey | Required components and contracts | Environment | Per-component branch, commit and artifact | Merge / deployment / validation evidence | Flag or entitlement | Customer-facing state | Owner and last verified |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `<id: feature name>` | `<audience and path>` | `<backend, frontend/mobile/SDK, APIs>` | `test` | `<component: ref>` | `<PR, deploy, test/UAT>` | `<state>` | `Internal testing / Unverified` | `<owner, date>` |
| `<same id>` | `<same audience>` | `<same dependencies>` | `staging` | `<component: ref>` | `<PR, deploy, test/UAT>` | `<state>` | `Staging validation / Unverified` | `<owner, date>` |
| `<same id>` | `<same audience>` | `<same dependencies>` | `production` | `<component: ref>` | `<PR, deploy, journey test, approval>` | `<state>` | `Available to named audience / Not available / Unverified` | `<owner, date>` |

For each feature also record: release or deployment decision, communication approval, linked API–Consumer Compatibility Map rows and alerts, last change and previous state, open dependencies, owner, and next verification action. A production API without a required consumer remains unavailable to that consumer's audience. A direct API can have a different approved audience and dependency set.
