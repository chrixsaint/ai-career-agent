# AI Collaboration Guide

## Purpose

This document defines the human-AI collaboration workflow used in this repository.

Its purpose is to ensure consistent execution from research to implementation while preserving developer ownership of decisions.

---

# Collaboration Workflow

Use this workflow for documentation and implementation tasks:

1. Research with NotebookLM.
2. Verify findings against official documentation.
3. Design options with ChatGPT.
4. Implement in the repository with Copilot or Claude Code.
5. Review and verify before commit.

---

# Role Boundaries

- NotebookLM: research and source retrieval
- ChatGPT: engineering reasoning and design trade-offs
- Copilot and Claude Code: repository-aware implementation
- Developer: final decision authority and approval

AI assistants support decisions; they do not replace developer ownership.

---

# Collaboration Rules

- Follow repository standards and existing architecture.
- Avoid duplicate documentation and duplicate implementations.
- State assumptions when context is missing.
- Keep changes small, reviewable, and verifiable.
- Update related documentation when implementation changes affect it.

---

# Verification Before Commit

Before committing AI-assisted work:

- Confirm the change matches the requested scope.
- Confirm tests/validation steps were performed where applicable.
- Confirm documentation remains consistent with the change.
