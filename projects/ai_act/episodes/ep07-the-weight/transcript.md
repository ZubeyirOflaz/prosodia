---
episode: 7
title: The Weight
defaults: { tone: measured, rate: normal }
---

## A finding, read flat {tone: neutral, rate: slow, note: "no colour at all; this is a document being read, not a story being told"}

The Federal Aviation Administration did not have a complete understanding of Boeing's safety assessments of a system called MCAS until after the first accident.

That sentence is written to be unexciting. {pause: 1.4}

It is a finding. It sits inside a report numbered AV2021020, published on 23 February 2021 by the Office of Inspector General of the United States Department of Transportation. The title runs: *Weaknesses in FAA's Certification and Delegation Processes Hindered Its Oversight of the 737 MAX 8*. Fourteen recommendations followed it.

The report holds more findings than I am going to give you. Two of them matter today.

The first is that the independence of the manufacturer's own certification personnel from company influence was not ensured. The second came from a survey the agency ran on itself. Fifty-six per cent of its aircraft-certification staff felt there was too much external influence on the agency, affecting safety.

Now the small part. The part this whole episode turns on.

The system commanded the aircraft's nose down, by moving the horizontal stabiliser, under certain conditions, triggered from angle-of-attack data. It could do that repeatedly. It existed so that the aircraft would handle like the model before it, so that pilots would need minimal retraining. And in the safety assessment, the thing that would stop it going wrong was a procedure crews already knew. Recognise runaway stabiliser trim. Cut it out.

The mitigation was a person.

## Where we are, and what today adds {tone: measured}

This is The Instrument.

You are already carrying four things from earlier in this series, and you do not need to recall them precisely — only to know they are there. You know how the Act decides whether a thing is an AI system at all. You know that duties in this Regulation attach to roles, not to technologies, and that the role that matters most is the split between whoever provides a system and whoever deploys it. You know how a system climbs into the high-risk tier. And you have heard the argument about whether risk was the right organising idea in the first place.

Today is the bill.

Everything in this series so far has been about getting a system classified. This episode is about what classification costs. What a provider of a high-risk AI system must actually build, document and hand over. What a deployer must actually do with it. And whether any of that reaches the thing you would want it to reach.

One disclosure before I go further, and it is not a small one. The report I opened on is American, it is about aviation certification, and there is no AI Act anywhere near it. MCAS is not an AI system in this Regulation's sense and I am not going to pretend otherwise. I am using that report for exactly one thing: what a human-oversight requirement assumes about the people it relies on. European law, here, does not correct the assumption that failed in Seattle. It writes the same assumption into an article and gives it a number.

So hold the analogy loosely. In this Act's vocabulary, Boeing would be a provider. The airlines would be deployers. The flight crew would be the human oversight. And the FAA would be a market-surveillance authority that had handed a large part of its own assessment work to the party being assessed.

That last one is a whole subject of its own and I am leaving it.

## What kind of thing this chapter is {tone: lucid}

Before any article, two corrections. You are probably arriving with one of them and it is worth killing both early.

The first wrong picture is a bag. A pile of independent rules, each satisfiable on its own, tick and move on. The Act says otherwise in its own text: when a provider chooses its risk-management measures, it must give due consideration to the effects and possible interaction resulting from the combined application of the requirements. They are wired to each other. Change your data and your documentation changes. Change your documentation and what your human overseer can know changes.

The second wrong picture is a flowchart. A decision tree, with a yes-or-no at each node and an answer at the bottom. Nothing in here terminates. These are duties that run for as long as the system is on the market, and several of them are drafted as *processes*, not as states.

There are seven of these requirements. I am going to teach you three of them properly and let the rest arrive as they are needed, because seven things read aloud in a row is four things you will lose.

I will call them, from here on, *the requirements*. And the thing they produce — the thing that proves they happened — I will call *the file*.

Watch the file. It is the most important object in this episode.

## The first requirement, and the word inside it {tone: precise}

Article 9 is headed risk management system, and if you hear "system" and think "a document", you will misread everything downstream.

