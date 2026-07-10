# Prompt-optimization: lessons learned & next-research proposal

Honest engineering notes from the planner/writer prompt-refinement loops. Section 4
is a **proposal only — do not run it as-is**; it is a high-cost effort the user will
refine before committing. Companion refs: [`carlin-craft.md`](carlin-craft.md) (the
craft gold standard) and the optimizer at
`experiments/loops/refine_role.workflow.js`.

---

## 1. What we ran (timeline)

| Run | Design | Outcome |
|---|---|---|
| Planner v1 | single lenient reviewer, absolute scores | **Inflated** — 5/5/5/5; hid real weaknesses |
| Planner v2 | harsh anchored rubric, single-pass **forward edit** | **Accepted a regression** (stakes 4→3) + prompt bloat (18→60 lines) |
| Planner v3 | keep-best, but **reject-on-any-worse-vote** gate | **0 accepted**; also a read→write **prompt-corruption bug** + `args` didn't propagate (re-ran planner instead of writer) |
| Writer v1 | keep-best + **consensus-regression** gate + schema I/O | **Clean** — 2 accepted / 5 rejected, no corruption, stayed lean |

Only the last design behaved correctly. The progression is itself the lesson: each
fix exposed the next flaw.

---

## 2. Lessons learned (transferable)

