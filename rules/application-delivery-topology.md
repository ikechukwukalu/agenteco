# Application Delivery Topology Declaration

## Purpose

Before planning a new application, the selected specialist must establish how the application delivers its frontend and backend. The team must not assume that Laravel is a full-stack frontend application.

## Mandatory First Question

At startup, before feature planning or implementation, the selected specialist must ask the Project Owner to select the delivery topology:

1. **Full-stack Laravel:** Laravel provides the backend and the customer-facing frontend.
2. **API-core platform:** Laravel provides REST APIs only; one or more separate frontend applications consume those APIs.

If the Project Owner selects API-core platform, the selected specialist must collect and record each frontend interface:

- repository and local directory;
- framework;
- audience and access boundary;
- interface role, such as customer, operations, administration, or partner;
- owner and release relationship;
- API contract/dependency relationship to the Laravel backend.

## Project Context Record

Project Context must contain a platform map that identifies the core backend, every declared interface, and the architecture mode. Optional component context may document repository-specific details, but the platform map remains the cross-repository source of truth.

## Existing Projects

When starting or resuming an existing project, the selected specialist must inspect and reconcile the current topology. If it is not recorded, ask the Project Owner; do not infer full-stack Laravel from the backend framework alone.

## Feature Planning

After topology is declared, every feature plan must identify its affected interfaces and backend/API work. A feature may be delivered to one interface or intentionally replicated across multiple interfaces with role-specific permissions and journeys.

