# Repository Instructions: AI Career Agent

> **Status:** Frozen
>
> **Lifecycle:** Repository Instruction
>
> **Authority:** `docs/COPILOT_CONFIGURATION.md`
>
> **Consumed By:**
> - GitHub Copilot Chat
> - GitHub Copilot Agent
>
> **Depends On:**
> - `docs/REPOSITORY_STANDARD.md`
> - `docs/AI_WORKFLOW_SPECIFICATION.md`
> - `docs/AI_DEVELOPMENT_WORKFLOW.md`
> - `docs/COPILOT_CONFIGURATION.md`
>
> **Last Updated:** 2026-08-05

---

# 1. Repository Overview

## VERIFIED FACT

This repository contains the **AI Career Agent**, a personal assistant designed to continuously discover relevant job opportunities and assist in preparing high-quality, user-controlled applications. The system automates repetitive job search tasks while ensuring the user retains final control over every decision.

**Mission:** Build a production-quality AI career assistant that continuously discovers relevant job opportunities and helps prepare high-quality, user-controlled applications while preserving user control over every application decision.

---

# 2. Project Layout

## VERIFIED FACT

The repository follows a strict organizational structure.

- `app/` — Application source code.
- `tests/` — Unit, integration, and end-to-end tests.
- `docs/` — Repository documentation and governance.
- `knowledge/` — External research and reference material.
- `.github/` — GitHub Copilot configuration, instructions, prompts, and workflows.
- `.claude/` — Claude Code configuration and session assets.

Repository organization is governed by:

- `REPOSITORY_STANDARD.md`
- `PACKAGE_STRUCTURE.md`

---

# 3. Technology Stack

## VERIFIED FACT

Core technologies used throughout this repository:

- **Language:** Python
- **Dependency Management:** uv
- **Framework:** FastAPI
- **Validation:** Pydantic v2
- **Database:** PostgreSQL
- **ORM:** SQLModel
- **Migrations:** Alembic
- **Formatting & Linting:** Ruff
- **Testing:** pytest

---

# 4. Development Workflow

## VERIFIED FACT

All implementation work must follow the engineering workflow defined in:

- `AI_DEVELOPMENT_WORKFLOW.md`

Implementation follows:

- Milestone-by-Milestone planning.
- Feature-by-Feature implementation.
- Foundation First engineering.
- Incremental implementation packages.
- Evidence-based verification.
- Human approval before commit.

GitHub Copilot is an implementation assistant operating within this workflow and does not replace repository governance.

---

# 5. Coding & Architecture Expectations

## VERIFIED FACT

GitHub Copilot must follow all repository standards.

Implementation must:

- Respect the modular architecture.
- Follow the provider-independent design.
- Preserve repository abstractions.
- Respect coding standards.
- Follow UTC time handling.
- Preserve UUID-based identity.
- Preserve immutable normalization models where specified.

**Modification Strategy**

Reuse existing implementations and utility modules before introducing new ones.

Extend existing abstractions whenever possible and follow established repository patterns rather than creating parallel implementations.

Do not introduce unnecessary files, abstractions, or architectural changes.

---

# 6. Build and Verification Commands

## VERIFIED FACT

Never claim a task is complete without observable verification.

Common verification commands include:

```bash
uv sync

ruff check .

ruff format .

pytest

fastapi dev app/main.py
```

If additional repository verification commands are introduced, use those defined by repository governance.

---

# 7. Context & Information Priority

## VERIFIED FACT

When information conflicts, use the following precedence order:

1. Official product documentation.
2. Repository Truth Policy.
3. `REPOSITORY_STANDARD.md`
4. Frozen repository specifications.
5. Current workspace context (`@workspace`, `@file`).

Never allow generated suggestions to override repository governance.

---

# 8. AI Behaviour Boundaries

## VERIFIED FACT

GitHub Copilot is an implementation assistant.

Copilot must:

- implement approved work;
- follow repository standards;
- preserve architecture;
- provide repository-aware code suggestions.

Copilot must not:

- redesign repository architecture;
- modify frozen governance documents;
- introduce new architectural patterns;
- change dependency management independently;
- rewrite repository standards;
- bypass Human Approval Gates.

All Agent Mode changes require manual review before commit.

---

# 9. Definition of Done

## VERIFIED FACT

A task is considered **Done** only when:

1. All applicable functional requirements defined in `REQUIREMENTS.md` are satisfied.
2. The implementation conforms to `ARCHITECTURE.md` and repository standards.
3. Static analysis (`ruff`) completes successfully.
4. Automated tests (`pytest`) pass without errors.
5. Documentation is synchronized where required by the AI Development Workflow.
6. The implementation has passed the required Human Approval Gate before commit.

---

# 10. Repository Instructions Policy

## VERIFIED FACT

This file provides persistent repository grounding for GitHub Copilot.

Repository instructions should:

- minimize repository exploration;
- provide persistent engineering context;
- reinforce repository governance;
- reduce architectural drift;
- improve implementation consistency.

This file complements repository governance documents and must not duplicate them.

---

# 11. Prompt Library Relationship

## VERIFIED FACT

Repository instructions provide permanent repository context.

Reusable implementation logic belongs in:

```
.github/prompts/
```

Task-specific prompts are temporary and are governed by the Prompt Governance policy defined in `AI_DEVELOPMENT_WORKFLOW.md`.

---

# 12. Path-specific Instructions

## FUTURE CONFIGURATION

Repository-wide instructions may later be supplemented by path-specific instruction files located in:

```
.github/instructions/
```

These should only be introduced when official GitHub Copilot documentation and repository complexity justify their use.

---

# 13. Agent Mode

## VERIFIED FACT

Agent Mode is intended for autonomous implementation after planning has been completed.

Agent Mode must:

- work within approved implementation packages;
- preserve repository boundaries;
- minimize unnecessary file modifications;
- provide observable verification evidence;
- stop for Human Approval before commit.

---

# 14. Traceability

## VERIFIED FACT

All repository instructions must remain traceable to at least one of the following:

- Official GitHub documentation.
- Official VS Code documentation.
- `REPOSITORY_STANDARD.md`
- `AI_WORKFLOW_SPECIFICATION.md`
- `AI_DEVELOPMENT_WORKFLOW.md`
- `COPILOT_CONFIGURATION.md`
- `REQUIREMENTS.md`

No repository instruction may contradict frozen governance.

---

# 15. Repository Truth Policy

## VERIFIED FACT

This document follows the Repository Truth Policy.

Repository artifacts progress through the lifecycle:

- Planned
- Approved
- Implemented
- Frozen
- Released

This instruction file governs GitHub Copilot behaviour only.

It does not imply repository implementation status and must remain synchronized with repository governance.

---

**Status:** Draft (Pending Final Engineering Audit)

**Lifecycle:** Repository Instruction

**Authority:** `docs/COPILOT_CONFIGURATION.md`

**Next Lifecycle Stage:** Frozen
