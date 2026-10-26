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

### Update an existing installation

Check whether updates are available:

```bash
npx skills check
```

Update **AIOS only** in the current project (run inside that project's folder):

```bash
npx skills update aios-in-project-memory -p
```

If you originally installed it globally (`-g`):

```bash
npx skills update aios-in-project-memory -g
```

Restart your Claude Code or Codex session so it can load the updated Skill. Updating the **installed Skill** does not by itself reorganize existing project memory files; in older projects, invoke the updated Skill once to audit and safely migrate them if needed. See [automatic project-memory migration](#automatic-migration-of-existing-project-memory-v08).

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

## Nested projects and intelligent sharing

One project can have **nested targets at as many meaningful levels as the work requires**. AIOS keeps a single-goal project small, then builds deeper folders only when independent tasks need their own drafts, constraints or checkpoints.

For example, an application project might evolve into:

```text
applications/
├── AGENTS.md                 # Project entrypoint, where supported
├── shared/                   # Reusable facts across schools
│   └── activities.md
└── universities/
    ├── HKU/
    │   ├── shared/            # Verified HKU context useful to both tasks
    │   ├── personal-statement/
    │   └── interview/
    └── HKUST/
        ├── personal-statement/
        └── interview/
```

This is **only an example**, not a mandatory depth, tree shape or fixed naming convention. The model can nest further, choose a different grouping, or use lightweight references when that better fits the project. Multiple distinct targets must not leave their conflicting requirements mixed in the project root.

**Shared memory is dynamic and scoped.** If an interview task needs a factual achievement that currently appears only in a PS research note, AIOS should discover that source within the authorized project, verify its provenance and applicability, and link or promote the reusable evidence to an appropriate shared scope. School-specific word limits and draft decisions must not be promoted as universally applicable. A shared fact remains authoritative in one place, with relevant tasks linking to it.

**Each new session identifies its actual target and subtask before applying requirements.** It reads the relevant branch and only necessary shared evidence; it doesn't automatically import sibling rules or every project file.

**Already have mixed files at the root?** Updating the Skill does not rearrange them automatically. In that local project ask AIOS to inventory, back up, inspect and safely reorganize the existing files, check previous drafts for cross-target requirement leakage, verify references, and retain uncertain material for review.

## Works with Claude Code and Codex, without a controller chat

AIOS now maintains a **small, evidence-linked project-state view only when multiple independent workstreams or dependencies justify it**. A new session can discover the correct task, verified progress, blockers and affected shared facts. It does not make all drafts or requirements globally applicable. No dashboard, central manager session or new setup is required for ordinary use.

Optional, host-aware integrations can help with advanced projects: Claude Code Skills/Hooks/subagents or supported scheduling choices, and Codex project instructions/multi-agent/Automations when the actual host exposes them. These are **not enabled by default**. If you ask for a recurring project check, AIOS should verify scheduling support, permissions and the scheduler's access to your real project files before claiming a task was configured. A cloud job may not see a laptop folder.

The Skill remains portable and file-first. The extra guidance lives in [project coordination](references/project-coordination.md) and [optional host adapters](references/host-adapters.md), loaded only when needed.

## Automatic migration of existing project memory

When an updated, trusted AIOS Skill is **actually loaded** in a writable project, it can inspect the project's existing instructions and memory, detect obsolete structures, and **automatically apply safe, reversible adjustments**. It preserves the original data, repairs navigation and checks that new sessions can find the correct scope. A small marker in the project entrypoint (e.g. `AIOS memory policy: 0.9.0`) identifies the latest successfully applied policy; merely installing a new Skill version does **not** advance it.

**Not a background updater:** Updating the CLI-installed Skill does not automatically change old `AGENTS.md`/`CLAUDE.md` files. A legacy project must load/invoke the updated Skill at least once to bootstrap this behavior; afterward a generated entrypoint can check locally available Skill instructions on later sessions. If the installed Skill is unavailable, the project continues to work using existing instructions rather than claiming a version check.

**No destructive autopilot:** It can create missing indexes, directories and validated references, but must preserve snapshots/history and ask before irreversible deletion, risky overwrites, permission changes or sharing sensitive data outside its original boundary. A repeat launch should not endlessly rearrange a healthy project.

To upgrade an old project, update your local Skill using your installer, open the **existing** project folder in your file-capable agent, and request:

> Use the latest aios-in-project-memory in this project. Audit my existing project memory, safely migrate only what is actually needed, preserve and verify all files, and write the applied memory policy version only after successful checks.

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
