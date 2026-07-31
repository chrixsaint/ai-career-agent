---
category: git
last_verified: 2026-07-31
---

# Git Command Reference

> A collection of Git commands used throughout the AI Career Agent project.

**Rule:** Only add commands that have been used, tested, and understood.

---

## Git Status

```yaml
command: git status
category: git
difficulty: beginner
last_verified: 2026-07-31

aliases:
  - check repository status
  - check changes
  - repository status
  - see modified files

related_workflows:
  - Check Your Repository
  - Save and Push Your Work

related_commands:
  - git add .
  - git diff

tags:
  - git
  - status
  - repository
```

### Intent

See the current state of your repository.

### Command

```bash
git status
```

### When to Use

- Before staging changes.
- Before committing.
- Before pushing.
- Whenever you're unsure of the repository state.

### Example

```bash
git status
```

### Expected Output

Displays:

- Current branch
- Modified files
- Staged files
- Untracked files

### Explanation

Shows the current status of your working directory and staging area. This command never modifies your files.

### Notes

One of the safest and most frequently used Git commands.

---

## Git Add

```yaml
command: git add .
category: git
difficulty: beginner
last_verified: 2026-07-31

aliases:
  - stage files
  - stage changes
  - add all files

related_workflows:
  - Save and Push Your Work
  - Create a New Repository

related_commands:
  - git status
  - git commit

tags:
  - git
  - staging
```

### Intent

Stage all current project changes.

### Command

```bash
git add .
```

### When to Use

After reviewing your changes and before committing.

### Example

```bash
git add .
```

### Expected Output

Usually no output if successful.

### Explanation

Moves all modified, new, and deleted files into Git's staging area.

### Notes

Run `git status` afterward to verify the staged files.

---

## Git Commit

```yaml
command: git commit -m "message"
category: git
difficulty: beginner
last_verified: 2026-07-31

aliases:
  - save changes
  - create commit
  - snapshot project

related_workflows:
  - Save and Push Your Work
  - Create a New Repository

related_commands:
  - git add .
  - git push

tags:
  - git
  - commit
```

### Intent

Create a snapshot of the staged changes.

### Command

```bash
git commit -m "Your message"
```

### When to Use

After staging your changes.

### Example

```bash
git commit -m "Add backend project structure"
```

### Expected Output

Git reports the new commit hash and a summary of changed files.

### Explanation

Creates a permanent checkpoint in the repository history.

### Notes

Write commit messages that describe **what changed**.

---

## Git Push

```yaml
command: git push
category: git
difficulty: beginner
last_verified: 2026-07-31

aliases:
  - upload code
  - upload commits
  - push to github
  - sync repository

related_workflows:
  - Save and Push Your Work
  - Create a New Repository

related_commands:
  - git commit
  - git pull

tags:
  - git
  - github
  - remote
```

### Intent

Upload local commits to the remote repository.

### Command

```bash
git push
```

### When to Use

After committing changes.

### Example

```bash
git push
```

### Expected Output

Git reports the objects uploaded and confirms the remote branch update.

### Explanation

Uploads your local commits to GitHub (or another remote repository).

### Notes

The first push for a new branch may require:

```bash
git push -u origin <branch-name>
```
