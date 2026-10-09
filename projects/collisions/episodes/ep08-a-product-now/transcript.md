---
episode: 8
title: A Product Now
defaults: { tone: measured, rate: normal }
---

## Tempe {tone: somber, rate: slow, note: "a real night and a real person; quiet, steady, no theatre"}

Tempe, Arizona. The night of the eighteenth of March, 2018.

A woman named Elaine Herzberg is pushing a bicycle across a road, {pause: 0.5} away from the crosswalk. Coming towards her is a Volvo that has been modified — a test vehicle, running the automated driving system of a ride-hailing company's research unit. There is a person sitting in the driver's seat {pause: 0.4} whose job is to watch the road.

{pause: 0.8}

The car *sees* her.

{pause: 1.0}

{tone: measured} Radar picks her up about six seconds before impact, and the laser scanner follows almost immediately. Six seconds is not a moment. It is long enough to brake, {pause: 0.3} long enough to steer, {pause: 0.3} long enough to do both and still have time left.

What happens inside those six seconds {pause: 0.5} is the reason for this episode.

{tone: lucid, rate: normal} The system cannot classify an object as a pedestrian unless that object is near a crosswalk. She is not near one. So for around five seconds the software keeps changing its mind about what she is. Vehicle. Bicycle. Unknown object. Back again. Repeatedly.

{pause: 1.4}

{tone: pointed, rate: slow} And every time it changes its mind, it throws away the track. {tone: lucid, rate: normal}

{pause: 1.2}

The track is the history — {pause: 0.5} where this thing has been, and therefore where it is about to be. Called a vehicle or a bicycle, the system assumes she is travelling the same way as traffic, in the next lane along. Called an unknown object, it assumes she is standing still. Each new label starts the counting again {pause: 0.4} from nothing.

{tone: precise} Two more facts, and both of them are decisions that a *person* made in an office. The Volvo's own factory emergency braking had been switched off while the test system was running. And the test system was configured to wait one full second {pause: 0.5} before braking hard.

{pause: 0.8}

The investigation was run by the National Transportation Safety Board. The determined probable cause was the failure of the operator in the driver's seat to monitor the driving environment, because she was visually distracted — {pause: 0.4} streaming a television programme on a phone. Among the contributing factors, the Board pointed at the company's inadequate safety culture.

{tone: measured} Hold both halves of that, because the episode lives in the gap between them. {tone: somber, rate: slow} The vehicle saw her for six seconds. {pause: 0.6} The probable cause was the human being.

{pause: 1.4}

{tone: pointed} And nothing malfunctioned. {tone: somber}

{pause: 1.2}

## The disclosure, made once {tone: neutral, note: "candid and plain; a disclosure, not an apology"}

Before anything else, a disclosure, {pause: 0.4} and it is a large one.

This was the United States, in 2018, under American law. No European product liability instrument applied to it, and none could have. The instrument this episode is about reaches only products placed on the market after the ninth of December 2026 — {pause: 0.5} and as this is recorded, that date has not arrived.

{tone: pointed} So everything from this point on is a counterfactual. {tone: neutral}

{pause: 1.2}

I am going to run an American night in 2018 through a European statute that has not yet applied to a single thing. I say that once, plainly, and I will not apologise for it again. The statute is coming. {pause: 0.5} The machines are already here.

## Where we are {tone: lucid}

{tone: warm} This is The Collisions. {tone: lucid}

For seven episodes we have lived inside one instrument, the data protection Regulation, asking what it does when it meets a machine. Today a second instrument walks in, {pause: 0.4} and it is a stranger to everything we have built so far. It was not written about artificial intelligence. It was written about things that injure people.

And the trouble this episode is about is simple to state. {tone: pointed} This instrument judges a product by what it was at a moment. The machines we are talking about do not stay at a moment. {tone: lucid}

{pause: 1.4}

From the earlier series you need one clause and nothing more: {pause: 0.3} that the AI Act governs these systems as products placed on a market. Today's instrument governs what happens after a product placed on a market {pause: 0.4} kills somebody.

