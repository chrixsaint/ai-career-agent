# Temporary Playground

> **Purpose:** This file is a temporary engineering workspace used during implementation. It exists solely to facilitate iterative design reviews, implementation planning, and AI-assisted engineering discussions.

This file is **not** part of the project's permanent documentation.

It is **not** governed by the repository documentation standards.

It is **not** considered a source of truth.

Its contents are expected to change frequently and may be removed entirely once an implementation task is complete.

---

# How This File Is Used

For each implementation task:

1. Draft the implementation specification.
2. Submit the specification to NotebookLM for engineering review.
3. Apply any approved corrections.
4. Implement the code.
5. Verify the implementation.
6. Remove or replace the completed specification with the next implementation task.

This file acts as a temporary collaboration workspace between the developer, AI assistants, and NotebookLM.

---

# Scope

This file may contain:

- Temporary implementation specifications.
- Design alternatives.
- Engineering notes.
- Questions and answers.
- Review feedback.
- Draft interfaces.
- Proposed class structures.
- Temporary code snippets.

This file shall **not** define project architecture, repository standards, coding standards, or other permanent project decisions.

Those responsibilities belong to the official project documentation.

---

# Current Implementation Task

## File

`app/services/collection/base.py`

---

## Objective

Design the provider-independent abstract base class for all job collectors.

This class defines the contract that every job source implementation must follow.

It establishes the foundation of the Job Collection subsystem.

---

## Responsibilities

The BaseCollector shall:

- Define the common collector interface.
- Enforce asynchronous collection.
- Return standardized `RawJobCapture` models.
- Remain completely provider-independent.
- Provide shared logging infrastructure.
- Define the lifecycle expected from every collector.

---

## Out of Scope

The BaseCollector shall **NOT**:

- Call external APIs.
- Parse JSON.
- Parse XML.
- Parse HTML.
- Perform retries.
- Implement rate limiting.
- Handle provider authentication.
- Persist data.
- Score jobs.
- Rank jobs.
- Perform AI reasoning.

These responsibilities belong to protocol collectors or downstream services.

---

## Public Interface

### Properties

- `source_name`
- `source_type`

### Required Methods

- `fetch()`

### Optional Shared Infrastructure

- logger

The implementation should expose the smallest possible public interface while remaining extensible.

---

## Dependencies

The BaseCollector may depend on:

- abc
- logging
- typing
- RawJobCapture
- collection.constants
- collection.exceptions

The BaseCollector shall **NOT** depend on:

- httpx
- BeautifulSoup
- selectolax
- lxml
- aiolimiter
- vendor SDKs
- provider-specific modules

---

## Collector Lifecycle

Every collector should follow the same lifecycle.

```text
fetch()
    │
    ▼
Retrieve external data
    │
    ▼
Validate response
    │
    ▼
Normalize
    │
    ▼
Return list[RawJobCapture]
```

---

## Expected Inheritance

```text
BaseCollector
│
├── APICollector
│      │
│      └── ATSCollector
│
├── FeedCollector
│
└── HTMLCollector
```

Concrete providers inherit from the protocol collectors.

Examples:

- JoobleCollector
- EuraxessCollector
- GreenhouseCollector
- LeverCollector
- AdzunaCollector
- RemoteOKCollector

---

## Definition of Done

The implementation is complete when:

- Every collector can inherit from BaseCollector.
- The class contains no provider-specific logic.
- The interface is stable.
- The abstraction is protocol-independent.
- The implementation aligns with the Job Collection Architecture.
- The design satisfies the project's modularity and provider-independence requirements.

---

# Notes

This file is temporary.

Once `BaseCollector` has been implemented, verified, committed, and pushed:

1. Remove this specification.
2. Replace it with the next implementation task.
3. Repeat the same engineering workflow for the next file.

This document should always contain **exactly one active implementation specification**.
