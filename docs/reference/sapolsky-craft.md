# Sapolsky craft reference

Distilled from **Human Behavioral Biology** (Stanford BIO 150, 2010) by **Robert M. Sapolsky**,
per the process in [`craft-sourcing.md`](craft-sourcing.md). Sections are named for the persona
file they feed. Confidence labels: `[Observed]` (quoted in §I), `[Inferred]` (pattern, no single
quote), `[Unverified]` (secondary — must be resolved before synthesis).

> **Self-contained by rule.** This dossier describes one person. It makes no comparison to
> another source and no decision about which persona will use what — those belong to the
> synthesis stage.

> **Pass 3 of 3** (three, not six: a device source needs its techniques evidenced, not a whole
> style reconstructed — see §0). Pass 1 mined the corpus and read the opening lecture. **Pass 2
> counted every device per lecture across all 25**, which changed most of the picture — see §J.
> The headline: one device is present in **all 25 lectures**, and it is the one he was hired for.
> Almost everything else clusters in one or two lectures, and pass 1's frequency table turned out
> to be measuring his syllabus rather than his style.
>
> **Pass 3** re-transcribed the method lectures locally with `faster-whisper`, which supplied the
> sentence-level metrics that auto-captions had made impossible (§D), and read lecture 21 cold as
> held-out discovery, finding six moves the earlier passes had missed (§B-13 to §B-18, §K).

> ⚠ **Quotation caveat, applies to every excerpt below.** Only **11 of 25** lectures carry
> punctuated captions; the median track has a punctuation density of **0.04 marks per 100
> words**, i.e. effectively none. All text is YouTube auto-captioning, which mis-transcribes
> technical terms and proper nouns. Excerpts are therefore **reliable for phrasing patterns and
> vocabulary, and unreliable as exact wording.** Nothing here should be quoted as his words in
> anything published without checking the audio.

---

## §0 Source card

| | |
|---|---|
| **Person** | Robert M. Sapolsky, John A. and Cynthia Fry Gunn Professor of Biology, Neurology and Neurosurgery, Stanford |
| **Corpus** | 25 lectures, **36.7 h**, **354,729 words** of auto-captions; median lecture **96.8 min** |
| **Caption quality** | Auto-captions only: **corpus median punctuation density 0.04** marks per 100 words. Sentence-level statistics were therefore impossible from captions |
| **Fixed at pass 3** | Four method lectures (1, 21, 22, 25) re-transcribed locally with `transcribe.py` (faster-whisper `small`) — **50,151 words at 5.2–7.3** marks per 100 words, which makes §D real. Ratios per 1,000 words continue to come from the full 25-lecture caption corpus, where duplication affects numerator and denominator alike |
| **Not obtained** | Audio; slides (referred to constantly); any written self-description of his teaching method; his books, where the same argument is made in print |
| **Acquisition** | `fetch.py sources/sapolsky.json` — subtitles only, from the Stanford course playlist. 2026-09-10 |
| **Permission** | Publicly posted Stanford course lectures; captions fetched for private style analysis. Raw corpus gitignored and uncommitted |

**Role: device source.** He is hired for specific techniques, not for a whole voice, so the bar
is that the corpus evidences **those techniques** clearly — which it does, abundantly (§B-2,
§B-3, §B-8, and the frequency counts in §I-9).

Recorded for the file, since a future reader may ask what this corpus could support if the job
were ever widened: it is 36.7 h and freely obtainable ✔; single-speaker, with student
interjections taken on-mic ✔; an **unedited residential lecture course** rather than an artefact
built for a remote audience — slide-driven and room-dependent; and accompanied by **no written
account of his own pedagogy** in what was acquired, so his intent has to be inferred from the
corpus rather than read from him. None of that limits the assigned job. It would matter only if
someone proposed reconstructing a whole style from him.

## §1 Hired for

**Techniques, not a voice.** Chiefly: explaining a single phenomenon at several interacting
levels of causation, and refusing any single-cause account of it — plus the teaching moves that
carry it (§B-3, §B-8). Everything below is read through that job. He is not hired for
architecture, register, or subject matter, and the question at synthesis is not whether his
corpus is complete but whether a given technique is **in harmony with the persona's method**.

---

## §A Plan-level craft — feeds `roles/planner.md`

1. **The unit is one long session** — 25 lectures, median **96.8 min**, unsegmented and
   unedited. `[Observed §I-1]`
