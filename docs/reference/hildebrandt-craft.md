# Hildebrandt craft reference

Distilled from **Law for Computer Scientists and Other Folk** (OUP, open access) and the
**COHUBICOL** project materials of **Mireille Hildebrandt**, per the process in
[`craft-sourcing.md`](craft-sourcing.md). Sections are named for the persona file they feed.
Confidence labels: `[Observed]` (quoted in §I), `[Inferred]` (pattern, no single quote),
`[Unverified]` (secondary — resolve before synthesis).

> **Self-contained by rule.** This dossier describes one person. It makes no comparison to
> another source and no decision about which persona will use what — those belong to synthesis.

> **Pass 2 of 3.** Pass 1 mined the corpus and read the introduction and the master-course
> syllabus. Pass 2 read **chapters 2, 10 and 11 in full** — the three that carry her frame — which
> added seven prose-level moves she had not been credited with, and produced the first
> **structural claim corroborated across two independent artefacts** (§A-7).

---

## §0 Source card

| | |
|---|---|
| **Person** | Mireille Hildebrandt — Research Professor, Vrije Universiteit Brussel; Professor of Smart Environments, Data Protection and the Rule of Law, Radboud; PI of COHUBICOL |
| **Corpus** | The complete open-access book, **11 chapters, 113,029 words of her own prose**, plus the COHUBICOL master-course syllabus (3.1k words) and two project documents |
| **Corpus kind** | **Written.** No audio was sought: she is hired for frame, not delivery, so speech metrics do not apply — this is a property of the job, not a gap in the corpus |
| **Read in full (pass 2)** | Chapters 2 (*Law, Democracy and the Rule of Law*), 10 (*'Legal by Design' or 'Legal Protection by Design'?*) and 11 (*Closure: on ethics, code and law*) |
| **Prose quality** | Punctuation density **5.53** marks per 100 words; all sentence-level metrics valid |
| **Two extraction hazards, both handled** | The publisher's pages carry (a) export/navigation chrome and (b) **open peer-review comment threads** — other people's words on the same URL. Both are now stripped by `fetch.py`; the second matters, because a quotation lifted from a commenter would be misattributed to her. Word counts fell from 117,510 to 113,029 once both were removed |
| **Known residue** | The mined n-gram lists for this source are still partly polluted by heading repeats and are **not cited anywhere below**; every §I excerpt is from body prose |
| **Not obtained** | Her monographs (*Smart Technologies and the End(s) of Law*), the COHUBICOL Typology of Legal Technologies itself, her journal articles, and any recorded lecture |
| **Acquisition** | `fetch.py sources/hildebrandt.json`, 2026-09-10 |
| **Permission** | Book chapters **CC-BY 4.0**; syllabus **CC BY-NC**. Raw corpus stays gitignored and uncommitted |

**Role: content source.** The bar is enough primary text to evidence the frame accurately and
quote it correctly, which 113k words of openly-licensed prose clears comfortably.

## §1 Hired for

**The gaze** — how to look at a legal question when its object is computational. Her own
statement of the aim, from the master course, is the tightest available: to "sensitize law
students to the assumptions and methodological constraints of computer science, **to learn how
to ask the right questions** when assessing 'legal tech', and to develop acuity with regard to
how computational law may affect human rights and the rule of law." `[Observed §I-1]`

---

## §A Plan-level craft — feeds `roles/planner.md`

1. **Her book's spine is stated as a numbered sequence**, and the first move is foundational
   rather than topical: "First… this book answers the question 'what law is' by asking the
   question 'what law does'. Second… 'domains of cyberlaw' that are particularly relevant for
   computer science… Third, the book discusses the 'frontiers of law in an onli**f**e world'…
   Finally, the closing chapter addresses the relationship between law, code and ethics."
   `[Observed §I-2]`
2. **The foundations exist to pre-empt two specific misreadings.** "To prevent mistaking law for
   either a bag of independent rules or a rigid hierarchical system of decision trees, this book
   takes off with a discussion of the nature of modern positive law." The opening unit is
   designed against the errors a technically-trained reader will otherwise make. `[Observed §I-3]`
