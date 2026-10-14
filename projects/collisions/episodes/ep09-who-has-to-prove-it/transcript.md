---
episode: 9
title: Who Has to Prove It
defaults: { tone: measured, rate: normal }
---

<!-- WRITER'S NOTES (not spoken).
1. Length: about 5,200 spoken words, roughly 40 minutes against a 36-minute target. Nothing is padded. I kept the two opening paragraphs of "What the rule assumes about the machine". That beat must not be thinned, and restating the logs-say-what-not-why point there is deliberate, for listeners who lapsed earlier. If a trim is needed, cut those two paragraphs (about 80 words).
2. Blocking recap: fixed using the editor's wording, with one change. "Is the next thing we'll take away" became "we'll take away in a moment", because the first variant removes the human decisions, not the breach presumption.
3. Optional date change taken: "In September 2022" and "That July". The annex and Official Journal dates stay in full.
4. "Which version. Which input. Which output." is kept, as the note allows. -->

## Horizon {tone: measured, note: "A real injustice told plainly; restraint carries the weight"}

This begins in English criminal law, not Union law and not product liability, and I'm borrowing one rule of evidence from it, nothing more.

The Post Office, in England and Wales. Its branches kept their accounts on a computer system called Horizon, supplied by Fujitsu.

When Horizon said a branch ought to be holding more money than it was, {pause: 0.5} the gap had a name.

A shortfall.

{tone: somber} Between 1999 and 2015, the Post Office prosecuted sub-postmasters, the people who ran those branches, on the strength of shortfalls that Horizon reported. For theft, for fraud, for false accounting. {pause: 0.8} Some of them went to prison.

{tone: measured} I'll be careful about how many were prosecuted. The published counts differ, depending on who did the counting and over which years. So I'll use the one word every source supports.

Hundreds.

That care is deliberate. This episode is about a number produced by a machine and treated as settled, and I'd rather not make that mistake in its first minute.

{pause: 1.0}

Now the rule underneath those trials.

A statute of 1984 said that a criminal court in England and Wales could not simply take a computer's word for it. Section 69 of the Police and Criminal Evidence Act required that a document produced by a computer come with proof that the computer had been operating properly, and had not been improperly used. Whoever relied on the record had to show that the machine behind it was sound.

In 1997 the Law Commission, reviewing hearsay in criminal evidence, examined that section. It found, in its own words, that the section served "no useful purpose". It recommended repeal, {pause: 0.4} with nothing in its place. What would remain, on the Law Commission's approach, was a presumption that mechanical instruments were in order at the material time, {pause: 0.3} unless there was evidence to the contrary.

Two years later the section was gone, repealed by the Youth Justice and Criminal Evidence Act 1999.

So a court trying one of those cases began from a position. {tone: pointed} The computer was working, unless somebody showed that it was not. {pause: 1.2} {tone: somber} And the somebody was the accused, {pause: 0.5} arguing against a system that belonged to the accuser and had been built by the accuser's supplier.

{pause: 1.4}

{tone: measured} One more fact, and it is reported rather than read. I have it from accounts of a freedom-of-information response and from commentary, not from a document I have seen. When the Law Commission consulted on removing that requirement, the Post Office responded in favour.

It asked for the rule to go. {pause: 0.8}

There's an easy way to hear that, and I'm going to decline it. The easy version is a story about a villain. The more useful version is about structure. A burden of proof was moved by a reform that looked technical, {pause: 0.4} and the party that stood to gain had supported moving it. {tone: contemplative} A structure like that can fail without anybody in it being wicked. All it needs is one party holding the machine. {tone: measured}

How all of that came to light, and what followed, is a long story of its own, and I'm leaving it to other tellings.

## Where this sits {tone: lucid}

This is The Collisions, and this is the ninth episode of ten.

Last time, the product liability Directive arrived, and two of its ideas matter today. A product is defective when it does not give the safety a person is entitled to expect. And the harm has to be on a short, closed list, {pause: 0.3} or this instrument pays nothing.

That episode ended on a gap. Strict liability takes away the need to prove that anyone was careless. It leaves the claimant proving that the thing was defective, {pause: 0.4} and that the defect caused the harm.

