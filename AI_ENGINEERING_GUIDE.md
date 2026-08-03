# AI Engineering Guide

> **Purpose:** This document defines the repository-wide engineering standards, operating rules, and persistent context that every AI assistant, coding agent, or automated contributor must follow when working on the AI Career Agent project.

This guide complements the project's architecture, coding standards, implementation guide, and repository standards while remaining independent of any specific AI vendor or development tool.

---

# Required Reading

Before performing significant work, review the following documents in the order listed.

## Core Project Documents

1. `docs/PROJECT_VISION.md`
2. `docs/REQUIREMENTS.md`
3. `docs/ROADMAP.md`
4. `docs/ARCHITECTURE.md`

## Database Documentation

5. `docs/DATABASE_DESIGN.md`
6. `docs/DATABASE_ARCHITECTURE.md`
7. `docs/DATABASE_SCHEMA.md`

## Engineering Standards

8. `docs/IMPLEMENTATION_GUIDE.md`
9. `docs/CODING_STANDARDS.md`
10. `docs/REPOSITORY_STANDARD.md`
11. `docs/GIT_WORKFLOW.md`
12. `docs/technology-stack.md`

These documents define the repository's authoritative standards and take precedence whenever they apply.

---

# AI Contributor Rules

AI contributors shall:

- Understand the requested task before proposing changes.
- Follow the established project architecture.
- Reuse existing implementations before introducing new ones.
- Preserve the repository structure.
- Prefer official documentation and authoritative sources.
- Explain significant engineering decisions.
- Keep implementation and documentation synchronized.
- Verify work before considering a task complete.
- Respect the Single Responsibility Principle across code and documentation.
- Maintain consistency with the project's architectural decisions.
- Implement new functionality incrementally following the project roadmap.

---

# AI Engineering Standards

All AI functionality shall follow the provider-independent architecture.

Always:

- Implement AI features through the abstraction layer defined in `app/services/ai/base.py`.
- Adhere to the `AIProvider` abstract base class contract.
- Keep business logic independent of AI vendors.
- Isolate provider-specific implementations inside `app/services/ai/providers/`.
- Return structured outputs using Pydantic models whenever results are consumed programmatically.
- Keep prompts modular, reusable, and provider-independent whenever practical.
- Place provider-specific prompt optimizations only inside the corresponding provider implementation.
- Follow the implementation sequence defined in `IMPLEMENTATION_GUIDE.md`.

Never:

- Import external AI SDKs directly into routers or business services.
- Couple domain logic to a specific AI provider.
- Duplicate AI integration logic.
- Hardcode provider-specific request handling outside provider implementations.
- Introduce vendor-specific assumptions into shared business logic.

---

# Standard Engineering Workflow

For implementation tasks:

1. Understand the request.
2. Review the relevant documentation.
3. Review the existing implementation.
4. Propose the implementation approach.
5. Implement the solution.
6. Verify the implementation.
7. Update documentation when required.
8. Summarize the completed work.

For documentation tasks:

1. Review the existing documentation.
2. Preserve the Single Source of Truth.
3. Improve clarity and consistency.
4. Update related documents when architectural or engineering decisions change.
5. Verify that cross-document references remain accurate.

---

# Repository Philosophy

This repository follows a **Single Source of Truth** approach.

Principles:

- The Git repository is the authoritative source of project knowledge.
- Documentation governs implementation.
- NotebookLM is used for research, validation, and knowledge retrieval.
- AI assistants strengthen both the software and the documentation.
- Prefer extending existing documentation rather than creating duplicate sources.
- Architectural decisions should be documented before implementation whenever they materially affect the project.

---

# Success Criteria

A task is complete only when:

- The requested work has been completed.
- The implementation follows the established architecture.
- Repository standards have been respected.
- Documentation remains synchronized.
- Appropriate verification has been performed.
- Cross-document consistency has been preserved.
- The implementation can be understood and maintained by future contributors.

---

# Scope

This document defines repository-wide engineering guidance for AI contributors.

It does **not** define:

- System architecture
- Functional requirements
- Technology selection
- Coding standards
- Git workflow
- Database design
- Implementation details

Those responsibilities belong to their respective authoritative documents.

---

# Tool-Specific Configuration

Repository engineering guidance is maintained in this document.

Tool-specific configuration files (such as `.claude/`) should remain in their official locations when the corresponding AI tooling is used. These files supplement, but do not replace, the repository-wide engineering standards defined here.

---

**Last Updated:** 2026-08-03
**Status:** Repository Standard
