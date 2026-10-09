---
episode: 5
title: Meaningful Information
defaults: { tone: measured, rate: normal }
---

## Three judgments in one morning {tone: measured, note: "a story opening; concrete and unhurried, a scene being set rather than a case being argued"}

Amsterdam. {pause: 0.5} The fourth of April, 2023.

The Court of Appeal — the *Gerechtshof Amsterdam* — handed down three judgments on a single day. Three linked cases. They are written in Dutch, and I have not read them in Dutch. Everything I am going to tell you about them reaches me through English-language reporting, and I will say that again at the one point where it genuinely matters.

The people who brought the cases drive cars for a living. Some drove for Uber. Some drove for Ola Cabs. Behind them stood a British trade union, the App Drivers and Couriers Union, and a data-rights organisation called Worker Info Exchange.

Hold on to that last detail. It matters later that not one of these drivers did this *alone*.

What the drivers wanted was their own file. What the companies held about them. How the companies had worked out the things a platform works out about a driver — {pause: 0.4} which jobs arrive, what a rating means, whether an account stays open tomorrow morning.

They asked.

{pause: 1.0}

What came back was thin, {pause: 0.4} and in some cases it did not come at all. The Court of Appeal found that several of the automated processes running on those two platforms were decisions of the kind the Regulation singles out for special treatment. It found that access requests had been wrongly refused. It ordered Ola to grant them. And it said something about what an answer has to contain: {pause: 0.5} enough for the person to understand the reasons for the decision, or to challenge it.

{pause: 1.0}

But the finding this episode is built on is not about a document at all. {pause: 0.5} It is about a *person*.

Both companies told the court that a human being reviewed what the system produced. Somebody at a desk, {pause: 0.4} looking at an output, deciding whether it should stand. The court did not take that on trust. {tone: pointed} It looked at what that person actually did. {tone: measured}

{pause: 1.2}

Keep that person in your mind. We come back to them, and to the phrase an English report of this judgment uses to describe what they were actually doing.

## Where this is, and what today adds {tone: lucid, note: "orientation; open and companionable, laying out what the listener already holds"}

This is The Collisions.

Four episodes in, you are carrying four things, and today spends two of them.

The first is the controller — {pause: 0.3} the organisation that determines why data gets processed and how. That is the organisation the duties land on, whoever wrote the software.

The second is the word *solely*, from last time. The rule about automated decisions bites where a decision runs on automation alone, and putting a human in the loop is the standard way out of it.

The other two — the closed set of reasons you need before you touch data at all, and the categories walled off before any reason is reached — {pause: 0.3} you will not need today.

Today is the sequel to the first two, and it is the one people think they already know. Today is what you are told, {pause: 0.4} and what you can ask for.

The Regulation says you are owed *meaningful information about the logic involved*. Those are its words, and I will give you the sentence they sit in shortly.

Two readings of that phrase are popular and both of them lose. {tone: wry} One says it means the source code, the model, the machinery — hand it over. The other says it means a paragraph of marketing prose about how we value transparency, because nothing more is really required. {tone: lucid} Neither survives contact with the text, and by 2025 neither survives contact with the Court of Justice either.

{pause: 1.4}

The claim this episode is built to land is this one, and I will come back to it twice more before the end. The Regulation asks the system for a *reason*. It assumes that somewhere behind the answer {pause: 0.3} there is a *because*. {tone: pointed} A learned model does not hold a because. {tone: lucid} {pause: 1.2} It holds weights, and it can tell you what would have had to be different for the answer to change. Whether those two things are the same thing is the argument, and it is not one I am going to settle in this episode.

{tone: warm} One thing I am leaving out, and I would rather name it than have you notice it missing. The right we are working with today entitles you to considerably more than the one clause we are chasing — {pause: 0.3} where the data came from, who else has had it, how long it is being kept. Those are real and they are useful. I am staying with one clause, because one clause is where the collision is.

## What the machine is actually doing {tone: curious, note: "working the system out aloud with the listener; careful to describe a type and not a known platform"}

Before any rule touches this, let me describe the kind of system we are talking about — and let me be careful about what I am describing.

