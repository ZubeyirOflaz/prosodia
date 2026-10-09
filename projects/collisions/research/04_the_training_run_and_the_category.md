# Docket 04 — The training run, and the category  ·  compiled 2026-09-20

Written for **Episode 2 (A Reason to Touch It)** and **Episode 3 (The Category It Cannot Ask
For)**, both of which the plan marked **NOT YET WRITABLE** — three `[OUTSIDE DOCKET]` items each.
This closes all six. **Episode 4 (Solely) was checked and carries no outside items**; it is already
writable on `01` and `02`.

**Provenance.** Located by web search on 2026-09-20 against curia.europa.eu, edpb.europa.eu,
dataprotection.ie, ACM, arXiv and contemporaneous trade press. Article 4a below is **verbatim from
EUR-Lex**, not from a summary. Bibliographic details are verified; interpretive summaries are the
compiler's. Apart from the operative text, nothing here has been read in full.

**Two findings in this file contradict the plan.** They are flagged 🔴 where they appear, and the
plan has been corrected against both. Neither weakens its episode; both sharpen it.

---
---

# PART ONE — Episode 2

## The opening instance: a regulator goes to court

**Data Protection Commission v Twitter International Unlimited Company**, High Court of Ireland,
proceedings issued **8 August 2024**, struck out **4 September 2024**. *Verified: the parties, both
dates, the statutory power, and the terms of the undertaking, from the DPC's own statements.*

**What happened, in order.**

1. Around **25–26 July 2024** users noticed a setting on X, **on by default**, opting their public
   posts and their Grok interactions into training. (Entry two below.)
2. The DPC brought **urgent High Court proceedings on 8 August 2024** under **section 134 of the
   Data Protection Act 2018**, seeking suspension of the processing of EU and EEA users' public
   posts for training Grok.
3. X agreed to suspend. On **4 September 2024** the proceedings were **struck out** on TIUC giving
   a **permanent undertaking**.
4. **The undertaking covered the past as well as the future**: data from posts made between
   **7 May 2024 and 1 August 2024** that had been used to develop, refine or train Grok **would be
   deleted and not further processed**.

**Why the DPC itself said this mattered.** It was the **first time a lead supervisory authority had
taken court proceedings of this kind**, and the first exercise of the DPC's section 134 power.

> 🔴 **CORRECTION TO THE PLAN, and the episode is better for it.** The plan's move line reads:
> *"a regulator goes to court to stop a training run that has already happened — and comes away
> with a promise about the future and nothing at all about the past."* **The second half is wrong.**
> The undertaking expressly reached the past: the data was to be deleted.
>
> **The true version is sharper.** The regulator got the **data** deleted. It did not get — and on
> the public record did not ask for — anything about the **model that had already been trained on
> it**. So the move is not "nothing about the past". It is: *the past was addressed by deleting the
> copy, and the thing the copy was used to build was left standing.* That is the question the
> episode hands to the third entry in this part, and it is a genuine open question rather than a
> regulator's oversight. **Write it that way.**

