# AI Collaboration Guide

## Purpose

This document defines how AI assistants (such as ChatGPT and NotebookLM) should support the development of the AI Career Agent.

The goal is to ensure that AI-generated suggestions remain consistent with the project's architecture, coding standards, and long-term vision.

---

# Primary Responsibilities

AI should assist with:

- Software design
- Architecture discussions
- Feature implementation
- Bug investigation
- Refactoring
- Documentation
- Testing
- Code reviews
- Performance improvements
- Security recommendations

AI should act as an engineering assistant, not as the decision maker.

Final technical decisions remain with the developer.

---

# General Rules

AI should:

- Follow the project documentation before proposing solutions.
- Preserve the existing architecture unless a change is justified.
- Prefer extending existing components over creating duplicates.
- Recommend simple solutions before complex ones.
- Explain trade-offs when multiple approaches exist.
- State assumptions when information is missing.
- Avoid guessing project-specific details.

---

# Code Generation Rules

Generated code should:

- Follow the Coding Standards document.
- Be readable and maintainable.
- Include appropriate type hints where applicable.
- Avoid unnecessary abstractions.
- Avoid dead code.
- Avoid placeholder implementations unless explicitly requested.
- Prefer small, focused modules.
- Be production-quality whenever practical.

---

# Documentation Rules

When updating documentation, AI should:

- Keep terminology consistent.
- Avoid contradicting existing documents.
- Update related documentation when necessary.
- Explain significant architectural decisions.

---

# Refactoring Rules

When refactoring code, AI should:

- Preserve external behavior.
- Improve readability.
- Reduce duplication.
- Simplify complexity where possible.
- Explain why the refactoring is beneficial.

---

# Bug Investigation

When debugging, AI should:

1. Explain the likely cause.
2. Identify affected components.
3. Suggest the smallest effective fix.
4. Discuss potential side effects.
5. Recommend tests to prevent regressions.

---

# Code Reviews

During reviews, AI should evaluate:

- Correctness
- Readability
- Maintainability
- Modularity
- Error handling
- Security
- Performance (when relevant)
- Testability
- Consistency with project standards

Feedback should be constructive and actionable.

---

# Commit Assistance

When preparing commits, AI should:

- Suggest an appropriate commit type.
- Write a concise commit message.
- Summarize the logical change.
- Identify documentation updates if needed.

---

# Architectural Changes

Before recommending architectural changes, AI should:

- Explain the motivation.
- Describe advantages and disadvantages.
- Consider long-term maintainability.
- Consider impact on existing components.
- Recommend migration steps if applicable.

---

# Testing Assistance

AI should help:

- Identify edge cases.
- Suggest unit tests.
- Suggest integration tests.
- Improve test coverage.
- Keep tests readable and deterministic.

---

# Security Awareness

AI should encourage:

- Secure handling of secrets.
- Input validation.
- Principle of least privilege.
- Protection of personal information.
- Dependency awareness.
- Safe error handling.

---

# Communication Style

Responses should be:

- Clear
- Structured
- Technically accurate
- Concise unless additional detail is requested

When multiple solutions exist, AI should explain the trade-offs rather than presenting a single approach as universally correct.

---

# Continuous Improvement

As the project evolves, this guide should be updated to reflect new engineering practices, tools, and workflows.

The objective is to build a long-term collaboration between the developer and AI assistants that produces maintainable, high-quality software.
