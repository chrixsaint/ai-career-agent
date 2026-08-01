# Prompt Library

## Purpose

This document contains reusable prompts that support AI-assisted development of the AI Career Agent.

The prompts in this library are intended for repeated engineering tasks and have been refined through practical use.

Unlike `.claude/skills/`, this document is designed for human reference and can be used with NotebookLM, ChatGPT, Claude Code, and GitHub Copilot.

---

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

# Planning

(Added as the project evolves.)

---

# Code Review

(Added as the project evolves.)

---

# Debugging

(Added as the project evolves.)

---

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
