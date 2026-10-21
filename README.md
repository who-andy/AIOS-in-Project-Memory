[English](README.md) | [简体中文](README.zh-CN.md)

# AIOS in Project Memory

**Give your local project a memory that survives AI conversations.**

This Skill lets AI **create its own memory files inside your project folder, update your progress as you work, and restore that context in a new chat or a different AI agent**. Continue learning or building without explaining everything from scratch.

No manually designed folder structure. No copying a huge chat into every new session. **Your AI decides what files the project needs and keeps them up to date.**

## Install

```bash
npx skills add who-andy/AIOS-in-Project-Memory
```

Install for use across projects:

```bash
npx skills add who-andy/AIOS-in-Project-Memory -g
```

Check that the Skills CLI discovers the Skill:

```bash
npx skills add who-andy/AIOS-in-Project-Memory --list
```

Requires Node.js/npm and a compatible AI agent. Installation uses the open-source [Skills CLI](https://github.com/vercel-labs/skills).

## How it works

1. **Talk to your AI.** Discuss a project, study a subject, or work on software as usual. You can initialize memory immediately, or wait until you've worked out what you want.
2. **The AI creates the memory files.** Once you ask it to initialize, the AI looks at the available context and creates appropriate project instructions and records **in the local project folder**. It decides the file names and structure.
3. **Progress is recorded during work.** The generated project instructions tell future agents to save important decisions, corrections, assessment results, blockers, and next steps as they happen.
4. **Resume in another conversation or AI tool.** Open the same project folder with an agent that can read its instructions and files. It loads the relevant memory and carries on from the recorded state.

For example, after several weeks of studying, the project might have a short entrypoint, a progress record, and detailed notes. The actual layout is **created by the model for your project**, not imposed by this Skill.

## Start with one sentence

**Discuss first, initialize when ready**

> We've discussed this project enough. Use aios-in-project-memory to create and maintain long-term memory files in this local project folder. Decide what files are needed yourself.

**Save important details while brainstorming**

> Use aios-in-project-memory to capture important discussion details in this project folder while we brainstorm. We'll initialize the full memory system when I'm ready.

**Already halfway through a project**

> I've already worked on this project across several chats. Use aios-in-project-memory to recover my current progress from the history and files you can access, build local project memory, and help me continue from here.

## Grows and shrinks with your project

**One goal? Keep it simple.** AIOS starts with the smallest useful memory structure. Opening another chat does not create another workstream.

**Several related goals? Share facts, separate progress.** An application project might later have a CV, personal statement, and activities. They share one authoritative record of facts while each retains its own draft decisions and next step. The AI chooses when separate records are actually useful; you don't need to plan folders in advance.

**Goals finished or removed? Simplify again.** The AI can archive or consolidate active records once there is a clear reason. Old evidence remains recoverable. Silence alone does not mean a task is finished, and unrelated drafts are not automatically rewritten when a shared fact changes.

The goal is **the least complicated structure that still lets the next AI resume correctly**.

## What gets remembered?

Whatever is useful for the **next conversation to continue accurately**: goals, current progress, verified results, decisions and their reasons, mistakes, corrections, unresolved questions, and the next step.

The AI keeps a short starting point for fast recovery and more detailed history for when it's needed. It distinguishes confirmed facts from ideas and unverified claims. Old notes can be imported later if a project started before the Skill was installed.

## Renaming from the earlier Skill

If you previously installed the older `adaptive-project-memory` Skill, remove that old installation using your agent's Skill manager or delete its old Skill folder after installing this version. This prevents duplicate Skill entries. Existing **project memory files should be left intact**.

## Requirements and limitations

This is a **prompt-based Agent Skill**, not a background recording service. Reliable saving requires a writable, persistent project folder and an AI host that loads the generated project instructions in future sessions. Claude Code, Codex, and similar file-capable agents are natural use cases; setup varies by tool.

**Cross-AI recovery works through shared project files.** A different AI needs access to that folder and must read the project instructions. If earlier chats were never saved and are unavailable, the Skill cannot recreate them.

Memory stays in the location you authorize. Keep private learning records and sensitive project context out of public repositories unless you deliberately choose to publish them.

## Project

[Skill instructions](SKILL.md) · [中文说明](README.zh-CN.md) · [Evaluation scenarios](evals/README.md) · [Changelog](CHANGELOG.md) · [MIT License](LICENSE)

Structural checks:

```bash
python3 -m unittest discover -s tests -v
```

These check Skill rules and packaging. Real-world long-session reliability still needs testing across hosts and models.
