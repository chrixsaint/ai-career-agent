---
title: Dev Prompt Engineer — Prompting & Building with LLMs
source: knowledge/inbox/Dev Prompt Engineer.md
date: 2026-07-31
tags: [prompt-engineering, prompts, cookbooks]
owner: @chrixsaint
confidence: high
summary: Canonical prompt-engineering guide and source kit with official Anthropic/OpenAI references, videos, and cookbooks; intended for NotebookLM ingestion and prompt-library maintenance.
---

# NotebookLM Source Kit: Prompting & Building with LLMs

For each resource: official URL → best video → GitHub repo → supplementary articles (only where they add something the docs don't).

---

## 1. Anthropic Prompting Documentation ⭐⭐⭐⭐⭐

- **Official URL:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
  (Overview page, if you want the index first: https://docs.anthropic.com/en/docs/prompt-engineering)
- **Best video:** "Prompting 101" from Code w/ Claude 2025 — Anthropic's own applied AI team walking through prompting fundamentals.
  https://www.youtube.com/watch?v=ysPbXH0LpIE
- **GitHub repo:** anthropics/prompt-eng-interactive-tutorial — the official 9-chapter interactive course (notebooks you can run against the API).
  https://github.com/anthropics/prompt-eng-interactive-tutorial
  (Sits inside the broader anthropics/courses repo, which also has tool-use and evals courses: https://github.com/anthropics/courses)
- **Articles:** Skip — the docs + tutorial are comprehensive enough that most third-party writeups just restate them without adding value.

---

## 2. OpenAI Prompting Guide ⭐⭐⭐⭐⭐

- **Official URL:** https://platform.openai.com/docs/guides/prompting
  (Companion strategy page: https://developers.openai.com/api/docs/guides/prompt-engineering)
- **Best video:** No single official OpenAI-published video matches the docs' depth as of this search — worth checking OpenAI's YouTube channel directly before adding one, rather than an unofficial recap.
- **GitHub repo:** openai/openai-cookbook — the practical companion to the docs, with runnable prompting techniques and examples.
  https://github.com/openai/openai-cookbook
- **Articles:** Skip for the same reason as Anthropic's — most blog posts on this topic are summaries of the six core strategies already in the guide.

---

## 3. GitHub Copilot Documentation ⭐⭐⭐⭐☆

- **Official URL:** https://docs.github.com/en/copilot/concepts/prompting/prompt-engineering
  (Companion best-practices page: https://docs.github.com/en/copilot/get-started/best-practices)
- **Best video:** No single flagship official video — GitHub's docs page links out to blog content rather than a canonical video. Worth checking the GitHub YouTube channel for their Copilot Chat demo series if you want one.
- **GitHub repo:** N/A in the traditional sense — Copilot's "repo" is really its documentation source (github/docs), but that's not something you'd feed into NotebookLM as a primary source.
- **Articles:**
  - "How to write better prompts for GitHub Copilot" (The GitHub Blog) — written by GitHub's own developer advocates, adds the "developer vs. ML researcher" framing and a worked example not in the docs.
    https://github.blog/developer-skills/github/how-to-write-better-prompts-for-github-copilot/

---

## 4. Microsoft Prompt Engineering Guidance ⭐⭐⭐⭐☆

- **Official URL:** https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/prompt-engineering
- **Best video:** "Understanding Prompt Engineering Fundamentals" — part of Microsoft's official Generative AI for Beginners video series, presented by Nitya Narasimhan.
  https://learn.microsoft.com/en-us/shows/generative-ai-for-beginners/understanding-prompt-engineering-fundamentals-generative-ai-for-beginners
- **GitHub repo:** microsoft/generative-ai-for-beginners — the official 21-lesson course; lessons 4–5 are specifically prompt engineering fundamentals and advanced prompts, aimed at engineers building with the concepts, not just chat users.
  https://github.com/microsoft/generative-ai-for-beginners
- **Articles:** Skip — the Learn docs and the course lessons cover this thoroughly for a software-engineering audience already.

---

## 5. Anthropic Engineering Blog ⭐⭐⭐⭐⭐

- **Official URL:** https://www.anthropic.com/engineering
  (Also mirrored/aggregated at https://claude.com/blog)
- **Best video:** No single video — this is a blog, not a course, so there isn't a canonical companion video. If you want moving-picture context on how Anthropic thinks about building with LLMs, "Prompting 101" from item 1 doubles well here too.
- **GitHub repo:** N/A directly, but many posts link to real repos worth pulling in separately as you go — e.g. the "Building Effective Agents" post references patterns implemented in the Claude Cookbook (anthropics/anthropic-cookbook).
  https://github.com/anthropics/anthropic-cookbook
- **Articles:** Not applicable — treat the blog itself as the primary source rather than looking for secondary write-ups of it.

---

### Notes for import

- A few slots above (Copilot video, OpenAI video) have no strong canonical official match — flagged rather than filled with a mediocre third-party video, per your "official first" rule.
- The two cookbook repos (Anthropic, OpenAI) are worth adding as their own NotebookLM sources if you want runnable code alongside the docs, not just prose.

---

## AI Engineering OS — First Pass (Sections 1, 4 core, 3, 9)

Scope note: this covers the pieces most load-bearing for your immediate 2-week FastAPI/Playwright build. Sections 2, 5, 6, 7, 8, and 10 (VS Code extension audit, prompt libraries, conference-talk curation, "ultimate toolkit") need 40+ more searches to do properly — genuinely a job for the Research feature, not one chat turn. Ask for it and I (or that mode) can run the rest.

---

## SECTION 1 — Claude for Software Engineering

| Resource                                                                                                                                       | Type                                                   | Why it's worth it                                                                                                                                                                                                                                                                                          | Priority    |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| [Best practices for Claude Code](https://code.claude.com/docs/en/best-practices)                                                               | Official docs                                          | This is _the_ source — covers CLAUDE.md, context scoping, permissions, parallel sessions, subagents. Written by Anthropic for exactly your setup (repo-scale work).                                                                                                                                        | Must-have   |
| [Anthropic prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) | Official docs                                          | Covers XML structuring, thinking, agentic system prompting — the techniques Sections 1's sub-bullets (XML prompting, thinking modes, planning) all trace back to.                                                                                                                                          | Must-have   |
| [anthropics/prompt-eng-interactive-tutorial](https://github.com/anthropics/prompt-eng-interactive-tutorial)                                    | GitHub (official)                                      | Runnable 9-chapter course — best way to _drill_ clarity, role prompting, chaining rather than just read about them.                                                                                                                                                                                        | Recommended |
| [ClaudeLog](https://claudelog.com/)                                                                                                            | Community docs/wiki                                    | Not official, but the most cited community reference specifically for Claude Code mechanics (context window behavior, subagent patterns, speed/reliability tradeoffs). Cross-check anything from here against the official docs since community advice on fast-moving tools goes stale.                    | Recommended |
| ["Claude Code Best Practices: 8 Rules I Learned the Hard Way"](https://www.iwoszapar.com/p/claude-code-best-practices)                         | Blog                                                   | Adds a failure-mode framing the docs don't emphasize as sharply: over-stuffed CLAUDE.md, "trust without verify," unbounded "go investigate" tasks flooding context, over-broad permissions on sensitive repos. Genuinely useful checklist for a solo 2-week sprint where you won't have a second reviewer. | Recommended |
| [TurboDocx: "How to Write a CLAUDE.md File That Actually Works"](https://www.turbodocx.com/blog/how-to-write-claude-md-best-practices)         | Blog                                                   | Concrete pattern for structuring CLAUDE.md with progressive disclosure (`@imports`) so Claude only loads detail when a task needs it — directly useful once your FastAPI repo grows past a few modules.                                                                                                    | Recommended |
| "Prompting 101" — Code w/ Claude 2025                                                                                                          | [YouTube](https://www.youtube.com/watch?v=ysPbXH0LpIE) | Official Anthropic applied-AI team session, not a third-party recap.                                                                                                                                                                                                                                       | Recommended |

---

## SECTION 4 — Model Context Protocol (MCP), scoped to your stack

| Resource                                                                                                                                      | Type            | Why it's worth it                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Priority                                              |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| [modelcontextprotocol.io](https://modelcontextprotocol.io) (docs) / [spec repo](https://github.com/modelcontextprotocol/modelcontextprotocol) | Official        | The protocol itself — origin, architecture, JSON-RPC message types. Read this before installing servers so you understand what you're wiring together.                                                                                                                                                                                                                                                                                                                                                                                       | Must-have                                             |
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)                                                               | Official GitHub | The canonical list of maintained servers — GitHub, Filesystem, PostgreSQL, Puppeteer (browser automation), Google Drive, Slack, etc. Anthropic-managed, community-built.                                                                                                                                                                                                                                                                                                                                                                     | Must-have                                             |
| [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)                                                                       | Official GitHub | Direct hit for your stack — gives an agent full browser control via Playwright's accessibility tree (no screenshots/vision models needed). Install: `claude mcp add playwright npx @playwright/mcp@latest`. **Caveat worth knowing:** the maintainers now recommend their newer CLI+SKILLS approach over MCP for high-throughput coding agents, because MCP's tool schemas and accessibility trees eat context budget that a CLI invocation doesn't. Worth trying both and seeing which fits your context budget once your test suite grows. | Must-have                                             |
| GitHub MCP server (in modelcontextprotocol/servers)                                                                                           | Official        | Lets Claude read issues/PRs/repo state directly instead of you copy-pasting — useful for a solo project where you're also the reviewer.                                                                                                                                                                                                                                                                                                                                                                                                      | Recommended                                           |
| Filesystem MCP server (in modelcontextprotocol/servers)                                                                                       | Official        | Scoped file read/write outside Claude Code's own tools — most useful if you're also driving Claude Desktop or another client alongside Claude Code.                                                                                                                                                                                                                                                                                                                                                                                          | Optional (Claude Code already has native file access) |
| PostgreSQL MCP server (in modelcontextprotocol/servers)                                                                                       | Official        | Read-only schema inspection + queries — relevant once your FastAPI app has a real Postgres backing store, so Claude can reason about schema without you pasting DDL every session.                                                                                                                                                                                                                                                                                                                                                           | Recommended once DB exists                            |

---

## SECTION 3 — AI Coding Agents: landscape and recommendation

| Tool            | Strength                                                                                                   | Weakness                                       | Best use case                                                                                                   | Sources                                                                                                                                                                                                          |
| --------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Claude Code** | Leads SWE-bench Verified (~80.9% w/ Opus 4.6), 1M-token context, terminal-first, deep multi-file reasoning | No visual IDE polish; you live in the terminal | Deep, long-running, autonomous refactors and cross-file reasoning — your primary driver given your stated stack | [Requesty comparison](https://www.requesty.ai/blog/agentic-coding-tools-compared-2026-claude-code-cursor-codex-aider), [jobsbyculture comparison](https://jobsbyculture.com/blog/ai-coding-agents-compared-2026) |
