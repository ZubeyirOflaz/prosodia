# Casework — voice candidates  ·  researched 2026-10-09

The `casework` persona has a delivery specification but **has never had a voice of its own**. Its four
craft dossiers say so explicitly: Fisher's was built from captions ("Not obtained: Audio"), Harford's
voice "is not separable from production", Sapolsky's register is "Unverified", and Hildebrandt is a
written source. The series have been rendered with the Political Thinkers narrator clip. This file is
the search for the persona's own voice: people whose **voice and delivery** fit what the persona asks
for, as starting points for listening.

**The choice is expensive to change.** Every series reuses one reference clip (the series roadmap's
practical notes: it is "the primary defence against timbre drift"), and hours of rendering will rest on
it. So listen widely, then audition the finalists through the actual pipeline before committing (see the
end of this file).

---

## ⚠ Read first — permission, and why it depends on who will hear it

**The casework series are for the user's own listening only — never shared, commercially or free**
(user, 2026-10-09). If one is ever shared, the **transcripts** are shared and others render them in a
voice of their own; the audio stays private. On that basis, the main obstacles to using a real
person's voice largely fall away:

- **GDPR:** processing "by a natural person in the course of a purely personal or household activity"
  is outside the Regulation (Art. 2(2)(c)). The Court of Justice limits that to activity not published
  to an indefinite audience (*Lindqvist*, C-101/01) — which private listening is not.
- **AI Act:** the deep-fake disclosure duty in Art. 50(4) does not reach this use. Art. 2(10): the
  Regulation "does not apply to obligations of deployers who are natural persons using AI systems in
  the course of a purely personal non-professional activity."