3. **Her course assessment is a four-step analytical spine, fixed in advance** — each student is
   assigned a **real, named** legal-tech system and writes to this structure: connection with
   the assigned technology (500 words) → what consequences it may have in terms of **direct or
   indirect legal effect** (1000) → how this may affect **the Rule of Law** (500) → what **Legal
   Protection by Design** could mean here (500). The gaze, operationalised as a template.
   `[Observed §I-4]`
4. **The research question must be genuinely open** — "no questions to which you already know
   the answers" — and the method must come from the student's own discipline. `[Observed §I-4]`
5. **Vendor claims are the object of study, not the description of it.** The COHUBICOL Typology
   is used to challenge students "to properly engage with the claims made by the systems'
   providers and to consider whether or not those systems could have an impact on legal
   protection." `[Observed §I-1]`
6. **Citation is deliberately restrained for this audience** — on her own book's open review she
   writes: "there are libraries full of highly relevant literature on many subjects in this
   book. I deliberately avoided referring to all of them to not drown the readers."
   `[Observed §I-5]`

7. **Her own chapter reproduces the four-step spine independently of the syllabus.** Chapter 10
   runs: the technology described operationally (10.1 machine learning, 10.2 distributed ledgers
   and smart contracts) → its legal status (10.2.2 under private law, 10.2.3 under public law) →
   *Implications for the Rule of Law* (10.1.3) → what design could mean (10.3 legal by design
   against legal protection by design). That is the same order as her course assessment, arrived
   at in a different artefact for a different purpose — the one structural claim in this dossier
   with two independent witnesses. `[Observed §I-16]`

## §B Prose-level craft — feeds `roles/writer.md`

1. **Answer "what is it?" by asking "what does it do?"** Her signature epistemic move, applied
   to law itself: the book "answers the question 'what law is' by asking the question 'what law
   does'", and squarely faces "the question of law's **mode of existence**, by asking what law
   does — and how." `[Observed §I-2, §I-6]`
2. **Refuse both misconceptions in the same breath** — neither a bag of independent rules nor a
   hierarchy of decision trees (§A-2). `[Observed §I-3]`
3. **Law as architecture, on a shared definition with computing.** "Both law and computer science
   are about architecture, rather than merely about rules (and principles)", where architecture
   means three things: being constructed rather than natural; being relational and
   high-dimensional; and a **double ecological nature** — the construct must survive in its
   environment while itself forming the environment for its inhabitants. She then makes the
   high-dimensionality concrete: a supreme court overruling precedent "will cause numerous
   subtle or not so subtle changes in the interpretation of the law by lower courts", which
   changes conduct, which triggers legislative response. `[Observed §I-7]`
4. **Ground a legal institution in the medium that afforded it.** Modern positive law is
   presented as "an affordance of a specific information and communication technology, namely
   the printing press", carrying "the affordances of text-driven abstraction: sequential
   processing and hierarchical ordering" — and judicial independence follows from the medium:
   "the need for interpretation that is core to text-driven law results in an increasingly
   independent position for the courts." `[Observed §I-8]`
5. **The three drivers as a working distinction** — text-driven law (13 uses), data-driven (21),
   code-driven (18) — which lets her ask what changes when the driver changes rather than
   whether technology is good or bad. `[Observed §I-9]`
6. **Legal protection by design against legal by design** — 35 and 31 uses respectively; the
   pairing is the spine of chapter 10. `[Observed §I-9]`
7. **Contestability as the test of a decision.** She separates three requirements — the process,
   the justification, and "the contestability of the decision" — and draws the distinction that
   does the most work: **"a justification is not equivalent with an explanation, which rather
   serves as a means to make the decision contestable."** She also treats contestability as
   intrinsic to law rather than a remedy bolted on: "the inherent contestability of judgments,
   both regarding the identification of relevant facts and the interpretation of the legal
   norm." `[Observed §I-10]`
8. **Neither embrace nor reject; discriminate.** "The idea, however, is not to reject the new
   onli**f**e world. The real challenge is to figure out **when to condone it, when to embrace
   it and when to decline and reject** what is on offer." `[Observed §I-11]`
9. **Name the genre and its difficulty.** The book is deliberately both textbook and essay, and
   she says why: "Teaching law to computer scientists will always be an attempt, an 'essay', to
   bridge the disciplinary gaps between two scientific practices that each have their own
   methodological demands and constraints." `[Observed §I-12]`