Here is what the Act says it is. A risk management system shall be understood as — and these are its words — *a continuous iterative process planned and run throughout the entire lifecycle of a high-risk AI system, requiring regular systematic review and updating*. End of quotation.

So: not a document. A practice, running the whole time the thing exists, which produces documents as evidence that it ran.

And now the word. The one that decides whether you understand this chapter or merely admire it.

Article 9 requires that the measures be such that the relevant residual risk associated with each hazard, and the overall residual risk, is — quoting — *judged to be acceptable*. Closing the quotation there.

Residual risk. The risk left over after you have done everything you are going to do.

Most people meet that phrase and assume it means the risk you must now go and eliminate. It does not. The Act does not ask for elimination. It asks that what remains be judged acceptable, and it does not, in that article, say by whom or against what. A high-risk AI system can be fully compliant with Article 9 while carrying risk that somebody has looked at and decided to live with.

Acceptable. {pause: 1.4}

That is not a loophole. That is what risk regulation *is*, in every field that has it, and pretending otherwise would leave you expecting a safety guarantee from an instrument that never promised one.

Now the limit, because a rule without its limit is a rule you will over-apply. Article 9 says the risks it covers are only those which may be reasonably mitigated or eliminated through the development or design of the system, or through providing adequate technical information. Risks that live somewhere else — in the institution using it, in the incentives around it, in what a civil servant does with a number — are not what Article 9 is pointed at.

Remember that. It comes back.

## Data, and a question that sounds technical {tone: lucid}

Article 10 governs the data. Training data, validation data, testing data.

Its most quoted sentence asks that those data sets be — and these are the Act's words — *relevant, sufficiently representative, and to the best extent possible, free of errors and complete in view of the intended purpose*. That is the end of the quotation.

Read carelessly, that says the data must be perfect, which is absurd and would make the article unsatisfiable. Read properly, two qualifiers are carrying the whole sentence. *To the best extent possible* softens error-freeness and completeness into something an engineer could argue about. And *in view of the intended purpose* makes representativeness relative — representative of the population this system will actually be pointed at, not of the world.

Whether even that is achievable for any real dataset is genuinely disputed. A good many people who work on this say the drafting reaches further than any practice can go, and that the qualifier is the only thing keeping it honest. I would put that one down as contested, not settled.

But the sentence people quote is not the sentence that does the most work. That one is further up, in the governance practices Article 10 requires you to have. Among them: the formulation of assumptions, in particular with respect to *the information that the data are supposed to measure and represent*.

Stop on that. It is the only place in the Act that asks the question I want you to leave with.

Let me use a system you already know. The Dutch Tax Administration's risk-classification model in its childcare-benefits division — the one that ran from 2013, that sorted applications so officials could scrutinise the ones it scored highest, whose variables included dual nationality and low income and whether the applicant's name read as non-Dutch. Amnesty International's report on it is called *Xenophobic machines*. In May 2022 the Dutch government accepted that institutional racism in part of the Tax Administration was a root cause of what followed.

You have the facts. I only want one property of the model.

It was trained on examples of correct and incorrect applications. So here is the question. {pause: 1.4}

How did anyone know which ones were incorrect? {pause: 1.8}

Because somebody had investigated them and found them so. Which means the labels record something narrower than they appear to. Not which applications were wrong — which applications had previously been *found* wrong, by an organisation, with its own history of where it chose to look.

That is exactly the assumption Article 10 makes you write down. Not a technical detail. The difference between a model that finds fraud and a model that reproduces an institution's past attention.

And Article 10 goes on to require examination for possible biases, and appropriate measures to detect, prevent and mitigate the ones you find — with a clause aimed straight at this: especially, it says, where data outputs influence inputs for future operations.

Which is the feedback loop. You investigate where the model points. Those investigations become next year's labels. The model points harder in the same direction.

Now the limit, and it is a real one. Article 15 — accuracy, robustness and cybersecurity — names feedback loops explicitly and requires they be reduced as far as possible. But it says that of high-risk systems that *continue to learn after being placed on the market*. A model that is trained once and frozen does not fall inside that sentence. The loop I just described can happen entirely outside it, through the organisation, in the data gathered for the next version.

