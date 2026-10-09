# Docket 06 — Enforcement, injury, and who has to prove it  ·  compiled 2026-09-20

Written for **Episodes 7, 8, 9 and 10** — every remaining episode of the series. Nine
`[OUTSIDE DOCKET]` items across the four. **Two of them were never research problems**: GDPR
Art. 82 is already held verbatim in `01`, and the Product Liability Directive's open-source
exclusion was one command away from a file we already had cached. Both are copied across below.

**Provenance.** The two operative-text sections are **verbatim from EUR-Lex**, extracted on
2026-09-20 from the cached consolidated HTML with the completeness guard reporting no loss.
Everything else was located by web search on 2026-09-20 against NTSB, Law Commission, EUR-Lex,
Oxford Academic and practitioner records. Bibliographic details verified; interpretive summaries
are the compiler's. Nothing outside the operative text has been read in full.

⚠ **This file contains three numbers that sources disagree about and two that are moving weekly.**
Each is marked. The rule for all of them is the same and it is the series' own: **give the figure
with its source and its date, or give the shape without the figure.** Never average two sources.

---
---

# PART ONE — Episode 7 (Two Assessments, One System)

## Who was actually appointed, and the honest answer is that it is a mess

Member States had until **2 August 2025** to designate their **national competent authorities**
under the AI Act — a **market surveillance authority** and a **notifying authority** — and to name
a **single point of contact**. *Verified: the deadline and the two authority types (AI Act
Art. 70).*

**What the reporting says, and it does not agree with itself:**

| Reported | Figure |
|---|---|
| Member States having designated **both** a market surveillance and a notifying authority | **9** |
| Member States that **missed** the deadline for competent authorities | **at least 12** |
| Member States that had **not** appointed a single point of contact | **19** |
| Member States having **formally designated** a single point of contact to the Commission (2026 reporting) | **8** |

🔴 **Read that table as evidence of a state of affairs, not as four facts.** The counts are taken
at different dates, against different obligations, by different counters. **The episode must not
present them as a series.** Pick **one** figure, name who counted it and when, and say the rest in
shape: *more than a year after the deadline, a substantial minority of Member States had still not
completed the designation, and the counts themselves disagree.*

⚠ **The plan asks for "how many named their data protection authority". THAT NUMBER IS NOT
ESTABLISHED HERE**, and it is the one the episode most wants. **Do not estimate it.** The episode
can make its point without it: the question of *whether* data protection authorities should hold
this role has a named answer, and that is the next entry.

> **Why the absence is usable rather than a hole.** The plan's beat is *two assessments, one
> system*. The strongest version does not need a count — it needs the fact that **the instrument
> presupposes an authority that in a substantial minority of Member States had not been named**, at
> a point where its obligations were already running. **An institution that does not exist yet
> cannot coordinate with anybody**, and that is the collision, stated without a disputed number.

---

## The named argument for giving the job to the data protection authorities

**Joanna Mazur, Claudio Novelli and Zuzanna Choińska, "Should data protection authorities enforce
the AI Act? Lessons from EU-wide enforcement data", *International Data Privacy Law* **16(1)**,
March 2026, article `ipaf033`.** *Verified: all three authors, exact title, journal, volume, issue,
month, year, article number; Oxford Academic.* This closes the plan's marker — **the empirical
claim now has its holders, its journal and its date.**

**What they did, and it is why this is an empirical citation and not an opinion piece.** They
examined **how actively data protection authorities already enforce** data protection rules in
cases concerning **AI-based products and services and automated decision-making systems**, across
the Union.

**What they recommend.** That data protection authorities be included as **market surveillance
authorities** for high-risk systems under **Annex III, points 3 to 5** of the AI Act. Note the
narrowness — *three points of one annex*, not the whole regime. **Report the narrowness; it is what
makes the proposal serious rather than territorial.**

