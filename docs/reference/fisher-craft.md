# Fisher craft reference

Distilled from the **CopyrightX** corpus of **William W. Fisher III** (Harvard Law), per the
process in [`craft-sourcing.md`](craft-sourcing.md). Sections are named for the persona file
they feed. Confidence labels: `[Observed]` (quoted in §I), `[Inferred]` (pattern, no single
quote), `[Unverified]` (secondary — must be resolved before synthesis).

> **Self-contained by rule.** This dossier describes one person. It makes no comparison to
> another source and no decision about which persona will use what — those belong to the
> synthesis stage, so that any source can be re-analysed or dropped without touching the
> others.

> **Pass 4 of 6 — a verification pass.** Pass 1 surveyed the 40 segments; pass 2 read his written
> account of the course design (correcting §B-13 and §A-2); pass 3 read his 2020 examination
> (closing §E, adding §B-16). **Pass 4 tested every structural claim mechanically against all 40
> segments** rather than the sampled ones — see **§J**. It confirmed six claims with frequency
> data, materially strengthened the §G warning, **falsified one claim** and **softened another**.
>
> This is *verification by the same reader*, not the `≥2 independent analysts` corroboration the
> process specifies — that needs readers blind to each other. What a full-corpus mechanical check
> does address is the same underlying risk, from the other direction: a claim generalised from a
> handful of sampled segments now has to survive a count over every one of them. Two did not.

---

## §0 Source card

| | |
|---|---|
| **Person** | William W. Fisher III ("Terry Fisher"), WilmerHale Professor of Intellectual Property Law, Harvard Law School |
| **Lecture corpus** | 40 segments, **≈17 h**, **141,164 words** of human-punctuated captions (density 5.2 marks/100 words); auto-caption tracks with inline word timings for all 40 |
| **Reliable prose subset** | **38 of 40 segments · 970 min.** Segments 13 (*Visual and Architectural Works*) and 31 (*Other Approaches*) fall below the punctuation gate and are excluded from all sentence statistics |
| **Self-description (read in full, pass 2)** | *Lessons from CopyrightX* (2015, 8,617 words) — delivered as the Peter Jaszi Distinguished Lecture and written partly "to provide some guidance to teachers considering similar projects" |
| **Also read (pass 3)** | CopyrightX final exam, Spring 2020 (6,400 words) — open-book, two questions, 2,000 words each, seven weeks |
| **Also obtained** | Lecture index; 2013 syllabus; "Maps of Intellectual Property" page |
| **Not obtained** | Audio (no pitch/energy metrics); the *Illustrations* sets; the residential Harvard classes; the teaching-fellow seminars; the case-study library and its teaching manuals |
| **Acquisition** | `fetch.py sources/fisher.json` — subtitles only, never video; PDFs via curl + pdftotext. 2026-09-10 |
| **Permission** | Originally CC BY-NC-SA; he **relaxed it to attribution-only**, persuaded by Richard Stallman, expressly to "maximize the number and variety of educational projects and **derivative works** that can be built (directly or indirectly) on our foundation." `[Observed §I-21]` Raw corpus stays gitignored and uncommitted regardless |

**Gate 0: passes all four.** Obtainable · single voice · designed (twelve-week HarvardX
course, annual since 2013, six lectures since substantially revised) · **self-described**.

**Measured outcomes** — unusual for a craft source, and worth recording because they mean
the design is not merely admired: Harvard "overall effectiveness" 4.66 and 4.64 of 5; online
course 4.57. Retention 74–80% first-to-last seminar; **40–41% full completion including a
passed exam, against a ~7% MOOC average**. Highest-rated single component was **the maps
(4.40, then 4.76)** — above the lectures and the case studies. Lowest by far was the
asynchronous discussion forum (2.91, then 2.42), which he reports repeatedly failing to fix.
`[Observed §I-22]`

## §1 Hired for

**Architecture** — how an intricate legal apparatus is decomposed into teachable parts,
sequenced across a series, and interleaved with the lenses used to judge it.

His own statement of the course's third objective is the closest thing in the corpus to a
purpose statement: **"Cultivate Wise Practice"** — that a participant, on later meeting a real
dispute, draws on both an informed judgment about what the system is *for* and a practised
skill at working out which resolution advances it. He is explicit that the second "can be
acquired only through practice", which is why real case studies carry so much of the course.
`[Observed §I-23]`

---

## §A Plan-level craft — feeds `roles/planner.md`

1. **The unit is a segment, not a lecture.** Twelve 90-minute lectures are published as **40
   individually-titled segments**, median **27.3 min** (range 8–43.5), median **3,614 words**
   — most lectures being exactly three. `[Observed §I-1]`
2. **Nine doctrinal lectures, three theory lectures — his own count.** "Nine of the 12
   lectures consist of surveys of the principal sets of rules in copyright law; the other three
   present the main theories upon which scholars (and sometimes lawmakers) rely when shaping
   or evaluating the copyright system." The three are *Fairness and Personality Theories*
   (2nd), *Welfare Theory* (4th), *Cultural Theory* (10th). `[Observed §I-2]`
   *(Pass 1 said "four of twelve" — a miscount, corrected here from his own text.)*
3. **He calls the pattern oscillation.** "The weekly lectures **oscillate** between doctrine
   and theory." It is a stated design principle, not an accident of ordering: every stretch of
   machinery is followed by a lens for judging it. `[Observed §I-24]`
