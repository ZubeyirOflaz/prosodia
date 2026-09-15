---
episode: 10
title: Does It Travel
defaults: { tone: measured, rate: normal }
---

## Two counts {tone: measured}

In August 2022, two researchers at the Centre for the Governance of AI put a paper on the arXiv preprint server. Charlotte Siegmann and Markus Anderljung. Their title was a question about reach — whether European regulation would shape the global market in artificial intelligence. Their answer was a qualified yes. Not for the whole regime. For parts of it, and especially for large American technology companies running the kinds of systems Europe was about to call high-risk.

Two and a half years later, in April 2025, Anda Bologa published a short piece at the Center for European Policy Analysis in Washington. The title was — quote — "Burying the Brussels Effect? AI Act Inspires Few Copycats" — end quote. The method was counting. Which other legislatures had actually written a law that looked like this one? Canada and Brazil had drafts. Both were stuck. And that was close to the whole list.

So: the same object, two careful teams, opposite answers.

{pause: 1.2}

Except that one of them was counting laws, and the other was predicting what companies would do. That difference is the whole of today, and I will come back to it more than once.

## Where we are, and what today is not {tone: lucid}

This is The Instrument, a series about the European Union's Artificial Intelligence Act — what it is built out of, what it can see, and whether anybody can enforce it.

Today there is no statute in the episode. No article numbers. No quotations from the text, and nothing new to learn about how the Act classifies anything. This is one of the episodes that hands you a tool rather than a rule: machinery for judging the thing, rather than more of the thing.

And here is the boundary, because it would be easy to mistake this for a different episode. I am not going to survey other countries' AI laws. I am not going to tell you what Washington or Beijing or Ottawa has decided. The question is narrower and, I think, more useful: does a European rule change behaviour outside Europe — and if it does, through what?

That second half is what most of the argument is about.

## The name for the thing {tone: lucid}

The framework has a name and an author. Anu Bradford, professor at Columbia Law School, published *The Brussels Effect: How the European Union Rules the World* with Oxford University Press in 2020. The phrase was already in circulation. The book is where the mechanism gets taken apart.

And it is two mechanisms, not one. This is the distinction everything else in this episode hangs from, so I am going to say it slowly.

The first is the **de facto** effect. A company finds that running one worldwide product is cheaper than running two, so it applies the strictest rule everywhere, including in countries that never asked for it. No foreign government does anything at all. The law of one market becomes the design of a global product because that was the cheaper engineering choice.

The second is the **de jure** effect. A foreign legislature reads the European rule and passes something like it. A parliament acts. A statute appears.

One runs through companies. The other runs through parliaments. They can happen together, and on Bradford's account they often do — in an order. Once the multinationals have already adapted their global operations, they acquire an interest in having the same rule at home, because a rule everyone must follow removes the disadvantage of being the one who followed it first. The firm that complied becomes a lobbyist for compliance.

{pause: 1.4}

Two mechanisms. Companies, or parliaments. Hold on to that and the rest of this will stay in focus.

## What it looks like when it actually happens {tone: measured}

The de facto mechanism has a problem that the de jure one does not. A statute is a document; you can count it. A company quietly deciding to build one product instead of two leaves almost no trace, and when it does leave a trace, you usually have to infer the reason from the conduct.

So the strongest evidence is a case where the firm explained itself in public.

May 2018. The General Data Protection Regulation was days from applying. Julie Brill, corporate vice-president and deputy general counsel at Microsoft, wrote on the company's own blog that Microsoft would — quote — "extend the rights that are at the heart of GDPR to all of our consumer customers worldwide" — end quote. The right to know what is collected, to correct it, to delete it, to take it somewhere else. And the reasoning, in the same post — quote — "As an EU regulation, GDPR creates important new rights specifically for individuals in the European Union. But we believe GDPR establishes important principles that are relevant globally" — end quote.

That September, Microsoft said the tools were being used by millions of people, including about two million in the United States — a country the European regulation does not reach. Take that figure as what it is: the company's own number, reported by the company, about its own product.

Now a question, and I mean it as a real one.

{pause: 1.4}

Which of the two mechanisms was that? {pause: 1.4}

