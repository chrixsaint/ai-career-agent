### Version 1 Artifact Specification: implement-approved-corrections.prompt.specification.md

#### 1. Purpose

This prompt standardizes the transition from **Audit/Review Findings** to **Implemented Corrections**. It ensures that when an Engineering Review or NotebookLM Evidence Audit identifies approved corrections, those corrections are implemented precisely without introducing architectural drift or unapproved scope expansion.

#### 2. Responsibility

This prompt has one engineering responsibility:

**Physical Implementation of Approved Corrections.**

It is strictly prohibited from:

- redesigning architecture or standards;
- generating implementation plans;
- evaluating its own work;
- introducing features not explicitly mandated by the approved audit report.

#### 3. Workflow Position

- **Trigger:** Triggered when an Engineering Review or NotebookLM Evidence Audit identifies approved corrections requiring implementation.
- **Pre-requisite:** An approved Engineering Review or Evidence Audit containing explicit corrections to implement.
- **Successor:** Return to repository verification after implementation is complete.

#### 4. Dependencies

- **REPOSITORY_STANDARD.md** — Repository Truth Policy and repository governance.
- **AI_DEVELOPMENT_WORKFLOW.md** — Engineering workflow and implementation lifecycle.
- **COPILOT_CONFIGURATION.md** — GitHub Copilot behavior and Human Approval Gates.
- **PROMPT_LIBRARY.md** — Synchronization between prompt specifications and implementations.

#### 5. Required Prompt Inputs

The prompt shall accept the following implementation inputs:

- Approved corrections from the Engineering Review or NotebookLM Evidence Audit.
- The approved implementation plan when applicable.
- The target repository artifact requiring modification.
- Any governing repository documents required to implement the approved corrections.

#### 6. Expected Prompt Output

The prompt shall produce an implementation report structured as follows:

1. Gap Resolution Summary.
2. Updated Artifact.
3. Verification Commands required after implementation.

#### 7. Implementation Constraints

- **Zero Innovation:** Implement only the approved corrections. If any correction is ambiguous, request clarification rather than assuming intent.
- **Preserve Frozen Governance:** Do not modify frozen governance artifacts unless the approved correction explicitly targets them.
- **Repository Governance Precedence:** Repository governance remains the authoritative source for repository-specific behavior. Official documentation shall be consulted whenever repository governance requires verification of external standards or technologies, consistent with the Repository Source of Truth Policy.

#### 8. Human Approval Requirements

**STOP**

The output of this prompt is advisory.

The Human Developer must review the implemented corrections before the implementation proceeds to verification.

#### 9. Verification Expectations

Implementation is verified only when observable verification evidence demonstrates that each approved correction has been implemented successfully.

Assertions that an issue has been corrected are insufficient.

#### 10. Completion Criteria

A correction task is complete when:

1. Every approved correction has been implemented.
2. Required verification commands have completed successfully.
3. The updated artifact remains consistent with repository governance and the approved implementation plan where applicable.

#### 11. Prompt Lifecycle

- **Current State:** **Frozen**
- **Status:** **Approved for Freeze**
- **Physical Path:** `.github/prompts/implement-approved-corrections.prompt.md`
- **Specification Path:** `docs/specifications/prompts/implement-approved-corrections.prompt.specification.md`