2. **The spine is a ladder of causation ordered by time-depth.** A behaviour is explained by
   asking what happened one second before (neurons), then minutes to hours (hormones), then
   days to months, then adolescence, childhood, foetal life, genes, centuries of culture, and
   finally evolution. The course walks the ladder rung by rung — evolution and genetics
   (lectures 2–9), neuroscience and endocrinology (10–14) — before spending the back half
   applying the whole ladder to concrete behaviours: sexual behaviour, aggression, language,
   schizophrenia. `[Observed §I-2, §I-3]`
3. **The anti-thesis is declared in lecture 1 — but the declaration is all the phrase-level
   evidence there is.** "That would be the general strategy for the course: we will **resist
   categorical thinking over and over and over** — and not just because that's cool and nuanced
   and subtle." The words "categorical thinking" appear **6 times, all of them in lecture 1**, and
   nowhere in the other 24. He announces the rule once, memorably; whether he *enforces* it is not
   something a phrase count can show, and pass 1 should not have said "enforced".
   `[Observed §I-4; corrected §J-1]`
4. **The methodology lectures come late, after the content.** *Chaos and Reductionism* (21) and
   *Emergence and Complexity* (22) are about how to think, and they arrive once the listener has
   twenty lectures of material to think about. `[Observed §I-1]`
5. **Application lectures run in multi-part blocks** — Human Sexual Behavior I–III, Aggression
   I–IV. The hardest applications get four sessions, not one. `[Observed §I-1]`

## §B Prose-level craft — feeds `roles/writer.md`

1. **Cold open on a concrete scenario, before any framework.** The course opens: "we start off
   with a scenario — 40-year-old guy, quiet suburban life, married fifteen years, two kids,
   three and a half dogs, everything standard, everything's going wonderfully — and one day out
   of nowhere he punches somebody in the face at work." `[Observed §I-5]`
2. **Name the bucket, then dissolve it — established once, at length, then invoked thinly.**
   "Bucket" appears **60 times, 25 of them in lecture 1**, and in 14 of 25 lectures overall: the
   metaphor is built in the opening session and thereafter used as shorthand rather than rebuilt.
   He lays out the disciplinary categories available for explaining a behaviour, shows the damage
   of living in one, and then denies the categories are real: "over-emphasising the importance of the bucket you happen to
   live inside of, and thus suddenly everything about this behaviour is explained by a gene, a
   neurotransmitter, a childhood trauma." Then: "there's no buckets — all there are are
   **temporary platforms**, and each platform is simply the easiest, most convenient way of
   describing the outcome of everything that came before." `[Observed §I-6]`
3. **The recursive push-back — vividly stated, thinly evidenced at phrase level.** He lets an
   explanation settle and then undercuts it by asking what caused *that*: "just as we're about to
   settle happily into that bucket, we push back a bit and say: well, what smell, what sound, what
   sensory stimulation in the environment caused those neurons to get activated?" Phrases of that
   family ("step back", "push back") appear in only **6 of 25** lectures, so either the move is
   less frequent than pass 1 implied, or he performs it in words a phrase count cannot catch. The
   distinction matters and this corpus does not settle it. `[Observed §I-7; qualified §J-2]`
4. **"What's up with…?"** — 35 corpus instances. A colloquial framing that converts a topic into
   a puzzle: "What went on in the brain one second before that caused that behaviour to occur?
   **What's up with** the neurobiology?" `[Observed §I-3]`
5. **"It depends" as a real answer — but concentrated where the material demands it.** 50
   instances, of which **37 fall in a single lecture** (Behavioral Genetics II, where it is the
   substantive answer to heritability questions), and it appears in 10 of 25 lectures. A
   substantive answer, not a verbal tic. `[Observed; corrected §J-3]`
6. **Second-person saturation — heavy, and variable.** "you" and "your" run at **26.4 per 1,000
   words** across the corpus, by a wide margin the dominant address; but the per-lecture range is
   **14.1 to 48.2**, a more-than-threefold spread. It is a strong habit, not a constant setting.
   `[Observed §I-8; qualified §J-5]`
7. **Questions carry the exposition** — 10.7% of sentences in the punctuated subset end in a
   question mark, and four of his twelve most frequent sentence openers are interrogative
   ("how do you", "what do you", "what's up with", "what you see"). `[Observed §I-8]`
8. **He demonstrates the fallacy on non-subject material first.** Categorical thinking is shown
   with a language continuum and a number-series puzzle before it is applied to biology, so the
   listener meets the error in a domain where they have no stake. `[Observed §I-4]`
