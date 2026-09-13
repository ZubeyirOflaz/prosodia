# Harford craft reference

Distilled from **Cautionary Tales** (Pushkin Industries) by **Tim Harford**, per the process in
[`craft-sourcing.md`](craft-sourcing.md). Sections are named for the persona file they feed.
Confidence labels: `[Observed]` (quoted in §I), `[Inferred]` (pattern, no single quote),
`[Unverified]` (secondary — resolve before synthesis).

> **Self-contained by rule.** This dossier describes one person. It makes no comparison to
> another source and no decision about which persona will use what — those belong to synthesis.

> **Pass 2 of 3.** Pass 1 read three episodes closely. Pass 2 extended the corpus to **seven**
> and re-ran every structural claim over all of them — see **§J**. It **falsified three pass-1
> claims**, every one a generalisation from the single episode I had read most closely, and
> strengthened four others. The frequencies below are the seven-episode ones.

> ⚠ **Attribution caveat, applies to every excerpt.** Cautionary Tales is **not single-voice**.
> It uses actors to dramatise scenes — the credits name Ben Crow, Melanie Gutteridge, Gemma
> Saunders, Rufus Wright, and in one series Helena Bonham Carter and Jeffrey Wright — plus sound
> design and original music by Pascal Wise. A transcript cannot reliably separate Harford's
> narration from dramatised dialogue, so **some lines in this corpus are not his**. Excerpts
> below were chosen from passages that are clearly narration, but the boundary is not
> machine-verifiable. Scripts are also co-written with Andrew Wright and edited by Julia Barton.

---

## §0 Source card

