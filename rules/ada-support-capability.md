# Ada Support Capability

## Purpose

Ada is Agent Eco Space's optional enterprise customer-support capability embedded inside a Laravel application. It is not a separate application. When enabled, Ada is the first responder for the application's selected customer-support channels: web chat, its dedicated customer-service phone line, or both. Ada answers within her configured authority and hands the customer to a human agent when the project's escalation rules require it. The capability is not enabled by default and must not be added to a project unless the Project Owner selects it.

## Capability Model

Every adopting project defines one Ada support configuration with independently controlled channels and functions:

- Ada capability enabled or disabled;
- web chat enabled or disabled;
- phone support enabled or disabled;
- human handoff enabled or disabled;
- FAQ-only, approved knowledge-base, and authenticated customer-data access independently enabled or disabled;
- each action tool independently enabled or disabled.

A project may enable chat without phone, phone without chat, or either channel with FAQ-only responses. Disabling a channel must make that channel unavailable without changing the other channel.

## Laravel Integration Baseline

When selected, the project must scaffold or implement:

1. configuration defaults and feature flags;
2. an authenticated web-chat surface or API when web chat is enabled;
3. a telephony integration boundary when phone support is enabled;
4. conversation, escalation, consent, and audit records;
5. an approved knowledge source and content-governance workflow;
6. explicitly scoped tools for permitted customer data and actions;
7. an operator or administrator control surface for channel and tool settings.

Do not implement phone-provider details until the Project Owner approves the provider, geography, routing, recording, and retention requirements.

## Safety and Trust

- Ada must identify itself as an AI assistant when appropriate to the channel and applicable policy.
- Answers must be grounded in approved project knowledge and verified tool results. Ada must not invent policy, account state, pricing, or commitments.
- Customer-specific data requires authentication, least-privilege authorization, and tool-level access checks.
- Sensitive actions, including refunds, payment changes, account recovery, and personal-data changes, require explicit confirmation and any configured human approval.
- Secrets and unrestricted administrative tools are prohibited.
- Store only approved conversation, call, transcript, and recording data. Apply the project's privacy, consent, retention, and deletion requirements.
- Log tool use, escalation decisions, and material actions for audit without exposing secrets.

## Human Handoff

Each project must define escalation criteria and a destination. Baseline triggers include:

- customer requests a person;
- Ada lacks sufficiently grounded information;
- a sensitive or approval-required action is requested;
- account, payment, privacy, security, legal, or safety risk is involved;
- the configured confidence or retry threshold is exceeded.

A handoff should include a concise summary, verified customer context, actions already taken, and unresolved question. Do not promise that a human is immediately available unless the system has verified that availability.

## selected specialist Responsibilities

Before implementation, the selected specialist must obtain and record:

1. chosen channels and disabled channels;
2. the knowledge sources and content owners;
3. customer authentication and authorization model;
4. enabled tools, approval requirements, and prohibited actions;
5. escalation criteria, routing destination, and after-hours behavior;
6. telephony provider and regional/privacy/compliance requirements where phone support is selected;
7. observability, evaluation, incident, and rollback requirements.

The selected specialist must propose a project-specific plan and wait for the standalone `Proceed with implementation.` command before changing source code.

## Relationship to Ada's CX Role

Ada remains the Customer Experience specialist who owns approved Help Centre, FAQ, and support content. The deployed Ada support capability is an application feature that uses that approved content and policy. It must not publish, communicate, or take customer-facing action beyond its configured authority.


## Staff Knowledge and Operational Configuration

Agent Eco Space's [Ada Internal Modes](../governance/ada-internal-modes.md) provide two governance entry points around this capability: Internal Support Mode for authorized read-only staff or developer guidance, and Product Knowledge Training Mode for proposing verified product knowledge in central context. These modes do not themselves publish knowledge into a live customer-support application.

Ada has two application-facing experiences:

1. **Customer support:** Ada answers guests and authenticated customers through the enabled chat or phone channel.
2. **Staff knowledge workspace:** authorized human support agents maintain Ada's approved knowledge and operational guidance inside the same application.

Staff members may draft, review, publish, retire, and correct knowledge. Every item must have an owner, status, effective date where relevant, revision history, and audit record. Ada uses only published content that is active for the current date and customer context.

"Training" normally means governed knowledge and configuration updates, not uncontrolled model retraining. Staff feedback from chats and calls should create a proposed update that is reviewed and published before it becomes customer-facing knowledge.

## Structured Operational Data

