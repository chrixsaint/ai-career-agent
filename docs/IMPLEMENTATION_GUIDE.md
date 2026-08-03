# Implementation Guide

> **Purpose:** This document expands the milestones defined in `ROADMAP.md` into an engineering execution guide.

It defines:

- implementation objectives
- completion criteria
- execution tasks
- verification steps
- definitions of done

This document complements `ROADMAP.md`.

It does not replace:

- Project Vision
- Requirements
- Architecture
- Technology Stack
- Repository Standards

---

### **Phase 1 – Foundation**

#### **Milestone: Repository organization**

- **Objective**: Establish the 6-layer repository structure required for modular separation of concerns.
- **Official Documentation**: [uv: Structure and files](https://docs.astral.sh/uv/concepts/projects/layout/).
- **Completion Criteria**: The directory tree reflects the responsibilities defined in the repository standard.
- **Execution Tasks**:
  1. Initialize the project using `uv init --app`.
  2. Create mandatory directories: `app/`, `tests/`, `docs/`, `knowledge/`, and `.claude/`.
  3. Initialize core project documentation files in `docs/`.
- **Verification**: Run `ls -R` to verify the structure against the Repository Layers table.
- **Definition of Done**: The repository structure is established and follows the **Single Responsibility Principle** for documentation and code.

#### **Milestone: Development environment**

- **Objective**: Configure local development tools and AI collaboration frameworks.
- **Official Documentation**: [uv: First steps](https://docs.astral.sh/uv/getting-started/first-steps/).
- **Completion Criteria**: A reproducible Python environment is active and managed by `uv`.
- **Execution Tasks**:
  1. Install `uv` using the standalone installer.
  2. Synchronize the environment with `uv sync`.
  3. Configure `AI_ENGINEERING_GUIDE.md` with project-specific instructions.
- **Verification**: Verify the environment state with `uv venv` and confirm `AI_ENGINEERING_GUIDE.md` is loaded.
- **Definition of Done**: The environment is stable, documented, and ready for incremental development.

#### **Milestone: FastAPI application setup**

- **Objective**: Initialize the application entry point and modular router assembly.
- **Official Documentation**: [FastAPI: Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/).
- **Completion Criteria**: A functional FastAPI instance is registered with at least one modular router.
- **Execution Tasks**:
  1. Create `app/main.py` and instantiate the `FastAPI` class.
  2. Implement `app/api/routers/system.py` with a health check.
  3. Register the router in `main.py` using `app.include_router()`.
- **Verification**: Start the server with `fastapi dev` and verify the `/health` endpoint and Swagger UI.
- **Definition of Done**: The application entry point contains no business logic and uses modular subpackages.

#### **Milestone: Dependency management with uv**

- **Objective**: Establish a secure and deterministic workflow for managing external libraries.
- **Official Documentation**: [uv: Managing dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/).
- **Completion Criteria**: All dependencies are declared in `pyproject.toml` and locked in `uv.lock`.
- **Execution Tasks**:
  1. Add core dependencies: `fastapi[standard]`, `pydantic-settings`, and `sqlmodel`.
  2. Commit `pyproject.toml` and `uv.lock` together.
- **Verification**: Run `uv lock --check` to ensure the lockfile is up to date.
- **Definition of Done**: The project uses the machine-readable source of truth for all dependencies.

###### **Milestone: Documentation framework**

- **Objective**: Establish a structured knowledge base and evidence-based research methodology.
- **Official Documentation**: [AI Engineering Guide](AI_ENGINEERING_GUIDE.md).
- **Completion Criteria**: The repository contains active documentation for vision, requirements, architecture, and engineering standards.
- **Execution Tasks**:
  1. Define the **Document Taxonomy** and naming conventions in REPOSITORY_STANDARD.md.
  2. Implement the **NotebookLM Research Methodology**.
  3. Initialize AI_ENGINEERING_GUIDE.md and AI_DEVELOPMENT_PLAYBOOK.md.
- **Verification**: Review documentation for adherence to the **Single Responsibility Principle**.
- **Definition of Done**: Documentation provides a stable, authoritative source of truth for the project.

```
#### **Milestone: Initial testing framework**

- **Objective**: Establish an asynchronous testing baseline "from day 0".
- **Official Documentation**: [FastAPI: Async Tests](https://fastapi.tiangolo.com/advanced/async-tests/).
- **Completion Criteria**: `pytest` executes a non-blocking integration test against the application skeleton.
- **Execution Tasks**:
  1. Add `pytest` and `httpx` to development dependencies.
  2. Configure `AsyncClient` fixture with `ASGITransport` in `tests/conftest.py`.
  3. Create a system test verifying the health check status code.
- **Verification**: Run `pytest` and confirm the first async test passes.
- **Definition of Done**: The testing framework is active and follows asynchronous programming patterns.

#### **Milestone: Continuous integration preparation**

- **Objective**: Design the automated checks required for the Task Completion Workflow.
- **Official Documentation**: [GitHub: About community profiles](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/about-community-profiles-for-public-repositories).
- **Completion Criteria**: Configuration files for automated linting and testing are present.
- **Execution Tasks**:
  1. Configure `ruff` for code quality and formatting.
  2. Establish the `git commit` checklist.
- **Verification**: Run `ruff check` on the existing application skeleton.
- **Definition of Done**: The project is prepared for automated validation in subsequent phases.

---

#####  **Phase 2 – Job Collection**
Prerequisite: Review **DATABASE_ARCHITECTURE.md** and **DATABASE_SCHEMA.md** before implementing SQLModel models.

######  **Milestone: Job source abstraction**
*   **Objective**: Implement a Strategy pattern for various job discovery methods.
*   **Official Documentation**: [Python: abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html).
*   **Completion Criteria**: A unified interface exists for all job collectors.
*   **Execution Tasks**:
    1. Define the `BaseCollector` ABC in `app/services/collection/base.py`.
    2. Implement common normalization methods.
*   **Verification**: Create a `MockCollector` and verify it returns standardized job data.
*   **Definition of Done**: Collectors are modular and adhere to the Single Responsibility Principle.

#### **Milestone: Public API integration**

- **Objective**: Implement collectors for external job listing APIs.
- **Official Documentation**: [FastAPI: Settings](https://fastapi.tiangolo.com/advanced/settings/).
- **Completion Criteria**: Raw job data is successfully retrieved from at least one public API.
- **Execution Tasks**:
  1. Manage API keys using `pydantic-settings` and `.env`.
  2. Implement an asynchronous HTTP client for fetching job data.
- **Verification**: Verify data retrieval logs without exposing sensitive secrets.
- **Definition of Done**: The system discovers opportunities from external API sources.

#### **Milestone: Company career page collection**

- **Objective**: Implement collection logic for direct company career listings.
- **Official Documentation**: [FastAPI: Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).
- **Completion Criteria**: Data is collected from company-specific career pages.
- **Execution Tasks**:
  1. Implement specialized scraping or collection logic for target domains.
  2. Map source-specific data to the `RawJob` model.
- **Verification**: Compare collected data against the source career page content.
- **Definition of Done**: Direct company listings are integrated into the collection pipeline.

#### **Milestone: Job normalization**

- **Objective**: Transform raw collection output into a consistent internal representation.
- **Official Documentation**: [Pydantic: Response Model](https://fastapi.tiangolo.com/tutorial/response-model/).
- **Completion Criteria**: All jobs share a common schema regardless of source.
- **Execution Tasks**:
  1. Implement a normalization service to clean and map fields.
  2. Enforce data types and constraints using Pydantic.
- **Verification**: Validate normalized data against the `Job` schema.
- **Definition of Done**: The system produces a clean, standardized collection of job postings.

#### **Milestone: Duplicate detection**

- **Objective**: Prevent redundant processing by identifying identical opportunities from different sources.
- **Official Documentation**: [Python: Standard Library (hashlib)](https://docs.python.org/3/library/hashlib.html).
- **Completion Criteria**: The system successfully identifies and filters duplicate postings.
- **Execution Tasks**:
  1. Implement a fingerprinting algorithm for jobs (e.g., hash of title, company, and location).
  2. Add filtering logic to the processing layer.
- **Verification**: Process a dataset containing known duplicates and verify they are filtered.
- **Definition of Done**: The processing pipeline maintains data integrity by removing duplicates.

######  **Milestone: Data persistence**
*   **Objective**: Implement the SQLModel/PostgreSQL layer for long-term storage.
*   **Official Documentation**: [SQLModel: Tutorial](https://sqlmodel.tiangolo.com/tutorial/); [Alembic: Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html).
*   **Completion Criteria**: Database tables match the physical schema and are version-managed.
*   **Execution Tasks**:
    1. Define `Job`, `Company`, and `JobSource` models in `app/models/` following **DATABASE_SCHEMA.md**.
    2. Initialize the migration environment in the `migrations/` directory.
    3. Generate the initial static, reversible migration.
*   **Verification**: Run `alembic upgrade head` and verify the physical schema in PostgreSQL.
*   **Definition of Done**: Data is persistable, versioned, and managed by Alembic.
```

---

##### **Phase 3 – Job Intelligence**

###### **Milestone: AI service abstraction**

- **Objective**: Implement a provider-independent Strategy pattern interface for all AI capabilities.
- **Official Documentation**: [Python: abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html); [Pydantic: Models](https://docs.pydantic.dev/latest/concepts/models/).
- **Completion Criteria**: A common Python interface defines the contract for all AI inference and generation tasks.
- **Execution Tasks**:
  1. Define the `AIProvider` abstract base class in `app/services/ai/base.py`.
  2. Implement core members: `generate_text`, `generate_structured_output` (using Pydantic models), and `is_configured`.
  3. Define internal AI service exception types to isolate vendor errors.
- **Verification**: Create a `MockAIProvider` that satisfies the interface and returns deterministic test data.
- **Definition of Done**: The application interacts with AI capabilities through a stable abstraction that contains no vendor-specific logic.

###### **Milestone: AI provider integration (Gemini & Groq)**

- **Objective**: Implement concrete AI providers for the primary and fallback services.
- **Official Documentation**: [Gemini API: Quickstart](https://ai.google.dev/gemini-api/docs/quickstart); [Groq: OpenAI Compatibility](https://console.groq.com/docs/openai).
- **Completion Criteria**: The system can execute inference runs using Google Gemini as the primary and Groq as the resilient fallback.
- **Execution Tasks**:
  1. Implement the `GeminiProvider` using the official Google Generative AI SDK.
  2. Implement the `GroqProvider` using OpenAI-compatible client standards.
  3. Manage API keys for both providers using `pydantic-settings` and `.env`.
- **Verification**: Verify successful `generate_text` responses from both providers in development logs.
- **Definition of Done**: Both primary and fallback providers are functional and swappable via the service layer.

###### **Milestone: Career profile filtering**

- **Objective**: Filter opportunities according to user-defined career categories.
- **Official Documentation**: [Pydantic: Field Validation](https://docs.pydantic.dev/latest/concepts/fields/).
- **Completion Criteria**: Collected jobs are categorized into software, biomedical, or biochemistry profiles.
- **Execution Tasks**:
  1. Define keyword and attribute matchers for career domains.
  2. Implement filtering logic in the intelligence service.
- **Verification**: Test category assignment against known job types.
- **Definition of Done**: Jobs are methodically filtered based on configured career profiles.

###### **Milestone: Recommendation engine**

- **Objective**: Orchestrate the ranking logic for the discovery pipeline.
- **Official Documentation**: [FastAPI: Dependencies](https://fastapi.tiangolo.com/tutorial/dependencies/).
- **Completion Criteria**: The system produces an ordered list of opportunities for the user.
- **Execution Tasks**:
  1. Implement the intelligence service layer.
  2. Integrate the AI service abstraction for relevance scoring and profile matching.
  3. Implement failover logic to switch providers if the primary hits rate limits.
- **Verification**: Verify the service returns structured recommendation data using the abstraction.
- **Definition of Done**: The engine determines which opportunities match user preferences using a provider-agnostic pipeline.

###### **Milestone: Relevance scoring**

- **Objective**: Leverage LLMs to evaluate job relevance numerically via the abstraction layer.
- **Official Documentation**: [Gemini API: Structured Outputs](https://ai.google.dev/gemini-api/docs/structured-output).
- **Completion Criteria**: Jobs receive a numerical relevance score based on the user's profile.
- **Execution Tasks**:
  1. Design prompt templates that use the `generate_structured_output` method.
  2. Define Pydantic models for the scoring response (score + reasoning).
  3. Implement system prompts optimized for Gemini's structured output standards.
- **Verification**: Execute a scoring run and verify the validated Pydantic output meets requirements.
- **Definition of Done**: Intelligence scoring is numerical, data-driven, and model-powered through the abstraction.

###### **Milestone: Explainable recommendations**

- **Objective**: Provide human-readable reasoning for system recommendations using model "Thinking" capabilities.
- **Official Documentation**: [Gemini API: Thinking](https://ai.google.dev/gemini-api/docs/thinking).
- **Completion Criteria**: Users can view the reasoning behind every recommendation.
- **Execution Tasks**:
  1. Capture AI explanations during the relevance scoring milestone.
  2. Utilize XML tags (e.g., `<thinking>`) in prompts to improve grounding and reasoning quality.
  3. Expose the `ai_explanation` field through the API schemas.
- **Verification**: Review AI-generated explanations for clarity, groundedness, and adherence to user preferences.
- **Definition of Done**: The system explains why an opportunity was recommended using the provider's reasoning capability.

###### **Milestone: Daily recommendation generation**

- **Objective**: Automate the batch generation of recommendations.
- **Official Documentation**: [FastAPI: Lifespan Events](https://fastapi.tiangolo.com/advanced/events/).
- **Completion Criteria**: A new set of recommendations is available to the user daily.
- **Execution Tasks**:
  1. Implement a pipeline runner that processes new jobs through the discovery flow.
  2. Persist the results in the `job_recommendation` table.
- **Verification**: Trigger a full run and verify that the `date_generated` field is current.
- **Definition of Done**: Recommendation generation is a repeatable, daily pipeline.

---

---

##### **Phase 4 – Application Assistance**

###### **Milestone: CV tailoring**

- **Objective**: Generate tailored CV recommendations for selected jobs through the AI abstraction.
- **Official Documentation**: [Gemini API: Long Context](https://ai.google.dev/gemini-api/docs/long-context).
- **Completion Criteria**: The system produces job-specific CV improvement suggestions.
- **Execution Tasks**:
  1. Implement a tailoring service that consumes the `AIProvider` interface.
  2. Design prompts that focus on "minimal, verifiable improvements" grounded in the job description.
  3. Use Gemini’s long-context window to analyze the full career history without truncation.
- **Verification**: Manually review a tailored CV against the job requirements for accuracy.
- **Definition of Done**: The system assists the user without vendor lock-in or automatic submission.

###### **Milestone: Cover letter generation**

- **Objective**: Draft high-quality cover letters based on job and user data.
- **Official Documentation**: [Claude Platform Docs: Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices).
- **Completion Criteria**: AI-generated cover letter drafts are available for user approval.
- **Execution Tasks**:
  1. Implement the generation service using the provider-agnostic `generate_text` method.
  2. Apply structured XML-based prompting to guide the model's role and tone.
  3. Persist drafts in the `cover_letter` table.
- **Verification**: Confirm the letter mentions specific job and company attributes correctly.
- **Definition of Done**: The system generates tailored cover letter recommendations.

###### **Milestone: Application recommendations**

- **Objective**: Provide strategic advice for the application process using model reasoning.
- **Official Documentation**: [Gemini API: Thinking](https://ai.google.dev/gemini-api/docs/thinking).
- **Completion Criteria**: User receives actionable tips for specific job applications.
- **Execution Tasks**:
  1. Implement prompts that utilize model reasoning to evaluate job-to-user fit for interview prep.
- **Verification**: Review tips for consistency with career profile interests and collected job data.
- **Definition of Done**: The system assists user-controlled preparation through the AI layer.

---

### **Phase 5 – User Experience**

#### **Milestone: Dashboard**

- **Objective**: Provide a central interface for career activity overview.
- **Official Documentation**: [FastAPI: Static Files](https://fastapi.tiangolo.com/tutorial/static-files/).
- **Completion Criteria**: User can view a summary of discovered jobs and recommendations.
- **Execution Tasks**:
  1. Define the dashboard API response model.
  2. Implement aggregate queries for recommendation counts and statuses.
- **Verification**: Verify the dashboard appears in the Swagger documentation.
- **Definition of Done**: The user has an intuitive interface for decision-making.

#### **Milestone: Job browsing**

- **Objective**: Enable interactive browsing of the clean job collection.
- **Official Documentation**: [SQLModel: LIMIT and OFFSET](https://sqlmodel.tiangolo.com/tutorial/limit-and-offset/).
- **Completion Criteria**: User can paginate through and view detailed job data.
- **Execution Tasks**:
  1. Implement paginated endpoints for the `Job` model.
  2. Use `response_model` to return detailed company and source metadata.
- **Verification**: Request a page of jobs and verify company relationships are loaded.
- **Definition of Done**: All collected postings are browsable by the user.

#### **Milestone: Search and filtering**

- **Objective**: Provide targeted discovery tools for the job collection.
- **Official Documentation**: [FastAPI: Query Parameters](https://fastapi.tiangolo.com/tutorial/query-params/).
- **Completion Criteria**: User can filter jobs by location, employment type, and profile.
- **Execution Tasks**:
  1. Implement query parameter filters for the job browsing endpoints.
  2. Add full-text search capability to job descriptions.
- **Verification**: Execute a filtered search and verify the results match criteria.
- **Definition of Done**: Search and filtering support specific career profile requirements.

#### **Milestone: Saved opportunities**

- **Objective**: Allow users to track leads of interest.
- **Official Documentation**: [SQLModel: Automatic IDs](https://sqlmodel.tiangolo.com/tutorial/automatic-id-none-refresh/).
- **Completion Criteria**: User can "save" opportunities to a dedicated shortlist.
- **Execution Tasks**:
  1. Implement the status update logic for the `Job` model.
  2. Create endpoints for listing saved jobs.
- **Verification**: Save a job and verify it appears in the saved list.
- **Definition of Done**: Opportunities are persistable for manual decision-making.

#### **Milestone: User preferences**

- **Objective**: Manage the user's career interests and locations.
- **Official Documentation**: [FastAPI: Body - Nested Models](https://fastapi.tiangolo.com/tutorial/body-nested-models/).
- **Completion Criteria**: User can update their career profile and interests.
- **Execution Tasks**:
  1. Implement the `User Profile` table and associated API endpoints.
  2. Validate preferences using Pydantic schemas.
- **Verification**: Update a preference and verify it influences recommendation scoring.
- **Definition of Done**: The system adapts as user skills and career goals evolve.

---

### **Phase 6 – Automation**

#### **Milestone: Scheduled job collection**

- **Objective**: Automate the discovery of new opportunities.
- **Official Documentation**: [FastAPI: Lifespan Events (Background)](https://fastapi.tiangolo.com/advanced/events/).
- **Completion Criteria**: Job collection runs periodically without manual triggering.
- **Execution Tasks**:
  1. Implement a scheduled task runner (e.g., using `apscheduler` or `lifespan`).
- **Verification**: Confirm collection logs show periodic execution.
- **Definition of Done**: Repetitive discovery workflows are automated.

#### **Milestone: Recommendation pipeline**

- **Objective**: Automate the end-to-end intelligence flow.
- **Official Documentation**: [FastAPI: Concurrency](https://fastapi.tiangolo.com/async/).
- **Completion Criteria**: Collected jobs are automatically categorized and scored.
- **Execution Tasks**:
  1. Chain collection, normalization, and scoring into a background workflow.
- **Verification**: verify that new recommendations appear after a scheduled collection run.
- **Definition of Done**: The modular processing pipeline is fully automated.

#### **Milestone: Notifications**

- **Objective**: Alert the user to high-relevance career matches.
- **Official Documentation**: [FastAPI: Background Tasks (Email)](https://fastapi.tiangolo.com/tutorial/background-tasks/#background-tasks).
- **Completion Criteria**: User receives notifications for matches above a threshold.
- **Execution Tasks**:
  1. Integrate an email or messaging service into background tasks.
  2. Configure threshold settings in the user profile.
- **Verification**: Trigger a mock high-score match and verify notification delivery.
- **Definition of Done**: Notifications support timely user decision-making.

#### **Milestone: Background processing**

- **Objective**: Offload slow intelligence tasks to prevent API blocking.
- **Official Documentation**: [FastAPI: Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/).
- **Completion Criteria**: The API remains responsive during large-scale intelligence runs.
- **Execution Tasks**:
  1. Implement the `BackgroundTasks` pattern for collection and scoring.
  2. Return `202 Accepted` for manual trigger requests.
- **Verification**: Start a collection run and verify immediate API response time.
- **Definition of Done**: Slow operations are decoupled from the request-response cycle.

#### **Milestone: Monitoring**

- **Objective**: Observe the health and performance of automated workflows.
- **Official Documentation**: [FastAPI: Middleware](https://fastapi.tiangolo.com/tutorial/middleware/).
- **Completion Criteria**: The system provides visibility into pipeline success/failure rates.
- **Execution Tasks**:
  1. Implement structured logging for background task states.
  2. Add request correlation IDs via middleware for easier tracing.
- **Verification**: Check logs for successful task completion messages.
- **Definition of Done**: Automated workflows are observable and diagnostic-friendly.

---

### **Phase 7 – Production**

#### **Milestone: Security hardening**

- **Objective**: Protect application data and framework interfaces.
- **Official Documentation**: [FastAPI: Security First Steps](https://fastapi.tiangolo.com/tutorial/security/first-steps/).
- **Completion Criteria**: API endpoints are secured and secrets are managed correctly.
- **Execution Tasks**:
  1. Implement password hashing and JWT authentication.
  2. Hide documentation in production environments.
- **Verification**: Attempt unauthorized access and confirm `401 Unauthorized` responses.
- **Definition of Done**: Production code follows high-security standards.

#### **Milestone: Performance optimization**

- **Objective**: Minimize resource usage and response latency.
- **Official Documentation**: [FastAPI: Performance](https://fastapi.tiangolo.com/#performance).
- **Completion Criteria**: The system meets latency targets for UI interactions.
- **Execution Tasks**:
  1. Optimize SQL queries using joins and indexes.
  2. Use `uvloop` for high-performance serving.
- **Verification**: benchmark endpoint response times under load.
- **Definition of Done**: The system is tuned for reliable production speed.

#### **Milestone: Production deployment**

- **Objective**: Containerize the system for consistent execution.
- **Official Documentation**: [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/).
- **Completion Criteria**: A minimal Docker image successfully serves the application.
- **Execution Tasks**:
  1. Create a multi-stage `Dockerfile` using `uv` for dependencies.
  2. Implement `compose.yml` for orchestration of API and database.
- **Verification**: Run `docker compose up` and access the production system.
- **Definition of Done**: Deployment uses the **exec form** of `CMD` for graceful shutdowns.

#### **Milestone: Logging**

- **Objective**: Establish production-grade audit and error logging.
- **Official Documentation**: [FastAPI: Handling Errors](https://fastapi.tiangolo.com/tutorial/handling-errors/).
- **Completion Criteria**: Logs provide sufficient context for diagnosing production issues.
- **Execution Tasks**:
  1. Configure centralized logging with appropriate severity levels.
  2. Never log sensitive data such as API keys or secrets.
- **Verification**: intentionally trigger an error and verify it is accurately logged.
- **Definition of Done**: The system maintains clear and useful production audit logs.

#### **Milestone: Backup strategy**

- **Objective**: Protect user and job data from loss.
- **Official Documentation**: [PostgreSQL: Documentation (Backup and Restore)](https://www.postgresql.org/docs/current/backup.html).
- **Completion Criteria**: Regular database backups are performed and verified.
- **Execution Tasks**:
  1. Automate database snapshots and secure storage.
- **Verification**: perform a test restoration from a backup.
- **Definition of Done**: The project has a sustainable data recovery workflow.

###### **Milestone: Operational documentation**

- **Objective**: Produce maintenance and deployment guides.
- **Official Documentation**: [AI Development Playbook](AI_DEVELOPMENT_PLAYBOOK.md).
- **Completion Criteria**: Documentation covers all operational procedures.
- **Execution Tasks**:
  1. Document environment setup and deployment steps.
  2. Create a "Known Gotchas" section for future maintainers.
- **Verification**: Verify documentation accuracy by following the steps from scratch.
- **Definition of Done**: The project maintains clear, up-to-date operational standards.

```

```
