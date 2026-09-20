# Environment Secrets Confidentiality

Agent Eco Space treats values stored in `.env` and every `.env.*` file as confidential, except for the exact `.env.example` template. This protection applies even when a human asks an agent to retrieve or disclose a value.

## Protected files and stores

Protected sources include:

- `.env`;
- every `.env.*` file other than the exact `.env.example` filename, including environment-specific and local variants;
- CI/CD secret variables;
- cloud secret stores, password managers, deployment credentials, and production configuration; and
- terminal process environments when inspecting them would reveal confidential values.

Agents must not read, retrieve, print, quote, summarize, copy, export, transmit, or disclose values from these sources. Do not use commands, scripts, logs, stack traces, diffs, screenshots, or tool output to expose them. A human request such as “What is our Paystack key?” does not override this rule.

An agent may explain where an authorized human can find, create, rotate, or validate a secret. It may inspect safe configuration code, variable names, schemas, and the exact `.env.example` file to understand requirements. It may verify that a required variable is present only through a method that does not reveal its value.

## The `.env.example` exception

`.env.example` is an inspectable and maintainable configuration template. It contains variable names, safe placeholders, and non-sensitive examples only. It must never contain a live credential, token, private key, password, or other secret.

If an apparent real secret is discovered in `.env.example`, do not repeat it. Alert the human, recommend immediate removal and rotation, and record only the exposure category and remediation—not the value.

## Authorized secret insertion

An agent may add or replace a specifically identified secret only when the approved task requires it, the human explicitly authorizes that operation, and the active environment provides a method that does not expose the value in conversation or output. Prefer a secret manager or a human-performed entry over handling plaintext.

Authorization to insert a secret is not authorization to read back, disclose, validate by printing, or inspect unrelated protected values. If the available mechanism would expose a secret, stop and guide the human through the secure step instead.

## Storage and continuity

Secret values must never appear in:

- commits, tracked files, diffs, pull-request bodies, issues, or review comments;
- central context, decisions, contracts, changelogs, documentation, or API examples;
- `.agenteco/outbox/context/` packages;
- test fixtures, generated reports, logs, screenshots, or chat messages.

Context may record only safe metadata: required variable name, purpose, owning system or team, applicable environment, configuration location, rotation expectation, and whether configuration is pending or verified without revealing the value.

Before committing, verify that protected value-bearing files remain untracked and appropriately ignored. If a secret may have been exposed, stop further propagation, alert the human, recommend immediate rotation or revocation, and preserve only sanitized incident evidence.