From a few episodes before that, one tool. {tone: precise} An account addressed to an institution, showing that a process was proper, {pause: 0.4} is a justification. An account addressed to a person, good enough that they could argue with it, {pause: 0.4} is an explanation. {tone: lucid} When I handed you that tool, I said a point would come where the law stops asking anybody to explain anything. {pause: 0.5} This is that point.

Today, then: who has to prove it. Horizon shows the burden sitting with the person who cannot see the machine. The Directive pushes it toward the person who can, {pause: 0.3} partly and on conditions.

The whole episode fits in a sentence, and you'll hear it again. {tone: pointed} The law gave up on making the machine explain itself, and decided instead who loses when it stays silent. {pause: 1.4} {tone: lucid}

## The watch, and the ledger {tone: curious}

Start with something you have no stake in.

A witness says they looked at their watch and it read nine o'clock. Nobody asks for proof that the watch was working. If someone has a reason to doubt it, they can raise one. Otherwise the watch is taken to be right. For a watch, that's sensible. It's simple, and when it fails {pause: 0.3} it tends to fail where you can see it.

Now notice what the presumption does next. A judgement made about simple instruments gets stretched to cover anything that counts as an instrument. So an accounting system running across a whole network of branches {pause: 0.5} got the treatment a watch gets.

That's the error, and once you've heard it you'll hear it everywhere. A simple instrument earns a sensible presumption. {tone: pointed} A complex system inherits the same presumption, and nobody notices. {pause: 1.2} {tone: lucid}

So what does the record of a complex system look like? {pause: 0.5} Take a deployed model, meaning a learned system that has been put to work. What follows is the general shape of how such systems are run and kept. It is not a report about any particular firm.

{tone: precise} Broadly, five kinds of record can exist, and two matter most to a court.

The first is the version history: {pause: 0.3} which model was running, with which settings, on the day in question. These systems get updated, so a claim about a model is always a claim about one version of it.

The second is the log of inputs and outputs. What went in, what came out, and when.

The other three I'll leave aside.

{tone: lucid} Now the record that's missing.

{tone: pointed} None of them says why. {pause: 1.2} {tone: lucid}

The log tells you that, on this input, under this version, the system produced that output. It can't tell you the reason, because nothing in the system's running ever wrote one down. What happens inside is arithmetic over an enormous number of fitted values, {pause: 0.4} and arithmetic leaves no reasons behind it.

{pause: 1.0}

Once more, in fewer words. Logs establish what happened, under which version, on which input. They don't establish the reason. {pause: 0.8}

Keep that distinction close. The law's answer to it is procedural, and the rest of this episode follows that answer.

## The burden {tone: measured}

Two articles of the Directive matter today. One is on disclosure of evidence, and one is on the burden of proof. You might expect two separate rules, or a flowchart with a yes or no at each box. Hear them instead as one mechanism, {pause: 0.3} with a judgement at every joint. {tone: warm} It will come together over the next few minutes. {tone: measured}

Begin with the default, the position before anything shifts. The article headed "Burden of proof" opens like this:

> "Member States shall ensure that a claimant is required to prove the defectiveness of the product, the damage suffered and the causal link between that defectiveness and that damage."

Those are the Directive's words. Call that the burden.

You'll probably hear "burden of proof" as the job of convincing the judge. The burden in this article has more structure than that. {tone: precise} It's three separate things. The product was defective. The claimant suffered damage. And the first caused the second. {tone: measured}

Each can fail on its own. Prove a defect and a serious injury, {pause: 0.3} and you can still lose because you can't connect them. Prove the injury and a link to the product, {pause: 0.3} and you can still lose because no defect is shown.

{pause: 1.0}

{tone: pointed} In short: three things to prove, and losing any one loses the case. {pause: 1.2} {tone: measured}

Now notice which of the three are hard from outside the machine. The damage, a claimant can usually show, because it happened to them. Defect and causation are claims about what went on inside. {pause: 0.4} Those are the very things the log never says.

## The disclosure rule {tone: lucid}

The first answer is to make the other side open up.

The article on disclosure covers a claimant who has, in its words,

