# NotebookLM Rules

> **Purpose:** This document defines the official standards for using NotebookLM throughout the AI Career Agent project. NotebookLM is an AI-powered learning and knowledge retrieval system that complements the Git repository. It is designed to accelerate learning, improve software development, and help both developers and AI assistants quickly retrieve high-value engineering knowledge.

---

# 1. Purpose

NotebookLM exists to:

- Retrieve technical information quickly.
- Answer project-related questions.
- Summarize documentation.
- Connect concepts across different technologies.
- Accelerate software development.
- Improve long-term learning and retention.
- Help AI assistants provide better project-specific guidance.

**Important Principle**

The Git repository is the permanent source of truth.

NotebookLM is the intelligent learning assistant built on top of that knowledge.

---

# 2. Core Philosophy

NotebookLM should contain **high-value knowledge only**.

Every uploaded resource should make the notebook smarter.

Before uploading any resource, always ask:

> **"Which notebook becomes smarter if I upload this resource?"**

Follow these principles:

- Prefer official documentation.
- Prefer quality over quantity.
- Keep notebooks focused.
- Avoid duplicate resources.
- Remove outdated material.
- Upload resources that will remain useful long term.

NotebookLM is **not** a storage system.

It is a curated engineering knowledge base.

---

# 3. Notebook Structure

Maintain approximately **10–12 focused notebooks**.

Each notebook should cover one major engineering topic.

## 01 Python Fundamentals

- Python language
- Typing
- Packaging
- Virtual environments
- Best practices

---

## 02 FastAPI Backend

- FastAPI
- Dependency Injection
- Authentication
- SQLAlchemy
- Middleware
- Background Tasks

---

## 03 APIs & HTTP

- REST
- HTTP
- HTTPX
- JSON
- API Design
- Authentication

---

## 04 AI Engineering

- AI concepts
- Embeddings
- Vector Databases
- AI Providers
- Inference
- RAG

---

## 05 Prompt Engineering

- Anthropic
- OpenAI
- Microsoft guidance
- Prompt libraries
- Prompt design patterns

---

## 06 MCP

- Model Context Protocol
- MCP Clients
- MCP Servers
- Integration patterns

---

## 07 Playwright Automation

- Browser automation
- Authentication
- Scraping
- Testing
- Automation workflows

---

## 08 System Design

- Clean Architecture
- SOLID
- Design Patterns
- Scalability
- Distributed Systems

---

## 09 Developer Productivity

- VS Code
- Git
- GitHub
- GitHub Copilot
- Linux
- Terminal
- Developer tooling

---

## 10 AI Career Agent

Everything specific to this project.

Including:

- Architecture
- Roadmap
- Features
- Business logic
- Lessons learned
- Implementation decisions
- Reusable project knowledge

---

# 4. What Should Be Uploaded

Prioritize resources such as:

- Official documentation
- Official API references
- Official engineering blogs
- Official GitHub repositories
- High-quality books
- Conference talks
- High-quality YouTube tutorials
- Architecture diagrams
- Personal implementation notes
- Cheat sheets
- Project documentation

Every uploaded resource should provide long-term value.

---

# 5. What Should NOT Be Uploaded

Avoid uploading:

- Duplicate resources
- Outdated tutorials
- Marketing pages
- Clickbait articles
- Low-quality blogs
- Unrelated documentation
- Temporary research
- Incomplete notes

NotebookLM should remain carefully curated rather than becoming a dumping ground.

---

# 6. Learning Philosophy

NotebookLM should help you **understand concepts**, not memorize them.

After learning a concept:

- Build a small working example.
- Apply it to the AI Career Agent project.
- Record important lessons.
- Update an existing cheat sheet or create a new one if appropriate.

The goal is to develop engineering intuition—not dependence on AI.

---

# 7. Active Learning Workflow

Every learning resource should follow this workflow:

Research

↓

Read documentation

↓

Watch the recommended video

↓

Save resource to **knowledge/inbox**

↓

Move it to the correct knowledge folder

↓

Upload it to the correct NotebookLM notebook

↓

Ask NotebookLM to explain the key ideas

↓

Build a small implementation

↓

Apply it to the AI Career Agent

↓

Document what was learned

↓

Create or improve a cheat sheet

Learning is complete only after the knowledge has been applied.

---

# 8. Notebook Size Guidelines

Keep notebooks focused.

Recommended guidelines:

- Approximately 20–50 high-quality resources per notebook.
- Split notebooks if they begin covering unrelated subjects.
- Prefer fewer high-quality resources over many repetitive ones.
- Remove outdated resources as technologies evolve.

Quality is always more valuable than quantity.

---

# 9. AI Collaboration Rules

Whenever an AI assistant recommends a new resource, it should also:

- Explain why the resource is valuable.
- Recommend the correct repository folder.
- Recommend the correct NotebookLM notebook.
- Identify duplicate resources if they exist.
- Suggest creating or updating a cheat sheet.
- Explain how the resource supports the AI Career Agent project.
- Connect the resource with related technologies already in the knowledge base.

The objective is to continuously improve both the repository and NotebookLM.

---

# 10. NotebookLM Prompt Library

Frequently use prompts such as:

- Summarize the five most important concepts.
- Explain this as a senior backend engineer.
- How does this relate to FastAPI?
- How should I apply this to my AI Career Agent?
- Compare this approach with similar technologies.
- What are the common mistakes developers make?
- What implementation patterns should I follow?
- Generate a practical implementation checklist.
- Which concepts should I study next?
- Create a concise cheat sheet from this documentation.

These prompts encourage deeper understanding rather than passive reading.

---

# 11. Practical Resource Mapping

| Resource                     | Repository Folder       | NotebookLM Notebook       | Cheat Sheet      |
| ---------------------------- | ----------------------- | ------------------------- | ---------------- |
| Python Documentation         | `03-python`             | 01 Python Fundamentals    | ✅ Yes           |
| FastAPI Documentation        | `04-fastapi`            | 02 FastAPI Backend        | ✅ Yes           |
| HTTPX Documentation          | `08-api`                | 03 APIs & HTTP            | ✅ Yes           |
| Anthropic Documentation      | `06-llm`                | 04 AI Engineering         | ✅ Yes           |
| Prompt Engineering Guides    | `07-prompt-engineering` | 05 Prompt Engineering     | ✅ Yes           |
| MCP Documentation            | `09-mcp`                | 06 MCP                    | ✅ Yes           |
| Playwright Documentation     | `10-playwright`         | 07 Playwright Automation  | ✅ Yes           |
| System Design Resources      | `16-system-design`      | 08 System Design          | Optional         |
| GitHub Copilot Documentation | `12-github`             | 09 Developer Productivity | ✅ Yes           |
| AI Career Agent Notes        | `15-career-agent`       | 10 AI Career Agent        | Project-specific |

---

# 12. Maintenance Process

Maintain NotebookLM continuously.

After every research session:

- Review newly collected resources.
- Remove duplicates.
- Replace outdated documentation.
- Keep notebooks focused.
- Update summaries when necessary.
- Improve cheat sheets.
- Ensure every uploaded resource continues to provide long-term value.

NotebookLM should evolve alongside the project.

---

# Final Goal

NotebookLM should become your personal engineering mentor.

It should be capable of helping you:

- Understand new technologies.
- Retrieve information quickly.
- Connect ideas across different topics.
- Support AI-assisted software development.
- Accelerate implementation of the AI Career Agent.
- Build reusable engineering knowledge for future projects.

The ultimate objective is not simply to collect documentation, but to create an intelligent engineering knowledge system that improves with every project you build.

---

**Last Updated:** 2026-07-31