I am describing a *type*. The record from Amsterdam does not hand me the internals of either platform, and I am not going to invent them for you.

A platform of this kind does not run one decision. It runs several, and they are automated to different degrees.

There is allocation — which driver is offered which job. That is continuous, high-volume, and there is no human anywhere near it; {pause: 0.3} nobody could be, at that rate.

There is scoring. A model consumes a driver's history — the record of how the work went — and emits a number. Very often that number is a probability of something the operator does not want. Call it a fraud probability. It is an estimate, not a verdict.

And there is deactivation. The account stops working. {pause: 0.5} The person stops earning.

{pause: 1.0}

Now, how do those three connect? {pause: 1.0} Usually by a threshold and a queue. The score crosses a line. A case lands in a queue. Somebody opens it, sees a flag, {pause: 0.4} and clicks.

That person is where the whole legal argument lives, and the epistemic problem is this. When a company tells you a human reviews the output, you have learned something real — {pause: 0.6} about the company's account of itself. {tone: pointed} Whether you have learned anything about the *system* depends entirely on what that human sees, how long they have, and whether anything they could have done would have changed the outcome. {tone: curious}

{pause: 1.4}

That gap — {pause: 0.3} between the account and the practice — is what the Amsterdam court walked into.

## The words that do the work {tone: precise, note: "the statutory core; deliberate and even, so the structure of the provision reads as structure"}

Here is the sentence. It is paragraph one, point h, of Article 15 of the General Data Protection Regulation, and the words are the Regulation's own:

> "the existence of automated decision-making, including profiling, referred to in Article 22(1) and (4) and, at least in those cases, meaningful information about the logic involved, as well as the significance and the envisaged consequences of such processing for the data subject."

End of quotation.

{pause: 1.0}

{tone: lucid} Plainly: they have to tell you there is a machine deciding. They have to tell you how it reached the result, and what they tell you has to be *meaningful* — which is the Regulation's word, not mine. And they have to tell you what it means for *you*.

{pause: 0.8}

That last limb is the one that gets dropped, and it is worth slowing down for. It does not say tell them what the system does. {tone: pointed} It says tell them what it does *to them* — the significance, and the consequences you are expecting, for the person in front of you. {tone: precise}

{pause: 1.4}

That is the last article number I am going to lean on, and I will now give these rules names instead.

The same words appear three times in the Regulation, in three different places, {pause: 0.4} doing two different jobs.

Twice, they are a **telling** duty. One version applies where the data came from you — you filled in the form, you tapped the button — and it says the controller must tell you these things *at the time* the data is obtained, without your asking. The other version applies where the data did *not* come from you: {pause: 0.3} it was scraped, bought, inherited, inferred. Then the controller still has to tell you, within a reasonable period and at the latest within a month of getting it.

Once, they are an **asking** right. You write and ask, and the controller has to answer.

From here on: the telling duties, and the asking right. Same phrase, different trigger.

{pause: 1.0}

Now the limit, because this one gets dropped constantly. The phrase is owed, in the Regulation's own construction, *at least* in the cases of automated decision-making it has just pointed at — the ones you met last episode, where the decision runs on automation alone and hits you legally or nearly as hard. The words *"at least"* are doing real work: {pause: 0.4} they set a floor, not a ceiling. But if a controller tells you no such decision was made about you, {pause: 0.5} the most direct route to this particular disclosure is closed. You are then back to arguing about whether it really was such a decision — which, as you will have gathered from Amsterdam, is exactly what people argue about.

There is a second sentence you need, and it is short. The Regulation requires that any of this information be provided — and these are its words again —

> "in a concise, transparent, intelligible and easily accessible form, using clear and plain language".

End of quotation.

{pause: 1.0}

{tone: lucid} In ordinary words: it has to be short, it has to be findable, and it has to be readable by the person it is addressed to.

{pause: 0.8}

{tone: wry} That standard is not met by a privacy policy. Not because privacy policies are wicked, but because a document written to survive a regulator's reading is not a document written to be intelligible to a driver in a car park, {pause: 0.3} and *intelligible* is the word in the statute.

