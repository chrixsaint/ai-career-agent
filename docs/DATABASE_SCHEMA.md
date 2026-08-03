# Database Schema

> **Purpose:** This document defines the authoritative physical database schema for the AI Career Agent. It translates the conceptual data model described in `DATABASE_DESIGN.md` into a deterministic physical schema following the architectural standards established in `DATABASE_ARCHITECTURE.md`. It serves as the implementation specification for the project's SQLModel models and Alembic database migrations.

The conceptual database model is defined in `DATABASE_DESIGN.md`.

The persistence architecture and implementation standards are defined in `DATABASE_ARCHITECTURE.md`.

The implementation sequence for the persistence layer is defined in `IMPLEMENTATION_GUIDE.md`.

This document specifies the physical database structure only. It defines tables, columns, data types, constraints, relationships, indexes, and enumerations required for implementation. It does not define business logic, application behavior, or SQLModel implementation details.

---

---

### **database-schema.md**

# 1. Purpose and Scope

This document defines the authoritative physical database schema for the AI Career Agent. It serves as the bridge between the conceptual data model and the technical implementation, providing the field-level specifications required to implement **SQLModel** classes and **Alembic** migrations.

The scope includes all tables, enumerations, constraints, and indexes required to satisfy the system's functional requirements (**Phase 2 through Phase 5**). This specification adheres strictly to the standards defined in **`DATABASE_ARCHITECTURE.md`**.

---

# 2. Physical Schema Conventions

Every table in this schema specification implicitly includes the following "Standard Physical Columns" as mandated by the persistence architecture [324–326]:

| Physical Column | PostgreSQL Type | Responsibility                           |
| :-------------- | :-------------- | :--------------------------------------- |
| `id`            | `UUID`          | Primary Key; generated via UUID v4.      |
| `created_at`    | `TIMESTAMPTZ`   | Audit: Record creation; stored in UTC.   |
| `updated_at`    | `TIMESTAMPTZ`   | Audit: Last modification; stored in UTC. |

---

# 3. PostgreSQL Enumerations

To ensure strict data validation and "explicit behavior over implicit behavior", the following native PostgreSQL ENUM types shall be defined:

### `job_status`

- **Facts**: Required for the `Job` entity.
- **Architectural Decision**: Define values: `discovered`, `saved`, `applied`, `rejected`, `expired`.
- **Engineering Rationale**: Provides the state machine for the Job lifecycle through Phase 2 (Discovery) and Phase 5 (Saved opportunities).

### `employment_type`

- **Facts**: Required for filtering requirements **FR-008**.
- **Architectural Decision**: Define values: `full_time`, `part_time`, `contract`, `internship`, `other`.

### `experience_level`

- **Facts**: Required information for the `Job` entity.
- **Architectural Decision**: Define values: `entry`, `mid`, `senior`, `lead`, `executive`.

### `source_type`

- **Facts**: Required for the `Job Source` entity.
- **Architectural Decision**: Define values: `public_api`, `career_page`, `web_scraper`.

---

# 4. Core Domain Tables (Phase 2)

### `job`

- **Facts**: Primary unit of discovery.
- **Architectural Decision**: Map conceptual fields to physical types.
  - `fingerprint`: `TEXT` (Non-nullable, Unique Index).
  - `title`: `TEXT`
  - `description`: `TEXT`
  - `location`: `TEXT`
  - `remote_status`: `BOOLEAN`
  - `salary`: `TEXT` (stored as text to preserve currency/ranges until Phase 7)
  - `date_posted`: `TIMESTAMPTZ`
  - `deadline`: `TIMESTAMPTZ` (Nullable)
  - `job_url`: `TEXT` (Non-nullable)
  - `status`: `job_status` (Default: `discovered`)
  - `company_id`: `UUID` (Foreign Key to `company`)
  - `source_id`: `UUID` (Foreign Key to `job_source`)
- **Engineering Rationale**: The `fingerprint` is the physical gatekeeper for requirement **FR-005** (Duplicate detection).

### `company`

- **Facts**: Organization offering the job.
- **Architectural Decision**:
  - `name`: `TEXT` (Non-nullable)
  - `industry`: `TEXT`
  - `website`: `TEXT`
  - `headquarters`: `TEXT`
  - `careers_url`: `TEXT`
- **Engineering Rationale**: Company data provides the supporting metadata required for ranking and CV tailoring in later phases.

### `job_source`

- **Facts**: Identifies where jobs are collected.
- **Architectural Decision**:
  - `name`: `TEXT` (Non-nullable, Unique)
  - `type`: `source_type`
  - `base_url`: `TEXT`
  - `collection_config`: `JSONB`
