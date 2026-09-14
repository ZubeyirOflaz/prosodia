---
episode: 1
title: "The Gate"
defaults: { tone: measured, rate: normal }
---

## A system runs for the last time {tone: measured, rate: slow}
In the middle of December 2025, a piece of software in the Netherlands ran for the last time.

It had run every week for years. Each week it took a map of a Dutch city, already divided into small cells, and gave every cell a score for the days ahead. A high score meant more expected crime. The police called the high cells hotspots, and the hours inside them hot times. Burglary, car theft, bicycle theft, nuisance — those were the four things it looked for.

Its name was the Criminaliteits Anticipatie Systeem. The Crime Anticipation System. CAS.

It was piloted from 2015 and went national in 2017. The Netherlands was the first country in the world to run predictive policing across an entire country, and this was the thing it ran.

Then the Nederlandse Politie switched it off. There was no announcement at the time. It was reported two months later, in February 2026.

The reason the police gave was this. The operational value of the system was unclear. There had never been clear goals. There had never been measurable success criteria. And in Amsterdam, roughly one incident in fifty was correctly predicted. {pause: 1.0}

One in fifty.

Ten years of a national programme, and the people who ran it could not say what it had achieved — because nobody had ever written down what achieving it would look like.

Hold that. The law this series is about has a great deal to say about a system like CAS. But it does not begin by asking whether the thing worked.

Not first. {pause: 1.2}

## Where we are {tone: measured}
This is *The Instrument*: twelve episodes on a single piece of European law, and on what that law can and cannot see.

The law is Regulation (EU) 2024/1689 — the Artificial Intelligence Act — as amended in 2026. The thing worth understanding about it, before any article number, is the shape Europe chose. Europe decided to regulate artificial intelligence the way it regulates lifts, toys and medical devices. As a product. Something made by someone, placed on a market, carrying obligations from the moment it leaves the workshop.

Whether that was the right choice is the question this series ends on. I am not answering it today, and later in this episode I will tell you exactly why I am holding it back.

You need nothing to start. Every term after this one is earned inside the series.

Today is the first question the Act asks of anything at all: is this an AI system? Get through that, and everything else in the Regulation is waiting on the other side. Fail it, and this law has nothing whatsoever to say about you.

Two habits I need you to put down before we go further.

The first: this Act is not a bag of independent rules you can pick through for the ones that apply to you. It is a sequence. Each part hands work to the next, and any part read alone will mislead you.

The second costs technically-trained listeners the most. The Act is not a decision tree. There is no flowchart at the bottom of it that converts your system into an answer. There are definitions with contested edges, and most of the real work is arguing about which side of an edge you are standing on.

One more thing. I am not going to open a series about AI regulation on a chatbot. You have heard that example. It is a poor teaching case, because everybody already agrees a chatbot counts — and the interesting part of a definition is never its centre.

## The system, before any rule touches it {tone: precise}
So: what did CAS actually do, described in the language of the people who build these things rather than the language of the law.

Criminology calls this place-based predictive policing. The working formulation — the one that circulates in the field rather than belonging to any single author — runs roughly like this: applying statistical or machine-learning methods to past data in order to identify likely targets for police intervention. Notice what that contains and what it leaves out. It tells you where to look. It says nothing about whether anyone is caught.

CAS drew on three sources. BVI, the central police crime database. GBA, the municipal population administration. And CBS — Statistics Netherlands — for demographics. The data went in depersonalised and anonymised. Out came a number, per cell, per week.

How big was a cell? The public sources give two figures, and they are not close. The official record is the Dutch government's Algorithm Register, and until that settles the point I am not going to give you a number I cannot stand behind.

And one property of CAS matters more than any of its numbers. It was a closed system. An officer sent to a square could not see which data had produced that square. The number arrived. The reasons did not.

## What the text actually says {tone: quoting, rate: slow}
These next words are the Act's own. Regulation 2024/1689, Article 3, point 1. It defines the term "AI system", and it reads:

"a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments."

End of definition. {pause: 1.2}

That is the whole of it. From now on I will call it the gate, because that is its function. Everything else in this Act stands on the far side of it.

## The load-bearing word {tone: lucid}
Said plainly: a machine that works something out for itself, rather than being told the answer step by step — and whose working-out comes back as something that acts on the world. A prediction. Content. A recommendation. A decision.

The load-bearing word is *infers*. Almost everything else in that sentence is elastic. "Varying levels of autonomy" includes very little autonomy. "Explicit or implicit objectives" means the objective need never have been written down. "Outputs that can influence physical or virtual environments" is close to everything. Strip the elastic away and one question is left. Does it infer?

