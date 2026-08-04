# AI Workflow Specification

**Version:** Draft 0.1
**Status:** Specification (Not Final)
**Purpose:** Define the requirements for the permanent AI-assisted software engineering workflow used throughout the AI Career Agent project.

---

# 1. Objective

The objective of this document is to define the specification for a permanent AI-assisted software engineering workflow.

The workflow will govern how the following tools are used throughout the entire software development lifecycle:

- NotebookLM
- ChatGPT
- GitHub Copilot Chat
- GitHub Copilot Agent
- VS Code AI features
- Human Developer

This document is **not** the workflow itself.

Instead, it defines the engineering requirements that the final workflow must satisfy.

The final workflow will only be created after this specification has been independently audited against the uploaded repository documentation and official product documentation.

---

# 2. Background

The repository now contains:

- Architecture documentation
- Coding standards
- Package structure
- Database architecture
- Job Collection architecture
- AI collaboration standards
- AI development playbook
- Research backlog
- Official GitHub Copilot documentation
- Official VS Code AI documentation

These documents collectively define the engineering standards of the project.

A permanent AI-assisted workflow must now be established before further implementation continues.

---

# 3. Scope

The workflow shall define:

- Engineering responsibilities
- Tool responsibilities
- Development lifecycle
- Documentation lifecycle
- Implementation lifecycle
- Verification lifecycle
- Review lifecycle
- Commit lifecycle
- AI collaboration rules
- Repository governance

The workflow must remain applicable throughout the entire project lifecycle.

---

# 4. Goals

The workflow should:

- Minimize architectural drift.
- Minimize duplicated work.
- Minimize AI hallucinations.
- Minimize inconsistent coding practices.
- Maintain repository consistency.
- Encourage evidence-based engineering.
- Preserve frozen architectural decisions.
- Scale from small fixes to large multi-file implementations.
- Support long-term maintainability.

---

# 5. Constraints

The workflow must:

- Be based on uploaded documentation.
- Prefer official documentation over assumptions.
- Clearly distinguish verified practices from engineering recommendations.
- Remain technology-independent where possible.
- Support incremental implementation.
- Keep documentation synchronized with implementation.

---

# 6. Questions the Workflow Must Answer

The permanent workflow must define:

## 6.1 Tool Responsibilities

For each AI tool:

- What is its primary responsibility?
- What is outside its responsibility?
- What decisions require human approval?

---

## 6.2 Development Lifecycle

The workflow must follow the engineering lifecycle below:

1. Research (NotebookLM)
2. Verification of Official Documentation
3. Architecture Design & Engineering Review
4. Architecture Validation
5. Implementation Planning
6. Incremental Implementation
7. Verification (Tests, Builds, Ruff)
8. Documentation Synchronization
9. Project Status Update
10. Final Audit
11. Commit & Push

---

## 6.3 Copilot Usage

## 6.3 Copilot Usage

The workflow must define how GitHub Copilot uses:

- Repository Instructions
- Prompt Files
- Workspace Context
- Agent Mode
- Chat Mode
- Extensions
- Semantic Search
- Inline Completions

The workflow must determine:

- Required configuration
- Optional configuration
- Future configuration

Every capability must be supported by official documentation before adoption.
---

## 6.4 Documentation Governance

The workflow must define:

Which documents are:

- Authoritative
- Frozen
- Versioned
- Temporary
- Historical

The workflow must also define when documentation should be updated.

## 6.4.1 Prompt Governance

The workflow must define the lifecycle of prompt files.

Prompt files shall be classified as:

- Permanent project prompts
- Reusable engineering prompts
- Task-specific prompts
- Experimental prompts

The workflow must define:

- ownership
- review requirements
- versioning
- retirement policy

---

## 6.5 Implementation Units

The workflow must determine whether implementation should occur:

- File by file
- Feature by feature
- Batch by batch
- Milestone by milestone

The workflow must justify the chosen implementation strategy.

---

## 6.6 Verification

The workflow must define:

- Ruff verification
- Test execution
- Documentation verification
- NotebookLM audits
- Human review
- Acceptance criteria

---

## 6.7 Research Backlog

The workflow must explain:

When implementation should stop because additional research is required.

When research should be deferred to the Research Backlog.

---

# 7. Expected Deliverables

Once this specification has been audited and approved, it should produce the following permanent repository artifacts:

- docs/AI_DEVELOPMENT_WORKFLOW.md
- docs/COPILOT_CONFIGURATION.md
- .github/copilot-instructions.md
- .github/prompts/
- Any additional documentation justified by official evidence.

---

# 8. Out of Scope

This specification does not define:

- Project architecture
- FastAPI implementation
- Database implementation
- Business logic
- UI implementation

These are governed by their respective subsystem documents.

---

# 9. Success Criteria

The specification shall be considered complete only when:

- Every workflow stage has been defined.
- Every AI tool has clearly assigned responsibilities.
- Every recommendation is classified as either:
  - Verified
  - Engineering Recommendation
  - Remaining Unknown
- Unsupported assumptions have been eliminated.
- Missing documentation has been identified.
- NotebookLM concludes that no further evidence-based improvements are required.

Only after these criteria are satisfied may the permanent workflow documents be created.
