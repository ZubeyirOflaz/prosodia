# Docket 03 — Is a trained model personal data?  ·  compiled 2026-09-16

Written for **Episode 1 (The Same File, Twice)**, which the plan marked as **not plannable** — five
`[OUTSIDE DOCKET]` items, over the budget of three. This closes the three that decide the episode's
question. Two remain open and are named at the end.

**Provenance.** Located by web search on 2026-09-16 against curia.europa.eu, edpb.europa.eu and
arXiv records. Bibliographic details verified; interpretive summaries are the compiler's. Nothing
read in full.

---

## The regulator's answer, and it is deliberately unfinished

**European Data Protection Board, Opinion 28/2024 on certain data protection aspects related to the
processing of personal data in the context of AI models, adopted 17 December 2024.** *Verified:
body, opinion number, exact subject, date; PDF at
`edpb.europa.eu/system/files/2024-12/edpb_opinion_202428_ai-models_en.pdf`.* Issued on a request
from the **Irish** supervisory authority, which matters: Ireland supervises most of the large model
providers established in the Union.

**Four questions were asked.** When and how an AI model can be considered **anonymous**; how a
controller demonstrates **legitimate interest** in the development phase; the same in the
deployment phase; and what follows for a model when the **development processing was unlawful**.

**The holding on anonymity, and it is the episode's hinge.** A model trained on personal data
**cannot in all cases be considered anonymous**. Anonymity is assessed **case by case**. A model
may be anonymous where the probability of extracting personal data from it — **directly, or
through queries** — is **negligible for each data subject**.

> **Read what that test actually demands.** It is not a property of the model, it is a claim about
> what an adversary can get out of it. So it is falsifiable by experiment, and someone has run the
> experiment. That is the next entry.

---

## The experiment that the test has to survive

**Milad Nasr, Nicholas Carlini, Jonathan Hayase, Matthew Jagielski, A. Feder Cooper, Daphne
Ippolito, Christopher A. Choquette-Choo, Eric Wallace, Florian Tramèr and Katherine Lee, "Scalable
Extraction of Training Data from (Production) Language Models", arXiv:2311.17035, submitted
28 November 2023.** *Verified: title, arXiv number, submission date, and the author list.*

**What they did.** Extracted training data from open models (Pythia, GPT-Neo), semi-open ones
(LLaMA, Falcon) and a closed production one (ChatGPT). Against the aligned model they used a
**divergence attack** — pushing it off its chatbot register — which emitted training data at
roughly **150 times** the rate of ordinary use. They disclosed to OpenAI and waited ninety days
before publishing.

**Why it belongs in this episode and not a technical one.** The EDPB's test turns on whether
extraction probability is negligible. This is the field's own measurement of that probability, by
named researchers, on a production system, with a date. The episode does not need to teach the
attack; it needs the listener to understand that **the legal test was written in terms the
engineering literature can answer, and the answer is not "negligible" by default.**

⚠ *The 150x figure is the paper's own, for one attack on one model at one time. Date-stamp it and
do not generalise it to models in 2026.*

---

## And then the Court moved the ground

**Case C-413/23 P, *European Data Protection Supervisor v Single Resolution Board*, Court of
Justice, judgment of 4 September 2025.** *Verified: case number, parties, court, date; Curia press
release `cp250107en.pdf`, and EUR-Lex CELEX 62023CJ0413.*

**The facts, and they are pleasingly concrete.** After the resolution of **Banco Popular Español**
on 7 June 2017, the Single Resolution Board ran a procedure letting former shareholders and
creditors comment on a preliminary compensation decision. It passed some of those comments, in
**pseudonymised** form, to **Deloitte**, which was valuing the effects of the resolution.

**The holding.** Pseudonymised data is **not automatically personal data for every party**.
Whether it is depends on whether **the recipient** can reasonably re-identify, judged on technical,
organisational and legal factors. So the same file can be **personal data in the hands of the
sender and not in the hands of the receiver**. The Court set aside the General Court's judgment.

This is the first time the Court has said so explicitly, and it **departs from the long-standing
position of data protection authorities**, who had treated pseudonymised data as personal data
always and everywhere.

> **This is the collision, and it is why the episode is called "The Same File, Twice".** The EDPB
> opinion (December 2024) reasons from what can be got out of a thing. The Court (September 2025)
> reasons from **who is holding it**. Both are live. The Court is later and it binds. An episode
> that gives only the EDPB test teaches a rule the Court has since relativised; an episode that
> gives only the Court teaches a relativity the EDPB has not accepted for models. **Give both, in
> date order, and say plainly that the relationship between them is unsettled.**

⚠ **Do not overstate the Court.** It ruled on a transfer of pseudonymised comments to an auditor,
not on model weights. Whether its relative approach reaches a trained model is exactly the open
question — and saying so out loud is the episode, not a hedge.