## The machinery around the words {tone: lucid, note: "the plumbing, one piece at a time; each piece lands, then the place it stops"}

Where we have got to: {pause: 0.3} a phrase you are owed, in plain language, sometimes without asking and sometimes on request. Now the plumbing around it.

Four pieces. I will give you them one at a time, and each one comes with the place it stops.

**The clock.** {tone: precise} The controller must respond without undue delay and in any event within one month; that month can be extended by two further months where the request is complex or there are a lot of them, and the extension has to be notified to you inside the first month, with reasons. {tone: lucid} Two numbers, one sentence. One month as the rule, three as the outer edge — {pause: 0.4} and silence is not an option the Regulation offers.

**The copy.** The asking right does not entitle you to a summary of what they hold. In the text's own phrase, the controller shall provide *"a copy of the personal data undergoing processing"* — those are its words. A copy.

**The limit on the copy**, which is the next sentence of the same article, and you must carry it with the rule. Quoting again: that right to a copy

> "shall not adversely affect the rights and freedoms of others".

End of quotation. Other people's data is in your file too. So is, on many controllers' reading, their commercial secrecy. Hold that thought for ten minutes.

**The refusal.** A controller may refuse, or charge, where a request is — and this is the text's phrase —

> "manifestly unfounded or excessive, in particular because of their repetitive character".

Those are its words. It sounds like a wide door. The paragraph's last line closes most of it: {pause: 0.4} the controller bears the burden of demonstrating that the request is manifestly unfounded or excessive. {tone: pointed} The default is answer; the exception has to be proved by the person relying on it. {tone: lucid}

{pause: 1.4}

And then there are the ways out of the telling duty — {pause: 0.3} the exits. The version that applies to data not collected from you has four of them, and I am giving you two.

The first is that you already have the information. Fair enough in principle; the danger is a controller deciding on your behalf that what you do is obvious.

The second is the one that matters for machines. The duty falls away where providing the information proves impossible or would involve — the Regulation's phrase — *"a disproportionate effort"*. End of quotation. The rest of that sentence tells you what the drafters had in mind: {pause: 0.3} archiving in the public interest, scientific or historical research, statistics. Archives. And the sentence after it is the limit, so keep hold of it: {pause: 0.4} where the exception applies, the controller must still take appropriate measures to protect people's rights, and the text names one of them — *"making the information publicly available"*. That is the Regulation's own example, not my suggestion.

{pause: 0.8}

So it was written for the historian with a box of letters from 1890 {pause: 0.3} and no forwarding addresses.

{tone: wry} It is now reached for by anyone who has collected the open web {pause: 0.3} and would rather not write to everybody.

## Why a duty to a person, and not a register {tone: contemplative, note: "a step back to look at the design; thoughtful, not mournful"}

Step back and ask why the machinery has this shape.

There is another way to build transparency, and it is not exotic. You could require the *organisation* to publish: {pause: 0.3} here are the automated systems we run, here is what each one decides, here is what goes into it. Publish once, for everybody, in a place a journalist or a regulator or a union can read. {pause: 0.5} A register.

Europe built the *other* thing. It built a duty that runs to an individual — {pause: 0.3} delivered to you at collection, or handed to you on request. Subject-facing.

{tone: measured} I want to be careful at this point. I am comparing two designs, not reporting a meeting in a drafting room; I do not have the legislative history in front of me, and I am not going to pretend the register was formally tabled and voted down.

{tone: contemplative} But the trade is visible from the outside, and it is real. An individual duty is precise — it gives *you* something, about *you*, that you can act on. {tone: pointed} It also scales terribly. {tone: contemplative} {pause: 1.0} It is enforced one complaint at a time, by people who mostly do not know they have the right, against organisations for whom answering properly is a cost {pause: 0.4} and answering thinly is free.

{pause: 1.0}

Which is why Amsterdam needed a union.

## Austria, and a phone contract {tone: measured, note: "a second case, told plainly; the ordinariness of the refusal is the point"}

Now the turn. {pause: 0.6}