9. **Low hedging** — 1.07 hedges per 1,000 words. The pattern is to assert cleanly and then
   complicate, rather than to qualify in advance. `[Observed §I-8]` / `[Inferred]` as to intent.
10. **Pass 1's "method lexicon" was mostly measuring the syllabus, not the style.** Counted per
    lecture, the picture collapses: **83 of 88** uses of "reductive/reductionism" fall in the
    lecture *titled* "Chaos and Reductionism", and **24 of 35** uses of "emergence" fall in
    "Emergence and Complexity". Those are topic words, not method words, and a corpus organised by
    topic will always make them look like habits. The exception is decisive and is the next item.
    `[Corrected §J-4]`
11. **"Level of" / "levels of" — 207 uses, present in all 25 lectures.** The only device in this
    corpus that appears in **every single** lecture, and the only frequency claim that survives
    per-lecture counting. It is also precisely what he is hired for: the habit of naming which
    level of causation an explanation belongs to. Distribution is genuinely spread (35, 18, 16,
    13, 13, 12… across lectures), not concentrated. `[Observed §J-4]`
12. **"What's up with…?" — 35 uses across 14 of 25 lectures**, moderately distributed and holding
    up as a real recurring habit. `[Observed §I-3; verified §J-4]`
13. **He names his own incomplete grasp of the material, out loud, at the start of the hardest
    unit.** "Overall these are probably the most difficult lectures of the course, the most
    difficult material. In part because **I'm not sure if I completely understand what I'm talking
    about**, but also because this is intrinsically some really different ways of thinking about
    things in the realm of science." A teacher conceding partial mastery before beginning is
    unusual enough to count as a signature. `[Observed §I-11]`
14. **He predicts the audience's split reaction to the assigned reading, and names all three
    camps.** The chaos book "incites a subset of people to passionate enthusiasm… another small
    subset into just the… greatest level of irritation… And everybody else is just vaguely
    puzzled." `[Observed §I-11]`
15. **He offers his own reading history as the argument for the material's force, with a joke
    against himself.** "This book, when I first read it… this was like the first book I had read
    where I finished it and immediately started over again. First one since like *Where the Wild
    Things Are* in terms of influence." `[Observed §I-11]`
16. **One pattern, walked across scales, to show that it is scale-free.** Bifurcation is traced
    through neuronal arborization, then the descending aorta splitting "into two and splits into
    two and splits into two", then capillaries, then the trachea into bronchi and bronchioles —
    and only then the point: "notice the difference in scale… you can have just as complex
    branching coming off of a single neuron as the branching you're getting in a gazillion
    different capillaries… **independent of scale**." `[Observed §I-12]`
17. **He builds the opponent's account in its own terms until its cost becomes absurd.** Having
    set up bifurcation, he asks "how does the body code for that?" and then constructs the
    reductive answer explicitly: "There is some sort of set of rules telling [an] aorta… there is
    some gene or genes which specify the point where this bifurcates… another type of gene that
    specifies the next one." A gene per branch point — the enumeration *is* the refutation. This
    is the mechanism behind §B-2, which pass 1 asserted without showing how it is done.
    `[Observed §I-12]`
18. **He flags when one field has borrowed another's vocabulary.** Neuronal complexity is measured
    as "arborization, using terms straight out of [dendrology]" — the loan is named rather than
    used silently. `[Observed §I-12]`

## §C Delivery craft — feeds `roles/tone.md`

- **Fast** — **161 words per minute** across 36.7 h (text ÷ runtime). `[Observed §I-1]`
- **Address is overwhelmingly second-person** (§B-6), with "we" at 8.4 and "I" at 5.3 per 1,000.
  `[Observed §I-8]`
- **Interrogative rhythm** — see §B-7. `[Observed]`
- **He speaks to a live room and lets it in**: student interjections are taken on-mic and
  answered by name mid-flow. `[Observed §I-10]`
- **Slide-dependent** — "my least favourite slide of the day", "this happens to be my favourite
  slide". `[Observed §I-10]`
- **Humour**: not assessed in pass 1. The auto-captions strip laughter and timing, and the
  register question cannot be settled from this corpus without audio. `[Unverified]`

## §D Delivery profile — feeds `voice_profiles.yaml`