Let me get that word honest before we use it, on something with nothing at stake.

A thermostat with a bimetallic strip. The metal bends as it warms, and at a certain bend it closes a circuit. Nobody would call that inference. A person chose the temperature and built the choice into the metal.

Now a different thermostat. This one watches when you come home for three weeks, and starts the heating before you arrive. Nobody wrote your schedule down. It derived your schedule from the pattern of your comings and goings, and then did something in the world about it. That is inference. The rule governing its output was not supplied to it. It was worked out.

The distinction has nothing to do with complexity. A ferociously complicated formula, written out longhand by a human being, is not inference. A very simple regression is — and by regression I mean a formula whose numbers were fitted to past data rather than chosen by a person.

So — a payroll system, ten thousand lines long, applying tax rules a legislature wrote. Does it infer? {pause: 1.6}

No. Every rule inside it was handed to it by a person. It is enormous, and this definition is not interested in it.

## Working the gate on CAS {tone: measured}
Now let me do this properly, the way it would be done in practice, because the method is half of what I want you to take from the episode. The moves are: name the issue, name the instrument, state the test, apply it to these facts, put the best case against yourself, then conclude.

The issue: was CAS an AI system within the meaning of this Act.

The instrument: the gate.

The test has elements, and they run together — all must be present, though several are so wide they cost nothing to satisfy.

Now apply them to CAS. It was software running on a computer, so machine-based is satisfied. It produced its weekly scores without a person recomputing them, which clears the autonomy element, and the bar there is very low, because the definition says *varying* levels. It was scoring for expected crime, which is an objective — and notice that the definition will accept an *implicit* one, a point we come back to. Its outputs were predictions, the first thing the definition names. And patrol cars moved on the strength of those outputs, which is influence on a physical environment.

That leaves inference. Was the mapping from three databases to a weekly number written down by a person, or fitted from data?

Fitted. It was a model.

Now the counter-argument, and it is a real one — the standard objection from statistics, which you will hear from anyone who has built this kind of thing. CAS is a regression over some crime counts and some census columns. Calling that artificial intelligence is a category error; actuaries have done this sort of work since long before anyone used the phrase. The objection is right about the technology and beside the point in law. The gate does not ask how advanced a method is. It asks whether the output was derived rather than dictated. A regression derives.

Conclusion: CAS goes through the gate. Comfortably.

## Why this rule, and not a list {tone: curious}
Why write the test that way at all? Because an instrument like this can take one of two shapes, and the other shape lost.

The first shape is a list. You name the techniques — machine learning, say, and logic-based systems, and statistical methods — and you say that anything built with one of them is in. Read the list, find your technique, know where you stand.

The second shape names no technique at all. It describes a function, and asks whether your system performs it.

A list has one enormous virtue, and it is the virtue of legal certainty: you can read it and know the answer. And it has one fatal flaw. A list ages, and it ages against people with an incentive to age it. Every technique named can be renamed, recombined or superseded, and each time, the law has to be reopened by legislators who move at the speed of legislators. A definition built on inference has nothing in it to rename.

What was traded away is exactly that certainty, and the trade is not small. Nobody can read the word "infers" off the page and know where it stops. Which is why the Commission had to publish guidelines on the definition in February 2025 — a document whose whole job is to say what a single word in a single sentence means. And the most-quoted line in those guidelines is a negative one.

The text says a system "may exhibit adaptiveness" after deployment. *May.* Not must. So adaptiveness is not required. A system trained once, shipped, and never updated again in its working life is still an AI system under this Act. If you arrived believing that AI means "it keeps learning", set that belief down. It is the commonest mistake made about this definition, and the law is explicit against it.

There is a serious objection to the whole enumerating habit — the charge that an instrument built by listing only ever sees what it listed. That objection was put to the Commission formally, in writing, before this Act existed, and I will come to who put it.

## Change one fact {tone: pointed}
The way to feel the edge of a rule is to stand beside it and move one thing.

Change one. Delete the model. Put in its place a rule written by a policy officer in a memo: send a car to any square with three or more burglaries in the last month. Same three databases. Same map. Much the same squares, in practice — high-crime squares stay high-crime squares. Same cars, same streets, and the same residents watching the same patrols go past.

Is it an AI system? {pause: 1.6}

Arguably not. Nothing infers. A person chose the rule and wrote it down; the computer only counts. The Commission's guidelines lean the same way — simple rule engines fall outside. So the whole of this Act, with everything in it, governs one of those two systems and stays silent about the other, while the people living in those squares experience no difference at all.

