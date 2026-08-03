# Database Architecture

> **Purpose:** This document defines the architectural standards governing the physical persistence layer of the AI Career Agent. It translates the conceptual model defined in `DATABASE_DESIGN.md` into a consistent persistence architecture for SQLModel, PostgreSQL, and Alembic.

This document is the authoritative source of truth for all persistence-layer architectural decisions.

The conceptual database model is defined in `DATABASE_DESIGN.md`.

The implementation sequence is defined in `IMPLEMENTATION_GUIDE.md`.

The overall system architecture is defined in `ARCHITECTURE.md`.

---

---

### **database-architecture.md**

# Purpose

### Responsibility

This document serves as the **authoritative technical bridge** between the high-level conceptual database design and the physical SQLModel/PostgreSQL implementation. It defines the irreversible architectural decisions, technical constraints, and implementation patterns required to ensure a consistent, scalable, and maintainable persistence layer.

### Scope

The scope is strictly limited to the **Data Persistence** layer. It governs the technical behavior of data at rest, including schema definition, record auditing, and migration workflows.

### Architectural Boundaries

- **Domain Boundary**: This document defines the state of data. It does not define behavior (Services) or presentation (API Schemas).
- **Tooling Boundary**: Standards are specific to **SQLModel** and **PostgreSQL**.
- **Infrastructure Boundary**: It stops before the physical environment configuration (e.g., Docker volumes), which is owned by operational documentation.

### Relationships

- **DATABASE_DESIGN.md**: This document is the physical successor, providing the "How" for the conceptual "What" defined in the high-level design.
- **IMPLEMENTATION_GUIDE.md**: Acts as the technical prerequisite for the Phase 2 persistence milestones.
- **SQLModel**: Defines the Python-level inheritance and type-mapping strategy.
- **Alembic**: Establishes the versioning and evolution standards for the physical schema.

---

# Identifier Strategy

### Primary Key Strategy

**Engineering Inference**: The project shall adopt **UUID (v4)** as the primary identifier strategy for all core domain entities (`Job`, `Company`, `JobSource`, `CareerProfile`, `UserProfile`).

- **Justification**: UUIDs support the project's goal of "Scalability" and "Extensibility" by allowing for safe data merging from distributed collection sources and enabling the generation of unique IDs in the application layer before the record reaches the database.

### Identifier Consistency

All primary key fields shall be named `id` across all tables to ensure architectural consistency and simplify generic CRUD implementation.

### Future Extensibility

The use of UUIDs ensures the system can transition to a multi-user or distributed architecture without the risk of primary key collisions associated with auto-incrementing integers.

---

# Audit and Timestamp Strategy

### Field Definitions

Every table must include the following audit fields:

- `created_at`: The timestamp when the record was first persisted.
- `updated_at`: The timestamp of the most recent modification.

### Timezone Policy

**Facts**: The project prioritizes "Explicit behavior over implicit behavior".
**Engineering Inference**: All timestamp fields shall be stored using the **UTC** timezone. In PostgreSQL, this maps to the `TIMESTAMP WITH TIME ZONE` (`TIMESTAMPTZ`) type to ensure absolute temporal accuracy across different deployment regions.

### Audit Philosophy

Auditing is a first-class citizen of the persistence layer. The system favors **immutability for historical context** (e.g., job details at the time of discovery) while using timestamps to track the lifecycle of mutable state (e.g., user approval status).

---

# Data Integrity Principles

### Primary Keys

Every record must be uniquely identifiable via a non-null, immutable primary key.

### Foreign Keys

**Engineering Inference**: Referential integrity shall be enforced strictly at the database level using physical foreign key constraints. This ensures the "Consistency" mandated by coding standards is maintained even if application-level logic fails.

### Uniqueness

Physical uniqueness constraints shall be applied to any field serving as a natural identifier, including job fingerprints, source base URLs, and profile names.

### Nullability

