# Official References

## Purpose

This document serves as the project's curated index of authoritative technical references.

Its purpose is to quickly locate the exact official documentation pages used throughout the development of the AI Career Agent.

It is intended for:

- Developers
- NotebookLM
- Claude Code
- ChatGPT
- GitHub Copilot

This document does **not** duplicate official documentation.

Instead, it provides direct links to the specific pages that define the project's engineering decisions.

---

## Scope

This document contains references for:

- Programming languages
- Frameworks
- Libraries
- Development tools
- Infrastructure
- AI engineering
- Testing

Only official documentation should be included.

---

## Maintenance

Before adding a reference, verify that:

- It comes from the official documentation.
- It has been used during this project.
- It provides long-term value.
- A direct page link can be provided instead of a general homepage.

Remove references that are no longer relevant to the project's active technology stack.

---

# Backend

## Python

### Purpose

Core programming language used throughout the project.

### When to Use

Language syntax, typing, packaging, standard library, and best practices.

### Official References

(To be added as the project evolves.)

### Project Notes

Use the smallest official page that completely answers the engineering question.

---

## FastAPI

### Purpose

Backend web framework.

### When to Use

API development, routing, dependency injection, request validation, testing, application architecture.

### Official References

(To be added as the project evolves.)

### Project Notes

Prefer page-level links instead of the documentation homepage.

---

## Pydantic

### Purpose

Data validation and application settings.

### Official References

(To be added.)

## The relationship between CRUD operation AND I/O

specifically around persistent storage/records

So yes — every CRUD operation is implemented via I/O, but not all I/O is CRUD.

Mapping them out
CRUD operation What it does Is it I/O?
Create Insert a new record Yes — writing (output) to a DB/file
Read Fetch existing data Yes — reading (input) from a DB/file
Update Modify existing data Yes — read + write
Delete Remove data Yes — write (a deletion is still a write operation)

---

## SQLModel

### Purpose

Database models and ORM.

### Official References

(To be added.)

---

## SQLAlchemy

### Purpose

Database engine and advanced ORM features.

### Official References

(To be added.)

---

## Alembic

### Purpose

Database schema migrations.

### Official References

(To be added.)

---

# Development Tools

## uv

### Purpose

Project dependency and environment management.

### Official References

(To be added.)

---

## pytest

### Purpose

Testing framework.

### Official References

(To be added.)

---

## Git

### Purpose

Version control.

### Official References

(To be added.)

---

## GitHub

### Purpose

Repository hosting, collaboration, and CI/CD.

### Official References

(To be added.)

---

## Docker

### Purpose

Containerized development and deployment.

### Official References

(To be added when Docker is introduced.)

---

# AI Engineering

## Claude Code

### Purpose

AI-assisted implementation.

### Official References

(To be added.)

---

## Anthropic

### Purpose

Prompt engineering and Claude best practices.

### Official References

(To be added.)

---

## OpenAI

### Purpose

Prompt engineering and ChatGPT best practices.

### Official References

(To be added.)

---

## NotebookLM

### Purpose

Research, architecture validation, and official documentation search.

### Official References

(To be added.)

---

# Revision Policy

This document should evolve together with the project.

Only include:

- Official documentation
- Page-level references
- Resources that are repeatedly used during development

Avoid:

- Third-party tutorials
- Blog posts
- Copied documentation
- Outdated references
