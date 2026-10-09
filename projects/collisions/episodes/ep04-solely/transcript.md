---
episode: 4
title: Solely
defaults: { tone: measured, rate: normal }
---

## A man sues the company that did not decide {tone: measured}

A man asks a bank for a loan. The bank says no.

That is the whole of the event, from where he was standing. A German bank, an application, a refusal.

{pause: 1.0}

But the refusal did not begin in the bank. Before anybody there looked at him, a company he had never contacted, never written to, never held an account with, had computed a number about him. The number was a probability — how likely he was to pay a loan back. The bank had bought that number. The bank had used it.

The record calls him OQ. Two letters. The Court does not print the names of private individuals, so two letters is the whole of him in the law reports: a man who wanted money for something we are never told about, and did not get it.

And he did not sue the bank.

{pause: 1.4}

He went after the company that had made the number. A credit reference agency called SCHUFA — a firm that had never met him, never corresponded with him, and had not, on any ordinary use of the word, refused him anything. Its answer to him was the obvious one. We did not decide. We do not lend money. Take it up with your bank.

On the seventh of December 2023, the Court of Justice of the European Union — sitting as a Grand Chamber, the formation it uses for the questions it considers important — told that company it was wrong.

Producing the score, the Court held, is itself an automated decision about an individual, in the sense the Regulation means, where the third party who receives it draws strongly on it in deciding whether to enter into, carry out or end a contract with the person.

{pause: 1.0}

Now, a warning about that sentence, and it matters more than it sounds. Those were my words for the holding, assembled from reports of it. The phrase everyone quotes is *draws strongly on*. I have not read the Court's own operative paragraph in its own language, and I am not going to read you words I have not verified as the Court's. So take that formulation as a faithful report of the test, not as the text of it. That distinction is going to come back later in this episode, from a completely different direction.

What matters now is the shape of what happened. A rule about automated decisions went looking for the decision — and it did not find it where the decision appeared to have been made.

## Where we are {tone: neutral}

This is The Collisions, and this is the fourth episode.

The series takes European instruments written at different times, by different people, about different things, puts them onto the same machine, and asks which rule actually bites, who it binds, and what falls through the seam between them.

You should be carrying three things out of the first three episodes. What makes information personal data, and how unstable that gets when the thing holding it is a trained model. That touching personal data at all requires a lawful basis, and that the word "necessary" does far more work in that test than it looks like it does. And that a short list of categories is not merely regulated but prohibited, with a small number of doors out.

Everything so far has been about the *data*. Whether you may hold it, whether you may use it, what you may use it for.

Today the subject changes. Today is about the *decision* — about what happens at the other end of the pipe, when the processing stops being processing and becomes an outcome that lands on somebody's life.

One article. Four paragraphs. About two hundred words of statute, and I am going to spend the whole episode on it, because almost every word in it is contested and at least one of them is load-bearing in a way you would not guess from reading it.

## The example I am not going to use {tone: wry}

There is an example everybody reaches for here, and I am declining it.

The robot recruiter. The system that reads ten thousand CVs and throws away nine thousand of them without a human ever opening the file. It is a good example. It is vivid, it is modern, and it is what you probably pictured when I said automated decision.

I am using credit scoring instead, for one reason. There is a judgment about credit scoring. There is a named man, a dated refusal, a real company and a Grand Chamber ruling that you can go and read. The recruiter is a thought experiment, and this series does not build on thought experiments when a court has done the work.

There is also a second thing I want to head off, and it is a misreading you will fall into if I do not stop you now.

This article looks exactly like a flowchart. It reads like one. Is this a decision? Was it solely automated? Did it have a serious enough effect? If yes, is one of the exceptions available? If so, here are the safeguards you owe. Question, branch, question, branch, answer.

Every node on that chart is contested. Not one of them is a yes-or-no you can settle by reading. The flowchart shape is real — the article really is built that way — and the crispness is fake. If you leave this episode able to draw the chart but not able to say why each box is an argument, I have taught you the wrong thing.

{pause: 1.2}

## What a credit score actually is {tone: lucid}

Before any rule touches this, the system, described the way the people who build it would describe it.

A credit score takes in a handful of features about a person — mostly two. Whether they have paid things back before, and how long their accounts have been open. There are others, and none of them is the interesting part.

