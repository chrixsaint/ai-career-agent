# Coding Standards

## Purpose

This document defines the coding standards and engineering principles for the AI Career Agent.

Its goal is to ensure the codebase remains consistent, maintainable, scalable, and easy to understand throughout the project's lifetime.

These standards apply to all source code, tests, scripts, and documentation.

---

# Core Principles

The project follows these principles:

- Readability over cleverness.
- Simplicity over unnecessary complexity.
- Consistency over personal preference.
- Composition over duplication.
- Small, focused modules.
- Explicit is better than implicit.
- Write code for humans first.

---

# Clean Code Principles

The codebase should strive to:

- Be easy to read.
- Be easy to test.
- Be easy to modify.
- Minimize technical debt.
- Avoid unnecessary abstractions.
- Avoid premature optimization.

---

# SOLID Principles

Where appropriate, follow the SOLID principles:

- Single Responsibility Principle (SRP)
- Open/Closed Principle (OCP)
- Liskov Substitution Principle (LSP)
- Interface Segregation Principle (ISP)
- Dependency Inversion Principle (DIP)

These principles should guide architecture decisions rather than be applied mechanically.

---

# DRY Principle

Follow the Don't Repeat Yourself (DRY) principle.

If logic is duplicated, prefer extracting reusable components instead of copying code.

---

# KISS Principle

Keep solutions as simple as possible.

Do not introduce additional complexity unless it provides a clear long-term benefit.

---

# YAGNI Principle

"You Aren't Gonna Need It."

Do not implement features based solely on future possibilities.

Only build functionality required by the current roadmap unless there is a compelling architectural reason.

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

# Error Handling

Errors should:

- Be handled explicitly.
- Provide meaningful messages.
- Avoid silent failures.
- Avoid broad exception handling unless justified.

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

# Documentation

Public modules, classes, and important functions should include documentation explaining:

- purpose
- inputs
- outputs
- important assumptions

Code should not require excessive comments to be understood.

---

# Testing

New functionality should include appropriate tests.

Tests should be:

- independent
- deterministic
- readable
- maintainable

---

# Refactoring

Continuous refactoring is encouraged.

Refactoring should improve:

- readability
- maintainability
- modularity

without changing external behavior.

---

# Code Reviews

Every change should be reviewed for:

- readability
- correctness
- maintainability
- simplicity
- consistency with project standards

---

# Continuous Improvement

These standards are intended to evolve with the project.

Major changes to engineering practices should be documented and agreed upon before adoption.
