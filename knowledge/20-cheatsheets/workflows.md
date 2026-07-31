# Terminal Workflows

> A collection of common terminal workflows used throughout the AI Career Agent project.
>
> **Rule:** Each workflow should represent a complete task, not just a single command.

---

# Save and Push Your Work

## Goal

Save your completed work and upload it to GitHub.

### Step 1 – Review changes

```bash
git status
```

Checks what has changed.

---

### Step 2 – Stage changes

```bash
git add .
```

Prepares all changes for the next commit.

---

### Step 3 – Create a commit

```bash
git commit -m "Describe your changes"
```

Creates a snapshot of your work.

---

### Step 4 – Upload to GitHub

```bash
git push
```

Pushes your commit to the remote repository.

---

# Check Your Repository

## Goal

See the current state of your project.

```bash
git status
```

Use this whenever you're unsure what's happening in your repository.

---

# Create a New Repository

## Goal

Initialize a new project and publish it to GitHub.

### Step 1 – Initialize Git

```bash
git init
```

Creates a new Git repository in the current project.

### Step 2 – Check the Repository

```bash
git status
```

Verifies that Git has been initialized correctly.

### Step 3 – Stage Your Files

```bash
git add .
```

Stages all project files so they can be included in the first commit.

### Step 4 – Create the First Commit

```bash
git commit -m "Initial project structure"
```

Creates the first snapshot of your project history.

### Step 5 – Connect the Remote Repository

```bash
git remote add origin <repository-url>
```

Connects your local Git repository to the remote GitHub repository.

### Step 6 – Push to GitHub

```bash
git push -u origin main
```

Uploads the initial commit to GitHub and sets the `main` branch to track the remote branch.