{tone: precise} Directive (EU) 2024/2853, the revised Product Liability Directive. {tone: wry} That is the last time I will say the number out loud. From here it is just the Directive. {tone: lucid}

{pause: 0.6}

And two things you probably believe about product liability are going to get in your way, so let me take them off you now.

The first is that it is about things that break. The night in Tempe is why I chose it against that belief — {pause: 0.4} the radar worked, the scanner worked, the classifier returned an answer every single time. {pause: 0.5} Just a different one.

The second is that the definitions article at the front of a statute is a glossary, the boring part you skip. In this instrument the definitions article is where the liability is actually *decided*. Almost every hard question in this episode is answered by a sentence in it.

## What the machine was doing {tone: lucid, note: "an engineer's walk-through, worked out alongside the listener"}

Start with the vehicle as the people who build such vehicles would describe it, {pause: 0.4} before any rule touches it.

It runs a loop, many times a second — five stages, and only one of them matters tonight. Sensors return a picture of the world. Objects in that picture get matched across successive frames, so the thing seen now is understood to be the thing seen a tenth of a second ago. That matching is called the track, and everything downstream — {pause: 0.3} predicting where the object will be, choosing what the car does, actually braking — {pause: 0.3} is built on it. Then round again.

The track is the load-bearing part. A single detection tells you something is there. A track tells you it is moving, and how, and where it will be in two seconds. Braking safely is a decision about the *future*, {pause: 0.4} so it is a decision made out of track history.

{pause: 0.8}

{tone: precise} There is also a boundary around all of it that engineers give a name to: {pause: 0.3} the operational design domain. The set of conditions the system is built to handle. Outside it, the system is not expected to work, and everyone who builds these things knows that the boundary is where the danger lives. {tone: lucid}

And that boundary is where the person in the driver's seat comes in. The safety operator was the designed mitigation for exactly this class of failure — {pause: 0.4} the engineered answer to the question, what happens when the software does not understand what it is looking at. {tone: pointed} That makes the human's role a design question, and it is why an investigation that ends with the operator has not finished describing the design. {tone: lucid}

{pause: 1.4}

{tone: wry} One caution on all of that. The account I just gave is an investigator's account. It is not the company's. When a firm describes what its own system did, {pause: 0.3} you are hearing evidence about the firm.

## The word that had to change {tone: curious, rate: normal}

So. A statute about products. {pause: 0.4} What is a product?

{pause: 1.4}

You will already have an answer, and it is the same answer European law carried for four decades: {pause: 0.3} a physical object. A kettle. A car. A bottle of medicine. {tone: lucid} The instrument the Directive revises was written in 1985, and the Directive still carries that year in its own text, {pause: 0.3} in a provision preserving special liability systems that existed in national law on the thirtieth of July 1985.

For most of the years since, the interesting question was whether code was a thing at all.

The definitions article now answers it. Quoting the Directive:

> "'product' means all movables, even if integrated into, or inter-connected with, another movable or an immovable; it includes electricity, digital manufacturing files, raw materials and software."

Closing the quotation.

{pause: 0.6}

{tone: pointed} Plainly: software is a product. {tone: lucid}

{pause: 1.2}

Not software embedded in a machine. *Software*. On its own, as a movable thing, {pause: 0.3} in the same breath as electricity and raw materials.

That one clause is why this Directive is in a series about artificial intelligence at all.

{pause: 0.8}

{tone: precise} Two neighbouring words come with it, and they do the work the main word cannot.

A **related service**, in the Directive's own words, is a digital service integrated into or inter-connected with a product in such a way that — quoting —

> "its absence would prevent the product from performing one or more of its functions."

Closing the quotation. {tone: lucid} Forget customer support; that is not this. This is the cloud service your device cannot work without. Cut the connection, {pause: 0.4} and the thing on your kitchen counter stops being what you bought.

{tone: precise} Then a **component**, and the Directive gives it one line. Quoting again:

> "'component' means any item, whether tangible or intangible, raw material or related service, that is integrated into, or inter-connected with, a product."