Those features go into a model that was fitted on historical outcomes — on a large population of past borrowers, some of whom paid and some of whom did not.

What comes out is a number on a continuum: an estimated probability that this person will repay. Nobody has been refused anything yet.

And now the part that decides this entire episode.

{pause: 1.0}

The cut-off is somewhere else.

The score is continuous. Somewhere between very likely and very unlikely, there is a line, and on one side of the line you get the loan and on the other you do not. That line lives in the lender's credit policy — not in the model, and not in the scoring company. It is a threshold, written into a document, set by people in a risk department who chose a number because of how much default the bank was willing to absorb this year.

So the thing that determines whether you get the money is a threshold in a policy, applied to a probability made by a stranger.

Does a system like this exist as I have described it? Yes. Straightforwardly, unglamorously, at enormous scale, and for decades — which is my own suggestion for why the first case the Court ever got about automated decisions was about consumer credit and not about anything newer or more interesting.

The machines got to credit first. The law caught up there first too.

## What the text actually says {tone: quoting, rate: slow}

Here is the operative sentence. Article 22, paragraph 1, of the General Data Protection Regulation. I am reading the Regulation's own words, and I will tell you when I stop.

Quote. The data subject shall have the right not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her. End quote.

## The word "right" is a trap {tone: measured}

{pause: 1.4}

In plain terms: if a machine, by itself, makes a call about you that carries real weight, the Regulation says you have a right not to be on the receiving end of that.

From here on I am going to call that **the solely rule**, and I am not going to read you the number again.

Now — the first thing to notice is the word "right", because it is a trap.

An ordinary right is something you exercise. You have the right to object; you object. You have the right of access; you ask. On that reading, the solely rule is an opt-out you have to remember to use, and silence on your part means the machine may go ahead.

That is not how it has been read. The dominant reading, and the direction the Court leans, is that this operates as a *prohibition* with exceptions built in — the controller may not do it in the first place, whether or not you have ever heard of the Regulation. The difference is enormous. On the opt-out reading, the duty is yours, and you cannot discharge a duty about a system you have never been told exists. On the prohibition reading, the duty is theirs, before you appear.

I should be straight with you about the state of that argument. The Court's reasoning leans one way and the Regulation's own choice of the word leans the other, and I cannot put names on the other side of that for you. But if you hold only one reading, hold the prohibition.

## Three conditions, and the one that carries the weight {tone: precise}

Three conditions have to hold before the solely rule bites. There has to be a **decision**. It has to be **based solely on automated processing**. And it has to produce **legal effects, or similarly significantly affect** the person.

Take them in that order, because each one is a place where a company will try to get out.

**Decision.** You probably hear that word as the final answer — the yes, the no, the letter that arrives. On that reading, SCHUFA made no decision at all, and every model vendor on the continent is outside the article, because the vendor supplies an input and someone else supplies the answer. Hold that on one side. We come back to it.

**Solely.** This is the word in the title of this episode, and it is the word that decides whether the article reaches anything at all.

Let me demonstrate the error on something with nothing at stake. A document is translated by software. A person then reads the translation over, signs it, and changes not a single word — because they do not speak the source language and would not know what to change.

Who translated the document?

{pause: 1.4}

You did not hesitate. The software translated it; the person signed it. We have no trouble at all separating the act from the signature when the stakes are zero.

Now put the stakes back. A caseworker with four hundred files a day, a screen showing a score, a policy saying to follow the score, no authority to overrule it and no information about how it was made. When that caseworker clicks accept, has a human decided?

{pause: 1.4}

The answer that has emerged — and I am telling you it has emerged, not that the Regulation says it — is that "solely" is not about whether a person was physically present in the process. It is about whether the involvement was *meaningful*. A person who cannot differ, has nothing to differ on, and has no time to differ in, has not made the decision. They have signed the translation.

I am planting that as a question rather than answering it, because there is a court that looked at an actual human in an actual loop and measured it, and that court belongs to the next episode. You do not need to carry it today.

{pause: 1.0}

One word out of turn, before I get to the third condition. The article says *including profiling*, and that word is not a fourth test to pass — it is one kind of automated processing, named so that nobody could argue it was something else. The Regulation defines it itself, and the definition is much wider than the word.

Quote. Profiling means any form of automated processing of personal data consisting of the use of personal data to evaluate certain personal aspects relating to a natural person. End quote. It then gives examples of what those aspects might be — a person's performance at work, their economic situation, their health — and the list runs on past those three.

