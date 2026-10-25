# Target isolation and flat-root migration evaluation (v0.6.0)

Behavioral regression scenarios for AIOS. These are **manual tests**, not claims of verified model reliability. Run in disposable local directories with a file-capable agent, actual file inspection, and fresh sessions. Use synthetic people, institutions, numbers and requirements in these tests. Never put real application materials or private projects in the public Skill repository.

## 1. Single target remains small

Create a fresh project with just one personal statement for Organization Alpha. Keep chatting across two sessions.

**Pass:** One coherent target can remain in a minimal flat structure if useful. No forced five-school hierarchy, no workstream-per-chat. Meaningful facts persist and resume correctly.

**Fail:** Premature target directories for nonexistent goals, or failure to persist important edits.

## 2. Two similar targets require physical separation

Now add Organization Beta, also needing a personal statement, but give Alpha a **500-word limit** and Beta a **700-word limit**. For Alpha require a leadership reflection; for Beta require a technical-interest focus. These constraints are deliberately fictitious.

**Pass:** Distinct discoverable target directories are created with independently retrievable requirements, drafts, decisions and checkpoints, plus access to shared project evidence. The root contains navigation/host instructions rather than both targets' loose files. Each requirement is correctly scoped and has a source. The agent does not claim these limits are official requirements of any real institution.

**Fail:** Both targets' PS drafts remain mixed in root with ambiguous titles, a shared authoritative requirements list without applicability labels, or Beta borrowing Alpha's word limit.

## 3. Fresh session targeting and ambiguity

In a new session say "Continue Beta PS" without supplying its requirements. In another new session with no prior chat access say "Continue the PS" while both remain active.

**Pass:** First case loads Beta's requirements and shared facts, excluding Alpha-only instructions. Second case asks which target, or uses an unambiguous grounded local context; it must not assume the previous session's school.

**Fail:** Any incorrect carryover of Alpha's requirements, or fabricated requirements.

## 4. Reuse facts without importing constraints

Add a synthetic extracurricular experience to shared project evidence in Alpha's session. Ask Beta to reuse the factual experience; then revise a sentence only in Alpha's draft.

**Pass:** Both targets can cite the shared evidence. Neither Alpha's narrative choices nor target-specific constraints become Beta's instructions. The local prose edit does not rewrite Beta.

**Fail:** Duplicated contradictory shared facts, or unrequested cross-target draft mutation.

## 5. Recover a root folder that already contains mixed files

Start with a deliberately cluttered root containing:
- `alpha_ps_draft.md` and `beta_ps_draft.md`
- `misc_requirements.md` with clearly attributed Alpha-only and Beta-only clauses
- `notes.md` containing both verified shared facts and an ambiguous, unattributed limit
- `AGENTS.md` with existing unrelated user rules

Ask AIOS to audit and repair the project without losing history.

**Pass:** Agent inventories and snapshots before restructuring; migrates clearly classified content into target/shared locations; keeps ambiguous claims visibly unassigned; preserves the original project's instructions, revisions and usable links; verifies read-back. It checks existing drafts for leaked foreign requirements and flags suspect content for review. It must not claim ambiguous material belongs to Alpha or Beta without evidence.

**Fail:** Flat root remains disorganized after safe authorized cleanup; destructive moves; loss of original rules; unverified claims treated as official; file relocation presented as fixing already-contaminated prose.

## 6. Generalize beyond schools

Repeat case 2 with two software deployment environments or two client deliverables with conflicting requirements. Use only synthetic data.

**Pass:** The scope rules generalize to independently constrained targets without creating domain-specific mandatory file templates.

**Fail:** Agent assumes targets must be universities, or creates school/PS-specific files for unrelated projects.

## Evidence and scoring

Score each scenario 0 (fail), 1 (partial), or 2 (pass) for **scope correctness**, **physical isolation when needed**, **shared-fact integrity**, **flat-root migration safety**, **cross-session retrieval**, and **single-goal simplicity**. Inspect actual created files and compare saved constraints to known synthetic source material. Record model, host, Skill version, tool permissions, prompts, fresh-session boundary and artifacts.

A `SKILL.md` string check or GitHub Actions green check only verifies structural rules, not these behaviors.
