---
episode: 1
title: The Gate
defaults: { tone: measured, rate: normal }
---

## The week they stopped running it {tone: somber}

In the middle of December 2025, the Dutch national police stopped running a program called the Criminaliteits Anticipatie Systeem. In English, the Crime Anticipation System. Everyone called it CAS.

Once a week, CAS took the map of a city and cut it into small squares. Each square got a score for the days ahead. The scores came out of the system as two words officers used in ordinary conversation — hotspots, and hot times. Where, and when.

The Nederlandse Politie piloted it from 2015. It went national in 2017. The Netherlands was the first country anywhere to run predictive policing across a whole country, and it ran this one for a decade.

Then they switched it off. The discontinuation was reported in February 2026.

The reason they gave is the part to hold on to. The police said the operational value of the system was unclear. There were no clear goals. There were no measurable success criteria. And in Amsterdam, roughly one incident in fifty was correctly predicted.

Ten years of that.

Those reasons came from the police themselves. Separately, and worth noticing, the Dutch government runs a voluntary register of algorithms used by its public bodies, and CAS has an entry in it.

One more thing, and it matters much later than you would expect. For ten years this was a police system, run by the police, for the police. Keep that somewhere.

## Where we are {tone: measured}

This is The Instrument.

Over this series, we take apart one legal machine: Regulation (EU) 2024/1689, the European Union's Artificial Intelligence Act, as it stands after its 2026 amendment. You need nothing to begin. Every term this series uses, it earns, and this is the episode where the earning starts.

Europe made one decision that shapes everything else you will hear. It chose to regulate artificial intelligence the way it already regulates lifts, toys and medical devices — as a product, placed on a market. Whether that was the right decision is the question this series ends on. Not today.

Today is the front door. Before any rule in this Act touches anything at all, something has to decide whether the Act is even talking about the thing in front of you. That test is the whole of today.

Two assumptions to put down first, because a technically-minded listener arrives carrying both.

The first is that a regulation like this is a bag of rules — a pile of separate obligations you work through and tick off. It is not built that way. The obligations sit downstream of gates, and each gate decides whether the next question gets asked at all.

The second is that it is therefore a decision tree, something you could sit down and implement. It is not that either. The branches are words like "infers" and "autonomy", and nobody has yet said, with authority, where those words stop.

One more. The example you are expecting is a chatbot, and I am declining it. A chatbot walks through today's test so easily that it teaches you nothing about where the test actually is. A police map is a better teacher, because with a police map the answer is arguable.

## What CAS actually did {tone: precise}

Describe the machine before the law touches it.

CAS ran on a weekly cycle. It drew on three sources, all of them depersonalised and anonymised. The first was BVI, the central police crime database — what had been reported, and where. The second was GBA, the municipal population administration. The third was CBS, the national statistics office: the demographics of an area. From those three it produced, for every small square of the city, a risk score for the coming period.

It covered four kinds of crime. Burglary, car theft, bicycle theft, and nuisance.

I am not going to tell you how big a square was. My sources disagree with each other, and they disagree by a wide margin — one of them describes a patch of ground, the other something more like a city block — and I have not been able to check either against the register. So: small. Small enough that a score points a car at a street rather than at a district.

One more property, and it does more work today than anything else. CAS was a closed system. An officer looking at a square that had come up hot could not see which data had made it hot.

The field that studies this has a name for what CAS was: place-based predictive policing. Statistical technique applied to work out likely targets for police attention — places, in this instance, rather than people. Hold on to that distinction. Places, not people. It returns.

## The words that do the work {tone: quoting, rate: slow}

Three pieces of text today, from the same Regulation, and each citation is said once.

Regulation (EU) 2024/1689, Article 1. The Act's words: "The purpose of this Regulation is to improve the functioning of the internal market and promote the uptake of human-centric and trustworthy artificial intelligence, while ensuring a high level of protection of health, safety, fundamental rights enshrined in the Charter." The sentence runs on from there, through democracy, the rule of law, the environment and innovation. End of the Act's words.

Article 3, point 1. The Act's words: "AI system means a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments." The Act's words end there.

Article 2, paragraph 1, point (c). The Act's words: "providers and deployers of AI systems that have their place of establishment or are located in a third country, where the output produced by the AI system is used in the Union." End of the Act's words.

## Reading those three {tone: precise}

Take the first one again. The internal market comes first in that sentence. Protection comes second, in a subordinate clause. Whatever else this instrument turns out to be, it says out of its own mouth what kind of instrument it is.

The second I will call *the gate*, and I will not read the number at you again.

The third I will call *the reach*.

## Who the reach catches {tone: lucid}

