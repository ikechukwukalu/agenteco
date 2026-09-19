# Documentation and Continuity

Implementation is incomplete until another authorized specialist can understand what changed, why it changed, how it was verified, and what must happen next.

## Continuity record

For every completed task, update the assigned repository context directory and any affected shared records with:

- task objective and business reason;
- verified before-and-after behaviour;
- implementation approach and significant files or components;
- decisions created, changed, corrected, deprecated, or superseded;
- contracts produced or consumed and affected sibling repositories;
- database, configuration, infrastructure, security, compatibility, and migration effects;
- tests, commands, evidence, and known coverage gaps;
- feature, API, operational, README, migration, and release documentation changed;
- `CHANGELOG.md` entry or an explicit, evidence-based reason it does not apply;
- branch, commit, pull request, release, and source revisions;
- unresolved risks, deferred work, and the clearest next action.

Do not write vague notes such as `feature completed` or duplicate code diffs without explaining their product and contract meaning. Separate verified facts from proposals and uncertainty.

## Feature and API documentation

Backend and frontend specialists must identify the repository's current documentation system before changing documented behaviour. Record, where applicable:

- documentation tool and version;
- configuration and source locations;
- generation or validation command;
- generated or published destination;
- ownership and update workflow;
- last verified revision.

Examples include Knuckles/Scribe for Laravel, OpenAPI or Swagger, Storybook, Compodoc, Typedoc, JSDoc, generated SDK references, or a verified repository-specific system. Examples are not defaults: inspect the repository and use what is actually installed.

When behaviour, contracts, examples, errors, authentication, parameters, responses, components, or user flows change, update the applicable feature and API documentation in the same authorized scope. Generated documentation must be regenerated or validated according to repository policy.

## Changelog

`CHANGELOG.md` is a required release and continuity artefact. Check it during preflight and update it for user-visible changes, contracts, security, compatibility, configuration, migration, deprecation, operational behaviour, fixes, and releases. Preserve the repository's existing format and release convention.

If no changelog entry applies, state why in completion evidence. Do not silently omit the check.

## Cross-repository handoff

When another repository is affected, update the shared contract or handoff record with the producer revision, consumer impact, adoption status, compatibility constraints, and required follow-up. The implementer does not claim the consumer was updated without repository evidence.
