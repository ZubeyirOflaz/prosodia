---
episode: 1
title: The Gate
defaults: { tone: measured, rate: normal }
---

## A system switched off {tone: measured}

In the middle of December 2025, the Dutch national police stopped running a piece of software they had been running for ten years.

The stopping was reported two months afterwards, in February 2026.

The software was called the Criminaliteits Anticipatie Systeem — the Crime Anticipation System. Everyone called it CAS. Once a week, it took the map of a Dutch city and cut it into small squares. Each square got a score for the week ahead. How likely was a burglary here. A car stolen from that street.

It produced times as well as places. The people who ran it called the outputs hotspots, and hot times.

How big was a square? The published descriptions of CAS contradict each other on that, so I am not going to give you a figure. Small. Small enough for one car.

CAS was piloted from 2015 and ran nationally from 2017. The Netherlands was the first country in the world to run predictive policing across a whole country. For a decade, patrol shifts in Dutch cities were shaped in part by those squares.

Then the police worked out that they could not say whether any of it had worked.

That is close to their own account of why they stopped. The operational value was unclear. There were no clear goals. There were no measurable success criteria. And in Amsterdam, of the incidents that actually happened, roughly one in fifty had been predicted.

Ten years. Nobody had ever written down what the thing was for.

{pause: 1.4}

And in all that time, nobody asked the question this episode is about. Nobody asked whether CAS was, in law, an artificial intelligence system.

## Where we are, and what today adds {tone: lucid}

This is The Instrument.

Europe has decided to regulate artificial intelligence the way it regulates lifts, toys and medical devices. As a product. Something placed on a market, by somebody, for somebody else to use — and therefore something that can be made to meet requirements before it goes out of the door. Over this series we build that instrument from its foundations upward, and at every stage we ask what the product frame can see, what it structurally cannot, and whether anybody can actually enforce it.

You need no law and no code to follow this, and no earlier episode either. Every term after this one is earned inside the series.

Today is the entrance. Before any of the machinery can touch a system, the system has to *count* — it has to be the kind of thing this law is about at all. That test is the whole of today.

Two assumptions to put down before we start, because most people arrive holding at least one.

The first is that this law is a bag of rules — a list of things you may not do with a computer. It is an architecture instead. The parts hold each other up, and a rule read out of its place in that architecture will mislead you every time.

The second assumption is more tempting, and it belongs to anyone with technical training. It is that the law works like a decision tree — that you answer a fixed set of questions in order and come out the far end with an answer. It does not behave that way. The words in it are contested, the guidance about them is not binding, and a great deal of it will not be settled until courts get hold of it years from now. Some of what you will hear today is genuinely unresolved, and I will say so when it is.

## What CAS actually did {tone: precise}

Start with the machine, in the language of the people who built it, before any legal word touches it.

CAS ran on a weekly cycle. It drew on three sources of data. The central police crime database — BVI. The municipal population administration — GBA. And demographic statistics from Statistics Netherlands — CBS. That data was depersonalised and anonymised before it went in. Out the other end came the scores: the squares, and the hours.

It covered four kinds of crime, and only four. Burglary was one. Car theft was another. And *only four* is the part worth keeping, because a system that scores a square for four things is silent about everything else that happens there.

One more property, and it is the one that matters most. CAS was a closed system. An officer looking at a hot square could not see which data had produced that square.

Think about what that leaves the officer holding. A patrol goes to a street because of a number, and nobody in the building can say what the number is made of.

So CAS offered no explanation, and no justification either. Those are two different things, and it withheld both. An explanation tells you how the number came about — which street, and which years of recorded crime pushed the score up. A justification tells you why acting on the number was the right thing to do. CAS gave an officer neither. It gave an output.

Criminology has a name for what CAS was: place-based predictive policing. The working definitions in that literature come to much the same thing — statistical technique applied to identify likely targets for police intervention. I am giving you the sense of the term there, not a citation. The target is a square on a map. The intervention is a car.

So, before any law: a weekly statistical model over three databases, producing geographic risk scores that direct where officers go, with no visibility into its own reasoning.

