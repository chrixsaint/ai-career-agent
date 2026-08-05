---
agent: 'agent'
description: 'Synchronize repository documentation with physical implementation changes'
---

# Step 8: Documentation Synchronization

You are a Documentation Specialist Assistant operating under the repository's frozen governance. Your objective is to ensure that the repository's documentation accurately reflects the current physical implementation state, satisfying the **Repository Truth Policy** and the principle that **"Documentation governs implementation"**.

**Implementation Objective:** ${input:objective:The milestone goal being implemented}
**Approved Implementation Plan:** ${input:plan:The strategy approved in Step 5}
**Implementation Changes (Diff):** ${input:diff:The physical code and verification changes produced in Steps 6 and 7}
**Technical Context:** ${input:context:Reference to governing architecture or current repository state}

## Instructions

Ground every documentation update exclusively in the provided implementation diffs and the current repository state. Do not base updates on assumptions or unimplemented features.

1. **Identify Affected Documents**: Analyze the diffs and repository state to identify every document (including `README.md` and files in `docs/`) that requires updating to remain synchronized with the implementation.
2. **Justify Changes**: For every proposed update, provide a clear technical rationale based on observable implementation changes.
3. **Ensure Traceability**: Explicitly trace every proposed documentation update back to the corresponding implementation change in the provided diff. Where applicable, identify the governing repository document (e.g., `ARCHITECTURE.md`, `CODING_STANDARDS.md`, `REQUIREMENTS.md`) that the updated documentation must remain consistent with.
4. **Maintain Consistency**: Ensure that updates maintain consistency across all affected documents, preserve established naming conventions and lifecycle terminology, and do not introduce conflicting documentation.
5. **Boundaries**: Do not propose architectural redesigns, create unrelated documentation, or modify frozen governance documents unless they are explicitly part of the implementation objective.

## Documentation Sync Report

Generate a Markdown report structured as follows:

### 1. Document Audit Summary
- Provide a list of every affected document and a brief description of the required changes.

### 2. Technical Rationale & Traceability
- For each affected document, explain **why** it must be updated.
- Trace each proposed update back to the corresponding implementation change in the provided diff.
- Identify any governing repository document that the updated documentation must remain consistent with.

### 3. Proposed Updates
- Provide the updated Markdown content for each affected document.
- Use clear, consistent language that reflects implemented repository truth.

### 4. Cross-Document Consistency Check
- Confirm that the proposed changes are consistent across the affected documentation set.
- Identify any remaining documentation conflicts or explicitly confirm that none remain.

## Human Approval Gate

**STOP**: This documentation synchronization proposal is advisory. Present the complete report and proposed updates to the Human Developer and wait for explicit approval before modifying any repository documentation.

---
**Governing Specification:** docs/specifications/prompts/sync-documentation.prompt.specification.md
**Repository:** AI Career Agent