So the Act sees this problem. It sees it in one article as an assumption you must document, and in another as a defect you must mitigate if your system keeps learning. It does not, anywhere, forbid the thing itself.

**Change one fact.** Suppose the labels had been drawn from confirmed adjudications rather than from opened investigations. Ask yourself what moves. {pause: 1.4}

Nothing in the classification rules moves. The system is high-risk either way; the use case is what does that. Nothing in the human-oversight article moves. Article 10 is the only place in this Regulation where that change is visible at all — and it is visible there as a paragraph in a file.

Where we are, before I go on. Two things are established. The chapter's first requirement permits leftover risk, so long as someone judges it acceptable. And its second requires you to write down what your data were really measuring — which is a genuine and unusual demand, and its output is a document.

## The file, and the person who might read it {tone: measured}

Article 11 requires technical documentation, drawn up before the system goes on the market, kept up to date, containing at a minimum the elements set out in Annex IV. I am not going to walk Annex IV. It is a list, it is long, and read aloud it would teach you nothing you could hold. What is worth knowing is that smaller firms and start-ups may supply those elements in a simplified form, on a template the Commission is to produce, and that notified bodies must accept that form.

Article 12 requires logs. Not server logs in the sysadmin sense — the Act's phrasing is that the system shall technically allow for the automatic recording of events over the lifetime of the system, so that its functioning can be traced. And there is a matching duty on the other side: a deployer keeps the logs it controls for a period appropriate to the purpose, and at least six months.

Then there are several more articles of provider bookkeeping which I am going to skip, and I am telling you I am skipping them rather than letting you assume the chapter ended.

Because the beat that matters is what all of it is *for*, and that is Article 21. Upon a reasoned request from a competent authority, a provider gives that authority all the information and documentation necessary to demonstrate conformity — in a language the authority can easily understand. And, on the same kind of request, access to the automatically generated logs, so far as the provider controls them.

That is the file's reader. Everything upstream exists so that a sentence like that one can be answered.

Notice who is not in it.

## What the provider tells the deployer {tone: precise}

Article 13 is where the chapter hands over.

It requires that the system be designed so that its operation is — quoting — *sufficiently transparent to enable deployers to interpret a system's output and use it appropriately*. Closing there. And it requires instructions for use.

"Instructions for use" sounds like a manual. In this Act it is defined — at Article 3 — as the information the provider supplies to inform the deployer of, in particular, the system's intended purpose and its proper use. Which makes it the legal instrument through which knowledge, and with knowledge a share of responsibility, moves from the party that built the thing to the party that switches it on.

What has to be in it is specific. The characteristics, capabilities and limitations of performance. The accuracy levels the system was tested against, with their metrics, and any known or foreseeable circumstances that could affect them. Any known or foreseeable circumstance which may lead to risks to health, safety or fundamental rights. And the human oversight measures, including the technical measures put in place to help a deployer interpret the outputs.

Everything in that list is the word *known*, or the word *foreseeable*, doing load-bearing work.

Hold that thought for four minutes.

## The overseer {tone: pointed}

Article 14. Human oversight.

Almost everyone arrives at this article believing it means a person approves each decision. It does not say that, anywhere, for almost anything.

What it says is this. High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they — and here is the phrase — *can be effectively overseen by natural persons during the period in which they are in use*. That is the end of the quotation.

A capability, built in at design time. Not an approval step.

And the Act then specifies what that capability has to enable. The person assigned oversight must be able to properly understand the system's relevant capacities and limitations, and monitor its operation, including so as to detect anomalies and unexpected performance. They must remain aware of what the Act itself calls, in brackets, *automation bias* — its own gloss on this is the tendency of automatically relying, or over-relying, on the output produced by the system. They must be able to correctly interpret the output. They must be able, quoting again, *to decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse* its output. And to interrupt it — through a stop button or a similar procedure that allows the system to come to a halt in a safe state. Closing the quotation.

Now the restatement, plainly. Article 14 does not put a human in the loop. It requires that a human *could* get into the loop, understand what they are looking at, and stop it.