That was one limb of seven. The others reach providers — the Act's word for whoever puts a system out under their own name — placing a system on the Union market from anywhere in the world. Deployers, meaning whoever uses the thing under their own authority, established or located in the Union. Importers and distributors. Manufacturers who put their own name on a system inside their product. Authorised representatives of providers from outside the Union. And affected persons located in the Union.

Hear what the deployer limb does. If your organisation is established in the Union and it is using one of these systems, that is sufficient by itself. Nobody has to ask where the output goes.

And hear what the last limb does, which is stranger. The residents of those scored Amsterdam squares are affected persons located in the Union. That is enough to put them inside the scope of this Regulation. It is also very nearly everything this Regulation has to say to them. Being inside the scope of a law and getting something from it are two different conditions, and the distance between them is one of Episode 3's questions.

Whose name is on which role — provider, deployer, importer, distributor — is Episode 3's whole subject, and I am leaving it there.

## Six checkpoints {tone: lucid}

Take the gate as a path, and walk a candidate system along it.

First checkpoint: is the thing machine-based. Second: does it operate with some degree of autonomy — and note the text says *varying* levels, which lets a very low level through. Third, and this one is not a requirement at all, for a reason I will come back to in a moment: it *may* exhibit adaptiveness after deployment. Fourth: it works towards objectives, and those objectives may be explicit or implicit. Fifth: from its input, it *infers* how to generate an output. Sixth: that output can influence a physical or a virtual environment.

Said without the statutory furniture: a machine that works something out for itself, towards some purpose, and produces something that changes the world a little.

Walk almost anything modern along that path and it clears station after station without slowing. Almost everything difficult in this Act's front door is sitting inside one word.

## The word everything hangs on {tone: curious}

Infers.

In ordinary English, to infer is to work something out from evidence. Here it carries far more weight than that. It separates a system that *derives* how to produce its output from a system that is *told* how.

Take it on something with nothing at stake first. A thermostat. It reads a temperature, compares it against a number a person set, and switches the boiler on below that number. Nothing in that behaviour was worked out by the thermostat. A person wrote down the whole relationship, and the machine executes it. Nobody calls that inference.

Now change the thermostat. It watches, for three weeks, when the house fills up in the evening, and it starts heating before anyone arrives — and no person ever told it when they arrive. The relationship between input and output was derived from data rather than written by hand. That is inference on anybody's reading.

Very few of the systems you will actually be asked about sit at either end. Between those two thermostats there is a very wide middle, and that middle is where every argument about this Act's front door happens.

Now the auxiliary verb I promised you. The text says a system *may* exhibit adaptiveness after deployment. May. The Commission published guidelines on this definition in February 2025, and their most-quoted line is a negative one: because the word is "may", adaptiveness is not necessary. A system that never learns another thing after the day it shipped is still an AI system.

That closes the most popular escape route there is. The objection runs: our model is frozen in production, so this cannot be about us. It is about you.

## Why a definition and not a list {tone: contemplative}

There was another road, and it was the one Europe started down.

The Commission's original proposal, of April 2021, defined an AI system by pointing at an annex, and the annex listed families of technique: machine learning approaches, logic- and knowledge-based approaches, statistical approaches. Build your thing out of one of those, and you were inside.

That approach has an obvious virtue. You can read it and know. It also has a fatal one, for a technology on this timetable: a list ages, and a list can be walked around by whoever is willing to call their technique something else.

So the list went, and a functional test replaced it. The gate names no technique at all. It asks what the thing does.

What was traded away to get that is legal certainty, and the trade was not small. Nobody can read the word "infers" off the page and know where it stops. Which is precisely why the Commission had to publish guidelines in the same month the definition took effect — the text alone does not tell you.

You will meet this trade again in almost every episode. A rule drawn tightly enough to be checkable is a rule that ages badly. A rule drawn to survive the technology is a rule nobody can apply with confidence.

## Working CAS through the gate {tone: precise}

Now the method, and the method is half the lesson, so I am going to say the moves out loud as moves.

The issue is whether CAS is an AI system. The instrument is the gate. The test is the six checkpoints. Then the facts, then the strongest thing to be said against, then the conclusion.

Before I walk it — of those six checkpoints, which one do you think is worth arguing about?

{pause: 1.4}

Machine-based: plainly yes. Autonomy: it produced a score for every square, every week, with no person doing that arithmetic — and "varying levels" admits a low level. Objectives: an implicit one counts under this text, and directing patrol effort towards likely crime is an objective whether or not anyone wrote it in a document. Output: the text lists predictions by name, and a prediction is exactly what came out. Influence on a physical environment: a car goes down a particular street.

Which leaves inference, as it almost always does.

Here is the strongest case against. CAS is a description of the past. Burglaries happened, they were counted, the counts were arranged on a map. That is arithmetic and cartography. Nobody calls a bar chart an inference.

