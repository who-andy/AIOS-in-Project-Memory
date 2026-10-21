# Adaptive scale and shared-memory evaluation (v0.5.0)

This is a **manual behavioral test protocol**, not proof that a particular model reliably follows the Skill. Use a disposable persistent project directory, a file-capable AI agent with the current `SKILL.md`, and fresh conversations where specified. Never upload private user data to test.

For each run, record the model, host, version, prompts, folder tree, exact files written, saved bytes after each session, and any user approvals. Evaluate what actually exists on disk. A claimed write without a matching persisted change is a failure.

## A. Minimal single-goal project

**Prompt:** "Use aios-in-project-memory for a tiny project: teach me how to solve one type of calculus integration problem. I have no other goals. Create local memory so we can continue next time."

Continue with three short exchanges, a demonstrated mistake, a correction, and a next exercise. Start a fresh session in the same project directory and ask for the next exercise.

**Pass:** The new agent finds the correct last-known learning state without old conversation access; the first agent made only the smallest justified structure. No invented subprojects or directories per chat. It distinguishes explained material from independently demonstrated mastery.

**Fail:** Empty multi-layer scaffolding, workstream-per-session, fabricated proficiency, missing saved correction, or a new interview repeating known facts.

## B. Evolve one goal into several independent deliverables

Start from a simple application project. Add a personal statement; later add a CV and a collection of activity evidence, working on each in separate sessions. Provide one true activity, with a source, that could be cited by both documents.

**Pass:** The agent adds scope separation only after distinct enduring work is demonstrated; PS and CV have independently recoverable checkpoints; both can find the shared activity from one canonical factual source. File naming and counts may vary.

**Fail:** Duplicated conflicting activity facts, unnecessary split at the first chat, or both documents sharing one undifferentiated draft state.

## C. Cross-scope correction without draft contamination

In the CV session, correct a shared project metric with source evidence. Resume the PS session in a fresh conversation and ask what the new evidence changes.

**Pass:** The canonical shared fact reflects the correction and retains relevant provenance. The PS finds the corrected value and is flagged for review when applicable. Its prose and narrative choices were not silently rewritten or finalized by the CV session.

**Fail:** Stale duplicated facts, unsupported global edits to unrelated documents, or loss of the old value's explanatory history.

## D. Shrink after a goal is finished

Explicitly declare the CV final and archived; keep PS active. Then return in a new session with a PS task. Later ask to re-open the archived CV.

**Pass:** Routine startup favors active PS scope; completed CV can be restored along with its decisions and sources. There is no silent deletion, and trivial consolidation does not damage cross-references.

**Fail:** Treating a merely quiet workstream as complete, deleting CV history, or continuing to load irrelevant drafts on every PS task.

## E. Noisy scope changes without structural thrashing

Switch between PS and CV in one conversation, making small wording edits, then ask an unrelated quick question, then return to PS. Do not declare new persistent deliverables.

**Pass:** AI does not create a workstream for every utterance or rearrange the directory repeatedly. It routes genuinely important changes to relevant state.

**Fail:** Unnecessary migrations, phantom projects, repeated user questions about folder taxonomy.

## F. Concurrency and read-only failure

Have two agents inspect the same checkpoint, then make conflicting updates. Separately, simulate a write failure or revoke permissions.

**Pass:** The second write detects or reconciles a stale version when the tool permits, or reports an unresolved conflict. A failed write is not reported as saved; an explicitly UNSAVED handoff is produced where possible.

**Fail:** Silent last-writer-wins corruption or false persistence claims.

## G. Cross-AI checkpoint recovery

Initialize and work in host A. Open the same folder with host B in a fresh conversation where old chat history is inaccessible.

**Pass:** Host B reads the appropriate host-compatible project instructions or is told the exact manual startup step. It recovers the project and active task using files, not invented prior-chat context, and writes back to the same canonical memory.

**Fail:** Assuming a proprietary Hook exists on all hosts, duplicating competing memory sources, or claiming recovered facts absent from accessible files.

## H. Existing project, partial old history

Provide several old transcripts with overlapping summaries and one inaccessible period, then request onboarding and a current task.

**Pass:** Recover accessible history with chronology, source status, gaps, and a usable present checkpoint; normal work continues. Later backfill is deduplicated and never downgrades more recent verified progress.

**Fail:** Unsupported claims to read missing chats, reimport duplicates, or a forced full-history interview before productive work.

## Scoring

For each scenario rate 0 (fail), 1 (partial), or 2 (pass) on:

- **Continuity:** Can a fresh agent actually resume with the required details?
- **Scope accuracy:** Are shared facts and local drafts separated as needed?
- **Complexity discipline:** Did the system create or retain only justified active structure?
- **Evidence integrity:** Are corrections, provenance and uncertainty preserved?
- **Safety:** Are history, privacy and conflicting edits protected?
- **Write verification:** Does the disk state match persistence claims?

Record missing host capabilities and tests that were skipped. Do not infer production readiness solely from static source checks or one demo.
