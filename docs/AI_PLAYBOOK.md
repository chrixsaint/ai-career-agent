# AI Playbook

> **Purpose:** This document defines how AI tools are used throughout the software development lifecycle of the AI Career Agent. It establishes the responsibilities of each tool, when each tool should be used, and how they work together while following the repository standards.

The AI Playbook defines **tool orchestration**.

Repository governance is defined in `REPOSITORY_STANDARD.md`.

Human-AI collaboration practices are defined in `AI_COLLABORATION.md`.

---

# Guiding Principles

The repository follows these principles when using AI.

- Use the right tool for the right task.
- Prefer official documentation over AI-generated assumptions.
- Verify important engineering decisions before implementation.
- Avoid asking multiple AI tools to solve the same problem unless performing validation or review.
- The Git repository remains the project's source of truth.

---

# AI Development Workflow

The recommended engineering workflow is:

1. Research with NotebookLM.
2. Verify against official documentation.
3. Design with ChatGPT.
4. Plan implementation with Claude Code.
5. Implement with Claude Code or GitHub Copilot.
6. Review, test, and validate before committing.

Each tool contributes a different capability.

---

# NotebookLM

## Primary Responsibility

Research and knowledge retrieval.

## Use For

- Official documentation
- Requirements lookup
- Architecture validation
- Engineering standards
- Repository documentation research
- Learning project context

## Avoid

- Writing production code
- Editing repository files
- Defining repository conventions

---

# ChatGPT

## Primary Responsibility

Engineering reasoning and technical design.

## Use For

- Architecture discussions
- Engineering trade-offs
- Documentation design
- Repository governance
- Design reviews
- Complex debugging
- Project planning

## Avoid

- Acting as the primary source of official documentation
- Making implementation decisions without repository context
- Replacing project standards

---

# Claude Code

## Primary Responsibility

Repository-aware software engineering.

## Use For

- Repository exploration
- Multi-file implementation
- Refactoring
- Planning implementation
- Running tests
- Terminal operations
- Repository maintenance
- Codebase analysis

Claude Code has awareness of:

- Repository structure
- Git history
- Terminal environment
- `CLAUDE.md`
- `.claude/`

## Avoid

- Replacing official documentation
- Introducing repository conventions without documented standards

---

# GitHub Copilot

## Primary Responsibility

Implementation assistance inside the development environment.

## Use For

- Code completion
- Boilerplate generation
- Refactoring assistance
- Test generation
- Inline documentation
- IDE-assisted development

## Avoid

- High-level architectural decisions
- Repository governance
- Requirement interpretation without supporting documentation

---

# Responsibility Matrix

| Activity                | Primary Tool                 |
| ----------------------- | ---------------------------- |
| Official documentation  | NotebookLM                   |
| Repository research     | Claude Code                  |
| Architecture            | ChatGPT                      |
| Engineering design      | ChatGPT                      |
| Implementation planning | Claude Code                  |
| Code generation         | GitHub Copilot / Claude Code |
| Repository refactoring  | Claude Code                  |
| Debugging               | Claude Code / ChatGPT        |
| Documentation drafting  | ChatGPT                      |
| Repository review       | Claude Code                  |

---

# Source of Truth

The repository follows this order of authority:

1. Official documentation
2. Repository standards
3. Project documentation
4. Source code
5. AI assistants

AI tools assist development.

They do not replace official documentation or repository standards.

---

# Scope

This document defines how AI tools are orchestrated during software development.

It does **not** define:

- Human collaboration principles
- Repository organization
- Coding standards
- System architecture
- Project requirements

Those responsibilities belong to their respective documents.

---

# Continuous Improvement

The AI engineering workflow should evolve as AI tooling improves.

Changes to tool responsibilities should be based on official documentation and practical engineering experience rather than personal preference.