Now we ask what the law would call it.

## What the text actually says {tone: quoting, rate: slow}

The law is Regulation (EU) 2024/1689 — the Artificial Intelligence Act. The definition sits in Article 3, point 1, and this is the whole of it. Quoting now.

"A machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments."

End of quotation.

## The gate gets a name {tone: measured}

{pause: 1.4}

That is the only definition of artificial intelligence that matters in European law, and from here on I am going to stop reading you numbers and call it what it is. The gate.

## The word that carries the weight {tone: pointed}

One word in that sentence does more work than all the others put together.

*Infers.*

Everything else in that sentence is either loose or optional. Loose is not the same as absent — a thing that meets none of them is still out. But look at how little they exclude. "Machine-based" rules out almost nothing. "Varying levels of autonomy" takes in a system with hardly any. And "may exhibit adaptiveness" — that word *may* is the most argued-over syllable in the Act. The European Commission published guidelines on this definition in February 2025, and the line from those guidelines that gets quoted more than any other is a negative one. Because the text says the system *may* exhibit adaptiveness, adaptiveness is not required. A system that never learns another thing after the day it ships is still an AI system.

So put the optional parts aside and you are left with a working question, and it is a plain one.

Does the thing figure out how to produce its output — or does it follow rules a person wrote down?

That is the gate. That is what you can carry out of this episode and use on Monday. Not "is there a neural network in it". Not "did somebody call it AI in the brochure". Does it *infer*.

## Why a word, and not a list {tone: contemplative}

It did not have to be built this way, and the alternative is not hypothetical — it was the first draft.

The Commission's original proposal, published on the twenty-first of April 2021, defined an artificial intelligence system by pointing at an annex. The annex listed techniques and approaches: machine learning, logic- and knowledge-based systems, statistical methods. If your thing used one of the listed techniques, you were in. If it did not, you were out.

A list has one enormous virtue. You can read it, and you can know.

A list also has one fatal property. It ages. And worse than ageing, it can be walked around by anybody willing to describe their technique with a different noun. Name the methods and you have told every engineer in Europe exactly which words to stop using.

So the list went, and a functional definition came in. The Act now names no technique at all. It describes a behaviour — inference — and catches anything that behaves that way, whatever the vendor calls it.

Something real was traded away for that. Legal certainty. Nobody can read the word "infers" off the page and know where it stops. That is precisely why the Commission had to publish those February 2025 guidelines: the definition needed explaining almost as soon as it existed. And here is the part to keep. Those guidelines are not binding. They are the Commission's view of the text, and they carry weight, and they are not law. The reading that will actually bind everybody comes later, from courts, on facts nobody has thought of yet.

That is settled, by the way, and worth marking as settled. The guidelines do not bind. Almost nothing else today is that clean.

## Running the test on CAS {tone: precise}

Take the gate to the system.

Was CAS machine-based? Obviously. Did it operate with some level of autonomy? It produced its weekly scores without a human deciding each one. Did it have objectives? It had at least an implicit one: mark the squares where crime is likely. Did its outputs influence a physical environment? A patrol car in a residential street is about as physical as an environment gets.

Which leaves the load-bearing word.

Did CAS infer?

{pause: 1.4}

Yes. And it is worth being slow about why. CAS was not a set of instructions somebody typed out. It was a model fitted to years of recorded crime and population data, and what it produced — the score for this square, this week — was not written down anywhere by a person. It was derived. Nobody could point to the line that set a particular square's score, because there wasn't one. The system worked out how to generate that output from the input it received.

Through the gate. Comfortably.

Now the counter-argument, and I am going to put it in my own voice, because it is my objection and I am not going to lend it somebody else's authority. Here is what I would say to the text. This is a regression over three databases. We have had regressions since the nineteenth century, and calling one of them inference is generous. If the front door of this Act is wide enough to admit a regression, it is wide enough to admit the spreadsheet in every municipal office in Europe.

