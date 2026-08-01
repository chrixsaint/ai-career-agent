# Git Workflow

## Purpose

This document defines the Git workflow for the AI Career Agent project.

The goal is to maintain a clean, understandable, and traceable project history.

---

# Branch Strategy

For now, development will primarily use:

- `main` – Stable, working code.
- Feature branches – Optional for larger features.

Examples:

- feature/job-collector
- feature/recommendation-engine
- feature/dashboard

For small personal changes, working directly on `main` is acceptable as long as each commit is complete and the project remains in a working state.

---

# Commit Principles

Each commit should:

- Represent one logical change.
- Be small enough to review easily.
- Leave the project in a working state.
- Avoid mixing unrelated changes.

Prefer multiple focused commits over one large commit.

---

# Commit Message Format

Use the following format:

<type>: <short summary>

Examples:

feat: add LinkedIn job collector

fix: prevent duplicate job insertion

docs: update coding standards

refactor: simplify job ranking logic

test: add unit tests for recommendation engine

chore: update project dependencies

---

# Commit Types

Use these commit types consistently:

- feat – New functionality
- fix – Bug fixes
- docs – Documentation changes
- refactor – Internal code improvements without changing behavior
- test – Tests
- chore – Maintenance tasks
- ci – Continuous integration changes
- build – Build system or dependency changes
- perf – Performance improvements
- style – Formatting changes that do not affect behavior

---

# Writing Good Commit Messages

A good commit message should describe:

- What changed.
- Be concise.
- Be written in the imperative mood.

Good examples:

feat: add company model

fix: handle empty API response

docs: document database entities

refactor: split scraper into reusable modules

Avoid vague messages such as:

- update
- changes
- fix stuff
- work in progress
- misc

---

# Commit Checklist

Before committing, verify that:

- `git status` was run after staging to confirm exactly what will be committed.
- The project builds successfully.
- Tests pass (where applicable).
- Documentation has been updated if required.
- Code follows the Coding Standards.
- No secrets or credentials are committed.
- The commit represents one logical change.

If `pyproject.toml` changes dependency configuration, update `uv.lock` in the same change set.

Avoid committing unfinished work unless there is a specific reason.

---

# Pull Requests

If collaborating in the future, pull requests should include:

- Summary of changes
- Reason for the change
- Testing performed
- Related issues (if applicable)

---

# Version Tags

Use semantic versioning for releases.

Format:

vMAJOR.MINOR.PATCH

Examples:

v0.1.0

v0.2.0

v1.0.0

---

# Project Philosophy

Git history should tell the story of the project.

A developer should be able to understand how the project evolved by reading the commit history alone.