And here is why that fails. CAS did not only count. It fitted a statistical model across police records, population administration and area demographics, and produced a number for a week that had not happened yet, for a square where nothing had been reported. The relationship that turns those three databases into that number was derived from data. Nobody sat down and wrote it.

The closed box is consistent with that. There was no written rule to put in front of anyone.

CAS is through the gate.

## Change one fact {tone: pointed}

A definition only becomes real when you find its edge, so let me move one thing at a time and let the answer flip.

First. Delete the model. In its place a policy officer writes a rule, on one line: send a car to any square with three or more burglaries in the last month. Same squares. Same cars.

Same street, same residents, same officer at the door. What has changed?

{pause: 1.4}

Nothing infers anything. A human being wrote down the whole relationship between the data and the output, and that system is arguably outside this Act entirely. Identical effect on identical residents. Different legal universe. If that strikes you as strange, hold the feeling; it is the single best argument against building a law on a definitional gate, and it gets a whole episode of its own.

Second. Put the model back, and change only what comes out of it. Instead of a hot square, the output is a ranked list of named individuals, ordered by how likely each is to offend. Still an AI system — nothing about the gate has moved. But it has now walked into territory the Act may forbid outright, depending on a single word that Episode 5 turns on.

Third. Change nobody's code and nobody's data. Change only the company. The system is built and operated by a vendor in the United States with no establishment in the European Union, scoring Dutch squares for Dutch police. They never hand the system to anyone. They run it, and what crosses the border is the score — so nothing has been made available, and nothing has been placed on any European market. The reach takes them anyway, because the output produced by the system is used in the Union. That is where an American engineering team discovers it is inside a European regulation nobody in the building has read.

## The second gate {tone: precise}

There is a second gate today, and three later episodes lean on it, so it gets earned here.

This Act attaches almost nothing to *building* a system. Read the obligations and they hang off two events instead. Both are defined terms, and both are worth hearing in the Act's own language.

## Two events, in the Act's own words {tone: quoting, rate: slow}

The first event. The Act's words: "placing on the market means the first making available of an AI system or a general-purpose AI model on the Union market." End of the Act's words.

Making available is itself defined. The Act's words: "the supply of an AI system or a general-purpose AI model for distribution or use on the Union market in the course of a commercial activity, whether in return for payment or free of charge." End of the Act's words.

The second event. The Act's words: "putting into service means the supply of an AI system for first use directly to the deployer or for own use in the Union for its intended purpose." End of the Act's words.

## Which door CAS came in by {tone: precise}

Strip the statutory furniture off that pair and you get one sentence. The duty bites at the moment the thing is handed to somebody else, or the moment it is first switched on to do the job it was made for.

Note what is sitting inside the first definition: free of charge. Giving it away is supplying it. And note the phrase at the end of the second: intended purpose, which is itself a defined term, and Episode 4 is where it is unpacked.

Which brings us back to the thing I asked you to hold. A police system, run by the police, for the police.

Which of the two doors did CAS come in by?

{pause: 1.4}

You cannot tell from what I have given you, and neither can I. Whether the force wrote that code itself or a supplier built it for them, I have not been able to confirm, and I am not going to assert it. That gap turns out to be useful, because it is exactly the fact that decides the answer. If a supplier handed the system over, that is a supply — something made available, for use, on a market. If the force built it and switched it on for its own purpose, then there is no market anywhere in this story, and it comes in by the other route entirely: first use, for its own purpose, by the organisation that made it.

Either way it comes in. But the route is not decoration. The route decides which name this Act puts on you, and which duties arrive with the name — and that is Episode 3.

Everything this series says about products rests on that pair of events. Eleven episodes from now, when we ask whether a product was the right thing to regulate, this is the beat the question comes back to.

## Five ways to explain the same decade {tone: contemplative}

Ask why CAS existed for ten years and you can answer at several levels, each of them true.

Technically, it is a weekly statistical model over three databases. Organisationally, it is a closed box in a command room with no channel to ask why. Institutionally, it is a police force running a decade-long programme whose success it never defined. Economically, it is a procurement decision nobody had to defend against an outcome. And in terms of rights, it is a score attached to ground rather than to a person — which is precisely why it slipped so many nets, because scoring a place is not a decision about anybody until an officer acts on it.

Now push back one level, because a level is a convenient place to stop, not a cause.

"Nobody defined success" explains nothing by itself. It summarises something that sits upstream of it. What produced it? A procurement in which no one was ever going to be asked, at renewal, whether the thing worked. And what produced *that*? Say it plainly: no measurement was required of anyone, by anyone, at any point in ten years. Not by the police. And not, as it turns out, by any law.

What to take from all five is this. The gate is a technical test. It asks about autonomy, and inference, and output. Every other level in that list — the closed command room, the undefended procurement, the decade without a measurement — is completely invisible to it.