| metric | value | note |
|---|---|---|
| `speech_rate_wpm` | **160** | confirmed on all four (159, 159, 160, 165) — the tightest figure in this dossier; the caption estimate was 161 |
| unit length | **96.8 min** median | 53.9–105.1 |
| `sent_len_mean` / `median` / `p90` | **16.1 / 13 / 32** | local transcription of 4 lectures, 50,151 words; per-lecture mean 13.8–19.2 |
| `short_sent_frac` (≤8 w) | **0.35** | range 31–43% across the four |
| `question_rate` | **0.089** | range 7.0–11.9%. The auto-caption estimate of 0.107 ran slightly high |
| `you_per_1k` / `we` / `I` / hedges | 26.4 / 8.4 / 5.3 / 1.1 | all items — ratios survive unpunctuated text |
| `long_pause_midsentence_frac` | **still unavailable** | The metric aligns the words before a gap against a punctuated transcript. It read a spurious `1.0` from auto-captions, because with no terminators to align against every gap classifies as mid-sentence. Local transcription fixes the punctuation but discards the word-level timings, so this one needs the two joined — the only §D cell still open |
| `pause_ratio`, `long_pause_per_min` | 0.43 / 13.3 | caption proxies, uncalibrated, and weakened further by caption quality |
| `f0_sd_st`, `arousal_std`, register | — | not measured; needs audio |

## §E Standards — what he would reject — feeds `roles/editor.md`

No written self-description was obtained, so this section is weaker than it should be and rests
on the corpus.

1. **A single-cause explanation of anything.** The stated main point of the course is the
   interaction between levels; an account that lands in one bucket and stays there is the error
   the course exists to prevent. `[Observed §I-6]`
2. **Treating a level of description as a cause.** A bucket is "the most convenient way of
   describing all of the influences that came beforehand" — mistaking the description for the
   mechanism is the failure. `[Observed §I-6]`
3. **Category boundaries taken as real.** "When you pay attention to categorical boundaries you
   don't see big pictures." `[Observed §I-4]`
4. **Premature closure.** Every settled explanation gets pushed back one level. `[Observed §I-7]`
5. **A false definite answer where the honest one is conditional** — "it depends", 50 times.
   `[Inferred]`

## §F Defaults — feeds `persona.yaml`

- Unit length ≈ 97 min, which reflects a university timetable rather than a design choice, and
  should not be read as a recommendation. `[Inferred]`
- Single speaker, but not single-voice in the strict sense: the live room is audible and
  answered. `[Observed §I-10]`
- No filler ban list can be drawn from this corpus: lecture-hall discourse markers ("okay so",
  "all sorts of") are frequent and are artefacts of live speech rather than devices.
  `[Inferred]`

## §G Transfer & exclusions

**Converts directly, and is medium-independent:** the ladder of causation by time-depth; naming
a bucket and then dissolving it into a temporary platform; the recursive push-back; the
colloquial puzzle framing; demonstrating a reasoning fallacy on neutral material before applying
it to the subject; "it depends" as a legitimate answer.

**Needs conversion:** slide references, which are frequent; the live-room exchanges, which have
no analogue in scripted audio and are part of how he sustains a 97-minute session; the
multi-part application blocks, which assume a semester.

**Do not import:** the biology — the entire subject matter is out of scope for the job he is
hired for; the 97-minute unit; the fast 161 wpm delivery, which suits a live room with visual
support and is a separate decision from the method; and any verbatim phrasing, given the caption
quality (§0).

**A caution specific to this source.** The device is powerful and it is also a licence to
digress: each push-back opens a new level, and a persona that adopts the move without a stopping
rule will produce episodes that never land. The corpus does not supply the stopping rule — his
semester does, by ending. Whatever bounds the recursion will have to come from elsewhere.
`[Inferred]`

## §H Candidate prompt lines

Nominations only; selection happens at synthesis.

1. `planner` — Give each episode a ladder of levels at which its phenomenon can be explained,
   and say which rungs this episode climbs.
2. `planner` — Place the methodological episode after the listener has enough material to apply
   it to, not before.
3. `writer` — Open on a concrete case before naming any framework or discipline.
4. `writer` — Name the category an explanation belongs to, then show it is a convenient platform
   rather than a cause.
5. `writer` — After an explanation settles, push back one level and ask what produced it; do this
   deliberately and a bounded number of times.
6. `writer` — Demonstrate a reasoning error on neutral material first, where the listener has
   nothing at stake, before applying it to the subject.