10. **Ethics is not offered as the softer alternative to law.** Chapter 11's stated argument: "if
    ethics aligns itself with the force of technology, this may overrule the force of law, and,
    paradoxically, reduce the space for ethics." Consequences are treated "from the perspective
    of law", not "a matter of individual moral preferences or intellectual reflection, but a
    matter of confronting 'what law does' when such rights and obligations are violated."
    `[Observed §I-13]`

11. **A borrowed image, run through a whole section.** She opens the question "what is law?" on
    a legal historian's joke — "'Trying to define law is like trying to hammer a pudding to the
    wall', wrote legal historian Uwe Wesel" — and then keeps using it: "the proof of the pudding
    is in the eating", "the fluidity of the legal pudding", "to prevent us from nailing the legal
    pudding to the wall (a rather unproductive project)". One image, carried, rather than a fresh
    one per point. `[Observed §I-17]`
12. **The audience's own idiom, borrowed to explain a legal property.** On the law's need for
    reinterpretation: "This may be **a feature, rather than a bug**." She reaches into software
    vocabulary to make a legal virtue legible. `[Observed §I-17]`
13. **Correct the intuitive reading of a legal value before building on it.** "Legal certainty,
    one of the core values of the law, is **not** about fixating the meaning of legal norms once
    and for all. Instead, legal certainty targets the delicate balance between stable
    expectations and the ability to reconfigure or contest them." The engineer's reading of
    "certainty" is named and refused. `[Observed §I-17]`
14. **Define by a triad held in tension, not by a formula.** Following Radbruch, law is
    constituted by three values — "(1) legal certainty, (2) justice, and (3) instrumentality" —
    and "to qualify as law, a normative framework must aim to sustain, develop and balance these
    values – **even though they may be incompatible in concrete cases**." The definition includes
    its own conflicts. `[Observed §I-17]`
15. **Homonym disambiguation, executed.** For "source": she first enumerates the ordinary senses
    — "a spa that provides for refreshing mineral water, an archive to be used for historical
    research, a witness queried by a journalist, or an encyclopaedia" — then shows the legal sense
    is categorically different, "both more and less than a source of knowledge about the law, as
    the sources of law are **constitutive** of law", and closes with negative examples: "a
    newspaper article with information about the law is not a source of law, and neither is a
    Wikipedia article or the website of a law firm." `[Observed §I-18]`
16. **Describe the mechanism operationally, then test it against the field's own definition.**
    Before any law, she walks A/B testing step by step — version A, a minimal change to version
    B, a 50/50 split, automated clickstream measurement, the winner becomes the default, repeat —
    and only then asks: "Let's see if this qualifies as an example of ML", checking it against
    Tom Mitchell's textbook definition. The technology is established on its own terms first.
    `[Observed §I-19]`
17. **State the conclusion first and label it as such.** "**Spoiler**: one of the main differences
    is that law provides closure whereas ethics remains in the realm of reflection as it does not
    have force of law." Then the argument. `[Observed §I-20]`
18. **Name the expected example and decline it.** "The example I will use throughout this chapter
    is **not** about the ethical dilemmas of driverless cars, but the question of algorithmic
    fairness." `[Observed §I-20]`
19. **Take the audience's canonical thought experiment seriously, then attack its framing — and
    make the first objection an empirical one.** On Asimov's laws: "These 'laws' raise more
    questions than they answer, which makes them a very interesting attempt to confront the
    unpredictability of autonomous computational systems." On the MIT Moral Machine's self-driving
    dilemmas: "A closer look at the reality of supposedly driverless cars, however, demonstrates
    **two objections against the way the issue is framed**." The first is not philosophical but
    factual — "experts are not in agreement whether the level of autonomy that is assumed in the
    portrayal of these choices will ever be achieved" — and she cites a roboticist against it:
    Rodney Brooks "predicts that self-driving cars will require separate lanes and roadblocks."
    Only then the second objection, that the issue is "framed in somewhat naïve utilitarian terms".
    **Before reasoning about a hypothetical system, ask whether it will exist.** `[Observed §I-22]`
20. **Borrow the other field's vocabulary, and the audience's own culture, as evidence.** "In
    robotics, developers speak of 'the envelop' of a robot. 'The envelop' is usually designed
    simultaneously with the robot, to ensure its functionality and the safety of those interacting
    with it." And an XKCD cartoon is used as an argument about the ordering of Asimov's laws — "as
    the cartoon below indicates, the sequence is not arbitrary" — with its licence noted.
    `[Observed §I-22]`
