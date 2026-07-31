# Knowledge Base Rules

> **Purpose:** This document defines the official standards for organizing, maintaining, and using the knowledge base for the AI Career Agent project. It serves as the operating manual for both human contributors and AI assistants (GitHub Copilot, ChatGPT, Claude, and future AI tools).

---

# 1. Purpose

The knowledge base exists to:

- Serve as the single source of truth for all learning resources used throughout this project.
- Organize documentation in a consistent, scalable manner.
- Make information easy to discover and reuse.
- Enable AI assistants to understand the repository structure and provide better guidance.
- Build a reusable engineering knowledge library that can be used in future software projects.

---

# 2. Core Principles

The following principles apply to every resource added to this repository.

## Single Source of Truth

Each resource has one canonical location.

Avoid duplicates whenever possible.

If the same resource is needed elsewhere, reference the original instead of copying it.

---

## Prefer Official Sources

Always prioritize:

1. Official documentation
2. Official engineering blogs
3. Official GitHub repositories
4. Official YouTube channels
5. Trusted books
6. Community tutorials

---

## Keep Topics Focused

Each folder should contain resources for one major topic only.

Do not mix unrelated technologies.

---

## Make Information Discoverable

Resources should have descriptive filenames.

Avoid vague names such as:

- notes.md
- tutorial.md
- final_notes.md

Prefer names like:

- FastAPI Authentication.md
- Playwright Browser Automation.md
- Claude Prompt Engineering.md

---

## Learn Once, Reuse Forever

The purpose of this knowledge base is not simply to store information.

Its purpose is to reduce future learning time.

Whenever useful:

- summarize
- simplify
- create cheat sheets
- document lessons learned

---

# 3. Folder Responsibilities

## 01-project

Project planning, roadmap, goals, requirements, setup guides, project documentation.

---

## 02-architecture

Clean Architecture

SOLID Principles

Design Patterns

Architecture Decision Records

System diagrams

---

## 03-python

Python language

Typing

Packaging

Virtual environments

Project-specific Python patterns

---

## 04-fastapi

FastAPI

Dependency Injection

Routing

Authentication

Background Tasks

Middleware

---

## 05-ai

General Artificial Intelligence concepts.

Machine Learning.

AI workflows.

---

## 06-llm

Large Language Models.

Model comparison.

Inference.

Embeddings.

Vector databases.

Prompt evaluation.

---

## 07-prompt-engineering

Anthropic prompting

OpenAI prompting

Microsoft prompting

Prompt libraries

Prompt design patterns

---

## 08-api

REST

HTTP

Requests

HTTPX

API design

Authentication

JSON

---

## 09-mcp

Model Context Protocol

MCP servers

MCP clients

Integration examples

---

## 10-playwright

Browser automation

Web scraping

Testing

Form automation

Authentication flows

---

## 11-vscode

VS Code configuration

Extensions

AI tools

Workspace settings

Productivity tips

---

## 12-github

Git

GitHub

GitHub Actions

Copilot

Version control

Repository management

---

## 13-testing

pytest

Unit testing

Integration testing

Mocking

Test strategies

---

## 14-devops

Docker

Deployment

CI/CD

Infrastructure

Environment management

---

## 15-career-agent

Everything specific to this project.

Business logic.

Features.

Roadmap.

Architecture.

AI workflows.

---

## 16-system-design

Scalable software architecture.

Distributed systems.

Caching.

Messaging.

High-level design.

---

## 17-databases

SQLite

PostgreSQL

SQLAlchemy

Alembic

Indexes

Database optimization

---

## 18-security

JWT

OAuth

API Security

Environment variables

Secrets management

Rate limiting

CORS

---

## 19-career

Interview preparation

Backend interview resources

Resume

Portfolio

Job search

Career development

---

## 20-cheatsheets

Short practical references.

No tutorials.

Only frequently used commands, syntax, workflows and reminders.

---

## inbox

Temporary storage only.

Every resource must eventually be moved into its proper folder.

The inbox should remain empty whenever possible.

---

# 4. Inbox Workflow

Every new resource follows this workflow.

Research

↓

Download

↓

Place inside **knowledge/inbox**

↓

Review

↓

Categorize

↓

Move to correct folder

↓

Upload to NotebookLM

↓

Create cheat sheet if necessary

↓

Delete from inbox

The inbox is **never permanent storage**.

---

# 5. NotebookLM Organization Rules

Each NotebookLM notebook should focus on one major topic.

Examples:

- FastAPI
- Python
- Playwright
- APIs
- Prompt Engineering
- MCP

Avoid mixing unrelated subjects.

Every NotebookLM notebook should primarily contain:

- Official documentation
- Official videos
- High-quality tutorials
- Personal notes
- Project-specific references

Whenever possible:

- Keep one notebook per technology.
- Add concise summaries.
- Record key takeaways.
- Record useful prompts.
- Record implementation patterns used in this project.

---

# 6. Naming Conventions

Use descriptive names.

Examples:

- FastAPI Authentication.md
- Playwright Login Automation.md
- Claude Prompt Engineering.md

Avoid names like:

- notes.md
- final.md
- new_notes.md
- tutorial2.md

Keep naming consistent.

---

# 7. README Standards

Every numbered folder should contain a README.md explaining:

- Purpose of the folder
- Topics covered
- Why the topic matters to this project
- Recommended official documentation
- Recommended videos
- Folder organization
- Important notes

The README should help both humans and AI assistants understand the folder immediately.

---

# 8. Cheat Sheet Standards

Cheat sheets should be:

- Short
- Practical
- Frequently referenced
- Easy to scan

They should contain:

- Commands
- Syntax
- Common patterns
- Common mistakes
- Best practices
- Quick examples

They should **not** become full tutorials.

---

# 9. Source Quality Hierarchy

Resources should be added using the following priority:

1. Official documentation
2. Official engineering blogs
3. Official GitHub repositories
4. Official YouTube channels
5. Books
6. Community tutorials
7. Reddit (experience sharing only)

When conflicting information exists, prefer the higher-ranked source.

---

# 10. AI Collaboration Rules

Every AI assistant working on this repository should follow these principles:

- Read existing documentation before creating new content.
- Prefer official documentation over assumptions.
- Explain concepts before generating code when requested.
- Suggest the correct folder for new resources.
- Suggest the correct NotebookLM notebook.
- Recommend creating cheat sheets when appropriate.
- Prefer maintainable solutions over clever shortcuts.
- Clearly state assumptions when information is missing.
- Reuse existing project patterns before introducing new ones.
- Optimize for long-term maintainability and learning.

---

# 11. Maintenance Process

Maintain the knowledge base continuously.

After every research session:

- Review the inbox.
- Categorize new resources.
- Remove duplicates.
- Update relevant README files.
- Add useful summaries.
- Create or improve cheat sheets when valuable.

Review the knowledge base periodically to:

- Remove outdated information.
- Replace obsolete resources.
- Update links.
- Improve organization.
- Keep NotebookLM notebooks focused and current.

---

**Last Updated:** 2026-07-31
