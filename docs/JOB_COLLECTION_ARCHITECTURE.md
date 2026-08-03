# Job Collection Architecture

> **Purpose:** This document defines the architecture of the Job Collection subsystem. It specifies how external job sources are integrated into the AI Career Agent, how providers are organized, and how raw job postings enter the processing pipeline.

Implementation details belong in the source code.

System-wide architecture belongs in `ARCHITECTURE.md`.

Implementation sequencing belongs in `IMPLEMENTATION_GUIDE.md`.

Database persistence belongs in `DATABASE_ARCHITECTURE.md` and `DATABASE_SCHEMA.md`.

---

# Architectural Goals

The Job Collection subsystem is designed to be:

- Modular
- Extensible
- Provider-independent
- Maintainable
- Testable
- Asynchronous
- Standards-based

Each collector should own one responsibility.

---

### Responsibilities

The Job Collection subsystem is responsible for the transition from **external provider state** to **internal raw state**.

- **Retrieve**: Fetch data via HTTP, Feed retrieval, or selector-based parsing.
- **Authenticate**: Securely apply credentials without hardcoding values (**NFR-004**).
- **Validate**: Verify that the provider response matches the expected structure.
- **Map**: Transform provider-specific fields (e.g., Jooble `snippet` or Lever `descriptionPlain`) into the system's `RawJobCapture` Pydantic model.
- **Comply**: Adhere to `robots.txt`, rate limits, and nightly processing windows (e.g., EURAXESS 02:00-06:00).
- **Report**: Log retrieval metrics, duration, and remaining rate limit quotas.

````


The Job Collection subsystem is **not** responsible for:

- Duplicate detection
- Job ranking
- Recommendation generation
- AI reasoning
- Database persistence

Those responsibilities belong to downstream architectural layers.

---

# Position Within the System

The Job Collection subsystem is the first stage of the application pipeline.

### Collector Orchestration
Collectors are instantiated and managed through a centralized orchestration pattern to ensure loose coupling.

#### Collector Factory
A `CollectorFactory` is responsible for initializing concrete collectors based on the `source_type` and `name` attributes defined in the `job_source` database table. This ensures that adding a new provider (e.g., Ashby) only requires a new class implementation and a database record, adhering to **NFR-005**.

#### Execution Strategy
*  **Async Concurrency**: Collectors utilize `httpx.AsyncClient` for non-blocking I/O.
*  **Dependency Injection**: The factory and its collectors are provided to the collection service via FastAPI's `Depends()` system.
```

```text
External Providers
        │
        ▼
 Job Collection
        │
        ▼
 Job Processing
        │
        ▼
 Job Intelligence
        │
        ▼
 AI Assistance
        │
        ▼
 User
````

---

### Collector Hierarchy

The subsystem follows the Strategy Pattern. Every concrete provider inherits from the most appropriate abstraction to maximize code reuse and ensure interface consistency.

#### BaseCollector (ABC)

The root interface for all job discovery components.

- **Validation Contract**: Mandates the use of Pydantic models for raw data output to satisfy **CODING_STANDARDS.md**.
- **Fingerprinting**: Defines the standard hashing algorithm used to generate unique IDs for initial capture logging (**FR-005**).
- **Identification**: Manages custom `User-Agent` strings to ensure compliance with provider Terms of Service.

#### APICollector

Specialized for REST-based providers (e.g., Jooble, Adzuna, Remote OK).

- **Resilience**: Implements centralized rate limiting (via `aiolimiter`) and backoff retry strategies.
- **Auth Handling**: Standardized parsing of API keys and App IDs from `configuration.md`.

#### FeedCollector

Specialized for periodic XML, RSS, or Atom retrieval (e.g., EURAXESS).

- **Schema Validation**: Verifies incoming XML against vendor-supplied XSD files (e.g., EURAXESS guidelines).
- **Madgex Integration**: Serves as the base for platform-specific feeds used by Nature and Science Careers.

#### ATSCollector (extends APICollector)

Specialized for Applicant Tracking Systems (e.g., Greenhouse, Lever, Ashby).

- **Multi-Token Orchestration**: Implements logic to iterate through multiple company-specific board tokens stored in the `job_source.collection_config` JSONB field.

