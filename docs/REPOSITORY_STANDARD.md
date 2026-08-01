# Repository Standard

> **Purpose:** This document defines the permanent organizational standards for the AI Career Agent repository. It establishes how the repository is structured, how documentation is organized, how files are named, how engineering decisions are governed, and how official standards are adopted throughout the project's lifecycle.

---

# Guiding Principles

This repository follows the principle of **separation of responsibilities**.

Every directory and document must have a single, well-defined purpose.

Repository organization should be driven by documented standards rather than convenience or personal preference.

Whenever an official standard exists, it takes precedence over project-specific conventions.

Project-specific standards should only be introduced when no official standard exists or when a documented architectural decision justifies the deviation.

The repository should remain as simple as possible while fully supporting the current phase of the project.

---

# Repository Layers

The repository is organized into six logical layers.

Each layer has a distinct responsibility and should avoid overlapping with the others.

| Layer                    | Responsibility                                                                                                                                     |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Official Standards       | External standards defined by Python, FastAPI, uv, GitHub, Claude Code, pytest, and other official tools.                                          |
| Repository Standards     | Repository-wide governance, organization, naming conventions, document taxonomy, and engineering rules defined by this project.                    |
| Project Documentation    | Documents describing the project's vision, requirements, architecture, roadmap, implementation, and operational status.                            |
| AI Engineering Framework | Project documentation describing AI workflows, collaboration, and engineering practices.                                                           |
| Source Code              | Production application code, configuration, and automated tests.                                                                                   |
| Knowledge Base           | External documentation, learning resources, examples, notes, and NotebookLM sources used for research but not as the repository's source of truth. |

---

# Repository Structure

The repository is organized as follows.

| Location     | Responsibility                                                     |
| ------------ | ------------------------------------------------------------------ |
| `app/`       | Application source code.                                           |
| `tests/`     | Unit, integration, and end-to-end tests.                           |
| `docs/`      | Project documentation and repository governance.                   |
| `knowledge/` | External knowledge base and learning resources.                    |
| `.claude/`   | Claude Code configuration, skills, commands, agents, and settings. |

The repository root contains configuration files required by official tools, including:

- README.md
- CLAUDE.md
- pyproject.toml
- uv.lock
- .gitignore

The following files are introduced only when their responsibilities become active:

- LICENSE
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- SECURITY.md
- SUPPORT.md

---

# Official Standards

Whenever an official standard exists, it should be adopted instead of creating a custom convention.

The following structures are governed by official documentation.

## Python

- Package structure
- `snake_case` module naming
- `__init__.py`
- Type hints
- Standard library usage

## FastAPI

- `app/` application layout
- `main.py`
- APIRouter
- Dependency Injection
- Pydantic models
- Async programming patterns

## uv

- `pyproject.toml`
- `uv.lock`
- Dependency management

## GitHub

- Repository root files
- Community health files
- `.github/` directory
- GitHub Actions
- Repository templates

## Claude Code

- `CLAUDE.md`
- `.claude/`
- `.claude/skills/`
- `.claude/agents/`
- `.claude/commands/`
- `.claude/settings.json`

Official tooling should always be preferred over custom abstractions.

---

# Official Standards Lifecycle

Official standards should be adopted according to the current phase of the project.

An officially recommended structure, document, workflow, or configuration should only be introduced when its responsibility becomes active.

This repository intentionally avoids implementing inactive standards solely for future completeness.

Official standards are adopted progressively as the project evolves.

Whenever a new responsibility becomes active, the corresponding official documentation should be consulted before introducing a project-specific solution.

---

# Project Standards

The following conventions are defined by this repository.

## Documentation

Project-owned documentation belongs inside `docs/`.

Examples include:

- Project Vision
- Requirements
- Architecture
- Repository Standard
- Roadmap
- Project Status
- Coding Standards
- Git Workflow
- Technology Stack
- Database Design
- AI Playbook
- AI Collaboration

---

## Knowledge Base

The `knowledge/` directory stores external reference material.

It supports:

- NotebookLM
- Personal learning
- Official documentation
- Examples
- Videos
- Notes

The knowledge base supports development but is **not** the project's source of truth.

---

## AI Engineering Framework

Project-specific AI engineering documentation belongs in `docs/`.

Examples include:

- AI_PLAYBOOK.md
- AI_COLLABORATION.md

Claude Code operational files belong only in their official locations (`CLAUDE.md` and `.claude/`).

---

# Repository Evolution Philosophy

The repository evolves incrementally.

Documentation, directories, workflows, and configuration should be introduced only when they become necessary.

Avoid placeholder files that have no active responsibility.