Profiling, in the Regulation's sense, is evaluating a personal aspect. The everyday marketing sense of the word is much narrower. If a system estimates something about a person from data about that person, that is profiling, whatever the product is called.

And now the third condition.

**Legal effects, or similarly significantly affects.** This is the threshold, and it is the vaguest thing in the article. A refused loan is comfortably inside it. A refused job, a cancelled insurance policy — inside. A reordered feed, a marginally worse price — argued about, genuinely, with no settled answer. The line between an effect that is significant and an effect that merely feels significant is being drawn case by case, right now, and I am not going to pretend otherwise.

{pause: 1.2}

So far, then, two things. The solely rule reads as a prohibition rather than an opt-out. And it turns on three conditions, every one of which is a place where a defence begins.

## Why a rule about process, and not about outcomes {tone: contemplative}

Step back and ask why this rule, rather than a different one.

There was another road available, and it is the one most people assume the law took. Regulate the *outcome*. Make a rule that says a credit decision must not discriminate, that it must be accurate, that it must be justifiable on its merits — and say nothing whatever about who or what produced it. A person, a model, a coin: the rule would not care, because the rule would be about the answer.

Europe did not do that here. Europe regulated the *process* — who decided, by what means, and what you are entitled to demand afterwards.

There are good reasons. Outcome rules need someone to adjudicate the merits of every decision, which does not scale to millions of loan applications. Process rules can be audited. And a process rule reaches systems nobody has invented yet, which an outcome rule tied to a particular kind of harm does not.

But look hard at what was traded away, because this is the criticism of the solely rule that has never been answered.

{pause: 1.0}

The solely rule is satisfied by adding a human.

Put a person into the loop with genuine authority, and the article stops applying. It has nothing further to say. It does not ask whether the decision was correct. It does not ask whether the model was any good. It does not ask whether the threshold in the risk policy was set at a defensible place. Add a meaningful human, and a badly-built system producing wrong answers is outside the article entirely.

That is my judgment and not the Regulation's, and I will say it plainly: this article is about *how* you were decided about, and it is almost silent on whether the decision was right.

## Working it {tone: measured}

Back to OQ, and let me say the moves out loud as I make them, because the method is half of what I am teaching.

**The issue.** Does the solely rule reach SCHUFA at all, when SCHUFA did not refuse anything?

**The instrument.** The three conditions we just walked. And the argument turns entirely on the first of them — is producing the score a *decision*?

**The defence, and it is a strong one.** We do not decide. We compute. We supply a number to a customer, and our customer, exercising its own commercial judgment, decides what to do with it. If you want the obligations in this article performed, ask the bank. The bank refused the man.

That is not a silly argument. On the ordinary meaning of "decision", it is the better argument.

**The counter.** Follow it through and see where it lands you. If the article reaches only the party that signs the letter, then every duty in it falls on the bank — including the duty to let the man express a point of view, and to contest. Contest *what*, exactly? The bank did not build the model. The bank cannot tell him which of his data mattered, or how, because the bank does not know. The bank bought a number.

So the ordinary reading puts the whole of the article onto the one party structurally incapable of performing it, and puts the party that actually made the thing entirely outside. The article would become a rule about who signs the letter.

**The conclusion.** The Court reached past the bank. Producing the score is itself the automated decision — conditionally. Where the recipient draws strongly on that score in deciding whether to enter into, perform or terminate a contract, the obligations land on the company that made the number.

And I want the limit audible in the same breath, because this is exactly where people drop the qualifier. This is the thing I said would come back. At the start of this episode I separated a faithful report of a holding from the words of the holding. Here is the same move with higher stakes: taking a conditional ruling and hardening it into a flat rule. The holding does not say a score is always a decision. It says it is one where the customer leans on it heavily enough. Take that condition away and you have a rule the judgment did not lay down.

{pause: 1.4}

## Three doors, and there is a toll on each {tone: precise}

Suppose you are inside the rule. There are three ways out, and I am going to give you two of them properly.

The first: the decision is **necessary for entering into, or the performance of, a contract** between the person and the controller. Those are the Regulation's words. And that word "necessary" is the same demanding word we met two episodes ago — not "convenient", not "this is how the industry does it". No less intrusive way of achieving the thing. The burden of showing it sits on the controller, not on you.

