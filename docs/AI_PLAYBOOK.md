# AI Playbook

> **Purpose:** This document defines the AI Engineering Operating System for this repository. It explains the role of each AI tool, when to use it, and how the tools work together throughout the development lifecycle.

---

# AI Tool Selection Principles

Choose the tool that best matches the task.

- Use the right tool for the right problem.
- Prefer the smallest tool capable of completing the task.
- Verify important engineering decisions using official documentation.
- Avoid asking multiple tools to solve the same problem unless performing validation or review.

---

# NotebookLM

**Primary Role**

Research and knowledge retrieval.

**Use For**

- Requirements lookup
- Architecture questions
- Official documentation
- Engineering standards
- Design validation
- Learning project context

**Avoid**

- Writing production code
- Modifying repository files
- Creating repository conventions

---

# VS Code Copilot

**Primary Role**

Implementation assistance inside the development environment.

**Use For**

- Code generation
- Boilerplate
- Refactoring
- Unit tests
- Inline documentation
- Repository-aware coding assistance

**Avoid**

- High-level architecture decisions
- Project planning
- Requirement interpretation without supporting documentation

---

# ChatGPT

**Primary Role**

Engineering reasoning and technical design.

**Use For**

- System architecture
- Design discussions
- Code reviews
- Complex debugging
- Engineering trade-offs
- Development planning
- Documentation design
- AI engineering framework design

**Avoid**

- Acting as the primary source of official documentation
- Replacing repository-specific standards
- Making implementation decisions without project context

---

# Collaboration Strategy

The AI tools complement one another.

Typical workflow:

1. Research with NotebookLM.
2. Validate against official documentation.
3. Design with ChatGPT.
4. Implement with VS Code Copilot.
5. Verify and review before committing.

---

# Guiding Principle

No AI assistant is the source of truth.

- Official documentation is the authority for technical standards.
- The Git repository is the authority for project knowledge.
- AI assistants help interpret, implement, and improve the project while following repository standards.

---

**Last Updated:** 2026-08-01