Closing the quotation. {tone: lucid} Say that again with the furniture removed: {pause: 0.4} a component can be something you could never hold in your hand. A model running on somebody else's servers {pause: 0.3} can be a component of a car.

{pause: 1.4}

{tone: curious} Now, a question for you, and take a second on it. The perception software in that Volvo — {pause: 0.4} under these three words, what is it?

{pause: 1.8}

{tone: lucid} It is a product in its own right, because software is a movable. It is also a component of the vehicle, because it is integrated into one. And if part of it ran remotely, on a link the car needs to function, that part is a related service, which is also a component. The same code wears three of the Directive's coats at once, {pause: 0.5} and which coat it is wearing decides who you *sue*.

## Placed, and put into service {tone: precise}

Two more pieces of vocabulary, and these ones are about time {pause: 0.3} rather than things.

**Placing on the market** means the first time a product is made available on the Union market. **Putting into service** catches something else: {pause: 0.3} a thing that never went on sale at all, used commercially in the Union for the first time, having never been made available before that use.

{tone: lucid} The second one exists for exactly our situation. A company builds a system, never sells it to anybody, {pause: 0.4} and drives it on a public road. Nothing was placed on any market. {tone: pointed} But it was put into service, and the Directive counts that moment the same way. {tone: lucid}

{pause: 1.2}

So far, then, we have two things. Software is a product. And a thing you never sold can still have entered the world, in the Directive's sense, {pause: 0.3} the first time you used it commercially.

{pause: 0.8}

## Who this instrument is looking for {tone: measured}

The Directive uses an umbrella word — **economic operator** — and it covers six different roles. {tone: wry} I am not going to read you six roles. Two of them matter tonight. {tone: precise}

The **manufacturer** is the one who develops, manufactures or produces the product. Also, and this catches more people than it looks: {pause: 0.3} anyone who puts their name or trademark on it and so presents themselves as its maker. And also anyone who develops or produces a product for their own use. A firm that builds a driving system and drives it itself {pause: 0.3} is the manufacturer of that system.

The **distributor** sits further down the chain and is treated gently. A distributor becomes liable only where no economic operator established in the Union can be identified, the injured person asks the distributor to name someone upstream, and the distributor fails to do it within one month. {tone: wry} That is the whole of the distributor's exposure: {pause: 0.3} a failure to answer a question. {tone: precise} The same rule can reach the provider of an online platform that lets consumers contract with traders.

Behind all of them, the Directive has a net for the manufacturer who is not in Europe at all: an importer, an authorised representative, and failing both, a fulfilment service provider. Somebody inside the Union has to be reachable.

{tone: warm} And then the person the whole apparatus is for. The **injured person** need not have bought anything. Need not be a customer, a user, a party to any contract. Need not prove that anyone was careless.

{pause: 0.8}

{tone: somber, rate: slow} Elaine Herzberg bought nothing from anybody. {pause: 0.4} She was crossing a road. {tone: measured, rate: normal}

{pause: 1.0}

Set that against the vocabulary of the AI Act for one sentence, and then I will let it go: {pause: 0.3} that instrument divides the world into providers and deployers, and asks who put the system into use. {tone: pointed} This one barely cares who deployed it. It wants to know who made the thing, and who changed it. {tone: measured}

{pause: 1.4}

## Control, and what it does to time {tone: curious, rate: normal}

Which brings us to the hinge of the whole instrument, {pause: 0.4} and it is a phrase most people have never heard.

{pause: 0.6}

{tone: precise, rate: slow} **Manufacturer's control.** {tone: curious, rate: normal}

{pause: 0.8}

You would guess it means ownership. {tone: wry} It does not. {tone: precise} The Directive defines it two ways, and the second one is the one that matters. A product is within the manufacturer's control where the manufacturer performs, authorises or consents to the integration or supply of a component — {pause: 0.3} including software updates or upgrades — {pause: 0.3} or to modification of the product. And, quoting the definitions article:

> "the manufacturer of a product has the ability to supply software updates or upgrades, themselves or via a third party".

Closing the quotation.

{pause: 0.6}

{tone: contemplative, rate: slow} Take that slowly. {tone: pointed} Control is a matter of reach. {tone: lucid, rate: normal}

