# Project-state coordination (optional reference for complex work)

**Load this reference only** when a project has multiple active goals, independently evolving agents/sessions, dependencies, or cross-scope changes. For a single-goal project, the ordinary AIOS checkpoint is sufficient. This reference describes **functions**, not mandatory filenames, folders, database schemas, or a separate controller process.

## Project pulse

Maintain the smallest navigable project-wide view that can answer:
- What are the **actual active scope paths**, and where does each scope's canonical checkpoint live?
- Which high-impact outcomes are **in progress, waiting, blocked, completed, archived or uncertain**?
- What is the **next actionable step**, and which verified prerequisite or approval blocks it?
- Which shared evidence or contract was recently revised, **by whom/which source, when, and with what confidence**?
- Which other scopes might need review because an authoritative fact, requirement, interface or dependency changed?

For tiny projects, these may be a few lines in the existing entrypoint or checkpoint. Larger projects may use a short project index pointing to individual scoped checkpoints and source records. Never create a dashboard, manager Session, new agent, issue tracker or dedicated state folder just to satisfy the words “project pulse.” Actual evidence and working documents remain authoritative over summarized statuses.

## Lightweight coordination loop

At entry and meaningful milestones:
1. **Resolve scope**: active target/workstream, applicable ancestor constraints, access boundary, and canonical records.
2. **Read selectively**: its own checkpoint, relevant project pulse, and shared evidence. Read source artifacts when the pulse may be stale.
3. **Reconcile evidence**: compare reported status with observed files/tests/PRs/notes; identify dependency changes and stale or ambiguous claims. Never infer that a task is complete merely because another agent said so.
4. **Work normally**: perform the user's requested work rather than producing coordination metadata in place of work.
5. **Persist**: write scoped work and reliable evidence first; then update the small pulse and references. Include enough why/source information to recover across sessions.
6. **Surface meaningful impact**: mark affected tasks or drafts **needs review** with precise source pointers. Do not silently apply a different scope's requirements or rewrite other owners' deliverables.
7. **Verify**: reread changed state/links and confirm the persisted bytes before reporting success.

Status transitions should be grounded: a task is `done` only if its explicitly relevant acceptance evidence supports it; `blocked` names the blocker; `waiting` identifies who/what is expected. Use statuses only for meaningful multi-task work; no status machinery for casual chats.

## Cross-session change notices without an always-on controller

On a shared fact/interface/constraint update, record a brief **change note** at the canonical source: old/new value where safe, evidence, time or revision, affected known scopes, and pending review. Keep links from potentially dependent scopes or a small pending-review section in existing navigation. Other Agents find it on their **next authorized visit**; no promise of instant notification or spontaneous background intervention. When a host provides real messaging or scheduling, optional delivery may supplement this durable record, but must not replace it.

### Provenance and fan-out

Differentiate:
- **Global/shared evidence**: facts verified or properly qualified for cross-scope consumption.
- **Parent-scope evidence**: valid only in that branch.
- **Local draft decisions**: never globally binding without independent validation.
- **External dynamic facts**: need current checks before use where materially time-sensitive.
- **Reported progress**: provisional until verified against outputs and tests where possible.

A change to a fact does not authorize automatic edits to PS narratives, third-party accounts, software interfaces, or other target deliverables. Flag required review; ask for approval if a material decision or risky edit would result.

## Concurrent Agents and worktrees

Only add concurrency handling when two or more agents actually write to shared state. Multiple worktrees or detached branches may have **different filesystem snapshots**, so “same project name” alone does not imply a common live memory directory. Verify the actual shared path, branch and merge route before delegating.

Before a shared write:
- Establish which agent or artifact owns the canonical record and current base revision, when the tools expose one.
- Prefer **one writer** for the small project pulse; let independent workers update their own scoped records. Others contribute proposed changes, diffs or handoff notes.
- Use available version/commit checks, compare-and-swap, merge/rebase, or explicit conflict review. Do not blindly last-write-wins.
- Reconcile simultaneous claims of completion or contradictory facts with source evidence.
- If the host cannot provide atomic writes or version checks, avoid concurrent writes to the same file; serialize through one coordinator Agent or separate append-only pending notes in clearly different files, then merge with review.
- A worker's “done” message never substitutes for verifying actual files/tests before marking the project milestone complete.

Do not require users to create a persistent “manager chat.” The current authorized Agent can perform this lightweight coordination on demand. Do not silently spawn agents, grant broad repository permissions, create branches, schedule tasks or increase spend simply because a project has several workstreams.

## Human interface: what to show

Keep ordinary replies about **the user's actual goal**. Mention coordination only if it changes the next action: a relevant dependency is blocked, an important shared fact changed, two tasks conflict, or safe authorization is needed. Avoid status spam and file-maintenance questions. When asked for “project status,” produce a concise, sourced view based on the last verified records, clearly indicating unavailable or stale information.

## Checks

Test at least: one-goal project unchanged; two workstreams with one dependency; one shared correction affecting only appropriate targets; missing or stale status evidence; separate Agent write conflicts; different worktrees without common state; and new-session recovery of an affected scope.
