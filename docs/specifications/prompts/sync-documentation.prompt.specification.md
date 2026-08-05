### Version 1 Artifact Specification: `sync-documentation.prompt.specification.md`

#### 1. Purpose
#### VERIFIED FACT
This prompt standardizes **Step 8 (Documentation Synchronization)** of the project's 11-step engineering lifecycle. It ensures that the repository's documentation (including `docs/` and `README.md`) accurately reflects the physical implementation state, maintaining the **Repository Truth Policy** and the principle that **"Documentation governs implementation"**.

#### 2. Scope
#### VERIFIED FACT
This specification governs the physical prompt file located at `.github/prompts/sync-documentation.prompt.md` and its corresponding engineering specification in `docs/specifications/prompts/`. It applies to identifying and applying required documentation updates following successful implementation and verification (Steps 6 and 7).

#### 3. Dependencies
#### VERIFIED FACT
*   **`docs/AI_DEVELOPMENT_WORKFLOW.md`**: Provides the engineering lifecycle stage (Step 8) this prompt implements.
*   **`docs/REPOSITORY_STANDARD.md`**: Defines the "Repository Truth Policy" and document taxonomy.
*   **`docs/COPILOT_CONFIGURATION.md`**: Establishes the tool's responsibility to "Assist documentation".
*   **`docs/PROMPT_LIBRARY.md`**: Defines the design principles (Single Responsibility) and standard structure for prompt files.
*   **`.github/copilot-instructions.md`**: Provides the persistent grounding context and AI behavior boundaries.

#### 4. Inputs
#### VERIFIED FACT
The prompt requires the following data to ensure high-fidelity synchronization:
*   **Implementation Objective**: The specific goal of the active milestone.
*   **Approved Implementation Plan**: The Step 5 strategy that governed the changes.
*   **Implementation Diffs**: The physical code and verification changes produced in Steps 6 and 7.
*   **Current Repository State**: To ensure updates are grounded in implemented reality rather than theoretical designs.
*   **Governing Repository Documents**: Reference to existing documentation that must be maintained (e.g., `ARCHITECTURE.md`, `CODING_STANDARDS.md`).

#### 5. Outputs
#### VERIFIED FACT
The prompt must produce a structured Documentation Sync report including:
*   A list of every **affected document** (e.g., `README.md`, files in `docs/`).
*   The **technical rationale** for why each document requires updating based on the implementation.
*   **Traceability** showing the implementation change or governing repository document that justifies each proposed update.
*   The **updated Markdown content** for each document.
*   Verification that the proposed updates maintain **cross-document consistency**.

#### 6. Relationship to Repository Instructions
#### VERIFIED FACT
While repository instructions provide persistent grounding (the "Who" and "What"), this prompt provides **reusable tactical logic** (the "How") for the synchronization phase.

#### 7. Relationship to AI Development Workflow
#### VERIFIED FACT
This artifact is the operational implementation of **Step 8 (Documentation Synchronization)** of the frozen development lifecycle.

#### 8. Position within the 11-step engineering lifecycle
#### VERIFIED FACT
The prompt is triggered at **Step 8**, occurring after **Step 7 (Verification)** is complete and before **Step 9 (Project Status Update)**.

#### 9. Required Prompt Inputs
#### VERIFIED FACT
Using official GitHub prompt file syntax, the prompt shall utilize:
*   `${input:objective}`: The milestone goal being implemented.
*   `${input:plan}`: The approved strategy from Step 5.
*   `${input:diff}`: The physical code changes requiring documentation updates.
*   `${input:context}`: Reference to governing architecture or the current repository state.

#### 10. Expected Prompt Output
#### ENGINEERING RECOMMENDATION
The output should be formatted as a **Markdown Documentation Audit Report**, followed by the proposed document updates.
*   **Rationale**: A structured report allows the Human Developer to verify the "reasoning" behind documentation changes before accepting the updated content.

#### 11. Prompt Constraints
#### VERIFIED FACT
The prompt must NOT:
*   Propose new architectural patterns or redesigns.
*   Create unrelated or speculative documentation.
*   Modify frozen governance documents unless they are explicitly part of the implementation objective.
*   Bypass manual **Human Approval Gates**.
*   Base updates on assumptions rather than **observable implementation changes**.

#### 12. Human Approval Gates
#### VERIFIED FACT
The output of this prompt is **advisory**. The Human Developer must manually review and approve the proposed documentation updates before they are committed to the repository.

#### 13. Verification Requirements
#### VERIFIED FACT
The prompt must instruct the agent to utilize **observable results** (the provided diffs and current repository state) and ensure that every proposed update is traceable back to a physical implementation change or the governing repository documentation.

#### 14. Definition of Done
#### VERIFIED FACT
A synchronization task is complete when all documentation affected by the implementation is identified, updates reflect implemented truth, cross-document consistency is preserved, and the implementation is ready for mandatory Human Developer review.

#### 15. Repository Boundaries
#### VERIFIED FACT
The prompt must focus exclusively on the **current implementation package** or milestone. It must not attempt to document future features or unrelated subsystems.

#### 16. Prompt Lifecycle
#### VERIFIED FACT
This artifact is currently in the **Planned** stage of the **Repository Truth Policy**.

---

### 1. Evidence Classification

| Section | Label | Rationale |
| :--- | :--- | :--- |
| **1–9. Purpose through Inputs** | ## VERIFIED FACT | Derived from `AI_DEVELOPMENT_WORKFLOW.md`, `REPOSITORY_STANDARD.md`, and established implementation patterns. |
| **10. Expected Prompt Output** | ## ENGINEERING RECOMMENDATION | Structured reporting is an established repository engineering convention for reviewability. |
| **11–16. Constraints through Lifecycle** | ## VERIFIED FACT | Transcribed from frozen AI Behavior Boundaries and the **Repository Truth Policy**. |

---

### 2. Gap Analysis

| Section | Status | Product | Exact Documentation Topic |
| :--- | :--- | :--- | :--- |
| **9. Prompt Variables** | Partially Supported | GitHub | Prompt files (Public Preview) |

**Analysis**: The specification is fully supported by the frozen repository governance. The only remaining uncertainty is the exact behavior of variable expansions for multiple-file contexts in the GitHub Copilot Public Preview.

---

### 3. Required Official Documentation
No additional official documentation is required. The **"Prompt Files"** syntax examples in the knowledge base provide sufficient evidence for frontmatter and variable usage [691–693, 757].

---

### 4. Final Verdict
**READY FOR ENGINEERING REVIEW**
