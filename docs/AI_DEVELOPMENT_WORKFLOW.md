# AI Development Workflow

**Status:** Draft – Pending Final Engineering Audit

**Version:** 1.0.0

---

# Purpose

This document defines the permanent AI-assisted software engineering workflow for the AI Career Agent project.

It implements the approved **AI_WORKFLOW_SPECIFICATION.md** and establishes the operational engineering process used throughout the repository.

The workflow governs the complete software development lifecycle, including:

- research
- architecture
- implementation
- verification
- documentation
- repository governance

The workflow exists to ensure that every implementation:

- follows repository standards
- minimizes architectural drift
- minimizes duplicated effort
- minimizes merge conflicts
- minimizes AI hallucinations
- remains fully traceable from requirements through implementation

This workflow applies to every feature, bug fix, refactor, documentation update, and architectural change within the repository.

---

# 1. Workflow Architecture

The repository follows a modular engineering pipeline.

Each stage has a clearly defined responsibility.

No stage may be skipped.

```mermaid
graph TD

A[Define Objective]

--> B[Research - NotebookLM]

B --> C[Verify Official Documentation]

C --> D[Architecture Review - ChatGPT]

D --> E[Specification Validation - NotebookLM]

E --> F[Implementation Planning]

F --> G[Implementation]

G --> H[Verification]

H --> I[Documentation Synchronization]

I --> J[PROJECT_STATUS Update]

J --> K[Repository Audit]

K --> L[Atomic Commit]

L --> M[Milestone Review]


Every stage produces an observable output that becomes the input for the following stage.

Implementation must never bypass verification.


### 2. Engineering Responsibilities
Every participant in the workflow has clearly defined responsibilities, explicit boundaries, and required approval gates. No tool may operate outside its assigned responsibility.

#### 2.1 Human Developer (Authoritative)
*   **Primary Responsibility**: Authoritative engineering decision-maker. Defines objectives, approves architecture, reviews AI-generated code, and authorizes all commits.
*   **Outside Responsibility**: Should not perform repetitive implementation tasks that can be delegated to AI after sufficient verification.
*   **Approval Gate**: Must manually review and approve every file diff before a commit is created.

#### 2.2 NotebookLM (Verification)
*   **Primary Responsibility**: Documentation research, specification validation, and cross-document consistency audits.
*   **Outside Responsibility**: Does not implement production code, approve commits, or replace human governance.
*   **Approval Gate**: Findings must be verified by a Human Developer if they conflict with frozen repository standards.

#### 2.3 ChatGPT (Design)
*   **Primary Responsibility**: Engineering design, architecture review, and trade-off analysis.
*   **Outside Responsibility**: Does not replace official documentation or serve as the authoritative repository specification.
*   **Approval Gate**: Architectural proposals require human validation against `ARCHITECTURE.md` before adoption.

#### 2.4 Claude Code (Execution)
*   **Primary Responsibility**: Implementation planning, multi-file coding, and repository-aware refactoring.
*   **Outside Responsibility**: Does not modify frozen specifications or approve architectural changes without human intervention.
*   **Approval Gate**: Plan Mode output must be human-approved before execution begins.

#### 2.5 GitHub Copilot (Assistance)
*   **Primary Responsibility**: Inline completions, semantic search, and autonomous task completion via Agent Mode.
*   **Outside Responsibility**: Does not determine repository architecture or modify standards independently.
*   **Approval Gate**: Agent Mode changes must be reviewed by the Human Developer before inclusion in an Implementation Package.






# 4. Development Lifecycle

Every implementation follows the same engineering sequence.

| Step | Activity | Primary Responsibility |
|------|---------------------------|----------------|
| 1 | Define Objective | Human |
| 2 | Research | NotebookLM |
| 3 | Verify Official Documentation | Human |
| 4 | Architecture Review | ChatGPT |
| 5 | Specification Validation | NotebookLM |
| 6 | Implementation Planning | Claude Plan Mode |
| 7 | Incremental Implementation | Claude / Copilot |
| 8 | Verification (Tests, Ruff, Builds) | Human + AI |
| 9 | Documentation Synchronization | Human + AI |
| 10 | PROJECT_STATUS.md Update | Human |
| 11 | Final Repository Audit | NotebookLM |
| 12 | Atomic Commit | Git |
| 13 | Milestone Review | Human |

No implementation should bypass this lifecycle.



# 5. AI Session Start Checklist

Before every implementation session:

- Pull the latest repository changes.
- Review PROJECT_STATUS.md.
- Identify the current milestone.
- Review the relevant architecture documents.
- Review repository standards.
- Confirm implementation scope.
- Confirm affected files.
- Confirm verification requirements.
- Load required repository context.
- Begin implementation.

```
# 6. AI Session End Checklist

Before ending every session:

- Run Ruff.
- Run tests.
- Verify build success.
- Update affected documentation.
- Update PROJECT_STATUS.md.
- Verify repository consistency.
- Record new research gaps.
- Commit atomically.


