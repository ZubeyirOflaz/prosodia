---
episode: 1
title: "The Gate"
defaults: { tone: measured, rate: normal }
---

## A system switched off {tone: measured}
In the middle of December 2025, the Dutch national police switched off a computer program.

It had been running since 2015 — a pilot first, then nationwide from 2017. The Netherlands was the first country in the world to put predictive policing to work across a whole country. The program was called the Criminaliteits Anticipatie Systeem. The Crime Anticipation System. Every week it took the map of a city, cut into small squares, and gave each square a score for the week ahead. Burglary. Car theft. Bicycle theft. Nuisance. The scores came back to officers as two words they used every day: hotspots, and hot times.

The published descriptions disagree about how big one of those squares was, so I am not going to give you a number.

The shutdown was reported in February 2026. And the reason the police gave is the reason this episode exists. Not that a court had struck it down. Not that anyone had sued. They stopped it because they could not say whether it worked. There were no clear goals. There were no measurable success criteria. In Amsterdam, on their own account, roughly one incident in fifty was correctly predicted.

Ten years. {pause: 1.2}

Nobody had written down what it was for.

## Where we are {tone: lucid}
This is *The Instrument*: twelve episodes on the European Union's Artificial Intelligence Act — Regulation E U twenty twenty-four, sixteen eighty-nine.

Europe made a particular choice about how to regulate artificial intelligence. It could have been built outward from fundamental-rights law, and for a while it looked as though it might be. What Europe built instead is product law. An AI system is a **product**, placed on a market, the way a lift is placed on a market, or a toy, or a medical device. The whole series builds that instrument from the bottom to see what it can do. Whether that choice was the right one is the question the series ends on, and I will come back to that before we finish today.

You need nothing to start. Every term after this one is earned inside the series.

Today is the first question the Act asks of anything at all. Is this an AI system?

You are probably expecting me to answer that with a chatbot. I am not going to. A chatbot is an easy case and easy cases teach you nothing about a boundary. A weekly map of a Dutch city is a hard case, and it is hard in a useful direction: it is dull, it is old, it is statistics, and it is exactly the kind of thing an organisation deploys without ever once asking itself the question this Act now asks.

## The system, on its own terms {tone: precise}
So — before any rule touches it — what did this thing actually do?

A weekly cycle. Three sources of data went in. The central police crime database. The municipal population administration. And demographic data from the national statistics office. The police describe those inputs as depersonalised and anonymised. Out of them came a score per square, per crime type, for the coming period.

I am going to call this place-based predictive policing — my working description, not a term of art I am handing you on anyone's authority. Statistical technique applied to work out where police attention should go. Places, in this family of systems, rather than people. That distinction is going to do an enormous amount of work in a minute.

And one more operational fact, which the Dutch police themselves recorded. It was a closed system. An officer looking at a hot square could not see which data had driven that particular prediction.

Hold that one next to a distinction worth having early. An **explanation** tells you why a thing happened. A **justification** tells you why it was right. A closed system gives you neither — it gives you an output and a request that you act on it. Whatever else is true of this Act, notice that the machine here could not be argued with, because there was nothing in it to argue against.

## What the text actually says {tone: quoting, rate: slow}
Now the words themselves. I will read them once, and then never again.

Article 3, point 1. Quote:

"'AI system' means a machine-based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments." End of quote.

From here on I will call that **the gate**.

And now the other question, because you cannot ask what is covered without asking who is covered. Article 2 sets out who the Act applies to, limb by limb, and three of those limbs do the work today. The first catches providers who place a system on the Union market, or put one into service here — and it says in terms that it makes no difference whether the provider sits inside the Union or in a third country. The second catches deployers whose place of establishment is in the Union, or who are located here. Those two are the baseline, and between them they take in nearly everything you will meet. The third limb closes the gap where neither of those is true, and that one is worth the Act's own words. Article 2, paragraph 1, point (c). The Act applies to, quote, "providers and deployers of AI systems that have their place of establishment or are located in a third country, where the output produced by the AI system is used in the Union." End of quote.

Call the three of them together **the reach**. In everyday terms: build it here, or use it here, or send what it produces here — and the Union claims you.

## In plain words {tone: lucid}
The gate, said normally: something built by machine, that works with some independence from a human, that has some goal — whether or not anyone wrote the goal down — and that works out, from what it is given, how to produce something that changes the world. Predictions count. Recommendations count. Content counts.

The load-bearing word is *infers*. Everything turns on it and the Act does not define it.

So let me test it on something with nothing at stake. A thermostat. It reads a temperature, compares it to a number you set, and switches a boiler. Does it infer?

{pause: 1.6}

No. Nothing was worked out. The relationship between input and output was written down in advance by a person, completely, and the device executes it. Inference, in the sense the gate means, is when the system derives the rule from the data rather than receiving the rule from a human. That is the distinction. It is also — I want to be honest about this now rather than at the end — much blurrier in practice than that sentence makes it sound.