The second: **explicit consent** — which raises the obvious question of how freely you consent to anything when the alternative is no mortgage.

The third I am naming and leaving. Union or Member State law may authorise an automated decision, provided that law lays down suitable safeguards. That door is where national welfare systems, tax administrations and a great deal of public-sector automation actually live, it is a large subject, and this episode is not going through it. I am telling you it exists so you do not think I forgot.

Now the toll. Getting through a door does not get you out of the article. On the contract route and the consent route, the controller must put in place suitable measures — and the Regulation specifies a floor. At the least: the right to obtain human intervention on the controller's part, the right to express your point of view, and the right to contest the decision. Call those **the three safeguards**.

Read what that floor is made of. A human. A hearing. A challenge.

Notice what is not in it. Nothing about the decision being correct. Nothing about the model being any good.

{pause: 1.0}

And there is a fourth paragraph, which is a near-prohibition rather than a door. Decisions taken through those exceptions may not be based on the special categories from the last episode — the health data, the ethnic origin, the sexual orientation — unless one of two narrow things applies, explicit consent or substantial public interest, and safeguards are in place on top.

Hold that against what the last episode established, and you will see the difficulty immediately. Nobody has to write down the forbidden category for a model to be using it. A near-prohibition on decisions based on special categories assumes somebody can say what the decision was based on.

## Change one fact {tone: curious}

The boundary of a rule only becomes audible when you move it. So: same case, one detail different.

**First.** The bank puts a human in front of every file. A real person, reviewing, and following the score in ninety-nine cases out of every hundred. Is the decision still based solely on automated processing?

{pause: 1.4}

The answer the law is converging on is that it depends on something you cannot see from the ninety-nine. It depends on whether the hundredth case was possible. A reviewer with the authority, the information and the time to depart from the score, who happens to agree almost always, is a genuine decision-maker with a good model. A reviewer who could not have departed is a signature. The same statistic describes both.

**Second.** The score does not refuse the loan. The score sets the interest rate. The man gets his money — at four points above what his neighbour pays.

Now the first two conditions are untroubled. It is automated, and it is a decision. Everything rests on the third: does a worse price *similarly significantly affect* him? And I genuinely do not know. Over a mortgage's life, four points is a sum of money that changes what kind of life you have. It is also, structurally, a price — and the law has never treated being charged more as the same kind of event as being turned away. That is the live edge of this threshold, and where the pressure is.

**Third, and this one moves the hinge itself.** SCHUFA sells the same score to twelve lenders. One treats it as decisive. Eleven treat it as one factor among many, alongside an interview, a business plan, a relationship going back years.

The company is identical. The model is identical. The number is identical.

And the article reaches it for the first customer and does not reach it for the other eleven — because the test is not about what the scorer does. It is about what the recipient does with what the scorer made. Your obligations under this article depend on someone else's internal practice, which you may not be able to observe.

{pause: 1.2}

## Which level is the answer on {tone: contemplative}

Let me take one step that is about explanation itself rather than about law, and then I will stop.

Ask where this decision was made, and you can answer truthfully at three different heights.

*Technically*, it was a probability produced by a fitted model. *Organisationally*, it was a threshold in a credit policy, applied to that probability — a line set by whoever decided how much default the bank would tolerate this year. *Institutionally*, it was made by a private credit bureau that has become, in practice, a piece of national infrastructure: a firm nobody elected, whose number follows you between banks.

Three heights, all of them true. And not one of the three is anywhere the man could reach.

Here is the move. Each of those levels is a convenient place to stop describing, and none of them is the cause. Say "the model decided" and you have described everything upstream of the model — the training population, the features somebody chose to collect — in one word. Push back one level and ask what produced the threshold, and the answer is a risk appetite. Push again and ask what produced the risk appetite, and you are in the bank's cost of capital.

Do that indefinitely and you reach a place where nobody decided anything and no rule can attach, which is the standard way of being sophisticated about these systems and of being useless about them.

I raise it for one reason. **The organisational level — the threshold in the policy document — is where the decision about OQ actually lives, and no instrument in this series regulates it.** The Regulation governs the processing of his data. The Court reached the maker of the score. Nobody at all has anything to say about the number in the risk policy that turned a probability into a refusal.

## What the rule assumes about the machine {tone: pointed}

Now the beat this series exists for.