> "presented facts and evidence sufficient to support the plausibility of the claim for compensation".

End of quotation. If that claimant asks, the defendant can be required to disclose relevant evidence at its disposal.

Call it the disclosure rule.

You may be picturing one side tipping its filing cabinets onto the other side's desk. Set that aside. This rule has a gate in front of it {pause: 0.4} and a fence around it. {pause: 0.8}

{tone: precise} The gate is plausibility. Asking is not enough. You first have to show, from what can be seen outside, {pause: 0.4} that your claim is plausible. That's a lower bar than proof, but it's still a bar.

The fence is proportionality. In the Directive's phrase, disclosure is limited to what is "necessary and proportionate". In deciding that, a court has to weigh the legitimate interests of everyone concerned, third parties included. The text singles out confidential information and trade secrets.

{tone: wry} That brings in the phrase a defendant is likely to reach for first. Trade secret. {tone: lucid}

The Directive borrows its definition of the term from another Union directive. What matters is the job the term does in this article. You'd expect it to work as a reason to refuse. The text gives it a different job. Suppose a defendant must disclose something that is a trade secret, {pause: 0.3} or is said to be one. Then courts are to have the power to take the specific measures needed to keep it confidential while it's used in the proceedings, and afterwards.

So the secret is protected, and the claimant still gets in. The court decides how. {pause: 0.8}

{tone: curious} There is one more power, and on my reading it's the closest this Directive comes to a duty to explain. {tone: lucid} A court can require disclosed evidence to be presented, in the text's words, {pause: 0.3} "in an easily accessible and easily understandable manner". End of quotation. It can do that on a reasoned request from the other side, or where it thinks it appropriate. Either way, the effort has to be proportionate for the party who has to make it.

That makes the evidence readable, which is a real gain. Measured against the tool from earlier in the series, this isn't an explanation. It isn't a justification either. {tone: pointed} It's the record itself, made legible to the court and to the person on the other side, and nobody is asked to say why. {pause: 1.4} {tone: lucid}

## The presumptions {tone: measured}

A disclosure rule on its own is a request with a court's name on it. What gives it force is what happens when the request isn't met.

The burden article goes on to set out circumstances in which, in its words, "the defectiveness of the product shall be presumed". There are three. The first is the sanction that makes the disclosure rule real.

{tone: pointed} If the defendant fails to disclose relevant evidence as the disclosure rule requires, {pause: 0.4} the defect is presumed. {tone: measured}

{pause: 1.4}

Said the short way: {pause: 0.3} disclose, or be presumed defective. {pause: 0.8}

Now the word "presumption". You may bring a softer meaning to it, a court simply taking something for granted. {tone: precise} The Directive's version has a hinge. The fact counts as established unless the other side displaces it. The article says so in terms: the defendant has the right to rebut any of these presumptions. "Presumed" means that it is now the defendant's job to show otherwise.

And the limit, in the same breath. What a refusal presumes is the defect. Only that. It does not presume that the defect caused the injury, {pause: 0.3} and it presumes nothing at all about the damage.

{tone: measured} The second circumstance is where another body of law walks in. The defect is presumed where the claimant shows the product fails "mandatory product safety requirements", to use the text's phrase, in Union or national law. Then comes the qualifier. The requirements have to be, in the text's words, "intended to protect against the risk of the damage suffered". End of quotation. So the rule broken has to be a safety rule {pause: 0.3} aimed at the kind of harm that actually happened. Call that the breach presumption.

The third is what the text calls an "obvious malfunction", during reasonably foreseeable use or ordinary circumstances. It suits things that visibly go wrong. It fits badly with a learned system that gives a confident wrong answer, {pause: 0.4} because nothing about that is obviously a malfunction. {pause: 0.5} The car from last episode never malfunctioned at all.

The causal link then gets a presumption of its own. Suppose the product has been established as defective, and the damage is, quoting, "of a kind typically consistent with the defect in question". Then the link is presumed. It needs the defect first. After that, a defect and a matching kind of harm {pause: 0.3} are allowed to stand in for the chain between them.

## The complexity presumption {tone: lucid, note: "The centre of the episode; unhurried; let each condition land on its own"}