7. `writer` — Frame a topic as a puzzle to be solved rather than a body to be covered.
8. `writer` — Where the honest answer is conditional, say "it depends" and then say on what.
9. `editor` — Fail any account that explains a phenomenon from a single level and stops there.
10. `editor` — Fail any passage that treats a level of description as though it were the cause.

## §I Evidence

Locators are item slugs under `experiments/craft_sourcing/corpus/sapolsky/`. **All excerpts are
auto-caption text; see the §0 caveat.**

1. **Corpus shape** — `out/sapolsky-profile.json`: 25 items, median `duration_min` 96.8, 354,729
   words, 161 wpm; lectures 21 *Chaos and Reductionism* and 22 *Emergence and Complexity*;
   *Human Sexual Behavior* I–III and *Aggression* I–IV.
2. **The time ladder** — `01-introduction…`: "what went on in that organism a half second before
   that behavior occurred… which is the world of what's going on with neurons, what's going on
   with circuitry" · "stepping back and saying okay, one millisecond before that behavior
   occurred, what was going on in the brain, what parts of the brain, what neurotransmitters —
   all of that — stepping back before that…"
3. **The ladder plus the puzzle framing** — "What went on in the brain 1 second before that
   caused that behavior to occur? What's up with the neurobiology? What sensory stimuli caused
   those neurons to generate?" (35 corpus instances of "what's up with")
