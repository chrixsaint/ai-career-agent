# Technology Stack

> **Purpose:** This document provides a high-level overview of the technologies selected for the AI Career Agent. It explains what technologies are used, why they were selected, and their current adoption status.

The authoritative source for project dependencies is:

- `pyproject.toml`
- `uv.lock`

Implementation details belong in their respective documentation.

---

# Technology Selection Principles

Technologies adopted by this project should be:

- Well documented
- Actively maintained
- Widely adopted
- Cost-effective
- Modular
- Suitable for long-term maintenance

Whenever practical, prefer open-source technologies.

---

# Backend

| Technology | Purpose                           | Status |
| ---------- | --------------------------------- | ------ |
| Python     | Primary programming language      | In Use |
| FastAPI    | Web API framework                 | In Use |
| Pydantic   | Data validation and serialization | In Use |
| Uvicorn    | ASGI application server           | In Use |

---

# Database

| Technology | Purpose                        | Status  |
| ---------- | ------------------------------ | ------- |
| PostgreSQL | Primary relational database    | Planned |
| SQLAlchemy | Object Relational Mapper (ORM) | Planned |
| Alembic    | Database migrations            | Planned |

---

# AI

| Technology | Purpose                                  | Status  |
| ---------- | ---------------------------------------- | ------- |
| OpenAI API | CV tailoring and cover letter generation | Planned |

---

# Development

| Technology | Purpose                               | Status |
| ---------- | ------------------------------------- | ------ |
| uv         | Dependency and environment management | In Use |
| Git        | Version control                       | In Use |
| GitHub     | Repository hosting                    | In Use |

---

# Testing

| Technology | Purpose                      | Status  |
| ---------- | ---------------------------- | ------- |
| pytest     | Unit and integration testing | Planned |

---

# Documentation

| Technology | Purpose                         | Status |
| ---------- | ------------------------------- | ------ |
| Markdown   | Repository documentation        | In Use |
| NotebookLM | Official documentation research | In Use |

---

# Optional Technologies

The following technologies may be introduced if project requirements justify them.

Examples include:

- pydantic-settings
- orjson
- email-validator

Optional technologies should only be adopted when they provide a clear benefit.

---

# Future Technologies

Future phases of the project may introduce additional technologies.

Potential additions include:

- Docker
- GitHub Actions
- Playwright

These technologies should only be adopted when required by the project roadmap.

---

# Scope

This document defines technology selection.

It does **not** define:

- repository organization
- coding standards
- system architecture
- setup procedures
- deployment procedures

Those responsibilities belong to their respective documents.

---

# Source of Truth

This document provides a human-readable overview of the project's technology choices.

The machine-readable source of truth for project dependencies remains:

- `pyproject.toml`
- `uv.lock`

Whenever these files and this document differ, the project configuration files take precedence.