21. **Historicise the institution: date it, and say how hard it is to feel its novelty.** "The
    human rights declarations of the 17th and 18th centuries provided those subject to the power of
    a sovereign state with an entitlement to civil and political rights… **Being subject to a
    sovereign became being a subject in law.**" And then: "It is hard to imagine how novel the
    attribution of such rights was, even if initially their enforcement was neither practical nor
    effective." `[Observed §I-23]`
22. **Explain why a legal move works by naming a behavioural mechanism.** "Some attribute the
    power of this attribution to the '**endowment bias**'; if people come to believe they 'have'
    these rights, they will invest in 'keeping' them. If the struggle this entails succeeds, these
    rights will eventually be instituted as effective subjective rights." `[Observed §I-23]`
23. **Justify a right as a public good rather than a private entitlement.** "Note that these legal
    goods are considered worthy of protection **as public goods**, because a society that does not
    protect them cannot support a viable democracy that depends on independence of thought and
    unhindered development of both individual and group identities." `[Observed §I-23]`

## §C Delivery craft — feeds `roles/tone.md`

She is a **written** source and her register is the least transferable thing about her; recorded
so that synthesis does not borrow it by accident.

- **She barely addresses the reader**: "you"/"your" at **0.56 per 1,000 words**, against "we" at
  3.88 and "I" at 1.42. Questions end 2.8% of sentences. `[Observed §I-14]`
- **Long, subordinated sentences** — mean 22.5 words, median 20, p90 43, longest 211; 24% short
  (≤8 words). `[Observed §I-14]`
- **Low hedging** — 0.62 per 1,000 words. Declarative scholarly prose. `[Observed §I-14]`
- She reaches for the concrete analogy at exactly the hard points (the house, the supreme court
  ripple, the printing press), which is the one delivery habit that would survive being spoken.
  `[Inferred]`

## §D Delivery profile — feeds `voice_profiles.yaml`

**Not applicable by kind.** A written corpus supports no speech metrics, and none were sought.
The prose numbers above are the usable measurements. `f0_sd_st`, `speech_rate_wpm`,
pause structure: not measured, and not a gap.

## §E Standards — what she would reject — feeds `roles/editor.md`

1. **Law described as a bag of rules, or as a decision tree.** Both named as errors the book is
   built to prevent. `[Observed §I-3]`
2. **An explanation offered where a justification is owed.** The two are not equivalent; an
   explanation earns its place by making a decision contestable. `[Observed §I-10]`
3. **Ethics substituted for legal analysis** — and specifically the assumption that an ethics
   framing is the safer or softer one. Her argument is sharper than that: **law provides closure
   and ethics does not**, "as it does not have force of law" — but ethics decided "behind the
   closed doors of the board room" can acquire **the force of technology** and provide closure
   anyway, "though not by way of democratically legitimated legislation". An ethics framing can
   therefore be *less* accountable than a legal one, not more. `[Observed §I-13, §I-20]`
3b. **"By design" offered as an ethical commitment rather than a legal requirement.** Her
   objection to value-sensitive and privacy-by-design as *ethical* proposals is two-part and
   practical: they do not level the playing field, so "companies that apply such ethical design
   may be pushed out of the market"; and they make "protection dependent on the ethical
   inclinations of those who develop and market the choice architecture of citizens, instead of
   demanding that such choice architecture must meet minimum standards". `[Observed §I-21]`
4. **A legal term read as its computing homonym.** Her own open-review thread has a computer
   scientist stuck on "modern positive law" because "the word positive means quite a different
   thing to me" — evidence that the failure is real, and that she treats it as the author's
   problem to solve. `[Observed §I-15]`
5. **Drowning a non-specialist in citations** — restraint is a stated authorial choice, not
   laziness. `[Observed §I-5]`
6. **Wholesale acceptance or wholesale rejection of a technology.** The task is to discriminate
   case by case. `[Observed §I-11]`
7. **A question whose answer you already have.** `[Observed §I-4]`

## §F Defaults — feeds `persona.yaml`

Nothing transferable. Chapter lengths (4.6k–23.4k words) reflect a textbook's needs, and there
is no spoken unit to measure. `[Inferred]`