Now the most important paragraph in this episode.

Even after disclosure, a claimant can be stuck. Everything has been handed over, and it says what happened, {pause: 0.4} but not why.

For that situation the article has a paragraph of its own. It opens, in its words,

> "A national court shall presume the defectiveness of the product or the causal link between its defectiveness and the damage, or both".

Then come two conditions, and both must be met.

{tone: precise} The first condition is that the claimant "faces excessive difficulties, in particular due to technical or scientific complexity", in proving the defect or the causal link.

The second is that the claimant "demonstrates that it is likely" that the product is defective, or that the causal link exists.

That's the end of the Directive's words. Call it the complexity presumption. {tone: lucid}

Hear its shape. The verb is "shall". Once a court finds both conditions met, the presumption follows. And the text says it applies despite the disclosure of evidence. {tone: pointed} It's built for the case where everything was handed over and nothing was settled. {pause: 1.2} {tone: precise}

Now its limits. Excessive difficulty is the court's judgement to make. Likelihood is the claimant's to show. That's a lighter word than "prove", but it's still something the claimant has to show. And whatever the court presumes, the defendant can rebut.

{tone: lucid} One more thing, and this reading is mine. The paragraph speaks of technical or scientific complexity in general, {pause: 0.3} with no word about artificial intelligence, and these systems fit that description very well.

{pause: 1.0}

Strip it down. Suppose a system is too complicated for the claimant to prove what went wrong, {pause: 0.3} but they can show it's likely that something did. Then the court presumes it, and the maker has to prove otherwise. {pause: 0.8}

{tone: curious} Now a question, and take a moment with it. A defendant flatly refuses to hand over its logs. What does that refusal, by itself, get the claimant? A presumed defect, a presumed causal link, or both?

{pause: 2.0}

{tone: precise} A presumed defect, and no more. For the causal link the claimant still has work to do. That means the next presumption along: {pause: 0.3} a defect, plus damage of a kind that typically goes with it.

{tone: contemplative} So that's the mechanism, and you can hear now why it isn't a bag of rules. The disclosure rule draws its force from the first presumption. The complexity presumption only operates once disclosure has run. And there's no flowchart in it, because every gate is a *judgement* word: {pause: 0.5} plausible, proportionate, likely.

## Where the layers meet {tone: measured}

The AI Act reaches these facts too, and this time it works for the claimant. It requires providers of high-risk systems to document them, and to build them so that they log what they do, {pause: 0.3} which is exactly the evidence this Directive's disclosure rule can compel.

Follow it through. If the record exists, the disclosure rule can reach it, and refusing to produce it presumes the defect. If the record should exist and doesn't, there's nothing to disclose. But the missing record may itself be a failure to meet a mandatory requirement, {pause: 0.4} which is the breach presumption. Will a court treat a logging duty as a safety requirement aimed at the harm in a given case? {pause: 0.6} Nobody has yet said.

{tone: warm} This is the one place in this series where two instruments read as though they were built to fit together. {tone: pointed} On the text, they do. {pause: 1.0} {tone: warm} It's the best news the series has, and I'd like it on the record at its full weight.

## Why this rule {tone: contemplative}

Why this, and not something else?

The obvious alternative was to require explanation by law. The rule would say that a system whose decisions can't be explained may not be placed on the market. Neither the Directive nor the AI Act keeps an unexplainable system off the market. The Directive leaves the inside of the system as unreadable as it found it. {tone: pointed} What it changes is who loses when it stays that way. {pause: 1.2} {tone: contemplative}

I think that was the right choice, and the reasoning is mine rather than the drafters'. A rule demanding explanations would get explanations: {pause: 0.4} documents written to satisfy the rule. {tone: wry} This series has met enough of those. {tone: contemplative} Putting a price on silence at least makes no pretence that the machine can explain itself.

And it answers a real failure. Horizon is that failure written as a rule. The machine was presumed sound, {pause: 0.3} and the person outside it was left to prove otherwise. For its own kind of claim, the Directive turns that around. The party holding the machine has to open it. And where opening it settles nothing, {pause: 0.4} the doubt can fall on the maker.