{pause: 1.2}

If you *can* push an update to a thing, that thing is within your control — {pause: 0.5} even though it is in somebody's driveway, and has been for three years, and you have never touched it since.

For a physical kettle, a manufacturer's involvement ends at the loading dock. For software, the Directive says: {pause: 0.3} your involvement ends when you lose the ability to reach it. Which, for most modern systems, {pause: 0.5} is never.

{pause: 1.0}

{tone: precise} The mirror image is **substantial modification**, and that is more demanding than simply a big update. Where product safety rules already set a threshold for what counts as substantial, that threshold governs. Where they set none, the Directive supplies a two-limb test, and both limbs have to be satisfied: {pause: 0.4} the change must alter the product's original performance, purpose or type in a way the manufacturer's initial risk assessment did not foresee — {pause: 0.4} *and* it must change the nature of the hazard, create a new one, or raise the level of risk.

{tone: lucid} *Both*. A change that surprises the risk assessment but leaves the hazard as it was {pause: 0.3} falls outside. So does a change that raises risk in a way the risk assessment already anticipated.

{pause: 0.8}

{tone: precise} And then the consequence, which is the sharpest sentence in the article on who is liable: {pause: 0.4} any person who substantially modifies a product outside the manufacturer's control, and then makes it available or puts it into service, {pause: 0.3} is considered to be a manufacturer of that product.

{pause: 0.8}

{tone: pointed} Not of the modification. Of the product. {tone: curious}

{pause: 1.4}

## What counts as defective {tone: measured, rate: normal}

Now the test {pause: 0.3} everything turns on.

{tone: lucid} The example you are expecting, in an episode about liability for artificial intelligence recorded in 2026, is a chatbot that told somebody something dangerous. I am not using it, for two reasons. Nothing has been decided on facts like those under this instrument. And a chatbot lets you dodge the hardest question this Directive asks, {pause: 0.4} which is not about the machine at all. Keep the vehicle.

{tone: measured} The article on defectiveness opens like this:

> "A product shall be considered defective where it does not provide the safety that a person is entitled to expect or that is required under Union or national law."

Closing the quotation. Call it the defect test.

{pause: 0.8}

{tone: lucid} Notice what is missing from it. No malfunction. No failure. No departure from specification. A product can perform exactly as designed, exactly as its makers intended, every component doing its job — {pause: 0.6} and be defective, because the safety it provided was not the safety a person was entitled to expect.

{tone: pointed} So defect is a comparison. It sets the machine against an expectation, and the expectation is the half that is not inside the box. {tone: lucid}

{pause: 1.4}

{tone: precise} The article then says all circumstances shall be taken into account, and gives a long list of them. Three are worth having. The presentation and characteristics of the product, including its instructions. Reasonably foreseeable use. And relevant product safety requirements, {pause: 0.3} including safety-relevant cybersecurity requirements.

{tone: lucid} There is a limit written in straight after, and dropping it would be the classic mistake. A product is not defective for the sole reason that a better product, including an update or upgrade, {pause: 0.3} has since come along. The state of the art moving on does not retrospectively condemn what you sold.

{pause: 1.0}

{tone: measured} So: Tempe, run through the defect test. Did that vehicle provide the safety a person was entitled to expect?

{pause: 0.6}

Not the safety a specification promised. {tone: somber, rate: slow} The safety a person — {pause: 0.5} a person pushing a bicycle across a road at night, who had signed nothing and agreed to nothing — {pause: 0.3} was entitled to expect. {tone: contemplative}

{pause: 1.4}

That is a different question from the one the investigators answered, {pause: 0.4} and it does not obviously have the same answer.

## Why they built it this way {tone: contemplative}

Stop and ask why a legislature would write a rule in that shape, {pause: 0.4} because the shape is strange.

{tone: lucid} Strict liability exists for one reason: {pause: 0.3} an injured person cannot investigate a manufacturing process. If the law asked you to prove that somebody was careless, you would have to get inside a factory, or a codebase, or a training pipeline, {pause: 0.4} and you cannot. So a bargain was struck decades ago. {tone: pointed} The law gave up on fault, and kept causation. {tone: lucid}

