---
episode: 7
title: Two Assessments, One System
defaults: { tone: measured, rate: normal }
---

## The list that was due {tone: measured}

The second of August, 2025 was a deadline.

By that day, every Member State of the Union had to have named three things in writing.

A market surveillance authority — the body that polices products already out in the world. The one that can demand a document, order a recall, go and look.

A notifying authority — the body that appoints and supervises the private assessors who certify that a product meets the law.

And a single point of contact. One office, one address, so that anybody with a question about an artificial-intelligence system in that country knows where to send it.

Twenty-seven governments. Three names each. A date written into the statute.

The day came, and the list was not finished.

{pause: 1.4}

How unfinished is a question I cannot answer cleanly, and the reason is worth a minute of your time. There are counts in circulation. They do not agree with each other, they were taken at different dates against different obligations, and I am not going to read you a series of numbers that cannot be compared. So take the shape instead.

More than a year after the deadline, a substantial minority of Member States had still not completed the designation. And the counts of how many disagree with one another.

That is the fact this episode starts from: a vacancy.

{pause: 1.4}

An office that does not exist yet cannot disagree with anybody.

And while the office was unnamed, the obligations it was supposed to supervise were already running. The statute did not wait for its own enforcer.

## Where we are {tone: lucid}

This is The Collisions.

The premise of the series is that every AI system in Europe is governed by more than one instrument at once, and the instruments were drafted by different people, at different times, about different things. Each episode takes one seam and asks which rule actually bites, who it binds, and what falls through.

Two things from earlier episodes are load-bearing today. The controller — the one who determines the purposes and the means of processing, and therefore owes the duties. And minimisation — adequate, relevant, limited to what is necessary — which is the one that collides with something later in this episode.

Two more are in the background, and I will call them back when they are needed. Purpose limitation: data collected for one stated purpose cannot simply be repointed at another. And the special categories, where the prohibition comes first and the doors out of it are a closed list.

From the earlier series on the AI Act you need two clauses and no more. High-risk systems carry engineering duties on the people who build them. And deployers of some of those systems owe a fundamental-rights impact assessment of their own.

Today the two instruments meet at a document.

One system. Two mandatory assessments. Two vocabularies of risk that use the same English word to mean different things. Two authorities, which in some countries may turn out to be the same people. And a person, somewhere at the end of it, who is mentioned in one subclause and consulted where appropriate.

## What an assessment actually is {tone: precise}

Before any rule touches this, let me describe the thing itself — in the language of the people who do it.

An impact assessment is a document.

It usually starts as a template. Somebody opens it, and writes a description of the processing — where the data comes from, what happens to it, who it goes to. That description is normally lifted out of a design document or a solution architecture that already exists, because nobody writes it twice.

Then a table of risks. Each with a likelihood, a severity, and a score.

Then a column of mitigations, one against each risk. Encryption. Access controls. Retention periods. A review board.

Then a residual score, after mitigation, which is lower than the score before it.

Then a signature.

{pause: 1.4}

Now notice what is not in that description.

Nobody ran the system.

The document is an account of a system, written from documents about the system, by people who work on the system. At no point does the format require anybody to put an input in and see what comes out. An accuracy figure, if somebody pastes one in, is a performance number — it is a claim about how often the thing is right, not an account of who it is wrong about. And a risk register does not detect a proxy. Nothing in the format could. A proxy is discovered by measuring outcomes across groups, which is an experiment, and a risk register has no cell for an experiment.

Hold that description. Both of the duties I am about to teach you are duties to produce something like it.

And two things you are likely to assume about those duties are wrong, so let me refuse them now.

The first is that data protection law is a bag of independent rules that a compliance team works through. It is sequenced. One duty bites when you choose how to build the thing. A second bites before you start processing. A third bites when the second one comes back with an answer nobody likes. Miss the order and you have missed the mechanism.

The second is that it works like a decision tree — that there is a list of triggers, and if your system is not on the list you are outside. There is a list. The list is expressly examples.

## By design {tone: precise}

The first duty is one you have probably heard named and probably misheard.