I do not think that objection has been answered. The Commission's guidelines lean toward keeping simple rule engines out of scope, and beyond that the boundary is genuinely unclear. Nobody serious claims otherwise. What we can say is that CAS sits well inside the line, wherever the line eventually falls, because a fitted statistical model is the easy case and not the hard one.

## Change one fact {tone: curious}

Here is where the gate becomes audible.

Keep the Netherlands. Keep the police. Keep the map, the squares, the weekly briefing. Change one thing: delete the model, and replace it with a rule that a policy officer writes in a document. Send a car to any square that has had three burglaries in the last month.

Same cars, same streets. The same residents, scored the same way and watched the same amount — and for the same reason.

And on the guidance as it stands, the Act does not apply. No inference — a person wrote the rule down, and the machine only counted. The system falls out of the gate entirely, and with it falls every obligation that follows.

{pause: 1.4}

That is the honest shape of what a definitional gate does. Two systems with identical effects on identical people, and the law reaches one and not the other, on the strength of how the output was computed.

Now change a different fact.

Keep CAS exactly as it was — but this time the Dutch police did not build it. They bought it, from a company in California with no office and no representative anywhere in Europe. Californian engineers and Californian servers, scoring Dutch squares.

Does European law reach that company?

{pause: 1.4}

It does. Article 2 of the Act sets out its scope, and I will call that one the reach. The relevant limb, quoting: "providers and deployers of AI systems that have their place of establishment or are located in a third country, where the output produced by the AI system is used in the Union." End of quotation. Third country, in this law's language, means anywhere outside the Union.

Two words in there are doing quiet work. For now, take the rough shape. A provider is whoever puts a system out under their own name. A deployer is whoever uses one under their own authority. The Californian company would be the first. The Dutch police would be the second, and only the second. In the real CAS they were both at once, because they built the thing and then ran it themselves.

But the hook in that limb is the last clause. The output produced by the system is used in the Union. It does not ask where the company is, where the model was trained, or where the servers hum. It asks where the answer lands.

The reach also has holes, and they are written into the Act itself. There are five worth knowing. I am going to give you two, and leave the rest alone, because each one is a hole shaped like an argument and none of them is today's.

The first is the one this episode's own instance walks straight past. A police force scoring squares to get ahead of burglaries is inside this law. The same force doing the same thing for national security is outside it — and so is anything used exclusively for military or defence purposes. The Act says that in terms. Where exactly that line falls is argued over hard, and it is not argued over today.

The second: research, testing and development, before a thing is placed on the market or put into service, is outside the Act. So is anything developed and put into service for the sole purpose of scientific research and development. But the drafters narrowed that hole themselves, in a sentence of their own, and it matters here. Testing in real-world conditions is not covered by the exclusion. So a pilot out on real streets, with real data, before anybody has placed anything on any market — that is back inside.

There are three more holes. All of them are genuine limits on everything I have said today, all of them are argued over, and I am naming the fact of them rather than pretending the reach is total.

## The second gate {tone: pointed}

There is a second door, and the whole series rests on it, so we earn it now.

The Act does not attach duties to *building* something. You can build whatever you like. The duties attach at two moments, and both are moments of handover.

Here is the first, in the Act's own words. Quoting: placing on the market is "the first making available of an AI system or a general-purpose AI model on the Union market". End of quotation.

Which sends you straight to a second definition. Quoting again: making available is "the supply of an AI system or a general-purpose AI model for distribution or use on the Union market in the course of a commercial activity, whether in return for payment or free of charge". End of quotation.

Set aside that phrase "general-purpose AI model" — it is a separate category, and you do not need it today. Strip the rest back and one plain thing is left: you handed the system to somebody else, for money or for nothing.

Now the other door. Quoting: putting into service is "the supply of an AI system for first use directly to the deployer or for own use in the Union for its intended purpose". End of quotation. Which is to say: the thing went into use for the first time, doing the job it was made for. Somebody else's use, or your own.

Notice that last bit — "for own use". That is what catches CAS. The Dutch police were not selling anything. They built it and they ran it themselves, which means nothing was ever placed on any market. And yet the law still finds them, because they put it into service for their own use.