{pause: 1.2}

You no longer have to show anybody did anything wrong. You do have to show the thing was defective, and that the defect caused your harm.

{pause: 0.8}

The extension to software closes a gap the 1985 rule left gaping — {pause: 0.3} whether code was a movable at all. The provisions about updates answer a specific, modern failure: {pause: 0.3} a product that was safe when sold and unsafe after a patch.

{tone: contemplative} And something was traded away to get all of that. It is the fact this whole series turns on, {pause: 0.5} and it is next.

## The damage list {tone: curious}

Suppose you win. {pause: 0.4} Suppose you establish that a system was defective and that the defect caused your harm.

{tone: precise} The Directive then asks what kind of harm it was. And the answer is a *closed* list. Not a description of compensable loss, not a general principle — {pause: 0.4} a list, of three kinds, and if your harm is not on it {pause: 0.3} you get nothing under this instrument.

Death or personal injury, including medically recognised damage to psychological health. That is the first.

Damage to, or destruction of, property. That is the second, and it arrives with three exclusions carved out of it. I will give you two. Damage to the defective product itself does not count — {pause: 0.3} the thing that broke is not the damage. And property used exclusively for professional purposes does not count.

{tone: curious} The third kind is the one that surprises people: {pause: 0.4} destruction or corruption of data — where the data is not used for professional purposes. {tone: lucid}

Once your harm is on the list, the Directive is reasonably generous. It covers all material losses flowing from that damage, and non-material losses too, so far as national law provides for them.

{pause: 0.8}

But the list is the gate, {pause: 0.5} and look at what stands outside it.

{tone: precise} Pure economic loss. Money you lost that is not attached to a damaged body or a damaged thing. {tone: somber} Consider the man in the German case we spent an episode on — {pause: 0.3} refused a loan on the strength of a score produced by a company he had never dealt with. Suppose the scoring model was defective in every sense this Directive recognises. He has no personal injury, no damaged property, no corrupted household data.

{pause: 0.8}

{tone: grave, rate: slow} He recovers nothing here. {pause: 0.5} Not a reduced amount. {pause: 0.4} Nothing. {tone: somber, rate: normal}

{pause: 1.2}

A wrongly refused loan, a lost job, a cancelled benefit, a person filtered out of a shortlist by a model doing exactly what it was built to do — {pause: 0.5} none of it is on the list.

{tone: measured} The Directive does say, in terms, that it leaves national law on other liability regimes untouched, so the door out of the building is not locked. But the door *this* instrument opens {pause: 0.3} is not the one most people harmed by these systems need.

{pause: 0.8}

That is my judgement, and I want it marked as mine: {pause: 0.5} {tone: pointed} the damage list is where this Directive stops, and it stops precisely where these machines do most of their damage. {tone: measured}

{pause: 1.6}

Hold on to that. It is one of the pieces of evidence this series will need at the end.

## Change one fact {tone: curious}

{tone: precise} Where we are, then. Software is a product. A defect is a gap — {pause: 0.4} between what a thing did, and what a person was entitled to expect of it. And the awkward part, which we are about to test three times: {pause: 0.4} that expectation is fixed to a moment, and the thing it is judged against {pause: 0.3} does not hold still. {tone: curious}

{pause: 0.8}

One question before the first variant, and you can answer this from what we have already done. Of the words I have given you tonight, which single one decides whether a maker is still on the hook {pause: 0.3} years after the thing left the factory?

{pause: 1.8}

*Control*. {pause: 0.5} Hold it there; all three variants run through it.

The way to hear where a rule's edges are is to vary one detail {pause: 0.3} and watch the answer move. Three goes.

**First.** A driving system is sold, and it is fine. Eighteen months later the maker pushes an update over the air, {pause: 0.4} and the update introduces the defect.

The maker's instinct is to reach for the escape in the article on exemptions: the defendant escapes if it proves the defectiveness probably did not exist when the product went out, or came into being afterwards. {tone: wry} Reasonable enough for a kettle. {tone: curious}

