# AI Collaboration

> **Purpose:** This document defines how developers collaborate with AI tools throughout the software development lifecycle. It establishes the human responsibilities, collaboration practices, and verification processes required to use AI effectively while maintaining engineering quality.

The AI Playbook defines **tool responsibilities**.

This document defines **collaboration practices**.

Repository governance is defined in `REPOSITORY_STANDARD.md`.

---

# Guiding Principles

The repository follows these principles when collaborating with AI.

- The human developer is responsible for all final technical decisions.
- AI assists engineering; it does not replace engineering judgment.
- Official documentation takes precedence over AI-generated responses.
- Repository standards take precedence over AI suggestions.
- Trust AI outputs only after verification.

---

# Collaboration Workflow

The recommended workflow is:

1. Define the objective.
2. Provide relevant context.
3. Review the proposed solution.
4. Verify against official documentation when necessary.
5. Implement incrementally.
6. Validate the result.
7. Review before committing.

AI collaboration should be iterative rather than relying on a single prompt.

---

# Context Management

Provide AI with relevant, high-quality context.

Examples include:

- Repository documentation
- Source code
- Error messages
- Stack traces
- Build output
- Test failures

Reference files directly whenever possible instead of describing them.

Avoid providing unrelated information that increases context without improving understanding.

---

# Planning Before Implementation

For non-trivial work:

- Explore the existing codebase.
- Understand the current architecture.
- Produce an implementation plan.
- Review the plan before editing code.

Planning should precede implementation.

---

# Incremental Development

Large changes should be divided into smaller, reviewable tasks.

Each task should:

- Have a clear objective.
- Produce a working result.
- Be independently verifiable.

Prefer multiple small improvements over one large AI-generated change.

---

# Verification

AI-generated work should always be verified.

Whenever practical:

- Run tests.
- Run the application.
- Verify build output.
- Review generated code.
- Compare implementation against requirements.

Prefer evidence over assertions.

Successful verification should be based on observable results rather than AI confidence.

---

# Human Review

Before accepting AI-generated work, review it for:

- Correctness
- Readability
- Maintainability
- Simplicity
- Consistency with repository standards

The human developer retains final responsibility for every accepted change.

---

# Managing AI Context

Long conversations can reduce AI effectiveness.

When changing tasks:

- Start a new conversation when appropriate.
- Remove irrelevant context.
- Keep prompts focused on one objective.

Provide only the information needed to complete the current task.

---

# Understanding AI Limitations

AI tools can:

- Misinterpret incomplete context.
- Introduce unnecessary complexity.
- Generate incorrect implementations.
- Produce plausible but inaccurate information.

Treat AI as an engineering assistant rather than an authoritative source.

---

# Repository Responsibilities

When collaborating with AI:

- Follow `REPOSITORY_STANDARD.md`.
- Follow `CODING_STANDARDS.md`.
- Follow `GIT_WORKFLOW.md`.
- Verify architectural decisions against `ARCHITECTURE.md`.
- Verify implementation against `REQUIREMENTS.md`.

Repository documentation remains the primary project reference.

---

# Scope

This document defines human collaboration with AI.

It does **not** define:

- AI tool responsibilities
- Repository organization
- Coding standards
- System architecture
- Project planning

Those responsibilities belong to their respective documents.

---

# Continuous Improvement

AI collaboration practices should evolve alongside AI tooling.

New workflows should be adopted only after they demonstrate clear improvements in engineering quality, maintainability, or developer productivity.