4. **The oscillation is announced in both directions, with the episode number attached.** "In
   the 3rd lecture, we will return to legal doctrine." "In the 10th lecture, we will return for
   the last time to copyright theory." `[Observed §I-3]`
5. **A three-level model of what understanding requires.** "Understanding law requires much
   more than memorizing a collection of rules. It also demands, at a minimum, securing a
   critical understanding of the theories that either animate those rules or could be used to
   change them and acquiring an appreciation of how the rules influence behavior and the
   capacity to predict how they have been (or would be) applied to real controversies."
   Doctrine, theory, and practice, each with its own channel in the course. `[Observed §I-24]`
6. **His own view is withheld until the tenth of twelve lectures, on purpose.** "I do not
   attempt in the lectures, or in my teaching, to resolve that disagreement. Rather, I strive to
   inform students and viewers what the principal contentions are… (**Partly to afford them
   room to reflect, I wait until the tenth lecture to present my own perspective** on the most
   attractive conception of those functions.)" Judgment is a *series-level* placement decision
   with a stated reason. `[Observed §I-25]`
7. **Illustrations are scheduled, not sprinkled.** Each doctrinal group carries a separate
   *Illustrations* item alongside its segments. `[Observed §I-4]`
8. **Position-in-the-arc opening.** Every lecture-opening segment states its index, where it
   sits in the whole, and what the listener should already hold. `[Observed §I-5]`
9. **Omission is stated aloud.** "The history of the negotiations that resulted in the TRIPS
   agreement is intricate — much too intricate to be explored here." `[Observed §I-6]`
10. **For intricate material the goal is a map, not retention.** "Rather my goal has been to
    convey to you the key principles and trends — and to **mark the locations** of the treaty
    provisions to which we will return when examining specific features of copyright law."
    `[Observed §I-7]`
11. **The finale places the listener inside an unfinished project** rather than summarising.
    `[Observed §I-8]`

## §B Prose-level craft — feeds `roles/writer.md`

The canonical order of moves, with handles.

1. **The frame, and where it actually lands.** "Hello. I'm Terry Fisher. This is the Nth of 12
   lectures on copyright." **All twelve lecture-opening segments carry it, and the ordinal is
   always stated — 12 of 12.** But two of the 28 interior segments use it too (segments 15 and
   27), where it announces the segment's place *within* its lecture instead of the lecture's
   place in the series. So the frame marks a boundary and states a position; the boundary is
   usually, not always, a lecture. `[Observed §I-5, §I-9; verified §J-1 — the "interior segments
   do not use it" half of this claim was falsified]`
2. **Position + inventory — in about two-thirds of segments, not all.** 27 of 40 locate
   themselves in their opening sentences: the index, the place in the arc, what the listener
   already holds, what today adds. The other 13 **open cold on material** instead — a named case,
   a primary document, a doctrine stated flat. Both are real patterns and the choice between them
   is not random: the cold opens cluster in the interior of a lecture. `[Verified §J-2]`
3. **Cold open on a document** — interior segments open on primary material and quote it: "In
   1783, the author Joel Barlow wrote a letter to the Continental Congress… Here's the heart of
   his letter." `[Observed §I-9]`
4. **The warning, and the deferral** — difficulty named and retention stakes lowered in the
   same breath: "A WORD OF WARNING: This material is intricate. You are unlikely to retain all
   of it right now." Plus eight instances of "For the time being, you need to know only that…".
   `[Observed §I-10]`
5. **The spiral promise** — 15 instances of "we will return to…", usually with a lecture
   number, so the deferral is a commitment rather than a dodge. `[Observed §I-3]`
6. **Simplest true statement, then the exception flagged** — "Each country in the world
   creates, interprets, and enforces its own copyright laws. With minor exceptions that we'll
   consider in a minute…" `[Observed §I-11]`
7. **The restatement** — "in other words," is his **most frequent sentence opener (75×)**: a
   plain-language paraphrase immediately after a technical formulation. Variant: "To put the
   same point another way." `[Observed §I-12]`
8. **The micro-hypothetical — one short sentence, with a tail.** 51 instances corpus-wide; the
   median runs **17 words**, and they are concrete and often absurd in a clarifying way:
   "Suppose that you make a perfect replica of The Thinker." But six of the 51 run past 40 words
   and one reaches 124, so "never elaborate" would be too strong — the *typical* hypothetical is
   a single varied fact, not the only kind. A distinct instrument from his case studies (§B-16).
   `[Observed §I-13; verified §J-4]`
9. **Backward reference by name** — "You'll recall, I…" (14×), "As we've seen," (12×). He
   re-anchors rather than assuming retention. `[Observed §I-14]`
10. **Concession then turn** — "To be sure," (16×). `[Observed §I-14]`
11. **Indeterminacy admitted flatly** — "More guidance than that may be impossible."
    "Application of the doctrine is thus very hard to predict in advance." The limits of the
    doctrine are content, not apology. `[Observed §I-15]`
12. **Own view marked as his own, when it comes** — "in my view, it doesn't hold up." "My own
    view is no." Eight instances, and see §A-6 on their placement. `[Observed §I-16]`
13. **He separates exposition from interrogation by channel — this is a design decision, not
    a temperament.** Pass 1 concluded from a 3% question rate that he is "an architect, not a
    Socratic interrogator." His own account corrects that: **"During the two live classes, I
    don't lecture at all, and I rarely focus on the assigned materials. Instead, I engage the
    students in Socratic discussions of case studies."** So the recorded lecture is
    *deliberately* expository and near-questionless, because the questioning has a different
    channel. Two instruments, cleanly split. `[Observed §I-17]`