{pause: 0.6}

It is *closed* here. {tone: precise} The Directive says that escape is unavailable where the defectiveness is due to software, including updates or upgrades — {pause: 0.4} provided the product was within the manufacturer's control. {tone: lucid} And we know what control means. If you could push the update, {pause: 0.3} the door is shut. Call this one the update trap. {tone: curious}

{pause: 1.0}

**Second.** A company buys a model, fine-tunes it on its own data so that it does something the original risk assessment never contemplated and in a way that raises the risk, {pause: 0.3} then deploys it.

{tone: lucid} That is a substantial modification, made outside the original maker's control. The buyer is now considered a manufacturer of that product — {pause: 0.4} of the whole thing, tuning and all, not merely of the part they touched. {tone: curious}

{pause: 1.0}

**Third, and this is the one that catches people.** The maker does nothing at all. {pause: 0.5} Stops issuing security updates for a system still in service. A known vulnerability is exploited {pause: 0.3} and somebody is hurt.

{tone: lucid} The update trap has four routes into it, and one of them is a *lack* of software updates necessary to maintain safety. An absence. Doing nothing is a route to liability, {pause: 0.4} so long as the thing remained within your control — and, once more, control means you could have reached it.

{pause: 1.0}

Three variants, one pattern. {tone: pointed} In this instrument, shipping is not the end of anything. {tone: curious}

{pause: 1.4}

## Free, open, and inside anyway {tone: curious}

A fourth variant, because you will have thought of it. The software is free and open source. Surely that is outside all this?

{pause: 1.4}

{tone: precise} The scope article says, quoting:

> "This Directive does not apply to free and open-source software that is developed or supplied outside the course of a commercial activity."

Closing the quotation.

{pause: 0.6}

Listen to which words are carrying the weight. Not "free". Not "open-source". *Outside the course of a commercial activity.* {tone: pointed} The licence does not decide it. {tone: lucid}

{pause: 1.2}

Free and open-source software supplied in the course of a commercial activity sits squarely inside the Directive, {pause: 0.4} and a very great deal of it is.

{pause: 0.8}

{tone: warm} And in the same article, one sentence that is this series {pause: 0.3} written into a statute. {tone: precise} The Directive does not affect the applicability of Union law on the protection of personal data, and it names the data protection Regulation specifically. {tone: warm} The later instrument looked at the earlier one and said: {pause: 0.4} I am not replacing you. We both apply. {tone: lucid}

{pause: 0.8}

The AI Act reaches the same vehicle, and reaches it differently — it writes safety requirements for systems of this kind, where this Directive writes no requirements at all, {pause: 0.4} only consequences. So what one instrument demands of a manufacturer becomes, in the other instrument's courtroom, {pause: 0.3} a circumstance the court weighs when deciding whether the safety was what a person was entitled to expect.

## What the rule assumes about the machine {tone: lucid, rate: normal}

We have three explanations of Tempe in play, and they sit on different levels. Naming the level is a habit worth having.

The *technical* explanation: {pause: 0.3} an unstable classifier and a discarded track history.

Push one level back and ask what produced that, and you get the *organisational* explanation: {pause: 0.3} an emergency braking function deliberately switched off — because a system that brakes for phantoms is unusable — and a human being designated to make up the difference.

Push again, and the *economic* explanation is waiting underneath. The cost of a false positive is felt by the operator every single day, in a car that stops for shadows. {tone: somber} The cost of a false negative was felt once. {tone: lucid}

{pause: 1.0}

{tone: measured} The incentives in that asymmetry are not hidden or wicked. They are just arithmetic, {pause: 0.3} and they point one way.

{tone: contemplative} Those three are a chain, not a menu you choose from — {pause: 0.3} each link a compact way of naming everything behind it. And the chain does end somewhere, because the law puts a stop on it. Push all the way back and you arrive at a question the Directive genuinely asks: {pause: 0.4} what a person was entitled to expect. That is where this episode lands, and it lands there now.

{pause: 0.8}

{tone: curious} So. What does this Directive assume about the thing it is judging?