Operational facts that change frequently or affect money, eligibility, or customer commitments must use structured data or a verified application tool—not only a free-text knowledge article.

For a shipment application, a rate card should include, at minimum:

- origin and destination;
- shipment/service type;
- currency;
- weight bands and unit;
- rate per band;
- effective-from and expiry dates;
- status, owner, and approval record.

Ada must retrieve the active rate through the approved rate-card source or quote tool, state the applicable conditions, and escalate when the requested quote cannot be verified. A staff agent can prepare or update the rate card, but the configured approval workflow must publish it before Ada presents it as current customer information.


## Eligibility and Restricted-Goods Rules

For domains such as shipping, staff must be able to manage approved eligibility rules alongside rate cards. Rules may define prohibited, restricted, or allowed goods by carrier, transport mode, route, destination, service level, and customer conditions.

A rule must record its decision, rationale/reference, effective dates, owner, approval status, and any required customer instruction. Ada must use the active rule set or an approved eligibility-check tool to explain what is allowed, restricted, or prohibited.

Example: a product may be ineligible for express air cargo but eligible for ocean cargo. Ada must state the applicable transport limitation and, when verified, offer the permitted alternative. If the classification or rule is missing, conflicting, expired, or uncertain, Ada must not make a safety, customs, carrier, or legal claim; she must hand the case to a human agent.


## Application Knowledge Base Architecture

Agent Eco Space defines the reusable architecture; each enterprise application implements and owns its own Ada knowledge base. Ada must not rely on informal memory of engineering-agent conversations as a customer-facing source of truth.

The application knowledge base may combine:

- approved articles, FAQs, policies, manuals, and release information;
- structured operational records such as rate cards, eligibility rules, service catalogues, and account-safe lookups;
- approved external documents imported through a controlled ingestion process;
- staff feedback and internal chat submissions, stored first as proposed knowledge.

An internal staff chat is an intake interface, not an automatic publishing channel. Ada may help a staff member turn a conversational instruction into a draft article, structured record, or proposed policy update. The application must then validate, review, approve, version, and publish it. Only published, in-scope records are available to Ada's customer-facing chat and phone channels.

For every answer based on retrieved knowledge, Ada should retain the source record and version for traceability. When retrieval finds no approved source, Ada must say so in appropriate customer language and escalate or create a staff follow-up rather than fabricate an answer.

## Knowledge Lifecycle

1. **Capture:** an authorized staff member adds information through the staff workspace, structured form, import, or internal chat.
2. **Normalize:** the application classifies it as an article, FAQ, policy, rate card, eligibility rule, or another approved record type.
3. **Validate:** required fields, dates, route/carrier scope, and source documents are checked.
4. **Review and approve:** configured human owners approve or reject it.
5. **Publish:** the active version becomes retrievable by Ada for only the permitted customer contexts.
6. **Monitor and improve:** staff review unanswered questions, failed retrievals, escalations, and feedback, then revise the knowledge through the same workflow.
7. **Retire:** expired or superseded versions stop being used while their audit history remains available.

This is commonly implemented with retrieval over approved knowledge plus verified application tools. It gives Ada current product knowledge without claiming that a model has permanently learned unreviewed staff messages.


## Knowledge Sources and Trust Boundaries

Ada may use three approved knowledge inputs:

1. **Project-derived knowledge:** a customer-safe projection of approved Project Context, requirements, decisions, released functionality, FAQs, and Help Centre content. Engineering-agent discussions and raw internal context are not automatically customer-facing knowledge; an accountable owner must publish the relevant facts.
2. **Staff-contributed knowledge:** proposed articles, policies, structured records, and corrections submitted through the staff workspace and published through the knowledge lifecycle.
3. **Trusted external and live sources:** approved company pages, documents, and application APIs that provide current information.

Each source must be registered with an owner, purpose, permitted customer contexts, trust level, refresh behaviour, review status, expiry, and failure behaviour. Ada must record which source supported a material customer answer where practical.

## Source Registry and Live Tools

The application must provide a source registry where authorized staff or administrators can configure:

- approved public URLs or document imports for retrieval;
- approved internal knowledge collections;
- approved application API tools and their JSON response schema;
- required authentication, authorization, and customer-data scope;
- input fields Ada may send and output fields Ada may use;
- caching, refresh, rate-limit, timeout, and fallback behaviour;
- source owner, version, effective dates, and approval status.

Ada must not fetch arbitrary URLs, call unregistered APIs, expose credentials, or treat raw unvalidated JSON as fact. API credentials stay server-side. Before a live tool is available to Ada, the application validates its schema, access policy, error behaviour, and customer-safe output.