14. **Closing = a substantive last point plus a forward handoff, never a summary** — "In the
    last segment of this lecture, I'll discuss a few applications and refinements of the
    welfare approach and then **step back from the details and ask you, through these
    lenses**, what are the strengths and weaknesses of copyright." `[Observed §I-18]`
15. **Signature move — the apparatus is a machine, and is taught as one.** "…the way in which
    the **machinery** of the copyright system works in practice." "The machinery of the
    copyright system is intricate, surprisingly so." "These three features surely do not
    exhaust the set of important aspects of the **copyright machine**." `[Observed §I-19]`
16. **Three distinct case instruments, never confused with one another.** `[Observed §I-17,
    §I-23, §I-31]`
    - **Class case studies — real, never invented.** "All of the case studies examine **real
      (not hypothetical)** controversies. In form, they more closely resemble the kinds of case
      studies used in business schools than the cases typically employed in law schools." Each
      is a short summary, slides, and a ten-page teaching manual; the work is "examining how the
      participants in those controversies did or could have employed the law."
    - **In-lecture micro-hypotheticals** — one sentence, invented, obviously so (§B-8).
    - **Exam fact patterns — composites of real material, with the fictionalisation
      declared.** His 2020 question runs on real films, real named consultants, a real filter by
      a named creator and a real viral instance, then states in a bracketed note: "This question
      contains a fictionalized composite of several events. Most of the statements made in the
      question are true, but others are 'alternative facts'… If you happen to know… aspects of
      the actual events that are inconsistent with the narrative set forth above, you should
      ignore that knowledge." Constructed, and the construction is disclosed.
17. **He quotes the court inside his own sentence, attributed mid-clause — and glosses it for a
    non-lawyer as he goes.** "The Rocky character, 'has become identified,' says the court, 'with
    specific character traits ranging from his speaking mannerisms to his physical
    characteristics.'" · "the character was 'lifted lock, stock, and barrel from the prior Rocky
    movies'" · and inside a quotation of a congressional report: "'your committee' — **meaning
    your congressional committee** — 'felt that it should be the exclusive right of the author…'"
    The primary text and his explanation interleave rather than alternating in blocks.
    `[Observed §I-35]`
18. **He stacks complicating cases, then resolves them — and says "difficult to say" when it is.**
    On fictional characters he raises Superman, whose depiction shifts across comics, narrative
    and finally Christopher Reeve's face: "Which, if any of the Superman incarnations, thus enjoys
    copyright protection? **Difficult to say.**" Then: "Here's another complicating factor" — James
    Bond across six actors, where "tuxedos and a British accent can only go so far in obscuring
    the differences among these depictions." Only then the resolution: "Typically, no. Modern
    courts are quite forgiving of indeterminacy of these sorts." `[Observed §I-36]`
19. **He maintains the map aloud: naming kinship between doctrines, and saying which ones do not
    matter.** "This exclusion, you will probably notice, is a **cousin** of the Scenes A Faire
    doctrine, which we discussed in lecture number one." And immediately: "This exclusion doesn't
    much matter, however, because there's usually not much point in appropriating stock
    characters." Telling the listener what *not* to spend attention on is as deliberate as telling
    them what to learn. `[Observed §I-36]`
20. **He lands the doctrine on a practice the listener already knows, then points forward.** "A
    crucial implication of the protectability of fictional characters is that almost all **fan
    fiction**, which is increasingly common nowadays, is legally problematic. Now, I hasten to add
    that fan fiction may escape liability under one of the affirmative defenses to copyright
    infringement that we'll discuss in detail in lecture number nine." `[Observed §I-36]`
21. **He signals the return from a digression.** "So to return to the main line…" `[Observed §I-36]`
22. **He uses legislative history as evidence, points at the operative words, then paraphrases the
    intent in plain language.** "The House and Senate reports explaining the basis of that statute
    contained a passage that seemed to cast doubt on the validity of these assignments. Here it
    is. The crucial language is highlighted." — then, after the quotation: "In other words, the law
    was designed to protect authors from their own foolishness or vulnerability." `[Observed §I-37]`
23. **A doctrinal rule is taught through one dated human story with real money in it — and the
    artifact itself is played.** George Graff co-wrote "When Irish Eyes are Smiling" in 1912,
    assigned the first term for royalties, hit "financial difficulties", and sold his royalties and
    his renewal expectancy in that song and 68 others for **"a lump sum payment of $1,600"**; the
    publisher renewed in 1939 and Graff sued. The lecture then plays a 1913 recording of the song.
    `[Observed §I-38]`
24. **He runs both branches of an undecided question.** "If Witmark prevailed, then many authors
    would not get a **second bite at the apple**. They could, and would, assign their expectancy
    interests, along with the first term of their copyrights, sometimes for very little money…
    By contrast, if Fred Fisher Music prevailed, authors in the [same position]…" The stakes of a
    doctrinal question are made legible by playing out each outcome. `[Observed §I-38]`

## §C Delivery craft — feeds `roles/tone.md`

- **Three persons, three jobs.** you 6.17 / we 6.39 / I 5.03 per 1,000 words. The inclusive
  **"we" is procedural** ("we'll consider in a minute", "we will return"); **"you" addresses
  the listener's state** ("you are unlikely to retain", "you should be familiar", "you need to
  know only"); **"I" announces the plan** ("I'll be examining today"). `[Observed]`