{pause: 1.4}

{tone: precise} Two assumptions, and they are both in the text.

The first is that a product has a *state* at a moment. One of the circumstances the article on defectiveness tells a court to weigh is a moment in time — {pause: 0.3} when the product went out onto the market or into service, or, where the maker keeps control beyond that, when it left their hands. There is a point at which the thing is fixed, and it is against that fixed thing {pause: 0.3} that a judgement gets made.

The second is that safety is something a person can be *entitled to expect*.

{pause: 1.0}

{tone: lucid} Now hear the Directive contradict its own first assumption, {pause: 0.3} in its own words. Among the circumstances a court must weigh, quoting:

> "the effect on the product of any ability to continue to learn or acquire new features after it is placed on the market or put into service."

Closing the quotation.

{pause: 1.4}

{tone: contemplative} The drafters *knew*. They wrote into the operative text that the product may go on learning after it leaves. They named the moving thing. And then they asked a court {pause: 0.4} to judge it against a moment.

{pause: 1.0}

{tone: measured} So here is the claim, and it is the whole episode. {tone: pointed} The Directive knows the machine moves. It says so in its own text. And it has no method for judging a moving thing {pause: 0.3} except to ask what a reasonable person expected of it. {tone: lucid}

{pause: 1.6}

Put that beside the tool we built a couple of episodes back — {pause: 0.3} the difference between a justification and an explanation. {tone: precise} An explanation is addressed to the person something happened to, and earns its keep by making the decision contestable. A justification is addressed to an institution, and shows that things were proper.

{pause: 0.8}

{tone: pointed} "The safety a person is entitled to expect" is a justification standard wearing an explanation's clothes. {tone: lucid}

{pause: 1.4}

It sounds as though it is about you. It is a general expectation, assessed by a court, about a class of product. {tone: contemplative, rate: slow} At no point does it require anyone to say why this system decided that this object was a bicycle, {pause: 0.4} and then not a bicycle, {pause: 0.4} and then nothing at all.

## Where it is contested {tone: curious}

One question before the unsettled parts, and you can answer this one now. A driving system performs exactly to its specification, {pause: 0.4} and kills somebody. Can it be defective?

{pause: 1.8}

{tone: lucid} Yes. Because the test is *expectation*, and a specification is only somebody's account {pause: 0.3} of what they meant to build.

{pause: 1.0}

{tone: measured} Four joints in all of this are not settled, and honesty requires saying which kind of unsettled each one is. {tone: warm} One thing first, though: {pause: 0.3} there is nobody I can name on either side of any of these, because nobody has yet had to take a position on them in front of a judge. {tone: curious}

{pause: 0.6}

Whether a statistical error rate can be a defect at all. Every model of this kind has a rate at which it is wrong; {pause: 0.3} that is what it is for. {tone: wry} If being wrong sometimes is defectiveness, everything is defective. If it is not, nothing is. {tone: curious} Contested, and the text does not resolve it.

{pause: 0.8}

What a person is entitled to expect of a system that is right almost all the time. Say a system gets it right ninety-nine times in a hundred — {pause: 0.3} that figure is mine, for the sake of argument, and no such measurement is in front of us. Is the hundredth case a defect {pause: 0.3} or a known cost?

{pause: 1.4}

Contested. And notice its shape: {pause: 0.4} {tone: pointed} it is a normative question wearing a factual one's clothes. {tone: curious}

{pause: 1.2}

{tone: precise} Whether the state-of-knowledge defence swallows machine learning whole. A defendant escapes if it can prove that nobody could have found the defect — {pause: 0.3} and the yardstick, in the Directive's phrase, is the objective state of scientific and technical knowledge, either when the product went out or across the period it remained within the maker's control. Note both limits: {pause: 0.3} the standard is objective, so what this particular defendant happened to know is beside the point; and for software that window stretches well past the shipping date. The Directive's final chapter carries an article headed "derogation from the development risk defence". I have the heading, not the words, so take it only as a pointer: {pause: 0.3} Member States are given room to depart from that defence. Where some do and some do not, {pause: 0.3} the answer to this question will differ by country.