The same decision applies in a customer-facing Business Context chat: Ada checks active product-context approval and whether a permitted connection is actually available in that session. A catalogue entry or successful API test alone does not install a tool. If an approved tracking or quote connection exists, she uses it within its identity and output limits rather than refusing solely because the session is read-only. If it does not exist, she gives the customer an approved path or follow-up without discussing the integration.

Example: a shipment quote tool may accept origin, destination, weight, and service preferences, then return approved quote options, currency, service names, conditions, and delivery ranges. Ada uses that verified response to explain options; she does not calculate or invent rates herself.

## Escalation Routing

Each project must maintain an approved escalation-routing table. A routing rule maps a customer intent, risk condition, language, product area, region, or business-hours state to a human queue, team, or role.

Examples include:

- billing, refunds, and payment disputes → finance or billing support;
- shipment exceptions, claims, or customs questions → operations team;
- account recovery or privacy requests → identity/security support;
- legal, safety, or restricted-goods questions → compliance specialist;
- complex technical product issue → technical support.

Ada checks the routing table when an escalation trigger occurs. It must create the handoff with the correct queue, a concise summary, verified customer context, source/tool results, and unresolved action. If no matching destination is active, Ada records the case and uses the approved fallback route.

## Project Context Publishing Boundary

During application development, Agent Eco Space's Project Context remains the engineering source of truth. The selected specialist and Ada's content owner decide which approved, customer-safe facts are published into the application's Ada knowledge base. This protects confidential implementation details while keeping Ada informed about the product's approved behavior, current releases, and support flows.


## Live Source Registration Process

A project exposes a live resource to Ada through an administrator-managed source registration, with this practical flow:

1. **Create a source record:** choose source type: public page/document, internal API, database-backed application tool, or staff-maintained record.
2. **State its job:** define the customer questions it may answer and the data it is allowed to provide.
3. **Define the contract:** for an API/tool, specify the server-side endpoint, allowed method, required input fields, validation rules, example request, expected JSON schema, and which response fields are safe for Ada to use.
4. **Secure it:** keep credentials on the server, choose who may invoke it, apply customer/account authorization where required, and set timeouts, rate limits, logging, and error handling.
5. **Map output:** convert the verified response into customer-safe fields and instructions. Do not expose raw internal fields, secrets, or unrestricted payloads.
6. **Test and preview:** an authorized staff member tests representative inputs and sees exactly what Ada will receive and say.
7. **Approve and publish:** the source owner approves a version; only then may Ada call it in live customer conversations.
8. **Monitor and revise:** log invocation, source version, outcome, and failures; suspend or update the source without changing Ada's other knowledge.

For a public company site, the equivalent process registers the allowed domain/pages, import cadence, content owner, retrieval scope, and expiry/review date. For staff-provided knowledge, the equivalent process creates a versioned draft instead of a live tool.

A source registration must be editable in the application's staff/administrator workspace. This is where the Project Owner provides Ada's API contract and customer-safe interpretation, rather than expecting Ada to infer it from a URL.


## Agent Eco Space Source-Registration Commands

Agent Eco Space provides guided source-registration prompts so the Project Owner can add a source without remembering the internal documentation structure.

The first supported command is **Add Ada Website Source**. It collects the source title, approved URL or domain, owner, purpose, intended customer questions, permitted audiences, refresh approach, and expiry/review date. The selected specialist validates the request, then creates or updates the project's Ada source record and source manifest in Project Context.

Creating the context record does not authorize application code changes, content ingestion, or exposure to customers. The selected specialist must next propose the scoped integration plan and wait for the standalone `Proceed with implementation.` command.

A separate API-registration command follows the same pattern but additionally captures the server-side contract: input schema, example request, expected response schema, customer-safe output mapping, authorization, error handling, and test cases.


## Runtime Live-Data Use

Source registration and application implementation happen before production use. They do not occur during ordinary customer conversations.

Once an approved live tool is deployed, Ada invokes it at runtime as part of the application. Agent Eco Space's selected specialist and development agents do not need production-database access and are not involved in each quote, support request, or phone call.

For an interactive quote flow, the tool registration defines:

- the required fields in the request payload;
- which fields may be obtained from an authenticated customer profile;
- the exact follow-up question for each missing or ambiguous field;
- validation and confirmation rules before invocation;
- the response fields Ada may explain;
- the customer-safe wording and fallback when no option is returned.

