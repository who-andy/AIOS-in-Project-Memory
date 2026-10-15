[English](README.md) | [简体中文](README.zh-CN.md)

# AIOS in Project Memory

**Your project remembers, even when your AI doesn't.**

An open-source Agent Skill that lets your AI **design, build, and maintain persistent project memory** for long-running learning, development, research, and anything else you want to pick up where you left off.

Your AI decides what to remember, asks useful questions, and creates the project-specific files itself. You don't need to design a memory system.

## Install in one command

```bash
npx skills add who-andy/AIOS-in-Project-Memory
```

Install globally to make the Skill available across your projects:

```bash
npx skills add who-andy/AIOS-in-Project-Memory -g
```

Or target specific supported agents, such as Claude Code and Codex:

```bash
npx skills add who-andy/AIOS-in-Project-Memory -g -a claude-code -a codex
```

These commands use the open-source [Skills CLI](https://github.com/vercel-labs/skills). **Node.js and npm/npx are required.** The CLI will guide you through selecting agents and installation scope unless options are provided. You do not need to publish or install a separate npm package for this repository.

Check which skills the CLI can find before installing:

```bash
npx skills add who-andy/AIOS-in-Project-Memory --list
```

> **Important:** Installing a Skill teaches compatible agents how to manage memory. Persistent saving requires the agent to load the instructions and have read/write access to your chosen project workspace. No prompt can recover old conversations the host cannot access.

## What it does

| Capability | How it helps |
| --- | --- |
| **Adaptive conversation** | The AI asks about goals and current progress only when needed, without making you choose filenames or technical architecture. |
| **Model-designed memory** | The AI creates a suitable project entrypoint and records for your specific project instead of applying a rigid template. |
| **Capture during work** | Meaningful corrections, decisions, test results, learning evidence, and next steps are saved as work proceeds, when a writable workspace is available. |
| **Resume across sessions** | Future agents can load a compact project checkpoint and retrieve relevant history instead of relying on a huge chat. |
| **Join halfway through** | Already spent months studying or developing? The AI reconstructs your current position from accessible old chats, documents, code, and records. |
| **Portable and evolving** | Human-readable project files can be used by different tools, and their organization can evolve with the project. |

## Quick start

Choose the approach that matches how you work.

**1. Discuss first, initialize later**

> Let's brainstorm this project first. When I say we're ready, use adaptive-project-memory to create a long-term memory system from what we've discussed.

**2. Discuss and save useful context from the beginning**

> Use adaptive-project-memory in capture-only mode while we brainstorm. Save important details in this project workspace, but don't finalize the project structure until I say so.

**3. Start from an existing project**

> I've been learning this subject for months across multiple chats. Use adaptive-project-memory to recover my current progress from whatever history and files you can actually access, record what remains unknown, and set up memory so we can continue from here.

**4. Initialize right away**

> Use adaptive-project-memory to initialize persistent project memory for this work. Ask only the questions you need, and choose the files and structure yourself.

## How it works

```text
Your goals and ongoing discussion
              |
    Adaptive Project Memory
              |
    Understand / ask when needed
              |
   AI designs project memory files
              |
 AI creates project instructions
  (AGENTS.md / CLAUDE.md / etc.)
              |
Future sessions read the checkpoint
   and write meaningful updates
```

The [SKILL.md](SKILL.md) contains the reusable method. **Your agent generates the project's own memory files and instructions**, including where to read current progress and when to persist new evidence. File names and layouts are chosen for the actual project.

The first conversation can remain a free discussion. If you want that discussion saved, enable capture-only mode **before** important details are lost.

## Already halfway through a project?

Retroactive onboarding is built in. The agent looks for relevant, authorized sources it can **actually access**, reconstructs documented progress, and keeps a record of missing or conflicting history. New records can be imported later without starting again.

You do **not** need to provide every old chat. But a session that is unavailable to the AI cannot be reconstructed unless you connect or supply the relevant contents. Your ongoing work should continue even if recovery is incomplete.

## Supported environments and limitations

This is a **prompt-first Agent Skill**, with no background recorder or mandatory database. It works best in AI coding agents that can read and write persistent files and load project-level instructions at the start of new sessions.

- **Claude Code / Codex:** install through Skills CLI, then use it in a writable project.
- **Other supported agents:** discovery, auto-loading, and write permissions vary by host.
- **Fileless AI chats:** the AI may prepare an export, but cannot silently save to your local disk.

The agent must verify writes rather than falsely claiming autosave. Keep sensitive records in a private workspace; **do not publish personal project memory to a public GitHub repository** without explicit approval.

## Contributing and evaluation

This is an early project. Feedback is especially valuable on long-running study projects, existing software repositories, and switching between AI tools.

- [Read the Skill instructions](SKILL.md)
- [Behavioral evaluation scenarios](evals/README.md)
- [Changelog](CHANGELOG.md)
- [License](LICENSE)

Run the package's structural tests:

```bash
python3 -m unittest discover -s tests -v
```

These tests check structural requirements; real-world memory retention across models and long sessions still needs empirical evaluation.

If you find it useful, consider starring the repository or opening an issue with a reproducible example.