And the limit, because this is the rule most often stated without one. There is a place in the Act where two people are required — where no action may be taken on an identification unless it has been separately verified and confirmed by at least two natural persons with the necessary competence, training and authority. That rule is narrow. It applies to one sub-point of one category, remote biometric identification. And even there it is switched off for law enforcement, migration, border control and asylum, where Union or national law considers applying it disproportionate.

So if you leave today thinking the AI Act imposes four-eyes review on high-risk AI, you will be wrong about almost every system you meet.

Then Article 26, the deployer's side, and one sentence of it is the most useful sentence in this episode. Deployers — quoting — *shall assign human oversight to natural persons who have the necessary competence, training and authority, as well as the necessary support*. Closing.

Four nouns, and the Act joins them. Competence. Training. Authority. Support.

**Change one fact.** Take a deployer who does it almost right: the overseer is qualified, trained on the system, understands its limitations — and works three levels below anyone who can stop the line. {pause: 1.4}

Authority. {pause: 1.4}

Remove that one word from the arrangement and Article 26 is not satisfied, and more to the point the oversight is decorative. A person who can recognise the failure and cannot act on it is not a control. They are a witness.

**Change one more.** Now invert it. The overseer has every scrap of authority and no way of knowing when to use it, because the circumstance in front of them is not in the instructions for use.

That is the Boeing finding, in the Act's own language. The procedure existed. Crews knew it. What was missing was the knowledge that this was the situation it applied to — and the regulator did not fully hold the manufacturer's own safety assessment of the system until after the first accident.

Article 14 and Article 26 together are a very well-drafted answer to the second problem and no answer at all to the first.

## Does oversight work? {tone: contemplative}

This is a contested joint and I am going to tell you which way the weight leans.

Against. In the strong form — the belief that a human monitor reliably catches an automated system's errors — the weight of evidence leans against it, and has for a long time.

The human-factors research on automation bias, and on how badly people perform sustained vigilance tasks where the thing they are watching is usually right, is consistent, and it is old. I am going to characterise that literature rather than name a paper, because I could not verify the specific citations I had to hand, and a confident name is worth less than an honest description.

Here is what makes this more than an academic point. Article 14 names automation bias in its own text. The drafters knew. They wrote the failure mode into the provision — and then kept the human as the mitigation anyway, with an instruction that the person remain *aware* of a tendency that decades of work suggests awareness does not fix.

That is my own judgement and I will mark it as mine: human oversight, as drafted, is the weakest control in this chapter. Not useless. Weakest. And it is the control the rest of the architecture leans on hardest when a system does something nobody planned for.

## Why this rule, and not a different one {tone: lucid}

Step back and ask what else the drafters could have written.

The alternative to a process duty is an outcome duty. A rule about what the system must not do, rather than about how carefully you must build it.

I am going to say what one would sound like, and I am flagging first that the words are mine and not the Act's, because nothing in this Regulation is drafted this way and I do not want you carrying an invented sentence around as though it were law. An outcome duty would read something like: this system shall not discriminate. Or: this system shall be accurate to within a stated figure.

Those are my illustrations. They are not in the text.

And you can see why not. A conformity assessment happens before the system meets anybody. An outcome duty cannot be certified in advance, against a system whose behaviour depends on where it is deployed, on whose data it meets, on what an organisation does with its output. Ask a notified body to certify that a thing will not discriminate and you have asked it to predict the future.

So the Act requires something a file can evidence. Did you run a risk-management process? Did you document your data assumptions? Did you build in an oversight capability? Those are all checkable, before anything happens, by reading.

And now the trade, which is the sentence I most want you to keep.

A provider can satisfy every article in this chapter and still place on the market a system that harms people — as long as the process ran and the file is in order.

That is not cynicism. It is what *ex ante* process regulation is. It buys you administrability and scale and something to check before harm rather than after, and the price is that compliance and safety are two different questions with two different answers.

Ask yourself, honestly: could a system satisfy all seven requirements and still hurt somebody? {pause: 1.8}

Yes. And the Act knows it, which is why there is an enforcement loop for what happens afterwards — post-market monitoring, and a duty to report serious incidents. I am not teaching that loop here. It belongs with enforcement, it is a later episode's material, and you do not need it today.