> **The beat this supports.** The episode's question is whether two assessments of one system, run
> by two authorities under two instruments, converge or collide. Here is a team arguing from
> enforcement data that the answer is to **merge part of the job** — and confining the merger to
> the categories where the data protection authorities already have a track record. **That is an
> argument from evidence about capacity, which is exactly what the plan asked for.**

⚠ **Not read in full.** The summary above is of the abstract and the authors' stated contribution.
**Do not characterise their data set, their method or their sample size** — none of that is
established here.

---
---

# PART TWO — Episode 8 (A Product Now)

## The opening instance, in the investigators' own findings

**Tempe, Arizona, the night of 18 March 2018.** A modified **Volvo XC90** operating in the **Uber
Advanced Technologies Group** test programme struck and killed **Elaine Herzberg**, who was
crossing the road away from a crosswalk, pushing a bicycle. *Verified: date, place, vehicle, the
operator's programme, and the victim's name, from the National Transportation Safety Board's
investigation as reported.*

**The sequence, which is the whole reason this instance was chosen:**

- **Radar detected her roughly six seconds before impact**, with the lidar following almost
  immediately. **She was seen. The system had six seconds.**
- The system **could not classify an object as a pedestrian unless it was near a crosswalk.** She
  was not near one.
- For about **five seconds** the classification **alternated** between *vehicle*, *bicycle* and
  *unknown object*.
- **Each reclassification threw away the track history** — and with it the prediction. Classified
  as a vehicle or a bicycle, the system assumed she was travelling **in the same direction, in the
  neighbouring lane**. Classified as an unknown object, it assumed she was **static**.
- The **Volvo's own factory emergency braking was disabled** while the test system was engaged.
- Uber's system was configured to **wait one full second before initiating emergency braking**.

**The probable cause, as determined.** The **operator's failure to monitor** the driving
environment, because she was **visually distracted** — streaming a television programme on a phone.
Contributing factors included Uber ATG's **inadequate safety culture**.

> **Why this instance and not a cleaner one, and the writer must hold both halves.** The plan wants
> a system whose *defect* is hard to locate. Here it is, laid out by investigators: nothing
> malfunctioned. The radar worked. The lidar worked. The classifier returned an answer every time —
> **just a different one, six times in five seconds**. The defect is in the **design of how those
> answers were used**, the **disabling of a working safety system**, and a **one-second delay
> written in on purpose**.
>
> **And the official probable cause was the human being in the driver's seat.** *State both.* An
> episode that gives only the software design is arguing with the investigators; an episode that
> gives only the finding wastes the instance. **The gap between "the probable cause was the
> distracted operator" and "the vehicle saw her for six seconds" is the episode.**

⚠ **Three cautions.** This is **American**, under **American** law, and the revised Directive would
not have applied to it — **say so**, because the episode uses it as a fact pattern, not a
precedent. ⚠ **The NTSB report number is not established here** — refer to "the National
Transportation Safety Board's investigation", not to a docket number. ⚠ The "six times in five
seconds" phrasing above is the **compiler's** compression of *alternated between three
classifications over about five seconds*; **the precise number of transitions is not established**,
so say *repeatedly* unless somebody reads the report.

---

## The open-source exclusion, verbatim

Closed from our own cached source, not from a summary. **Directive (EU) 2024/2853, Article 2 —
Scope**, verbatim from EUR-Lex (CELEX `32024L2853`), extracted 2026-09-20:

```text
Article 2
1. This Directive shall apply to products placed on the market or put into service after 9 December 2026.
2. This Directive does not apply to free and open-source software that is developed or supplied outside the course of a commercial activity.
3. This Directive does not apply to damage arising from nuclear accidents in so far as liability for such damage is covered by international conventions ratified by Member States.
4. This Directive does not affect:
(a) the applicability of Union law on the protection of personal data, in particular Regulation (EU) 2016/679 and Directives 2002/58/EC and (EU) 2016/680;
(b) any right which an injured person has under national rules concerning contractual liability or concerning non-contractual liability on grounds other than the defectiveness of a product as provided for in this Directive, including national rules implementing Union law;
(c) any right which an injured person has under any special liability system that existed in national law on 30 July 1985.
```