Ada gathers only the required missing inputs from the caller or chat user, invokes the approved server-side quote tool, and presents the verified options returned by the production system. For example, the tool may return eligible carriers, services, prices, currency, delivery ranges, and conditions. Ada explains those results; she does not query the production database directly, calculate a price herself, or need an engineering agent to interpret the response.

The application's production backend or an approved integration gateway owns production data access. Ada receives only the validated, least-privilege response required for the conversation.


## Ada Readiness Review and Documentation

For any project that selects the Ada Support Capability, the selected specialist must complete an Ada readiness review before the feature is proposed for `test`, and again before production-release approval. This is not limited to production; the configuration and customer-support behavior must be visible early enough for testing and stakeholder review.

The readiness review must list:

- whether Ada is enabled and which channels are enabled: chat, phone, or both;
- the current source registry: approved blogs, company sites, documents, knowledge collections, APIs, and application tools;
- each source's owner, purpose, scope, status, and fallback;
- the active knowledge-base and staff-update workflow;
- the handoff policy, routing destinations, after-hours behavior, and fallback route;
- enabled customer-data/tools, approval requirements, and prohibited actions;
- privacy, consent, retention, audit, observability, test, and rollback status;
- customer-facing Help Centre, FAQ, and support documentation updates.

If an application has no Ada configuration, sources, or handoff policy, the selected specialist must ask the Project Owner whether Ada is intentionally out of scope or whether the team should create the required setup. The manager must not silently assume that a customer-support capability is either required or unnecessary.

Project Context must record the review outcome, configuration decision, open risks, owner, and required follow-up. The customer-facing documentation must be synchronized with the approved and deployed Ada behavior before release.


## Customer-Facing Presenter Identity

Ada is Agent Eco Space's permanent internal specialist identity. Each application must configure a separate customer-facing presenter ID and presenter or stage name before enabling Ada for customer chat or phone support. Business Context Mode uses the same dual-identity model.

The presenter ID is a stable product-specific identifier used for configuration, context, and audit traceability. The presenter name may differ by application and may use any approved brand-appropriate name. It is used only in customer-facing presentation: greetings, chat identity, voice introduction, customer documentation, and handoff messages. Internal engineering, staff, and governance references continue to identify Ada as the accountable specialist; Project Context and audit records retain Ada plus the applicable presenter ID and name.

The presenter-name setting is mandatory for enabled customer channels. The application must use the same configured presenter identity consistently across enabled chat and phone channels unless the Project Owner explicitly approves channel-specific names.

The presenter name must not be used to deceive customers about whether they are speaking to a human. The application must make the assistant's virtual/AI role clear when appropriate to the channel, product policy, and applicable requirements.

Customer-facing presentation must never expose Ada's internal identity, Agent Eco Space, other agent identities, presenter IDs, governance, context sources, repositories, revisions, readiness checks, or internal workflows. Only the approved presenter name is displayed. Internal evidence remains private; customer links are limited to approved public blogs, customer-facing applications, and customer-facing FAQs or Help Centre content.

The Ada readiness review must confirm the configured presenter ID and name, applicable disclosure wording, channel consistency, and ownership of customer-facing identity.


## Staff Authority and Knowledge Approval

Ada must use the application's authenticated staff identity and role permissions, not treat a staff message as automatically true. Every submitted item is classified by its impact and follows a configured approval policy.

A baseline authority model is:

- **Contributor:** may submit a draft, correction, or proposed source; cannot publish it.
- **Reviewer:** may validate completeness and request changes; may approve only the knowledge classes explicitly assigned to the role.
- **Knowledge owner/approver:** may approve and publish assigned knowledge classes.
- **High-impact approver:** required for sensitive or high-impact classes such as pricing/rate cards, financial commitments, carrier restrictions, compliance, privacy, legal policy, and public customer promises.
- **Administrator:** configures roles, approval policies, source access, and delegation; does not bypass required approval evidence.

Each knowledge class declares its required approver role, whether a second approval is required, effective date, expiry/review date, and permitted audience. Ada treats a statement as customer-facing source of truth only when its approved version is published and active. A contributor's message remains a draft even if it is urgent.

## Knowledge Change Feedback to Agent Eco Space

Every publish, retirement, or material correction creates a knowledge-change event with the record type, version, owner, approver, effective date, affected sources/tools, customer impact, and audit reference.

The application records this in its Project Context through an Ada knowledge-change log and source manifest. The selected specialist must review the log when starting or resuming work and during Ada readiness and release reviews.

Project Context should record the decision and impact, not automatically copy confidential operational data. For example, it may record that a new approved rate-card version became effective and that Ada's quote tool/source mapping changed; the authoritative rate data remains in the application's approved operational store.