**Data protection by design and by default.** Most people hear that and think of a settings page. Privacy-friendly defaults. The toggle that starts in the off position.

That is a consequence of it. It is nowhere near the size of it.

Article 25 of the General Data Protection Regulation says that the controller shall — and these are the Regulation's words — *both at the time of the determination of the means for processing and at the time of the processing itself, implement appropriate technical and organisational measures* — and that is the end of the Regulation's words.

From here on I will call it **by design**.

Read the two moments, because the first one is the one that does the work. At the time of determining the means. Not when the data arrives. When somebody decides *how* — which is to say, at architecture, at procurement, in the meeting where a team decides whether to build a model or buy one, whether to keep raw records or hashes, whether the logs will hold the inputs or only a reference to them. Before a single row of anybody's data has moved.

And then again, continuously, while the processing is happening.

Plainly: the duty is to build it a certain way, and then to keep it that way.

There is a phrase inside that provision I need to earn, because it is odd. The controller must act *taking into account the state of the art*. Not the best available — the state of the art. A moving standard. What was appropriate in 2019 is not a defence in 2026, and nobody sends you a notification when the line moves. That is a peculiar thing to say to any field. It is a very peculiar thing to say to a field that re-baselines every quarter.

{pause: 1.4}

So: a standard you are obliged to keep checking, in a field that keeps moving it.

And now the limit, because this is exactly the kind of rule people leave the room holding too widely. The same sentence that says *state of the art* also says *the cost of implementation*, and the nature and scope and context and purposes of the processing, and the risks. All of those are in the same breath. So by design is not a counsel of perfection. It is a proportionality sentence: the better the available technique and the higher the risk and the cheaper the fix, the less excuse you have. Drop the cost clause and you will overstate this duty every time you apply it.

Then the second paragraph, and this is the *by default* half. Only personal data which are necessary for each specific purpose are to be processed. And the Regulation tells you what that "only" applies to. Four things: how much you collect, how far you process it, how long you keep it, and who can reach it.

{pause: 1.4}

Of those four, which two do you think actually get written into a design document — and which two get forgotten?

{pause: 1.4}

My answer, and you should treat it as mine rather than as anybody's finding: the first two get decided on purpose, because somebody has to choose what fields to capture and what the system does with them. Retention and access are the two that drift. They are set once, by default, in a configuration nobody revisits, and they are the two the Regulation went out of its way to name.

{pause: 1.4}

So far, one thing. Before you process anything, the law has already reached into the design meeting.

## Likely to result in a high risk {tone: precise}

The second duty is the one this episode is named for, and it turns on four words that are going to cause you trouble unless we deal with them now.

*Likely to result in a high risk.*

The trouble is not the words. The trouble is that a second instrument uses the same English word about the same machine to mean something else entirely.

Here is the Regulation, in Article 35, and again these are its words: where a type of processing *is likely to result in a high risk to the rights and freedoms of natural persons, the controller shall, prior to the processing, carry out an assessment of the impact of the envisaged processing operations on the protection of personal data.* End of the Regulation's words. I will call it **the impact assessment**.

Now. Read what the risk is a risk *to*, and what it is a risk *from*.

To: the rights and freedoms of natural persons. From: the processing.

The other instrument does something different. It classifies a *system* as high-risk according to what the system is for — the domain it operates in, the decision it feeds. That is a property of a product, assigned by category, and it is assigned before anybody knows whose data will go into it.

One word. Two objects.

{pause: 1.4}

So, a question, and take your time with it. When somebody tells you that a system is high risk — what have they actually told you?

{pause: 1.4}

They have told you almost nothing, until you ask which statute they are speaking. Under one, they have told you the system sits in a listed category, which is a fact about the product. Under the other, they have told you that this particular processing of these particular people's data is likely to hurt somebody, which is a fact about a situation. A system can be high-risk in the product sense and generate almost no processing risk. And a perfectly mundane system, pointed at the right database, can be the other thing.

A listener who lets those two collapse into one word will get every allocation question in this series wrong. That distinction is the one I would have you keep from this half of the episode.