That is the first serious thing this episode has to hand you, and it is not yet a criticism. It is a fact about what kind of test this is.

Change two. Keep the model, change the output. Instead of scoring squares, it ranks named individuals by their likelihood of offending. Still through the gate — nothing about that changed. But it is now standing against a prohibition, and prohibitions are where this law bites hardest. That is episode five's, and I leave it there.

Change three needs another piece of machinery. Two, in fact. And the first of them is the concept this entire series rests on.

## The second gate {tone: measured}
This Act attaches almost no duties to building a system. Build the most alarming thing you can imagine, keep it in the room you built it in, never run it for real and never hand it to anybody — and most of this Regulation stays asleep.

Two things wake it. They are separate triggers, and collapsing them into one is the commonest way people get this wrong.

The first trigger is supply. The Act calls it placing on the market, and defines it through a second term, making available. I am going to paraphrase these two rather than recite them, and I will tell you when I stop paraphrasing. Placing on the market is the first time a system is made available on the Union market. Making it available means supplying it there, for distribution or for use, in the course of a commercial activity — and it counts whether or not anybody pays. Give the thing away, and it is still supply.

The second trigger involves handing the thing to nobody at all. The Act calls it putting into service, and for this one I want the Act's own words, because four of them decide this episode. Article 3, point 11. Putting into service means, and I am quoting: "the supply of an AI system for first use directly to the deployer or for own use in the Union for its intended purpose." End of definition.

Two terms in that sentence I owe you a working sense of, and only a working sense, because episode three is where they are properly earned. A provider is the party that puts a system out under its own name. A deployer is the party using a system under its own authority.

And the four words that matter here: *or for own use.* You put a system into service when you first use it yourself, for the thing it was built for. Nobody receives it. Nobody buys it. The duty attaches anyway.

So: who placed CAS on the market? {pause: 1.4}

Nobody. It was never sold, never licensed, never supplied to anyone outside the force. The Dutch police built it and the Dutch police ran it.

But market placement is not the only road in, and this is the step I want you to make with me rather than take from me. The Act's definition of provider works like this. You develop a system, or have one developed for you. Then you do one of two things with it: you place it on the market, or you put it into service. And a single condition hangs over both of those — you do it under your own name or trademark. Not just the second one. Both.

The Dutch police took the second road. They did not sell it; they ran it themselves, under their own authority, as theirs. Building it was not enough. Running it was. And that is what makes the Nederlandse Politie the provider of the very system it also deploys: one organisation sitting on both sides of a split that the whole Regulation is built around.

What that split does, and why nearly every real dispute in this field lives inside it, is episode three. Today, lodge two things. Both roles can sit in one organisation, and in the public sector they very often do. And a system built and used inside one organisation reaches this law through a different door than a system that is sold. Same software. Different door. The obligations waiting behind each are not identical.

## The reach {tone: measured}
The second piece is scope: who this law can reach at all. That is Article 2, and I will call it the reach.

What follows is my summary of the list, not its wording. The reach runs to providers who place systems on the Union market or put them into service there — and the text goes out of its way to add that it makes no difference whether those providers sit inside the Union or in a third country. That phrase will come back in a moment, so let me fix it now: in the Union's own drafting language, a third country is simply any state outside the Union. Nothing ordinal about it. Britain is a third country. So is Japan.

The reach also runs to deployers located in the Union. To importers and distributors. And at the end of the list it runs to affected persons located in the Union — the residents of those scored squares, who appear in this Regulation as people it applies to, and who, through most of the rest of it, are almost nobody.

Now change three. CAS is built and run for Dutch cities, but by an American vendor with no European establishment, scoring Dutch squares from a server in Virginia.

The reach has a limb for exactly that. Article 2, paragraph 1, point (c). Here the Act speaks for itself, and I am quoting: "providers and deployers of AI systems that have their place of establishment or are located in a third country, where the output produced by the AI system is used in the Union." End of quotation.

Output. Not the company's address, and not the server's. What the thing produced, and where that landed. That single word pulls a firm which has never opened a European office or signed a European contract inside European law, because a Dutch patrol car drove somewhere on the strength of what it made.

There is a great deal more in the reach, and I would rather name what I am leaving than let you think it isn't there. Article 2 carries exclusions — whole categories the Act steps back from. National security, and military and defence purposes. Systems developed and put into service for the sole purpose of scientific research and development. Research, testing and development carried out before a system is placed on the market at all. Purely personal, non-professional use. And software released under free and open-source licences, which carries substantial exceptions of its own. Each of those is a hole shaped like an argument. Each deserves more time than this episode has, and I am naming them in order to leave them.

