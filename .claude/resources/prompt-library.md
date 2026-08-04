# Prompt Library

## Purpose

This document contains reusable prompts that support AI-assisted development of the AI Career Agent.

The prompts in this library are intended for repeated engineering tasks and have been refined through practical use.

Unlike `.claude/skills/`, this document is designed for human reference and can be used with NotebookLM, ChatGPT, Claude Code, and GitHub Copilot.

---

### prompt to check everything about the last task before progressing

Based on the finalized repository documentation and implementation guides, review the current project state and determine the exact next implementation task.

Do not redesign previous work.

Determine:

1. Which file should be implemented next.
2. Why this file must come next.
3. Which documents define its implementation.
4. Any prerequisite checks before implementation.
5. The expected definition of done.
6. Whether any existing implementation should be adjusted before continuing.

If the next task is another architectural contract, explain why it precedes concrete provider implementations.

Use only the repository documentation and current implementation state.

## Scope

This library contains prompts for:

- Research
- Planning
- Architecture
- Code Review
- Debugging
- Documentation
- Testing
- Refactoring

It does not contain project documentation or executable Claude Skills.

---

## Maintenance

Only add prompts that:

- Have been used successfully multiple times.
- Produce consistent results.
- Provide long-term value.
- Are tool-agnostic where practical.

Remove obsolete prompts as engineering workflows evolve.

---

# Research

## NotebookLM — Engineering Research

### Purpose

Research implementation questions using official documentation before making architectural or coding decisions.

### When to Use

- Before implementing new features.
- Before adopting new libraries.
- When validating engineering decisions.

### Supported Tools

- NotebookLM

### Prompt

<your standard NotebookLM research prompt>

### Expected Outcome

- Determine whether existing documentation is sufficient.
- Identify missing official documentation.
- Answer the engineering question using verified sources.

### Notes

Always prioritize official documentation over third-party sources.

---

# Architecture

(Added as the project evolves.)

---

# START APPLICATION

fastapi dev app/main.py

curl http://127.0.0.1:8000/health #

---

# Planning

(Added as the project evolves.)

---

# Code Review

(Added as the project evolves.)

Review this file and suggest meaningful comments that improve long-term maintainability.

Comment only where it helps explain:

- the intent of the code,
- the architectural decision,
- the reason a particular approach was chosen,
- non-obvious business rules,
- important implementation details that future developers should know.

Do NOT comment:

- obvious Python syntax,
- imports,
- simple assignments,
- self-explanatory code,
- every function or every line.

Comments should explain WHY, not WHAT.

Follow the project's coding standards and keep comments concise, accurate, and maintainable.

## for NOTEBOOKLM remember this prompt when trying to build any project ROADMAP 1ST PROMPT

Using the methodology defined in NOTEBOOKLM_RESEARCH_METHODOLOGY.md, determine whether the current project documentation and official documentation available in this notebook are sufficient to evaluate the implementation sequence of this project.

If additional official documentation is required, follow the methodology before answering.

If sufficient:

Research how production-quality software projects using the documented technology stack (Python, FastAPI, SQLModel, SQLAlchemy, PostgreSQL, Alembic, Pydantic, pytest, uv, and the project's documented tooling) are typically implemented.

Do not redesign the project.

Do not introduce technologies that are not part of the documented technology stack.

Your objective is to validate and refine the implementation sequence.

For every phase in ROADMAP.md:

1. Explain the engineering objective.
2. Determine whether the milestone order is appropriate.
3. Break every milestone into the smallest logical implementation tasks.
4. Define the completion criteria for every task.
5. Define the completion criteria for every milestone.
6. Verify the implementation order against official documentation and established engineering practices.
7. Identify any missing implementation tasks.
8. Identify any unnecessary tasks.
9. Explain why each task belongs to its milestone.
10. Clearly distinguish documented facts from engineering inference.

The final result should be an evidence-based implementation blueprint that can be followed from the first commit to production deployment while remaining consistent with the project's documented technology stack, architecture, coding standards, and engineering principles.

Do not generate source code.

Do not redesign the project architecture.

Focus only on defining the implementation sequence.

## 2ND PROMPT

Using the methodology defined in NOTEBOOKLM_RESEARCH_METHODOLOGY.md,

review the implementation blueprint you generated.

Your goal is to optimize it for long-term software engineering execution.

For every roadmap milestone:

- keep the original roadmap milestone names unchanged,
- create a repeatable template,
- define:
  • Objective
  • Official Documentation
  • Completion Criteria
  • Execution Tasks
  • Verification
  • Definition of Done

Do not introduce new roadmap milestones.

Do not change the milestone order.

Do not redesign the project.

Expand every roadmap milestone using the same template.

Do not skip any milestone.

Preserve the roadmap order and milestone names.

Every milestone must contain:

Objective
Official Documentation
Completion Criteria
Execution Tasks
Verification
Definition of Done

## The final result should be suitable for directly expanding ROADMAP.md into an engineering execution document while remaining concise, maintainable, and easy to follow throughout the lifetime of the project.

# Debugging

(Added as the project evolves.)

---

##

docs/

Core Project
├── PROJECT_VISION.md
├── REQUIREMENTS.md
├── ROADMAP.md
├── PROJECT_STATUS.md

Architecture
├── ARCHITECTURE.md
├── DATABASE_DESIGN.md
├── DATABASE_ARCHITECTURE.md
├── DATABASE_SCHEMA.md

Engineering
├── IMPLEMENTATION_GUIDE.md
├── CODING_STANDARDS.md
├── GIT_WORKFLOW.md
├── REPOSITORY_STANDARD.md
├── technology-stack.md

AI
├── AI_ENGINEERING_GUIDE.md
├── AI_DEVELOPMENT_PLAYBOOK.md
├── AI_COLLABORATION.md

# Documentation

(Added as the project evolves.)

---

# Testing

(Added as the project evolves.)

---

# Refactoring

(Added as the project evolves.)

---

# Revision Policy

The prompt library should evolve alongside the project.

Only retain prompts that:

- Are repeatedly useful.
- Improve engineering consistency.
- Reduce repetitive work.
- Are grounded in official documentation where applicable.