**Two things in Article 2 that the plan's variant 5 needs, and one it did not ask for.**

- **The exclusion is Art. 2(2)**, and the load-bearing words are **"outside the course of a
  commercial activity"** — *not* "open source". Free and open-source software supplied **in** the
  course of a commercial activity is **inside** the Directive. **The plan's variant asks what
  happens when the software is free and open source; the answer is that the licence does not
  decide it — the commercial activity does.**
- **Art. 2(4)(a) is the series' own seam, written into the text**: this Directive does not affect
  the applicability of the GDPR. **Two instruments, one machine, and the later one says so in
  terms.** That is a one-sentence gift for an episode about layering.

**Also held, and it answers the plan's "as enforced" beat directly.** **Article 22(1)**: Member
States shall bring the necessary measures into force **by 9 December 2026**.

---

## Transposition, as at the week of compiling

**Deadline: 9 December 2026** (Art. 22(1)), and the Directive applies only to products placed on
the market **after** that date (Art. 2(1)). At the date of this file — **20 September 2026** — that
is **under twelve weeks away and it has not yet passed.**

**Reported as at mid-September 2026:** **three** Member States have completed transposition —
**Hungary, Croatia and Lithuania** — with about **twelve** more advancing draft legislation. Several
have taken preparatory steps without publishing a draft, and several have no known public progress.
⚠ **This is practitioner tracking, not a Commission count, and it moves weekly. Date-stamp it to
mid-September 2026 or give the shape without the number.**

> **The beat this makes available, and it is stronger than a complaint about delay.** The plan says
> nothing has been decided under this Directive and nothing can be. **Now say why, precisely: the
> instrument does not reach a single product placed on the market before 9 December 2026, and as
> the series is recorded that date has not arrived.** Not a backlog. Not under-enforcement.
> **An instrument whose first eligible product does not yet exist.** Everything the episode teaches
> about defect and burden of proof is teaching about a regime that has not yet had a case — and
> saying that plainly is more honest, and more interesting, than implying a body of practice.

---
---

# PART THREE — Episode 9 (Who Has to Prove It)

## The opening instance — Horizon, and the presumption underneath it

**The Post Office Horizon scandal**, England and Wales. Between **1999 and 2015** the Post Office
prosecuted sub-postmasters for theft, fraud and false accounting on the strength of shortfalls
reported by **Horizon**, an accounting system supplied by **Fujitsu**. *Verified: the parties, the
system, the supplier, the period and the nature of the prosecutions.*

⚠ **THE NUMBERS CONFLICT AND THE EPISODE MUST NOT SPLIT THE DIFFERENCE.** Reported figures include
**736** prosecutions between 1999 and 2015, and **more than 900** between 1999 and 2015 (elsewhere
given for 2000–2015), with **236** people imprisoned. **Use one figure, attribute it, and say the
counts differ** — or say *hundreds*, which every source supports. Given the episode's own subject
is evidential reliability, **being visibly careful with this number is a demonstration of the
episode's thesis**, not a hedge.

**The evidential rule, and this is the part that makes it a Series B episode.**

- **Section 69 of the Police and Criminal Evidence Act 1984** required that a computer-produced
  document, to be used in evidence in a criminal trial, be **accompanied by proof that the computer
  was operating properly** and was not improperly used. **The burden sat on the party relying on
  the record.**
- In **1997** the **Law Commission**, in *Evidence in Criminal Proceedings: Hearsay and Related
  Topics*, concluded that s. 69 served **"no useful purpose"** and recommended it be **repealed and
  not replaced** — the effect being that, **in the absence of evidence to the contrary, courts
  would presume that mechanical instruments were in order at the material time.**
- **Section 69 was repealed by the Youth Justice and Criminal Evidence Act 1999.**