## §G Transfer & exclusions

**Converts directly:** asking what a norm *does* in order to say what it *is*; naming and
refusing the two misconceptions; law-as-architecture with its three properties and the
ripple-effect illustration; grounding an institution in the medium that afforded it; the
text/data/code-driven distinction; legal protection by design against legal by design;
contestability as the test, with justification distinguished from explanation; the
condone/embrace/decline triage; the four-step analytical spine from her course (§A-3), which is
the single most directly usable artefact in this corpus.

**Do not import:** her register. Second-person address at 0.56 per 1,000 words, 43-word
sentences at the 90th percentile, and a citation apparatus are the properties of a scholarly
textbook, and spoken aloud they would produce exactly the lecture that listening cannot carry.
The frame is what is being borrowed; the prose is not. Also leave behind the book's domain
coverage (cybercrime, copyright, ICT liability as taught there) and its 2019 vintage of specifics.

**A caution specific to this source.** Her vocabulary is precise and load-bearing — "mode of
existence", "affordance", "positive law", "contestability" — and each term carries an argument
that a listener has not been given. Borrowing the words without building the argument would
produce the appearance of her gaze and none of its substance. Whatever adopts this frame has to
earn each of those terms in plain language first. `[Inferred]`

## §H Candidate prompt lines

Nominations only; selection happens at synthesis.

1. `writer` — Establish what a rule *does* before saying what it is, and let the doing define it.
2. `writer` — Name and refuse the two standard misreadings early: that the law is a bag of
   independent rules, and that it is a decision tree.
3. `writer` — Where a norm is hard to place, show its architecture: what it was built out of,
   what it has to survive, and what it becomes the environment for.
4. `writer` — Trace an institution back to the medium that made it possible, and ask what changes
   when the medium changes.
5. `writer` — Distinguish a justification from an explanation, and say which one the listener is
   actually being offered.
6. `writer` — Test any automated decision by asking whether it can be contested, by whom, and on
   what basis.
7. `writer` — Refuse both wholesale acceptance and wholesale rejection; say when to condone, when
   to embrace, and when to decline.
8. `writer` — Never let an ethics framing stand in for the legal question of what happens when a
   right is violated.
9. `writer` — Before using a term of art, earn it in plain language — especially one whose
   ordinary or computing sense differs from its legal sense.
10. `planner` — For a system under examination, run the same four steps: what it is, what legal
    effect it may have directly or indirectly, how that bears on the rule of law, and what
    protection by design would require here.
11. `planner` — Make the provider's own claims about a system an object of scrutiny rather than
    the description of it.
12. `editor` — Fail any passage that borrows a term of art without having built the argument that
    gives it meaning.
13. `writer` — Describe the system on its own terms — step by operational step — before asking
    what the law makes of it, and check your description against the field's own definition.
14. `writer` — Where a legal value has an intuitive reading the listener will bring with them,
    name that reading and correct it before building on the term.
15. `writer` — Take one borrowed image and carry it through the whole passage rather than
    reaching for a fresh analogy per point.
16. `writer` — Name the example everyone expects, decline it, and say what you will use instead.
17. `writer` — Before reasoning about what the law should do with a system, ask whether that
    system will exist as described, and cite someone who builds them.
18. `writer` — Where a right or a rule feels timeless, date it, and say plainly how strange it was
    when it was new.
19. `writer` — Where a protection looks like a private entitlement, say what public good it serves
    and what fails without it.

## §I Evidence

Locators are item slugs under `experiments/craft_sourcing/corpus/hildebrandt/`. Chapter
references are to *Law for Computer Scientists and Other Folk*; `syllabus` is the COHUBICOL
master-course document.

1. **Aim of the teaching; vendor claims as object** — `meta-cohubicol-master-course`: "The
   objective is to sensitize law students to the assumptions and methodological constraints of
   computer science, to learn how to ask the right questions when assessing 'legal tech', and to
   develop acuity with regard to how computational law may affect human rights and the rule of
   law." · "The Typology of Legal Technologies plays a core role in the course assessment,
   challenging students to properly engage with the claims made by the systems' providers and to
   consider whether or not those systems could have an impact on legal protection."
