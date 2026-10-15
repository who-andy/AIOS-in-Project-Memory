# AIOS in Project Memory

**Adaptive Project Memory v0.4.0** is a prompt-first Agent Skill for persistent project memory.

The Skill teaches an AI agent to ask useful questions, autonomously design project-specific files, and preserve decisions, progress, corrections and evidence during work. The project-specific `AGENTS.md`, `CLAUDE.md`, or equivalent entrypoint is created by the model, not prescribed in a fixed template.

## Start in any of three ways

1. **Discuss, then initialize.** Chat normally. Once ready: "Use adaptive-project-memory to initialize this project from our discussion. You design the files." Existing accessible dialogue becomes the source.
2. **Discuss with capture.** Say: "Use adaptive-project-memory in capture-only mode while we brainstorm. Save useful details, but don't initialize until I say so." Grant an authorized writable location. The model saves provisional records while discussion continues.
3. **Initialize now.** Say: "Initialize a persistent memory system for this project. Ask only questions that materially affect your design."

To resume, open the project in a host that loads its generated entrypoint, recover the current checkpoint, perform the work, and save material updates as they occur.

## Join a project already underway

A project might have months of study sessions or development work before the Skill is added. Say: "Use adaptive-project-memory to reconstruct my existing project progress from the materials available to you, and initialize long-term memory without restarting."

The agent checks relevant materials it can access, rebuilds the current state with evidence, records gaps, and continues working. More records can be added later without duplicating old imports. Historical sessions outside the host's accessible context must be supplied or connected before they can be included.

## Install

Copy the directory containing [SKILL.md](SKILL.md) to the recognized skills directory. For Claude Code: `~/.claude/skills/adaptive-project-memory/` or `<project>/.claude/skills/adaptive-project-memory/`. For Codex in supported environments: `<project>/.agents/skills/adaptive-project-memory/`. Other AI hosts may use different conventions.

## Design

- **Model-designed**: the AI decides which files and structure fit this project, and how they evolve.
- **High-recall capture**: save material discussions and test results promptly, keeping discarded options clearly tentative.
- **Recoverable history**: keep the current checkpoint concise, while retaining evidence and decisions.
- **Portable**: generated project entrypoints make continuity discoverable to future agents.
- **Evidence-aware**: distinguish verified, user-reported, tentative and unknown information.
- **Safe**: verify writes; never publish private notes or secrets without authorization; evolve records non-destructively.

## Limits

A Skill is a prompt package, not a daemon. Automatic writing requires an authorized persistent writable workspace and instructions loaded by the AI host. Fileless chats cannot silently save to your local computer. Prior messages cannot be recovered once inaccessible if they were never persisted.

## Evaluation

Run `python3 -m unittest discover -s tests -v` for deterministic contract checks. These do not demonstrate real model behavior. Human-run scenarios: [evals/README.md](evals/README.md).

[中文说明](README.zh-CN.md) · [Changelog](CHANGELOG.md) · [MIT License](LICENSE).