Two things you might already be assuming about this Act, both wrong, and both the natural assumption for anyone with technical training.

The first is that it is a bag of independent rules you can look up one at a time. Wrong shape entirely. What you have is a sequence of gates, and each one decides which of the following ones you ever reach.

The second is that it is a decision tree — feed in your system, read off your obligations. That fails for a different reason. At nearly every junction the Act asks a question that requires a judgement, and the judgement is yours, made in advance, and defensible later to someone who may disagree.

## Why this rule and not another {tone: curious}
There was an obvious alternative, and the Commission tried it first.

In the original proposal — the document numbered COM twenty twenty-one, two hundred and six final, published in Brussels on the twenty-first of April 2021 — an AI system was defined by reference to a list. An annex enumerating techniques and approaches: machine learning, logic- and knowledge-based approaches, statistical methods. If your system used one of the listed things, you were in.

A list has one enormous virtue. You can read it and know.

And one fatal defect. A list ages, and worse, a list can be walked around. Rename the technique, restructure the pipeline, and the annex no longer describes you — while the system does exactly what it did before. A functional definition built on inference names no technique at all, so there is no name to change.

What was traded away for that was legal certainty, and it was a real trade, not a free one. Nobody can read the word "infers" off the page and know where it stops. Which is why, in February 2025, the Commission had to publish guidelines on the definition of an AI system.

The most quoted thing in those guidelines is a negative. Because the text says a system "*may* exhibit adaptiveness" — may, not shall — adaptiveness is not a requirement. A system that is trained once, shipped, and never learns another thing is still an AI system. That matters here more than anywhere, because a weekly statistical model refreshed on new crime data is precisely the sort of unglamorous machinery people assume is too old-fashioned to be caught.

## Working the gate {tone: precise}
So let us actually do it, out loud, the way the analysis is really done.

The question is whether the Crime Anticipation System is an AI system within the meaning of the gate. The test has five joints, and all of them have to hold.

Machine-based. Plainly yes.

Varying levels of autonomy. It produced a weekly map without a human recomputing it. Yes — and note the standard is *varying levels*, which is a low bar by design.

For explicit or implicit objectives. Here it gets interesting, and I am going to come back to it, so park it. Say for now: implicitly, to predict where crime will occur.

Infers from input how to generate outputs. The model's weights came from historical data, not from a policy officer's judgement about what a burglary neighbourhood looks like. That is inference.

Outputs that influence physical environments. A patrol car goes somewhere. Yes.

Now the counter-argument, at its strongest. Someone could say: this is regression. Arithmetic over three databases, of a kind a criminologist could have done with a calculator in 1985, and calling it artificial intelligence is a category error driven by the word in the statute's title.

That objection is real, and it is not a defence. The gate does not ask whether a thing is impressive. It asks whether the relationship between input and output was derived or declared. In this system it was derived.

Conclusion: through the gate. Not close to the line, but not far from it either — and where the line runs is genuinely unsettled, which we will come to.

## Change one fact {tone: pointed}
The fastest way to feel a boundary is to move one thing and watch the answer flip.

**One.** Delete the model. Instead, a policy officer at headquarters writes down a rule: send a car to any square with three or more burglaries in the last month. Same map. Same squares. Same cars, same streets, same residents, same effect on the same people.

Is that an AI system?

{pause: 1.6}

Almost certainly not. Nothing was inferred — a human declared the rule and the computer applied it. Which means the whole of this Regulation, every obligation in it, is switched off by replacing a statistical model with a policy officer who produces the identical outcome. The harm is untouched. The law is absent.

**Two.** Keep the model, change the output. Instead of scoring squares, it ranks named individuals by their likelihood of committing a burglary. Still through the gate, obviously. But now it is in different territory altogether — the prohibitions in Article 5 — and that is Episode 5's material, not mine.

**Three.** Keep everything, move the builder. The system is used in the Netherlands, on Dutch squares, by the Dutch police — but it was built and is run by an American company with no establishment in Europe. Who does the Act catch?

Both of them, by different limbs, and the difference is worth hearing. The police are a deployer located in the Union, so the second limb has them, and nobody has to think about where the vendor sits. The vendor, supplying that system for use here, is a provider placing it on the Union market — the first limb, which says in terms that an American establishment is irrelevant. And if the vendor arranged matters so that it never handed over the system at all, keeping the model on servers in California and sending Amsterdam nothing but the weekly scores, then the third limb closes behind it anyway, because the output is used in the Union. Three limbs, three different jobs.

## What the reach does not cover {tone: neutral}
I am now going to name several holes and walk past them, because each one is a hole shaped like an argument and none of them fits in this episode.