2. **Book spine; what law does** — ch1: "this book answers the question 'what law is' by asking
   the question 'what law does'. Second, having introduced the basic elements of the law, this
   book targets 'domains of cyberlaw' that are particularly relevant for computer science…
   Third, the book discusses the 'frontiers of law in an onli**f**e world'… Finally, the closing
   chapter addresses the relationship between law, code and ethics."
3. **The two misconceptions** — ch1 §1.6.1: "To prevent mistaking law for either a bag of
   independent rules or a rigid hierarchical system of decision trees, this book takes off with a
   discussion of the nature of modern positive law in the light of constitutional democracy."
4. **The four-step assessment spine** — `syllabus`: "Connection with the assigned LegalTech
   (500) · Exploration of what consequences the LegalTech may have in terms of direct or indirect
   legal effect (1000) · Argumentation of how this may affect the Rule of Law (500) ·
   Argumentation of what Legal Protection by Design could mean here (500)" · "The question must
   be open (no questions to which you already know the answers), and the answer should be based
   on a clear methodology (that is part of your own disciplinary background)."
5. **Citation restraint** — her reply in the book's open review: "Honestly, there are libraries
   full of highly relevant literature on many subjects in this book. I deliberately avoided
   referring to all of them to not drown the readers."
6. **Mode of existence** — ch2: "This chapter will squarely face the question of law's 'mode of
   existence', by asking what law does – and how. This means checking on the sources of law, the
   nature of legal reasoning and the question of the relationship between law, democracy and the
   Rule of Law."
7. **Architecture** — ch1 §1.1: "both law and computer science are about architecture, rather
   than merely about rules (and principles)", with "the fact of being constructed (artificial)
   rather than natural, the relational and high-dimensional nature of whatever is constructed,
   and, the double ecological nature of the construct — a. as it has to survive in a specific
   (often dynamic) environment, b. while the construction itself forms the environment for its
   inhabitants." · "A supreme court that overrules precedent will cause numerous subtle or not so
   subtle changes in the interpretation of the law by lower courts that need to anticipate how
   their verdicts will fare."
8. **Medium as affordance** — ch1: "I will briefly situate the rise of modern positive law as an
   affordance of a specific information and communication technology (ICT), namely the printing
   press." · "abstract (general) norms that share the affordances of text-driven abstraction:
   sequential processing and hierarchical ordering." · "The need for interpretation that is core
   to text-driven law results in an increasingly independent position for the courts."
9. **Distinction frequencies** — corpus counts: "legal protection by design" 35, "legal by
   design" 31, data-driven 21, code-driven 18, text-driven 13, "rule of law" 92, "legal
   certainty" 48, architecture 53, interpret- 124.
10. **Contestability; justification vs explanation** — "(1) … process, (2) the justification of
    the decision, and, (3) the contestability of the decision." · "Note, however, that a
    justification is not equivalent with an explanation, which rather serves as a means to make
    the decision contestable as to its [basis]." · "All this demonstrates the inherent
    contestability of judgments, both regarding the identification of relevant facts and the
    interpretation of the legal norm."
11. **Condone / embrace / decline** — ch1: "The idea, however, is not to reject the new
    onli**f**e world. The real challenge is to figure out when to condone it, when to embrace it
    and when to decline and reject what is on offer."
12. **Textbook and essay** — ch1: "Teaching law to computer scientists will always be an attempt,
    an 'essay', to bridge the disciplinary gaps between two scientific practices that each have
    their own methodological demands and constraints." · audience: "geared to those who have no
    wish to become lawyers but are nevertheless forced to consider the salience of legal rights
    and obligations with regard to the construction, maintenance and protection of computational
    artefacts."
13. **Ethics, code and law** — ch11 abstract: "This chapter explores the interaction between law,
    ethics and code. I argue that if ethics aligns itself with the force of technology, this may
    overrule the force of law, and, paradoxically, reduce the space for ethics." · ch1: "The
    latter is often considered under the heading of ethics, here it is studied from the
    perspective of law… It is therefore not a matter of individual moral preferences or
    intellectual reflection, but a matter of confronting 'what law does' when such rights and
    obligations are violated."
14. **Register** — `out/hildebrandt-profile.json`: `you_per_1k` 0.56, `we_per_1k` 3.88,
    `i_per_1k` 1.42, `hedge_per_1k` 0.62, `question_rate` 0.028; `sent_len_mean` 22.5,
    `sent_len_median` 20, `sent_len_p90` 43, `sent_len_max` 211, `short_sent_frac` 0.24;
    `punctuation_density` 5.53.