Then: *prior to the processing*. Not before go-live. Not before launch. Before the processing — and processing, as the Regulation defines it, includes collection, and adaptation, and use. Which means that for a model, the training run is processing. So the assessment belongs before the training run, not before the product announcement. Those can be a long way apart.

And that is the first sign of the problem this episode ends on: the document comes before the thing it describes.

When must you do one? The Regulation gives a general test and then says an assessment shall *in particular* be required in three named cases. In particular. Examples, not a gate.

I will give you two of the three, and the first is worth hearing in the Regulation's own language. It is *a systematic and extensive evaluation of personal aspects relating to natural persons which is based on automated processing, including profiling, and on which decisions are based* that produce legal effects or similarly significantly affect them — and that is the end of the quotation. That is the one that catches scoring, ranking, sorting: the profiling systems this series keeps meeting. The second is processing *on a large scale* of the special categories. The third is about systematic monitoring of public space, and I am leaving it there.

*Large scale* is undefined in the text. I am not going to give you a threshold, because the Regulation does not contain one and inventing one would be the exact failure this series exists to avoid.

What must the assessment contain? The Regulation says it *shall contain at least* four things, and I am going to say them once, quickly, because the point is not the four. A systematic description of the processing and the purposes; an assessment of the necessity and proportionality against those purposes; an assessment of the risks to people's rights and freedoms; and the measures envisaged to address them.

In plain terms: describe it, justify it, work out what could go wrong for people, and say what you are going to do about that.

Two more pieces and then we can put it together.

The controller must seek the advice of the data protection officer, where one is designated. And — this is the only place a human being who is not an employee appears in the whole architecture — here is the Regulation again: *where appropriate*, the controller shall seek the views of data subjects or their representatives on the intended processing, *without prejudice to the protection of commercial or public interests or the security of processing operations*. End of the Regulation's words. So the one consultative duty owed to the people being assessed arrives conditional, and comes with a commercial override written into the same sentence.

Finally, the review. The Regulation does not say annually. Quoting it: *where necessary*, the controller shall carry out a review to assess if processing is performed in accordance with the assessment, *at least when there is a change of the risk represented by processing operations*. Those are its words. The trigger is a change in the risk.

And one sentence about what happens when the assessment comes back badly. Quoting the next provision: where the assessment *indicates that the processing would result in a high risk in the absence of measures taken by the controller to mitigate the risk*, the controller shall consult the supervisory authority prior to processing. That is the provision's own language, and the thing it describes is called prior consultation. I am naming it and moving on.

{pause: 1.4}

So we have two things now. A duty that bites when you decide how to build. And a duty to write a document about the risk before you start — with a review that fires when the risk changes, and a referral upward when you cannot fix it.

## Why this rule and not another {tone: contemplative}

There was another way to do this, and Europe did not take it.

Licensing. A regulator looks at the system before it runs, and says yes or no. That is how a good deal of product regulation works.

Licensing does not scale to processing. Every organisation in Europe processes personal data, most of them in dozens of ways, and most of those ways change every few months. A regime that required an official to approve each one would need an official behind every project in the Union, forever.

So the choice was self-assessment with documentation. You assess yourself. You write it down. You keep it. And the regulator arrives afterwards, if it arrives at all, and reads what you wrote.

Look at what survives of the licensing model in the finished text. Exactly one thing: prior consultation. And notice the condition on it. You consult the authority when *your own assessment* says the risk cannot be mitigated. The trigger for external scrutiny is a sentence the regulated party writes about itself.

That is the accountability paradox in miniature, and let me be precise about what I am claiming. The trade was real scrutiny of a few systems for shallow scrutiny of nearly all of them. Whether that trade was right is a question about institutions.

And who inside an organisation actually writes these documents — whether the people who sign them have any power, whether the documentation produces trustworthiness or only the record of it — that is a different series in this programme, and it is not today's. You do not need to carry it.

## The collision {tone: pointed}

Now put the two instruments on the same system and watch what happens.