> 🔴 **And here is the fact that makes this the right opening instance for an episode about who has
> to prove what.** **The Post Office supported the repeal.** It responded to the Law Commission's
> consultation in favour of removing the requirement — and then, for the next decade and a half,
> prosecuted its own sub-postmasters on computer evidence that it no longer had to prove was
> working.
>
> **Handle this at exactly its weight.** It is sourced to reporting of a freedom-of-information
> response and to commentary, **not to a document this compiler has read**, so attribute it as
> reported. And resist the prosecutorial tone: the point is not corporate villainy, it is
> **structural** — *a burden of proof was moved, by a reform that looked technical, and the party
> that benefited had asked for it.* That is the episode's thesis arriving in its first five
> minutes, which is exactly where the plan wants it.

⚠ **This is English law, not Union law.** The episode must say so. It is here because it is the
clearest documented instance in any European jurisdiction of **a presumption about machine
reliability producing a mass miscarriage of justice** — which is what the Directive's burden-of-
proof provisions are answering. **Do not imply the GDPR or the PLD applied to it.**

---

## The instrument that was going to do this, and was withdrawn

**Proposal for a Directive on adapting non-contractual civil liability rules to artificial
intelligence (the AI Liability Directive), COM(2022) 496, presented 28 September 2022.**
*Verified: exact title, document number, date; EUR-Lex CELEX `52022PC0496`.*

**The withdrawal, with all three dates the plan asked for:**

- **11 February 2025** — listed for withdrawal in **Annex IV of the Commission Work Programme
  2025**, the stated reason being **"no foreseeable agreement"**.
- **16 July 2025** — the Commission's **2533rd meeting**, at which the withdrawal was taken.
- **6 October 2025** — **notice of the withdrawal published in the Official Journal.**

> **Why the dates are the beat and not the background.** The plan's mid-episode turn is that the
> instrument built to shift the burden for **fault-based** claims against AI systems **does not
> exist**. The three dates let the episode say how a proposal dies in the Union: not by a vote
> against it, but by appearing in an annex, then in a minute, then in a notice. **Three
> administrative steps over eight months, and no debate at the end of it.** ⚠ *That characterisation
> is the narrator's; the dates are sourced.*

---

## GDPR Article 82 — already held, copied across

The plan's marker says: *"if the docket does not supply it, this beat is cut rather than
reconstructed."* **It does supply it.** `01_operative_text.md` holds **Article 82 — Right to
compensation and liability** verbatim from EUR-Lex. **The beat is not cut. Quote it from `01`,
which is the authoritative extraction; do not restate it from here.**

> **And note what the pairing gives Episode 9.** The GDPR has a **compensation route** with a
> reversed-ish burden on the controller; the revised PLD has **disclosure of evidence** (Art. 9) and
> **a presumption of defectiveness** (Art. 10), both held in `01`; and the instrument that would
> have done the same for fault-based AI claims was withdrawn. **Three routes, two of them live, one
> of them gone — and Horizon showing what happens when the burden sits the other way.** The episode
> has everything it needs.

---
---

# PART FOUR — Episode 10 (VERDICT — Layers)

## The Omnibus status, consolidated

Episode 10's single outside item is the Digital Omnibus, and **docket `04` Part Two already closes
most of it**. Gathered here so the verdict's writer does not have to reconstruct it:

- **The package split.** The **AI strand** was **adopted**; the **GDPR strand** was not.
- **AI strand:** Council and Parliament reached agreement **7 May 2026**; **Council adopted
  29 June 2026**; **Regulation (EU) 2026/1744 of 8 July 2026** (OJ L, 24.7.2026), **applying from
  27 July 2026**. It **deleted AI Act Art. 10(5)** and inserted a broader **Art. 4a** — held
  verbatim in docket `04`.
- **Data strand (the GDPR half):** **still in negotiation**, with a committee vote not expected before early 2027 (re-checked 5 October 2026). Proposed
  **Art. 88c** (a legitimate-interest route for AI development and operation, with enhanced
  transparency and an unconditional right to object) and a residual special-category exemption.
  **Not adopted. Article 9 is unamended.**
