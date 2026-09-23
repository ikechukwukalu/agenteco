# Ecosystem Context Intake and Refresh

Agent Eco Space uses a two-phase context model: one complete ecosystem intake for durable product understanding, followed by fast repository-scoped loading for ordinary tasks.

## Initial ecosystem intake

The first specialist session for a product, or the first session after adoption without a verified intake record, studies the complete accessible ecosystem before implementation planning. It must understand:

1. product purpose, glossary, architecture, topology, active business rules, and current decisions;
2. every registered repository, its type, purpose, owner, default specialist, delivery mode, and context directory;
3. contracts produced and consumed, including APIs, events, packages, data, authentication, files, queues, and operational dependencies;
4. repository relationships, consumers, handoffs, known drift, risks, releases, and pending outbox records;
5. the current repository's exact scope within that ecosystem.

For products with APIs, the intake also records whether each backend has a current API–Consumer Compatibility baseline. The selected backend specialist initializes the full route and known-consumer baseline; another role records it as missing or partial and recommends that work rather than fabricating backend authority or automatically invoking Chinedu.

The intake is evidence-led. Repository implementation remains authoritative for what exists, while approved central context remains authoritative for intended business meaning. Inaccessible sources and uncertainty are reported rather than filled with assumptions.

The central context records the intake date, context revision, repository revisions or versions reviewed, specialist, coverage, access gaps, and discovered relationships. This record prevents repeated full discovery without hiding staleness.

## Fast task path

After a verified intake, future tasks begin quickly. The specialist loads:

- current product business rules and active decisions;
- the scoped-rule index and only rules applicable to the role, task, repository, audience, and environment;
- the matching role snapshot when available, plus feature-availability rows relevant to the task and its consumers;
- the assigned repository's manifest and exact `context/repositories/<repository-name>/` directory;
- contracts, consumers, producers, handoffs, and decisions directly relevant to the task;
- newer context changes since the last verified intake.
- unresolved Consumer Impact Alerts affecting the assigned repository, regardless of the apparent task type.

The specialist then moves to task clarification and scope as soon as these minimum sources are sufficient. It must not repeatedly reread the whole ecosystem, narrate routine loading, or delay safe work with broad rediscovery.

Other repository context is loaded when a dependency, contract, drift signal, or human-approved ecosystem refresh requires it.

## Sibling-repository awareness

At startup, identify the sibling repositories already known to produce for, consume from, deploy with, or otherwise affect the assigned repository. If knowledge is incomplete or stale, give the human a short, non-blocking choice to refresh it.

Example:

> My full ecosystem understanding was last verified on `<date>` at context revision `<revision>`. `<repositories or context areas>` have changed or remain unverified. Would you like me to study the ecosystem again and update the connection map? I can continue this task within the verified repository scope unless the stale dependency makes that unsafe.

Never start a full refresh automatically. Continue the current task when its verified scope is safe. Make refresh blocking only when stale knowledge could cause an incorrect or unsafe implementation.

## Refresh triggers

Recommend a full ecosystem refresh when any of these applies:

- the configured refresh interval has elapsed;
- the central context has materially changed since the recorded revision;
- a repository was added, removed, renamed, split, or archived;
- a producer, consumer, API, event, package, data, authentication, or deployment contract changed;
- recorded repository revisions are materially behind;
- context drift, an unknown dependency, or a conflicting decision is discovered;
- the human explicitly requests a refresh.

The default reminder interval is 14 days unless the product manifest defines another value. Time alone creates a reminder, not an automatic scan or implementation blocker.

## Reading authority

Business rules and active decisions may always be reread because they define current product meaning. Superseded rules and decisions remain available for history but are loaded only when the task or a conflict requires them.

Checking the small rule index and current feature-availability rows is part of the fast path. Do not reread every rule body or every feature record for an unrelated task.

## Time-conscious communication

Report intake as a compact receipt: ecosystem revision, assigned repository context directory, directly connected repositories, freshness, access gaps, and whether a refresh was offered. Do not dump the downloaded context back to the human. Once scope is safe, begin the task workflow immediately.