But the definition is worth ninety seconds, because it contains something nobody expects. A *serious incident*, in this Act, has four limbs. Death or serious harm to health is one of them, obviously. Serious harm to property or the environment is another. The one people miss is in the middle: the infringement of obligations under Union law intended to protect fundamental rights.

So a rights breach is, in this Regulation's own vocabulary, an incident — in the same list as a death. That tells you something about what the drafters were reaching for, and the next beat tells you how far the reach actually gets.

## Naming the level {tone: contemplative}

Let me do something deliberate, and only once.

When something like the benefits scandal happens, you can explain it at several levels, and each one feels like the cause.

*Technical.* A classifier trained on labels that recorded institutional attention. A control law triggered from a single kind of sensor input.

*Organisational.* A decision that this product would need minimal retraining, because retraining costs money. A decision that a risk score was sufficient grounds to act against a family.

*Institutional.* A regulator that did not hold the manufacturer's own safety assessment. A tax authority with recovery targets and no route for a person to contest a number.

*Economic.* Underneath both of those. "No simulator training required" is a figure on a sales sheet. So is a recovery target.

Each of those levels is a convenient way of describing everything upstream of it. Push on the technical choice and you find the organisational one. Push on that and you find money.

And now the fifth level, which is where you actually wanted to end up. *Rights.* What the system did to people.

Here is the finding, and it is the reason this chapter is worth forty minutes. Nothing in the requirements reaches that level. Not one of them. They are duties about process, and their subject is a system and a file. The Act does have an instrument pointed at rights, and it is Article 27 — the fundamental rights impact assessment.

It is a procedural duty.

I am describing Article 27 rather than reading it to you, and I will be straight about why: I do not have its text in front of me in a form I am willing to quote. What I can tell you is what the rest of the Act does with it. Elsewhere, in a provision about live biometric identification by police, the Act makes the use lawful only where the authority has *completed a fundamental rights impact assessment as provided for in Article 27*. So it is real, it is a precondition, and it produces a document.

And it attaches to deployers — certain deployers. Largely public bodies.

**Change one fact.** Take a high-risk system deployed by a public authority, and hand it instead to a private firm doing something very similar. {pause: 1.4}

The system has not changed. Its classification has not changed. The requirements have not changed. But the duty to assess its impact on fundamental rights may simply not attach — and one of the Act's two rights-facing instruments disappears from the picture, silently, because of who owns the building.

Whether that assessment turns out to be a genuine constraint or a template somebody fills in is still moving, and nobody can tell you yet. Nothing in this chapter applies before December 2027.

## What the rule assumes about the machine {tone: pointed, note: "this is the centre of the episode; slow, no flourish"}

So, finally, the question this series exists to ask.

What does Article 14 assume about the system it governs?

Three things. It assumes a system whose outputs a trained person can interpret correctly — and interpret in the time available, which in a cockpit is seconds and in a benefits office is however long the queue allows. It assumes that person has been told what the system's limitations are. And it assumes that being told is enough to make them a control.

Where does that information come from? Article 13. The instructions for use. Written by the provider.

So trace the chain. The overseer's competence to override depends on their knowledge. Their knowledge comes from the instructions. The instructions contain what is *known* or *foreseeable* to the provider.

Which means the entire oversight requirement is bounded by what the organisation that built the system already understood about it.

Say it the other way round. The Act requires a provider to tell a deployer what the limitations are. It has no mechanism whatsoever for limitations the provider does not know about.

And that is the category that produces the accidents. Not the risk on the register. The behaviour that surprised the people who designed it.

That is precisely the shape of the finding I opened with. The safety assessment named the mitigation, and the mitigation was a crew procedure, and the procedure was sound — for the situation the assessment imagined. The regulator did not fully hold that assessment until afterwards.

European law, on this point, does not correct the assumption. It writes it into an article, gives the article a number, and requires that it be documented.

That is the third time I have said a version of the same thing, and I have said it three times on purpose. This chapter regulates a process, evidences it with a file, and the file can be complete while the system is not safe.