Article 2 excludes systems used exclusively for military, defence or national security purposes, whoever is operating them. It excludes systems developed and put into service for the sole purpose of scientific research and development. It excludes people using AI in a purely personal, non-professional activity. And it excludes systems released under free and open-source licences — unless they are high-risk, or fall under the prohibitions, or under the transparency duties. High-risk, there, is a defined class: a list of uses the Act names, and products it already regulates. It is a classification, not a verdict on how dangerous your system feels. Episode 4 builds it.

Run back over those exclusions and you will notice that a determined organisation could spend a career living in them. I am naming them, not exploring them. That is a cut, and I would rather tell you I made it.

One thing in Article 2 I will not walk past. Its final limb extends the Act to — the Act's own phrase — "affected persons that are located in the Union." End of the phrase. So the residents of those scored squares are in the instrument; the scope article puts them there in terms. What the rest of the instrument hands them is thinner than you would expect. There is a route to complain to an authority. There is, in narrow circumstances, a right to ask for an explanation. Whether that adds up to anything a person can use is Episode 11's question, and that is where you find out how thin.

## Levels {tone: contemplative}
Ask why this system ended the way it did, and you can answer at several different heights.

Technically: a weekly regression over three databases, with poor predictive performance.

Organisationally: a closed box in a command room, with no channel through which anyone could ask why.

Institutionally: a police force that ran a decade-long national programme without ever defining what success would look like.

Each of those is true, and each is a description rather than a cause. Push on the institutional one. A force does not define success for a programme because nothing in its environment required it to — which is an economic fact about procurement, about a purchase nobody had to justify against an outcome. Push once more and you are at politics: a visible response to burglary that someone could point at.

I am going to stop there, because the point is made. One height remains, and it is the one that matters most today. The rights-based answer says something very specific: geographic scoring is not a decision about a person until an officer acts on it. That is exactly why this system slipped so many nets for so long.

And the gate — the test we just ran — sees one of those heights. The technical one.

## What the gate assumes about the machine {tone: pointed}
Which brings me back to the joint I parked.

The gate presumes a system that has objectives — explicit or implicit — and whose outputs can be read as inferences *toward* those objectives. That presumption runs through the whole Act. Its risk tiers are built on intended purpose. Its documentation duties describe what a system is for. Its human oversight provisions assume a human who knows what the system is trying to achieve.

So. What was the Crime Anticipation System for?

{pause: 1.8}

The Dutch police answered that question themselves, after ten years, when they turned it off. There were no clear goals. There were no measurable success criteria. There was an output, produced weekly, consumed daily, acted on by officers in cars — and no statement anywhere of what it was supposed to achieve, and no measurement that could have told anyone whether it had.

A law that classifies systems by their intended purpose has no test for a system whose purpose was never operationalised. The gate would still have let it through — implicit objectives are enough to be caught. But the entire apparatus downstream of the gate is built to hold a provider to an account of what their system is for, and here the honest account, after a decade of national deployment, was: nothing that anyone could measure.

{tone: grave} A test that asks only what the machine does has no way to see a failure that size.

## Where this is contested {tone: measured}
Three disagreements, and they are not of the same kind.

Whether a deterministic rule engine infers. **Contested.** The Commission's guidance leans toward excluding simple rule systems, and nobody who works on this believes the boundary is clear. The honest position is that the line is unsettled and more guidance than that may not be possible.

Whether those February 2025 guidelines bind anyone. **Settled, and the answer is no.** They are non-binding. They tell you what the Commission thinks. The interpretation that will actually bind comes from courts, years from now, on facts nobody has yet.

And whether a definitional gate is the right architecture at all — as against regulating uses, whatever technique produces them. **Genuinely open**, and I can put names to it. Michael Veale and Frederik Zuiderveen Borgesius, writing in *Computer Law Review International* in 2021, made the diagnosis bluntly. They were writing about the proposal — the same document with the list in its annex, from April of that year — not about the Act that eventually passed, and that matters. Their charge was that the thing takes its structure from four decades of European product-safety law rather than from rights law, and inherits that machinery's assumptions along with it. Begin from the risk to fundamental rights, and you would not have built this.

That instinct had institutional backing while the proposal was live. In June 2021 the European Data Protection Board and the European Data Protection Supervisor issued a joint opinion on it. Their target was a different article from today's — they went at the prohibitions, at the method of writing down a positive list of banned practices, and they argued the analysis should start from risk to fundamental rights, aligned with data-protection law. I will not stretch them further than that; they were not attacking the gate. But the family resemblance is mine to point out: a distrust of any method that enumerates first and asks about harm second.

Against all of that stands the choice the Union actually made, and it has a real argument behind it. One definition, one entry point, twenty-seven member states, and something a company can be told in a sentence. Which side is right is the subject of Episode 6, and I am not settling it here.

## As written, as enforced {tone: measured}
Now the gap that this series will keep returning to.

