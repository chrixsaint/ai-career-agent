# Architecture

> **Purpose:** This document defines the high-level architecture of the AI Career Agent. It describes how the system is organized, how information flows through the application, and the responsibilities of each major architectural component.

Implementation details belong in the source code.

Technology selection belongs in `technology-stack.md`.

Coding practices belong in `CODING_STANDARDS.md`.

Project goals belong in `PROJECT_VISION.md`.

---

# Architectural Goals

The architecture is designed to be:

- Modular
- Maintainable
- Extensible
- Testable
- AI-assisted
- Provider-independent
- Easy to evolve

Every architectural component should own a single responsibility.

---

# Application Organization

The backend follows the official FastAPI recommendations for larger applications.

The application is organized as a Python package rooted in `app/`.

As the project grows, the application will be organized into dedicated modules for concerns such as:

- Routers
- Schemas
- Services
- Dependencies
- Configuration (Registry defined in configuration.md)

The `app/main.py` module serves as the application entry point.

Its responsibilities are limited to:

- Creating the FastAPI application
- Registering routers
- Applying global configuration
- Registering shared dependencies
- Registering exception handlers

Business logic should not be implemented in `main.py`.

Related endpoints should be organized using FastAPI's `APIRouter` to keep the application modular and maintainable.

---

# System Overview

The AI Career Agent follows a modular processing pipeline.

```text
                Job Sources
                     │
                     ▼
              Job Collection
                     │
                     ▼
            Job Normalization
                     │
                     ▼
          Duplicate Detection
                     │
                     ▼
             Job Filtering
                     │
                     ▼
              Job Ranking
                     │
                     ▼
            Recommendations
                     │
                     ▼
             AI Abstraction
          ┌──────────┴──────────┐
          ▼                     ▼
   Job Intelligence      AI Assistance
          │                     │
          ├──────────┬──────────┤
          ▼          ▼          ▼
Recommendation   CV Tailoring   Cover Letter
 Explanation
                     │
                     ▼
               User Review
```

Each stage receives structured input, performs one responsibility, and produces structured output for the next stage.

---

# Architectural Layers

## Job Collection

Responsible for discovering job opportunities from external sources.

Examples include:

- Public job APIs
- Company career pages
- Web scraping

This layer only collects raw job data.

---

## Job Processing

Responsible for transforming raw job data into a consistent internal representation.

Responsibilities include:

- Data normalization
- Validation
- Duplicate detection

The output of this layer is a clean, standardized collection of job postings.

---

## Job Intelligence

Responsible for evaluating job opportunities.

Responsibilities include:

- Career profile matching
- Job filtering
- Relevance scoring
- Recommendation generation
- AI-powered recommendation explanations

This layer determines which opportunities best match the user's preferences.

The Job Intelligence layer communicates with AI capabilities through the AI Abstraction layer rather than interacting directly with external AI providers.

---

## AI Abstraction

Responsible for providing a provider-independent interface between the application's domain logic and external AI services.

Responsibilities include:

- Providing a unified interface for AI capabilities.
- Isolating provider-specific implementations.
- Supporting integration with multiple AI providers.
- Enabling provider replacement with minimal architectural impact.

This layer encapsulates external AI providers and prevents vendor-specific concerns from leaking into business logic.

The architecture supports a primary AI provider together with optional fallback providers.

Provider selection, failover logic, and implementation details belong outside the business domain.

---

## AI Assistance

Responsible for improving application quality and supporting the job application process.

Capabilities include:

- CV tailoring
- Cover letter generation

This layer consumes AI capabilities through the AI Abstraction layer.

It assists the user but never submits applications automatically.

---

## User Layer

Responsible for presenting recommendations and supporting manual decision-making.

The user always retains final control over every application.

---

# Data Flow

Information flows through the system in one direction.

```text
Collect
    ↓
Normalize
    ↓
Validate
    ↓
Filter
    ↓
Rank
    ↓
Recommend
    ↓
AI Abstraction
    ↓
Assist
    ↓
User Decision
```

Each architectural component communicates through well-defined data structures.

---

# Architectural Principles

The architecture follows these principles.

## Separation of Responsibilities

Each module owns one responsibility.

Responsibilities should not overlap.

---

## Loose Coupling

Modules should communicate through well-defined interfaces.

Avoid unnecessary dependencies between unrelated components.

Architectural components should depend on abstractions rather than concrete external providers whenever practical.

---

## High Cohesion

Related functionality should remain together.

Unrelated functionality should remain separate.

---

## Modularity

Application functionality should be divided into independent components that can evolve with minimal impact on the rest of the system.

FastAPI routers should group related endpoints while business logic remains outside the API layer.

---

## Extensibility

New job sources, recommendation strategies, and AI providers should be added without requiring major architectural changes.

---

## Provider Independence

Business logic should remain independent of external AI vendors.

The architecture should allow AI providers to be introduced, replaced, or removed with minimal impact on the remainder of the application.

---

## Testability

Architectural components should be independently testable.

Business logic should remain separate from framework-specific code whenever practical.

External AI services should be replaceable with test doubles or mock implementations during automated testing.

---

# Scope

This document defines the high-level system architecture.

It does **not** define:

- Project goals
- Functional requirements
- Implementation roadmap
- Coding standards
- Git workflow
- Technology selection
- Provider-specific implementation details

Those responsibilities belong to their respective documents.

---

# Future Evolution

The architecture should evolve intentionally as the project grows.

Significant architectural changes should:

1. Follow official framework guidance where applicable.
2. Preserve modularity and separation of responsibilities.
3. Minimize coupling between components.
4. Preserve provider independence for external integrations where practical.
5. Be reflected in this document before implementation when they materially change the system architecture.