- **Personality rights** (in Germany the general right of personality, which covers one's voice) are
  infringed by use that reaches others — publication, commercial exploitation, misattribution. Private
  listening does not realistically produce that.
- `CLAUDE.md`'s rule is narrower than first stated here: it requires **bundled or preset** voices to be
  license-clear — voices shipped with the open-source project. A private clip that never enters the
  repository is not bundled.

**What still applies:**

- **Copyright in the source recording.** A voice is not copyrightable, but the broadcast or audiobook a
  clip is cut from is. A private copy from a lawful source is generally allowed (in Germany, § 53 UrhG),
  but **not by circumventing copy protection** (§ 95a UrhG) — so cut the clip from a freely available
  broadcast, podcast or talk rather than by stripping DRM from a purchased audiobook. Platform terms of
  service may separately forbid downloading.
- **It has to stay private.** The repository is on GitHub; every `*.wav` and `*.mp3`, `inbox/` and
  `outbox/` are already gitignored and none is tracked, so a clip or render cannot be committed by
  accident. Syncing between one's own machines is still private use.

**For any series whose audio might be shared, this warning stands in full.** The exemptions above end
the moment audio reaches someone else, and the voice is expensive to change: everything rendered in it
would need the person's permission or a full re-render. Decide who will hear a series' audio **before**
choosing its voice; if it might be anyone but the author, use a licensable voice (section F) or ask the
person at the start. This is a documented rule, not a code check (user's choice, 2026-10-09) — `CLAUDE.md`
tells the agent to raise it.

⚠ *General information about EU and German law, not legal advice.*

**Routes to a voice that can be shared later:**
1. **Ask the person** — academics and broadcasters sometimes agree for a non-commercial project.
2. **Commission a narrator with that profile** under a written licence that explicitly covers voice
   cloning (section F lists narrators of exactly this kind of book).
3. **Record someone you know** reading in that style — ten clean seconds is enough for Chatterbox.

---

## What to listen for

Derived from the persona (`voice_profiles.yaml`: "precise and engaged, never theatrical"; `tone.md`), how
the user listens — **headphones, on public transport** — and what Chatterbox does and does not copy:

1. **Depth is welcome.** With headphones a low voice is no disadvantage, and the user often prefers one
   (2026-10-09). What still matters is **articulation**: consonants that stay distinct with a train in the
   background. *(An earlier version of this list leaned against very deep voices on in-car loudspeaker
   research; that does not apply to headphones and nobody was excluded on that basis.)*
2. **An explainer, not an orator or a newsreader.** The persona works an argument out *with* the
   listener. Listen for thinking-aloud phrasing, not declamation.
3. **Two registers in one voice.** Series C needs gravity when a right is actually lost, and a dry, wry
   reset between dense stretches. A voice that can only do one will flatten one of them.
4. **Natural emphasis on the load-bearing word** — the persona's `pointed` tone amplifies whatever
   contour the voice already has.
5. **Long-listening comfort:** no heavy vocal fry, sharp sibilance or sing-song. Imagine 40 minutes of it.
6. **Accent carries over.** Chatterbox's own guidance warns that output inherits the reference clip's
   accent. Choose the accent you want for **all four series**, and listen to how the person handles
   European names (*Vyriausioji tarnybinės etikos komisija*, *Gerechtshof Amsterdam*).
7. **Pace does NOT matter.** Tested 2026-10-09: a slower reference clip does not slow Chatterbox, and the
   renderer applies 0.9× to every episode anyway. Do not rule anyone out for speaking fast, or in for
   speaking slowly.

Recording quality does not matter at this stage either (user's note): find the person first, then look
for clean audio.

**About the links.** 🎧 marks something you can play. Podcast-app pages (Apple Podcasts, Amazon Music,
Listen Notes) play episodes in the browser and work outside the UK; **BBC Sounds / bbc.co.uk pages may be
UK-only**, so where a BBC programme is also a podcast the podcast feed is given. **Audible pages play a
sample** from the play button on the cover. Links were found by search on 2026-10-09 and not each opened.

---

## Start here — a shortlist of ten

Chosen on **evidence of doing this persona's job** — explaining law or social science to a lay audience
in audio, at length — and spread across accents and voices so one listening session covers the range.
⚠ The compiler cannot hear: this ranks the job, not the timbre. Only listening settles it.

|     | who                                   | why this persona                                                                                                                                                                                                                     | 🎧 listen                                                                                                                                                                                                                          |
| --- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | **Joshua Rozenberg** · English        | Forty years explaining law to radio listeners: BBC legal correspondent 1985–2000; launched *Law in Action* in 1984, presented it again from 2010 to its farewell edition in March 2024. The only journalist made KC (honoris causa). | [*Law in Action* archive](https://www.listennotes.com/podcasts/law-in-action-bbc-radio-4-Jqy3swMj0vo/) (podcast feed; episodes to March 2024 are his)                                                                              |
| 2   | **Laurie Taylor** · English           | Former Professor of Sociology at York who **trained and worked as an actor first**; has presented *Thinking Allowed* (BBC Radio 4, social-science research) since 1998.                                                              | [*Thinking Allowed*](https://podcasts.apple.com/gb/podcast/thinking-allowed/id261548752)                                                                                                                                           |
| 3   | **Brenda Hale (Lady Hale)** · English | Former President of the UK Supreme Court; **narrates her own memoir** *Spider Woman*.                                                                                                                                                | [*Spider Woman* sample](https://www.audible.com/pd/Spider-Woman-Audiobook/1473590795) · [SOAS lecture, *Life in the Supreme Court*](https://www.youtube.com/watch?v=u3BR54O8ph4)                                                   |
| 4   | **David Runciman** · English          | Cambridge political theorist turned podcaster: *Talking Politics* (2016–22), now *Past Present Future* — analytic, conversational, long-form.                                                                                        | [*Past Present Future*](https://podcasts.apple.com/us/podcast/past-present-future/id1682047968)                                                                                                                                    |
| *5  | **Bryan Stevenson** · American        | Lawyer; his reading of *Just Mercy* is described as "pleasant, deep, and rich" with "clean diction", and "the pauses matter as much as the words" — the gravity Series C needs.                                                      | [TED, *We need to talk about an injustice*](https://www.ted.com/talks/bryan_stevenson_we_need_to_talk_about_an_injustice) · [*Just Mercy* sample](https://www.audible.com/pd/Just-Mercy-Movie-Tie-In-Edition-Audiobook/B00O4FH8E8) |
| 6   | **Helen Thompson** · English          | Cambridge Professor of Political Economy; *Talking Politics*, now *These Times* — historical, explanatory.                                                                                                                           | [*These Times*](https://podcasts.apple.com/nz/podcast/these-times/id1685475850)                                                                                                                                                    |
| 7   | **Jamie Susskind** · English          | Barrister writing on technology and democracy — the persona's subject — and **reads his own** *The Digital Republic*.                                                                                                                | [*The Digital Republic* sample](https://soundcloud.com/bloomsburypublishing/the-digital-republic-by-jamie-susskind)                                                                                                                |
| 8   | **Michael Sandel** · American         | Political philosopher; *The Public Philosopher* (BBC Radio 4) and the 2009 Reith Lectures — Socratic reasoning about rights and limits, close to how proportionality is taught.                                                      | [*The Public Philosopher*](https://podcasts.apple.com/us/podcast/the-public-philosopher/id514253822)                                                                                                                               |
| 9   | **Philippe Sands** · English          | International lawyer and barrister; presented BBC Radio 4's *Intrigue: The Ratline* and shares narration of his books — legal history told through named people, the persona's method.                                               | [*Intrigue* feed (*The Ratline* series)](https://music.amazon.com/podcasts/3e6c9cda-8d3c-4fdf-8376-a9c5938dea38/intrigue) · [*East West Street* sample](https://www.audible.com/pd/East-West-Street-Audiobook/B01FRDISZI)          |
| 10  | **Michael Ignatieff** · Canadian      | Political philosopher and broadcaster; the 2000 CBC Massey Lectures were *The Rights Revolution* — Series C's subject, as radio lectures.                                                                                            | [Lecture 1 (CBC)](https://www.cbc.ca/player/play/audio/1.463798) · [Apple Podcasts](https://podcasts.apple.com/gb/podcast/the-2000-cbc-massey-lectures-the-rights-revolution/id151485663?i=1000652295166)                          |

---

## The full list

### A · Legal voices made for radio (UK)

- **Joshua Rozenberg** — shortlist 1.
- **Clive Anderson** · English — practised at the Bar for about fifteen years, then broadcasting; chairs
  BBC Radio 4's *Unreliable Evidence*, cross-examining senior judges and academics. Quick and witty —
  listen for whether the wit sits on top of the law or in place of it.
  🎧 *No direct link found* — search "Unreliable Evidence" in BBC Sounds.
  · about: [Middle Temple](https://www.middletemple.org.uk/bencher-persons-view/35175)
- **Jonathan Sumption (Lord Sumption)** · English — former Supreme Court Justice; the **2019 Reith
  Lectures**, *Law and the Decline of Politics*, five lectures before studio audiences.
  🎧 [Reith Lectures 2019](https://www.bbc.co.uk/programmes/m00057m8) (BBC, may be UK-only)
- **Philippe Sands** — shortlist 9.
- **Helena Kennedy (Baroness Kennedy)** · Scottish — barrister and broadcaster; narrates her own
  *Misjustice* / *Eve Was Shamed* (reviewers: "fantastic at getting across this passion").
  🎧 [Lisa Jardine Lecture 2019](https://www.youtube.com/watch?v=T-5KongPw1o) ·
  [JURIST interview, *the Rule of Law in Crisis*](https://www.youtube.com/watch?v=D2aoJnmCPMs) ·
  [*Misjustice* sample](https://www.audible.com/pd/Misjustice-Audiobook/1473576555)
- **Brenda Hale (Lady Hale)** — shortlist 3. Also 🎧 [valedictory remarks, Supreme Court 2019](https://www.youtube.com/watch?v=tkuLOTvB4Jc).
- **Geoffrey Robertson KC** · Australian — human-rights barrister; narrates his own *Lawfare*. Listen
  for whether the courtroom manner is too theatrical for this persona.
  🎧 [BBC *HARDtalk*](https://www.youtube.com/watch?v=ybvVB2iRQd4) ·
  [Mansfield public talk](https://www.youtube.com/watch?v=NcqQLyArsxo) ·
  [his narrations on Audible](https://www.audible.com/search?searchNarrator=Geoffrey+Robertson)

### B · Social science and philosophy on radio and podcasts

- **Laurie Taylor** — shortlist 2.
- **David Runciman** — shortlist 4.
- **Helen Thompson** — shortlist 6.
- **Michael Sandel** — shortlist 8.
- **Kwame Anthony Appiah** · English/Ghanaian — philosopher; the **2016 Reith Lectures**, *Mistaken
  Identities*. 🎧 [*Country*, via CBC Ideas](https://www.cbc.ca/radio/ideas/mistaken-identities-country-kwame-anthony-appiah-argues-against-a-mythical-romantic-view-of-nationhood-1.3921212) ·
  [*Country*, BBC](https://www.bbc.co.uk/programmes/b07zz5mf) (may be UK-only)
- **Onora O'Neill** · Northern Irish — philosopher; the **2002 Reith Lectures**, *A Question of Trust*.
  🎧 [Lecture 1, *Spreading Suspicion*, via ABC Listen](https://www.abc.net.au/listen/programs/bigideas/the-reith-lectures-2002---a-question-of-trust/3527146)
  ⚠ *one report says the ABC audio may have been withdrawn*
- **Stuart Russell** · English, based in the US — the **2021 Reith Lectures**, *Living with Artificial
  Intelligence*; a computer scientist on AI and governance, the persona's subject.
  🎧 [Reith Lectures 2021](https://www.bbc.co.uk/programmes/m001216k) (may be UK-only)
- **Brian Klaas** · American, based in the UK — political scientist at UCL; creates and **narrates**
  *Power Corrupts*. 🎧 [*Power Corrupts*](https://podcasts.apple.com/us/podcast/power-corrupts/id1458750622)
- **Michael Ignatieff** — shortlist 10.
- **Ronald Deibert** · Canadian — founder of the Citizen Lab (spyware investigations); the **2020 CBC
  Massey Lectures**, *Reset* — surveillance technology and civil society, close to Series C.
  🎧 [Lecture 1, *Look at that device in your hand*](https://www.cbc.ca/player/play/audio/1.5795778) ·
  [all six lectures](https://www.cbc.ca/radio/ideas/reset-reclaiming-the-internet-for-civil-society-1.5795345)
- **Tim Harford** · English — economist; a casework craft source, measured at ~127 wpm, though his
  dossier warns his voice is hard to judge through the production.
  🎧 [*Cautionary Tales*](https://podcasts.apple.com/us/podcast/cautionary-tales-with-tim-harford/id1484511465)

### C · American legal voices

- **Bryan Stevenson** — shortlist 5.
- **Jeffrey Rosen** — President of the National Constitution Center until his recent move to CEO
  Emeritus; hosted *We the People*, a weekly podcast of constitutional debate. The show now has new hosts,
  so pick **older episodes**. 🎧 [*We the People*](https://podcasts.apple.com/us/podcast/we-the-people/id83213431)
- **Dahlia Lithwick** — Slate; hosts *Amicus*, on law, justice and the courts.
  🎧 [*Amicus*](https://slate.com/podcasts/amicus)
- **Timothy Snyder** — Yale historian of tyranny and the rule of law; **narrates his own** *On Tyranny*.
  🎧 [Yale lecture 1, *The Making of Modern Ukraine*](https://www.youtube.com/watch?v=bJczLlwp-d8) ·
  [the course as a podcast](https://podcasts.apple.com/us/podcast/the-making-of-modern-ukraine/id1653131950) ·
  [*On Tyranny* sample](https://www.audible.com/pd/On-Tyranny-Audiobook/B06W9LYZXS)

### D · European law-and-technology scholars

Closest to the persona's subject; mostly lecture and conference recordings.

- **Joseph H. H. Weiler** — NYU, Jean Monnet Chair; moderates *EJIL: The Podcast!*.
  🎧 [EJIL interview](https://www.youtube.com/watch?v=4FdNP-8Ic9A) · [*EJIL: Live!*](https://ejil.org/live.php)
- **Lilian Edwards** · Scottish — Newcastle; internet and AI law since the 1990s.
  🎧 [*How to regulate foundation models*](https://www.youtube.com/watch?v=bMxBTYqDyOI)
- **Sandra Wachter** · Austrian — Oxford Internet Institute; the counterfactual-explanations work Series B
  taught. 🎧 [Oxford podcasts](https://podcasts.ox.ac.uk/people/sandra-wachter) ·
  [TWIML AI podcast](https://twimlai.com/podcast/twimlai/ais-legal-and-ethical-implications)
- **Mireille Hildebrandt** · Dutch — a casework craft source, the persona's frame.
  🎧 [*The Human Show* interview](https://the-human-show.captivate.fm/episode/mireille-hildebrandt-a-lawyer-philosopher-and-professor-at-radboud-universiteit-vrije-universiteit-brussels)
- **Jamie Susskind** — shortlist 7.

### E · The persona's other craft sources

- **William W. Fisher III** — Harvard Law, *CopyrightX*; dossier: register "dry and even".
  🎧 [Lecture 1.1, *The Foundations of Copyright Law*](https://www.youtube.com/watch?v=CqkonSY__ic)
- **Robert Sapolsky** — Stanford *Human Behavioral Biology*; a device source, live-room delivery.
  🎧 [Lecture 1](https://www.youtube.com/watch?v=NNnIGh9g6fA)

### F · Professional narrators of this kind of book — the licensable route

These read legal, political and technology nonfiction for a living, so a licence that covers cloning is a
normal commercial conversation. Each narrator link lists their titles; every title plays a sample.

- **Andrew Cullum** — narrates Lord Bingham's *The Rule of Law*.
  🎧 [audiobook preview](https://www.youtube.com/watch?v=vGmyVvGGjTo) ·
  [Audible sample](https://www.audible.co.uk/pd/The-Rule-of-Law-Audiobook/B0CW3VTLJJ)
- **David Rintoul** — narrates *East West Street* with Philippe Sands.
  🎧 [*East West Street* sample](https://www.audible.com/pd/East-West-Street-Audiobook/B01FRDISZI) ·
  [his narrations](https://www.audible.com/search?searchNarrator=David+Rintoul)
- **Nicol Zanzarella** — narrates Shoshana Zuboff's *The Age of Surveillance Capitalism*.
  🎧 [Hachette sample](https://soundcloud.com/hachetteaudio/the-age-of-surveillance-capitalism-by-shoshana-zuboff)
- **Larissa Gallagher** — narrates Kate Crawford's *Atlas of AI*.
  🎧 [Audible sample](https://www.audible.com/pd/Atlas-of-AI-Audiobook/B09NF4BZJW)
- **Chloe Cannon** — narrates Danielle Keats Citron's *The Fight for Privacy*.
  🎧 [Audible sample](https://www.audible.com/pd/The-Fight-for-Privacy-Audiobook/B0BFCPXQ3Q)
- **Dion Graham** — 2024 Audie for Best Non-Fiction Narrator (Jonathan Eig's *King: A Life*).
  🎧 [his narrations](https://www.audible.com/search?searchNarrator=Dion+Graham)

### G · Delivery references only — too recognisable to use

Worth hearing for *how* they explain law, but a cloned version would be heard as an impersonation.

- **Barack Obama** — former constitutional-law lecturer; *A Promised Land* won the 2022 Audie for
  narration by the author ("smooth baritone"). 🎧 [Audible sample](https://www.audible.com/pd/A-Promised-Land-Audiobook/0525633723)
- **Nina Totenberg** — NPR legal affairs correspondent since 1975.
  🎧 [her NPR reports](https://npr.org/people/2101289/nina-totenberg)
- **Michael Lewis** — *Against the Rules*, on fairness and referees, law included.
  🎧 [*Against the Rules*](https://www.pushkin.fm/podcasts/against-the-rules)

---

## Before committing: audition the finalists through the real pipeline

Chatterbox clones zero-shot, so testing a voice costs minutes. For each finalist with a clean 10–30 s
clip, run the existing audition, which renders a suite spanning the persona's whole tonal range with
its real settings:

```bash
prosodia-render audition --voices a.wav b.wav c.wav \
    --voice-profiles src/prosodia/author/personas/casework/voice_profiles.yaml
```

Then render one real Series C passage per finalist and **listen where you actually listen** — on the
train, on headphones, after the 0.9× tempo. A voice can sound right in a quiet room and wrong at
40 minutes, and Chatterbox's version of a voice is not the same as the voice. Once chosen, record the
clip's sha256 in `voices/README.txt`, like the existing clip, so it never changes silently.

**Provenance.** Facts about each person were checked by web search on 2026-10-09 against broadcaster,
publisher, university and retailer pages, linked above. Voice descriptions are quoted from published
reviews where given; otherwise none is offered — this list was compiled without hearing the voices.
