# GitHub Copilot Configuration

> **Status:** Draft
>
> **Lifecycle:** Governance Document
>
> **Authority:** Repository Standard
>
> **Depends On:**
> - REPOSITORY_STANDARD.md
> - AI_WORKFLOW_SPECIFICATION.md
> - AI_DEVELOPMENT_WORKFLOW.md
>
> **Consumed By:**
> - .github/copilot-instructions.md
> - .github/prompts/
> - GitHub Copilot Agent
> - GitHub Copilot Chat
>
> **Last Updated:** YYYY-MM-DD

---

# 1. Purpose

## VERIFIED FACT

This document establishes the authoritative repository-specific configuration and operational standards for GitHub Copilot.

It defines how GitHub Copilot shall be configured, constrained, and used throughout the repository while remaining subordinate to repository governance and official documentation.

It acts as the governing bridge between the AI Development Workflow and the physical GitHub Copilot configuration.

---

# 2. Scope

## VERIFIED FACT

This document governs all GitHub Copilot functionality used within this repository, including:

- GitHub Copilot Chat
- GitHub Copilot Agent Mode
- GitHub Copilot Coding Agent
- Repository Instructions
- Prompt Library
- Workspace Context
- Inline Code Completions
- Semantic Workspace Features
- Official GitHub Copilot integrations approved for repository use

---

# 3. Outside Scope

## VERIFIED FACT

This document governs only GitHub Copilot configuration.

It does **not** govern:

- Repository architecture
- Coding standards
- Documentation governance
- AI workflow lifecycle
- Claude Code configuration
- NotebookLM research workflow
- VS Code workspace configuration
- Python environment configuration

These responsibilities remain governed by their respective authoritative repository documents.

---

# 4. Objectives

## ENGINEERING RECOMMENDATION

The objectives of this configuration are to:

- Provide consistent repository context to GitHub Copilot.
- Reduce hallucinations through authoritative grounding.
- Minimize unnecessary repository exploration.
- Improve implementation consistency.
- Ensure generated code follows repository standards.
- Reduce implementation drift across development sessions.
- Support deterministic AI-assisted software engineering.

---

# 5. Official GitHub Copilot Capability Inventory

## VERIFIED FACT

This repository recognizes the official GitHub Copilot capabilities supported by GitHub documentation.

Capabilities include:

- Repository Instructions
- Path-specific Instructions
- Prompt Files
- Agent Mode
- Chat Mode
- Workspace Context
- Semantic Search
- Inline Completions
- Commit Message Generation
- Pull Request Assistance
- Coding Agent
- Model Selection (where available)
- Workspace Indexing
- Official GitHub Extensions
- MCP integrations supported by GitHub

Only approved capabilities may become part of repository governance.

---

# 6. Capability Classification

## VERIFIED FACT

Capabilities are classified according to repository governance.

## 6.1 Required

These capabilities are mandatory.

- Repository Instructions
- Prompt Library
- Workspace Context
- Agent Mode
- Chat Mode
- Repository Grounding

---

## 6.2 Optional

These capabilities improve productivity but are not mandatory.

- Semantic Search
- Inline Suggestions
- Commit Message Generation
- Pull Request Review
- Smart Actions
- Vision Features (where available)

---

## 6.3 Future

These capabilities require future evaluation.

- External MCP integrations
- Experimental Agent workflows
- Organization-wide AI policies
- Multi-agent orchestration
- Fleet execution

---

## 6.4 Unsupported

## ENGINEERING RECOMMENDATION

The following remain outside repository approval until officially evaluated.

- Experimental preview features
- Unsupported extensions
- Community integrations lacking official documentation
- Repository automation without governance approval

---

# 7. Repository Responsibilities

## VERIFIED FACT

GitHub Copilot shall:

- Assist implementation.
- Generate code suggestions.
- Assist refactoring.
- Assist documentation.
- Assist testing.
- Provide semantic repository search.
- Execute approved Agent Mode tasks.

GitHub Copilot shall **not**:

- Define repository architecture.
- Modify repository standards.
- Replace official documentation.
- Override repository governance.
- Approve its own implementation.

---

# 8. Repository Context Sources