The solely rule assumes two things about the world it governs. It assumes a decision has a **moment** — a point in time at which it was made. And it assumes a decision has a **decider** — a party you can name, who made it.

For most of the history of administration, both were true. There was a desk, a person at it, and a date on the file.

A modern stack has neither. A vendor produces a number, months ago, for a population, with no knowledge of you. A policy team sets a cut-off, in a different year, for commercial reasons unconnected to your application. A caseworker works a queue in the order the number put them in — and the ordering has already done most of the work before anyone reads anything. There is no moment. There is a pipeline with your name passing through it.

Faced with that, the Court did the only thing it could with the statute it had. It went looking for the decision — and having failed to find it in the place the decision appeared to have happened, it walked the duty upstream, to whoever made the thing the decision was made out of.

{pause: 1.4}

The law went looking for where the decision actually was, and it found it in a company that had never met the man, and had never said no to him.

That is the claim to carry out of this episode. The Court stretched a word; that much is ordinary. What matters is *why* it had to. The article was drafted for a world with one decider, and it was applied to a world with three, so the Court had to pick one and reach for it.

And you should notice what that leaves standing. It reached the maker of the number. It did not reach the maker of the threshold.

## Where it is contested {tone: neutral}

Three things, and I am going to tell you which is settled, which is contested, and which is still moving.

Whether the solely rule is a prohibition or a right you have to invoke: **contested**, with the weight of opinion and the Court's own reasoning leaning towards prohibition. I would hold the prohibition reading and stay aware that it is a reading.

What "similarly significantly affects" reaches: **contested**, actively, and the pressure points are pricing and advertising. Nobody sensible claims it is settled.

Whether human review at industrial volume can ever be meaningful: **still moving**. The live question is what a reviewer would have needed, and whether they had it. Existence is cheap. And that is a factual question about a workplace, which is a strange thing to find at the centre of a data protection statute, and is also the reason the question is answerable at all.

## What OQ actually got {tone: somber}

And now the part that is easy to skip past, so I am not going to.

The Court answered the question the German court had sent. Producing the score can be the decision. The obligations can land on the scoring agency. It is a significant ruling — it is the first time the Court interpreted this article at all — and it changed the working assumptions of an entire industry.

The route there, and I am giving it in outline because the outline is what matters: a refusal, a complaint to a supervisory authority in the German state of Hesse, proceedings in an administrative court there, and a question sent to Luxembourg. Years. Then a ruling on a point of interpretation, and the case sent back down to the national court to be applied.

What OQ got was a ruling about roles.

Not money. Not the loan. He asked for something, and what he received — after all of it — was an authoritative statement about which of two companies owed him a set of procedural rights.

{pause: 1.4}

As the AI Act stands in September 2026, the same facts would also reach that instrument, and differently: credit scoring sits on its high-risk list, so the same number would pull a conformity assessment out of the company that built it and a use-time duty out of the bank that bought it. It would classify the system, and it would still not pay the man.

Two instruments, one refused loan, no cheque. I am planting that and not arguing it. It comes back at the end of this series, when there is enough evidence on the table to say what it means.

## What you now ask {tone: lucid}

Three questions to take away, and they work on any system, in any sector, whether or not a lawyer is anywhere near it.

**The first.** Who or what actually decided here — the model, the threshold, or the person who followed it? Ask it in that order, and ask it out loud, because organisations have usually never had to answer it. The most common honest response is that the three have never been separated, which is itself the finding.

**The second, and it is the one that does the most work.** Could the human in this process have said no? And did they have what they would have needed in order to say it — the authority, the information, the time? Those are three different questions and a system can pass one and fail the others. A reviewer with authority and no information is a rubber stamp with a job title.

**The third.** If the score-maker is not the decision-maker, who owes the duty? Because somebody does, and the answer will not be obvious, and the party who appears to have decided is frequently the party least able to explain anything.

{pause: 1.2}

Then one more, which is really a test of the other three. Ask what contesting this decision would consist of, concretely, tomorrow morning. Who do you write to. What do they have to look at. What could you possibly say that would change the answer.

Because that is where this episode hands over. The safeguards promise the man a human, a hearing, and a right to contest.

To contest something, you have to be told what it was.

And what you are entitled to be told turns out to be four articles, two courts, and an argument that has been running for nearly a decade about whether the Regulation ever promised you an explanation at all.