- **Rhythm** — mean sentence 19.8 words, median 17, p90 35, 16% short (≤8 words): medium-long
  exposition punctuated regularly by short sentences, not a uniform cadence. `[Observed]`
- **Quoting is verbally bracketed** — he announces a quotation ("Here's the heart of his
  letter") and closes it aloud ("close quote"), so the listener always knows whose words they
  are hearing. `[Observed §I-9, §I-20]`
- **Hedging is steady, not defensive** — 3.01 per 1,000 words, concentrated where the doctrine
  is genuinely indeterminate. `[Inferred]`
- **One marked delivery moment appears in the captions themselves** — "A WORD OF WARNING" is
  capitalised by the professional captioner. `[Observed §I-10]`
- **Humour is not a device in this corpus.** His register is dry and even. `[Inferred]`
- **He is deliberately not a talking head** — see §G; a large share of the delivery is carried
  by material other than his voice. `[Observed §I-26]`

## §D Delivery profile — feeds `voice_profiles.yaml`

Caption-derived proxies. Comparable to other sources measured the same way; **not** calibrated
against the VAD-based numbers in [`prosody-profiling.md`](prosody-profiling.md).

| metric | value | note |
|---|---|---|
| `speech_rate_wpm` | **137** (range 126–147) | manual captions ÷ runtime; the trustworthy figure. A 21 wpm spread across 17 h — deliberate and unusually consistent |
| unit length | **27.3 min** median (8–43.5) | median 3,614 words per segment |
| `sent_len_mean` / `median` / `p90` | 19.8 / 17 / 35 | 38 of 40 items punctuated (density 5.2 marks/100 words) |
| `short_sent_frac` (≤8 w) | 0.15 | |
| `question_rate` | 0.03 | range 0–0.10 — and see §B-13 before reading anything into it |
| `long_pause_midsentence_frac` | **0.927** | proxy, from word-timing gaps aligned to the punctuated track |
| `long_pause_per_min` | 16.3 | proxy, threshold relative to median word interval — uncalibrated |
| `f0_sd_st`, `arousal_std`, register | — | **not measured**; needs audio |

## §E Standards — what he would reject — feeds `roles/editor.md`

Pass 2 supplies this section from his own six stated **Pedagogic Principles** and three
objectives, so most of it is `[Observed]` rather than inferred.

1. **Simplification, as the price of accessibility.** His flattest red line: "It is often
   asserted or assumed that complex systems of ideas must be simplified to make them accessible
   to broad audiences. **CopyrightX rejects that proposition.**" The lectures are pitched to
   "meet the demanding standards of Harvard Law School students"; non-lawyers read the same
   judicial opinions and sit the same exam; "all students must wrestle with the most difficult
   questions in the field." `[Observed §I-27]`
2. **But jargon and missing background are faults, not rigour.** The paired commitment: "When
   crafting the lectures and case studies, we try to **minimize jargon** and to provide,
   whenever possible, **background information necessary to understand technical legal
   issues**" — plus a separate pre-course guide to reading judicial opinions for non-lawyers.
   The resolution he reaches is: do not simplify the substance; equip the listener to meet it.
   `[Observed §I-27, §I-28]`
3. **Passive listening treated as a known failure mode.** Principle 1: "Students do not learn
   well when they merely listen to or watch lectures. They are much more likely to master and
   retain information and ideas when they put them to use — solving problems, debating their
   merits and applications." He does not answer this inside the lecture; he answers it with a
   mandatory discussion class. `[Observed §I-29]`
4. **A rule taught without its theory, or without its application, is incomplete** — the
   three-level demand in §A-5. An account that memorises rules is a failed account.
   `[Observed §I-24]`
5. **False certainty where the doctrine is indeterminate** — "More guidance than that may be
   impossible" is the correct answer, not a failure to find one. `[Observed §I-15]`
6. **A silent gap** — material too large for the segment is named and excused aloud.
   `[Observed §I-6]`
7. **An unmarked opinion, and a premature one** — his views are labelled as his, and held back
   until the listener has had room to form their own. `[Observed §I-16, §I-25]`
8. **An invented controversy.** His case studies are real "not hypothetical" controversies as a
   stated rule; his one-sentence illustrative hypotheticals are a separate, clearly-signalled
   instrument. `[Observed §I-17]`
9. **An unresolved ambiguity, handed back.** His exam instructs: "If you find any aspect of the
   exam's content or instructions to be ambiguous, **do not request a clarification. Instead,
   develop your own interpretation that resolves the ambiguity and make that interpretation
   explicit in your response.**" Spotting an ambiguity, resolving it, and declaring the
   resolution is the graded skill. `[Observed §I-31]`
10. **An answer that does not say what it would need to know.** "If you need additional
    information to answer any of these questions, say what that information is and why it
    matters." Naming the missing fact, and why it would change the outcome, is part of a
    competent answer rather than a hedge. `[Observed §I-31]`
11. **Analysis that stops before consequences.** His fact-pattern question runs the full chain
    per party: what claims lie, what defences answer them, **the probability of prevailing**, and
    what remedies follow. A verdict without a remedy is half an answer. `[Observed §I-31]`
12. **Theory that never touches doctrine.** The second question requires arguing whether a named
    jurisdiction should adopt two specific statutory provisions, and "your answer should reflect
    familiarity with at least one of the four general theories… considered in this course."
    Theory is assessed by the work it does on a concrete provision, never on its own.
    `[Observed §I-32]`
13. **Simplify the instrument if you like; never the account of it.** One stated purpose of the
    statute he drafted for Namibia is "to simplify Namibia's copyright system and thus make it
    more readily understandable by nonlawyers" — while Principle 6 forbids simplifying the
    *teaching*. The distinction is deliberate and worth keeping. `[Observed §I-33]`

## §F Defaults — feeds `persona.yaml`

- **Unit length ≈ 27 min** (his median segment), with a real range of 15–45. `[Observed]`
- **Single voice, no simulated interlocutor** in the recorded material. `[Observed]`
- **Phrases that are load-bearing devices, not filler** — the restatement ("in other words"),
  backward reference ("you'll recall", "as we've seen"), concession ("to be sure"), the
  micro-hypothetical ("suppose, for example"), the deferral ("for the time being, you need to
  know only that"). Each is a *move* with a job; a watchlist built from this source should
  require the move and vary its wording, not ban the phrase. `[Observed]`
- **No filler habit was found** in 17 h. Any ban list must therefore come from elsewhere; this
  source does not supply one. `[Inferred]`

## §G Transfer & exclusions

**Converts directly to single-narrator audio:** position-in-the-arc opening; the
warning-and-deferral; the spiral promise with an episode number attached; the
micro-hypothetical; the restatement; flat admission of indeterminacy; marked and
deliberately-late own view; substantive close plus forward handoff; the machine metaphor;
verbally bracketed quotation.

**The central conversion risk — his medium is not voice-only, by design.** Principle 3,
*Multiple Media*: "the recorded lectures contain **little footage in which I appear as a
'talking head.' Most of the time, my voice is combined with (or replaced by) visual or audio
material** — illustrating cases, suggesting typologies of arguments." His two mindmaps hold
*all* of his lecture notes and appear as background throughout, and they were his
highest-rated component. His stated rationale is Pinker's: syntax is "an app that uses a tree
of phrases to translate a web of thoughts into a string of words", and a map hands the learner
the web directly instead of making them rebuild it from the string. `[Observed §I-26, §I-30]`

Audio is the most purely linear "string of words" available — the exact channel his maps exist
to bypass. Two consequences follow, and they are the most useful things in this dossier:

- **Anything visual must be rebuilt as spoken structure**, repeatedly re-anchored. His own
  linear-channel compensations are already in the corpus and are directly reusable: the
  position-in-the-arc opening, backward reference by name, and the numbered spiral promise all
  exist to keep a listener oriented without a picture.
- **Spatial deixis must be eliminated, and it is not a phrase-level fix.** Counting every form
  of it — "as you can see", "on your screen", "shown above/below", "at the top" — gives **131
  occurrences across 33 of the 40 segments**, so it is present in 82% of the corpus, including
  in segment openings ("the striking building shown on your screen"). Spoken with nothing to
  see, each one is a lie. This is the single largest conversion cost in adopting him, and its
  scale is only visible once counted. `[Observed §I-20; verified §J-6]`

**Other conversions:** scheduled *Illustrations* → a named beat, since no separate artefact
ships. Lecture-boundary framing → series-boundary framing, since the unit here is one episode.
And the function his live seminars carry — putting the material to use, which Principle 1 says
listening alone will not achieve — has **no channel** in recorded audio. Whatever answers it
must be built into the episode; that is a genuine gap in what this source can hand over, not a
detail. `[Observed §I-29]`

**Do not import:** US copyright doctrine and its 2013 vintage; the "Hello, I'm Terry Fisher"
signature (a personal identifier, not a method); the twelve-lecture count; the teaching-fellow
and affiliate apparatus, which is an institutional design rather than a craft technique; the
3% question rate as a virtue in itself, since §B-13 shows it is the product of a channel split
that recorded audio does not have.

## §H Candidate prompt lines

At most twelve, imperative, tagged with a target file. Nominations only — selection happens at
synthesis.

1. `planner` — Sequence the series so every stretch of machinery is followed by a lens for
   judging it, and announce the switch in both directions with the episode number attached.
2. `planner` — Size one episode to one apparatus, about 25–30 minutes; let a simple one run
   short and a hard one run long rather than padding or truncating.
3. `planner` — Hold the narrator's own verdict on the big question until late in the series,
   and say that you are holding it and why.
4. `planner` — Schedule the case pass as its own beat rather than sprinkling illustrations
   through the exposition.
5. `planner` — Build cases from real, documented controversies and analyse how the actual
   participants did or could have used the rules; never invent a controversy.
6. `writer` — Open a mid-series episode by saying where it sits in the arc and what the
   listener should already hold, then what today adds.
7. `writer` — When material is genuinely intricate, say so, say what the listener needs to hold
   *now*, and name the later episode where it returns.
8. `writer` — State the aim of a hard passage as marking the locations you will come back to,
   not as mastery.
9. `writer` — After any technical formulation, restate it once in plain words, varying how you
   introduce the restatement.
10. `writer` — Never simplify the substance to make it accessible; cut jargon and supply the
    missing background instead.
11. `writer` — Never write spatial deixis — no "as you can see", no "here", no "at the top" —
    because the listener has no picture; describe the structure instead.
12. `tone` — Bracket every quotation of primary text aloud, opening and closing it, so the
    listener always knows whose words they are hearing.

## §I Evidence

Locators are item slugs under `experiments/craft_sourcing/corpus/fisher/`; `LFC` is
*Lessons from CopyrightX*.

1. **Unit size** — `out/fisher-profile.json`, `per_item[]`: 40 items, median `duration_min`
   27.3 (8.0–43.5), median `words` 3,613.5.
2. **9 doctrine / 3 theory** — LFC: "Nine of the 12 lectures consist of surveys of the
   principal sets of rules in copyright law; the other three present the main theories upon
   which scholars (and sometimes lawmakers) rely when shaping or evaluating the copyright
   system."
3. **Spiral promise / announced oscillation** — `05-…-introduction`: "In the 3rd lecture, we
   will return to legal doctrine." · "In the 10th lecture, we will return for the last time to
   copyright theory…" · `04-…-multilateral-treaties`: "Several times during the remainder of
   this lecture series we will return to these themes."
4. **Scheduled illustrations** — `meta-lectures-index`: an `Illustrations` entry closes the
   Subject Matter, Welfare Theory, Authorship and Mechanics groups.
5. **Position-in-the-arc opening** — `23-…-reproduction`: "Hello, I'm Terry Fisher. This is the
   seventh of 12 lectures on copyright. We're just past the halfway point of this lecture
   series. By now, you should be familiar with the rules governing what types of creative works
   are subject to…"
6. **Omission stated** — "The history of the negotiations that resulted in the TRIPS agreement
   is intricate — much too intricate to be explored here."
7. **Map, not retention** — "Rather my goal has been to convey to you the key principles and
   trends — and to mark the locations of the treaty provisions to which we will return when
   examining specific features of copyright law."
8. **Finale** — `40-remedies-criminal-penalties`, final words: "…in the ongoing project of
   adapting that machine to deal responsibly with changing social and cultural circumstances. I
   hope you have found the lectures helpful in this regard. Thank you for your patience and
   attention."
9. **Interior cold open on a document** — `06-…-fairness`: "In 1783, the author Joel Barlow
   wrote a letter to the Continental Congress in the United States urging the adoption of
   copyright legislation. Here's the heart of his letter. 'There are certainly no kind of
   property in the nature of…'"
10. **Warning and deferral** — `04-…`: "A WORD OF WARNING: This material is intricate. You are
    unlikely to retain all of it right now." · "For the time being, you need to know only that
    this legal relationship is managed by yet another intermediary, the organization
    SoundExchange." (8 corpus instances of "for the time being")
11. **Simplest true statement** — `04-…`: "Each country in the world creates, interprets, and
    enforces its own copyright laws. With minor exceptions that we'll consider in a minute, the
    force of those laws reach no further than the country's borders. To put the same point
    another way…"
12. **Restatement** — `out/fisher-profile.json`, `mined.top_sentence_openers`:
    `"in other words," × 75`, rank 1 of all openers.
13. **Micro-hypothetical** — 31 corpus matches, including "Suppose that you make a perfect
    replica of The Thinker." and "Suppose, for example, that Picasso came to regret his Blue
    Period."
14. **Backward reference / concession** — mined openers: `"you'll recall, i" × 14`,
    `"as we've seen," × 12`, `"to be sure," × 16`, `"as a result," × 18`.
15. **Indeterminacy** — `24-…-improper-appropriation`, final words: "…you can distill an
    impression of the degree or kind of similarity that will likely get you in trouble, and the
    degree or kind that will not. More guidance than that may be impossible." · "Application of
    the doctrine is thus very hard to predict in advance."
16. **Own view marked** — "The third role of theory is, in my view, the most important." · "And
    in my view, it doesn't hold up." · "My own view is no."
17. **Channel split; real case studies** — LFC: "During the two live classes, I don't lecture
    at all, and I rarely focus on the assigned materials. Instead, I engage the students in
    Socratic discussions of case studies that raise difficult questions related to the themes of
    the week. All of the case studies examine real (not hypothetical) controversies. In form,
    they more closely resemble the kinds of case studies used in business schools than the cases
    typically employed in law schools."
18. **Close plus handoff** — `15-welfare-theory-the-incentive-theory`, final words: "In the last
    segment of this lecture, I'll discuss a few applications and refinements of the welfare
    approach and then step back from the details and ask you, through these lenses, what are the
    strengths and weaknesses of copyright."
19. **The machine** — "I'll be examining today the mechanics of copyright, in other words, the
    way in which the machinery of the copyright system works in practice." · "The machinery of
    the copyright system is intricate, surprisingly so." · "These three features surely do not
    exhaust the set of important aspects of the copyright machine."
20. **Spatial deixis / bracketed quotation** — mined openers: `"as you can" × 33`, rank 2 ·
    corpus: "…close quote."
21. **Licence relaxed for derivative works** — LFC: "Richard Stallman has persuaded me to open
    the doors even wider. Henceforth, users' only obligation will be to provide appropriate
    attribution… The goal, rather, is to maximize the number and variety of educational projects
    and derivative works that can be built (directly or indirectly) on our foundation."
22. **Outcomes** — LFC Figure 2 and surrounding text: Harvard overall effectiveness 4.66 / 4.64;
    online 4.57; Maps 4.40 / 4.76; online forum 2.91 / 2.42; "If instead one compares the number
    of students who enrolled in the course to the number who stuck with it to the end, took the
    exam, and passed it… the retention rate in 2013 was 40% and in 2014 was 41%" against a
    "roughly 7%" MOOC average.
23. **Wise practice** — LFC: "Wise practice entails, among other things, invoking or applying
    the law in a way that will advance its ultimate ends. That, in turn, requires knowing what
    those ends are." · "That skill, I believe, can be acquired only through practice. One of the
    reasons why case studies figure so prominently in CopyrightX is to provide the students
    opportunities for practice of this sort. By exposing them to many real controversies,
    examining how the participants in those controversies did or could have employed the law…"
24. **Three-level model; oscillation** — LFC Principle 2: "understanding law requires much more
    than memorizing a collection of rules. It also demands, at a minimum, securing a critical
    understanding of the theories that either animate those rules or could be used to change
    them and acquiring an appreciation of how the rules influence behavior and the capacity to
    predict how they have been (or would be) applied to real controversies." · "the weekly
    lectures oscillate between doctrine and theory; the classes focus on the application of
    doctrines and theories to case studies."
25. **Judgment withheld to lecture 10** — LFC: "I do not attempt in the lectures, or in my
    teaching, to resolve that disagreement. Rather, I strive to inform students and viewers what
    the principal contentions are… (Partly to afford them room to reflect, I wait until the tenth
    lecture to present my own perspective on the most attractive conception of those functions.)"
26. **Not a talking head** — LFC Principle 3: "the recorded lectures contain little footage in
    which I appear as a 'talking head.' Most of the time, my voice is combined with (or replaced
    by) visual or audio material — illustrating cases, suggesting typologies of arguments, and so
    forth."
27. **Rigor, and its pairing** — LFC Principle 6: "It is often asserted or assumed that complex
    systems of ideas must be simplified to make them accessible to broad audiences. CopyrightX
    rejects that proposition… they have not been 'dumbed down' in any way… all students must
    wrestle with the most difficult questions in the field." · "When crafting the lectures and
    case studies, we try to minimize jargon and to provide, whenever possible, background
    information necessary to understand technical legal issues."
28. **Separate on-ramp for non-lawyers** — LFC: "the online students (most of whom are neither
    lawyers nor law students) are encouraged to read, prior to the course, a guide to
    understanding and analyzing judicial opinions."
29. **Passive listening as a known failure** — LFC Principle 1: "Students do not learn well when
    they merely listen to or watch lectures. They are much more likely to master and retain
    information and ideas when they put them to use — solving problems, debating their merits and
    applications, and so forth."
30. **Maps, and the Pinker rationale** — LFC Principle 3: "I have prepared two 'mindmaps' that
    contain all of my lecture notes for the course. The first presents all of the main sets of
    rules that together constitute copyright law; the second presents the main copyright
    theories… Many students have reported that this format makes the concepts easier to understand
    than a linear outline." · quoting Pinker: "Syntax … is an app that uses a tree of phrases to
    translate a web of thoughts into a string of words."
31. **Exam standards: ambiguity, missing facts, the full chain** — `meta-exam-2020`: "If you find
    any aspect of the exam's content or instructions to be ambiguous, do not request a
    clarification. Instead, develop your own interpretation that resolves the ambiguity and make
    that interpretation explicit in your response." · Question 1 asks, per party: "(1) What claims
    might Disney assert… (2) What defenses might those parties assert in response? (3) What is the
    probability that Disney would prevail against each party? (4) If Disney prevailed, what
    remedies would be available…" · "If you need additional information to answer any of these
    questions, say what that information is and why it matters." · the bracketed "fictionalized
    composite… 'alternative facts'" disclosure. Open-book by design: "you may read, watch, or rely
    on any material you wish", with the lectures and maps remaining available throughout.
32. **Theory made assessable on a provision** — `meta-exam-2020` Question 2: a draft Copyright Act
    of Namibia he prepared for the Business and Intellectual Property Authority, "provisions
    highlighted in red deviate significantly from the corresponding aspects of the copyright
    systems of most countries"; the student picks a country and two red provisions and argues
    whether that country should adopt them — "Your answer should reflect familiarity with at least
    one of the four general theories of copyright law considered in this course."
33. **Simplify the instrument, not the teaching** — `meta-exam-2020`, purposes of the draft Act:
    "(b) to simplify Namibia's copyright system and thus make it more readily understandable by
    nonlawyers"; contrast §I-27.
34. **Planted doctrinal triggers inside a real narrative** — `meta-exam-2020`: source works of
    varying vintage (Hugo 1831, Andersen 1844), an employee-authored norm with one deliberate
    exception ("The genesis of only one of the films deviated from this pattern" — a 1986
    freelance script assigned in 1987), an algorithm whose workings are "unclear", years of
    tolerated unauthorised use, and a platform CEO on the record refusing automated filtering.
    Each detail activates a different part of the apparatus the course taught. `[Inferred]` that
    the placement is deliberate; `[Observed]` that the details are present.

---

## §J Verification — pass 4

Every structural claim tested against **all 40 segments** by mechanical count, rather than
against the segments that produced it. Method and outcome per claim, so a later reader can
re-run the test rather than trust the verdict.

| Claim | Test | Outcome |
|---|---|---|
| **§B-1** frame at lecture openings only | Matched the opening 150 characters of all 40 segments for the greeting and for a lecture ordinal | **Falsified in part.** 12/12 lecture openers carry frame + ordinal; **2 of 28 interior segments carry the frame too** (15, 27), with a segment-level position instead. Claim rewritten |
| **§A-8 / §B-2** position + inventory | Matched self-locating phrasing in the first ~260 characters of all 40 | **Softened.** 27/40 locate themselves; 13 open cold on material. The universal reading was wrong; both patterns are real |
| **§B-14** closings never summarise | Summary-marker and forward-handoff patterns over the last 320 characters of all 40 | **Confirmed, strongly: 0/40 summary markers.** Forward handoff in 18/40, so the "plus a handoff" half holds about half the time |
| **§B-8** micro-hypothetical is one sentence | Measured the sentence length of all 51 "suppose…" instances | **Confirmed at the median** (17 words); tail of 6 instances over 40 words, max 124. "Never elaborate" cut |
| **§B-7** restatement | Counted all occurrences and the segments containing them | **Confirmed as pervasive**: 137 occurrences across **33/40** segments |
| **§B-5** spiral promise | Same | **Confirmed, localised**: 28 across 15/40 — it clusters where material is deferred |
| **§B-4** deferral | Same | **Confirmed, localised**: 10 across 8/40 |
| **§B-11** indeterminacy admitted | Same | **Confirmed as a habit**: 12 across 11/40 — a quarter of the corpus, not a one-off |
| **§B-12** own view marked | Same | **Confirmed as rare**: 8 across **6/40**, consistent with his stated policy of withholding his own perspective until the tenth lecture (§A-6) |
| **§G** visual deixis | Counted every spatial-reference form | **Strengthened**: 131 across **33/40** segments — 82% of the corpus |

**What remains unmet.** The `≥2 independent analysts` rule. Every pass so far is mine, and a
mechanical count cannot notice a technique nobody thought to look for — it only tests claims
already written down. Discovery still needs a reader who has not seen this file. Two of the six
queued reads would be enough to change the corroboration status of §A and §B.
35. **Inline attributed quotation; the gloss inside the quote** —
    `12-…-fictional-characters`: "The Rocky character, 'has become identified,' says the court,
    'with specific character traits ranging from his speaking mannerisms to his physical
    characteristics.'" · "Indeed, says the judge, the character was 'lifted lock, stock, and barrel
    from the prior Rocky movies.'" · `22-…-protective-provisions`: "'your committee--' meaning your
    congressional committee-- 'felt that it should be the exclusive right of the author to take the
    renewal term…'"
36. **Stacked complications, resolution, doctrinal kinship, de-escalation, the known practice, the
    digression marker** — all `12-…-fictional-characters`: "some of the most famous fictional
    characters evolve over the course of their commercial careers… Which, if any of the Superman
    incarnations, thus enjoys copyright protection? Difficult to say. Here's another complicating
    factor… The premier example is James Bond, who has now been presented by six different actors.
    Tuxedos and a British accent can only go so far in obscuring the differences among these
    depictions… Typically, no. Modern courts are quite forgiving of indeterminacy of these sorts." ·
    "This exclusion, you will probably notice, is a cousin of the Scenes A Faire doctrine, which we
    discussed in lecture number one." · "This exclusion doesn't much matter, however, because
    there's usually not much point in appropriating stock characters." · "a crucial implication of
    the protectability of fictional characters is that almost all fan fiction… is legally
    problematic. Now, I hasten to add that fan fiction may escape liability under one of the
    affirmative defenses… that we'll discuss in detail in lecture number nine." · "So to return to
    the main line…"
37. **Legislative history as evidence** — `22-…-protective-provisions`: "the House and Senate
    reports explaining the basis of that statute contained a passage that seemed to cast doubt on
    the validity of these assignments. Here it is. The crucial language is highlighted." … "In
    other words, the law was designed to protect authors from their own foolishness or
    vulnerability."
38. **The dated human story, the money, the recording, both branches** —
    `22-…-protective-provisions`: "In 1912, Mr. Graff helped compose the song, 'When Irish Eyes are
    Smiling.' Here's a brief excerpt of a 1913 recording of the song. [MUSIC PLAYING…]" · "To raise
    some cash, Graff gave up his royalties for 'Irish Eyes,' and for 68 other songs, and in
    addition, assigned his expectancy interest in the renewal term for all of those 69 songs to
    Witmark, in return for a lump sum payment of $1,600." · "If Witmark prevailed, then many authors
    would not get a second bite at the apple… By contrast, if Fred Fisher Music prevailed…"

---

## §K Held-out discovery — pass 5

Pass 4 counted claims that already existed. Pass 5 did the opposite: a close read of **two full
segments never opened in any earlier pass** — `12 Fictional Characters` and `22 Protective
Provisions` — with one instruction, to look for techniques the dossier does not contain.

It found **eight** (§B-17 to §B-24), none of which any amount of counting would have surfaced,
because a count can only test what someone has already written down. Two of them change the
picture materially:

- **§B-23/24** — a doctrinal rule taught through a single dated human story with real money in it,
  and the undecided question resolved by playing out *both* outcomes. Nothing in passes 1–4
  suggested he narrates at all; the sampled openings and closings had made him look purely
  expository.
- **§B-19** — he actively de-escalates: "This exclusion doesn't much matter." Telling a listener
  what not to spend attention on is a distinctive habit and the earlier passes missed it entirely.

Pass 5 also produced more §G evidence without looking for it: "The crucial language is
highlighted", "as you can see", and an embedded audio recording all appear in these two segments,
confirming that the visual and media dependence runs through the corpus rather than clustering.

**Status.** Fisher stands at **pass 5 of 6**, and the remaining pass is the one I cannot do: a
read by someone who has not seen this file. Everything here is one reader's work, verified
mechanically and extended by held-out reading, which is as far as a single analyst can honestly
go. The corroboration column in §J stays open.
