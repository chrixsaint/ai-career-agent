This engineering audit of **`.github/copilot-instructions.md`** was performed against the frozen repository documentation and official GitHub Copilot standards.

### 1. Engineering Verification Matrix

| Requirement | Status | Audit Result |
| :--- | :--- | :--- |
| **Repository Purpose** | **FULLY IMPLEMENTED** | Covered in Section 1 (Overview). |
| **Repository Mission** | **PARTIALLY IMPLEMENTED** | Defined in Overview but lacks the specific phrasing from `PROJECT_VISION.md`. |
| **Repository Structure** | **FULLY IMPLEMENTED** | Section 2 maps the 6-layer architecture and specific tool directories (`.github`, `.claude`) [Turn 33]. |
| **Technology Stack** | **FULLY IMPLEMENTED** | Section 3 lists core technologies and environment management (`uv`) [Turn 33]. |
| **Development Workflow** | **FULLY IMPLEMENTED** | Section 4 references the 11-step sequence and subordinate assistant role [Turn 33]. |
| **Implementation Philosophy** | **FULLY IMPLEMENTED** | Section 5 enforces "Foundation First" and "Modular processing pipeline" [Turn 33]. |
| **Build/Verify Commands** | **FULLY IMPLEMENTED** | Section 6 provides specific `uv`, `ruff`, and `pytest` commands [Turn 33]. |
| **Preferred Modification Strategy** | **PARTIALLY IMPLEMENTED** | "Foundation First" is present, but the "Reuse before introduction" rule is missing. |
| **AI Behaviour Boundaries** | **FULLY IMPLEMENTED** | Section 8 defines boundaries for strategy, standards, and approvals [Turn 33]. |
| **Context Priority** | **FULLY IMPLEMENTED** | Section 7 defines the 5-step precedence order [Turn 33]. |
| **Definition of Done** | **MISSING** | No explicit section defining the criteria for task completion. |

---

### 2. Evidence Classification for Suggested Improvements

| Improvement | Classification | Rationale |
| :--- | :--- | :--- |
| **Mission Refinement** | **VERIFIED FACT** | Directly supported by the "Mission" section of `PROJECT_VISION.md`. |
| **Modification Strategy** | **VERIFIED FACT** | The "Reuse existing implementations before introducing new ones" rule is mandated by `AI_ENGINEERING_GUIDE.md`. |
| **Definition of Done** | **VERIFIED FACT** | Explicit criteria are defined in `AI_DEVELOPMENT_WORKFLOW.md` Section 4.2 [Turn 30]. |

---

### 3. Gap Analysis

*   **Repository Mission**: The instructions currently provide a general summary. To satisfy the requirement for an "authoritative grounding document," the explicit mission to "continuously discover relevant job opportunities and help prepare high-quality, user-controlled applications" should be included.
*   **Modification Strategy**: The agent must be explicitly instructed to "Reuse before introducing," as this is a core NFR for maintainability (**NFR-002**).
*   **Definition of Done**: Per the official "onboarding" goals, the instructions must "Reduce the likelihood of a cloud agent pull request getting rejected". Adding the 4-point Definition of Done from the workflow ensures the agent validates its own output against project requirements before submission [Turn 30].

---

### 4. Required Corrections

**Add to Section 1 (Repository Overview):**
```markdown
*   **Mission**: Build a personal AI career assistant that continuously discovers relevant job opportunities and helps prepare high-quality, user-controlled applications.
```

**Add to Section 5 (Coding & Architecture Expectations):**
```markdown
*   **Modification Strategy**: Reuse existing implementations and utility modules before introducing new ones. Follow the established patterns found in the codebase.
```

**Add New Section 9:**
```markdown
## 9. Definition of Done
## VERIFIED FACT
A task is considered **Done** only when:
1. All functional requirements (REQUIREMENTS.md) are satisfied.
2. The implementation follows the ARCHITECTURE.md.
3. Static analysis (Ruff) and automated tests pass with 0 errors.
4. Documentation remains synchronized across all layers [Turn 30].
```

---

### **Final Verdict**

**REQUIRES IMPLEMENTATION REVISION**