15. **The homonym problem, evidenced** — a computer scientist in the book's open review: "I find
    the use of the phrase 'modern positive law' here a bit confusing without an introduction. The
    word positive means quite a different thing to me, so I'm having trouble understanding what
    it would mean in a law context without consulting external resources." *(A reader's words,
    not hers — cited here as evidence that the failure mode is real, and labelled as such.)*
16. **The four-step spine, second witness** — ch10 section order: "10.1 Machine learning (ML)" ·
    "10.1.3 Implications of micro-targeting for the Rule of Law" · "10.2 Distributed Ledger
    Technologies (DLTs), smart contracts and smart regulation" · "10.2.2 The legal status of
    'smart contracts' under private law" · "10.2.3 The legal status of 'smart regulation' under
    public law" · "10.3 'Legal by Design' or 'Legal Protection by Design'?"
17. **The pudding; feature not bug; certainty; the triad** — ch2 §2.1: "'Trying to define law is
    like trying to hammer a pudding to the wall', wrote legal historian Uwe Wesel… In the end, the
    proof of the pudding is in the eating… The fluidity of the legal pudding is also the result of
    the dynamics and complexity of the environment that modern positive law interacts with. **This
    may be a feature, rather than a bug**, as the need for iterant interpretation that is core to
    written law requires flexibility in the face of changing circumstances. Legal certainty, one of
    the core values of the law, is not about fixating the meaning of legal norms once and for all.
    Instead, legal certainty targets the delicate balance between stable expectations and the
    ability to reconfigure or contest them. To prevent us from nailing the legal pudding to the
    wall (a rather unproductive project), legal philosopher Gustav Radbruch defined law in terms of
    three constitutive values: (1) legal certainty, (2) justice, and (3), instrumentality. To
    qualify as law, a normative framework must aim to sustain, develop and balance these values –
    even though they may be incompatible in concrete cases."
18. **Homonym disambiguation** — ch2 §2.1.1: "A source may be a spa that provides for refreshing
    mineral water, an archive to be used for historical research, a witness queried by a
    journalist, or an encyclopaedia… In law, the term 'source of law' has a very specific meaning.
    It refers to both more and less than a source of knowledge about the law, as the sources of law
    are constitutive of law… a newspaper article with information about the law is not a source of
    law, and neither is a Wikipedia article or the website of a law firm."
19. **Mechanism before law** — ch10 §10.1: "The current webpage is called version A, its design is
    changed in a minimal way… 50% of visitors are directed to version A, the other 50% to version
    B. The software conducts automated measurement of their clickstream behaviours… The version
    that is more effective is now the default page. The whole process is repeated with another
    slight change… Let's see if this qualifies as an example of ML. In his handbook on Machine
    Learning, Tom Mitchell recounts that…"
20. **Closure; spoiler; the declined example** — ch11: "Spoiler: one of the main differences is
    that law provides closure whereas ethics remains in the realm of reflection as it does not have
    force of law. However, a second difference turns the previous statement inside out: whereas law
    and the Rule of Law introduce checks and balances and demand democratic participation…, ethics
    may be decided by tech developers or behind the closed doors of the board room of corporate
    business enterprise. It can thus obtain the force of technology… Though the latter are not a
    black box for those knowledgeable on the technical side, they are black boxes for those who
    cannot read the code." · "The example I will use throughout this chapter is not about the
    ethical dilemmas of driverless cars, but the question of algorithmic fairness."
21. **LbD and LPbD, defined** — ch10 §10.3.1: "LbD is a specific subset of techno-regulation that
    is (1) the result of deliberate design choices, where (2) those choices aim to ensure
    compliance with legal obligations by way of technical enforcement. LbD involves two steps.
    First, it involves a specific (non-ambiguous) interpretation of the relevant legal norm, and,
    second, it involves the translation of that interpretation into a programming language." ·
    §10.3.2: "Legal protection by design (LPbD)… does not aim to guarantee enforcement of whatever
    legal norm, but rather aims to ensure that legal protection is not ruled out by the affordances
    of the technological environment… The scope of LPbD should be determined by way of democratic
    participation… Those subject to such LPbD should be able to contest its application in a court
    of law." · on ethical alternatives: "companies that apply such ethical design may be pushed out
    of the market… it makes protection dependent on the ethical inclinations of those who develop
    and market the choice architecture of citizens, instead of demanding that such choice
    architecture must meet minimum standards that provide effective and practical protection."

