### Version 1 Artifact Specification: `generate-commit.prompt.specification.md`

#### 1. Purpose
#### VERIFIED FACT
This prompt standardizes **Step 11 (Commit Preparation)** of the project's 11-step engineering lifecycle. It ensures that commit messages are accurate, evidence-based records of implemented truth that adhere to the project's **Git Workflow** and **Repository Truth Policy**.

#### 2. Scope
#### VERIFIED FACT
This specification governs the physical prompt file located at `.github/prompts/generate-commit.prompt.md` and its governing engineering specification in `docs/specifications/prompts/`. It applies exclusively to the generation of commit message content for completed implementation packages.

#### 3. Dependencies
#### VERIFIED FACT
*   **`docs/AI_DEVELOPMENT_WORKFLOW.md`**: Defines the lifecycle stage (Step 11) this prompt operationalizes.
*   **`docs/GIT_WORKFLOW.md`**: Provides the authoritative standards for commit principles, message formats, and types [409–411].
*   **`docs/COPILOT_CONFIGURATION.md`**: Classifies "Commit Message Generation" as an approved (Optional) capability.
*   **`docs/REPOSITORY_STANDARD.md`**: Establishes the Repository Truth Policy and the hierarchy of source-of-truth documents.
*   **`.github/copilot-instructions.md`**: Defines AI behavior boundaries and the mandatory requirement for Human Approval Gates.

#### 4. Inputs
#### VERIFIED FACT
The prompt requires the following data to generate a high-fidelity commit message:
*   **Approved Implementation Plan**: The Step 5 strategy that defined the scope of work.
*   **Implementation Diff**: The physical code changes produced and verified in Steps 6 and 7.
*   **Synchronized Documentation**: The updates made to `docs/` or `README.md` during Step 8.
*   **Current Repository State**: To ensure the summary is grounded in the broader repository context.

#### 5. Outputs
#### VERIFIED FACT
The prompt must produce a single, structured commit message that:
*   Follows the mandatory format: `<type>: <short summary>`.
*   Uses consistent **Commit Types** (e.g., `feat`, `fix`, `docs`, `refactor`).
*   Accurately summarizes only the implemented work represented by the supplied repository evidence.
*   Distinguishes implemented code changes from documentation or maintenance tasks.

#### 6. Relationship to Repository Instructions
#### VERIFIED FACT
Repository instructions provide persistent grounding in project identity and tech stack. This prompt provides **reusable tactical logic** for the final stage of the development lifecycle.

#### 7. Relationship to AI Development Workflow
#### VERIFIED FACT
This artifact is the operational implementation of **Step 11 (Commit Preparation)**. It bridges the gap between verified implementation and the permanent project history.

#### 8. Position within the 11-step engineering lifecycle
#### VERIFIED FACT
The prompt is triggered at **Step 11**, occurring after the **Step 10 Final Audit** is complete and before the physical git commit and push actions are executed.

#### 9. Required Prompt Inputs
#### VERIFIED FACT
Using official GitHub prompt file syntax, the prompt shall utilize:
*   `${input:plan}`: The approved implementation strategy from Step 5.
*   `${input:diff}`: The physical code and test changes produced in Steps 6 and 7.
*   `${input:docs}`: The physical documentation changes produced in Step 8.
*   `${input:context}`: Reference to the current repository state or project standards.

#### 10. Expected Prompt Output
#### ENGINEERING RECOMMENDATION
The output should be formatted as a **Proposed Commit Message** block.
*   **Rationale**: Isolating the message in a dedicated block allows the Human Developer to quickly copy or approve the content without extracting it from conversational prose.

#### 11. Prompt Constraints
#### VERIFIED FACT
The prompt must NOT:
*   **Generate Git commands** (e.g., `git commit -m "..."`). It must only produce message content [Query Requirement].
*   **Invent features** or summarize work not present in the supplied repository evidence.
*   Include unrelated changes or "miscellaneous" summaries.
*   Bypass manual **Human Approval Gates**.

#### 12. Human Approval Gates
#### VERIFIED FACT
The output of this prompt is **advisory**. The Human Developer must manually review and approve the proposed commit message before it is used in the repository's version history.

#### 13. Verification Requirements
#### VERIFIED FACT
The prompt must instruct the agent to utilize **observable repository evidence** (implementation diffs, synchronized documentation, and current repository state) rather than assertions of success to justify the content of the message.

#### 14. Definition of Done
#### VERIFIED FACT
A commit preparation task is complete when the generated message accurately reflects implemented truth, adheres to the project's formatting standards, and is ready for Human Developer review.

#### 15. Repository Boundaries
#### VERIFIED FACT
The prompt must focus exclusively on the **current implementation package** and the changes represented in the provided inputs.

#### 16. Prompt Lifecycle
#### VERIFIED FACT
This artifact is currently in the **Planned** stage of the **Repository Truth Policy**.

---

### 1. Evidence Classification

| Section | Label | Rationale |
| :--- | :--- | :--- |
| **1–9. Purpose through Inputs** | ## VERIFIED FACT | Derived from `AI_DEVELOPMENT_WORKFLOW.md`, `GIT_WORKFLOW.md`, and `COPILOT_CONFIGURATION.md`. |
| **10. Expected Prompt Output** | ## ENGINEERING RECOMMENDATION | Structured output blocks are an established repository convention for reviewability. |
| **11–16. Constraints through Lifecycle** | ## VERIFIED FACT | Transcribed from frozen AI Behavior Boundaries, `GIT_WORKFLOW.md`, and the **Repository Truth Policy**. |

---

### 2. Gap Analysis

| Section | Status | Product | Exact Documentation Topic |
| :--- | :--- | :--- | :--- |
| **9. Prompt Variables** | Partially Supported | GitHub | Prompt files (Public Preview) |

**Analysis**: The specification is fully supported by the frozen repository governance. The only remaining uncertainty is the exact behavior of the `${input:docs}` variable when expanding multiple file diffs in the GitHub Copilot Public Preview.

---

### 3. Required Official Documentation

No additional official documentation is required. The **"Prompt Files"** syntax examples in the knowledge base provide sufficient evidence for frontmatter and variable usage [722–723, 757].

---

### 4. Final Verdict

**READY FOR ENGINEERING REVIEW**
