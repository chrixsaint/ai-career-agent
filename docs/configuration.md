# Configuration

> **Purpose:** This document defines the authoritative configuration standards for the AI Career Agent. It serves as the single source of truth for application configuration, environment variables, configuration loading, validation, and secret management.

Implementation code belongs in `app/core/config.py`.

Technology selection belongs in `technology-stack.md`.

System architecture belongs in `ARCHITECTURE.md`.

Coding practices belong in `CODING_STANDARDS.md`.

---

# Configuration Philosophy

The configuration system is designed to be:

- Explicit
- Type-safe
- Predictable
- Environment-independent
- Secure
- Maintainable
- Easy to validate

Configuration should fail fast when required settings are missing or invalid.

Business logic must never depend on hardcoded configuration values.

---

# Configuration Lifecycle

Configuration evolves alongside the project roadmap.

Every new configuration value must:

- Have a single documented purpose.
- Be defined in this document before implementation.
- Be represented as a typed setting.
- Specify whether it is required or optional.
- Specify the project phase in which it becomes active.
- Be validated during application startup whenever practical.

---

# Configuration Hierarchy

Configuration values are resolved using the following precedence.

1. Operating system environment variables
2. Local `.env` file
3. Default values defined in the application

Higher-precedence values always override lower-precedence values.

Configuration loading should remain deterministic across all environments.

---

### Pydantic Settings Standards

Application configuration shall use pydantic-settings.
Configuration classes should:

- Use explicit type annotations.
- Validate configuration during startup.
- Avoid implicit defaults for required values.
- Group related settings together.
- Load configuration only once using dependency caching when appropriate.

**Configuration implementation belongs in `app/core/config.py`.**

---

### Environment Variable Registry

The following environment variables are currently defined by the project.

| Variable       | Purpose                                              | Required | Phase   |
| -------------- | ---------------------------------------------------- | -------- | ------- |
| PROJECT_NAME   | Human-readable name of the application               | No       | Phase 1 |
| ENVIRONMENT    | Execution context (development, testing, production) | No       | Phase 1 |
| DATABASE_URL   | PostgreSQL connection string                         | Yes      | Phase 2 |
| GEMINI_API_KEY | Primary AI provider                                  | Yes      | Phase 3 |
| GROQ_API_KEY   | Fallback AI provider                                 | Optional | Phase 3 |
| LOG_LEVEL      | Application logging level                            | No       | Phase 7 |

Future variables should be added to this registry before implementation.

```

---

# Configuration Categories

Configuration values are grouped by subsystem.

## Database

Responsible for persistence configuration.

Examples:

- `DATABASE_URL`

---

## Artificial Intelligence

Responsible for AI provider configuration.

Examples:

- `GEMINI_API_KEY`
- `GROQ_API_KEY`

---

## Application

Responsible for application-wide behavior.

Examples may include:

- Application name
- Environment
- Debug mode

---

## Logging

Responsible for application logging.

Examples:

- `LOG_LEVEL`

---

## Future Infrastructure

Future project phases may introduce configuration for:

- Scheduler
- Email
- Object storage
- Redis
- Monitoring
- External integrations

These settings should only be introduced when they become active project responsibilities.

---

```

---

# Secret Management

Sensitive information must never be committed to version control.

Secrets include, but are not limited to:

- API keys
- Access tokens
- Database credentials
- Private certificates

Approved locations include:

- Environment variables
- Local `.env` files (excluded from version control)
- Secure secret managers introduced during future deployment phases

Example files should never contain real secrets.

---

# Environment-Specific Configuration

## Development

Development configuration prioritizes:

- Simplicity
- Fast feedback
- Debugging support

Debug logging may be enabled.

---

## Testing

Testing configuration should:

- Be isolated from development databases.
- Use dedicated test configuration.
- Produce deterministic results.

---

## Production

Production configuration prioritizes:

- Security
- Reliability
- Observability

Debug features should be disabled unless explicitly required.

---

# Validation Rules

Configuration values should be validated before application startup completes.

Validation should ensure:

- Required values exist.
- URLs are valid.
- Enumerated values are supported.
- Numeric values fall within acceptable ranges.
- Invalid configuration produces clear startup errors.

Applications should fail during startup rather than at runtime when configuration is invalid.

---

# Traceability

Every configuration value documented here should have a corresponding implementation within the application's configuration module.

Configuration changes should:

1. Be documented in this file.
2. Be implemented in `app/core/config.py`.
3. Be reflected in implementation tasks when applicable.

This document remains the authoritative specification for application configuration.

---

# Future Configuration

Future project phases may introduce additional configuration for:

- Background scheduling
- Email notifications
- Browser automation
- File storage
- Monitoring
- Analytics
- Deployment infrastructure
- Cloud services

These settings should only be documented when they become active project responsibilities.

---

# Scope

This document defines application configuration.

It does **not** define:

- System architecture
- Database schema
- Source code implementation
- Technology selection
- Deployment procedures
- Infrastructure provisioning

Those responsibilities belong to their respective documents.

---

# Source of Truth

This document is the authoritative specification for application configuration.

The implementation source of truth is:

- `app/core/config.py`

Environment values are supplied by:

- Operating system environment variables
- Local `.env` files

Whenever implementation and this document differ, the documented configuration should be updated before introducing new configuration behavior.

---

# Future Evolution

Configuration should evolve intentionally as the project grows.

New configuration values should:

1. Solve a genuine project requirement.
2. Be documented before implementation.
3. Remain type-safe and validated.
4. Avoid duplication.
5. Preserve backward compatibility whenever practical.
6. Maintain a single authoritative source for every configuration value.