---

## §J Verification — pass 2

Pass 2 was extension rather than falsification: three chapters read in full, against a pass-1
that had rested on the introduction, the syllabus, and mined patterns.

| Claim | Outcome |
|---|---|
| §A-3 the four-step analytical spine | **Corroborated by a second artefact.** Chapter 10's own section order reproduces it independently of the course syllabus — the only structural claim here with two witnesses |
| §B-1 "what law does" answers "what law is" | Confirmed; chapter 2 states it again as the chapter's method |
| §B-7 contestability as the test | **Strengthened.** It is a *defining requirement* of legal protection by design, not merely a test she applies: "Those subject to such LPbD should be able to contest its application in a court of law" |
| §C her one transferable delivery habit (the concrete analogy at hard points) | **Confirmed and specified**: she carries a single borrowed image through a whole section rather than refreshing it (§B-11) |
| Seven prose moves | **New at pass 2** (§B-11 to §B-18); none contradicts pass 1 |

**The critical detail pass 2 supplies**, which pass 1 had only in outline: LbD "involves two
steps. First… a specific (**non-ambiguous**) interpretation of the relevant legal norm, and,
second… the translation of that interpretation into a programming language." The disambiguation
*is* the loss — it removes the contestability that made the norm law. Her whole critique turns on
that sentence, and a reader who had only pass 1 would have had the label without the argument.
22. **Attacking the framing; the field's vocabulary; the cartoon** — ch9: "These 'laws' raise more
    questions than they answer… A closer look at the reality of supposedly driverless cars,
    however, demonstrates two objections against the way the issue is framed. First, experts are
    not in agreement whether the level of autonomy that is assumed in the portrayal of these
    choices will ever be achieved. Some suggest that this type of robotics is running into a wall,
    due to the limitations of data-driven 'intelligence' in real-life scenarios… In robotics,
    developers speak of 'the envelop' of a robot… Rodney Brooks, a famous roboticist who designed
    an industrial robot that may be trusted in a shared space, predicts that self-driving cars will
    require separate lanes and roadblocks… Second, the issues are framed in somewhat naïve
    utilitarian terms." · "as the cartoon below indicates, the sequence is not arbitrary. By XKCD."
23. **Historicising; endowment bias; rights as public goods** — ch5 §5.1: "The rise of the modern
    state must be situated in the beginning of what historians call the era of 'Modernity', around
    the 15th and 16th century… Being subject to a sovereign became being a subject in law. It is
    hard to imagine how novel the attribution of such rights was, even if initially their
    enforcement was neither practical nor effective. Some attribute the power of this attribution
    to the 'endowment bias'; if people come to believe they 'have' these rights, they will invest
    in 'keeping' them." · "Note that these legal goods are considered worthy of protection as
    public goods, because a society that does not protect them cannot support a viable democracy
    that depends on independence of thought and unhindered development of both individual and group
    identities."

---

## §K Held-out discovery — pass 3

Pass 3 read two chapters **never opened in passes 1 or 2** — 9 (*Legal Personhood for AI?*) and 5
(*Privacy and Data Protection*, the longest in the book) — looking only for moves the dossier did
not contain. It found five (§B-19 to §B-23).

The one that matters most for this subject is **§B-19**. Faced with the canonical AI thought
experiment — Asimov's laws, then the self-driving trolley — she does not answer it. She attacks
the framing, and her *first* objection is empirical rather than philosophical: does the system
whose dilemmas we are theorising actually exist, and what do the people who build such things say?
Only after that does she object to the utilitarian framing. That inverts the usual order of an
AI-ethics discussion and is a directly transferable discipline.

**Status: Hildebrandt is complete at pass 3 of 3.** Her corpus is fully acquired (11 chapters, 113k
words of her prose, openly licensed), the three frame-carrying chapters are read in full, two
further chapters have been read as held-out discovery, and the structural claim in §A-7 has two
independent witnesses. What remains open is the same thing that remains open everywhere here: a
reader who has not seen this file. Six chapters (3, 4, 6, 7, 8) are still unread, and any of them
could hold moves five did not.
