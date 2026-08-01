---
name: update-status
description: Update the project status documentation after implementation work is completed.
when_to_use: When the developer asks to update PROJECT_STATUS.md or determine the current implementation progress.
disable-model-invocation: true
---

# Update Project Status

## Purpose

Maintain an accurate record of project progress by synchronizing `docs/PROJECT_STATUS.md` with the current repository state.

## Workflow

1. Review the current implementation and recent repository changes.
2. Read `docs/PROJECT_STATUS.md`.
3. Read `docs/ROADMAP.md` to determine the planned milestones.
4. Compare completed work against the roadmap.
5. Move completed tasks into the **Completed** section.
6. Update the **Current Task** section.
7. Identify the next logical milestone.
8. Ensure the status reflects the repository rather than assumptions.

## Verification

Before completing:

- Verify the status matches the repository.
- Verify completed milestones are not duplicated.
- Verify consistency between `PROJECT_STATUS.md` and `ROADMAP.md`.
- Do not modify unrelated documentation.
- If repository information is insufficient, ask for clarification instead of guessing.
