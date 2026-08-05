### 1. Artifact Specification: `implementation-plan.prompt.md`

#### 1. Purpose

#### VERIFIED FACT

This prompt standardizes **Step 5 (Implementation Planning)** of the project's development lifecycle. It ensures that before any code is modified in Step 6, a detailed, human-reviewable strategy is produced that adheres to the **"Foundation First"** principle and repository standards.

#### 2. Scope

#### VERIFIED FACT

This specification governs the physical prompt file located at `.github/prompts/implementation-plan.prompt.md`. It applies specifically to the transition from high-level architecture validation to incremental source code implementation.

#### 3. Dependencies

#### VERIFIED FACT

- **`docs/AI_DEVELOPMENT_WORKFLOW.md`**: Provides the 11-step lifecycle this prompt implements.
- **`docs/COPILOT_CONFIGURATION.md`**: Establishes the classification of the prompt as a **Required** configuration.
- **`docs/PROMPT_LIBRARY.md`**: Defines the design principles (Single Responsibility) and standard structure.
- **`.github/copilot-instructions.md`**: Provides the permanent grounding context (architecture, tech stack) the plan must respect.

#### 4. Inputs

#### VERIFIED FACT

The prompt requires the following data to generate a valid plan:

- The specific implementation objective for the active implementation package or milestone.
- Relevant **Frozen Documentation** (e.g., `REQUIREMENTS.md`, `ARCHITECTURE.md`).
- Current **Physical Repository State** (existing code and directory structure).

#### 5. Outputs

#### VERIFIED FACT

The prompt must produce a structured Implementation Plan including:

- A list of files to be created or modified.
- Recommended implementation order.
- Verification steps for each change (Step 7 alignment).
- Confirmation of compliance with the **Single Responsibility Principle**.

#### 6. Relationship to Repository Instructions

#### VERIFIED FACT

While repository instructions provide **permanent context** (the "Who" and "What"), this prompt provides **reusable task logic** (the "How") for the planning phase.

#### 7. Relationship to AI Development Workflow

#### VERIFIED FACT

This artifact is the operational implementation of **Step 5 (Implementation Planning)** of the development workflow.

#### 8. Position inside the 11-step engineering lifecycle

#### VERIFIED FACT

The prompt is triggered at **Step 5**. Its output is a mandatory prerequisite for **Step 6 (Incremental Implementation)**.

#### 9. Required Prompt Inputs

#### VERIFIED FACT

Using official GitHub prompt file syntax, the prompt shall utilize:

- `${input:objective}`: Brief description of the task.
- `${input:context}`: Reference to governing architecture or requirements.

#### 10. Expected Prompt Output

#### ENGINEERING RECOMMENDATION

The output should be formatted as a Markdown implementation checklist.

- **Rationale**: A checklist provides a structured, reviewable implementation plan before execution begins.

#### 11. Prompt Constraints

#### VERIFIED FACT

The generated plan must NOT:

- Independently redesign repository architecture.
- Propose modifications to frozen governance documents.
- Introduce parallel implementation patterns (must reuse existing ones).

#### 12. Human Approval Gates

#### VERIFIED FACT

The output of this prompt (the Implementation Plan) **requires explicit Human Developer approval** before the agent is permitted to begin implementation (Step 6).

#### 13. Verification Requirements

#### VERIFIED FACT

The prompt must instruct the agent to define verification commands (e.g., `uv sync`, `ruff check`, `pytest`) as part of the plan.

#### 14. Definition of Done

#### VERIFIED FACT

A planning task is complete when the generated implementation plan satisfies the applicable functional requirements, conforms to `ARCHITECTURE.md`, and is ready for Human Developer approval before implementation begins.

#### 15. Repository Boundaries

#### VERIFIED FACT

The prompt must enforce that implementation units are **Feature-by-Feature** and **Milestone-by-Milestone** rather than massive, monolithic changes.

#### 16. Prompt Lifecycle

#### VERIFIED FACT

This artifact is currently in the **Planned** stage of the **Repository Truth Policy**.

---

### 2. Evidence Classification

| Section                                         | Label                         | Rationale                                                                                                                                            |
| :---------------------------------------------- | :---------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- |
| **1-9. Purpose through Required Prompt Inputs** | ## VERIFIED FACT              | Directly derived from `AI_DEVELOPMENT_WORKFLOW.md`, `COPILOT_CONFIGURATION.md`, `PROMPT_LIBRARY.md`, and official GitHub Prompt Files documentation. |
| **10. Expected Prompt Output**                  | ## ENGINEERING RECOMMENDATION | Markdown checklist formatting is a practical engineering convention rather than a repository requirement.                                            |
| **11-16. Constraints through Lifecycle**        | ## VERIFIED FACT              | Directly implemented from frozen repository governance and the Repository Truth Policy.                                                              |

---

### 3. Gap Analysis

| Section                 | Status              | Product | Exact Documentation Topic     |
| :---------------------- | :------------------ | :------ | :---------------------------- |
| **9. Prompt Variables** | Partially Supported | GitHub  | Prompt files (Public Preview) |

**Analysis**: The specification is fully supported by the established repository governance. The remaining uncertainty concerns implementation details of GitHub Prompt Files that remain in Public Preview.

---

### 4. Required Official Documentation

No additional official documentation is required to implement Version 1. The Prompt Files documentation already present in the project knowledge base provides sufficient evidence for the frontmatter and input variable syntax.

---

### 5. Final Verdict

**READY FOR ENGINEERING REVIEW**