A firm deploys a model that sorts people. Under the data protection Regulation it is a controller, and it owes the impact assessment: risk to rights and freedoms, arising from processing, assessed before the processing, supervised by a data protection authority.

Under the AI Act, the same firm may be a deployer of a high-risk system, and it may owe a fundamental-rights impact assessment of its own: a different document, with a different object, supervised by a market surveillance authority.

That is the series' recurring collision and today it takes its plainest form. The other instrument reaches these same facts and demands a second assessment about a different thing. Same system, same week, same organisation, two documents.

The legislature knows. The AI Act contains a sentence that acknowledges the seam — it tells deployers that they may use the information the provider has supplied to help meet their obligation to produce the impact assessment. I am giving you the effect of that sentence rather than its wording. And read what the effect is. It is help: one assessment may feed the other. It stops there. Neither replaces the other, and nothing in it says the two can be merged into one document.

{pause: 1.4}

Underneath the paperwork there is something harder than duplication.

The data protection instrument says: collect less. Keep it for less time. Limit who can reach it. Those are principles, and two of them are minimisation and storage limitation.

The AI Act says: govern your training data, keep your logs, monitor the thing after it is on the market, be able to show what it did.

Both of those are binding. On the same organisation. About the same system. On the same day.

The engineer who deletes to comply with one is failing the other. The engineer who retains to comply with the other is failing the first. There is a resolution in principle — keep the minimum necessary for the second purpose, and say so — but it is a resolution somebody has to construct, in a room, with a lawyer, and it is not written down anywhere as an answer.

## Which regulator, and where {tone: lucid}

That brings us to the authorities, and to a piece of vocabulary this series owes you.

The usual understanding is that you complain to your own country's regulator and your own country's regulator deals with it. That is not how the Regulation is built, and a small set of defined terms carries the machinery.

Start with **cross-border processing**. Each Member State establishes an independent public authority under this Regulation — a supervisory authority, twenty-seven of them, roughly. Cross-border processing is processing that happens in the context of establishments in more than one Member State, or processing by a single establishment that substantially affects, or is likely substantially to affect, data subjects in more than one Member State. Note the second limb. You can be in one country and still be doing cross-border processing, if the people you affect are spread.

A **supervisory authority concerned** is one that is concerned because the controller is established in its territory, or because data subjects there are substantially affected, or because a complaint has been lodged with it. So a complaint makes an authority concerned.

And **main establishment**. Here is the definition in its own words: for a controller with establishments in more than one Member State, it is *the place of its central administration in the Union, unless the decisions on the purposes and means of the processing of personal data are taken in another establishment of the controller in the Union and the latter establishment has the power to have such decisions implemented*, in which case that one is the main establishment. End of the definition.

Hold the *unless*, because it is where the fights are. The main establishment is not automatically the headquarters. It is wherever the deciding actually happens, if the deciders can make it stick.

The main establishment determines which authority leads. The others are concerned, and a concerned authority that disagrees with the lead authority's draft decision cannot simply overrule it. It may raise a **relevant and reasoned objection** — an objection which clearly demonstrates the significance of the risks the draft decision poses for the fundamental rights and freedoms of data subjects, and, where applicable, for the free flow of personal data.

That is a defined instrument with a standard attached. You must show the significance of the risk. Disagreeing is not enough.

There is a whole chapter of this Regulation about how these authorities cooperate, and a procedure for what happens when they still cannot agree. I have summarised a chapter in a sentence, and I am telling you plainly that I did, because you should know there is machinery there that today's episode is not walking through.

## Change one fact {tone: curious}

Three variations. Each changes one thing, and each changes the answer.

**First.** The deployer is a public authority, and in that Member State the data protection authority has also been named the market surveillance authority for AI.

Now one office holds both mandates. The same lawyers, the same technologists, the same building, the same budget line — reading the same system, twice, with two different questions. Under one statute they are asking whether this processing is likely to result in a high risk to people's rights. Under the other they are asking whether a product on their market conforms to requirements.

