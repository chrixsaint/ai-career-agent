---
title: NotebookLM Sources — Prompting & Building with LLMs
source: knowledge/inbox/notebooklm-sources.md
date: 2026-07-31
tags: [prompt-engineering, notebooklm, resources]
owner: @chrixsaint
confidence: high
summary: Curated NotebookLM source kit listing official prompting docs, cookbooks, and videos for Anthropic, OpenAI, Microsoft, and Copilot.
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
