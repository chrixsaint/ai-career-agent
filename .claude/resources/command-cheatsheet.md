# Command Reference

## Purpose

This document provides a curated reference of commands used during the development and maintenance of the AI Career Agent.

It is intended for:

- Daily development
- AI-assisted engineering
- NotebookLM semantic search
- Quick command lookup

Only commands that are part of the project's regular workflow should be included.

---

## Scope

This document contains commands related to:

- Project setup
- Dependency management
- Development
- Testing
- Git workflow
- AI engineering
- Docker
- Project-specific workflows

One-time installation commands should remain in the official documentation and should not be duplicated here.

---

## Maintenance

Before adding a command, verify that it:

- Is used repeatedly during development.
- Comes from official documentation or established project workflows.
- Adds long-term value.
- Does not duplicate information maintained elsewhere.

Prefer linking to official documentation instead of copying it.

Remove commands that are no longer part of the project's workflow.

---

# Project Setup

## Synchronize Development Environment

### Command

```bash
uv sync
```

### Purpose

Synchronize the local development environment with the project's locked dependencies.

### When to Use

- After cloning the repository
- After pulling changes
- Whenever `uv.lock` changes

### Keywords

uv

environment

dependencies

sync

### Project Notes

Ensures the local environment matches the project's dependency lockfile.

### Official Source

uv Documentation

---

# Dependency Management

## Add a Dependency

### Command

```bash
uv add <package>
```

Example

```bash
uv add "fastapi[standard]"
```

### Purpose

Add a dependency and update the project configuration.

### When to Use

Whenever a new package is required.

### Keywords

uv

dependency

package

### Project Notes

The lockfile is updated automatically.

### Official Source

uv Documentation

---

## Update Dependency Lockfile

### Command

```bash
uv lock
```

### Purpose

Regenerate the dependency lockfile.

### When to Use

After modifying project dependencies.

### Keywords

uv

lockfile

dependencies

### Project Notes

Run before committing dependency changes.

### Official Source

uv Documentation

---

# Development

## Start FastAPI Development Server

### Command

```bash
uv run fastapi dev app/main.py
```

### Purpose

Start the FastAPI development server with automatic reload.

### When to Use

During application development.

### Keywords

FastAPI

development

server

uv

### Project Notes

The official documentation uses:

```bash
fastapi dev
```

This project uses:

```bash
uv run fastapi dev app/main.py
```

to ensure the application runs inside the project's managed environment.

### Official Source

FastAPI Documentation

---

# Testing

## Run All Tests

### Command

```bash
pytest
```

### Purpose

Execute the project's complete test suite.

### When to Use

Before committing changes.

### Keywords

pytest

testing

verification

### Project Notes

Run after implementing or modifying functionality.

### Official Source

pytest Documentation

---

# Git Workflow

## Check Repository Status

### Command

```bash
git status
```

### Purpose

Display the current state of the repository.

### When to Use

Before staging, committing, or pushing changes.

### Keywords

git

status

workflow

### Official Source

Git Documentation

---

## Stage Changes

### Command

```bash
git add .
```

uv run ruff check . --fix

uv run ruff format .

## To format file after writing

uv run ruff format tests/conftest.py

## to check if the files have been formated

uv run ruff check tests/conftest.py

## Verify the entire repository

uv run ruff check .

## Verify formatting

uv run ruff format --check .

## Verify functionality

pytest

### Purpose

Stage modified files for commit.

### Official Source

Git Documentation

---

## Create Commit

### Command

```bash
git commit -m "feat: short description"
```

### Purpose

Create a logical checkpoint in project history.

### Official Source

Git Documentation

---

# AI Engineering

## Start Claude Code

### Command

```bash
claude
```

### Purpose

Launch the Claude Code interactive development environment.

### Official Source

Claude Code Documentation

---

## Clear Context

### Command

```text
/clear
```

### Purpose

Start a fresh conversation by clearing the current context.

### Official Source

Claude Code Documentation

---

## Compact Context

### Command

```text
/compact
```

### Purpose

Reduce conversation size during long sessions.

### Official Source

Claude Code Documentation

---

## Review Current Changes

### Command

```text
/code-review
```

### Purpose

Request an AI review of the current implementation.

### Official Source

Claude Code Documentation

---

## Verify Implementation

### Command

```text
/verify
```

### Purpose

Ask Claude Code to verify the implementation before manual review.

### Official Source

Claude Code Documentation

---

# Docker

Docker commands will be added when Docker becomes part of the project's active workflow.

---

# Project-Specific Commands

Commands unique to the AI Career Agent will be added here as the project evolves.