De facto. No American legislature passed anything. A European rule reached about two million Americans through a decision taken in Redmond, for reasons the firm described as partly principle and which were also, obviously, cheaper than maintaining two versions of a consumer privacy stack.

That is the mechanism working. Dated, named, first-party, with evidence that somebody outside Europe actually used the thing.

## The condition that decides our case {tone: pointed}

Bradford does not claim this happens whenever Europe writes a strict rule. She sets out five conditions, and they are cumulative — all five, or the effect breaks. I am going to give you two of them and leave the other three, because two are enough to see the shape.

The first is the one everybody already assumes is the whole story: market size. Europe has to be big enough that no serious firm can simply decline to sell there. Fine. That one is not in dispute.

The condition that decides the Act's case is the last one, and it is called **non-divisibility**. Can the company separate the European version from everything else, cheaply?

A phone has one port. That is the cleanest illustration available, and it is worth a moment. A European directive required USB-C on phones sold in the Union from the end of December 2024, and Apple shipped USB-C on the iPhone 15 worldwide in September 2023. Be careful with that one: Apple never said the European rule was its reason, there were independent technical reasons to make the change, and the directive governs what is sold in Europe and nothing else. So that is a picture of the shape, rather than proof of intent. When the product physically cannot be divided, the strictest rule wins everywhere by default, and nobody has to decide anything.

Now ask it of a model.

Can a provider serve a model differently in different places? Different guardrails, different refusals, different documentation, a different set of features switched on for a European address? Not costlessly — but at a cost that looks nothing like running two factories and two supply chains.

{pause: 1.2}

If AI systems are more divisible than physical goods, then Bradford's own framework predicts a *weaker* Brussels effect here than for chemicals, or cars, or privacy. That conclusion is reached using her conditions, not against them. It is the most interesting thing her book does to this statute.

And it reframes the question people usually ask. Strictness alone decides nothing. What decides it is whether the firm can cheaply ship two versions — and if it can, European strictness produces a European product, not a global one.

## Back to the two counts {tone: lucid}

So far we have two things. A mechanism that splits in two — companies, or parliaments. And a condition, divisibility, that bears hard on the first half.

Which lets me pick the opening disagreement back up.

Bologa counted statutes. That is the de jure mechanism, measured directly and honestly, and the count came back close to empty. Canada and Brazil, both stalled in legislative limbo. Peru is the interesting one — two AI laws echoing the European template, with seventeen more bills behind them, and her own caveat attached: not the oversight capacity to make any of it bite. Date-stamp that count to April 2025. Counts of this kind move.

Siegmann and Anderljung were doing something else. They were predicting firm behaviour — the de facto mechanism — and they hedged in their own text, saying parts of the regime rather than the whole of it.

{pause: 1.2}

Two research teams measuring different mechanisms is not two research teams disagreeing. Reading them as a head-to-head is the easy, wrong version of this episode, and it is the version you will meet most often.

What does it cost to take each one seriously? Take Siegmann and Anderljung seriously and you stop watching foreign parliaments altogether. You start watching procurement documents and model cards, because their prediction is that documentation and evaluation practices spread even where no statute follows. Take Bologa seriously and the Act is a regional rule with compliance spillovers at its edges — real, but not a global standard, and never destined to become one.

Those are different things to go and look for. Neither is disproved by the other.

## The inversion {tone: measured}

There is a third reading, and it turns the whole claim over.

An article in the *German Law Journal*, titled "The Brussels Side-Effect: How the AI Act Can Reduce the Global Reach of EU Policy", makes the argument that strictness can produce withdrawal. Instead of one global product built to the European standard, you get a product shipped everywhere except Europe. The feature launches everywhere else and the European launch is "coming later". Sometimes it never arrives.

Notice that this is the divisibility argument again, read from the other end. If you can separate the European version, you can also subtract it.

And here is what adopting it would cost you, practically. You would have to count absences instead of presences — the model capability not offered here, the feature held back, the launch that quietly skipped a continent. Nobody keeps that register. It is a claim about a shape of evidence that essentially does not get collected, which does not make it wrong, and does make it very hard to test.

## The reframe {tone: contemplative}

The fourth position says the whole framing is aimed at the wrong institution.

