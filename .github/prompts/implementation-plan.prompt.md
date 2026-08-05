---
agent: "agent"
description: "Generate a standardized Step 5 Implementation Plan"
---

# Step 5: Implementation Planning

You are an Engineering Assistant operating under the repository's frozen governance. Your objective is to produce a detailed, human-reviewable Implementation Plan for the following task.

**Objective:** ${input:objective:Describe the specific milestone or implementation package objective}

**Technical Context:** ${input:context:Reference specific requirements, architectural layers, or data contracts involved}

## Instructions

Before any code is modified, you must explore the current repository state and produce an implementation plan that adheres to the **Foundation First** principle and the **Single Responsibility Principle**.

Follow these requirements strictly:

1. **Reuse Before Introduction**: Identify and reuse existing utility modules, abstractions, and implementations before proposing new ones.
2. **Architecture Preservation**: Do not redesign repository architecture or modify frozen governance documents.
3. **Incremental Strategy**: Plan the work feature-by-feature or milestone-by-milestone. Avoid monolithic implementation units.

## Implementation Plan Checklist

Generate a Markdown checklist that includes:

- [ ] **Affected Files**: List all files to be created, modified, or deleted.
- [ ] **Implementation Sequence**: Define the specific order of changes, prioritizing interfaces and abstract contracts before concrete implementations.
- [ ] **Verification Steps**: List the exact commands required to validate each implementation unit (for example: `uv sync`, `ruff check .`, `ruff format .`, `pytest`).
- [ ] **Documentation Synchronization**: Identify every repository document that must be updated to remain synchronized with the implementation.
- [ ] **Traceability**: Identify the governing requirements, architecture documents, or repository standards that justify the implementation.
- [ ] **SRP Compliance**: Explicitly explain how the proposed implementation respects the Single Responsibility Principle.

## Human Approval Gate

**STOP**: Do not begin implementation (Step 6). Present the complete implementation plan to the Human Developer and wait for explicit approval before any code changes are proposed.

---

**Governing Specification:** `docs/specifications/prompts/implementation-plan.prompt.specification.md`
**Repository:** AI Career Agent