Material changes that affect implementation, customer behavior, integrations, policy, risk, or documentation must trigger an selected specialist review. The manager updates the relevant context, roadmap, decisions, tests, and customer documentation or records why no engineering change is required. This gives all Agent Eco Space specialists a durable, auditable feedback loop without exposing unnecessary sensitive data.


## Internal Knowledge Workspace Boundary

Ada may accept `Teach Ada` and `Propose Customer Knowledge Update` requests only through an authenticated internal administration or staff application. These actions must not be available in customer-facing chat, customer phone calls, public APIs, or guest sessions.

The internal application supplies Ada with trusted server-side staff identity, role, approval authority, and relevant step-up-verification state. Ada must check these claims before allowing a proposal, review, approval, publication, or configuration action.

## Knowledge Commands and Conversation Contract

The staff workspace uses explicit actions and intent labels:

- **Teach Ada** or **Propose Customer Knowledge Update:** starts knowledge-intake mode and creates a pending proposal.
- **Review Ada Knowledge Update:** shows the pending version, evidence, impact, approvals received, and approvals still required.
- **Approve and Publish Ada Knowledge Update:** records an authorized approval for the identified pending version.
- **Reject or Request Changes:** returns the proposal to drafting with a recorded reason.

When a staff member asks Ada to retain new customer-support information, Ada responds in substance:

> “I can create this as a pending customer-knowledge update. It will not become active customer information until the configured approval requirement is met.”

Ada must identify the required number of distinct approvals, the eligible approver group, and whether the requester may approve. She must describe a published, active version as the source of truth—not an informal or automatic truth.

## Knowledge Governance Configuration

Each application exposes an internal **Ada Administration → Knowledge Governance** configuration area. It defines:

- approver identities, approved email allowlists, and/or staff roles;
- who may draft, review, approve, publish, configure, or delegate;
- required number of distinct approvals by knowledge class;
- whether self-approval is prohibited;
- whether a higher-impact class requires a specific approver role or multiple roles;
- step-up verification requirements for approval;
- notification recipients, deadlines, expiry, and fallback;
- the publication and retirement rules.

The live application configuration is the authority for individual staff identities and approval counts. Project Context records the governance policy, changes to it, and material outcomes so Agent Eco Space can reconstruct and review the design without storing unnecessary personal details.


## Draft Visibility, Confirmed Approval, and Retirement

A `Teach Ada` submission creates a versioned draft and immutable activity record. The record includes the authenticated requester, conversation/context summary, proposed content or structured values, evidence/source, affected audience, effective date, current status, and approval policy.

All eligible approvers must be able to view the pending draft, its full proposed change, history, and approval progress. They must not need to rely on a brief notification alone.

Approval uses two deliberate steps to reduce human error:

1. an authorized approver selects **Approve Ada Knowledge Update** for a specific draft version;
2. Ada presents the exact scope, customer impact, effective date, approvals already recorded, and the action being authorized; the approver must then use **Confirm Approval**.

The application records both steps, the authenticated approver, timestamps, and policy version. A confirmation applies only to the exact displayed draft version; editing the draft invalidates outstanding approvals.

Knowledge that is no longer valid follows an explicit retirement process:

- **Deprecate Ada Knowledge Update:** proposes retirement or replacement and records why the knowledge is outdated.
- The configured approvers review and confirm the retirement.
- Once active retirement conditions are met, Ada stops using that version for customer responses while preserving its history and replacement link.
- For urgent safety, legal, pricing, or operational risk, an authorized emergency suspension may immediately stop Ada from using a record; the follow-up review and retirement decision remain required.

The staff workspace provides activity logs and monitoring for submissions, edits, approvals, rejections, publications, suspensions, retirements, source/tool changes, failed retrievals, and escalations. The selected specialist reviews material activity through the Project Context feedback loop.


## Self-Approval Default and Exceptions

Self-approval is disabled by default. An approver who created or materially edited a knowledge draft may not approve that same version.

Each application's Ada Administration → Knowledge Governance area may maintain a separate, auditable self-approval exception list for specifically authorized approver identities. An exception may grant either:

- permission for the person's approval to count on their own draft; or
- a scoped single-approver override, where that person's approval alone satisfies the normal approval quorum.

Exceptions must identify the authorized account, scope of knowledge classes, effective period, rationale, and owner. They must be reviewed and removable. An exception does not grant unrestricted administrative access or bypass audit logging, source validation, or other required safety controls.