What was traded away is the gate. Plausibility has to be reached from outside, before disclosure opens, and for a system like this that will often take an expert. Experts cost money. A person who can't pay for one {pause: 0.3} may never reach the gate.

That gate is where this design will succeed or fail, and nobody yet knows where the courts will set it.

## Working a case {tone: lucid}

Let's work a case. It's assembled, so I'll tell you what it's built from. The design is the one the American investigators described in Tempe, the case that filled the last episode. Its perception system could not classify anything as a pedestrian unless it was near a crosswalk. It kept changing its mind about what it was seeing, and threw away its tracking history each time. And it was set to wait a full second before braking hard.

Everything else is mine. A vehicle placed on the market after the Directive applies. A European city. A pedestrian, struck and injured, who survived.

{tone: precise} The issue: can she carry the burden? The instruments: the burden, the disclosure rule and the presumptions, in that order.

Damage first, because it's easy. Personal injury is on the list.

{tone: lucid} Defect and causation are the hard two. From outside, what does she have? A vehicle driving itself hit her, {pause: 0.4} away from any crossing, at a spot where a person on foot could be seen, and it didn't brake before impact. Those are my facts, and they're the kind someone outside can actually show.

The first gate is plausibility. On those facts a defect claim looks plausible, comfortably so on my reading. So disclosure opens.

She can ask for the two records that matter. One is the version and settings that were running. The other is the logs from that night. She can ask for the design documents too. The defendant will say its perception model is a trade secret. That won't shut her out. The court can order measures to keep the material confidential and still let her expert work with it. And she can ask for the logs in an easily understandable form.

In this case, the record is good. It shows the classification changing, and the track thrown away each time. It also shows two things that people chose and wrote down: {pause: 0.4} the rule about crosswalks, and the one-second wait.

{tone: measured} The defendant's side, at its strongest, runs like this. The system performed to specification, and unstable classification is a known property of every system of its kind. And the collision might have happened anyway.

{tone: lucid} The conclusion, and it's mine. She probably gets there. The defect test asks about the safety a person is entitled to expect. In this case a court can put that question to specific, documented choices. Causation can then follow by presumption. Being struck by a vehicle that had detected you, {pause: 0.3} but never classified you as a person on foot, is damage of a kind typically consistent with that defect.

But notice why it worked. The decisive facts were human decisions, logged and documented. {tone: pointed} The record could answer the question because people had answered it first. {pause: 1.4} {tone: lucid}

## Change one fact {tone: curious}

So far, then, we have three things to prove. And there are four ways the defect can come to be presumed. Two matter most for these machines: {pause: 0.3} a refusal to disclose, and complexity plus likelihood. A third, a breach of the safety rules, we'll take away in a moment.

Now move one detail at a time.

**First.** Take the human decisions out. Same injury, same full disclosure. But this time there is no written rule about crosswalks and no configured delay. One learned model did the perceiving and the deciding. The logs show the pedestrian was detected. They also show that, under this version and on this input, {pause: 0.4} the system didn't brake. Nothing says why. The experts disagree. She can't prove a defect.

{tone: pointed} This is the case the complexity presumption was written for. {pause: 1.2} {tone: lucid} Excessive difficulty, from technical complexity: she has that. Likelihood: on my reading, a system that detected a person and didn't brake gives her a strong case for it. With both, the court shall presume, and the maker has to rebut.

{tone: curious} **Second.** The system complied with every product safety requirement that applied to it. So the breach presumption is gone. And the defendant reaches for an exemption. It isn't liable if it proves the defect, quoting, "is due to compliance of the product with legal requirements". End of quotation.

{tone: precise} Listen to "due to". The defendant has to prove the defect came from the compliance *itself*. That is a great deal more than showing it complied.

{tone: curious} So, a question, and commit to an answer. A system meets every safety requirement that applies to it, and injures someone. Is the maker off the hook, yes or no?

{pause: 2.0}

{tone: precise} Not by that alone. Compliance cost the claimant one route to proving the defect. The maker escapes only by proving the defect came from complying.

{tone: curious} **Third.** No injury at all. A model refused a person something, and left them out of pocket. That's last episode's gap. Purely economic loss isn't on the damage list, so the burden never comes up. {tone: wry} They're in the wrong building.