Nobody assessed the Crime Anticipation System under the AI Act. Not once, in the whole of its life.

Partly that is timing, and timing here needs its date attached, because this instrument is younger than it sounds and has already been amended. The Act was adopted in 2024 and amended in 2026, by Regulation E U twenty twenty-six, seventeen forty-four, in force from the twenty-seventh of July 2026. That amendment pushed the heavy regime — the one for stand-alone high-risk systems — out to the second of December 2027. The system was switched off two years before that regime arrives.

But I am not going to tell you it would have been caught by it when it did. Whether a weekly score attached to a map square, rather than to a named person, falls inside any of the Act's high-risk categories is itself unsettled — the listed law-enforcement cases are written around assessing a natural person. A grid square is not a natural person. That question belongs to Episode 4, and I am leaving it there.

The prohibitions had been in force since February 2025, for the last ten months of the system's life. None of them reaches a map of squares.

So what actually produced public knowledge about this system — its three data sources, its closed architecture, the fact that an officer could not see inside a prediction?

A voluntary national algorithm register. The Dutch government's own: a transparency instrument sitting entirely outside this Regulation, that nobody was compelled to file with, and the reason you and I can discuss any of this. The one-in-fifty figure did not come from there. That came from the police, when they explained why they were stopping.

## The second gate {tone: precise}
One more thing before I let you go, and it is the concept the rest of the series rests on.

The Act does not attach duties to *building* a system. I will say that again, because a technically-minded listener will not believe it the first time. Building is not the trigger.

Two things are. **Placing on the market**, and **putting into service**. Here are the Act's own words for each, and then I will translate.

Placing on the market, at Article 3, point 9, means, quote: "the first making available of an AI system or a general-purpose AI model on the Union market." End of quote.

Making available is itself defined, one point further on. At point 10, quote: "the supply of an AI system or a general-purpose AI model for distribution or use on the Union market in the course of a commercial activity, whether in return for payment or free of charge." End of quote.

And putting into service, at point 11, quote: "the supply of an AI system for first use directly to the deployer or for own use in the Union for its intended purpose." End of quote.

That phrase you have now heard three times — general-purpose AI model — is the Act's name for a model general enough to perform a wide range of distinct tasks competently, whichever downstream system it ends up inside. It has a chapter to itself and an episode to itself, which is Episode 9.

Strip the lawyer's clothing off the rest. The duty bites at the moment the thing is handed to someone else, or first used for the purpose it was made for.

And notice what the second one does. "Or for own use." An organisation that builds a system, never sells it, never gives it to anybody, and simply runs it on its own premises still reaches the Act — not by selling, but by using. Which is why the Dutch police, in this story, would be both things at once: the deployer, because they used it under their own authority, and the provider, because they had it built and put it into service themselves. That doubling is not an edge case. For public-sector AI it is the normal shape, and it is Episode 3's entire subject.

## What I am holding back {tone: contemplative}
So here is the promise, made now so it can be kept later.

Everything you have heard today follows from one decision: that an AI system is a thing placed on a market. The gate is a product definition. The reach is a market's reach. Placing on the market is a product-safety concept borrowed, almost without alteration, from four decades of European law about physical goods.

Whether that was the right choice is this series' one real verdict, and I am not going to give it to you now, because you have not seen the machinery yet and a verdict on machinery you have not seen is a slogan. Episode 12 lands it. Every episode between here and there puts one piece of the evidence in front of you.

## What you now ask {tone: lucid}
Take four questions out of this episode. They are worth more to you than the wording, and they work on any system you are ever handed.

Does this thing infer — or does it apply rules that a person wrote down? That single question decides whether an entire body of European law applies to you, and the two cases can produce identical behaviour on the street.

What is its stated objective, and is there a measurement that would tell you whether it met it? If there is no such measurement, you are looking at a system that cannot be evaluated — and an instrument that classifies by purpose has nothing to take hold of.

Whose output is used where? Where the output lands is a different question from where the company is registered, or where the servers sit.

And the last one, which is the Dutch police's own question, asked ten years late. If this system were switched off tomorrow, could anyone say what was lost?

Next time we step away from the text for one episode — the only one for a while — to ask why anybody believed a law could be written in time for a technology that moves like this one. We are back inside the instrument in Episode 3.

## Sources {tone: neutral}
Four things stand behind this episode.

The Regulation itself — Regulation E U twenty twenty-four, sixteen eighty-nine, Articles 2 and 3, in the consolidated text on EUR-Lex, as amended in 2026.

The European Commission's guidelines on the definition of an AI system, published in February 2025.

The Dutch government's Algorithm Register, which is the public record of the Crime Anticipation System and a remarkable document in its own right. The entry number is eight one two two, eight nine two two.

And the reporting, in February 2026, of that system's discontinuation, from which the police's own account of why comes.