## Five levels, and only one of them is the law's {tone: contemplative}
Now something slightly odd, because it is the habit I most want you to take away.

When a system goes wrong you can explain it at several levels, and people argue bitterly about which level holds the real explanation. Watch how that works here.

The technical level: CAS was a weekly model over three databases with no visibility into its own reasoning. True.

But a description is not a cause. What CAS was technically is a record of what an organisation chose to buy and keep. Push back one.

The organisational level: a closed box sat in a command room, with no channel for anyone to ask why. Better — it explains why nobody inside caught the problem. It still describes rather than causes. Push again.

The institutional level: a police force ran a decade-long national programme without ever defining success for it. Which raises an obvious question — how does that survive ten annual budgets? So there is an economic level underneath as well: a procurement decision nobody ever had to justify against an outcome, because no outcome was ever specified.

And last, the rights level, where most public argument about predictive policing actually lives. Scoring a patch of ground is not a decision about a person. Not formally. It becomes one when an officer acts on it. Which is precisely why this kind of system slipped so many nets for so long — the effect on people is real, and the paper trail of individual decisions is thin.

The point of that exercise is this. Each level is a convenient way of describing everything upstream of it, rather than a cause in its own right. And the gate — the test we have spent this episode on — sits at the first level only. It is a technical test. It asks what the software does. The other four are invisible to it.

## What the rule assumes about the machine {tone: pointed}
Which brings me to the thing this series exists to do, and which I will do in every episode: set what a system actually does against what the rule presumes it does.

Take the definition again, and listen for what it takes for granted. It presumes a system that has an objective — explicit or implicit, but an objective — and whose outputs can be read as inferences toward that objective. The whole sentence is built on purposefulness. It defines a thing that is *for* something.

CAS had outputs. CAS had no measurable objective. And we do not have to infer that from outside, because it is the reason the police themselves gave for stopping: no clear goals, no measurable success criteria. Ten years, and the honest answer to "what is this for" turned out to be: nothing anyone could check.

The gate itself survives that. A system with a vague aim still passes; implicit objectives count, and a fuzzy aim is still an aim. The trouble waits downstream. The machinery this Act builds on top of the gate classifies systems by what they are for. Risk tiers key off purpose. Documentation describes purpose. Oversight is oversight of performance against purpose. Every one of those is a measurement taken against a stated aim.

So what does that machinery do with a system whose aim was never made measurable?

Nothing. {pause: 1.2} It has no test for it. You can hold a perfectly compliant file on a system that has never been shown to do anything at all.

And notice what CAS gave the officers who used it, because the distinction is worth keeping. When a square lit up, what arrived was a justification for going there: the system says so. What did not arrive was an explanation: this is what drove the number. Those are different objects. A justification tells you that you may act. An explanation tells you why — and it is the only one of the two you can argue with.

Ask it as three questions, of any automated decision you meet. Can this be contested? By whom? On what basis? For a resident of a scored square in Amsterdam, across those ten years, the answers were no, nobody, and none.

## Where it is contested {tone: neutral}
Three disagreements, and I want to mark each for what it is, because a listener who cannot tell settled from contested is defenceless in this field.

Does a deterministic system infer? Contested. The Commission's guidance leans toward excluding simple rule engines, and nobody working on this treats the boundary as clear. Real systems are rarely either-or: they are a hand-written rule set with a fitted component somewhere in the middle. The honest position is that we will not know where the line falls until cases are decided.

Do those guidelines bind? Settled. They do not. They are non-binding. They tell you what the Commission thinks, which is worth a great deal in a meeting and nothing in a courtroom. The interpretation that will actually bind comes from courts, years from now, on facts nobody has met yet. More guidance than that may be impossible at the moment — and that is an answer, not a failure to find one.

And the largest. Is a definitional gate the right architecture at all, against the alternative of regulating uses regardless of technique — of saying that scoring people for police attention is governed, whether a model did it or a memo did it?

Here is the objection I promised you, and its holders. On 18 June 2021, the European Data Protection Board and the European Data Protection Supervisor published a joint opinion on the draft Act — Joint Opinion 5/2021. Their specific target was the way the Act handles prohibitions, which they attacked as a "positive list": enumerate the forbidden things, and whatever is not enumerated is permitted by silence. They also argued that risks to *groups* of people should be assessed, not only risks to individuals, which a system that scores neighbourhoods rather than names makes very concrete. The extension from their argument to the definitional gate is mine, not theirs — but it is the same objection, one level up. Build an instrument on enumeration, and you have built something that only sees what it listed.

