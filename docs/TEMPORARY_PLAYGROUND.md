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

---

## File

`app/services/collection/models.py`

## Objective

Implement the provider-independent Pydantic models that define the output contract of the Job Collection subsystem.

These models represent the boundary between external job providers and the internal processing pipeline.

Every collector must normalize provider-specific responses into these models before any persistence, duplicate detection, or AI processing occurs.

## Responsibilities

The models shall:

- Define the subsystem output contract.
- Be provider independent.
- Use Pydantic v2.
- Support every planned job provider.
- Preserve information required for downstream processing.
- Remain independent from SQLModel entities.
- Remain independent from persistence.

## Non-Responsibilities

The models shall not:

- Persist data.
- Perform business logic.
- Communicate with providers.
- Calculate AI scores.
- Detect duplicates.
- Rank opportunities.

## Open Design Questions

Before implementation the following architectural decisions must be finalized:

1. Which Pydantic models should exist?

2. Should RawJobCapture be immutable?

3. Which fields are mandatory?

4. Which fields are optional?

5. Should provider metadata be separated from normalized job data?

6. Should enums be introduced?

7. How should unknown provider fields be handled?

8. Which fields are required to satisfy DATABASE_SCHEMA.md while remaining provider-independent?