4. **Categorical thinking as the named enemy** — "there's a bunch of problems with categorical
   thinking" · "when you pay attention to categorical boundaries you don't see big pictures" ·
   "that would be the general strategy for the course: we will resist categorical thinking over
   and over and over, and not just because that's cool and nuanced and subtle" · demonstrations
   on a language continuum and on a number series ("what's the next number in this series and
   why — 42").
5. **Cold-open scenario** — `01-introduction…`, opening words: "this is bio 150, isn't it… so we
   start off with a scenario: 40 year old guy, quiet suburban life, married fifteen year[s], two
   kids, three and a half dogs, everything standard, everything's going wonderfully — and one
   day out of nowhere he punches somebody in the face at work."
6. **Buckets, and their dissolution** — "all these different categories that we can use to
   explain what's going on, all of these different buckets… over emphasizing the importance of
   the bucket you happen to live inside of, and thus suddenly everything about this behavior is
   explained by a gene, a neurotransmitter, a childhood trauma… living inside one bucket. What
   we're going to be doing over and over in here — is the main point of the course — is looking
   at how what goes on [in] your body influences behavior" · "any one of these buckets that we
   spend some time [in]… all we're going to do is think of that bucket as, at that point, the
   most convenient way of describing all of the influences that came beforehand — and in that
   regard there's no buckets, all there are are temporary platforms, and each platform is simply
   the easiest, most convenient way of describing the outcome of everything that [came before]."
7. **The recursive push-back** — "because this part of the brain got activated — but just as
   we're about to settle happily into that bucket, we push back a bit and say: well, what smell,
   what sound, what sensory stimulation in the environment caused those neurons to get
   activated?"
8. **Address and interrogative rhythm** — `out/sapolsky-profile.json`: `you_per_1k` 26.41,
   `we_per_1k` 8.42, `i_per_1k` 5.25, `hedge_per_1k` 1.07; `question_rate` 0.107 over the
   punctuated subset; mined openers include "how do you" ×15, "what do you" ×14, "what's up
   with" ×13, "what you see" ×12.
9. **Method lexicon by frequency** — corpus counts: interact 108, categor- 84, "in other words"
   78, "turns out" 71, reductive 69, bucket 60, "it depends" 50, emergen- 35, "what's up with"
   35.
10. **Live room, and slides** — "okay great, thank[s] Tom — so Tom pointed out my least favorite
    slide of the day earlier; this happens to be my favorite slide."

---

## §J Verification — pass 2

Every device counted **per lecture across all 25**, rather than corpus-wide. Corpus-wide totals
had made topic vocabulary indistinguishable from method vocabulary.

| Claim | Distribution | Outcome |
|---|---|---|
| **§A-3** categorical thinking as an enforced course rule | "categorical thinking" **6 hits, all in lecture 1**, 1/25 lectures | **Corrected.** He declares it once; "enforced" was unsupported |
| **§B-3** recursive push-back | "step back"/"push back" in **6/25** | **Qualified.** Either less frequent than claimed, or expressed in words a count cannot catch — unsettled |
| **§B-5** "it depends" | 50 hits, **37 in one lecture**, 10/25 | **Corrected.** Substantive answer where the material demands it, not a tic |
| **§B-10** the method lexicon | reductive **83/88 in one lecture**; emergence **24/35 in one** | **Falsified as style.** Those are the titles of those lectures. Topic vocabulary, counted as if it were method |
| **§B-2** buckets | 60 hits, **25 in lecture 1**, 14/25 | **Refined.** Built once at length, then used as shorthand |
| **§B-6** second-person saturation | 26.4/1k overall; per-lecture **14.1–48.2** | **Qualified.** Strong habit, threefold spread |
| **§B-11** levels of causation *(new)* | "level(s) of" **207 hits, 25/25 lectures** | **Confirmed, and the only universal device here** — and it is the one he is hired for |
| **§B-12** "what's up with" | 35 hits, 14/25 | **Confirmed** as a recurring habit |

**The transferable lesson.** On a corpus organised by topic — a lecture course, a textbook — raw
word frequency measures the syllabus. Every frequency claim needs a per-item distribution before it
means anything about style, and the test is simple: if the hits cluster in the lecture named after
the word, the word is the subject, not the method.

It is worth noting what survived. The single device this source was hired for is also the single
device present in all 25 lectures, while almost everything else that looked distinctive in pass 1
turned out to be localised. That is a reassuring result for the hiring decision and a chastening
one for corpus-wide counting.
11. **Naming his own limits; the predicted split; the reading history** — `21-chaos-and-reductionism`
    (local transcription), opening: "Overall these are probably the most difficult lectures of the
    course, the most difficult material. In part because I'm not sure if I completely understand
    what I'm talking about, but also because this is intrinsically some really different ways of
    thinking about things in the realm of science. And that's one of the reasons why I forced you
    guys to read this chaos book… this incites a subset of people to passionate enthusiasm about
    the book… another small subset into just the… greatest level of irritation… And everybody else
    is just vaguely puzzled… This book, when I first read it… was like the first book I had read
    where I finished it and immediately started over again. First one since like Where the Wild
    Things Are in terms of influence."
12. **Scale-free pattern; the reductio by enumeration; the borrowed vocabulary** — same lecture,
    mid-session: "you are said to have increased their arborization, using terms straight out of
    [dendrology]… You've got your descending aorta… and then it splits into two and splits into two
    and splits into two… You look at the pulmonary system, and it is the exact same bifurcation
    coming down your trachea, which splits into two bronchos, and then splits into bronchioles…
    notice the difference in scale… you can have just as complex branching coming off of a single
    neuron as the branching you're getting in a gazillion different capillaries… independent of
    scale. So now we come to the problem here, which is, so how does the body code for that?… And
    this is where you immediately run into trouble. What's a world we're sort of oriented to in a
    purely reductive world? There is some sort of set of rules telling [an] aorta that's growing
    like this that there is some gene or genes which specify the point where this bifurcates…
    another type of gene that specifies the next one."

---

## §K Held-out discovery — pass 3

Lecture 21, *Chaos and Reductionism*, read cold: never opened in pass 1 or 2, and newly punctuated
by local transcription. Six moves found (§B-13 to §B-18), and two of them matter.

**§B-17 supplies the mechanism the dossier was missing.** Pass 1 recorded that he "names the bucket,
then dissolves it" but never showed *how* the dissolving is done. Here it is: he constructs the
reductive account in its own terms and keeps constructing it — a gene for this branch point, a
different gene for the next, different genes again for the same pattern in a single neuron — until
the enumeration collapses under its own bookkeeping. The refutation is the build-out, not a
counter-argument.

**§B-13 is the kind of thing only a cold read finds.** He opens the hardest unit of his course by
saying he is not sure he fully understands it. Nothing in a frequency count would surface that, and
it recasts the register: the levels device is not delivered from above but worked through in front
of the room.

**Status: Sapolsky is complete at pass 3 of 3**, as a device source. His hired-for technique is
confirmed as the only device present in all 25 lectures (§J), its mechanism is now evidenced
(§B-17), and §D rests on 50,151 words of real transcription rather than on captions. All four
method lectures are now in: the figures moved only slightly from the two-lecture reading (mean
15.3 → 16.1, questions 9.5% → 8.9%) and the speech rate held at 160 across every one. One cell
stays open — the
mid-sentence pause fraction, which needs punctuation and word timings joined — and it is a tooling
gap, not a gap in him.