A woman the record calls CK was refused a mobile phone contract. Not a mortgage — {pause: 0.4} a phone. The refusal followed an automated credit assessment carried out by Dun and Bradstreet Austria, which concluded she was not creditworthy enough.

You have seen this shape before. One company decides; a different company made the thing the decision was made with. Last episode that pattern produced a ruling about *who is caught*. This time it produces a ruling about *what you then get told*.

CK asked for the logic. The Austrian data protection authority ordered the company to give it to her. The company went to court and said: {pause: 0.5} what you are asking me to disclose is a trade secret.

On the twenty-seventh of February 2025, {pause: 0.3} the Court of Justice answered. {tone: precise} I have not read the judgment in the original and I am paraphrasing throughout; take every formulation that follows as reported rather than quoted.

Three things.

**First, what the phrase means.** Meaningful information about the logic involved covers the relevant information about the *procedure and the principles actually applied* — {pause: 0.3} enough that the person can understand which of their personal data was used, and how, in arriving at the result. And the standard is set by what it has to achieve: {pause: 0.4} the person must be able to understand and to contest the decision.

{pause: 1.0}

{tone: pointed} **Second — and this is the holding this episode turns on — handing over the algorithm is neither required nor sufficient.** {tone: precise} {pause: 1.2} Not required: you cannot demand the model. Not sufficient: a complex mathematical formula, or a step-by-step description of every stage of the process, does not discharge the duty. Because it does not make the decision intelligible to the person the decision was about.

{tone: wry} Sit with that for a second, because it cuts both ways and most commentary only notices one of them. The maximalist reading loses. So does the compliance officer who prints out the pipeline and calls it transparency.

{tone: precise} **Third, the trade secret.** A controller cannot simply refuse on that ground. Where it says the material contains trade secrets or other people's data, it must supply that material to the competent supervisory authority or to the court, {pause: 0.3} which then balances the competing interests and determines how far the right of access reaches. Case by case.

{pause: 1.4}

{tone: lucid} Be precise about what that third holding did, because it is easy to oversell. The Court did not decide how much secrecy has to yield. It decided *who decides* — {pause: 0.4} and moved that decision out of the controller's hands and into a regulator's or a judge's.

So: a real answer to "can they just say no". Not an answer to "what will I actually be told".

{tone: pointed} The refusal is no longer self-certifying. {tone: lucid} {pause: 1.2} That is the change.

## Back to the desk in Amsterdam {tone: measured, note: "back to the case and the person at the desk; steady and unsentimental, the finding given its full weight"}

That brings us back to the person at the desk.

Uber and Ola both argued that a human reviewed the automated outcomes — the argument you met last episode, the one that takes a decision outside the rule about decisions made by automation alone. It is the standard way out, and it is a perfectly respectable way out {pause: 0.3} when it is true.

The court rejected it on the facts. As reported in English translation — and I stress that this is a translation of a Dutch judgment, not the court's own words in the court's own language — {pause: 0.5} {tone: pointed} the review was found to amount to *not much more than a purely symbolic act*. {tone: measured}

{pause: 1.4}

{tone: precise} Two limits on that finding, and both are load-bearing.

It was a national appellate court, not the Court of Justice. It does not set a Union-wide test for when human review is genuine.

And it was a finding about those processes, on those facts, at that time. It is not a general truth that human review is theatre, and anyone who quotes it that way {pause: 0.3} is quoting it wrong.

{tone: lucid} The useful thing is narrower and much stronger. The question is *factual*, {pause: 0.4} and somebody checked. What that person could see, how long they had, whether a different click was realistically available — those are things a court can look at, and a court did.

{pause: 1.0}

So where does that leave us? {pause: 1.4} Two things so far. The telling duties and the asking right are owed to you personally, in plain language, on a clock, with the burden of refusal on the controller. And what they are owed *about* is the procedure and the principles actually applied — {pause: 0.3} to the standard that you could argue with the outcome.

## Change one fact {tone: curious, note: "a variation drill; light on its feet, genuinely asking, leaving room for the listener to answer first"}

Now let me vary one detail at a time and watch the answer move.

**One.** The controller replies to your request with the list of features the model uses and the weight attached to each. Inputs, coefficients, the lot. Does that satisfy the duty?

