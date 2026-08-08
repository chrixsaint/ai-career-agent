Yes. We're done planning. From now on, we execute.

Here is the fastest path. Don't think ahead. Just complete one step and come back saying **"Proceed."**

---

# STEP 1 — Create a new NotebookLM

Create a brand new NotebookLM.

**Name**

> **GitHub Copilot Bootcamp**

Nothing else.

---

# STEP 2 — Upload ONLY the official GitHub documentation

Do **not** upload repository documents yet.

Upload only the GitHub Copilot official documentation that teaches:

* Installation
* VS Code integration
* Copilot Chat
* Ask Mode
* Edit Mode
* Agent Mode
* Prompt Files
* Repository Instructions
* Workspace Context
* Repository Indexing
* Terminal integration
* Model selection
* Permissions
* Best practices

This notebook should first understand **GitHub Copilot itself**, not your repository.

---

# STEP 3 — Upload ONLY the minimum repository documents

After the official docs are uploaded, upload only these repository files:

```
docs/COPILOT_CONFIGURATION.md

.github/copilot-instructions.md

docs/PROMPT_LIBRARY.md

docs/AI_DEVELOPMENT_WORKFLOW.md

.github/prompts/
    implementation-plan.prompt.md
    refactor-module.prompt.md
    generate-tests.prompt.md
    review-code.prompt.md
    sync-documentation.prompt.md
    generate-commit.prompt.md
```

Nothing else.

Do **not** upload architecture, requirements, database, roadmap, etc.

---

# STEP 4 — Give NotebookLM ONE instruction

Paste exactly this:

> You are my GitHub Copilot instructor. Your only objective is to teach me GitHub Copilot from beginner to advanced using the uploaded official documentation and repository documents. Teach one capability at a time. Never skip ahead. Every lesson must include: explanation, why it exists, VS Code walkthrough, screenshots to upload, practical exercises, observable validation, troubleshooting, review questions, and mastery verification. Do not proceed to the next lesson until I demonstrate understanding.

---

# STEP 5 — Start Lesson 1

Ask only:

> Begin Lesson 1.

Nothing more.

---

# STEP 6 — Follow the bootcamp

For every lesson:

1. Read.
2. Configure VS Code.
3. Upload screenshots.
4. Do the exercise.
5. Pass the validation.
6. Move to the next lesson.

Never skip a lesson.

---

# STEP 7 — Come back here

When Lesson 1 is finished, come back to me.

Just say:

> **Proceed**

I will help you interpret anything that is confusing, but I will **not** redesign the learning path.

---

## That's it.

No more planning.

No more governance.

No more documents.

Your job now is simply:

**Create Notebook → Upload docs → Paste instructor prompt → Begin Lesson 1.**

When you've done that, come back and say:

> **Proceed**