---

## The last two, closed — addendum of 2026-09-20

Both were listed below as still open. Both are now held, and the section that follows is left in
place as the record of what was missing. **Episode 1 is fully sourced.**

### Memorisation, and membership inference — the field's own terms

**Nicholas Carlini, Daphne Ippolito, Matthew Jagielski, Katherine Lee, Florian Tramèr and Chiyuan
Zhang, "Quantifying Memorization Across Neural Language Models", *International Conference on
Learning Representations (ICLR) 2023*; arXiv:2202.07646.** *Verified: authors, exact title, venue,
arXiv number.*

**Memorisation, operationally.** A model has memorised a string from its training data when,
prompted with the text that preceded it, the model **emits that string verbatim**. The paper's
point is that this is a **measurable quantity**, not a yes-or-no property, and it **grows** with
three things: the **size of the model**, the **number of times the example was duplicated** in the
training data, and the **length of the context** used to prompt.

> **Why that third finding is the one for this episode.** It means the same model can look
> memorisation-free under a short prompt and reproduce training data under a longer one.
> **Whether a model has memorised something is partly a fact about how hard you tried** — which is
> exactly the shape of the EDPB's "means reasonably likely to be used" test, arrived at
> independently by people measuring something else.

**Membership inference.** **Reza Shokri, Marco Stronati, Congzheng Song and Vitaly Shmatikov,
"Membership Inference Attacks Against Machine Learning Models", *IEEE Symposium on Security and
Privacy (S&P) 2017*.** *Verified: all four authors, exact title, venue, year.* Given a data record
and **black-box access** to a model, determine **whether that record was in the model's training
set**. It exploits the fact that models behave measurably differently on data they were trained on
than on data they are seeing for the first time.

**Keep the two apart, because they answer different legal questions.** Memorisation asks *can the
content be got out*. Membership inference asks *can it be established that a particular person's
record was in there at all* — which is a disclosure about that person even when nothing they wrote
comes back. **The second is the harder one for the anonymity claim**, and it is the quieter of the
two, so give it its own sentence rather than folding it into the first.

### GEMA v OpenAI — and it says more than corroboration

**Landgericht München I (Munich Regional Court I), *GEMA v OpenAI*, 42 O 14139/24, judgment of
11 November 2025.** *Verified: court, case number, date, parties, and the holdings below, from
multiple independent reports including the Council of Europe's Merlin database, EUIPO's case-law
service and several firms' notes.*

**The facts.** GEMA, the German collecting society, sampled ChatGPT and found that the model,
when prompted, **reproduced song lyrics of GEMA-affiliated writers** — sometimes exactly, sometimes
slightly altered. The lyrics were not freely available online with the rightsholders' consent.

**The holding.** **Memorisation of a work in the model is itself an act of reproduction** — both
where the work is held in the model and where it is delivered to a user on a prompt. The
**text-and-data-mining exception** covered the creation of the training corpus but **did not
extend to the training of the model itself**. OpenAI was ordered to desist, to pay damages, and to
give information about the scope of use and the revenue.

> ⚠ **The plan uses this for ONE SENTENCE of technical corroboration, and that limit should hold —
> but the sentence available is stronger than the plan assumed.** This is a court, in a Member
> State, finding as a fact that the model reproduced protected text on a prompt, and holding that
> **the memorised content is in the model**. For an episode asking whether personal data is
> retained in a model, that is a judicial finding about the underlying mechanism, reached under a
> different instrument.
>
> **And that is exactly why it must not be over-read.** It is **copyright**, not data protection;
> it is a **Regional Court**, not the Court of Justice; and the plan's own deferral rule puts the
> copying question in a later series. **One sentence, the court named, the date given, and the
> instrument named as a different one.** ⚠ Reported as under appeal in some accounts — do not
> state it is final.

---

## Still open for Episode 1 — two of the five

Both were marked `[OUTSIDE DOCKET]` by the plan and remain so. Neither blocks the episode, and each
is used for one sentence:

- **Landgericht München I, *GEMA v OpenAI*, 42 O 14139/24, judgment of 11 November 2025** — cited
  as one sentence of technical corroboration that models reproduce training material, not taught.
  Needs the court, case number, date and what was actually held.
- **A definition of memorisation and of membership inference** from the extraction literature, so
  the operational description can be checked against the field's own terms rather than the
  compiler's.

With those two the episode is fully sourced. Without them it is writable, because the three above
carry the argument and the plan's remaining markers are correctly flagged.

## Elsewhere in the series, still unsourced

`02` already records these; repeated here because Episode 1's plan is the only one now closed:
the DSA, DMA, Data Act and copyright episodes have **no instance at all**; there is nothing on the
withdrawn AI Liability Directive; and there is no post-SCHUFA Article 22 case law in this docket.
