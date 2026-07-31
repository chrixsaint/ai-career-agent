---
title: AI Engineering Accelerator
source: knowledge/inbox/Ai_Engineering_acelerator.md
date: 2026-07-31
tags: [ai-engineering, tooling, workflows, vs-code]
owner: @chrixsaint
confidence: medium
summary: Curated operating system for building an AI-powered backend: recommended tools, Claude practices, VS Code setup, MCP guidance, and NotebookLM procedures.
---

Below is your **AI Engineering Operating System** for building a serious AI‑powered backend in 2 weeks with Claude, VS Code, Ubuntu/WSL, FastAPI, Playwright, Git/GitHub, and NotebookLM.

Every section includes: official docs, best YouTube videos/playlists, talks, repos, blogs, courses, and (rarely) exceptional community resources. Each resource is ranked and briefly justified.

---

## SECTION 1 – Claude for Software Engineering

### 1.1 Official documentation (must-read)

| Resource                                                                                                                                          | Rank  | Why it’s worth your time                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Claude API Docs – Intro to Claude](https://docs.anthropic.com/claude/docs/intro-to-claude)                                                       | ★★★★★ | Core mental model of Claude: messages, system prompts, tools, streaming, rate limits.                                                                        |
| [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code)                                                                                | ★★★★★ | Agentic coding workflow: plan mode, hooks, CLAUDE.md, MCP, subagents, memory. [code.claude](https://code.claude.com/docs/en/best-practices)                  |
| [Anthropic “Claude API Development Guide” / Academy](https://docs.anthropic.com/)                                                                 | ★★★★★ | Deep dive into prompt engineering, XML prompting, tool use, structured outputs, best practices.                                                              |
| [Claude Code Best Practices (Anthropic blog)](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) | ★★★★★ | How to design “harnesses” (CLAUDE.md, hooks, skills, MCPs, LSP) so agents don’t break on large repos. [youtube](https://www.youtube.com/watch?v=lGalJmyI78w) |

### 1.2 Best YouTube videos & playlists

| Resource                                                                              | Rank  | Why                                                                                                                                                                       |
| ------------------------------------------------------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| “How I 100x My Coding Speed with Claude Code – Best Practices & Workflow Tips (2026)” | ★★★★★ | Real‑world Claude Code habits: CLAUDE.md, plan mode, small tasks, local branches, test builds, parallel instances. [youtube](https://www.youtube.com/watch?v=VkZAOmuwe84) |
| “Anthropic Just Revealed The Best Claude Code Setup” (AI Labs Pro)                    | ★★★★★ | Explains the “harness > model” idea, CLAUDE.md at scale, hooks, skills, plugins, LSP, custom MCPs, subagents. [youtube](https://www.youtube.com/watch?v=lGalJmyI78w)      |
| “Claude Code Best Practices: A Developer’s Guide (2026)”                              | ★★★★☆ | Maps commands, agents, skills, hooks, MCP, memory into a coherent workflow. [mcp](https://mcp.directory/blog/claude-code-best-practices)                                  |
| Anthropic official channel – Claude API & agent talks                                 | ★★★★☆ | Direct from Anthropic: system prompts, tool use, planning, safety, agent loops.                                                                                           |

### 1.3 Key topics & how to use them

You’ll use Claude for:

- **Architecture prompts**: “Propose a Clean Architecture for a FastAPI + Playwright + Postgres AI Career Agent.”
- **Planning prompts**: “Break this feature into smallest reviewable tasks, with acceptance criteria.”
- **Debugging prompts**: “Given this traceback and code, explain root cause and propose 3 fixes with trade‑offs.”
- **Refactoring prompts**: “Refactor this module to follow repository + service pattern, preserving behavior.”
- **Code review prompts**: “Review this PR diff for bugs, security, performance, and maintainability.”
- **Test generation**: “Generate pytest tests for these endpoints including edge cases.”
- **Documentation generation**: “Write a README and API docs from this codebase.”
- **Context management**: “Summarize this repo’s architecture and key invariants for a new engineer.”

Use **plan mode** for anything non‑trivial, and keep **CLAUDE.md** concise and versioned. [code.claude](https://code.claude.com/docs/en/best-practices)

---

## SECTION 2 – VS Code AI Setup

### 2.1 Must‑have extensions (ranked by impact)

| Category                     | Extension                                                    | Rank  | What it does                                                                                                                                                                                                           | Why it matters                                         |
| ---------------------------- | ------------------------------------------------------------ | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **AI pair programmer**       | **GitHub Copilot** (`GitHub.copilot`, `github.copilot.chat`) | ★★★★★ | Ghost‑text completions + chat panel that sees open files, explains errors, generates tests. [dev](https://dev.to/_d7eb1c1703182e3ce1782/vs-code-extensions-for-productivity-in-2026-the-complete-developer-guide-2579) | Baseline AI assistance integrated with VS Code.        |
| **AI agent in editor**       | **Continue** (`continue.continue`)                           | ★★★★★ | Open‑source AI IDE: model swapping, custom context (docs, Jira, Slack), chat, inline edits. [codebrewtools](https://codebrewtools.com/blogs/best-ai-native-vs-code-extensions-2026)                                    | Great for custom AI workflows and using Claude models. |
| **AI agent (Claude‑style)**  | **Cline** (`saoudrizwan.claude-dev`)                         | ★★★★★ | Full‑file & multi‑file agent that edits code, runs terminal commands, uses tools. [devtoolreviews](https://www.devtoolreviews.com/reviews/cline-vs-roo-code-vs-continue)                                               | Strong for agentic, repo‑scale changes.                |
| **AI agent (fork of Cline)** | **Roo Code** (`roo-code`)                                    | ★★★★☆ | Enhanced Cline with extra features (parallel tasks, advanced tooling). [devtoolreviews](https://www.devtoolreviews.com/reviews/cline-vs-roo-code-vs-continue)                                                          | Good if you want more aggressive automation.           |
| **Code quality**             | **Ruff** (`charliermarsh.ruff`)                              | ★★★★★ | Fast Python linter & formatter (replaces flake8, isort, many pylint checks). [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                       | Keeps Python clean and consistent.                     |
| **Formatter**                | **Black** (`ms-python.black-formatter`)                      | ★★★★★ | Opinionated Python formatter. [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                                                                      | Removes style debates.                                 |
| **Type checker**             | **Pylance** (`ms-python.vscode-pylance`)                     | ★★★★★ | MS Python language server: type checking, IntelliSense, refactors. [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                                 | Catches type bugs early.                               |
| **Error visibility**         | **Error Lens** (`usernamehw.errorlens`)                      | ★★★★★ | Shows errors/warnings inline next to code, not just in Problems panel. [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                             | Faster debugging.                                      |
| **Git superpowers**          | **GitLens** (`eamodio.gitlens`)                              | ★★★★★ | Per‑line blame, commit history, code↔commit navigation. [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                                            | Critical for understanding code evolution.             |
| **Git graph**                | **Git Graph** (`mhutchie.git-graph`)                         | ★★★★☆ | Visual commit graph, branch operations. [dev](https://dev.to/_d7eb1c1703182e3ce1782/vs-code-extensions-for-productivity-in-2026-the-complete-developer-guide-2579)                                                     | Clean repo overview.                                   |
| **Comments**                 | **Better Comments** (`aaron-bond.better-comments`)           | ★★★★☆ | Color‑coded comments (TODO, HACK, FIXME). [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                                                          | Improves code readability.                             |
| **Task tracking**            | **TODO Tree** (`Gruntfuggly.todo-tree`)                      | ★★★★☆ | Aggregates TODO/FIXME/NOTE into a tree view. [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                                                       | Helps track technical debt.                            |
| **API testing**              | **Thunder Client** (`rangav.vscode-thunder-client`)          | ★★★★☆ | Lightweight REST client inside VS Code. [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                                                            | Quick endpoint testing without leaving editor.         |
| **Docker**                   | **Docker** (`ms-azuretools.vscode-docker`)                   | ★★★★☆ | Manage containers, images, Compose from VS Code. [builder](https://www.builder.io/blog/best-vs-code-extensions-2026)                                                                                                   | Essential for containerized FastAPI.                   |
| **Python**                   | **Python** (`ms-python.python`)                              | ★★★★★ | Language support, venv, debugging, testing integration.                                                                                                                                                                | Non‑negotiable for Python work.                        |
| **Remote dev**               | **Remote – WSL**, **Remote – SSH**, **Dev Containers**       | ★★★★☆ | Develop inside WSL/containers/remote machines.                                                                                                                                                                         | Aligns with your Ubuntu/WSL setup.                     |

**Optional / nice‑to‑have**

- **CodeRabbit** (AI code review extension) – ★★★☆☆ if you want AI PR reviews in GitHub.
- **Material Icon Theme**, **Paste JSON as Code**, **Markdown All in One** – ★★★☆☆ for polish.

---

## SECTION 3 – AI Coding Agents

### 3.1 Landscape

| Tool                              | Strengths                                                                                                                                                                                    | Weaknesses                                             | When pros use it                                               |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | -------------------------------------------------------------- |
| **Claude Code** (CLI & extension) | Strong reasoning, plan mode, hooks, MCP, subagents, large context. [code.claude](https://code.claude.com/docs/en/best-practices)                                                             | Less “always‑on” ghost text; more command/chat driven. | Complex features, refactors, architecture, repo‑scale changes. |
| **Cline**                         | Full agentic editing, terminal control, multi‑file edits. [devtoolreviews](https://www.devtoolreviews.com/reviews/cline-vs-roo-code-vs-continue)                                             | Can be too aggressive without guardrails.              | Fast feature implementation, migrations, test generation.      |
| **Roo Code**                      | Cline + extra features (parallel tasks, advanced tooling). [devtoolreviews](https://www.devtoolreviews.com/reviews/cline-vs-roo-code-vs-continue)                                            | More complexity, steeper config.                       | Heavy automation, multi‑agent workflows.                       |
| **Continue**                      | Model flexibility, custom context, open‑source, chat + inline edits. [codebrewtools](https://codebrewtools.com/blogs/best-ai-native-vs-code-extensions-2026)                                 | Less “batteries‑included” than Cursor.                 | Custom AI stacks, privacy, integrating internal docs.          |
| **Cursor**                        | Deep editor integration, AI‑first UX, chat + edit modes. [nexasphere](https://nexasphere.io/blog/best-vs-code-ai-extension-2026)                                                             | Proprietary, less control over models.                 | Rapid prototyping, solo devs wanting AI‑native IDE.            |
| **Windsurf**                      | Agentic workflows, project‑wide understanding. [nexasphere](https://nexasphere.io/blog/best-vs-code-ai-extension-2026)                                                                       | Newer, ecosystem smaller.                              | Teams experimenting with AI‑first IDEs.                        |
| **GitHub Copilot Agent Mode**     | Tight GitHub integration, code completions, chat, agent features. [dev](https://dev.to/_d7eb1c1703182e3ce1782/vs-code-extensions-for-productivity-in-2026-the-complete-developer-guide-2579) | Less flexible than custom agents.                      | Everyday coding, small tasks, quick scaffolding.               |
| **Aider**                         | CLI agent that edits code, runs tests, uses git.                                                                                                                                             | More terminal‑centric.                                 | Scripted workflows, CI‑style AI tasks.                         |
| **OpenAI Codex**                  | Historically strong code generation.                                                                                                                                                         | Superseded by newer models/APIs.                       | Legacy integrations.                                           |

### 3.2 Recommended setup for your AI backend

- **Primary agent**: **Claude Code** (for planning, architecture, complex refactors, test strategy). [code.claude](https://code.claude.com/docs/en/best-practices)
- **In‑editor agent**: **Cline** or **Roo Code** (for fast, multi‑file edits and terminal work). [codebrewtools](https://codebrewtools.com/blogs/best-ai-native-vs-code-extensions-2026)
- **Fallback / pair programmer**: **GitHub Copilot** (ghost text, quick completions, chat). [dev](https://dev.to/_d7eb1c1703182e3ce1782/vs-code-extensions-for-productivity-in-2026-the-complete-developer-guide-2579)
- **Optional**: **Continue** if you want to plug in custom context (your NotebookLM exports, internal docs). [codebrewtools](https://codebrewtools.com/blogs/best-ai-native-vs-code-extensions-2026)

---

## SECTION 4 – Model Context Protocol (MCP)

### 4.1 Official & core resources

| Resource                                                                      | Rank  | Why                                                                                                                                          |
| ----------------------------------------------------------------------------- | ----- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| [Model Context Protocol (MCP) spec](https://modelcontextprotocol.io)          | ★★★★★ | Authoritative spec: hosts, clients, servers, JSON‑RPC messages, resources/tools.                                                             |
| [MCP spec GitHub repo](https://github.com/modelcontextprotocol/specification) | ★★★★★ | Schema, examples, versioned spec; crucial for building MCP servers.                                                                          |
| Anthropic MCP resources (Claude Code docs, blog)                              | ★★★★★ | Shows how Claude Code uses MCP to connect agents to internal tools, data, APIs. [mcp](https://mcp.directory/blog/claude-code-best-practices) |
| “Intro to MCP” / “Building MCP servers for Claude/OpenAI” YouTube tutorials   | ★★★★☆ | Practical examples of implementing MCP servers and connecting them to agents.                                                                |
| Example MCP servers (GitHub)                                                  | ★★★★☆ | Concrete code for connecting to APIs, DBs, and tools.                                                                                        |
