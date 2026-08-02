# AI Development Workflow

The recommended engineering workflow is:

1. Research with NotebookLM.
2. Verify against official documentation.
3. Design with ChatGPT.
4. Plan implementation with NotebookLM and ChatGPT.
5. Implement with GitHub Copilot.
6. Verify the implementation.
7. Update project status.
8. Commit and push.

Each tool contributes a different capability.

---

# Task Completion Workflow

Every implementation task must follow this workflow to keep the repository, documentation, Git history, and NotebookLM synchronized.

```text
Implement task
        │
        ▼
Verify task works
        │
        ▼
Determine commit message
        │
        ▼
Update PROJECT_STATUS.md
    • Current Task
    • Completed Milestones (add one line if applicable)
    • Last Completed Task
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

- Never commit unverified code.
- Always verify the implementation before updating `PROJECT_STATUS.md`.
- Determine the commit message before updating `PROJECT_STATUS.md`.
- The **Last Commit** entry must exactly match the Git commit message.
- Commit the implementation and the updated `PROJECT_STATUS.md` together.
- Push only after the commit has been created successfully.

## Purpose

This workflow ensures:

- The repository always reflects the current implementation state.
- `PROJECT_STATUS.md` and Git history remain synchronized.
- NotebookLM always has an accurate project snapshot.
- Every completed task is documented before it is committed.
- The development process remains simple, repeatable, and evidence-based.
