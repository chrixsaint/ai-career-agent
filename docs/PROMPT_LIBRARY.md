# Prompt Library

> **Status:** Draft
>
> **Lifecycle:** Repository Governance
>
> **Authority:** AI_DEVELOPMENT_WORKFLOW.md
>
> **Depends On:**
>
> - REPOSITORY_STANDARD.md
> - AI_DEVELOPMENT_WORKFLOW.md
> - COPILOT_CONFIGURATION.md
> - .github/copilot-instructions.md
>
> **Last Updated:** 2026-08-05

---

### 1. Version 1 Prompt Library Specification

## 1. Purpose

## VERIFIED FACT

The Prompt Library maintains **reusable repository intelligence** and engineering workflows for recurring development activities. It serves as the physical implementation of the "Prompt Governance" policy defined in the frozen **`AI_DEVELOPMENT_WORKFLOW.md`** [30, Turn 32].

Its purpose is to standardize recurring engineering workflows so GitHub Copilot produces consistent, repository-compliant outputs across implementation packages.

---

## 2. Scope

## VERIFIED FACT

This specification governs all **.prompt.md** files located in the **.github/prompts/** directory and the corresponding prompt engineering specifications located in **docs/specifications/prompts/**.
```

It does not govern:

- Task-specific conversational prompts.
- NotebookLM prompts.
- ChatGPT prompts.
- Claude interactive prompts.

---

## 3. Dependencies

## VERIFIED FACT

- **`docs/AI_DEVELOPMENT_WORKFLOW.md`**: Provides the foundational policy for prompt lifecycle, categories, and governance [30, Turn 32].
- **`docs/COPILOT_CONFIGURATION.md`**: Acts as the authority for capability classification and human approval gates.
- **`.github/copilot-instructions.md`**: Provides permanent repository grounding which prompts supplement with tactical implementation logic.

---

## 4. Lifecycle

## VERIFIED FACT

Prompt files follow the **Repository Truth Policy** lifecycle:

**Planned → Approved → Implemented → Frozen → Released** [638, Turn 32].

---

## 5. Relationships

## VERIFIED FACT

- **`copilot-instructions.md`** provides permanent repository context (mission, architecture, technology stack, engineering rules).
- **Prompt Library** provides reusable implementation logic.
- **Task-specific prompts** provide disposable context for a single implementation package.

---

## 6. Repository Governance

## VERIFIED FACT

Prompts are treated as **versioned repository logic** [Turn 32].

They remain strictly subordinate to:

1. Official documentation
2. Repository standards
3. Frozen repository governance

No prompt may override frozen governance.

---

## 7. Prompt Categories

## VERIFIED FACT

Per **`AI_DEVELOPMENT_WORKFLOW.md`** Section 11.1:

- Permanent
- Reusable
- Task-specific
- Experimental

[30, Turn 32]

---

## 8. Prompt Design Principles

## VERIFIED FACT

Every permanent prompt must:

- perform one engineering responsibility;
- remain reusable across implementation packages;
- reference repository governance rather than duplicate it;
- produce deterministic outputs where possible;
- avoid feature-specific implementation context;
- defer unsupported decisions to official documentation.

---

## 9. Prompt Structure

## VERIFIED FACT

Permanent prompts should contain:

- Objective
- Repository Context
- Inputs
- Expected Outputs
- Verification Requirements
- Constraints
- References to repository governance where applicable

---

## 10. Required Version 1 Prompts

## ENGINEERING RECOMMENDATION

| Prompt                          | Primary Responsibility        |
| ------------------------------- | ----------------------------- |
| `implementation-plan.prompt.md` | Implementation planning       |
| `review-code.prompt.md`         | Code review                   |
| `generate-tests.prompt.md`      | Test generation               |
| `sync-docs.prompt.md`           | Documentation synchronization |
| `architecture-audit.prompt.md`  | Architecture verification     |

---

## 11. Recommended Implementation Order

## ENGINEERING RECOMMENDATION

1. implementation-plan
2. review-code
3. generate-tests
4. architecture-audit
5. sync-docs
6. task-specific prompts

---

## 12. Prompt Ownership

## VERIFIED FACT

- Permanent and Reusable prompts are owned by the Human Developer.
- Task-specific prompts are owned by the active AI session.

[Turn 31, Turn 32]

---

## 13. Prompt Review Requirements

## VERIFIED FACT

Any Permanent or Reusable prompt requires manual human review before being committed.

[212, Turn 31, Turn 32]

---

## 14. Prompt Versioning

## VERIFIED FACT

Prompt files are versioned alongside the repository code they support.

[Turn 31, Turn 32]

---

## 15. Prompt Retirement Policy

## VERIFIED FACT

- Task-specific prompts are removed after their implementation package is completed.
- Experimental prompts are retired if they fail to improve engineering outcomes after two evaluation sessions.

[Turn 31, Turn 32]

---

## 16. Repository Directory Structure

## VERIFIED FACT

All permanent prompt files reside in **.github/prompts/** to allow GitHub Copilot to discover them automatically. Their governing engineering specifications reside in **docs/specifications/prompts/**.


## 17. Permanent Prompts
## VERIFIED FACT

Permanent prompts encapsulate durable repository engineering logic that is expected to remain valid across multiple implementation packages.

Examples include implementation planning, code review, documentation synchronization, testing, and architecture verification.

---

## 18. Task-specific Prompts
## VERIFIED FACT

Task-specific prompts provide disposable guidance for a single implementation package and should not become permanent repository assets.

---

## 19. Repository Boundaries
## VERIFIED FACT

Prompt files must not:

* redesign repository architecture;
* modify frozen governance independently;
* introduce new architectural patterns;
* change dependency management;
* bypass Human Approval Gates;
* duplicate permanent repository instructions;
* replace `.github/copilot-instructions.md`;
* contain implementation-specific repository state intended only for one feature.

---

## 20. Definition of Completion
## VERIFIED FACT

A permanent prompt is considered complete only when:

1. Governance review has passed.
2. NotebookLM evidence audit has passed.
3. Human approval has been granted.
4. The prompt has been committed.
5. Repository status has been synchronized.
6. The prompt lifecycle reaches the Frozen state.

---

### 2. Evidence Classification

| Section | Label | Rationale |
| :--- | :--- | :--- |
| 1–7 | VERIFIED FACT | Derived from frozen repository governance. |
| 8–9 | VERIFIED FACT | Repository governance rules for permanent prompt quality and structure. |
| 10–11 | ENGINEERING RECOMMENDATION | Recommended Version 1 implementation order following the repository workflow. |
| 12–20 | VERIFIED FACT | Direct implementation of AI Development Workflow and Repository Truth Policy. |

---

### 3. Gap Analysis

| Section | Classification | Product | Exact Documentation Topic |
| :--- | :--- | :--- | :--- |
| Prompt File Syntax | Partially Supported | GitHub | Prompt files (Public Preview) |

**Analysis**

The implementation plan is fully supported by the frozen repository governance.

The only remaining limitation concerns GitHub Prompt Files remaining in Public Preview.

---

### 4. Required Official Documentation

No additional official documentation is required.

The Prompt Files documentation already present in the knowledge base provides the required syntax, frontmatter, and input variable support needed for Version 1.

---

### 5. Final Verdict

**READY FOR ENGINEERING REVIEW**

---

## Open Questions

1. Should the repository standardize a common frontmatter template for all permanent prompt files, or allow each prompt to define only the metadata it requires?
2. Should future subsystem-specific prompts (for example, database, API, or security reviews) be governed within this document or introduced incrementally as new implementation packages become active under the Repository Truth Policy?
``