## The relief valves {tone: measured}

I have a whole chapter left and about four minutes for it, so I am going to compress it and say so.

Chapter VI is the Act's innovation machinery, and its centrepiece is the AI regulatory sandbox. If that sounds like a test environment, the Act's definition is more interesting than that: a controlled framework *set up by a competent authority*, in which a provider can develop, train, validate and test an innovative system, under a plan agreed with that authority, for a limited time, under regulatory supervision.

A regulator is inside it. That is what distinguishes it from a staging server.

Every Member State must ensure it has at least one, operational by 2 August 2027. Which is four months before the high-risk requirements bite for the Annex Three use cases — so the safe place to experiment is meant to exist before the duties do.

Two legal consequences are worth your attention, and they are the reason firms care.

First, the exit report. When a provider leaves, the authority writes up what was done and what was learned, and the Act says market-surveillance authorities and notified bodies shall take that report *positively into account*, with a view to accelerating conformity assessment to a reasonable extent. A document produced by a regulator that other regulators must weigh in your favour is a genuinely valuable object.

Second — and here is where you must keep the limit attached — no administrative fines. Where a provider observes the sandbox plan and follows in good faith the guidance the national authority gave, the Act says no administrative fines shall be imposed for infringements of this Regulation.

And now the carve-back, in the sentence immediately before it. Participants *remain liable under applicable Union and national liability law for any damage inflicted on third parties* as a result of what happens in the sandbox. So the regulator will not fine you. The person you injured can still sue you.

Sandboxes are the part of this Act that industry likes most. I will note something the text itself implies about how much we know: national authorities must report annually to the AI Office on how their sandboxes are going, with incidents and lessons learned, and those reports do not yet exist, because the sandboxes largely do not yet exist. The enthusiasm is running ahead of the evidence, and the Act's own evidence-gathering mechanism has not reported.

One more thing in this chapter is already live, and it is the only duty in this entire episode that is. Article 4 requires AI literacy — defined by the Act as skills, knowledge and understanding allowing providers, deployers and *affected persons*, taking account of their respective rights and obligations, to make informed deployment of AI systems and to gain awareness of the opportunities and risks. It has applied since 2 February 2025. Not a training course. A competence obligation, and the definition reaches to the people a system is used on.

And the 2026 amendment added one provision I will name and not explain: a new article permitting the processing of special categories of personal data for the purpose of detecting and correcting bias, which Article 10 now points at. Its conditions are not something I am going to teach you today.

## As written, as enforced {tone: measured}

So what is the status of everything I have just described? {pause: 1.4}

None of it applies yet.

The requirements, the file, the oversight duty, the deployer obligations — for the stand-alone use cases in Annex Three, they apply from 2 December 2027. For systems embedded in products already covered by Union product legislation, from 2 August 2028.

And when they do apply, the way a provider demonstrates compliance is conformity assessment. Conformity assessment runs, in the main, against harmonised standards — and a standard confers its legal effect only once it has been cited in the Official Journal.

So the question that decides whether any of this is real is not in this chapter at all. It is: who writes those standards, and do they exist?

As of June 2026, on the evidence available, the answer to the second half is no. That is the next episode, and so is the half of the aviation report I did not use — the half about what happens when a regulator delegates assessment to the party being assessed.

## What you now ask {tone: warm}

Three questions to take with you, and they work on systems that have nothing to do with this Regulation.

First. When someone tells you a human is in the loop, ask what that human is supposed to be able to *do* — and in how long, with what information, and on whose authority. All four. Competence without authority is a witness. Authority without information is a guess.

Second. Ask whether the obligation in front of you is about process or about outcome. And then ask the follow-up that makes it useful: could this obligation be fully satisfied by a system that harms people? If the answer is yes, you have not found a scandal. You have found out what kind of rule you are reading.

Third, and this is the one I would want you to use tomorrow. Where did the training labels come from — and what were they actually recording?

Not what they are called. What they recorded.

Because a label that says "incorrect application" may be recording an adjudication. Or it may be recording an investigation. Or it may be recording nothing more than where somebody, once, decided to look.