Say it the other way round, because this is the sentence the rest of the series leans on. A system built inside one organisation and never supplied to anybody reaches this Act by a different route than a system that is sold. Different route, different actors, different paperwork. Same law.

So far, then, we have two things. A gate that asks how the output is produced. And a moment — market, or service — at which duties begin. Everything else in this instrument hangs off those two.

## Which level are we standing on {tone: contemplative}

Now I want to do something that will feel like a digression and is not.

Ask why CAS failed and you can answer at four different heights.

Technically, it was a weekly regression over three databases that caught about one incident in fifty. Organisationally, it was a closed box in a command room with no channel to ask it why. Institutionally, it was a decade-long national programme that never defined what success would look like, and never had to justify its own renewal against an outcome.

And in terms of rights, it was geographic scoring. Scoring a square is not a decision about any particular person — not until an officer knocks on a door. That is exactly why it slipped past so many nets designed to catch decisions about people.

Every one of those four answers is true. None of them is more real than the others. Each is a convenient way of describing everything upstream of it. Push the technical answer one level back and you get the organisational one. Push that back and you get the institutional one.

The Act does see those residents, in one place. Its scope reaches, and I quote, "affected persons that are located in the Union". End of quotation. The people in the scored squares are inside this law. But being named in the scope of a law and being given something by it are two different things, and almost every duty that follows runs between providers, deployers and public authorities.

And here is the point I want to land, because it is the load-bearing claim of this episode.

The Act's front door is a question about how the machine works. Not about who the machine affects. The gate is a technical test, and of those four levels, it can see the technical one.

## What the rule assumes about the machine {tone: grave}

Which brings us to the beat this whole series exists for.

Take the gate back apart, and notice what it takes for granted. The definition says the system infers, for explicit or implicit objectives, how to generate its outputs. So it presumes a system that *has* objectives, and whose outputs can be understood as inferences toward them. That presumption runs right through the Act. Later on, the entire question of how heavily a system is regulated turns on something called its intended purpose: the use the provider intends, as stated in the instructions and the sales material. The law asks, over and over, what a system is *for*.

CAS had outputs for ten years. It did not have a measurable objective. That is not my judgment on it — it is the police's own stated reason for switching it off. No clear goals. No measurable success criteria.

{pause: 1.4}

So what does a law that classifies systems by their purpose do with a system whose purpose was never operationalised? It has no test for that. There is no provision anywhere in this Regulation that asks whether anyone ever defined what the thing was supposed to achieve, or whether anyone ever checked. The Act will accept a stated intended purpose and build an entire compliance regime on top of it. It never asks whether that purpose was measurable in the first place.

The gate asks what a system is for. Here, after ten years and a national deployment, the honest answer turned out to be: nothing that could be measured.

## Where this is contested {tone: measured}

Three disagreements, and they are in different states.

The first is the one we already met: does a deterministic system infer? Contested, and open. The Commission's guidelines lean toward excluding simple rule engines, and I have read nobody who thinks the boundary is clear. Expect that to be argued for years.

The second is settled, and I will restate it because it is easy to lose. That February 2025 guidance does not bind anyone. It is the Commission's reading, not the law.

The third is the biggest, and it is genuinely open. Should there be a definitional gate at all? An alternative design exists. Regulate the *use*, regardless of the technique. Score people's homes and you are regulated, whether you did it with a neural network, a regression, or a policy officer with a pen. On that view, the whole of today has been an elaborate exercise in asking the wrong question, because the residents of a hot square do not care how their square got hot.

I am going to keep that one in my own voice, because I cannot hand you somebody who holds it in exactly that form, and I am not going to invent one.

What I can give you is two pieces of recorded unease about the shape of the draft, from before it was finished.

In June 2021, the European Data Protection Board and the European Data Protection Supervisor published a joint opinion on the proposal. They criticised the idea of governing by a positive list of prohibited practices. They argued that the draft's notion of risk to fundamental rights should be aligned with how risk already works under the data protection regulation. And they called for a general ban on biometric identification in publicly accessible spaces. That is not "scrap the gate". It is two European supervisors saying the drafting instinct was wrong in kind.