{pause: 1.6}

No. And notice *why*, because the reason is not that it is too little. It is information about the model. {tone: pointed} You asked about a decision. {tone: curious} {pause: 1.0} Nothing in that reply tells you which of your data went in, what it looked like when it did, or what about your case produced this answer rather than another. On the Court's standard — could you understand it and contest it — {pause: 0.3} a coefficient table gets you nowhere.

**Two.** Change one thing. The controller replies: had your cancellation rate over the last ninety days been below this figure, {pause: 0.5} the flag would not have been raised. One sentence. A counterfactual. Does *that* satisfy it?

{pause: 1.6}

Arguably, {pause: 0.4} yes. It tells you which of your data was used, how it bore on the outcome, and what you would have to dispute to overturn it. It is contestable in a way the coefficient table is not. {tone: warm} Whether a counterfactual is genuinely an *explanation*, or only a very useful substitute for one, is an argument I am going to leave standing exactly there. You do not need to resolve it today.

{tone: curious} **Three.** Change the cast instead. The model is not the platform's. It was bought from a vendor. The deployer genuinely cannot explain the output, {pause: 0.3} because they do not have the thing that produces it, and their contract does not entitle them to it.

Does the duty move?

{pause: 1.6}

It does not. The controller is whoever determines the purposes and the means — that was the first episode, and it does not bend for procurement. The vendor relationship is the deployer's problem to have solved before deploying. It is not the driver's problem, and the Regulation nowhere provides that a duty evaporates {pause: 0.3} because you contracted badly.

{tone: wry} Say that one out loud and you can hear how much of the market it describes.

## Whose problem is this {tone: lucid, note: "climbing levels of explanation one push at a time; each push a small, deliberate step up"}

A word about the level we have been reasoning at, and then I push off it once.

Almost everything I have just said is at the level of the *rule*. The duty binds; the excuse fails; the deployer owes it anyway.

Now go and look at what actually happens when you send the request. It arrives in a queue, {pause: 0.3} staffed by people whose job is to close tickets, who have no access to the model and no authority to ask anyone who does. That is an *organisational* explanation of why you got a thin answer, and it is true.

{pause: 0.8}

But it is not the cause. Push back one level. The queue is staffed that way because answering properly costs money per request {pause: 0.3} and answering thinly costs almost nothing, and no one is priced for the difference. That is the *economic* explanation, and it is the design flaw the register would have avoided. A published description is written once. An individual answer is written every time somebody asks.

Push once more, and you arrive at Amsterdam again. The reason those drivers got an answer at all is that a union and a data-rights organisation carried cases through an appellate court in another country. Individually, none of them could have. {tone: pointed} The right is individual; the only way anyone has made it work at scale has been collective. {tone: wry}

{pause: 1.4}

I will stop pushing there, because you can do this forever and the point is made.

## What the rule assumes about the machine {tone: contemplative, note: "the claim the series exists for; unhurried, room around each step, never portentous"}

Here is the beat this whole series exists for.

{pause: 0.8}

These provisions assume that a decision has reasons that can be stated. That somewhere inside the process there is a *because* — {pause: 0.4} a fact about your case that produced this outcome, which somebody could retrieve and put into a sentence. That assumption is entirely reasonable when the decision-maker is a loan officer, a case worker, a manager. It is how the rest of administrative law works.

{pause: 1.0}

{tone: pointed} A learned model has no because. {tone: precise}

{pause: 1.4}

It has parameters, fitted to a distribution, which together implement a function from inputs to an output. There is no step in that process at which a reason is recorded, {pause: 0.3} because no reason was ever formed. What can be produced afterwards is of a different kind: {pause: 0.3} attributions, which say how much each input appeared to matter and which are notoriously unstable — run two accepted methods over the same case and they can disagree about which feature mattered most. Or a counterfactual: had this been different, {pause: 0.3} the answer would have changed.

{pause: 1.4}

{tone: contemplative} So the third and last time, plainly. The Regulation asks for the reason. The machine can offer you the difference that would have changed the answer. {pause: 0.8} Those may be close enough in practice that nobody should care. They may be different in a way that matters enormously. That question is the next episode, and it is the only thing I am asking you to carry forward.

