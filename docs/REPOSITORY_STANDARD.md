# Repository Standard

> **Purpose:** This document defines the permanent organizational standards for the AI Career Agent repository. It establishes how the repository is structured, how documentation is organized, how files are named, and which standards are governed by official tooling versus project-specific architectural decisions.

---

# Guiding Principles

This repository follows the principle of **separation of responsibilities**.

Every directory and document must have a single, well-defined purpose.

Repository organization should be driven by documented standards rather than convenience or personal preference.

Whenever an official standard exists, it takes precedence over project-specific conventions.

Project-specific standards should only be introduced when no official standard exists or when a documented architectural decision justifies the deviation.

---

# Repository Layers

The repository is organized into six logical layers.

Each layer has a distinct responsibility and should avoid overlapping with the others.

| Layer                    | Responsibility                                                                                                                                                          |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Official Standards       | External standards defined by Python, FastAPI, uv, GitHub, Claude Code, and other official tools.                                                                       |
| Repository Standards     | Repository-wide organizational rules, naming conventions, document taxonomy, and engineering governance defined by this project.                                        |
| Project Documentation    | Documents describing the project's vision, requirements, architecture, roadmap, implementation, and operational status.                                                 |
| AI Engineering Framework | Project documents defining AI strategy, collaboration practices, and engineering workflows.                                                                             |
| Source Code              | Production application code, configuration, and automated tests.                                                                                                        |
| Knowledge Base           | External documentation, learning resources, examples, videos, and NotebookLM sources used to support development but not replace the repository as the source of truth. |

---

# Repository Structure

The repository is organized as follows.

| Location     | Responsibility                                                     |
| ------------ | ------------------------------------------------------------------ |
| `app/`       | Application source code.                                           |
| `tests/`     | Unit, integration, and end-to-end tests.                           |
| `docs/`      | Project documentation and repository standards.                    |
| `knowledge/` | External knowledge base and learning resources.                    |
| `.claude/`   | Claude Code configuration, skills, commands, agents, and settings. |

The repository root contains configuration files required by official tools, including:

- `README.md`
- `pyproject.toml`
- `uv.lock`
- `.gitignore`
- `CLAUDE.md`
- `LICENSE` (when applicable)
- `CONTRIBUTING.md` (when applicable)

---

# Official Standards

The following structures are governed by official documentation and should not be changed without strong justification.

## Python

- Python package structure
- `snake_case` module naming
- `__init__.py` package initialization

## FastAPI

- `app/` package layout
- `main.py` application entry point
- Modular application organization

## uv

- `pyproject.toml`
- `uv.lock`
- Project configuration

## GitHub

- Repository root files
- `README.md`
- `LICENSE`
- `CONTRIBUTING.md`

## Claude Code

Claude Code follows the official repository structure.

- `CLAUDE.md` for persistent repository instructions
- `.claude/` for Claude-specific configuration
- `.claude/settings.json`
- `.claude/skills/`
- `.claude/agents/`
- `.claude/commands/`

Official Claude Code tooling should be used instead of introducing custom repository abstractions.

---

# Project Standards

The following conventions are defined by this repository.

## Documentation

Project-owned documentation belongs inside `docs/`.

Examples include:

- Project Vision
- Requirements
- Architecture
- Repository Standards
- Roadmap
- Project Status
- Coding Standards
- Git Workflow
- Deployment
- API Design

---

## Knowledge Base

The `knowledge/` directory stores external reference material.

It is organized into numbered domains to support:

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

- `AI_PLAYBOOK.md`
- `AI_COLLABORATION.md`

Claude Code operational files belong in the official `CLAUDE.md` and `.claude/` locations.

---

# Document Taxonomy

Every document should own a single responsibility.

| Document Type       | Responsibility                         |
| ------------------- | -------------------------------------- |
| README              | Repository introduction                |
| Vision              | Why the project exists                 |
| Requirements        | What the project must accomplish       |
| Roadmap             | Planned implementation milestones      |
| Project Status      | Current implementation progress        |
| Architecture        | System architecture and design         |
| Repository Standard | Repository governance and organization |
| Coding Standards    | Code quality and implementation rules  |
| Git Workflow        | Version control process                |
| AI Playbook         | AI tool orchestration and strategy     |
| AI Collaboration    | Human-AI collaboration model           |

Documents should reference one another rather than duplicate information.

---

# Naming Conventions

The repository uses consistent naming conventions.

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

- api-design.md
- database-design.md
- deployment.md
- development-environment.md

---

## Python Files

Use `snake_case.py`.

Examples:

- main.py
- database.py
- settings.py

---

## Directories

Python packages should use `snake_case`.

Documentation and knowledge directories may use `kebab-case` where appropriate.

---

# Ownership Boundaries

Each major document owns a single responsibility.

| Document                 | Responsibility                                      |
| ------------------------ | --------------------------------------------------- |
| `CLAUDE.md`              | Persistent repository instructions for Claude Code. |
| `AI_PLAYBOOK.md`         | AI tool orchestration and strategy.                 |
| `AI_COLLABORATION.md`    | Human-AI collaboration principles and workflow.     |
| `REPOSITORY_STANDARD.md` | Repository organization and governance.             |
| `ARCHITECTURE.md`        | System architecture and technical design.           |
| `CODING_STANDARDS.md`    | Coding conventions and implementation quality.      |
| `GIT_WORKFLOW.md`        | Version control workflow and commit standards.      |
| `PROJECT_STATUS.md`      | Current implementation progress.                    |
| `ROADMAP.md`             | Planned milestones.                                 |
| `REQUIREMENTS.md`        | Functional and non-functional requirements.         |

Documents should reference one another instead of duplicating information.

---

# Source of Truth

The repository follows a single-source-of-truth philosophy.

Priority order:

1. Official documentation
2. Repository standards
3. Project documentation
4. Source code
5. Knowledge base

NotebookLM is a research and retrieval assistant.

The Git repository remains the canonical source of truth.

---

# Change Policy

Repository organization should evolve intentionally.

Before introducing new directories, documents, naming conventions, or workflows:

1. Determine whether an official standard already exists.
2. Adopt the official standard whenever appropriate.
3. If no official standard exists, define a project standard before implementation.
4. Avoid duplicate responsibilities.
5. Preserve backward compatibility whenever practical.
6. Document significant organizational decisions.

---

**Last Updated:** 2026-08-01
