# Requirements

> **Purpose:** This document defines the functional and non-functional requirements for the AI Career Agent. It serves as the project's functional contract by specifying what the system must do and the qualities it must exhibit.

System design belongs in `ARCHITECTURE.md`.

Technology selection belongs in `technology-stack.md`.

Project planning belongs in `ROADMAP.md`.

---

# Functional Requirements

Functional requirements define the capabilities the system shall provide.

## Job Discovery

### FR-001

The system shall discover job opportunities from multiple sources.

### FR-002

The system shall support collecting jobs from public APIs.

### FR-003

The system shall support collecting jobs from company career pages.

### FR-004

The system shall normalize all collected jobs into a common internal representation.

### FR-005

The system shall detect and remove duplicate job postings.

---

## Job Intelligence

### FR-006

The system shall filter opportunities according to configured career profiles.

### FR-007

The system shall support filtering by location.

### FR-008

The system shall support filtering by employment type.

### FR-009

The system shall rank opportunities according to relevance.

### FR-010

The system shall recommend the most relevant opportunities.

---

## Career Profiles

### FR-011

The system shall support software engineering career profiles.

### FR-012

The system shall support biomedical engineering career profiles.

### FR-013

The system shall support biochemistry career profiles.

### FR-014

The system shall support interdisciplinary career profiles.

---

## Application Assistance

### FR-015

The system shall generate tailored CV recommendations for selected opportunities.

### FR-016

The system shall generate tailored cover letter recommendations.

### FR-017

The system shall require explicit user approval before any application-related action.

---

## Explainability

### FR-018

The system shall explain why an opportunity was recommended.

### FR-019

The system shall present recommendation information in a way that supports user decision-making.

---

# Non-Functional Requirements

Non-functional requirements define the expected qualities of the system.

### NFR-001

The architecture shall be modular.

### NFR-002

The system shall prioritize maintainability.

### NFR-003

The system should prioritize open-source technologies whenever practical.

### NFR-004

The system should minimize operational costs.

### NFR-005

The system shall support adding new job sources with minimal architectural impact.

### NFR-006

The project shall maintain clear and up-to-date documentation.

### NFR-007

The user shall retain final control over every application decision.

---

# Assumptions

The current requirements assume:

- Public job data can be obtained through APIs, company career pages, or other permitted sources.
- AI services are available when application assistance features are enabled.
- The project is initially intended for a single user.
- Career interests may evolve over time.

These assumptions may be revised as the project evolves.

---

# Constraints

The following constraints guide implementation.

- User approval is required before any application is submitted.
- The implementation shall follow repository standards.
- Architecture decisions shall preserve modularity.
- Functional requirements should not depend on specific implementation technologies.
- Requirements should remain implementation-independent.

---

# Scope

This document defines **what** the system must accomplish.

It does **not** define:

- System architecture
- Technology selection
- Source code organization
- Implementation details
- Development schedule

Those responsibilities belong to their respective documents.

---

# Traceability

Every implemented feature should satisfy one or more functional or non-functional requirements.

Requirements should be updated before implementing functionality that changes the expected behavior of the system.

---

# Future Evolution

Requirements should evolve intentionally as project goals change.

New requirements should:

1. Represent genuine user or business needs.
2. Avoid implementation details.
3. Be uniquely identifiable.
4. Preserve backward traceability whenever practical.