## VERIFIED FACT

GitHub Copilot shall consume repository context using the following precedence.

1. Official Documentation
2. Repository Truth Policy
3. REPOSITORY_STANDARD.md
4. AI_WORKFLOW_SPECIFICATION.md
5. AI_DEVELOPMENT_WORKFLOW.md
6. ARCHITECTURE.md
7. REQUIREMENTS.md
8. CODING_STANDARDS.md
9. PROJECT_STATUS.md
10. Current Workspace
11. Current User Prompt

When conflicts occur, higher-precedence documents govern.

---

# 9. Human Approval Gates

## VERIFIED FACT

The following require Human Developer approval.

- Agent Mode implementation
- Repository Instructions
- Permanent Prompt Library
- Repository Standards
- Workflow documents
- Frozen specifications
- Architecture changes
- Pull Requests
- Git commits

No autonomous AI may approve these artifacts.

---

# 10. Agent Mode Policy

## ENGINEERING RECOMMENDATION

Agent Mode shall be used only after:

- Objectives are defined.
- Planning is complete.
- Repository context is established.
- Human approval is granted.

Agent Mode should execute approved implementation plans rather than generate repository strategy.

---

# 11. Chat Mode Policy

## VERIFIED FACT

Chat Mode is intended for:

- Code explanation
- Troubleshooting
- Incremental implementation
- Repository questions
- Refactoring guidance

Long unrelated conversations should be avoided.

Context should be reset between unrelated engineering tasks.

---

# 12. Workspace Context Policy

## VERIFIED FACT

Repository context shall be grounded using:

- @workspace
- @file
- Repository Instructions
- Prompt Files
- Current implementation package
- Verbatim errors
- Build logs
- Ruff output
- pytest output

Summaries should not replace observable evidence.

---

# 13. Repository Instructions Policy

## VERIFIED FACT

The repository shall maintain:

.github/copilot-instructions.md

This document provides:

- Repository overview
- Build commands
- Coding expectations
- Architecture summary
- Development conventions
- Project terminology

Repository Instructions shall remain synchronized with repository governance.

---

# 14. Prompt Library Policy

## VERIFIED FACT

Reusable repository intelligence shall be maintained inside:

.github/prompts/

Prompt categories include:

- Permanent
- Reusable
- Task-specific
- Experimental

Permanent prompts require Human Developer approval before becoming repository assets.

---

# 15. Verification Requirements

## VERIFIED FACT

AI-generated work shall be verified using observable evidence.

Examples include:

- Ruff
- pytest
- Build output
- Static analysis
- Integration tests
- Repository review

AI confidence shall never replace engineering verification.

---

# 16. Configuration Change Policy

## VERIFIED FACT

This document shall only be modified when one or more of the following occurs.

- Official GitHub Copilot documentation changes.
- Repository governance changes.
- AI workflow changes.
- Human-approved engineering decisions.
- New repository AI standards are adopted.

Routine implementation work shall not modify this document.

---

# 17. Configuration Lifecycle

## VERIFIED FACT

Configuration follows the Repository Truth Policy.

Lifecycle:

Planned

↓

Approved

↓

Implemented

↓

Frozen

↓

Released

Configuration status shall always reflect repository truth.

---

# 18. Traceability

## VERIFIED FACT

Every configuration rule shall be traceable to at least one of the following.

- Official GitHub Documentation
- REPOSITORY_STANDARD.md
- AI_WORKFLOW_SPECIFICATION.md
- AI_DEVELOPMENT_WORKFLOW.md

Configuration rules shall never exist without a governing source.

---

# 19. Repository AI Contract

## VERIFIED FACT

GitHub Copilot is an engineering assistant.

It is not the repository authority.

Repository authority follows this order.

Human Developer

↓

Official Documentation

↓

Repository Standards

↓

Repository Governance

↓

Project Specifications

↓

AI Assistants

Every GitHub Copilot interaction shall remain subordinate to repository governance.

---

# 20. Status

**Current Status**

Draft

This document shall not become **Frozen** until:

- Engineering Review is complete.
- NotebookLM verification confirms consistency with repository governance.
- Official GitHub documentation supports all VERIFIED FACT classifications.