## What the rule assumes about the machine {tone: pointed}

This is the beat this whole series exists for, so let me be exact.

The gate presumes a particular kind of object. A system with an objective, explicit or implicit, from which its outputs can be read as inferences *towards* that objective. The entire structure of the Act downstream is built on the same presumption: classify the thing by what it is for, and regulate accordingly.

CAS had outputs. It had no objective that could be measured. The police said so themselves when they stopped it. No clear goals. No measurable success criteria.

So the gate asks what a system is for, and here, after ten years and a whole country, the honest answer turned out to be: nothing anybody could check.

{pause: 1.4}

A law that classifies systems by their purpose has no test at all for a system whose purpose was never operationalised. It will read one in — from the documentation, from the sales material, from whatever anybody wrote down at the start. And it will not notice that behind that stated purpose there was nothing.

Where the heavy part of this Act does reach a system, it does demand testing, against metrics and thresholds defined in advance and appropriate to the intended purpose, and it demands that the accuracy achieved be declared. So: test against a metric you chose, and publish the result. Nothing in that asks whether the metric was worth hitting. One in fifty, for ten years, is not the number that regime is built to catch, because a system that meets its declared metric and delivers nothing still passes. Episode 7 takes that requirement apart.

## Where people disagree {tone: measured}

Three joints, and they are in different conditions.

Does a purely deterministic system infer? Contested, and genuinely so. The February 2025 guidelines lean towards excluding simple rule engines. They do not draw a line anyone could apply without argument — and they are not, in the end, the body that decides.

Do those guidelines bind anyone? That one is settled, and the answer is no. They are non-binding. The interpretation that will actually bind comes from courts, years from now, in cases that have not been brought yet.

And the largest question: is a definitional gate the right architecture at all, against the alternative of regulating uses whatever technique produced them? Open. Seriously open. That argument has holders on both sides, and Episode 6 is where they speak, by name, at their strongest. It is not mine to settle today.

## As written, as enforced {tone: neutral}

Nobody ever assessed CAS under this Act.

The reason is dates, and dates in this field move, so take this one with its stamp attached. The heavy regime — and whether a map of squares is even inside that regime is Episode 4's question, not mine — applies from 2 December 2027. It was not always that date, and why it moved is the subject of a later episode. The shape of the problem is permanent; that number is not.

So the public knowledge we have about CAS came out of a voluntary national algorithm register, run by the Dutch government and sitting entirely outside the instrument this series is about, and out of a police force willing to publish its own reason for switching the thing off. None of it came from this Regulation.

I am also leaving something large on the table, and saying so. The reach has holes cut in it, and I have named none of them properly: national security, military and defence; pure scientific research and development; use by a private individual in a personal, non-professional capacity; and systems released under free and open-source licences, which has exceptions of its own. Each of those is a hole shaped exactly like an argument, and each is somebody's route out. They are not today's episode, and I would rather tell you they exist than let you leave thinking the door is solid.

## The verdict, held {tone: measured}

One promise, so that the ending of this series can keep it.

This series will finish by asking whether regulating artificial intelligence as a *product* was the right choice. I am not answering that today, and neither should you, because you have not yet seen the machinery — the tiers, the requirements, the standards, the people who are supposed to check. Judging an instrument you have not been shown is not judgement. Episode 12 lands it, and every episode between here and there leaves a piece of the evidence on the table.

Smaller judgements I will make as they arise. That one waits.

## What you now ask {tone: lucid}

Here is what today gives you. Four questions, to carry to the next system anybody shows you.

Does this thing infer, or does it apply rules a person wrote down? That single question decides whether a whole body of European law is in the room.

What is its stated objective — and is there any measurement that would tell you whether it met it? If nobody can answer the second half, you are looking at CAS again, whatever it is called.

Where does the output land? If your own organisation sits in the Union, being here is already enough on its own. And if it does not — if the company, the staff and the servers never touch the Union — output used here is enough on its own too.

And the last one, which is really the Dutch police's own question, arriving ten years late. If this system were switched off tomorrow, could anyone in the building say what had been lost?

Episode 2 steps away from the instrument, for one episode only, to ask why anyone believed a law could be written in time for a technology moving this fast. Episode 3 comes back inside the text, and we stay there.

## Sources {tone: neutral}

The text quoted today is the consolidated Regulation (EU) 2024/1689 as published on EUR-Lex. The reading of "may exhibit adaptiveness" comes from the European Commission's guidelines on the definition of an AI system, of February 2025. The abandoned list-based definition is in the Commission's own original proposal of April 2021. The operational account of the Crime Anticipation System, and the police's stated reasons for ending it, come from reporting on its discontinuation in February 2026; the Dutch government's algorithm register holds the entry for that system.