Those are not the same question, and they do not have the same standard of proof. One is supervisory and preventive. The other is conformity policing, with recall powers behind it. Whether any Member State has in fact made that arrangement I cannot tell you — that count is not established anywhere this programme has been able to reach, and I am not going to estimate it. But it is the arrangement a serious published argument is asking for, and we will come to that argument in a moment.

**Second.** Change the provider. Now it is established outside the Union entirely, with no establishment anywhere in it.

Then there is no place of central administration in the Union, which means, reading the definition as it stands, that there is no main establishment — and therefore no lead authority. The one-stop-shop has nothing to lead with. Every authority whose residents are substantially affected is a concerned authority, and none of them is the one in charge.

The Regulation does have a device for a controller with no Union establishment — a designated representative. It carries the obligations. It is not a place where a central administration sits.

**Third.** Keep everything, and change the release cadence. The system is updated weekly.

Now run the review provision. Quoting it: a review at least when there is a change of the risk represented by the processing. Closing the quotation. Each weekly update changes the model a little. No single one of them plausibly changes *the risk*. So the trigger never fires — not because anybody evaded it, but because the provision was drafted for systems that change in steps, and this one changes in a slope.

And run by design against the same facts. The duty bites at the time of determining the means. When, in a system that is re-determined every Tuesday, is that?

{pause: 1.4}

Three changes. A regulator with two hats. A provider with no home. A system with no moment.

## Naming the level {tone: contemplative}

When something goes wrong with these assessments, people reach for an explanation, and the explanation they reach for depends on where they work.

The organisational answer is that the assessment is written by the team that wants the project approved. Which is true, and it is not a scandal — the only people who understand the system work on it, and the document is a condition of the thing they have spent a year building.

But *organisational capture* is a convenient name for everything upstream of it. Push back one level and ask what produced it. The instrument chose self-assessment over licensing. Self-assessment means the assessor is the assessed. So what looks like a failure of corporate virtue is a design decision made in a legislature in 2016, arriving on a Tuesday in a project meeting.

The economic answer is that an assessment costs roughly the same whether the organisation has forty thousand employees or four. Fixed costs fall hardest on the smallest deployers. Push back a level on that one too, and you get something uncomfortable: the practical weight of the duty runs inversely to the size of the organisation carrying it. The largest controllers have standing teams who produce these documents efficiently and well. That is my reading of the incentive, not a finding by anybody.

And the rights-based level. In the whole of this architecture, the person being assessed appears once — in the subclause that says their views may be sought where appropriate, with the commercial override attached.

That connects to a tool this series built a few episodes ago. Ask of any account of a system: who is it addressed to? A justification is addressed to an institution, and it shows that the process was proper. An explanation is addressed to a person, and it earns its name by making a decision contestable.

Both of today's assessments are justifications. Neither is addressed to the person the system decides about. That is not an oversight in either instrument. It is what they are for.

## What the rule assumes about the machine {tone: pointed}

Now the question this whole series exists to ask. What does the rule assume about the thing it is governing?

The impact assessment assumes three things, and it assumes them in its own operative words.

It assumes you can give a *systematic description* of the envisaged processing operations. In advance.

It assumes you can assess *necessity and proportionality* against a purpose, which requires knowing the purpose, fully, before you start.

And it assumes you can assess the *risks to the rights and freedoms* of people — before any of those people have encountered the system.

For a database, those assumptions hold. A database does what its schema says. You can describe it in advance because somebody designed it in advance, and if you want to know what it will do, you read the design.

For a trained model, the assumptions are inverted. The behaviour is discovered after the training run, by evaluating it. And the behaviour that matters — the group it is worse at, the correlation it found, the input nobody thought of — is discovered later still, in use, by users.

So the document is written about a system that does not yet exist in the form that will cause the harm.

{pause: 1.4}

Say that again, slowly, because it is the claim of the episode. Both instruments require an assessment before the thing exists. Neither of them contains a mechanism for the moment somebody finds out what it actually does.

There is the review provision, and I have already shown you why it does not carry that weight — it fires on a change in the risk, and a discovery is not a change. The risk was always there. What changed is that somebody noticed.