## The instrument that isn't there {tone: measured, note: "Procedural history read evenly; the weight is institutional and never mournful"}

Where do they go instead? There are two places. One is the ordinary fault law of their own Member State. The other is the data-protection Regulation's compensation right.

Fault first. A fault claim means proving somebody was careless, {pause: 0.3} on top of everything else, and that is exactly what this Directive spares people. There was meant to be an instrument for fault claims too.

{tone: precise} In September 2022, the Commission presented a proposal for a directive on adapting non-contractual civil liability rules to artificial intelligence. It was called the AI Liability Directive. Its job, in outline, was to shift the burden in fault-based claims involving these systems.

On the eleventh of February 2025, it appeared in an annex to the Commission's work programme, {pause: 0.3} among proposals to be withdrawn. The reason given, in the programme's words, was "no foreseeable agreement".

That July, the withdrawal was taken at a meeting of the Commission.

On the sixth of October 2025, notice of the withdrawal was published in the Official Journal.

{pause: 1.0}

{tone: measured} An annex, a meeting, a notice. Three administrative steps across eight months. That description is mine; the dates are the record's. {tone: pointed} And on the record I have, there was no vote at the end of it. {pause: 1.2} {tone: measured}

Nothing in that record replaced it. So what's left for someone harmed by one of these systems? {pause: 0.5} This Directive, where the harm is on its list. National fault law, where it isn't. And one more door.

The data-protection Regulation, quoted once:

> "Any person who has suffered material or non-material damage as a result of an infringement of this Regulation shall have the right to receive compensation from the controller or processor for the damage suffered."

Those are the Regulation's words.

Its reach is wide: {pause: 0.3} material or non-material damage, it says, with no closed list attached. Take the person left out of pocket by a refused application, with nowhere to go under the Directive. They may have somewhere to go under this one, {pause: 0.3} provided their personal data was processed in breach of the Regulation.

And the burden? The Regulation doesn't say in so many words who has to prove the infringement. It does say who has to prove the escape. A controller is exempt only, quoting,

> "if it proves that it is not in any way responsible for the event giving rise to the damage".

End of quotation.

{tone: precise} Here is what that comes to. There has to be a breach, there has to be damage, and there has to be a link between them. The controller gets out only by proving it bore no responsibility of any kind. The limit sits at the front: {pause: 0.3} no infringement of the Regulation, no claim under it.

{tone: measured} So: two live routes built for harms like these, each with a condition the other lacks, and ordinary fault law behind them both. The one meant to ease fault claims was withdrawn.

Did withdrawing it leave a gap, or remove a duplicate? {pause: 0.8} I can't name holders for either side from the sources this programme has. So take these as the two arguments, each at its strongest.

{tone: neutral} The duplicate case says the ground is already covered, by this Directive's presumptions, national fault law and the Regulation's compensation right. Another instrument would only have laid more duties on the same ground.

The gap case says the presumptions only help a claim about a defect, for harm on the list. Everyone else is back on ordinary fault law, which eases nothing. Or they need a data-protection claim, which first needs a breach of a different instrument.

{tone: measured} The only reason on the record is the Commission's, and it was neither of these. It said no agreement was foreseeable. That reads, to me, as a judgement about whether the proposal could pass, {pause: 0.4} and it is silent on whether it was needed.

Whether it was needed is contested, and I'm leaving it there.

## Three levels {tone: curious}

Where we are, then. When the record is silent, the Directive decides who loses. Where the harm falls outside it, a person is left with fault law, or a data-protection claim that needs a breach.

Why do claims like these stall? {pause: 0.6} There's an answer at more than one level. Each answer is true, and each one stops too early.

At the technical level, the log records what, not why. That's true, and it's why the claim needs an expert.

Push one level back. Why does the log hold what it holds? {pause: 0.5} Because somebody decided, years before any incident, {pause: 0.4} what to record and for how long. Organisations write retention policies around their own costs and risks. Those policies decide in advance what a court will one day be able to see.