{pause: 0.8}

{tone: wry} And whether a trained model is a product or a component of one. {pause: 0.4} Still moving.

## Nobody has run this yet {tone: measured, note: "serious and plain, not portentous; this is about the calendar, not a tragedy"}

Now the part that ought to change how you hear everything I have just taught you.

{pause: 0.6}

Nothing has been decided under this Directive. No court anywhere in the Union has applied *this* defect test {pause: 0.3} to anything.

And it is worth being precise about why, because the reason is not the one you would guess. This is not a backlog, and it is not under-enforcement. {tone: precise} The scope article says the Directive applies to products placed on the market or put into service after the ninth of December 2026. Transposition into national law is due on the same day. As this is recorded, on the twentieth of September 2026, {pause: 0.4} that date has not arrived. {tone: measured}

{pause: 1.0}

{tone: contemplative} An instrument whose first eligible product {pause: 0.4} does not yet exist. {tone: measured}

{pause: 1.2}

As for transposition itself: reported in mid-September 2026, three Member States had completed it, with roughly a dozen more advancing draft legislation. {tone: wry} That is practitioner tracking rather than a Commission count, and it moves weekly — {pause: 0.3} so take the date attached to it seriously, and take the number lightly. {tone: measured} The shape is what lasts. Weeks from the deadline, {pause: 0.3} most of the Union had not finished.

{pause: 0.8}

I am spending this observation here, once, for the whole series, so that you can carry it forward: {pause: 0.5} {tone: pointed} everything in this episode is apparatus without practice. {tone: measured}

{pause: 1.4}

The defect test has no case law. The update trap has never been sprung. What I have given you is what the text says, {pause: 0.4} and the text has not yet met a judge.

{pause: 0.8}

{tone: wry} And there is one part of the Directive I have not touched, which you would otherwise assume I had forgotten: {pause: 0.3} the chapter on how long you have to bring a claim, and on who can recover from whom afterwards. Real rules, with real deadlines in them, {pause: 0.3} and they are not in this episode.

## What you now ask {tone: warm}

So what do you take to the next system you meet — {pause: 0.4} a system I have never heard of, in a sector this episode never mentioned?

{pause: 1.4}

{tone: precise} Three questions, and they are transferable.

Is this thing a product, a component, or a related service — {pause: 0.3} and who would say so?

{pause: 1.4}

You now know those are three different ideas rather than three names for one. You know a piece of software can be all three at once, and that which one it is decides who is standing in the defendant's box.

{pause: 0.8}

Who could still supply an update to this, and does that keep them inside?

{pause: 1.4}

Not who owns it. Not who is holding it. Who *could reach it*. That single question converts a sale that happened years ago into a live obligation, {pause: 0.4} and it is the question a firm's lawyers least want asked.

{pause: 0.8}

And the third, which is the one that decides whether any of the rest matters. What damage would this system's failure actually cause — {pause: 0.3} and is that damage on anybody's list?

{pause: 1.4}

Ask it about a hiring tool, a benefits model, a credit model. {tone: contemplative} Then notice how often the honest answer is that the harm those systems cause is real, {pause: 0.3} and severe, {pause: 0.3} and nowhere on the list we walked through tonight. {tone: warm}

{pause: 1.4}

One last thing, and it is the thing the next episode is made of.

Strict liability removes the need to prove that anybody was careless. That is a genuine gift to an injured person, {pause: 0.3} and it was hard won.

{tone: pointed} It does not remove the need to prove that the thing was defective, and that the defect caused the harm. {tone: measured}

{pause: 1.2}

Both of those still sit on the claimant.

{tone: contemplative, rate: slow} And remember what they are being asked to prove it about. A thing the law pictures as finished — {pause: 0.3} a state, a moment, a product as it was when it left — {pause: 0.5} which in fact kept moving after it left, and may still be moving now.

{pause: 1.0}

{tone: somber} For a system that no one can fully explain — a system that saw a woman for six seconds, {pause: 0.3} and changed its mind about her repeatedly, and threw away everything it knew each time — {pause: 0.8} proving that is the whole fight.