````
```text
BaseCollector (ABC)
        │
        ├──────────────┐
        │              │
        ▼              ▼
APICollector     FeedCollector
        │              │
        │              │
        ▼              ▼
ATSCollector   HTMLCollector
        │
        ▼
Concrete Providers
````

---

# Collector Types

## BaseCollector

Defines the common interface for all job providers.

Responsibilities include:

- lifecycle management
- fetch interface
- normalization contract
- error reporting
- logging hooks

Every collector must inherit from BaseCollector.

---

## APICollector

Responsible for REST-based providers.

Responsibilities include:

- HTTP requests
- authentication
- pagination
- retries
- timeout handling
- rate limiting
- JSON parsing

Examples include:

- Jooble
- Adzuna
- Remote OK

---

## FeedCollector

Responsible for XML, RSS, or Atom feeds.

Responsibilities include:

- XML retrieval
- feed parsing
- schema validation
- update scheduling

Examples include:

- EURAXESS

---

## ATSCollector

Specialized collector for Applicant Tracking Systems.

ATSCollector extends APICollector.

Responsibilities include:

- company token management
- company iteration
- ATS-specific normalization

Examples include:

- Greenhouse
- Lever
- Ashby
- Workable

---

## HTMLCollector

Responsible for sources without official APIs or feeds.

Responsibilities include:

- HTML retrieval
- selector-based extraction
- robots.txt compliance
- change tolerance

HTML parsing should only be used when official APIs or feeds are unavailable.

---

### Provider Mapping

| Provider            | Sub-Base      | Integration Method               |
| ------------------- | ------------- | -------------------------------- |
| **Jooble**          | APICollector  | REST API (POST)                  |
| **EURAXESS**        | FeedCollector | XML Retrieval (URL)              |
| **Greenhouse**      | ATSCollector  | Job Board API (JSON)             |
| **Adzuna**          | APICollector  | REST API (GET)                   |
| **Lever**           | ATSCollector  | Postings API (JSON)              |
| **Nature Careers**  | FeedCollector | Madgex Platform Feed             |
| **Science Careers** | FeedCollector | Madgex Platform Feed             |
| **Ashby**           | ATSCollector  | Partner API / Feed               |
| **Workable**        | ATSCollector  | REST API                         |
| **Remote OK**       | APICollector  | JSON Feed                        |
| **EURES**           | APICollector  | Official EU API (Phase 7 Review) |

```

---

# Provider Priority

## Phase 2

Primary implementation:

- Jooble
- EURAXESS
- Greenhouse

These providers provide the highest value for Romanian, EU, biomedical, research, and graduate opportunities.

---

## Future Expansion

Additional providers include:

- Adzuna
- Lever
- Ashby
- Workable
- Remote OK
- Nature Careers
- Science Careers
- EURES

Additional providers may be introduced without architectural changes.

---

# Shared Responsibilities

All collectors should provide:

- standardized logging
- standardized exception handling
- timeout management
- retry strategy
- User-Agent management
- request validation
- response validation
- normalization contract

Common functionality should remain in shared abstractions whenever practical.

---

# Normalization

Collectors retrieve external data.

They do not determine the application's internal representation.

Every collector returns standardized raw job data suitable for the Job Processing layer.

Normalization rules should remain provider-independent.

---

# Authentication

Authentication mechanisms vary by provider.

Supported methods include:

- API Key
- App ID / API Key
- Public endpoint
- Organization token

Authentication details belong in `configuration.md`.

Collectors should never hardcode credentials.

---

# Rate Limiting

Collectors must respect provider rate limits.

Rate limiting should be centralized and configurable.

Limits should be loaded from application configuration rather than embedded in collector implementations.

---

# Error Handling

Collectors should normalize provider-specific failures into project-defined exceptions.

Examples include:

- Authentication failures
- Timeout errors
- Rate limit responses
- Invalid responses
- Service outages

Business logic should never depend on provider-specific exceptions.

---

# Logging

Collectors should emit structured logs for:

- requests
- responses
- failures
- retries
- rate limiting
- execution duration

Logging standards are defined in `CODING_STANDARDS.md`.

---

# Testing

Every collector should support:

- unit testing
- mocked HTTP responses
- integration testing
- provider-independent verification

Testing should avoid live provider dependencies whenever practical.

---

# Extensibility

New providers should require:

- one collector implementation
- configuration entries
- provider registration

No existing collectors should require modification when introducing new providers.

---

### Relationship to Other Documents

This document defines the physical architecture of the Job Collection subsystem. It is governed by:

- **REPOSITORY_STANDARD.md**: Documentation taxonomy and location rules.
- **ARCHITECTURE.md**: System layering and data flow.
- **CODING_STANDARDS.md**: Mandates the use of `abc.ABC`, `async def`, and Pydantic models.
- **DATABASE_SCHEMA.md**: Defines the `source_type` and `collection_config` fields used by collectors.
- **configuration.md**: Definitive registry for API keys and rate limit settings.
- **IMPLEMENTATION_GUIDE.md**: Sequences Phase 2 collection milestones.

```

---

# Scope

This document defines:

- collector hierarchy
- provider organization
- architectural responsibilities
- provider mapping
- extension strategy

It does not define:

- implementation details
- provider credentials
- database schema
- AI logic
- job ranking
- recommendation algorithms

---

# Future Evolution

The Job Collection subsystem should evolve by adding new providers rather than modifying existing abstractions.

Architectural changes should:

1. Preserve provider independence.
2. Maintain the Strategy Pattern.
3. Minimize duplication.
4. Respect provider Terms of Service.
5. Preserve compatibility with the Job Processing layer.

```

```

```

```
