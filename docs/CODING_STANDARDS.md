# Coding Standards

## Purpose

This document defines implementation quality standards for Python, FastAPI, and pytest code in this repository.

These standards apply to application code and tests.

---

# Core Principles

- Readability over cleverness
- Simplicity over unnecessary complexity
- Consistency over personal preference
- Small, focused modules
- Explicit behavior over implicit behavior

---

# Python Standards

- Use type hints for function and method signatures.
- Use `snake_case` for modules, variables, and functions.
- Keep functions focused on one responsibility.
- Prefer standard library modules where practical.
- Avoid broad `except Exception` handlers unless the boundary requires it.

---

# Naming Conventions

Names should be:

- Descriptive
- Consistent
- Easy to understand
- Free of unnecessary abbreviations

Avoid generic names such as:

- data
- info
- temp
- value
- object

Prefer names that clearly describe their purpose.

---

# Functions

Functions should:

- Have one responsibility.
- Be small and focused.
- Have descriptive names.
- Avoid excessive nesting.
- Return predictable results.
- Minimize side effects.

---

# Classes

Classes should:

- Represent one concept.
- Have one clear responsibility.
- Hide implementation details.
- Expose a minimal public interface.

---

# FastAPI Standards

- Define request and response schemas with Pydantic models.
- Use `APIRouter` for route grouping instead of placing all routes in a single file.
- Use FastAPI dependency injection (`Depends`) for shared services and request-scoped dependencies.
- Declare `response_model` on endpoints when returning structured data.
- Keep endpoint handlers thin; place business logic in service modules.

## Async and Sync Guidance

- Use `async def` for I/O-bound handlers and dependencies.
- Use regular `def` for CPU-bound or purely synchronous logic.
- Do not block the event loop with long-running synchronous I/O in async handlers.

---

# Error Handling

Errors should:

- Be handled explicitly.
- Provide meaningful messages.
- Avoid silent failures.
- Avoid broad exception handling unless justified.

- Define global exception handlers at the API boundary for predictable error responses.

---

# Logging

Log information should help diagnose problems.

Avoid logging:

- secrets
- passwords
- API keys
- personal information

Logs should provide useful context without exposing sensitive data.

---

# Testing

Use `pytest` for automated tests.

Tests should be:

- independent
- deterministic
- readable
- maintainable

FastAPI testing should:

- Use `fastapi.testclient.TestClient` for API-level tests.
- Cover success and failure cases for each endpoint.
- Validate response status codes and response schemas.

---

# Refactoring

Continuous refactoring is encouraged.

Refactoring should improve:

- readability
- maintainability
- modularity

without changing external behavior.

---

# Continuous Improvement

These standards are intended to evolve with the project.

Major changes to engineering practices should be documented and agreed upon before adoption.