Push once more. Why does the expert decide the case? {pause: 0.5} Because a court is judging difficulty and likelihood about a system it can't evaluate itself. And the expert costs money that one party has and the other may not. The text sets the threshold at plausibility. {pause: 0.5} In practice, I'd put it at the price of an expert who can get you there.

{tone: contemplative} The chain stops at a principle, and lawyers have a name for it: {pause: 0.5} equality of arms. {tone: pointed} Neither side should be crippled because the other controls what both need in order to argue. {pause: 1.2} {tone: contemplative} On my reading, the disclosure article is that principle written as procedure.

## What the rule assumes about the machine {tone: contemplative, note: "The thesis arrived at; plain and unhurried and never a peroration"}

So what does this Directive assume about the thing it judges? {pause: 0.6}

{tone: precise} It assumes there is evidence. Somewhere a record exists which, once produced, lets a court decide. {tone: contemplative} For a kettle, that's true. For the car in the worked case it was true, because people had made decisions and written them down.

For a learned system, the record may establish everything {pause: 0.4} except the thing in dispute. {tone: precise} Which version. Which input. Which output. {pause: 0.6} Never why. {tone: contemplative}

{pause: 1.4}

The complexity presumption reads, to me, like the drafters knowing that. In it, the Directive admits that the record may settle nothing, {pause: 0.3} and decides in advance who carries the cost.

{tone: lucid} So, the claim a third time. In liability, the law gave up on making the machine explain itself, and priced the silence instead. Disclose, or be presumed defective. And suppose what you disclose is too complex to settle anything, {pause: 0.3} and the claimant shows the defect is likely. The court shall presume it anyway.

{tone: contemplative} Set that against the tool from earlier in the series. Every disclosure duty we've met, we've tested by asking who the account is addressed to. This mechanism asks only for the record, and for no account of either kind. Then it decides who carries the record's silence.

{pause: 0.8}

{tone: pointed} The law stopped asking for reasons. {pause: 0.6} It started allocating the cost of not having them. {pause: 1.6} {tone: contemplative}

## Where it is contested {tone: measured}

Besides the withdrawal, two joints in this aren't settled, and they're unsettled in different ways.

The first is whether national courts will actually use the complexity presumption, {pause: 0.3} or read "excessive" narrowly. That one is still moving. This is a directive, so each Member State writes it into its own law, by the ninth of December 2026. Its courts will then read it in their own traditions. Expect it to differ by country.

The second is whether disclosure can reach training data. That one is contested. The text reaches relevant evidence "at the defendant's disposal", to use its phrase. If the model was bought from another company, {pause: 0.4} its training data may not be at this defendant's disposal at all. And where it is, it's full of other people's interests, which the court must weigh.

## As written, as enforced {tone: neutral}

On practice, one fact will do. No court has yet awarded damages under this Directive, and none can yet. The Directive reaches only products placed on the market or put into service after the ninth of December 2026. As this is recorded, that date is still ahead.

And notice who will be missing when the first case comes. No regulator is a party. It will be decided between two parties and a court, with an expert or two. {pause: 0.5} And it can only ever work with what was recorded.

## What you now ask {tone: warm}

So what do you take to the next system you meet, perhaps in a sector this episode never mentioned? {pause: 0.6}

Three questions.

{tone: precise} First, who has the evidence here, and what happens to them if they don't produce it? {pause: 1.6} If the answer to the second half is "nothing", the first half doesn't matter.

Second, what would this person have to show, from outside, before a court would even order disclosure? {pause: 1.6} That's the gate, and asking it tells you who will ever get through.

And third, what in this system is logged, for how long, and who decided? {pause: 1.6} That decision was made long before anyone was harmed, and it decides what any court will ever see.

{pause: 1.4}

{tone: contemplative} Horizon began from a presumption that the machine was right, {pause: 0.3} and left the person outside it to prove otherwise. This Directive, at its sharpest, starts somewhere else. {tone: pointed} Whoever holds the machine and keeps it silent pays for the silence. {pause: 1.4} {tone: warm}

We have now laid every layer this series set out to lay: {pause: 0.3} an instrument about data, an instrument about products, and an instrument about injury. One question has been held since the first episode, and it's the only one left.

Episode 10.