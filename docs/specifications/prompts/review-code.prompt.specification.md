### Version 1 Artifact Specification: `review-code.prompt.specification.md`

#### 1. Purpose
#### VERIFIED FACT
This prompt standardizes **Step 7 (Verification)** and **Step 10 (Final Audit)** of the project's 11-step engineering lifecycle. It ensures that all code modifications are subjected to an **adversarial review** process that prioritizes evidence over assertions and verifies compliance with frozen repository governance.

#### 2. Scope
#### VERIFIED FACT
This specification governs the physical prompt file located at `.github/prompts/review-code.prompt.md` and its governing engineering specification located in `docs/specifications/prompts/`. It applies to the transition from incremental implementation to the final commit and push phases.

#### 3. Dependencies
#### VERIFIED FACT
*   **`docs/AI_DEVELOPMENT_WORKFLOW.md`**: Provides the engineering lifecycle stages (7 and 10) this prompt implements.
*   **`docs/COPILOT_CONFIGURATION.md`**: Establishes the classification of the prompt as a **Required** configuration.
*   **`docs/PROMPT_LIBRARY.md`**: Defines the design principles (Single Responsibility) and standard structure.
*   **`docs/CODING_STANDARDS.md`**: Provides the authoritative criteria for implementation quality.
*   **`.github/copilot-instructions.md`**: Provides the persistent grounding context and AI behavior boundaries.

#### 4. Inputs
#### VERIFIED FACT
The prompt requires the following data to execute an effective review:
*   The **Implementation Objective** for the active milestone.
*   The **Approved Implementation Plan** from Step 5.
*   The **Source Code Diff** representing the changes to be verified.
*   The **Current Repository State** to ensure findings are grounded in implemented repository truth.
*   Frozen repository standards (e.g., `ARCHITECTURE.md`, `CODING_STANDARDS.md`, `REQUIREMENTS.md`).

#### 5. Outputs
#### VERIFIED FACT
The prompt must produce a structured Adversarial Review Report including:
*   Identification of **correctness gaps** or edge cases missed.
*   Verification of compliance with the **Single Responsibility Principle** and **Modular Architecture**.
*   Confirmation that the **Definition of Done** has been satisfied.
*   A list of any documentation synchronization failures.
*   Traceability from review findings to the governing repository documents where applicable.

#### 6. Relationship to Repository Instructions
#### VERIFIED FACT
While repository instructions provide persistent grounding (the "Who" and "What"), this prompt provides **reusable tactical logic** (the "How") for the verification and audit phases.

#### 7. Relationship to the AI Development Workflow
#### VERIFIED FACT
This artifact is the operational implementation of **Step 7 (Verification)** and **Step 10 (Final Audit)** of the frozen development lifecycle.

#### 8. Position within the 11-step engineering lifecycle
#### VERIFIED FACT
The prompt is triggered at **Step 7** to validate incremental implementation and again at **Step 10** for the final repository audit before the commit is finalized.

#### 9. Required Prompt Inputs
#### VERIFIED FACT
Using official GitHub prompt file syntax, the prompt shall utilize:
*   `${input:objective}`: The milestone goal being implemented.
*   `${input:plan}`: The approved strategy from Step 5.
*   `${input:context}`: Reference to governing architecture or current repository state.
*   `${input:diff}`: The physical code changes to be reviewed.

#### 10. Expected Prompt Output
#### ENGINEERING RECOMMENDATION
The output should be formatted as a **Markdown Audit Report**.
*   **Rationale**: A structured report allows for easy visual inspection of "observable evidence" (e.g., test results, linter output) as required by the project's verification standards.

#### 11. Prompt Constraints
#### VERIFIED FACT
The generated review must NOT:
*   Propose new architectural patterns.
*   Bypass manual **Human Approval Gates**.
*   Ignore failing verification evidence (e.g., Ruff or pytest errors).
*   Rewrite repository standards independently.

#### 12. Human Approval Gates
#### VERIFIED FACT
The output of this prompt is **advisory**. The Human Developer retains final responsibility for technical decisions and must manually approve or reject the implementation before it is committed to main.

#### 13. Verification Requirements
#### VERIFIED FACT
The prompt must instruct the agent to utilize **observable results** (e.g., `ruff check .`, `ruff format .`, `pytest` output) rather than assertions of success.

#### 14. Definition of Done
#### VERIFIED FACT
A review task is complete when the adversarial report identifies whether the implementation satisfies all criteria in the repository's **Definition of Done** and is ready for mandatory Human Developer review.

#### 15. Repository Boundaries
#### VERIFIED FACT
The prompt must focus on verifying the **current implementation package** or milestone. It must not drift into planning future features or modifying unrelated subsystems.

#### 16. Prompt Lifecycle
#### VERIFIED FACT
This artifact is currently in the **Planned** stage of the **Repository Truth Policy**.

---

### 1. Evidence Classification

| Section | Label | Rationale |
| :--- | :--- | :--- |
| **1–8. Purpose through Position** | ## VERIFIED FACT | Derived from `AI_DEVELOPMENT_WORKFLOW.md`, `AI_COLLABORATION.md`, and `COPILOT_CONFIGURATION.md`. |
| **9. Required Prompt Inputs** | ## VERIFIED FACT | Utilizes the `${input:VAR}` syntax defined in official GitHub Prompt Files documentation. |
| **10. Expected Prompt Output** | ## ENGINEERING RECOMMENDATION | Markdown reporting is a practical engineering convention for "observable evidence". |
| **11–16. Constraints through Lifecycle** | ## VERIFIED FACT | Transcribed from frozen AI Behavior Boundaries and the **Repository Truth Policy**. |

---

### 2. Gap Analysis

| Section | Status | Product | Exact Documentation Topic |
| :--- | :--- | :--- | :--- |
| **9. Prompt Variables** | Partially Supported | GitHub | Prompt files (Public Preview) |

**Analysis**: The specification is fully supported by the frozen repository governance. The only remaining uncertainty is the exact character limit for the `${input:diff}` variable in the GitHub Copilot Public Preview.

---

### 3. Required Official Documentation

No additional official documentation is required. The **"Prompt Files"** syntax examples already present in the knowledge base provide sufficient evidence for frontmatter and variable placeholders.

---

### 4. Final Verdict

**READY FOR ENGINEERING REVIEW**
