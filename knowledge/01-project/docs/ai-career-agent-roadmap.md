---
title: AI Career Agent — Learning & Build Roadmap
source: knowledge/inbox/ai-career-agent-roadmap.md
date: 2026-07-31
tags: [roadmap, learning, plan]
owner: @chrixsaint
confidence: medium
summary: Stepwise learning and build roadmap mapping topics (Python, FastAPI, Playwright, Claude, MCP) to an ordered implementation plan and NotebookLM organization.
---

# AI Career Agent — Learning & Build Roadmap

_Curated July 2026. Prioritizes official docs, maintainer content, and free resources. Ranked best → good within each list._

---

## Section 1 — Python for AI Backend Development

| Resource                                                                                                        | Type          | Why                                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Python Docs — `asyncio`](https://docs.python.org/3/library/asyncio.html)                                       | Official docs | Ground truth for async I/O, which every scraper/agent loop depends on. Start here, not a tutorial.                                                                              |
| [Python Typing docs](https://docs.python.org/3/library/typing.html) + [mypy docs](https://mypy.readthedocs.io/) | Official docs | FastAPI and Pydantic are typing-driven; you need this fluently, not just "type hints exist."                                                                                    |
| [Real Python — Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)             | Article       | The best single explainer of the event loop mental model, better than most video content.                                                                                       |
| [uv (Astral) docs](https://docs.astral.sh/uv/)                                                                  | Official docs | Modern replacement for venv/pip/poetry — fast, single tool for env + packaging. Worth adopting now rather than learning pip-tools you'll abandon.                               |
| [Hypermodern Python (Claudio Jolowicz)](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/)         | Blog series   | Industry-standard reference for project structure, packaging, linting, CI — written by a maintainer, still the best "how do professionals structure a Python project" resource. |
| [Python Packaging User Guide](https://packaging.python.org/en/latest/)                                          | Official docs | Canonical source for `pyproject.toml`, src-layout, building distributable packages.                                                                                             |
| _Fluent Python_, 2nd ed. — Luciano Ramalho (O'Reilly)                                                           | Book          | Industry-standard for intermediate→advanced Python; only include if you want depth on data model/concurrency beyond what you need short-term.                                   |

**Why not more YouTube here:** at your level, official docs + Real Python + Hypermodern Python outperform video tutorials for this topic — this is reference material you'll return to, not linear learning.

---

## Section 2 — FastAPI

| Resource                                                                                         | Type            | Why                                                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [FastAPI official docs](https://fastapi.tiangolo.com/)                                           | Official docs   | Written by Sebastián Ramírez (creator); genuinely one of the best docs sets in the Python ecosystem — tutorial _and_ reference in one. Start with "Tutorial - User Guide," then "Advanced User Guide." |
| [FastAPI — Dependency Injection](https://fastapi.tiangolo.com/tutorial/dependencies/)            | Official docs   | You'll use DI constantly for DB sessions, auth, and shared services — read this section fully before building your service layer.                                                                      |
| [FastAPI — Background Tasks](https://fastapi.tiangolo.com/tutorial/background-tasks/)            | Official docs   | Directly relevant: this is how you'll trigger CV generation / email drafting without blocking requests.                                                                                                |
| [FastAPI — Security & OAuth2/JWT](https://fastapi.tiangolo.com/tutorial/security/)               | Official docs   | Needed once you add any authenticated dashboard/API layer.                                                                                                                                             |
| [ArjanCodes — FastAPI Course/playlist](https://www.youtube.com/@ArjanCodes)                      | YouTube channel | Best software-architecture-minded FastAPI content on YouTube — focuses on clean structure, not toy CRUD apps, matching where you already are.                                                          |
| [Full Stack FastAPI Template (tiangolo)](https://github.com/fastapi/full-stack-fastapi-template) | GitHub repo     | Official production-grade reference architecture (routers, services, SQLModel, Docker, CI) — study this instead of a random tutorial repo.                                                             |
| [Netflix Dispatch](https://github.com/Netflix/dispatch)                                          | GitHub repo     | Real large-scale FastAPI codebase in production use; excellent for seeing service-layer/repository patterns at scale.                                                                                  |

---

## Section 3 — Playwright

| Resource                                                                                                                     | Type            | Why                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Playwright for Python — official docs](https://playwright.dev/python/docs/intro)                                            | Official docs   | Your primary reference. Read "Writing Tests," "Locators," "Auto-waiting," "Actions" (forms/uploads), "Downloads," "Debugging" sections directly.                           |
| [Playwright — Best Practices](https://playwright.dev/python/docs/best-practices)                                             | Official docs   | Explicitly covers anti-patterns (hard waits, brittle selectors) — read before you write your scraper, not after.                                                           |
| [Playwright — Auth / storageState](https://playwright.dev/python/docs/auth)                                                  | Official docs   | Exactly what you need for login automation across job boards without re-authenticating every run.                                                                          |
| [Playwright Inspector & Trace Viewer docs](https://playwright.dev/python/docs/trace-viewer-intro)                            | Official docs   | The debugging workflow you'll actually use once scraping breaks on a real site.                                                                                            |
| [Playwright official YouTube channel](https://www.youtube.com/@Playwrightdev)                                                | YouTube channel | Maintainer-produced; short, accurate, no fluff — better than third-party "Playwright crash course" videos.                                                                 |
| [ScrapFly — Web Scraping With Playwright and Python](https://scrapfly.io/blog/posts/web-scraping-with-playwright-and-python) | Blog article    | Scraping-specific (not just testing-specific) guide: stealth, waiting strategies, anti-bot handling — fills the gap official docs leave since Playwright is testing-first. |
| [Playwright GitHub — examples](https://github.com/microsoft/playwright-python)                                               | GitHub repo     | Source + `/tests` folder is a good pattern reference for real locator strategies.                                                                                          |

**Anti-patterns to explicitly avoid** (per official best-practices doc): fixed `time.sleep()` waits instead of auto-waiting locators, brittle CSS selectors instead of `get_by_role`/`get_by_text`, and not using `storage_state` for session reuse.

---

## Section 4 — Claude (API, Claude Code, Prompting, MCP support)

> Anthropic's docs moved to **platform.claude.com** (previously docs.anthropic.com) — use this as your canonical source going forward.

| Resource                                                                                                                    | Type                  | Why                                                                                                                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Claude Platform Docs — Home](https://platform.claude.com/docs/en/home)                                                     | Official docs         | Root of everything: Messages API, tool use, structured outputs, streaming, prompt caching, context windows, rate limits.                                                             |
| [Claude API — Get Started](https://platform.claude.com/docs/en/get-started)                                                 | Official docs         | Your literal first API call — do this before anything else.                                                                                                                          |
| [Claude API — Tool Use / Tool Reference](https://platform.claude.com/docs/en/build-with-claude/tool-use)                    | Official docs         | Core to your agent: this is how Claude will call your job-search, scraping, and DB tools.                                                                                            |
| [Claude API — Structured Outputs](https://platform.claude.com/docs/en/build-with-claude/structured-outputs)                 | Official docs         | Directly maps to your "rank jobs" / "extract job description fields" use case — enforce JSON schemas instead of parsing free text.                                                   |
| [Prompt Engineering — Overview](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview)              | Official docs         | Covers XML tags, examples, chain-of-thought — Anthropic's own guidance on structuring system prompts, which you'll need for CV/cover-letter generation quality.                      |
| [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)                                                      | GitHub repo           | Official worked examples: tool use, PDF handling, embeddings-adjacent patterns, agent patterns — copy-paste-adapt quality.                                                           |
| [Anthropic Quickstarts](https://github.com/anthropics/anthropics-quickstarts)                                               | GitHub repo           | Official starter apps (computer use, customer support agent, financial data analyst) — good architecture references for a full agent app.                                            |
| [Claude Code — official docs](https://docs.claude.com/en/docs/claude-code)                                                  | Official docs         | Since you'll build this project _with_ Claude Code, learn its config (CLAUDE.md, custom commands, MCP integration) directly — this compounds your dev speed for the whole two weeks. |
| [Anthropic Academy — Claude API Development Guide](https://www.anthropic.com/learn/build-with-claude)                       | Official learning hub | Anthropic's own structured course-like path through the docs/cookbook — good as a checklist.                                                                                         |
| [Anthropic Engineering Blog — "Building Effective Agents"](https://www.anthropic.com/engineering/building-effective-agents) | Official blog         | Anthropic's own opinionated agent-architecture guidance (workflows vs. agents, when _not_ to add complexity) — the single best conceptual doc for Section 7 too.                     |

---

## Section 5 — OpenAI API

| Resource                                                                                        | Type          | Why                                                                                                                        |
| ----------------------------------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [OpenAI Platform Docs](https://platform.openai.com/docs/overview)                               | Official docs | Canonical reference — start with "Quickstart," then "Function calling," "Structured Outputs," "Responses API."             |
| [OpenAI — Structured Outputs guide](https://platform.openai.com/docs/guides/structured-outputs) | Official docs | Same use case as Claude's structured outputs — useful if you want a second-model fallback/comparison for extraction tasks. |
| [OpenAI — Function calling guide](https://platform.openai.com/docs/guides/function-calling)     | Official docs | Compare directly against Claude's tool-use model — useful if you keep the option to swap providers.                        |
| [OpenAI Cookbook](https://github.com/openai/openai-cookbook)                                    | GitHub repo   | Official examples including embeddings + vector search patterns for RAG-style resume/job matching.                         |
| [OpenAI — Embeddings guide](https://platform.openai.com/docs/guides/embeddings)                 | Official docs | Relevant if you want semantic similarity between your CV and job descriptions rather than keyword ranking.                 |

---

## Section 6 — Model Context Protocol (MCP)

| Resource                                                                                                           | Type          | Why                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------ | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [modelcontextprotocol.io — Documentation](https://modelcontextprotocol.io/docs/getting-started/intro)              | Official docs | Start here for concepts: servers, clients, tools, resources, prompts.                                                                                                                                                                                                                                                        |
| [MCP Specification (latest)](https://modelcontextprotocol.io/specification/2025-11-25)                             | Official spec | Authoritative protocol reference — JSON-RPC base, lifecycle, capability negotiation. Note: a **2026-07-28 spec** was just released moving MCP toward a stateless architecture — check the [MCP blog announcement](https://blog.modelcontextprotocol.io/posts/2026-07-28/) since this affects how you'd build a server today. |
| [modelcontextprotocol/modelcontextprotocol (GitHub)](https://github.com/modelcontextprotocol/modelcontextprotocol) | GitHub repo   | The actual spec + docs source, created by Anthropic's David Soria Parra & Justin Spahr-Summers.                                                                                                                                                                                                                              |
| [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)                                               | GitHub repo   | What you'll actually use to build your own MCP server(s) for job-scraping tools if you go that route.                                                                                                                                                                                                                        |
| [MCP — Example servers](https://github.com/modelcontextprotocol/servers)                                           | GitHub repo   | Official reference implementations (filesystem, fetch, sqlite, etc.) — the fastest way to see idiomatic server structure.                                                                                                                                                                                                    |
| [Anthropic — "Introducing the Model Context Protocol"](https://www.anthropic.com/news/model-context-protocol)      | Official blog | Original announcement with the architecture rationale — useful context for _why_ it's structured the way it is.                                                                                                                                                                                                              |

---

## Section 7 — AI Agents (Architecture, Planning, Memory, Orchestration)

| Resource                                                                                                   | Type             | Why                                                                                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Anthropic — "Building Effective Agents"](https://www.anthropic.com/engineering/building-effective-agents) | Official article | The best short conceptual read on this list — distinguishes simple "workflows" (your CV generator, likely) from true "agents" (your job-search/ranking loop), and warns against over-engineering. |
| [LangGraph — official docs](https://langchain-ai.github.io/langgraph/)                                     | Official docs    | If you want explicit graph-based control (nodes, conditional edges, checkpoints) over your pipeline — good fit for a multi-stage flow like scrape → extract → rank → generate → track.            |
| [OpenAI Agents SDK — docs](https://openai.github.io/openai-agents-python/)                                 | Official docs    | Lighter-weight alternative to LangGraph with an explicit "handoff" model between agents — worth comparing before committing.                                                                      |
| [LangGraph — GitHub repo](https://github.com/langchain-ai/langgraph)                                       | GitHub repo      | Source + examples; check recency of examples since the framework moves fast.                                                                                                                      |
| [Real Python — LangGraph Tutorial](https://realpython.com/langgraph-python/)                               | Article          | Practical, well-explained state/graph walkthrough beyond the official quickstart.                                                                                                                 |

---

## Section 8 — Databases (SQLite, PostgreSQL)

| Resource                                                               | Type          | Why                                                                                                                                                |
| ---------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SQLite — official docs](https://www.sqlite.org/docs.html)             | Official docs | Perfect for local dev / MVP application-tracking DB; zero setup.                                                                                   |
| [PostgreSQL — official docs](https://www.postgresql.org/docs/current/) | Official docs | Your production target once you deploy — read "Tutorial" + "SQL Language" sections.                                                                |
| [SQLModel — official docs](https://sqlmodel.tiangolo.com/)             | Official docs | Same author as FastAPI; unifies Pydantic + SQLAlchemy models — the natural ORM choice given your stack, and directly integrates with FastAPI's DI. |
| [SQLAlchemy 2.0 — official docs](https://docs.sqlalchemy.org/en/20/)   | Official docs | Read if you need capabilities SQLModel abstracts away (complex migrations, raw queries).                                                           |
| [Alembic — official docs](https://alembic.sqlalchemy.org/en/latest/)   | Official docs | Migrations — needed the moment your schema changes after you have real data (it will).                                                             |

---

## Section 9 — Job Scraping (APIs, Legal, Ethics, Datasets)

| Resource                                                                                                                     | Type              | Why                                                                                                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Remotive API](https://remotive.com/api-documentation)                                                                       | Official API docs | Free, no-auth-required remote job API — best first data source to integrate.                                                                                                                                                                    |
| [Adzuna API](https://developer.adzuna.com/)                                                                                  | Official API docs | Multi-country aggregator with salary data; free tier with `app_id`/`app_key` — good for salary-trend analytics (your Section 8/analytics requirement).                                                                                          |
| [USAJOBS API](https://developer.usajobs.gov/)                                                                                | Official API docs | US government jobs, free, requires registration; useful if targeting public-sector or as a clean well-structured API to learn the pattern on.                                                                                                   |
| [We Work Remotely RSS feed](https://weworkremotely.com/remote-jobs.rss)                                                      | RSS feed          | No auth needed, trivial to parse — good "first working data source" for day one.                                                                                                                                                                |
| [ever-jobs (GitHub)](https://github.com/ever-jobs/ever-jobs)                                                                 | GitHub repo       | Actively maintained aggregator hitting 10+ real sources (Recruitee/Teamtailor ATS APIs, RemoteOK, Himalayas, etc.) — study its source-adapter pattern; this is close to the exact shape of your Section 1 requirements (multi-board search).    |
| [web scraping legality — EFF / hiQ v. LinkedIn overview](https://www.eff.org/deeplinks) _(search "hiQ LinkedIn scraping")_   | Legal background  | Know the landscape: scraping _publicly accessible_ data has legal precedent (hiQ v. LinkedIn), but ToS violations and rate-limit abuse carry real risk — prefer official APIs (above) over scraping LinkedIn/Indeed directly wherever possible. |
| [Playwright + scraping ethics](https://scrapfly.io/blog/posts/web-scraping-with-playwright-and-python) _(same as Section 3)_ | Blog              | Covers `robots.txt` respect, rate limiting, and identifying yourself — reuse from Section 3.                                                                                                                                                    |

---

## Section 10 — GitHub (Professional Presentation)

| Resource                                                                                                                                                         | Type          | Why                                                                                                                                   |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------- |
| [GitHub Docs — About READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes) | Official docs | Baseline reference for what a strong README structurally needs.                                                                       |
| [Conventional Commits](https://www.conventionalcommits.org/)                                                                                                     | Spec/standard | Widely adopted commit-message convention — makes your portfolio repo read like a professionally maintained project.                   |
| [GitHub Docs — About GitHub Actions](https://docs.github.com/en/actions/about-github-actions)                                                                    | Official docs | For CI (lint/test on push) — a portfolio differentiator that shows production habits.                                                 |
| [Awesome README (GitHub)](https://github.com/matiassingers/awesome-readme)                                                                                       | GitHub repo   | Curated list of excellent real-world READMEs to model yours on — see how strong open-source projects present scope, setup, and demos. |

---

## Section 11 — System Design (Backend Architecture for This Project)

| Resource                                                                                                            | Type                     | Why                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [The Twelve-Factor App](https://12factor.net/)                                                                      | Official methodology doc | Config, dependencies, processes — the baseline checklist for any deployable backend, directly relevant to your Section 13 deployment.                                                                                                               |
| [ArjanCodes — Software Design & Architecture playlist](https://www.youtube.com/@ArjanCodes)                         | YouTube channel          | Best Python-specific treatment of SOLID, repository pattern, service layer, and dependency injection — practical, not academic.                                                                                                                     |
| [FastAPI Full Stack Template (again)](https://github.com/fastapi/full-stack-fastapi-template)                       | GitHub repo              | Concrete reference for how routers/services/repositories are actually laid out in a real FastAPI app.                                                                                                                                               |
| [Cosmic Python (_Architecture Patterns with Python_) — free online](https://www.cosmicpython.com/book/preface.html) | Free book                | Genuinely excellent, free, and precisely matches your needs: repository pattern, service layer, dependency inversion, all demonstrated in Python with a real domain example. This is the single best resource in this whole roadmap for Section 11. |

---

## Section 12 — Testing

| Resource                                                                                                                                              | Type          | Why                                                                                        |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------ |
| [pytest — official docs](https://docs.pytest.org/en/stable/)                                                                                          | Official docs | Fixtures, parametrize, markers — your testing foundation.                                  |
| [FastAPI — Testing guide](https://fastapi.tiangolo.com/tutorial/testing/)                                                                             | Official docs | `TestClient` patterns, dependency overrides for DB mocking — directly applicable.          |
| [Playwright — official Testing docs (pytest plugin)](https://playwright.dev/python/docs/test-runners)                                                 | Official docs | `pytest-playwright` integration — how to structure browser tests alongside your API tests. |
| [Real Python — Testing FastAPI applications](https://realpython.com/testing-third-party-apis-with-mocks/) _(or search "Real Python FastAPI testing")_ | Article       | Practical patterns for mocking external job-board APIs in tests.                           |

---

## Section 13 — Deployment

| Resource                                                                | Type          | Why                                                                                                                                                          |
| ----------------------------------------------------------------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Docker — official "Get Started"](https://docs.docker.com/get-started/) | Official docs | Containerize once, deploy anywhere below — non-negotiable for a portfolio-grade project.                                                                     |
| [FastAPI — Deployment docs](https://fastapi.tiangolo.com/deployment/)   | Official docs | Written for exactly your stack: Docker, workers (uvicorn/gunicorn), HTTPS, environment config.                                                               |
| [Fly.io docs](https://fly.io/docs/)                                     | Official docs | Good free tier, native Docker deploys, supports background workers — strong fit for Playwright-based scraping jobs that need more than a serverless timeout. |
| [Railway docs](https://docs.railway.com/)                               | Official docs | Fastest path from GitHub repo to live URL with a Postgres add-on — good for quick demoing.                                                                   |
| [Render docs](https://render.com/docs)                                  | Official docs | Similar to Railway; check current free-tier limits before committing (they change).                                                                          |
| [12-Factor App §III Config](https://12factor.net/config)                | Doc section   | Environment variable discipline — read alongside whichever platform you pick.                                                                                |

---

## Section 14 — NotebookLM Organization

Structure notebooks by **retrieval need during active building**, not by topic purity — you want to open one notebook per work session, not hunt across five.

| Notebook                           | Sources to Add                                                                                                                                                                                      |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1. Career Agent — Core Stack**   | FastAPI official docs, SQLModel docs, Playwright official docs, Claude API docs (platform.claude.com) — your daily-driver notebook, open constantly.                                                |
| **2. Claude + MCP**                | Claude tool-use/structured-outputs docs, Anthropic Cookbook README, MCP spec + Python SDK docs, "Building Effective Agents" article — for whenever you're building the AI-reasoning parts.          |
| **3. Scraping & Job Data Sources** | Playwright scraping-specific article, Remotive/Adzuna/USAJOBS API docs, ever-jobs repo README — for Section 3+9 work.                                                                               |
| **4. Architecture & Patterns**     | Cosmic Python chapters, Twelve-Factor App, FastAPI Full Stack Template README, ArjanCodes video transcripts (NotebookLM can ingest YouTube URLs directly) — reference when structuring new modules. |
| **5. Testing & Deployment**        | pytest docs, FastAPI testing/deployment docs, Fly.io or Railway docs, Docker get-started — pull up right before you write tests or ship.                                                            |
| **6. Project Log (your own)**      | Your own README drafts, architecture decisions, and daily notes — NotebookLM is excellent as a "what did I decide and why" journal across a 2-week sprint.                                          |

---

## Section 15 — Recommended Build Order (Learn Just-in-Time)

The philosophy: **never study a topic more than 1 day before you implement it.** Below, each step names the _minimum_ thing to read first.

| Step                               | Build                                                                                                                                                               | Learn immediately before                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **1**                              | Project skeleton: `uv init`, FastAPI hello-world, src-layout, git repo, README stub                                                                                 | Section 1 (uv/packaging) + Section 2 FastAPI Get Started only                                               |
| **2**                              | SQLite schema for `applications` table (SQLModel models)                                                                                                            | Section 8 SQLModel docs only — skip Postgres for now                                                        |
| **3**                              | First data source: Remotive API + WeWorkRemotely RSS → store raw jobs in DB                                                                                         | Section 9 (Remotive/RSS) — this is your first end-to-end slice, get it working fast                         |
| **4**                              | Add Adzuna + USAJOBS (multi-board search, salary data)                                                                                                              | Section 9 remaining APIs                                                                                    |
| **5**                              | Job description enrichment: Playwright to fetch full descriptions from listing URLs when API doesn't include them                                                   | Section 3 (Playwright basics — locators, waiting, no login yet)                                             |
| **6**                              | Claude integration #1: rank jobs against your profile using structured outputs                                                                                      | Section 4 (Get Started, Structured Outputs, one Cookbook example)                                           |
| **7**                              | Claude integration #2: generate tailored CV + cover letter (structured prompt, XML-tagged sections)                                                                 | Section 4 Prompt Engineering guide                                                                          |
| **8**                              | Draft outreach email generation                                                                                                                                     | Reuse Section 4 prompting knowledge — no new learning needed                                                |
| **9**                              | Application tracker: statuses, timestamps, follow-up reminder logic (plain cron/APScheduler, no framework needed yet)                                               | Nothing new — pure Python/DB work                                                                           |
| **10**                             | Remote/visa-sponsorship detection: keyword + Claude-assisted classification on description text                                                                     | Reuse Section 4 structured outputs                                                                          |
| **11**                             | Login-gated scraping (if targeting sites requiring auth)                                                                                                            | Section 3 Playwright Auth/storageState docs                                                                 |
| **12**                             | Analytics: interview rate, rejection rate, top skills, salary trends, top countries — SQL aggregation + a simple dashboard (FastAPI + Jinja2 or a small React page) | Section 8 SQL basics you haven't used yet                                                                   |
| **13**                             | Tests: pytest for services, `TestClient` for API, `pytest-playwright` for scraping                                                                                  | Section 12 — write tests for what already exists, don't TDD the whole build under time pressure             |
| **14**                             | Dockerize + deploy                                                                                                                                                  | Section 13 — Docker get-started + your chosen platform's docs                                               |
| **15**                             | Polish: professional README, GitHub Actions CI, architecture diagram                                                                                                | Section 10 + 11                                                                                             |
| **16 (optional, if time remains)** | MCP server wrapping your tools, so Claude Code (or any MCP client) can drive the agent directly                                                                     | Section 6 — only after core app works, this is a portfolio differentiator, not a dependency                 |
| **17 (optional)**                  | Migrate SQLite → Postgres for production, formalize with LangGraph/Agents SDK if the pipeline logic has grown complex enough to need it                             | Section 7 + remaining Section 8 Postgres docs — only if plain function orchestration is genuinely straining |

**Key principle applied throughout:** steps 1–10 get you a _working end-to-end agent_ using the simplest possible orchestration (plain Python + Claude tool calls), because Anthropic's own guidance is to add framework complexity (LangGraph, MCP servers, Postgres) only when a real need appears — which for a 2-week solo build is usually near the end, not the start.