{pause: 1.0}

{tone: measured} The AI Act reaches these same platforms and tells somebody else first — the deployer — reaching the affected person only for certain decisions, and with a thinner account of the part the system played. The overlap with the duty we have worked through today is smaller than either instrument's advocates say.

## Where it is contested {tone: precise, note: "a ledger of three open joints; even and exact, each status word given a clean landing"}

Three joints, and they are in different states. I will say which, out loud, because that is the part commentary usually skips.

Whether *the logic involved* means reasons for your particular decision, or a description of how the system works in general — {pause: 0.4} **contested**, and the next episode is about precisely this argument, with Wachter and Mittelstadt on one side and Selbst and Powles on the other.

Whether a trade secret can narrow what you are told — {pause: 0.4} **moved**, in 2025, and leaning against the controller. The refusal is no longer the controller's to certify. How much has to be disclosed once a judge is looking is still open.

Whether the disproportionate-effort exit covers collection at web scale — {pause: 0.4} **contested and largely untested**. I know of no judgment that settles it. That is an absence I am reporting as of this recording, not a claim that none exists anywhere.

## As written, as enforced {tone: measured, note: "the reckoning; plain and candid, the narrator's own view clearly flagged as such"}

So who checks?

{pause: 1.4}

A supervisory authority, on a complaint. A court, if someone brings one. That is the whole of it, and both routes start with a person who knows they have a right, knows it was not honoured, {pause: 0.3} and is willing to spend a year or more on it.

Meanwhile the mechanism does produce something, reliably. It produces documentation. Privacy notices exist in enormous quantity. Request-handling processes exist. Whether any of that produces the quality the Regulation names — information a person can act on — is a separate question from whether the paperwork exists, and the Amsterdam judgments are the clearest evidence we have that the two can come apart {pause: 0.4} completely.

{pause: 1.0}

Where I come down, and this is mine rather than anybody's holding: {pause: 0.5} {tone: pointed} the 2025 judgment changed *who decides* whether you are told, and it did not change *what you are told*. {tone: measured}

{pause: 1.4}

That is a genuine improvement and it is a smaller one than it was reported to be. I am not going to fold that into a verdict about the whole architecture today. {tone: wry} The series has one of those, and it is being saved.

## What you now ask {tone: precise, note: "the closing question-set; deliberate and even, each question given room to be answered"}

So. {pause: 0.4} What does this apparatus leave you able to do with a system you have never met?

{pause: 1.6}

Ask what would actually arrive, and in what time. Write the request. Note the date. The answer is due in a month, or in three with a reason given inside the first month — {pause: 0.3} and what comes back, or does not, tells you more about the organisation than any statement it has published about itself.

Then hold the reply up and ask the question this episode was built around. Is this about the *system*, or about my *case*? {pause: 1.6} That is the significance-and-consequences limb, and it is the one the Regulation put in and almost nobody answers. A description of the model, however honest, is not it.

And then the test that swallows both: {pause: 0.4} could I contest anything with this? Not — do I understand it. {tone: pointed} Could I *argue* with it. {tone: precise} {pause: 1.6} If the answer is no, you are holding a document that satisfies nobody's duty, however many pages it runs to.

Two more, quickly. When somebody tells you that answering properly would be disproportionate, ask who decided that, {pause: 0.3} and against what. And when the answer is *that is a trade secret*, remember that this is no longer the end of the conversation — {pause: 0.4} it is a request to have somebody else look instead of you.

{pause: 1.2}

{tone: contemplative} We have a duty to give meaningful information, with a court now telling us it has to be good enough to argue with. {pause: 0.6} And we have no agreement at all about what would count.

{tone: lucid} Next time we step out of the statute entirely — one episode away from the text, the only one in this series, and then we are back inside it for good. One sentence of the Regulation, read once, and two readings of it that cannot both be right.

{tone: contemplative} Because before you can judge whether a disclosure duty is worth anything, {pause: 0.5} you need to know what an explanation *is*.