- **Engineering Rationale**: Use of `JSONB` for `collection_config` satisfies **NFR-005** by allowing source-specific metadata (API keys, pagination offsets) to vary without schema changes.

---

# 5. Supporting Domain Tables

### `user_profile`

- **Facts**: Represents user preferences.
- **Architectural Decision**:
  - `preferred_locations`: `JSONB` (List of strings)
  - `preferred_job_types`: `JSONB` (List of `employment_type`)
  - `raw_experience_text`: `TEXT`
  - `raw_education_text`: `TEXT`
- **Engineering Rationale**: Storing complex preferences as `JSONB` supports the single-user assumption while remaining easy to query via the intelligence layer.

### `career_profile`

- **Facts**: User-defined career categories.
- **Architectural Decision**:
  - `name`: `TEXT` (Non-nullable, Unique)
  - `description`: `TEXT`
  - `matching_keywords`: `JSONB`
- **Engineering Rationale**: Matches the taxonomy required for Phase 3 filtering milestones.

---

# 6. Intelligence Tables (Phase 3)

### `job_recommendation`

- **Facts**: Output of the intelligence layer.
- **Architectural Decision**:
  - `job_id`: `UUID` (Foreign Key, Unique with `date_generated`)
  - `score`: `NUMERIC`
  - `position`: `INTEGER`
  - `ai_explanation`: `TEXT`
  - `date_generated`: `TIMESTAMPTZ`
- **Engineering Rationale**: The `score` uses `NUMERIC` for precision matching requirement **FR-009**.

---

# 7. Application Tables (Phase 4)

### `cv`

- **Facts**: Versions of user resumes.
- **Architectural Decision**:
  - `version`: `TEXT`
  - `file_path`: `TEXT`
  - `extracted_text`: `TEXT`
  - `user_id`: `UUID` (Foreign Key to `user_profile`)
- **Engineering Rationale**: `extracted_text` is an engineering necessity to avoid redundant PDF I/O during AI tailoring runs [Gap Analysis].

### `cover_letter`

- **Facts**: AI-generated documents.
- **Architectural Decision**:
  - `job_id`: `UUID` (Foreign Key)
  - `content`: `TEXT`
  - `version`: `TEXT`
- **Engineering Rationale**: Letters are associated with a specific job to satisfy **FR-016**.

---

# 8. Relationship Tables

### `career_profile_job_link`

- **Facts**: A Job belongs to multiple Career Profiles.
- **Architectural Decision**:
  - `job_id`: `UUID` (FK, `ondelete=CASCADE`)
  - `profile_id`: `UUID` (FK, `ondelete=CASCADE`)
  - **Constraint**: Unique combination of `job_id` + `profile_id`.
- **Engineering Rationale**: Implements the M2M relationship required for multi-category discovery.

---

# 9. Integrity Matrix

| Table                     | Constraint Name Template | Type        | Column(s)                     |
| :------------------------ | :----------------------- | :---------- | :---------------------------- |
| `job`                     | `uq_job_fingerprint`     | Unique      | `fingerprint`                 |
| `job`                     | `fk_job_company_id`      | Foreign Key | `company_id` → `company.id`   |
| `job`                     | `fk_job_source_id`       | Foreign Key | `source_id` → `job_source.id` |
| `job_source`              | `uq_job_source_name`     | Unique      | `name`                        |
| `career_profile_job_link` | `uq_profile_job`         | Unique      | `profile_id`, `job_id`        |

---

# 10. Index Matrix

| Table                | Index Name Template  | Type   | Column(s)     |
| :------------------- | :------------------- | :----- | :------------ |
| `job`                | `ix_job_status`      | B-Tree | `status`      |
| `job`                | `ix_job_date_posted` | B-Tree | `date_posted` |
| `job`                | `ix_job_fingerprint` | Unique | `fingerprint` |
| `job_recommendation` | `ix_rec_score`       | B-Tree | `score`       |

---

# 11. Future Schema Evolution

The following concerns are intentionally deferred:

1.  **Soft Deletion**: To be added in Phase 5 via `is_deleted` column.
2.  **Full-Text Search**: Gin/Gist indexes on `job.description` deferred to Phase 5.
3.  **Application Tracking**: Detailed `application` table deferred to Phase 6.

---

# 12. Final Verification

- **FR-005 Compliance**: Satisfied by `job.fingerprint` + `uq_job_fingerprint`.
- **Architectural Alignment**: All IDs are UUID; all timestamps are UTC TIMESTAMPTZ.
- **Persistence Standards**: Uses `lower_snake_case` and singular form.

---

**Last Updated**: 2026-08-03
**Status**: Authoritative Physical Specification
**Traceability**: DATABASE_DESIGN.md, DATABASE_ARCHITECTURE.md [320–346]