# 7. Implementation Package

Every implementation shall be organized as an Implementation Package.

Each package shall contain:

## Objective

What is being implemented.

## Requirements

Functional and non-functional requirements.

## Files

Every file expected to change.

## Documentation

Every document requiring updates.

## Verification

Required commands.

Examples:

- ruff check
- pytest
- build commands

## Completion Criteria

Definition of Done.

## Research Dependencies

Outstanding documentation gaps.


# 8. Implementation Units

Large milestones shall be divided into independently verifiable implementation units.

Implementation strategy:

- Milestone-by-Milestone planning
- Feature-by-Feature implementation
- File-by-File execution

Foundation-first ordering:

1. contracts
2. interfaces
3. data models
4. abstract implementations
5. concrete implementations
6. tests
7. documentation



# 9. Milestone Completion

A milestone is complete only when:

- all functional requirements are implemented
- architecture remains consistent
- Ruff passes
- tests pass
- documentation is synchronized
- PROJECT_STATUS.md is updated
- NotebookLM verification succeeds


### 10. Documentation Governance
Repository documentation follows the Single Source of Truth principle.

#### 10.1 Document Taxonomy
| Category | Definition | Update Trigger |
| :--- | :--- | :--- |
| **Authoritative** | Permanent project standards (e.g., `CODING_STANDARDS.md`). | When official tool or framework standards change. |
| **Frozen** | Approved architectural specifications (e.g., `base.py` contract). | Only to correct genuine engineering errors. |
| **Versioned** | Schemas and configurations tied to code state (e.g., API schemas). | Alongside the implementation change. |
| **Historical** | Records of project activity (e.g., Git history, migrations). | Automatically upon task completion. |
| **Temporary** | Disposable research and planning notes. | Deleted or archived after milestone completion. |
``
### 11. Prompt Governance
Prompt files are treated as versioned repository logic.

#### 11.1 Lifecycle & Categories
*   **Permanent**: Global project logic (e.g., `.github/prompts/review-code.prompt.md`).
*   **Reusable**: Modular logic for specific subsystems.
*   **Task-specific**: Disposable instructions for a single implementation session.
*   **Experimental**: Unverified prompts being tested for future promotion.

#### 11.2 Operational Procedures
*   **Ownership**: Authoritative prompts are owned by the Human Developer; task prompts are owned by the active Agent.
*   **Review Requirements**: Any new permanent or reusable prompt requires human code review before being committed to `.github/prompts/`.
*   **Versioning**: Prompts follow standard Git versioning alongside the code they support.
*   **Retirement Policy**: Task-specific prompts must be removed from the workspace after the corresponding PR is merged. Experimental prompts are retired if they fail to improve accuracy after two sessions.

#### 12.1 Configuration Status
*   **Required**:
    *  `.github/copilot-instructions.md` (Grounding)
    *  `.github/prompts/` (Reusable logic)
    *  Workspace Context (@ references)
*   **Optional**:
    *  Chat Mode (Iterative troubleshooting)
    *  Semantic Search (Exploration)
    *  Inline Completions (Manual coding acceleration)
*   **Future**:
    *  Extensions & External Agents (MCP integration)
    *  Agentic Workflows (Phase 6 automation)



# 13. Verification Workflow

Evidence is always preferred over assertions.

Verification shall include:

- Ruff
- pytest
- build verification
- runtime verification
- implementation review
- documentation review

Successful execution must be observable.


# 14. Error Recovery Workflow

If implementation fails:

1. Stop the AI immediately.
2. Restore the last working state.
3. Clear irrelevant context.
4. Identify the failure.
5. Research official documentation.
6. Improve the prompt.
7. Restart implementation.

After two unsuccessful correction attempts:

- stop implementation
- perform additional research
- update documentation if necessary


# 15. Research Workflow

Research must begin whenever:

- official documentation is missing
- repository standards conflict
- architecture becomes unclear
- implementation cannot be verified
- AI tools disagree

Research outputs should either:

- resolve the issue

or

- be recorded in

RESEARCH_BACKLOG.md



# 16. Repository Governance

Repository precedence:

1. Official Documentation
2. Repository Standards
3. Frozen Specifications
4. Project Documentation
5. Source Code
6. Knowledge Base

Significant architectural changes must update documentation before implementation begins.


# 17. Operational Rules

The following rules are mandatory.

1. Research before implementation.
2. Verify before coding.
3. Implement incrementally.
4. Verify every implementation.
5. Synchronize documentation immediately.
6. Record milestone progress.
7. Audit before committing.
8. Commit atomically.
9. Never bypass repository standards.
10. Never allow implementation to redefine architecture.



# 18. Workflow Completion

The workflow is considered complete when:

- implementation satisfies requirements
- repository standards remain consistent
- documentation is synchronized
- verification succeeds
- NotebookLM confirms architectural consistency
- PROJECT_STATUS.md reflects the repository state
- the implementation is committed atomically

Only then may work begin on the next implementation package.
```