| | |
|---|---|
| **Person** | Tim Harford — economist and journalist; the *Financial Times*'s Undercover Economist; presenter of *Cautionary Tales* and BBC Radio 4's *More or Less* |
| **Corpus** | **7 episodes, 263 minutes, 32,968 words**, transcribed locally. Narrative bodies (credits and the spoken source list removed) run **~4,543 words each**, tightly clustered (4,309–4,818) |
| **Why local transcription** | **No transcripts of his work exist.** Verified: the real Cautionary Tales feed (265 episodes, found via the Apple lookup API) carries no `podcast:transcript` tags, nor does the BBC feed for *50 Things* (110 episodes); the YouTube uploads offer auto-captions only, at **0.17** sentence terminators per 100 words, rendering "Irving Langmuir" as "moving langmuir" |
| **Transcript quality** | `transcribe.py` with faster-whisper `small`: **6.61–8.81** marks per 100 words, proper nouns correct. Residual errors are in the credits, where the show's own name comes out as "Chinary Tales" and "Caution Retails" — so quotations are good but worth checking against audio before publication |
| **Not obtained** | The other 258 Cautionary Tales episodes; *50 Things*; his books, which are the same craft in print; his FT columns (his site's category pages returned no article links to a scripted request) |
| **Acquisition** | `transcribe.py harford --ids …`, 2026-09-10 |
| **Permission** | Audio transcribed locally for private style analysis, not redistributed. Raw corpus gitignored and uncommitted |

**Role: content and device source, hired for cases.** The bar is a corpus that evidences how he
builds one. Seven complete cases support the narrative-craft claims below; the claims about how
he handles a *thesis* proved to need more than seven, and are marked accordingly.

## §1 Hired for

**Cases** — how a real, documented episode is opened, turned, and made to yield a transferable
lesson. He states the show's own thesis structure inside an episode: "this tale, **like all our
tales, is about the lessons we can learn**." `[Observed §I-1]`

---

## §A Plan-level craft — feeds `roles/planner.md`

1. **One episode is one case.** ~37 minutes, ~4,700 narrative words. `[Observed §I-8]`
2. **He does *not* systematically declare the lesson — pass 1 got this wrong.** Only **2 of 7**
   episodes contain an explicit lesson marker at all, and in one of those it falls at **86%** of
   the body. The Shipman episode's declaration at 17% — "Here, the lesson is that Harold Shipman
   could have been caught much earlier" — is a real move but **not the house pattern**, and pass 1
   generalised it from the one episode it had read most closely. Elsewhere the lesson is carried
   by the shape of the story and by the ending. `[Observed §I-1; corrected §J-1]`
3. **Ruling out the obvious framing is occasional, not habitual — 2 of 7.** Where it happens it
   is emphatic: "I'm not trying to pick apart Harold Shipman's psychology. No, this tale… is
   about the lessons we can learn." `[Observed §I-1; corrected §J-2]`
4. **The lesson comes from a different discipline than the story.** A serial-killer case is
   resolved by industrial statistics — "production line mathematics designed to inspect condoms
   and chocolate chip cookies". The case supplies the drama; the analytic frame is imported.
   `[Observed §I-2]`
5. **Sources are read aloud at the end, as a spoken bibliography, before the credits — 7 of 7,
   the only structural element that is genuinely universal in this corpus.**
   "Essential sources on Shipman's crimes are the Shipman Inquiry and Brian Whittle and Gene
   Rich's book, *Prescription for Murder*. David Spiegelhalter's excellent book *The Art of
   Statistics* covers the Shipman case. In my own book, *The Data Detective*… Other sources are
   at timharford.com." He names his own book among them, and points to a written list.
   `[Observed §I-3]`

## §B Prose-level craft — feeds `roles/writer.md`

1. **Cold open on a named person in a placed scene — 6 of 7.** "On the 21st of August 1974,
   Elaine Oswald made a visit to the doctor's office in a small town not far from Manchester." ·
   "Irving Langmuir stood in the control tower at the airport at Schenectady, upstate New York." ·
   "Air New Zealand Flight 901 is flying straight towards a mountain. 257 people are on board." An
   explicit date or weekday lands within the first two sentences in **4 of 7**; the others place
   the scene without one. **The seventh opens on the show's own mission instead** — the exception
   worth knowing: "As the night draws in and the fire blazes on the hearth, we warn the children
   by telling them stories. The Hobbit teaches them not to leave the path, but **my stories are
   for the education of the grown-ups**." `[Observed §I-4, §I-14; refined §J-3]`
2. **Sensory or period-placing detail in the opening — usually, not always.** "spectacles and
   the kind of big brown beard that was fashionable at the time"; "a cold and crisp November
   morning, barely above freezing"; "strapped into his X2 sky cycle with its star-spangled paint
   job". A crude word-list proxy finds such detail in the first 1,200 characters of **5 of 7**
   episodes, so it is a strong tendency rather than a rule — and the measure is coarse enough that
   this should be treated as provisional. `[Observed §I-4; qualified §J-10]`
3. **A hinge planted in the opening, and very short sentences used as pivots throughout — that
   habit is universal.** Either a one-word pivot — "with an almost completely clear blue sky.
   **Almost.**" — or a line whose menace only becomes visible later: "Leave your door unlocked, he
   said." Counting very short standalone sentences across the corpus finds them in **7 of 7**
   episodes, median **3 per episode**, so this is a deliberate rhythmic device rather than an
   occasional flourish. `[Observed §I-5; verified §J-11]`
4. **Where the show identification appears, it is always *after* the hook — never at the top.**
   Present in **5 of 7**, and in every case between **7% and 11%** of the way in: "…couldn't have
   been more wrong. I'm Tim Harford, and you're listening to Cautionary Tales." The listener is
   inside the story before being told what they are listening to. `[Observed §I-6; verified §J-4]`
5. **The counterfactual is a device he reaches for, not a signature — pass 1 overstated it.**
   Across seven episodes the median is **0.9 per 1,000 words**, the range 0.0–4.2, and **one
   episode contains none at all**. Pass 1's 1.6 was inflated by the Shipman episode, the outlier
   at 4.2. Where he does use it, it carries the moral weight: "he could have been caught early
   enough to have saved more than a hundred lives." `[Observed §I-2; corrected §J-5]`
6. **A two-option question put to the listener, then answered — occasional, 4 of 7.** "Which of
   the following do you think is more probable? A: Jeff is now a Hollywood movie star. Or B: Jeff
   is now an accountant. Intuitively, Jeff sounds like a movie star. But that's not right." Six
   instances across seven episodes. `[Observed §I-9; qualified §J-12]`
7. **Short sentences, a third of them very short — the most stable finding in the corpus.**
   Sentence median **12.0** across seven episodes (per-episode range 10–14), with **33%** running
   to eight words or fewer (range 26–42%). `[Observed §I-8; verified §J-6]`
8. **"But" is the workhorse pivot — 269 uses, 8.2 per 1,000 words — against "however" twice in
   32,940 words.** About 134 to 1. The turn is essentially always the plain conjunction.
   `[Observed §I-10; verified §J-7]`
9. **He rarely asks the listener to imagine.** "Imagine" appears 9 times and "picture" twice in
   32,940 words (0.27 and 0.06 per 1,000); he supplies the scene rather than requesting one.
   `[Observed §I-10; verified §J-7]`
10. **His own curiosity as a pivot — one instance in the whole corpus.** "But what fascinates me
    is the lesson the authors draw." Pass 1 listed this as a device on the strength of that single
    occurrence; seven episodes turn up no others, so it is **not** a habit and should not be
    carried forward as one. `[Observed §I-11; corrected §J-13]`
11. **Endings make the lesson consequential and never summarise — 0 of 7** contain a summary
    marker in the closing passage. Often an antithesis or a wry reversal: "It won't be
    aspiration, but desperation." · Scrooge's real gift: "Money. That's the Christmas spirit. God
    bless us. Everyone." `[Observed §I-12; verified §J-8]`

## §C Delivery craft — feeds `roles/tone.md`

- **Pace ~127 words per minute** (from caption timings on a 37.9-minute episode) — slower than
  his sentence length alone would suggest, because the production leaves room. `[Observed §I-8]`
- **Address is balanced and light**: "you" 6.7, "we" 6.4, "I" 4.7 per 1,000 words; questions end
  5.8% of sentences. `[Observed §I-10]`
- **Delivery is not separable from production.** Music, sound design and dramatised scenes are
  load-bearing in the finished artefact; what a transcript shows is the script, not the
  experience. Any claim about his *voice* from this corpus is weak. `[Inferred]`
- Humour is present and dry, and it lands at endings rather than through an episode.
  `[Observed §I-12]` / `[Inferred]` as to distribution.

## §D Delivery profile — feeds `voice_profiles.yaml`

| metric | value | note |
|---|---|---|
| `speech_rate_wpm` | **127** | one episode measured from caption timings |
| unit length | **~37 min**, ~4,700 narrative words | credits and spoken sources excluded |
| `sent_len_mean` / `median` | **13.7 / 12** | narrative bodies, 3 episodes |
| `short_sent_frac` (≤8 w) | **0.32** | |
| `question_rate` | 0.058 | |
| `punctuation_density` | 7.0–8.04 | whisper `small`, per episode |
| `you` / `we` / `I` per 1k | 6.7 / 6.4 / 4.7 | |
| `f0_sd_st`, `arousal_std` | — | not measured; needs audio analysis |

## §E Standards — what he would reject — feeds `roles/editor.md`

No written account of his method was obtained, so this rests on the corpus.

1. **A case that yields no transferable lesson.** His own framing: "my stories are for the
   education of the grown-ups", and the tales are "about the lessons we can learn" — though the
   lesson is usually *carried* rather than *stated* (§A-2). `[Observed §I-1, §I-14]`
2. **Psychologising the villain instead of finding the systemic failure.** Explicitly refused
   where that temptation is strongest, though not a stated rule across the corpus.
   `[Observed §I-1]`
3. **An unsourced claim.** Sources are named aloud and listed in writing. `[Observed §I-3]`
4. **A summary ending.** None of the three ends by restating; each ends on a consequence.
   `[Observed §I-12]`
5. **Announcing the topic before the story.** No episode opens on its subject. `[Observed §I-4]`

## §F Defaults — feeds `persona.yaml`

- Unit ≈ 37 minutes / ~4,700 spoken words of narrative. `[Observed]`
- **Not single-voice**: one narrator plus dramatising actors, plus music and sound design.
  `[Observed §I-13]`
- Co-written and separately edited, so the corpus is a team's script, not one person's prose —
  worth holding in mind before attributing any habit to him alone. `[Observed §I-13]`

## §G Transfer & exclusions

**Converts directly to single-narrator audio:** the cold open on a named person at a dated
moment; sensory specificity in the first thirty seconds; the planted hinge and the very short
pivot sentence; the frame arriving *after* the hook; declaring the lesson early and then
demonstrating it; ruling out the obvious-but-wrong framing; the counterfactual as the carrier of
the lesson; the two-option question answered on the spot; short sentences with a third very
short; "but" instead of "however"; the spoken bibliography; the consequential ending.

**Needs conversion:** everything the production does. Dramatised scenes voiced by actors, music
and sound design cannot be reproduced by a single synthesised narrator, and in the finished
artefact they carry a real share of the pacing and of the scene-setting his script leaves
implicit. A script written for this show and read by one voice would be thinner than the show
is, and the transcript does not show by how much. `[Inferred]`

**Do not import:** the credits; the show identification; the Pushkin house furniture generally.

**A tension worth flagging for synthesis, not resolving here.** Declaring the lesson at 17% works
because the material is a *story* whose outcome the listener may already half-know, so suspense
is not the engine — comprehension is. Whether that survives transplanting to material where the
listener's own uncertainty is the point is a question this corpus cannot answer, and it should be
decided against the persona's aim rather than assumed from his success. `[Inferred]`

## §H Candidate prompt lines

Nominations only; selection happens at synthesis.

1. `writer` — Open on a named person at a dated moment, with two or three physical details, and
   no statement of the topic.
2. `writer` — Plant a hinge in the opening whose meaning only becomes clear later, and let a
   very short sentence carry it.
3. `writer` — Put any framing — who you are, what this is — after the hook, never before it.
4. `writer` — Let the shape of the story and its ending carry the lesson; state it outright only
   where the obvious reading would otherwise win. *(Rewritten at pass 2 — the "declare it early"
   version rested on one episode and did not survive seven; see §J-1.)*
5. `writer` — Where a case invites a tempting wrong reading, name that reading and refuse it
   before offering your own.
6. `writer` — Where a failure had an avoidable cause, say what would have had to be different and
   what it would have been worth. *(Demoted at pass 2 from a signature to an available device;
   see §J-5.)*
7. `writer` — Where you want the listener to commit, offer two named options and then answer.
8. `writer` — Keep the median sentence near twelve words and let a third of them run under eight.
9. `writer` — Turn on "but"; never on "however".
10. `writer` — Supply the scene rather than asking the listener to imagine one.
10b. `writer` — Use a one- or two-word sentence as a pivot where the story turns; expect around
    three per episode, not one.
11. `writer` — End on the consequence, not a restatement.
12. `planner` — Read the sources aloud at the end, name your own among them, and point to a
    written list.

## §I Evidence

Locators are item slugs under `experiments/craft_sourcing/corpus/harford/`. All text is
locally transcribed audio; see the §0 caveats on attribution and residual errors.

1. **The show's own premise; the refused framing; the early lesson** —
   `catching-a-killer-doctor`, ~17% in: "I'm not trying to pick apart Harold Shipman's
   psychology. No, this tale, like all our tales, is about the lessons we can learn. Here, the
   lesson is that Harold Shipman could have been caught much earlier."
2. **Counterfactual carrying the lesson; the imported frame** — same episode, closing words: "If
   instead we had collected the simplest of datasets, if we had run the most basic analysis of
   that data, we would never have needed to depend on people risking the scorn of the police and
   the enmity of Harold Shipman to stop him. The statisticians, with their production line
   mathematics designed to inspect condoms and chocolate chip cookies, might have stopped his
   murder spree more than a decade earlier."
3. **Spoken bibliography** — same episode: "Essential sources on Shipman's crimes are the Shipman
   Inquiry and Brian Whittle and Gene Rich's book, *Prescription for Murder*. David
   Spiegelhalter's excellent book, *The Art of Statistics*, covers the Shipman case. In my own
   book, *The Data Detective*… Other sources are at timharford.com."
4. **Cold opens** — "On the 21st of August 1974, Elaine Oswald made a visit to the doctor's office
   in a small town not far from Manchester in the north of England… He had spectacles and the kind
   of big brown beard that was fashionable at the time." · "Irving Langmuir stood in the control
   tower at the airport at Schenectady, upstate New York… The year was 1946, a cold and crisp
   November morning, barely above freezing, with an almost completely clear blue sky." · "It was
   Friday the 13th, and some people would have expected bad luck. Suzy Hall didn't."
5. **The planted hinge** — "…with an almost completely clear blue sky. Almost." · "Leave your door
   unlocked, he said."
6. **Frame after hook** — `catching-a-killer-doctor`: "…couldn't have been more wrong. I'm Tim
   Harford, and you're listening to Cautionary Tales."
7. **Counterfactual frequency** — 23 matches for `might have|would have|could have|if instead|had
   (he|she|they|we)` across the three episodes, 1.6 per 1,000 words.
8. **Prose and pace** — narrative bodies: median 4,665 words; sentence mean 13.7, median 12.0;
   32% ≤8 words; questions 5.8%. Pace 127 wpm from caption timings on a 37.9-minute episode.
9. **Two-option question** — "Which of the following do you think is more probable. A. Jeff is now
   a Hollywood movie star. Or B. Jeff is now an accountant. Intuitively, Jeff sounds like a movie
   star. But that's not right."
10. **Connectives and address** — corpus counts across 14,568 words: "but " 110 (7.6/1k),
    "however" **0**, "of course" 10, "imagine" 4, "picture" 1; "you" 6.7, "we" 6.4, "I" 4.7 per
    1,000 words.
11. **Own curiosity as pivot** — `the-man-who-played-with-hurricanes`: "Thankfully it hasn't
    happened that fast. Not yet. But what fascinates me is the lesson the authors draw."
12. **Consequential endings** — "They had a touching faith in human ingenuity… And yet, we've left
    it so late that all that remains are a set of bad options. So if we try to remake the climate,
    we'll have a different motive. It won't be aspiration, but desperation." · "Finally, he gave
    Bob Cratchit the greatest Christmas gift of all. Money. That's the Christmas spirit. God bless
    us. Everyone."
13. **Not single-voice; a team's script** — credits across the three episodes: "written by me, Tim
    Harford, with Andrew Wright", "produced by Ryan Dilley" / "Alice Fiennes", "sound design and
    original music is the work of Pascal Wise", "Julia Barton edited the scripts", "It features
    the voice talents of Ben Crow, Melanie Gutteridge, Gemma Saunders and Rufus Wright", and in
    one series "Helena Bonham Carter and Jeffrey Wright".
14. **The show's mission, in the narrator's voice** — `how-britain-invented-then-ignored-blitzkrieg`,
    opening words: "As the night draws in and the fire blazes on the hearth, we warn the children
    by telling them stories. The Hobbit teaches them not to leave the path, but my stories are for
    the education of the grown-ups."

---

## §J Verification — pass 2

Corpus extended from three episodes to **seven** (32,968 words, 263 minutes), with every
structural claim re-counted across all of them.

| Claim | Test | Outcome |
|---|---|---|
| **§A-2** lesson declared early | First lesson marker per body, and its % position | **Falsified.** Present in only **2/7**, and at 86% in one of those |
| **§A-3** rules out the obvious framing | Refusal patterns per episode | **Downgraded** to occasional: **2/7** |
| **§B-1** cold open on a named person at a dated moment | First 330 characters of all 7 | **Refined.** Named person in a placed scene **6/7**; explicit date or weekday **4/7**; one episode opens on the show's mission |
| **§B-4** show ID after the hook | Identification position per episode | **Confirmed where present**: **5/7**, always 7–11% in, never at the top |
| **§B-5** counterfactual carries the lesson | Counts per 1,000 narrative words, per episode | **Falsified as a signature.** Median **0.9/1k**, range 0.0–4.2, **one episode has none** |
| **§B-7** short sentences | Sentence stats per episode | **Confirmed, the most stable finding here**: median 12.0 (10–14), 33% ≤8 words (26–42%) |
| **§B-8 / §B-9** connectives | Whole-corpus counts | **Strengthened**: "but" 269 against "however" 2 (≈134:1); "imagine" 9, "picture" 2 in 32,940 words |
| **§B-11** endings never summarise | Summary markers in closing passages | **Confirmed: 0/7** |
| **§A-5** spoken sources | Source-block detection | **Confirmed universal: 7/7** — the only element that is |

**The lesson of this pass is about the process, not about him.** All three falsified claims came
from the same source: the episode I read first and most closely. Close reading of a single item
produces claims that feel structural and are not, and the error is invisible from inside the
reading — it took counts over four more episodes to surface it. Note also how unevenly the
evidence requirement falls: the narrative-craft habits recur in every episode and settled almost
immediately, while the thesis-level claims are still unsettled at seven.

## §J Verification — pass 3

Pass 3 tested the four prose moves pass 1 had asserted but never counted. One held emphatically;
three were overstated. All four had come from close reading rather than measurement.

| Claim | Test | Outcome |
|---|---|---|
| **§B-3** very short pivot sentences | Counted standalone one- and two-word sentences in all 7 | **Confirmed and promoted**: present in **7/7**, median 3 per episode. A deliberate rhythmic device |
| **§B-2** sensory detail in the opening | Word-list proxy over the first 1,200 characters of all 7 | **Qualified**: **5/7**. A tendency, not a rule — and the proxy is crude, so provisional |
| **§B-6** two-option question | Pattern count across all 7 | **Qualified**: **4/7**, six instances. Occasional device |
| **§B-10** own curiosity as pivot | Pattern count across all 7 | **Corrected**: **1/7** — a single instance in 33,000 words. Not a habit; withdrawn as a device |

Question marks run at a median of **4.4 per 1,000 words**.

**Status: Harford is complete at pass 3 of 3.** Every claim in §A and §B has now been counted
across the seven-episode corpus. What a larger corpus would still change is the thesis-level
question left open at pass 2 — whether he has any systematic way of siting a lesson — which
remains unsettled and is marked as such in §A-2. It is a question about him, not a gap in the
method.