Note carefully what I am not saying. I am not saying the assessment is worthless. Forcing an organisation to write down its purpose, before it starts, in a document a regulator can later demand, does real work — it is why purpose limitation is enforceable at all. What I am saying is narrower and harder to fix. The apparatus is front-loaded, and the knowledge is back-loaded, and nothing in either instrument closes the gap between them.

## Where it is contested {tone: measured}

Three joints, and they are in different states.

The first is whether data protection authorities should be the AI Act's enforcers, and it has a named answer. Joanna Mazur, Claudio Novelli and Zuzanna Choińska, writing in the *International Data Privacy Law* journal in March 2026, under the title "Should data protection authorities enforce the AI Act? Lessons from EU-wide enforcement data". They examined how actively data protection authorities across the Union already enforce in cases involving AI-based products and automated decision-making systems. And they recommend that those authorities be included as market surveillance authorities for high-risk systems under points three to five of one annex of the AI Act.

Three points of one annex. That narrowness is the most serious thing about the proposal — it is an argument for merging the part of the job where the existing regulators already have a track record, and not the rest. I have not read the paper in full, so I am not going to characterise their data or their method beyond what they say they did.

The disagreement underneath is empirical, and it is about capacity. Not about whether data protection authorities are competent — about whether they have the people. Every hour spent policing conformity of a product is an hour not spent on a complaint about processing.

The second joint is whether one document can satisfy both instruments. Contested, and unresolved. The bridging sentence assumes the assessments can help each other. It stops well short of saying they can be merged, and nobody has authoritatively said what happens to an organisation that files one document and calls it both.

The third joint is only contested in one direction. Among people who work with both instruments, it is settled that "high risk" cannot safely share a word across them — they will tell you so within a minute of being asked. Everywhere else, including in a good deal of writing about AI regulation, the two are used interchangeably. Settled among specialists, unsettled in the room.

## As written, as enforced {tone: measured}

One reason this part of the Regulation is not decorative: the money.

Failing to assess is directly fineable, at a ceiling calculated on worldwide annual turnover, and it does not require anybody to have been harmed. That is unusual for a documentation duty, and it is part of why these documents get written at all.

What I am not going to give you is a tally of enforcement. This programme does not hold one, and a plausible-sounding number is exactly the kind of thing that gets repeated afterwards.

What I can tell you is the asymmetry. The data protection side of this has decades of institutional practice behind it, in one form or another, and a fine architecture that reaches these duties directly. The AI Act's assessment machinery, in a substantial minority of Member States, was still waiting for someone to be named as its enforcer more than a year after the deadline for naming them.

And as this is recorded, in September 2026, I have found no case anywhere in the Union in which one system's two assessments were examined against each other — no decision, no opinion, nothing testing whether the document written for one instrument answered the question asked by the other. That may be because it has not happened. It may be because nobody has looked. Either way, the seam has not been litigated.

## What you now ask {tone: lucid}

So what do you take to the next system you meet.

Ask which assessment it needs, under which instrument — and whether anyone has checked that the same document answers both questions, or merely been assured that it does.

{pause: 1.4}

Ask who wrote it. And then ask the question that follows, which almost nobody asks out loud: what did they want the answer to be? A document produced by the people who need the project approved is not thereby false. It is a document with a direction, and you should know which way it points before you read the risk scores.

{pause: 1.4}

And when somebody tells you the system is high risk — stop them. Ask whether they mean risk *to* the person in front of the system, or risk *from* the product on the market. Two statutes, one word, two answers. If they cannot tell you which they meant, they do not yet know which duties they owe.

Then ask which authority supervises this thing — and whether that authority has ever supervised anything like it. That question has a list behind it, and we started today with a list that was not finished.

{pause: 1.4}

And one about time. What would have to change before anyone reopened the assessment — and would anybody notice if it did?

{pause: 1.4}

Both of these instruments ask organisations to assess the risk of harm before the harm arrives. Neither of them says a word about who pays when it does.

For that there is a third instrument. Written in the 1980s, rewritten in 2024, and built out of a completely different idea about what a broken thing is.

That is where we go next.