Where does the weight of opinion lie on that? Genuinely open. I know of no settled answer, and I am not going to manufacture one for the sake of a tidy paragraph.

## As written, as enforced {tone: measured}
So what did this law actually do about CAS?

Nothing at all — and not because of a loophole. Because of a calendar. The heavy part of this Act, the regime for high-risk systems, splits into two streams with two different start dates. One stream is for systems that sit inside a product Europe already regulates: a lift, a toy, a medical device. The other is for systems that stand on their own — software that is not a component of anything, which is what CAS was. For that second stream, the heavy regime applies from 2 December 2027. That date has already moved once, deferred by the 2026 amendment, for reasons that belong to episode eight. CAS was switched off two years before the rules arrived.

I will not tell you that CAS would have been a high-risk system, because that is not obvious, and it is worth a clause to see why. The policing categories in this Act are written around natural persons — risks to a person, profiling of a person, assessment of a person. CAS scored patches of ground. Whether a place-scoring system lands inside the heavy regime at all is a real question, and it is the same point I made from the rights side a few minutes ago, arriving from the other direction. Classification is episode four's work, and I leave it there.

Something did produce public knowledge about CAS, though, and it was not this Regulation. It was a voluntary national algorithm register, run by the Dutch government, which anyone can read. Nobody compelled the police to describe CAS in it. They described it anyway.

Date-stamp that whole passage, incidentally. The deadline moves. The shape of the problem — a regime arriving after the systems it was written for have come and gone — does not.

## Where I come down, and what I am holding {tone: pointed}
Two judgements. One small and mine; one held back.

Mine, for today: the gate is the right kind of test wearing the wrong kind of name. What it identifies is systems whose behaviour was derived rather than dictated. That is a real and useful distinction, because derived behaviour is the kind you cannot fully audit by reading the source code. What it does not identify is dangerous systems, and it was never built to. So the word standing at the door is doing engineering work, not moral work. Almost everyone reading this Act for the first time expects the opposite, and the disappointment that follows is usually aimed at the wrong provision.

And the one I am holding. This series ends by asking whether treating artificial intelligence as a product placed on a market was the right choice. I am not answering that today, I want you to know that I am not, and I want you to know why. You have not seen the machinery. A verdict on an instrument you have met only the front door of is a prejudice with citations attached. Episode twelve lands it. From episode three onwards, every episode puts one piece of evidence on that table, and I will tell you each time it happens.

## What you now ask {tone: lucid}
Four questions to carry out of this — the things I want in your hands when you meet a system you have never met before.

One. Does this system infer, or does it apply rules somebody wrote down? That single distinction decides whether an entire body of European law exists for it.

Two. What is its stated objective — and is there a measurement that would tell you whether it met that objective? If the second answer is no, the first answer is decoration.

Three. Whose output is used where? That is the thing that carries this law across a border, and it will reach organisations where nobody in the building has read a word of it.

Four, and this one is CAS's own. If this system were switched off tomorrow, could anybody say what was lost?

For a decade of Dutch predictive policing, the answer to the fourth was no. That does not prove the system was useless. It proves that for ten years, nobody built the means to find out.

## Handover {tone: measured}
We now know what this Act counts. We do not know why anyone believed a law could be written in time for a technology that moves this quickly, or what it means to aim a document at a moving target.

So next episode we step away from the instrument. Once, and only once. Episode two has no article numbers in it: it asks whether regulating a technology is a coherent thing to attempt at all, and which parts of an instrument can be changed without reopening the statute — and who holds that power. Then we are back inside the text, and we stay there.

Episode three: who you are in the picture.

## Sources {tone: neutral}
Four things, if you want to go to the material yourself.

The Regulation. Regulation (EU) 2024/1689, the Artificial Intelligence Act, as amended by the Digital Omnibus on AI in 2026. Read it in the consolidated version on EUR-Lex, which stitches the amendments into the original; the definition quoted in this episode is Article 3, point 1, and the scope provision is Article 2.

The European Commission's guidelines on the definition of an AI system, published in February 2025. Short, readable, and non-binding — which is itself the lesson.

The joint opinion of the European Data Protection Board and the European Data Protection Supervisor on the draft Act, Joint Opinion 5/2021, dated 18 June 2021. It is the clearest statement of the objection this episode ended on, and it is published on the Supervisor's own website.

And the Dutch government's Algorithm Register, at algoritmes dot overheid dot nl, where the Crime Anticipation System is entry 81228922 — a state describing its own software to the public, voluntarily, with no regulation obliging it to. The police's account of why they stopped comes from the reporting of February 2026.