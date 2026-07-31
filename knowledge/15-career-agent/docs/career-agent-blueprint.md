---
title: AI Career Agent — Engineering Blueprint
source: knowledge/inbox/career-agent-blueprint.md
date: 2026-07-31
tags: [career-agent, blueprint, architecture]
owner: @chrixsaint
confidence: high
summary: Engineering blueprint: product vision, phased roadmap, recommended architecture and folder structure for the AI Career Agent project.
---

# AI Career Agent — Engineering Blueprint

**Author role:** Staff AI Engineer / Senior Backend Engineer / Technical Architect
**Audience:** Solo engineer building a production-quality portfolio project
**Stack:** Python, FastAPI, SQLite → Postgres, Playwright, Claude API, WSL/Ubuntu

---

## 1. Product Vision

### What this becomes

A **human-in-the-loop job search automation platform**, not a "job search bot." The system's job is to eliminate the _mechanical_ labor of applying (searching, reading, matching, drafting) while leaving every _judgment_ decision (which job to pursue, what to say, what to submit) to you. Think of it as **Bloomberg Terminal for your own job search**: one system that ingests noisy, multi-source data, normalizes it, ranks it against your goals, and hands you a short list with drafts ready for review.

The long-term product has three pillars:

| Pillar         | Description                                                                                          |
| -------------- | ---------------------------------------------------------------------------------------------------- |
| **Sourcing**   | Continuously discover roles across boards, internships, and startups; normalize into one schema.     |
| **Reasoning**  | Match, rank, and explain _why_ a job fits (or doesn't) using your profile + the JD.                  |
| **Generation** | Produce tailored CVs, cover letters, and outreach drafts — always as _drafts_, never auto-submitted. |

A secondary but important pillar is **analytics**: response rates, time-to-interview, which channels/tailoring strategies actually convert. This is what turns "a scraper with a GPT wrapper" into an actual engineering portfolio piece — it shows you can build a system that _learns from its own outcomes_.

### MVP vs. later versions — how a professional scopes this

A staff engineer's instinct here is **ruthless vertical slicing**: build one full pipeline (source → match → generate → track) for a _single_ job board before adding breadth. Breadth-first (13 features, each half-built) is the #1 failure mode of solo AI projects — it produces something that demos well and works never.

|                | MVP (Weeks 1–4)                                                                          | V2 (Weeks 5–8)                                                  | V3+ (Ongoing)                                                       |
| -------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Sourcing**   | 1 job board (API-based, e.g. RemoteOK or Greenhouse job boards), manual "add job by URL" | 2–3 boards, internship boards, remote/visa detection heuristics | Startup boards (Wellfound), multi-source dedupe, scheduled crawling |
| **Matching**   | Simple keyword + embedding similarity vs. profile                                        | LLM-based structured match with reasoning/explanations          | Learned ranking from historical outcomes                            |
| **Generation** | Tailored CV bullet suggestions (text only)                                               | Full CV tailoring + cover letter generation                     | Outreach email drafts, recruiter message generation                 |
| **Tracking**   | Manual status field per application                                                      | Full application lifecycle + interview stages                   | Analytics dashboard, funnel conversion metrics                      |
| **Interface**  | CLI / FastAPI + Swagger only                                                             | Minimal HTML dashboard                                          | Full frontend (React/Next.js)                                       |

**Definition of MVP done:** you can run one command, get 10 ranked jobs from one source with a tailored CV draft for the top 3, and mark one as "applied" — end to end, no manual data wrangling.

---

## 2. Feature Roadmap

Each phase is designed so its output is **usable on its own** — you should never be mid-phase with nothing to show.

### Phase 0 — Foundations

- **Purpose:** Establish the skeleton so every later phase has somewhere to plug in.
- **Outcome:** FastAPI app boots, SQLite schema migrates, config/secrets loading works, `pytest` runs (even with 1 trivial test), logging is structured.
- **Dependencies:** None.
- **Why first:** Every other phase writes code _into_ this scaffold. Building features before scaffolding means a rewrite later.

### Phase 1 — Ingestion (single source)

- **Purpose:** Get real job data into your database from one reliable, structured source (prefer an API/JSON feed over scraping for v1 — e.g. Greenhouse/Lever public job board JSON endpoints, or RemoteOK's API).
- **Outcome:** `jobs` table populated on a schedule/manual trigger; deduped by a content hash.
- **Dependencies:** Phase 0 DB + config.
- **Why before Phase 2:** You cannot design a matching algorithm against data you don't have. Real JD text exposes edge cases (missing fields, HTML-polluted descriptions) that shape your schema.

### Phase 2 — Job Description Extraction & Normalization

- **Purpose:** Turn messy HTML/PDF job descriptions into a structured record (title, seniority, skills, location, remote flag, salary if present, visa language).
- **Outcome:** A `job_description_parser` service — regex/heuristics first, Claude-assisted extraction second (structured output via tool-use/JSON schema).
- **Dependencies:** Phase 1 (needs raw JD text).
- **Why before matching:** Matching against unstructured text is unreliable and unexplainable. Structure first, reason second.

### Phase 3 — Candidate Profile Model

- **Purpose:** Formalize _your_ data — skills, experience, preferences (locations, visa needs, seniority target, must-haves) — as structured, versioned data, not a hardcoded prompt string.
- **Outcome:** `profile` table/JSON, editable without code changes.
- **Dependencies:** None technically, but sits here because you now understand what fields jobs expose, so you know what to match against.

### Phase 4 — Matching & Ranking Engine

- **Purpose:** Score each job against the profile with an explainable rationale, not just a black-box number.
- **Outcome:** `match_score`, `match_reasoning` per job; a ranked list endpoint.
- **Dependencies:** Phases 2 + 3.
- **Why before generation:** You don't want to spend LLM tokens tailoring a CV for a job that's a bad fit. Ranking is the filter that makes generation economical and relevant.

### Phase 5 — Document Generation (CV tailoring, cover letters)

- **Purpose:** Generate draft artifacts a human reviews and edits.
- **Outcome:** `generated_documents` table; Claude-generated CV bullet rewrites + cover letter drafts, stored with the exact job + profile version used (reproducibility).
- **Dependencies:** Phase 4 (only generate for jobs above a score threshold).
- **Why before outreach:** Cover letters and CVs are the core "must be right" artifacts; outreach messages are lower-stakes and can reuse the same generation pipeline once it's proven.

### Phase 6 — Application Tracking & Interview Pipeline

- **Purpose:** Track lifecycle: sourced → matched → drafted → applied → interviewing → offer/rejected.
- **Outcome:** `applications` table with status history (append-only log, not just a mutable field).
- **Dependencies:** Phase 5.
- **Why not earlier:** Nothing to track until documents exist and jobs are being applied to.

### Phase 7 — Browser Automation (Playwright)

- **Purpose:** Automate the _reading_ of JDs from sites without APIs, and semi-automate _filling_ application forms (never auto-submit).
- **Outcome:** Playwright scripts behind a queue/worker, with human-confirm-before-submit as a hard rule.
- **Dependencies:** Phases 1–2 (you already know what data shape you need before scraping for it).
- **Why this late:** Playwright automation is the most brittle, highest-maintenance part of the system (selectors break, anti-bot measures, CAPTCHAs). You want your core data model and generation pipeline stable _before_ you invest in fragile scraping — otherwise every schema change breaks scrapers too.

### Phase 8 — Multi-source expansion (internships, startups, visa/remote detection)

- **Purpose:** Broaden coverage now that the pipeline is proven end-to-end on one source.
- **Outcome:** Adapter pattern for sources; visa/remote detection as a classification step (heuristic + LLM fallback).
- **Dependencies:** Phases 1–7 all stable.

### Phase 9 — Analytics

- **Purpose:** Turn tracked data into insight — response rate by source, by tailoring strategy, time-to-response.
- **Outcome:** Aggregation queries/dashboard.
- **Dependencies:** Phase 6 needs weeks of real data to be meaningful.
- **Why last:** Analytics on no data is a vanity feature. This is intentionally the "polish" phase.

---

## 3. Recommended Architecture

````mermaid
flowchart TB
    subgraph Sources["Job Sources"]
        A1[Job Board APIs<br/>Greenhouse/Lever/RemoteOK]
        A2[Startup Boards<br/>Wellfound]
        A3[Company Career Pages<br/>Playwright scraper]
    end

    subgraph Ingestion["Ingestion Layer"]
        B1[Source Adapters]
        B2[Dedup + Normalize]
    end

    subgraph Core["FastAPI Backend"]
        C1[Job Description Parser<br/>heuristics + Claude structured extraction]
        C2[Matching / Ranking Engine]
        C3[Document Generator<br/>CV / Cover Letter / Outreach]
        C4[Application Tracker]
        C5[Analytics Service]
    end

    subgraph AI["AI Layer"]
        D1[Claude API<br/>extraction, matching rationale, generation]
        D2[Embeddings<br/>profile-to-JD similarity]
    end

    subgraph Data["Persistence"]
        E1[(SQLite → Postgres)]
        E2[File Storage<br/>generated docs, CVs]
    end

    subgraph Automation["Browser Automation"]
        F1[Playwright Workers]
        F2[Job Queue<br/>e.g. APScheduler / Celery+Redis later]
    end

    subgraph Frontend["Future Frontend"]
        G1[React/Next.js Dashboard]
        G2[CLI / Swagger UI — MVP interface]
    end

    A1 --> B1
    A2 --> B1
    A3 --> F1 --> B1
    B1 --> B2 --> E1
    E1 --> C1 --> D1
    C1 --> E1
    E1 --> C2 --> D2
    C2 --> E1
    E1 --> C3 --> D1
    C3 --> E2
    C3 --> E1
    E1 --> C4 --> E1
    E1 --> C5
    F2 --> F1
    C2 & C3 & C4 & C5 --> G2
    G2 --> G1
    ```

---

## 4. Recommended Folder Structure

````

career-agent/
├── app/
│ ├── main.py # FastAPI app entrypoint
│ ├── config.py # Settings via pydantic-settings, env-based
│ ├── api/
│ │ ├── routes/
│ │ │ ├── jobs.py
│ │ │ ├── applications.py
│ │ │ ├── documents.py
│ │ │ └── analytics.py
│ │ └── deps.py # shared FastAPI dependencies (DB session, auth)
│ ├── core/
│ │ ├── logging.py # structured logging setup
│ │ └── exceptions.py # custom exception classes + handlers
│ ├── ingestion/
│ │ ├── base.py # SourceAdapter interface
│ │ ├── sources/
│ │ │ ├── greenhouse.py
│ │ │ ├── remoteok.py
│ │ │ └── wellfound.py
│ │ └── dedupe.py
│ ├── parsing/
│ │ ├── heuristics.py
│ │ └── llm_extractor.py
│ ├── matching/
│ │ ├── embeddings.py
│ │ ├── ranker.py
│ │ └── rationale.py # Claude-based explanation generation
│ ├── generation/
│ │ ├── cv_tailor.py
│ │ ├── cover_letter.py
│ │ └── outreach.py
│ ├── tracking/
│ │ ├── models_events.py
│ │ └── service.py
│ ├── automation/
│ │ ├── playwright_worker.py
│ │ └── scripts/ # per-site interaction scripts
│ ├── ai/
│ │ ├── claude_client.py # thin wrapper: retries, rate limits, cost logging
│ │ └── prompts/ # versioned prompt templates (not inline strings)
│ ├── db/
│ │ ├── models.py # SQLAlchemy/SQLModel models
│ │ ├── session.py
│ │ └── migrations/ # Alembic
│ └── analytics/
│ └── queries.py
├── tests/
│ ├── unit/
│ ├── integration/
│ └── fixtures/
├── scripts/ # one-off CLI utilities (backfill, manual runs)
├── docs/
│ ├── adr/ # Architecture Decision Records
│ └── schema.md
├── .env.example
├── pyproject.toml
├── alembic.ini
├── docker-compose.yml # for future Postgres/Redis
└── README.md

````

---

## 5. Database Design (v1 schema)

```mermaid
erDiagram
    COMPANIES ||--o{ JOBS : posts
    JOBS ||--o{ APPLICATIONS : "applied via"
    JOBS ||--o{ MATCH_SCORES : scored_by
    PROFILE ||--o{ MATCH_SCORES : "matched against"
    APPLICATIONS ||--o{ APPLICATION_EVENTS : has
    APPLICATIONS ||--o{ GENERATED_DOCUMENTS : uses
    PROFILE ||--o{ GENERATED_DOCUMENTS : "generated from"

    COMPANIES {
        int id PK
        string name
        string website
        string industry
        bool known_visa_sponsor
    }
    JOBS {
        int id PK
        int company_id FK
        string title
        string source
        string external_id
        string raw_description
        string parsed_json
        string location
        bool is_remote
        bool visa_sponsorship
        string seniority
        string content_hash
        datetime posted_at
        datetime ingested_at
    }
    PROFILE {
        int id PK
        int version
        string data_json
        datetime created_at
    }
    MATCH_SCORES {
        int id PK
        int job_id FK
        int profile_id FK
        float score
        string reasoning
        string missing_requirements
        datetime scored_at
    }
    GENERATED_DOCUMENTS {
        int id PK
        int application_id FK
        int profile_id FK
        string doc_type
        string content
        string prompt_version
        string model_used
        datetime generated_at
    }
    APPLICATIONS {
        int id PK
        int job_id FK
        string status
        datetime applied_at
    }
    APPLICATION_EVENTS {
        int id PK
        int application_id FK
        string event_type
        string notes
        datetime occurred_at
    }
````