- **Single-LLM graders inflate.** v1 gave 5/5/5/5 on a merely-competent plan.
  *Fix:* an **anchored rubric** ("a competent survey is a 3, reserve 4–5 for genuinely
  Carlin-level"), **critique-first** (write the failure case before scoring), and an
  **adversarial panel** (purist + skeptic).
- **Forward-editing accepts regressions.** v2 shipped an edit that raised one axis and
  silently lowered another. *Fix:* a **keep-best hill-climb** — the champion only moves
  uphill; a candidate must be evaluated *against* it, not just edited in.
- **A too-strict gate rejects good edits.** v3's "reject if *any* judge calls *any* axis
  worse" killed edits that both judges rated improved, because with 6 axes × 2 judges the
  odds of one noisy "worse" vote are high, and any additive edit slightly trades
  brevity. *Fix:* a **consensus-regression gate** — reject only when *both* judges agree
  an axis regressed (tolerates single-vote noise).
- **Comparative blind A/B beats absolute 1–5.** Fresh reviewers re-anchor each round, so
  absolute scores drift (a "4" then a "3" can be the grader moving, not the artifact).
  Judging *candidate vs. champion, blind*, removes the drift and needs no stable scale.
- **Single samples are noisy.** One generated plan per round conflates edit-effect with
  sampling variance. *Fix:* evaluate over **multiple briefs/samples** (we used two
  subjects) and require the verdict to hold on both.
- **LLM read→write roundtrips silently corrupt files.** An agent asked to "return the
  file contents" prepended a chatty preamble that then got written back into the live
  prompt. *Fix:* **schema-constrained prompt I/O** (text travels only in a typed
  `prompt` field) and **always diff-verify** after any agent touches a file.
- **LLM meta-reviews are unreliable self-reports.** We caught **three** false claims by
  diffing ("byte-identical" twice, "file writes blocked" once — all wrong). *Rule:* never
  trust an agent's report of its own file effects; verify with `diff`/`wc`/`head`.
- **Root-cause tagging prevents over-editing.** Tagging each issue *this-prompt /
  other-role / brief / model* stops the loop from cramming another role's job (or the
  brief's) into the prompt, and keeps it lean.
- **Convergent finding — placement, not wording.** *Both* loops independently stalled on
  the same axes: **texture / named human anchors / source-wrestling / immersion**. The
  planner loop rejected trying to *legislate* them (over-restriction); the writer loop
  rejected trying to *execute* them everywhere (regression). Two independent loops
  agreeing makes this well-supported: it is a **placement/allocation** problem — *where*
  a tracked anchor or a source-wrestling stretch belongs is a plan/brief decision, not
  something either prompt's wording can fix.
- **These loops are expensive.** Individual runs cost hundreds of thousands to ~1.4M
  output tokens; a single mis-parameterized run (the `args` bug) wasted ~800k on a
  duplicate. **Cost-aware design is a first-class requirement**, not an afterthought.

---

## 3. Where the prompts ended

- **`planner.md`** — lean (~33 lines), one directive per craft-§A axis (driving
  question, dwell/compress, finale-narrows, seams, texture *allocation*, coverage
  integrity). No per-domain hardcoding.
- **`writer.md`** — ~50 lines; gained two accepted bullets: an **unresolved moral
  question** ("make the listener feel its weight rather than answering it") and **one
  voice / scaffolding phrases** ("hold that thought," "more on that later").
- Both are **lean and general**, and **wording-only refinement has hit diminishing
  returns** — the remaining gains are structural (see §4c) or need real-audio ground
  truth, not more grading of text.

---

## 4. Proposed next optimization research — **DO NOT RUN AS-IS**

A larger, higher-signal effort to refine before committing. Goal: escape single-source
overfit and local optima; get signal that generalizes.

**(a) Multiple Carlin subjects.** Analyze several Hardcore History series (e.g.,
*Supernova in the East*, *Blueprint for Armageddon*, *Wrath of the Khans*, *Death
Throes of the Republic*) to (i) broaden `carlin-craft.md` beyond one show's tics and
(ii) mint **multiple held-out test topics**. Refine on some, validate on others never
seen during refinement.

**(b) Force diverse generation methods.** Make the planner/writer produce
**deliberately different** candidates — varied organizing principles, different episode
counts, higher temperature, "generate 3 unlike approaches then pick" — so the optimizer
searches a wider field instead of polishing one local optimum. Judge across the
diversity, not a single style.

**(c) Structural placement/allocation (the §2 convergent fix).** Add a per-episode
**allocation**: the planner names, per episode/beat, the *tracked human anchor* and the
*contested points* to wrestle; the per-episode **brief** carries them. Then the writer's
existing (already-good) bullets fire *on cue* instead of everywhere. This is likely the
single highest-leverage change and does not need a loop to validate first.
**Update (2026-07): the *sourcing* half is now shipped** — `planner.md` finds
per-episode anecdotes/anchors (web-verified) as raw material, and the planner runner
allows WebSearch/WebFetch. The remaining, now-critical piece is the **writer-brief
plumbing**: the anecdotes live in the planner's outline, but `prosodia write` still
builds the brief from `series.yaml` only, so they don't yet reach the writer. Wire that
next — it's the step that makes the whole division actually function end-to-end.

**(d) Evaluation upgrades.** Held-out topics (above); a **human calibration checkpoint**
(you rate ~1 artifact/run so we can detect grader drift against a human anchor); and
ideally **close the loop on produced audio** — the real ground truth these text-graders
only approximate — once GPU rendering is available again.

**(e) Cost controls (mandatory).** Generate with a **cheaper model**, reserve the
expensive model for judging only; **hard token/round budget caps**; **fewer, higher-signal
rounds**; cache/reuse artifacts; and dedicated per-role scripts (avoid the `args`
footgun). Assume a serious run is **multi-million tokens** — scope it deliberately.

**(f) Anecdote veracity & sourcing (new — from the 2026-07 planner change; validated on EU).**
A test run of the updated planner produced an 8-episode EU plan with per-episode,
web-sourced anecdotes, each cited; it flagged uncertain items *inline* and *dropped* two
it could not verify (the anti-fabrication behavior working). What that surfaced for the cycle:
- **Veracity must become a first-class eval axis.** The planner *asserting* a source is not
  proof the source is real or supports the claim. Add an independent **fact-check pass** (a
  separate agent/tool that re-verifies each anecdote + source) and score anecdote *accuracy*
  and *vividness*. Hallucinated or misattributed sources are the top risk of this feature.
- **The mandatory per-episode "sources conflict" line over-constrains.** Episodes without a
  natural factual dispute got a *historiographical/interpretive* debate instead. Soften to
  "where one naturally exists," and explicitly allow interpretive debates — don't force a
  factual clash that isn't there.
- **"Exactly one episode" vs. seams plant/payoff conflict.** Maastricht had to be marked
  "shared (set up in Ep 7, delivered in Ep 8)." The rubric should treat an *explicit*
  set-up→pay-off as legitimate seam-work, not a coverage-overlap failure.
- **WHAT-vs-execution grey zone.** A verbatim quote is sometimes the *fact* itself; the prompt
  should state that quotes-as-facts are acceptable raw material (placement still the writer's).
- **Web-tool dependency & fetch robustness.** The planner needs WebSearch/WebFetch actually
  granted, and external sources can fail (a Thatcher Foundation page 403'd mid-run). Plan for
  fallbacks and a "flagged — needs a second source" state.
- **Plans got denser.** Richer per-episode texture makes a plan harder to skim; the new
  `prosodia plan-view` HTML review page is the intended mitigation for the human check.

**(g) Repetition / freshness — emergent tics & a generality test (new, 2026-07; from the EU ep4–8 rewrite).**
The named opener/tic problem was addressed with three shipped pieces: `writer.md` FRESHNESS
rules, a deterministic **repetition linter** (`author/repetition.py` + `prosodia
lint-repetition`), and **feed-forward** (prior episodes' openings/phrases injected into each
writer brief). EU ep4–8 then came back with the headline problem solved — distinct openings,
zero watchlist tics — but with NEW, subtler convergences the writers drifted onto independently:
- "the men who built it" (ep5–8), "I am (not) going to…" (ep6–8), "both readings are alive"
  (ep4,5,8), plus a per-episode over-reached metaphor or two.
Key caveat (user, and confirmed in practice): **some of these are intentional rhetorical
devices, not tics** — e.g. "over the heads of the people" *is* the series thesis; a reviser
found the editor had **over-counted** several flagged repeats. So repetition findings must be
**judged intentional-vs-oversight**, never auto-stripped.
**Open question before generalizing:** are these tics topic-specific or general model habits?
**Do NOT bake them into `writer.md`/the linter watchlist yet.** Test first: run a short
diagnostic series on a deliberately different topic — chosen: **"great political thinkers
through history and the circumstances that shaped them"** (character/idea-driven, a contrast
to institutional history) — through the same pipeline on the *current* prompts, then
lint/review for the same patterns. Recur → general → add to FRESHNESS + `STOCK_PHRASES`;
absent → they were artifacts of the EU topic. **Deferred by the user to a future cycle** (the
linter + feed-forward are already built; only the diagnostic run remains).

**Open questions for the user to decide first:**
1. Which/how many Carlin series to ingest, and which topics are refinement vs. held-out?
2. Do we build (c) — the allocation field — *before* the loop (likely yes; it's cheap and structural)?
3. Is a human-in-the-loop calibration checkpoint acceptable (adds latency, big quality gain)?
4. Do we gate the whole effort behind at least one **rendered-audio** evaluation, so we're optimizing against real output, not text proxies?
5. Budget ceiling per run, and cheap-vs-expensive model split.
6. How do we fact-check anecdote veracity — a dedicated verification agent/tool — and do we gate a plan on it before it can proceed to writing?

**Cost caveat:** this is a high-cost effort (plausibly several million output tokens);
do not launch without a budget cap and the decisions above settled.

---

## 5. Reusable assets

- **[`carlin-craft.md`](carlin-craft.md)** — the craft gold standard (§A plan-level, §B
  prose-level), distilled from *Supernova in the East* I–VI so we never re-ingest.
- **`experiments/loops/refine_role.workflow.js`** — the keep-best comparative optimizer,
  now with **schema-constrained prompt I/O** and the **consensus-regression gate**; role
  is set by a top-of-file constant (the `args` global did not propagate to scriptPath
  runs). Lives under the gitignored `experiments/` tree — treat as experimental scaffolding, not shipped code.