The second is adjacent, and I want to mark it as adjacent rather than let it pass as the academic version of the first. Michael Veale and Frederik Zuiderveen Borgesius, writing in *Computer Law Review International* in 2021, were looking at the draft rather than the law we ended up with. Their argument is about what the instrument is built out of. The Act takes its structure from four decades of European product-safety law rather than from rights law, and it inherits that machinery's assumptions along with its shape. That was a prediction when they made it. The structure they described is the structure that was adopted.

I do not think the weight of informed opinion has settled on whether a definitional gate was the right architecture. I am not going to manufacture a consensus where there is none. It is live.

## As written, against as enforced {tone: somber}

Now the practical part.

Nobody assessed CAS under the AI Act. Not once.

Partly that is timing, and the timing is worth pinning down, because this law is newer than it sounds. The Act was published in July 2024 and came into force twenty days after that. The definitions and the outright prohibitions started applying in February 2025. The bulk of it waited until August 2026. CAS ran on for about sixteen months after the Act came into force, and stopped before most of the Act had started.

And the heaviest part of it has still not started. The high-risk regime — the tier reserved for systems in a listed set of uses, carrying the whole weight of the Act's obligations — does not apply until the second of December 2027. That is a date, so treat it as contingent. It has already moved once, and it may move again.

But there is something more interesting here than a deadline. It is not obvious that CAS would have reached the high-risk regime at all. The Act's list of high-risk law-enforcement uses is written about natural persons — human beings, as opposed to companies. The risk of a person becoming a victim. The risk of a person offending. The profiling of persons. CAS scored squares. Whether a place-based system reaches that list at all is an unobvious question, and I have not seen it answered.

The deeper point is a different one. The instrument that actually produced public knowledge about CAS was not this Regulation. It was the Dutch government's Algorithm Register: a national, voluntary transparency scheme, sitting entirely outside the Act. CAS has an entry in it. That entry is the reason anybody outside the police can describe how the thing worked, what data it used, and that officers could not see inside it.

A voluntary national register did the work that a binding European regulation had not yet begun to do.

## What is being held back {tone: pointed}

One promise, so that you can hold me to it.

This series ends by asking whether treating artificial intelligence as a product was the right choice in the first place. That is the verdict, and I am not going to give it to you now. You have not seen the machinery yet, and a verdict on machinery you have not seen is an opinion with a soundtrack. Episode 12 lands it.

Local judgments I will make as they arise. That one waits.

## What you now ask {tone: lucid}

So what do you take with you, into a room with a system you have never met?

Ask first whether it infers, or whether it applies rules a person wrote down. That single question decides whether any of European AI law is in the room with you, and you can usually get an answer to it in five minutes from somebody who built the thing.

Ask what its stated objective is — and then ask the harder half. Is there a measurement that would tell you whether it met that objective? If the answer to the first is confident and the answer to the second is silence, you are looking at what the Dutch police looked at for ten years.

Ask where the output goes. Not where the company is, not where the model was trained. Where the answer lands, and who acts on it. That is what the reach is built on, and it is how organisations discover they are inside a law nobody in the building has read.

And ask the question the Dutch police eventually asked themselves, which is the one this episode began and ends on. If this were switched off tomorrow, could anybody say what had been lost?

{pause: 1.4}

The front door of this law is a question about how a machine works. It is not a question about who the machine affects. Everything we build on top of it inherits that choice.

## What comes next {tone: warm}

We now know what this Act counts. We do not know why anybody thought a law could be written in time for a technology moving this fast — or whether that worry is a serious analytic claim or a very convenient argument.

So next time we step away from the instrument. One episode only. Episode 2 asks whether a technology can be regulated at all while it is still moving, and it does not quote a single line of the Act.

Then we come straight back inside the text, in Episode 3, and we find out who you are in this picture. I gave you a rough shape for provider and deployer today — whoever puts the system out under their own name, and whoever uses it under their own authority — and rough is all it was. The Dutch police were both at once. The reason that is possible turns out to matter more than almost anything else in this law.