The repository should remain lean while remaining aligned with official standards.

---

# Active Responsibility Principle

Repository documentation should describe the project's current responsibilities.

Do not introduce documents, workflows, directories, or standards before their responsibilities become active.

Official standards should be adopted when the project reaches the stage where they provide value.

Inactive documentation increases maintenance cost and should be avoided.

---

# Document Taxonomy

Every document owns exactly one responsibility.

| Document            | Responsibility                        |
| ------------------- | ------------------------------------- |
| README              | Repository introduction               |
| PROJECT_VISION      | Why the project exists                |
| REQUIREMENTS        | What the system must accomplish       |
| ROADMAP             | Planned implementation                |
| PROJECT_STATUS      | Current implementation progress       |
| ARCHITECTURE        | Technical design                      |
| REPOSITORY_STANDARD | Repository governance                 |
| CODING_STANDARDS    | Code quality and implementation rules |
| GIT_WORKFLOW        | Version control workflow              |
| AI_PLAYBOOK         | AI orchestration strategy             |
| AI_COLLABORATION    | Human-AI collaboration model          |
| technology-stack    | Technologies used by the project      |
| database-design     | Database design                       |

Documents should reference one another rather than duplicate information.

---

# Naming Conventions

## Core Documents

Use `UPPER_SNAKE_CASE.md`.

Examples:

- README.md
- ARCHITECTURE.md
- ROADMAP.md
- REQUIREMENTS.md
- PROJECT_STATUS.md
- REPOSITORY_STANDARD.md

---

## Technical Documents

Use `kebab-case.md`.

Examples:

- technology-stack.md
- database-design.md

---

## Python Files

Use `snake_case.py`.

Examples:

- main.py
- database.py
- settings.py

---

## Directories

Python packages use `snake_case`.

Documentation and knowledge directories may use `kebab-case` where appropriate.

---

# Ownership Boundaries

Each document owns a single responsibility.

| Document               | Responsibility                                 |
| ---------------------- | ---------------------------------------------- |
| CLAUDE.md              | Persistent Claude Code repository instructions |
| AI_PLAYBOOK.md         | AI tool orchestration                          |
| AI_COLLABORATION.md    | Human-AI collaboration                         |
| REPOSITORY_STANDARD.md | Repository governance                          |
| ARCHITECTURE.md        | Technical architecture                         |
| CODING_STANDARDS.md    | Code quality                                   |
| GIT_WORKFLOW.md        | Version control                                |
| PROJECT_STATUS.md      | Current progress                               |
| ROADMAP.md             | Planned milestones                             |
| REQUIREMENTS.md        | Functional and non-functional requirements     |

Documents should reference one another rather than duplicate information.

---

# Source of Truth

The repository follows a single-source-of-truth philosophy.

Repository decisions should always be based on the highest applicable source in the following order:

1. Official documentation
2. Repository standards
3. Project documentation
4. Source code
5. Knowledge base

Official documentation defines external standards.

Repository standards define how those standards are adopted within this project.

Project documentation defines repository-specific architecture and engineering decisions.

Source code implements those decisions.

The knowledge base supports research and learning but does not replace the repository as the canonical source of truth.

NotebookLM is used as a research and documentation verification assistant.

The Git repository remains the canonical source of truth.

---

# Repository Decision Framework

Before introducing any change, answer the following questions:

1. Is there an official standard?
2. Does this artifact have one clear responsibility?
3. Is that responsibility active today?
4. Does another document already own it?
5. Does this simplify the repository?
6. Does it preserve a single source of truth?

If any answer indicates duplication, unnecessary complexity, or inactive responsibility, the change should be postponed, merged, relocated, or removed.

The preferred solution is always the simplest repository structure that fully supports the current phase of the project.

---

# Change Policy

Repository organization should evolve intentionally.

Every organizational change should follow this process:

1. Verify whether an official standard already exists.
2. Validate official guidance using NotebookLM when appropriate.
3. Adopt the official standard whenever applicable.
4. If no official standard exists, define a project standard.
5. Ensure the proposed change follows this Repository Standard.
6. Avoid duplicate responsibilities.
7. Preserve backward compatibility whenever practical.
8. Document significant architectural decisions.
9. Apply changes in small, reviewable batches.
10. Commit each completed batch before beginning the next.

Large repository restructuring should follow this workflow:

1. Research official documentation.
2. Verify findings with NotebookLM.
3. Update Repository Standards if necessary.
4. Produce an audit plan.
5. Review proposed changes.
6. Apply changes incrementally.
7. Verify repository consistency after each batch.
8. Commit the completed batch before continuing.

---

**Last Updated:** 2026-08-01
