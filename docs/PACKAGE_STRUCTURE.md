# Package Structure

> **Purpose:** This document defines the authoritative physical package structure of the AI Career Agent application. It specifies how the source code is organized to support the project's architecture, maintainability, extensibility, and long-term scalability.

Repository governance belongs in `REPOSITORY_STANDARD.md`.

System architecture belongs in `ARCHITECTURE.md`.

Job collection design belongs in `JOB_COLLECTION_ARCHITECTURE.md`.

Database design belongs in `DATABASE_ARCHITECTURE.md`.

Configuration standards belong in `configuration.md`.

---

# Design Principles

The package structure is designed to be:

- Modular
- Maintainable
- Extensible
- Testable
- Provider-independent
- Easy to navigate

Each package should own a single responsibility.

---

# Project Layout

The repository contains several top-level directories.

The overall repository organization is defined in `REPOSITORY_STANDARD.md`.

This document focuses exclusively on the physical organization of the application source code located under `app/`.

---

# Application Structure (`app/`)

The application follows the official FastAPI recommendations for larger applications and is organized into dedicated packages according to responsibility.

```text
app/
├── __init__.py
├── main.py                    # FastAPI application entry point
│
├── api/                       # HTTP interface
│   ├── __init__.py
│   ├── dependencies.py
│   └── routers/
│       ├── __init__.py
│       └── system.py
│
├── core/                      # Cross-cutting infrastructure
│   ├── __init__.py
│   ├── config.py              # Pydantic Settings implementation
│   ├── exceptions.py          # Global application exceptions
│   └── security.py            # Authentication and security helpers
│
├── database/                  # Database infrastructure
│   ├── __init__.py
│   ├── engine.py              # SQLModel / SQLAlchemy engine
│   ├── session.py             # Session management
│   └── base.py                # Shared database configuration
│
├── models/                    # SQLModel entities
│   ├── __init__.py
│   ├── base.py
│   ├── company.py
│   ├── job.py
│   └── job_source.py
│
├── schemas/                   # API request/response models
│   ├── __init__.py
│   ├── company.py
│   ├── job.py
│   └── system.py
│
└── services/                  # Business logic
    ├── __init__.py
    │
    ├── ai/
    │   ├── __init__.py
    │   ├── base.py            # AIProvider abstract interface
    │   ├── constants.py
    │   ├── exceptions.py
    │   ├── factory.py
    │   ├── models.py
    │   └── providers/
    │       ├── __init__.py
    │       ├── gemini.py
    │       └── groq.py
    │
    ├── collection/
    │   ├── __init__.py
    │   ├── base.py            # BaseCollector abstract interface
    │   ├── constants.py
    │   ├── exceptions.py
    │   ├── factory.py
    │   ├── models.py          # RawJobCapture models
    │   ├── utils.py
    │   ├── collectors/
    │   │   ├── __init__.py
    │   │   ├── api.py
    │   │   ├── ats.py
    │   │   ├── feed.py
    │   │   └── html.py
    │   └── providers/
    │       ├── __init__.py
    │       ├── jooble.py
    │       ├── euraxess.py
    │       ├── greenhouse.py
    │       └── ...
    │
    ├── intelligence/
    │   ├── __init__.py
    │   └── (future modules)
    │
    └── assistance/
        ├── __init__.py
        └── (future modules)
```

---

# Package Responsibilities

Each package owns a single technical concern.

## API Layer (`app/api/`)

Responsible for the HTTP interface and request-response lifecycle.

Responsibilities include:

- Request routing
- Dependency injection
- Request validation
- Response serialization
- HTTP status handling

Components:

- `routers/` — Groups related API endpoints.
- `dependencies.py` — Shared FastAPI dependencies such as database sessions, authentication, and configuration.

Business logic should never be implemented in this layer.

---

## Core Layer (`app/core/`)

Responsible for application-wide infrastructure and cross-cutting concerns.

Responsibilities include:

- Application configuration
- Security
- Global exception handling
- Shared infrastructure

Components:

- `config.py` — Physical implementation of the configuration defined in `configuration.md`.
- `exceptions.py` — Global application exceptions.
- `security.py` — Authentication, authorization, password hashing, JWT utilities, and related security helpers.

Business rules should remain outside this layer.

---

## Database Layer (`app/database/`)

Responsible for persistence infrastructure.

Responsibilities include:

- Database engine creation
- Session management
- Shared SQLModel configuration
- Database initialization

Components:

- `engine.py` — SQLAlchemy/SQLModel engine creation.
- `session.py` — Database session lifecycle.
- `base.py` — Shared database configuration.

Database entities belong in the `models/` package.

---

## Models Layer (`app/models/`)

Responsible for persistent domain entities.

Responsibilities include:

- SQLModel entities
- Shared database mixins
- Physical table definitions

Components:

- `base.py` — Shared mixins such as `IDMixin` and `TimestampMixin` defined in `DATABASE_ARCHITECTURE.md`.
- Domain models (`job.py`, `company.py`, `job_source.py`, etc.) — Physical implementation of the tables defined in `DATABASE_SCHEMA.md`.

Models represent persistent storage rather than API contracts.

---

## Schemas Layer (`app/schemas/`)

Responsible for API request and response contracts.

Responsibilities include:

- Request validation
- Response serialization
- Public API models

Schemas should remain independent from database models whenever practical.

---

## Services Layer (`app/services/`)

Responsible for business logic, orchestration, and external integrations.

Business logic should remain independent of HTTP frameworks, database implementations, and external AI providers whenever practical.

### AI Subsystem (`app/services/ai/`)

Responsible for the provider-independent AI abstraction.

Responsibilities include:

- AIProvider interface
- Provider selection
- Provider orchestration
- AI request and response models
- Vendor-specific implementations (Gemini, Groq)

This subsystem implements the AI architecture defined in `ARCHITECTURE.md`.

---

### Job Collection Subsystem (`app/services/collection/`)

Responsible for discovering opportunities from external providers.

Responsibilities include:

- External job retrieval
- Raw job capture
- Provider abstraction
- Protocol implementations
- Vendor integrations

This subsystem implements the Strategy Pattern defined in `JOB_COLLECTION_ARCHITECTURE.md`.

---

### Job Intelligence Subsystem (`app/services/intelligence/`)

Responsible for evaluating collected opportunities.

Future responsibilities include:

- Career profile matching
- Job filtering
- Relevance scoring
- Recommendation generation
- Recommendation explanations

This subsystem consumes standardized job data produced by the Job Collection subsystem.

---

### AI Assistance Subsystem (`app/services/assistance/`)

Responsible for AI-assisted application support.

Future responsibilities include:

- CV tailoring
- Cover letter generation

The Assistance subsystem assists the user but never submits applications automatically.

---

# Architectural Principles

The package structure follows these principles.

## Separation of Responsibilities

Each package owns one clearly defined responsibility.

Responsibilities should not overlap.

---

## Loose Coupling

Packages communicate through well-defined interfaces.

Implementation details should remain encapsulated within their owning package.

---

## High Cohesion

Related functionality should remain together.

Unrelated functionality should remain separate.

---

## Modularity

Application functionality should be divided into independent packages that can evolve with minimal impact on the remainder of the application.

---

## Extensibility

New AI providers, job sources, and business capabilities should be introduced by extending the existing package structure rather than modifying unrelated components.

---

## Provider Independence

Business logic should remain independent of external AI vendors and job providers.

Provider-specific implementations belong exclusively inside their respective provider packages.

---

## Testability

Every package should be independently testable.

Framework-specific code should remain separated from business logic whenever practical.

---

# Scope

This document defines the physical organization of the application source code.

It does **not** define:

- System architecture
- Functional requirements
- Database schema
- Technology selection
- Coding standards
- Implementation roadmap

Those responsibilities belong to their respective documents.

---

# Future Evolution

The package structure should evolve intentionally as the project grows.

Significant structural changes should:

1. Preserve modularity.
2. Preserve separation of responsibilities.
3. Minimize coupling.
4. Follow the established architectural layering.
5. Be reflected in this document before implementation whenever they materially change the application structure.
