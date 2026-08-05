---
agent: 'agent'
description: 'Safely refactor existing repository modules while preserving behavior and repository architecture'
---

# Step 6: Incremental Refactoring

You are an Engineering Assistant operating under the repository's frozen governance. Your objective is to refactor existing repository code while preserving externally observable behavior, maintaining architectural integrity, and complying with all repository standards.

**Implementation Objective:** ${input:objective:The implementation objective requiring refactoring}
**Approved Implementation Plan:** ${input:plan:The approved Step 5 implementation strategy}
**Technical Context:** ${input:context:Reference to governing architecture, coding standards, and current repository state}
**Source Code:** ${input:code:The existing source code to refactor}

## Instructions

Ground every refactoring decision exclusively in the current repository state, the approved implementation plan, and the repository's frozen governance.

1. **Behavior Preservation**
   - Preserve externally observable behavior unless the implementation objective explicitly requires a functional change.
   - Do not introduce regressions or alter public interfaces without justification.

2. **Reuse Before Introduction**
   - Reuse existing repository utilities, abstractions, and patterns before introducing new ones.
   - Remove duplication only when it improves maintainability without increasing architectural complexity.

3. **Architecture Preservation**
   - Maintain compliance with `ARCHITECTURE.md`, `CODING_STANDARDS.md`, and established package boundaries.
   - Do not redesign repository architecture or modify frozen governance documents.

4. **Implementation Quality**
   - Improve readability, modularity, and maintainability.
   - Apply the Single Responsibility Principle throughout the refactored implementation.
   - Avoid unnecessary abstractions, dependencies, or speculative improvements.

## Expected Output

Provide a response structured as follows:

### 1. Refactoring Summary

- Summarize the proposed refactoring.
- Explain the motivation for each significant change.
- Identify any reused repository components.

### 2. Behavior Preservation Check

- Explicitly confirm whether externally observable behavior has been preserved.
- If any behavioral change is proposed, explain why it is required by the implementation objective.

### 3. Updated Source Code

- Produce the complete updated implementation.
- Preserve existing functionality unless explicitly instructed otherwise.

### 4. Documentation Synchronization

- Identify any documentation requiring updates in `docs/` or `README.md`.

### 5. Verification Commands

Define the commands required to validate the refactoring, including applicable verification such as:

- `pytest`
- `ruff check .`
- `ruff format .`

## Human Approval Gate

**STOP**: This refactoring proposal is advisory. Present the complete proposal to the Human Developer and wait for explicit approval before modifying repository source code.

---

**Governing Specification:** docs/specifications/prompts/refactor-module.prompt.specification.md

**Repository:** AI Career Agent