An article in *Internet Policy Review*, "Brussels effect or experimentalism? The EU AI Act and global standard-setting", argues that what is actually happening is not export at all. It is iterative co-development, through standards bodies — and standards bodies are already international. Europe is not broadcasting a rule outward. Europe and everyone else are working out a technical specification together, in committees that were never national to begin with.

I should say plainly that this is the position the standards material in this series most supports. You have already heard where the high-risk regime's engine sits: a system gets its presumption of conformity from a harmonised standard, and as of June 2026 not one of the deliverables from the relevant European technical committee had been cited in the Official Journal, so the presumption had nothing under it. The substance of the regime lives in specification documents. The people writing those documents sit in international rooms.

If that is right, the influence does not run through the statute at all. It runs through a document nobody voted on, in both directions at once, and counting copycat laws would tell you almost nothing.

## The best objection I know {tone: pointed}

The divisibility argument is the one I find most persuasive, so it should take the hardest hit before I go anywhere near a conclusion.

Privacy is divisible too.

{pause: 1.2}

Microsoft could have built two regimes. Europeans get the deletion right; everyone else gets what they had before. That is a perfectly buildable system, and other companies built exactly it. Microsoft chose not to, and said so in public.

Which tells you that "technically separable" does not predict "actually separated". Engineering cost is not the only cost. Two products means two policies, two internal audits, two answers when a journalist asks which version you are on, and a permanent argument inside the company about who gets which. Firms unify for reasons that have nothing to do with whether unifying was strictly necessary.

So the divisibility argument tells you what is possible. It does not tell you what firms will do. That is a real weakness, it applies to my own preferred reading, and I do not have an answer that settles it.

## One more, and this one is mine {tone: measured}

There is a criticism of the frame itself that I want to put to you, marked clearly: no source in my research holds it, nobody is quoted saying it, and you should treat it as my framing rather than a position in the literature.

The phrase "Brussels effect" slides compliance into authority. A firm that obeys because obeying is cheaper than not obeying is not treating the rule as legitimate; it is doing arithmetic. And a frame built around Europe ruling the world carries a quiet assumption that the European settlement is the one that ought to spread.

The useful residue of that thought is a question. When you see a company comply, ask whether that signals the rule is authoritative, or only that it is cheaper to obey than to litigate. Those look identical from outside and they are not the same fact.

## Where this stands {tone: measured}

The weight does not lean here, and I am not going to manufacture a side.

What I can do is tell you the mechanism to watch for, because the honest finding of this episode is a gap. Every documented case of the de facto effect that I can point to is privacy or hardware. A data-protection regulation. A charging port. Not one of them is artificial intelligence.

So: the mechanism is well evidenced. Its application to this statute is a prediction.

{pause: 1.4}

And that means the thing that would settle it has a describable shape. It looks like the Microsoft instance. A named firm, naming a specific obligation from this Act, as its stated reason for a change made worldwide — followed by evidence that the change actually took effect somewhere Europe cannot reach. One of those would move the argument more than another year of counting foreign bills.

Nobody has one yet. If you see one, you will know what you are looking at.

## What you now ask {tone: lucid}

Three questions to carry out of this, and they work on any regime, not only this one.

First: is the product divisible? Can they ship a different version here — and what would it actually cost them not to? That single question does more work than any estimate of how strict the rule is.

Second: where is the influence running? Through the statute, or through a standard that no legislature voted on? Those produce very different kinds of convergence, and only one of them shows up in a count of laws.

Third, when somebody does copy: are they copying the structure, or only the vocabulary? A law that uses the words "high-risk" and "conformity assessment" without a body capable of assessing anything is a translation exercise. Peru, on Bologa's own account, is the case that makes that distinction matter.

## Handover {tone: pointed}

Every version of the argument you just heard depends on something at the far end being enforceable.

The Act claims reach. You met the scope rule in the first episode of this series: a provider outside the Union, whose system's output is used inside it, is covered. That is a claim about jurisdiction. Whether it is a claim that can be made to stick against a company with no European establishment, no European assets and no intention of paying — that is not a question a lens can answer.

So the next episode goes back inside the text, to the part of the Act that decides it. Who is watching. What they are allowed to do. And what, so far, they have actually done.