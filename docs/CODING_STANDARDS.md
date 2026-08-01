# Coding Standards

> **Purpose:** This document defines the implementation standards for source code in the AI Career Agent repository. It establishes the coding conventions, engineering principles, and framework-specific practices that ensure the codebase remains readable, maintainable, and consistent.

These standards apply to all production code and automated tests.

Repository organization is governed by **REPOSITORY_STANDARD.md**.

Version control is governed by **GIT_WORKFLOW.md**.

System design is governed by **ARCHITECTURE.md**.

---

# Core Principles

The project follows these engineering principles:

- Readability over cleverness.
- Simplicity over unnecessary complexity.
- Consistency over personal preference.
- Composition over duplication.
- Small, focused modules.
- Explicit behavior over implicit behavior.
- Write code for humans first.

---

# Engineering Principles

## Single Responsibility Principle (SRP)

Every module, class, and function should have one clear responsibility.

---

## DRY (Don't Repeat Yourself)

Avoid duplicated logic.

Extract reusable components when duplication becomes apparent.

---

## KISS (Keep It Simple)

Prefer the simplest solution that correctly solves the problem.

Avoid unnecessary abstractions.

---

## YAGNI (You Aren't Gonna Need It)

Do not implement features before they are required by the roadmap.

Future extensibility should not justify unnecessary complexity.

---

# Python Standards

Follow the official Python style guide where applicable.

## Type Hints

Use type hints for:

- Function parameters
- Return values
- Public methods
- Shared interfaces

Type hints improve readability, static analysis, and FastAPI integration.

---

## Naming

Use:

- `snake_case` for variables, functions, modules, and packages.
- `PascalCase` for classes.
- `UPPER_CASE` for constants.

Choose descriptive names.

Avoid abbreviations unless they are widely understood.

---

## Functions

Functions should:

- Perform one responsibility.
- Be easy to understand.
- Minimize side effects.
- Avoid excessive nesting.
- Return predictable results.

---

## Classes

Classes should:

- Represent one concept.
- Encapsulate implementation details.
- Expose a minimal public interface.

---

# FastAPI Standards

Follow official FastAPI architecture and programming practices.

## Application Structure

- Group endpoints using `APIRouter`.
- Keep route handlers thin.
- Place business logic inside service modules.
- Separate schemas, routers, and services.

---

## Pydantic Models

Use Pydantic models for:

- Request validation
- Response serialization
- Shared data contracts

Avoid using raw dictionaries for structured API data.

---

## Dependency Injection

Use `Depends()` for:

- Database sessions
- Authentication
- Shared services
- Request-scoped dependencies

Avoid manually constructing dependencies inside route handlers.

---

## Response Models

Declare `response_model` whenever an endpoint returns structured data.

This ensures:

- automatic validation
- OpenAPI documentation
- consistent API contracts

---

## Async Programming

Use `async def` for:

- Database operations
- HTTP requests
- File operations
- Other I/O-bound work

Use regular `def` for CPU-bound or synchronous logic.

Do not block the event loop with long-running synchronous operations.

---

# Error Handling

Handle errors explicitly.

Prefer:

- meaningful exception messages
- predictable API responses
- global FastAPI exception handlers

Avoid:

- silent failures
- broad exception handling
- swallowing exceptions

---

# Logging

Logs should help diagnose problems.

Never log:

- passwords
- secrets
- API keys
- tokens
- personal information

Logs should provide useful context without exposing sensitive information.

---

# Documentation

Public modules, classes, and important functions should include documentation explaining:

- purpose
- inputs
- outputs
- important assumptions

Code should be understandable without excessive comments.

---

# Testing

Use `pytest` for automated testing.

Tests should be:

- independent
- deterministic
- readable
- maintainable

FastAPI tests should:

- use `TestClient`
- validate request handling
- validate response models
- verify HTTP status codes
- cover both successful and failure scenarios

---

# Refactoring

Continuous refactoring is encouraged.

Refactoring should improve:

- readability
- maintainability
- modularity

without changing observable behavior.

---

# Scope

This document defines implementation quality.

It does **not** define:

- repository organization
- Git workflow
- system architecture
- project planning

Those responsibilities belong to their respective documents.

---

# Continuous Improvement

These standards should evolve alongside the project.

Whenever official Python, FastAPI, or pytest guidance changes, this document should be reviewed and updated accordingly.