Fields are **non-nullable by default**. Optional data (e.g., a job's application deadline) must be explicitly permitted via the `nullable=True` property in the model definition to prevent accidental data loss.

### Referential Integrity

All foreign keys shall define explicit `ondelete` actions (e.g., `CASCADE` for transient recommendations or `RESTRICT` for core companies) to maintain structural integrity.

### Business Rule Enforcement

Whenever practical, critical business rules (e.g., "no duplicate jobs from the same source") shall be enforced via database-level unique constraints.

---

# Duplicate Detection Strategy

### Fingerprint Philosophy

**Facts**: **FR-005** mandates the removal of duplicate job postings. The implementation guide specifies a "fingerprinting algorithm" hashing job attributes.
**Engineering Inference**: The `Job` model shall contain a dedicated `fingerprint` field. This field is a deterministic hash of the job's title, company name, and location.

### Uniqueness Enforcement

The `fingerprint` field shall have a **Unique Index** in the PostgreSQL schema. This turns the database into the final gatekeeper against redundant processing, ensuring the integrity of the job collection pipeline.

---

# Session and Connection Management

### Engine Ownership

The database engine shall be initialized as a singleton at the application level to manage the connection pool efficiently.

### Session Lifecycle

**Facts**: Phase 2 requires an asynchronous session dependency.
**Engineering Inference**: The application shall use **AsyncSession** for all I/O-bound database work. Sessions shall be request-scoped, created when a request starts and closed automatically when it ends using FastAPI's dependency injection system.

### Dependency Injection

All database access in the API layer must be performed through the `Depends(get_session)` pattern. Manual session creation within route handlers is prohibited.

### Transaction Ownership

Transactions shall be managed explicitly within the service layer. A successful business operation must end with a `session.commit()`, while failures should rely on automatic rollback upon session closure.

---

# PostgreSQL Type Strategy

### Mapping Philosophy

- **UUID**: Mapped to native PostgreSQL `UUID` type for optimal performance.
- **DateTime**: Mapped to `TIMESTAMP WITH TIME ZONE`.
- **JSON / JSONB**: Flexible metadata (e.g., raw API responses) shall be stored as **`JSONB`** to allow for efficient indexing of unstructured data.
- **Text**: Long-form text (e.g., job descriptions) shall use the PostgreSQL `TEXT` type to avoid the performance penalties of arbitrary length limits.
- **Enum**: Controlled states (e.g., job status, employment type) shall use native PostgreSQL `ENUM` types for strict data validation.

---

# Model Hierarchy

### Base Model Philosophy

The model hierarchy follows the principle of **"Composition over duplication"**.

### Mixins

Models shall utilize shared mixins to standardize cross-cutting concerns:

- **`IDMixin`**: Standardizes the UUID primary key definition.
- **`TimestampMixin`**: Standardizes the `created_at` and `updated_at` fields.

### Inheritance

Core domain models shall inherit from `SQLModel` and the appropriate mixins. Models shall distinguish between `table=True` (physical schema) and their data-only counterparts to maintain separation between the database and API contracts.

---

# Physical Naming Standards

### Table Names

Tables shall use **lower_snake_case** and **singular form** (e.g., `job`, `job_source`) to ensure consistency and PostgreSQL compatibility.

### Constraint Names

Constraint names shall follow a deterministic template: `fk_{table}_{column}` or `uq_{table}_{column}` to simplify migration management.

### Indexes

Indexes shall be named explicitly: `ix_{table}_{column}`. Indexes are mandatory for all foreign keys and frequently searched fields.

### Foreign Keys

Foreign key columns shall follow the `target_entity_id` naming convention (e.g., `company_id`).

---

# Relationship Enforcement

### Relationship Ownership

The "Many" side of a relationship (e.g., `Job`) owns the foreign key to the "One" side (e.g., `Company`).

### Cascade Philosophy

**Engineering Inference**: Cascade deletes are permitted for derived data (e.g., deleting a Job deletes its Recommendations) but restricted for core entities (e.g., cannot delete a Company if Jobs are attached) to prevent accidental historical data loss.

### Loading Philosophy

**Engineering Inference**: To prevent "N+1" query issues and ensure async compatibility, relationships shall use **`selectin`** loading by default.

### Back-population Philosophy

All relationships must define `back_populates` on both models to ensure the Python object graph remains synchronized during complex job processing.

---

# Migration Standards

### Migration Philosophy

Migrations are the **immutable history** of the schema. The database state must be entirely reproducible through the migration chain.

### Revision Standards

**Facts**: The implementation guide requires "static, reversible migrations".
**Engineering Inference**: Revision files shall use a `YYYYMMDD_slug` naming template (e.g., `20260802_init_core_tables.py`) to ensure absolute chronological ordering in the `versions/` directory.

### Rollback Expectations

Every migration must be tested for reversibility. A `downgrade()` function that completely cleans up the `upgrade()` changes is mandatory.

### Schema Evolution Principles

Schema changes shall be additive whenever possible to minimize risk. Breaking changes (e.g., dropping columns) must be performed in coordinated phases across the processing pipeline.

---

# Future Considerations

The following persistence concerns are intentionally deferred beyond Phase 2:

- **Soft Deletes**: Not required until user-facing "saved opportunities" management in Phase 5.
- **Database Partitioning**: Deferred until Phase 7 performance optimization.
- **Full-Text Search Indexing**: Deferred until the "Search and filtering" milestone in Phase 5.
- **Replication/High Availability**: Deferred until production deployment preparation.

---

**Last Updated**: 2026-08-02
**Status**: Active / Authoritative
**Owner**: Persistence Subsystem Architecture
**Traceability**: FR-001, FR-004, FR-005, NFR-001, NFR-002 [673–676]