- **The objections:** **EDPB–EDPS Joint Opinion 1/2026** (on the AI strand) and **Joint Opinion
  2/2026** (on the Digital Omnibus generally), **February 2026**.

### RE-CHECKED 5 October 2026 — and the answer sharpened

The standing instruction was to re-verify in the week Episode 10 is written. Done on **5 October
2026**. **The data strand is still not adopted, and the picture is now more definite than "in
negotiation":**

- **A vote in the ITRE–LIBE committees is envisaged at the beginning of 2027.** Not a plenary vote
  — a **committee** vote. The GDPR half has not reached the stage the AI half cleared in March 2026.
- For contrast, the AI half's path: committees (IMCO–LIBE) adopted a joint negotiating position
  **18 March 2026**; provisional political agreement **7 May 2026**; Council adopted **29 June
  2026**; **Regulation (EU) 2026/1744 of 8 July 2026**, applying **27 July 2026**.
- Reported indications that **several Member States share the supervisory authorities' concerns**
  about narrowing the GDPR's material scope, and that the Council's own working text drops some of
  the proposed consent provisions. ⚠ *Reported, not verified against a Council document.*

> 🔴 **This is the verdict's strongest single fact and it was not available when the plan was
> written.** The two halves of one package were proposed together in November 2025. **The half that
> eases obligations on industry was law within eight months. The half that would reconcile it with
> the rights instrument is not expected to reach a committee vote until 2027.** That is not a claim
> about anyone's motives — it is a sequence, with dates, that the episode can simply lay out.
>
> **And it answers the series' question in the series' own terms.** Episode 3 left a deployer told
> by one Regulation that it may exceptionally process special categories, and by another that such
> processing shall be prohibited. **As at October 2026 that contradiction is over a year old and
> has at least another year to run.** Layering did not produce a contradiction that was promptly
> fixed; it produced one that is being fixed at two different speeds.

⚠ **One nuance to get right, correcting docket `04`.** `04` records the EDPB and EDPS as not
considering a specific legitimate-interest provision necessary. The fuller position is narrower
than flat opposition: **Joint Opinion 2/2026 accepts legitimate interest as a basis for AI
development while asking for stronger safeguards**, and says the proposed **Art. 88c does not
clarify the matter** it was meant to settle. **Do not say the authorities opposed the basis. Say
they accepted it and said the drafting does not do the job** — which is a more damaging criticism
and a fairer one.

⚠ **THIS IS THE MOVING PART OF THE SERIES AND IT IS THE VERDICT EPISODE.** The plan already says
so: if the data half has been adopted by the time of writing, **the opening changes**. **Re-check
the status in the week Episode 10 is written** — everything above is as at 20 September 2026.

> **What the split does to the verdict, and it is better than the plan's version.** The plan's
> question is whether layering protects anybody. **The Omnibus is now evidence on that question
> rather than a postscript to it**: the layer that was *simplified first* was the one on industry,
> adopted inside fourteen months; the layer that would have reconciled it with the rights instrument
> is **still being negotiated**. **One half of a reconciliation passed.** An episode asking whether
> layers protect people has been handed a natural experiment in which order the layers move.

---
---

## What no episode in this series will have

Stated once, plainly, so no plan or script reaches for it:

- **How many Member States named their data protection authority** as market-surveillance authority
  under the AI Act. Not established. Episode 7 works around it.
- **A Commission count** of PLD transposition. Only practitioner tracking, dated mid-September 2026.
- **A decided case under the revised PLD.** There cannot be one before 9 December 2026.
- **The NTSB report number**, and the exact count of classification transitions.
- **Post-SCHUFA Art. 22 case law** beyond C-203/22, which is an Art. 15 case.
- **The DSA, DMA, Data Act, Data Governance Act and copyright instruments** — no operative text, no
  documented controversy. The plan's Series C sketches depend on research that does not exist yet.
