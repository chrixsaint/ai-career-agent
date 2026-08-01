---
name: next-milestone
description: Analyze the project roadmap and current status to determine the next smallest actionable implementation task.
when_to_use: When the developer asks what to build next or requests the next implementation milestone.
disable-model-invocation: true
allowed-tools:
  - Bash(cat *)
---

# Next Milestone

## Purpose

Determine the next implementation task by comparing the current project status with the planned roadmap.

## Workflow

1. Read `docs/PROJECT_STATUS.md` to understand the current implementation progress.
2. Read `docs/ROADMAP.md` to identify the planned milestones.
3. Compare the current status against the roadmap.
4. Identify the next logical milestone that has not yet been completed.
5. Recommend the smallest practical implementation task required to advance the project.
6. Define clear completion criteria.
7. Recommend an appropriate Git commit message following the project convention.

## Verification

Before completing:

- Verify that no prerequisite milestone is skipped.
- Ensure the recommended task is small enough to complete in a single development session.
- Ensure the recommendation follows KISS and YAGNI principles.
- If repository information is insufficient, ask for clarification instead of making assumptions.
