# AI Development Workflow

The recommended engineering workflow is:

1. Research with NotebookLM.
2. Verify against official documentation.
3. Design and review architecture with ChatGPT.
4. Validate architectural decisions with NotebookLM.
5. Plan implementation with NotebookLM and ChatGPT.
6. Implement with Claude Code.
7. Verify the implementation.
8. Update project documentation.
9. Update project status.
10. Commit and push.

Each tool contributes a different capability.

---

# AI Tool Responsibilities

The project uses specialized AI tools throughout the development lifecycle.

| Activity                          | Primary Tool  | Responsibility                                                                                             |
| --------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------- |
| Documentation Research            | NotebookLM    | Research official documentation, verify engineering decisions, and validate documentation consistency.     |
| Architecture & Engineering Design | ChatGPT       | Design system architecture, evaluate engineering trade-offs, and assist with long-term technical planning. |
| Implementation                    | Claude Code   | Implement source code, refactor modules, and follow the repository's coding standards.                     |
| Production Runtime AI             | Google Gemini | Primary AI provider for Job Intelligence and AI Assistance features.                                       |
| Production Runtime Fallback       | Groq          | Fallback AI provider for resilient inference when the primary provider is unavailable.                     |

Each tool should be used for the responsibilities where it provides the greatest value.

This separation improves research quality, architectural consistency, implementation accuracy, and production flexibility.

---

# Task Completion Workflow

Every implementation task must follow this workflow to keep the repository, documentation, Git history, and NotebookLM synchronized.

```text
Research
        │
        ▼
Design
        │
        ▼
Implement
        │
        ▼
Verify implementation
        │
        ▼
Determine commit message
        │
        ▼
Update documentation (if required)
        │
        ▼
Update PROJECT_STATUS.md
    • Current Phase
    • Completed Milestones
    • Last Completed Milestone
    • Last Commit
        │
        ▼
git add .
        │
        ▼
git commit -m "<same commit message>"
        │
        ▼
git push
```

## Workflow Rules

- Never implement without first validating the design against official documentation.
- Never commit unverified code.
- Always verify the implementation before updating project documentation or `PROJECT_STATUS.md`.
- Determine the commit message before updating `PROJECT_STATUS.md`.
- The **Last Commit** entry must exactly match the Git commit message.
- Commit the implementation, documentation updates, and `PROJECT_STATUS.md` together whenever they belong to the same task.
- Push only after the commit has been created successfully.

## Purpose

This workflow ensures:

- Engineering decisions are grounded in official documentation.
- The repository always reflects the current implementation state.
- Documentation, `PROJECT_STATUS.md`, and Git history remain synchronized.
- NotebookLM always has an accurate project snapshot.
- Every completed task is documented before it is committed.
- The development process remains simple, repeatable, evidence-based, and maintainable.