⚠ **Two things not established here**, and neither should be asserted: the identity of the
complainants whose complaints preceded the action (the plan's cast lists "the consumer
organisations who complained" — *either source that or cut it to "complaints"*), and whether the
undertaking's wording bound xAI as a separate legal person or only TIUC. **If the script needs the
provider/platform split as a legal fact, it does not have it.** It can still make the point
generically, as the plan's cast already does: "the model developer, which may be a different legal
person in the same group".

---

## The operator's own account of the pipeline

The plan asks for "the field's own account of what was trained on and when", with its own caveat
attached — *the operator's description of its own pipeline is evidence about the operator, not
about the system*. That caveat is exactly right and this entry is built to respect it.

**What the setting said**, as reported contemporaneously and as it appeared to users: *"Allow your
posts as well as your interactions, inputs, and results with Grok to be used for training and
fine-tuning"*, with the accompanying note that such data **"may be shared with our service provider
xAI for these purposes"**. It was **enabled by default** and applied to existing accounts without a
prior announcement. *Verified: the existence, default-on state and substance of the setting, widely
and consistently reported from 26 July 2024, including Forbes, 26 July 2024.* ⚠ **The quoted
wording is from reporting of the interface, not from a first-party document retrieved by this
compiler. Treat it as the reported wording and attribute it as such, or paraphrase.**

**A later change, and it is a good one-sentence beat.** In **October 2024** X updated its privacy
policy to permit **third parties** to train on users' posts. *Verified: reported 17–18 October 2024
by TechCrunch and The Register.* The point for the episode is structural, not gossip: the
corpus-sharing question is a different question from the training question, and the policy moved
first.

> **What this entry is FOR, and the writer must keep to it.** The plan's operative beat is *keep
> training and retrieval apart*. This entry supplies the operator's description of the **training**
> side only. It supplies **nothing** about how the corpus was filtered, de-duplicated or selected,
> and **nothing** about retrieval at inference time. The plan's "system, described operationally"
> beat describes a **generic** pipeline — selection, filtering, de-duplication, a training run,
> and separately retrieval — and that is the right level. **Do not attach the generic pipeline
> description to X as though it were reported fact about X.** Describe the generic pipeline
> generically, then say what this operator actually said about itself, which is one sentence about
> a checkbox.

⚠ **Do not state a corpus size, a number of posts, a model version or a training-run date.** None
is established here and all are guessable-sounding.

---

## What follows if the development processing was unlawful

**European Data Protection Board, Opinion 28/2024**, adopted **17 December 2024** — already in the
docket at `03`, where the **first** of its four questions (anonymity) is set out. **This closes the
fourth question.** *Verified: the four scenarios and the Board's position on each, against the
Opinion and multiple independent summaries of it.*

**The question.** What are the consequences of **unlawful processing of personal data in the
development phase** for the **subsequent** phases — in particular deployment?

**The Board takes three scenarios, and the third is the one that bites.**

1. **The data is retained in the model and the same controller goes on processing it.** The
   supervisory authority's corrective powers are in play, including an **order to delete**. If
   deletion is ordered, further processing is prohibited — which may **limit or halt the model's
   use**, with economic consequences. And separately: the failure to justify the **first**
   processing may **affect the balancing exercise for the second**. *A controller cannot enter the
   legitimate-interests balance for deployment with clean hands it does not have.*
2. **The data is retained in the model and a different controller deploys it.** That second
   controller must **satisfy itself that the development processing was not unlawful** — including
   by examining the source of the data and checking for prior decisions of supervisory authorities
   or courts. **A duty of inquiry, on the buyer.**
3. **The model has been anonymised before any further personal-data processing occurs.** Then the
   unlawfulness of the original processing **should not affect the subsequent operation of the
   model**, because that operation no longer involves personal data.

> **This is the episode's closing mechanism and it should be built deliberately.** Read scenario 3
> against Episode 1. Episode 1 established, on this same Opinion, that a model trained on personal
> data **cannot in all cases be considered anonymous** — anonymity is assessed case by case, and
> turns on whether extraction is negligible. So scenario 3 is the escape hatch, and **Episode 1 has
> already taught the listener how hard it is to walk through.** The callback is available and it is
> earned: *the way out of an unlawful training run is to show the model is anonymous, and we spent
> the last episode on how hard that is to show.*

**And it answers Grok directly.** Deleting the corpus (the undertaking) is not the same as dealing
with the model. On the Board's own framework the model is addressed only if it is anonymous, or by
a deletion order that reaches it. **The undertaking did neither.** *That is the compiler's reading
of two sourced facts placed side by side, not a holding by anybody — mark it as the narrator's
inference when it is spoken.*

⚠ **The Opinion is an opinion.** It binds nobody the way a judgment does. Say what it is: the
Board's view, dated December 2024, issued at the request of the Irish authority.

---
---

# PART TWO — Episode 3

## The opening instance: the form that answered a question it never asked

**Case C-184/20, *OT v Vyriausioji tarnybinės etikos komisija*, Court of Justice of the European
Union, Grand Chamber, judgment of 1 August 2022.** *Verified: case number, parties, court,
formation, date; EUR-Lex CELEX `62020CJ0184`.* The respondent is the Lithuanian **Chief Official
Ethics Commission**; the case came from the **Regional Administrative Court of Lithuania**.

**The facts, and they are exactly the fact pattern the persona wants.** Lithuanian
anti-corruption legislation required heads of bodies receiving public funds to file a
**declaration of private interests**, and required the content of those declarations to be
**published online**. The declaration included data relating to the declarant's **spouse,
cohabitee or partner**, naming them. OT, the head of such a body, did not file. He challenged the
publication requirement.

**The holding that matters here.** Publication of personal data **liable to disclose indirectly**
the sexual orientation of a natural person **constitutes processing of special categories of
personal data** within Article 9. The Court reasoned that from the name of a spouse, cohabitee or
partner, **information about the sex life or sexual orientation of the declarant and of that
partner may be deduced** — and that data **liable indirectly to reveal** sensitive information is
**not excluded** from the Article 9 regime. A narrow reading, confined to data that is intrinsically
sensitive on its face, would **undermine the effectiveness** of the protection.

> **This is why the word "revealing" is the episode's load-bearing term, and now it has a court
> behind it.** The plan says *"this one word is the whole episode"* and it was, until now, the
> plan's own assertion. It is the Grand Chamber's. **The episode can say: a form that asked for a
> name, and thereby processed data about sexual orientation, because the category can be deduced
> from the answer.** No prediction, no model, no proxies — just a household and a register. The
> listener meets the principle in its simplest possible instance before the machine arrives.

**Keep the limit visible.** This is about **publication** — a disclosure liable to reveal — and
the deduction is one an ordinary reader makes. It is **not** a holding that a statistical
prediction of a protected attribute is Article 9 processing. The plan already says so in its
contested joints (*"it was about publication, not prediction"*) and that formulation is accurate;
keep it. The judgment moves the boundary from *stating* to *revealing*; whether it reaches
*predicting* is the open question, and the episode's honesty depends on the gap being audible.

⚠ **Before quoting the operative part aloud, take it from the judgment.** The formulations above
are reported holdings, not verbatim operative text. The persona's rule is an exact quotation or
none — so **attribute and paraphrase** unless somebody reads CELEX `62020CJ0184`.

---

## The proxy problem, and the measurement trap

Three citations. The plan asked for one; it needs two, because it makes two distinct claims —
**that removing the attribute does not remove the attribute**, and **that measuring discrimination
requires holding the attribute**. Those are different findings by different people.

**For the proxy problem — the computer-science statement.** **Cynthia Dwork, Moritz Hardt, Toniann
Pitassi, Omer Reingold and Richard Zemel, "Fairness Through Awareness", *Proceedings of the 3rd
Innovations in Theoretical Computer Science Conference (ITCS '12)*, pp. 214–226 (ACM, 2012).**
*Verified: all five authors, exact title, conference, year, page range.* The relevant result is in
the title's argument: **blindness to the protected attribute does not deliver fairness**, because
group membership correlates with other available features which then serve as **proxies** for it.
The paper's name for the thing it is arguing against is the field's name for it — **fairness
through unawareness** — which is the term the plan already uses.

**For the proxy problem — the legal statement, and it is the better one to quote.** **Solon Barocas
and Andrew D. Selbst, "Big Data's Disparate Impact", *California Law Review* 104 (2016), p. 671.**
*Verified: both authors, exact title, journal, volume, year, first page; also SSRN `2477899`.*
Their mechanism is **redundant encoding**: removing the sensitive label does not remove the
disadvantage, because the remaining features already carry it — the data being a record of the
prior distribution of advantage. A further point the episode can use: **removing every proxy
degrades the model**, because the proxies carry task-relevant information too. *There is no free
version of the naive fix.*

> **Note for the writer, and it is a real connection, not a flourish.** **Andrew D. Selbst** is
> also the co-author of *"Meaningful information and the right to explanation"* in docket `02`, the
> paper that anchors the explanation debate. Same person, two of this series' arguments. **Use it
> once, in passing, if at all** — "the same writer who argued that an explanation has to make a
> decision contestable" — and never as an argument from authority.

**For the measurement requirement.** **McKane Andrus, Elena Spitzer, Jeffrey Brown and Alice Xiang,
"What We Can't Measure, We Can't Understand: Challenges to Demographic Data Procurement in the
Pursuit of Fairness", *Proceedings of the 2021 ACM Conference on Fairness, Accountability, and
Transparency (FAccT '21)*, March 2021; arXiv:2011.02282.** *Verified: all four authors, exact
title, conference, year, arXiv number.*

**Why this is the right citation and not a paraphrase of the trap.** It is **empirical**: the
authors interviewed **38 practitioners and professionals** working in or adjacent to algorithmic
fairness, and found that practitioners routinely **do not have** the demographic data their own
fairness tooling requires — while fairness toolkits **almost invariably** require access to
protected attributes or proxies for them. So the trap is not a clever legal observation; it is the
reported working condition of the people whose job this is. **The title is the episode's sentence
and it can be quoted as a title**, which sidesteps the persona's quotation rule entirely.

⚠ **Keep the two claims apart when speaking.** *Unawareness fails* (Dwork et al.; Barocas and
Selbst) and *measurement requires the forbidden field* (Andrus et al.) are separate findings. The
plan's "corollary" framing is right — but the corollary needs its own source, and now it has one.

---

## The collision — and it is not the one the plan describes

🔴 **CORRECTION TO THE PLAN, and this is the significant one.** The plan's collision beat reads:
the AI Act permits providers to process special-category data where strictly necessary to detect
and correct bias **in high-risk systems**, and *"the live legislative proposal would add the
matching door to Article 9 itself"*. **Both halves have moved**, in opposite directions.

### What is now in force

The AI Act's bias-detection permission is **no longer Article 10(5)**. Regulation (EU) 2024/1689
was amended by **Regulation (EU) 2026/1744 of 8 July 2026** (OJ L, 24.7.2026), applying from
**27 July 2026** — the AI strand of the Digital Omnibus, **adopted by the Council on 29 June 2026**.
It **deleted Article 10(5)** and replaced it with a **new, freestanding Article 4a**, which is
**broader**: it now reaches **deployers**, and **providers and deployers of AI systems and models
that are not high-risk**.

*Source: the series-A docket's own consolidated extraction, `projects/ai_act/research/07_operative_text.md`,
CELEX `02024R1689-20260727`, which already carries the amendment. **The text below is verbatim from
that extraction** — a copy across, as the plan requested, but of the current wording rather than
the repealed one.*

```text
Article 4a — Processing of special categories of personal data for bias detection and correction

1. To the extent strictly necessary to ensure bias detection and correction in relation to
high-risk AI systems in accordance with Article 10(2), points (f) and (g), of this Regulation,
providers of such systems may exceptionally process special categories of personal data, subject
to appropriate safeguards for the fundamental rights and freedoms of natural persons. In addition
to the provisions set out in Regulations (EU) 2016/679 and (EU) 2018/1725 and Directive (EU)
2016/680, as applicable, all the following conditions shall be met in order for such processing to
occur:
    (a) the bias detection and correction cannot be effectively fulfilled by processing other
    data, including synthetic or anonymised data;
    (b) the special categories of personal data are subject to technical limitations on the re-use
    of personal data, and state-of-the-art security and privacy-preserving measures, including
    pseudonymisation;
    (c) the special categories of personal data are subject to measures to ensure that the personal
    data processed are secured and protected, subject to suitable safeguards, including strict
    controls and documentation of the access, to avoid misuse and to ensure that only authorised
    persons have access to those personal data with appropriate confidentiality obligations;
    (d) the special categories of personal data are not transmitted, transferred or otherwise
    accessed by other parties;
    (e) the special categories of personal data are deleted once the bias has been corrected or the
    personal data has reached the end of its retention period, whichever comes first; and
    (f) the records of processing activities pursuant to Regulations (EU) 2016/679 and (EU)
    2018/1725 and Directive (EU) 2016/680 include the reasons why the processing of special
    categories of personal data was strictly necessary to detect and correct biases, and why that
    objective could not be achieved by processing other data.

2. Providers and deployers of other AI systems and models and deployers of high-risk AI systems may
exceptionally process special categories of personal data to the extent that:
    (a) such processing is strictly necessary to ensure bias detection and correction in view of
    possible biases that are likely to affect the health and safety of persons, have a negative
    impact on fundamental rights or lead to discrimination prohibited pursuant to Union law,
    especially where data outputs influence inputs for future operations; and
    (b) all of the conditions and safeguards set out in paragraph 1 are applied.

This paragraph does not create any obligation to conduct such bias detection and correction.
```

**Three things in that text the writer should not miss.**

- **"may exceptionally process"** — the drafters wrote the exception's own character into it.
- **Condition (a) is the measurement trap, legislated.** You may hold the forbidden field only if
  the job *cannot* be done with other data, *including synthetic or anonymised data*. Andrus et al.
  are the evidence about whether it can.
- **The last sentence of paragraph 2** — *"This paragraph does not create any obligation to conduct
  such bias detection and correction."* **A permission to look, and no duty to look.** The plan's
  economic level already says the cheapest posture is to know nothing and be able to prove nothing;
  **this sentence is that observation in the Union's own words**, and it is the strongest single
  line available to this episode.

### What is still a proposal

The **GDPR** strand — the Data Omnibus — was **split from the AI strand and is still in
negotiation** as at the week of recording. It has not amended Article 9 or Article 6. What is
proposed includes a **new Article 88c**, a defined legitimate-interest route for AI development and
operation conditioned on enhanced transparency and an **unconditional right to object**, and an
exemption for **residual** special-category data that finds its way into a training set where the
controller has taken appropriate measures to minimise and to remove or protect it.

**The objection, with its holders.** **EDPB–EDPS Joint Opinion 2/2026** on the Digital Omnibus, and
**Joint Opinion 1/2026** on the Digital Omnibus on AI, both **February 2026**. On the AI strand the
two authorities objected to the **widening** now in Article 4a — that it extends beyond high-risk
systems to all AI systems and models and to deployers — and asked for the **"strict necessity"**
standard to be **reinstated** where the proposal had softened it to "necessary". They recalled that
processing special categories is **in principle prohibited** and that exceptions must be narrowly
defined. On the GDPR strand they did not consider a specific legitimate-interest provision for AI
training to be necessary at all, since legitimate interests may already serve in some cases.

⚠ **"Strict necessity" survived into the adopted Article 4a** — the words *"strictly necessary"*
appear in both paragraphs above. **So do not say the objection was ignored; say the instrument was
widened over the objection of both supervisory authorities, and check any claim about which
specific recommendations were taken.** The adopted text is above; the opinions are dated February
2026; that is all this docket establishes.

> **The collision, restated — and it is better than the plan's version.** The plan had a
> prohibition in one instrument and a proposal to reconcile it in another. **The truth is worse and
> cleaner.** One instrument has **already enacted, and put in force**, a permission to process data
> that the other instrument still **prohibits**. The amendment that would make the two agree is
> **still in negotiation** and may not pass in the form proposed. So a deployer of an ordinary,
> non-high-risk AI system reading Article 4a today is told it **may exceptionally process** special
> categories to check for bias — and the Regulation that actually governs that processing says it
> **shall be prohibited**, with a closed list of doors that this is not one of.
>
> **Whether Article 4a is itself one of the Article 9(2) doors is the question**, and the answer is
> not in this docket because it is not settled anywhere. Article 4a says its conditions apply *"in
> addition to"* the GDPR's provisions, which reads as *not* displacing Article 9. **Say that, date
> it, and stop.** The plan's instruction — *date-stamp everything in this beat* — is now the most
> important instruction in the episode.

---
---

## What Episodes 2 and 3 still do not have

Neither blocks its episode; both should be spoken as absences if they are reached for.

- **No post-SCHUFA Article 22 case law**, still. `02` flagged this and it is unchanged. Episode 4
  is writable on SCHUFA alone, which is what its plan assumes.
- **No decision anywhere** holding that predicting a protected attribute is itself Article 9
  processing. The plan tells Episode 3 to state that as an absence with its date. **This compiler
  searched on 2026-09-20 and did not find one; that is the date to give, and the claim should be
  "none that this programme found", not "none exists".**
- **The complainants behind the DPC action**, and whether the Grok undertaking bound xAI as well as
  TIUC. Both named above.
- **Nothing first-party from xAI or X** — every account of the pipeline here is press reporting of
  an interface.

## Elsewhere in the series, still unsourced

Unchanged from `02` and `03`: the DSA, DMA, Data Act and copyright episodes have **no documented
controversy at all**; there is nothing on the withdrawn AI Liability Directive; and Episode 1's two
remaining items (the Munich *GEMA v OpenAI* judgment, and definitions of memorisation and
membership inference) are still open.
