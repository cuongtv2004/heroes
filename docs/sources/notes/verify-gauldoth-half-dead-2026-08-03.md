# Verify report: gauldoth-half-dead — 2026-08-03

Verifier: independent agent, did not read the article
Claims checked: 42
CONFIRMED: 34 | DOWNGRADE: 4 | NOT_FOUND: 0 | CONTRADICTED: 4

**BLOCKER:** G-32
**MAJOR:** G-14, G-21, G-23, G-35, G-42
**MINOR:** G-04, G-19, G-24, G-41
**NOTE:** G-08, G-11, G-26, G-34, G-36, G-39 + five claim-table / technical-note errors (§ Claim-table errors)

## Sources actually retrieved

| Handle | URL | Bytes / note |
|---|---|---|
| transcript | `https://web.archive.org/web/20130117072816/http://www.celestialheavens.com/homm4/texts/H4-DeathTexts.rtf` | 89,002 bytes, `RTF v1 ANSI cp1252`; de-RTF'd to 84,110 bytes / 2,430 lines |
| ray | `https://web.archive.org/web/20151020063103/http://mmh7.ubi.com/en/blog/post/view/lost-tales-q-a-with-terry-ray` | 49,047 bytes |
| fandom-gauldoth | `https://mightandmagic.fandom.com/api.php?action=parse&page=Gauldoth&prop=wikitext&format=json&formatversion=2` | |
| fandom-iduna | same API, `page=Iduna` | |
| aoh-necromancers | `https://web.archive.org/web/20070917000000id_/http://www.heroesofmightandmagic.com/heroes4/heroes_necromancers.shtml` | 23,576 bytes |
| aoh-campaign-heroes | `.../heroes4/heroes_campaign.shtml` (same form) | 22,226 bytes |
| aoh-halfdead | `.../heroes4/campaign_halfdead.shtml` | 12,202 bytes |
| bullard | `https://heroes.thelazy.net/api.php?action=parse&page=Jennifer%20Bullard/Acid%20Cave%20Interview&prop=wikitext&format=json&formatversion=2` | orig. `https://www.acidcave.net/jennifer_bullard_interview.html` |
| thelazy-reckoning | `https://heroes.thelazy.net/index.php/The_Reckoning` | |
| lost-manuscripts | `https://heroes.thelazy.net/api.php?action=parse&page=Lost%20Manuscripts&...` | |
| fulton-names | `https://heroes.thelazy.net/api.php?action=parse&page=Gregory%20Fulton/On%20Names%20in%20Heroes%20of%20Might%20and%20Magic%20III&...` | 99,848 bytes raw JSON |
| 3do-story | `https://web.archive.org/web/20020108023325id_/http://www.3do.com/mightandmagic/heroes4/story.html` | 9,898 bytes |

**No fabricated quote found.** Every quote the claim table attributes to the transcript and to Terry Ray was retrieved verbatim. Given the recent fabrication incident, that is the single most important negative result in this report.

---

## Details

### G-01
Claim: Gauldoth is a half-living, half-undead necromancer, king of Nekross on Axeoth.
Label in article: (unlabelled)
Verdict: CONFIRMED
Severity: NOTE
Searched: transcript; mmh7.ubi.com (ray)
Found: transcript, Epilogue — "I am Gauldoth Half-Dead, King of Nekross!  And I plan to stay this way." Campaign blurb — "Half of his body is living, while the other half is Undead."
Reason: Confirmed. **But `Axeoth` appears 0 times in the entire transcript** (grep, all 84 KB). The world-name must be sourced elsewhere; the cleanest available support is the official Ubisoft page the article already cites — "Set on the  world of Axeoth, these two free bonus campaigns" — which is `T2`, not `T1*`. Do not let a reader infer "Axeoth" comes from game text.

### G-02
Claim: The author of Heroes IV's story calls him a "hero", and built him as the opposite of every fantasy necromancer.
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: CONFIRMED
Severity: —
Searched: ray
Found: "That's one of the reasons I think the Gauldoth campaign is so popular.  In my eyes, he is a hero." · "I set out to make Gauldoth the  opposite of every necromancer from every fantasy story"
Reason: Both halves verbatim, from Ray himself (not editorial prose). `T4 EXPLICIT` correct.

### G-03
Claim: His game text names Sandro and Kilgor — two Enroth characters.
Label in article: (unlabelled in summary; sourced later) · `h4-death-texts-ch`
Verdict: CONFIRMED
Severity: —
Searched: transcript (grep: Sandro ×1, Kilgor ×1)
Found: block `Philosophy` — "When others like the powerful necromancer, Sandro, sought to control the world, the force of destruction supported them temporarily." · block `Creation and Destruction` — "For one, the Reckoning claimed the life of that Barbarian scum, Kilgor."
Reason: Both are Gauldoth's own narration/dialogue in the campaign text. Confirmed.

### G-04
Claim: Earliest memory: "My first childhood memory is of a crypt… the Vampire who kept me alive to feed on my young blood."
Label in article: T1* EXPLICIT · `h4-death-texts-ch` (block `The Past`)
Verdict: CONFIRMED (quote) / block attribution wrong
Severity: MINOR
Searched: transcript, line 121
Found: "I sat on the grass and pressed the living side of my face against the cool surface of one of the markers.  My first childhood memory is of a crypt - the musky smell of earth, the silent darkness, the Vampire who kept me alive to feed on my young blood."
Reason: Quote verbatim. **The block is `Full Circle` (line 107), not `The Past` (line 151).** Fix the block citation. (If the block name was added by the claim compiler rather than the article, this is a claim-table error.)

### G-05
Claim: The vampire was Loscan; the lich Kalibarr freed him via a holy crusader after offering ten children.
Label in article: T1* EXPLICIT · `h4-death-texts-ch`
Verdict: CONFIRMED
Severity: —
Searched: transcript, block `The Past`
Found: "My Master, Kalibarr, told me once that he had seen a power within me that couldn't be wasted, but Loscan, the vampire who kept me for his own, wouldn't release me even when Kalibarr offered him ten young children as a replacement.  Since Loscan was a member of the Necromantic Order, Kalibarr's hands were tied.  He couldn't force Loscan to turn me over, so he arranged for a holy crusader to learn the location of the vampire's crypt.  That was the end of Loscan."
Reason: Verbatim; the article's two ellipses elide exactly "the vampire who kept me for his own" and "He couldn't force Loscan to turn me over," — honest elision, no meaning changed.

### G-06
Claim: Grew up as Kalibarr's student and assassin.
Label in article: T1* EXPLICIT · block `Vengeance`
Verdict: CONFIRMED
Severity: —
Searched: transcript, block `Vengeance` (line 231)
Found: "Whenever someone crossed him, he usually had me slip poison in their wine or a dagger between their ribs."
Reason: Verbatim, correct block.

### G-07 ⚠️⚠️ (load-bearing)
Claim: How he became Half-Dead — the Reckoning, the burning library, the scroll beyond his power.
Label in article: T1* EXPLICIT · block `The Past`
Verdict: CONFIRMED
Severity: —
Searched: transcript, block `The Past` (lines 151–172)
Found: "During the first hours of the Reckoning, I returned to the Necromantic Order's secret library to find it on fire.  Kalibarr lived within.  I tried to find him, but the fire was too great." / "Naked and with burns that would soon claim my life, I opened a scroll that was far beyond my power." / "I lived, of course.  At least, part of me was still alive.  The rest was undead.  I had a foot in both worlds now - living and dead - but I didn't feel part of either."
Reason: Every fragment verbatim, all inside block `The Past`. This is genuine in-game campaign text, not a Fandom paraphrase. `T1* EXPLICIT` correct. **Survives the attack.**

### G-08 ⚠️⚠️ (load-bearing)
Claim: Right half undead, left half living — game text, confirmed at eight independent places.
Label in article: T1* EXPLICIT · `h4-death-texts-ch`
Verdict: CONFIRMED
Severity: NOTE (count is an undercount, not an error)
Searched: transcript, full-text grep for right/left + hand/arm/side/cheek/handed
Found — all six article quotes located verbatim:
- L97 "I felt the skin of my dead right hand come loose just enough for me to slip free of my bonds."
- L205 "I reached up with my dead right arm and grabbed his wrist."
- L609 "With that ink, I tattooed Mardor's name on the living skin of my left arm."
- L1416 "Slowly, I brushed Alana's warm cheek with the soft, living fingers of my left hand."
- L1666 "The zombie's left arm was missing, cut off at the shoulder.  It was no coincidence that my living arm was my left."
- L1370 "You are right handed.  You have always touched the crystal with your dead right hand."
Five further independent attestations the article does not use: L738 "Grasping the hilt in your dead right hand"; L1056 "Would I become like a stroke victim, the left side of my body dead and motionless?"; L1408 "Suddenly, Alana took hold of my right arm, unconcerned that she was touching dead flesh."; L1760 "a silver mask in the exact likeness of the living left side of my face"; L1940 "painful for me to hold it in my living left hand."
Reason: **11 explicit attestations, not eight.** Zero counter-examples: nowhere does the transcript put the living half on the right. `T1* EXPLICIT` correct; "eight" is conservative and may be raised. **Survives the attack.**

### G-09
Claim: The living half still needs food; the undead half hungers for nothing.
Label in article: T1* EXPLICIT · block `Gauldoth`
Verdict: CONFIRMED
Severity: —
Searched: transcript, block `Gauldoth` (line 27ff)
Found: "The part of me that still requires sustenance hungers for what normal people eat - a juicy piece of beef or perhaps some salmon grilled over a wood fire.  The rest of me - the undead half - hungers for nothing.  That half is empty."
Reason: Verbatim, correct block. Note the source uses hyphens `-` where the article renders em dashes `—`; cosmetic, applies to several quotes.

### G-10
Claim: "My undead flesh is far stronger **that** it appears" — the typo is verbatim in the source.
Label in article: T1* EXPLICIT · block `Bandit Ambush`
Verdict: CONFIRMED
Severity: —
Searched: transcript, line 209 (inside block `Bandit Ambush`, 175–218); grep for "than it appears" = 0 hits
Found: "\"My undead flesh is far stronger that it appears,\" I whispered as I crushed the bandit leader's neck and dropped his limp body to the ground."
Reason: The typo is genuinely in the shipped text. Correct block. Good catch by the article; keep the `[sic]` marker.

### G-11 ⚠️
Claim: "Eater of Children" is false — game text denies it outright.
Label in article: T1* EXPLICIT · block `Gauldoth`
Verdict: CONFIRMED
Severity: NOTE (on the fairness of the reading)
Searched: transcript, block `Gauldoth`
Found: "They called me the 'Ghoul', and 'Eater of Children' as they tied me to the stake.  That last nickname was almost amusing.  To this day, I still have not tasted human flesh, or blood either."
Reason: Quote verbatim and the denial is explicit and first-person. **Caveat the article must not gloss over:** the same transcript has Gauldoth trafficking in children. Block `Nekorrum`: "I was finally getting volunteers since I offered monetary incentives to families who surrendered any child below the age of six for necromantic instruction." And the Epilogue: "I ordered the child pens to be destroyed." So "he never ate children" is exactly true; "the slander is unfair" is not the same proposition. Phrase G-11 as *cannibalism denied*, not *innocence established*.

### G-12 ⚠️
Claim: The first scenario of the campaign is titled `Eater of Children`.
Label in article: (unlabelled)
Verdict: CONFIRMED
Severity: —
Searched: transcript line 13; aoh-halfdead
Found: transcript — "Scenario 1: Eater of Children". AoH — "- HALF-DEAD CAMPAIGN - Scenario 1 - Eater of Children"
Reason: Two independent attestations. The observation (game titles the scenario with the slander, then rebuts it in narration) is sound.

### G-13
Claim: Scenario description — "Alone in this new world for years, Gauldoth has lived like an animal in the wilderness…"
Label in article: T1* EXPLICIT · `aoh-h4-campaign-halfdead`
Verdict: CONFIRMED
Severity: —
Searched: aoh-halfdead; transcript line 15
Found (AoH, verbatim): "Alone in this new world for years, Gauldoth has lived like an animal in the wilderness. When some farmers catch him and try to burn him at the stake, Gauldoth barely escapes into the forest. Soon, rage and fear give birth to a new sense of purpose."
Reason: Identical to transcript line 15, i.e. Age of Heroes is reproducing genuine in-game scenario text here. `T1*` is the **right** tier for this specific claim (contrast G-23). Confirmed twice over.

### G-14
Claim: Sequence to the throne — Vitross, slowing spell, graveyard, **kills the druid Halas**, burns Vitross, turns **Mardor** into a **ghost** lieutenant, establishes Nekross, King of Nekross.
Label in article: T1* EXPLICIT · `h4-death-texts-ch`
Verdict: DOWNGRADE
Severity: **MAJOR**
Searched: transcript (all 3 Halas mentions: L219, L221, L225; all 20 Mardor mentions); aoh-halfdead scenario 1; `fandom:Halas`
Found — supported verbatim: "Ghoul!" and 'Eater of Children' at the stake; the slowing spell — "my spell would send an unearthly chill into the muscles of everyone present, slowing their movement enough for me to escape"; "A few nights later, I came upon a field of gravestones.  A graveyard!"; "I'm going to burn you, Mardor, until there is nothing left but bones… I need a military commander I can trust."; "Over the past few months… the former Sir Mardor, has taken the bulk of my army to carve out the borders of what will become the new Kingdom of Nekross"; "This was my first correspondence as King of Nekross".
Found — **not** supported: the transcript **never says Halas is killed**. The three Halas lines are the warning letter only. The nearest thing is past tense in block `Survival`: "However, I have never seen a power like the one this druid possessed." That is an inference, not a statement. Worse, `fandom:Halas` says: "While Halas is mentioned in the ''Heroes of Might and Magic IV'' scenario `Eater of Children`, he is not represented by an in-game unit."
Reason: Two defects inside one `T1* EXPLICIT` compound claim. (1) "kills the druid Halas" must be demoted to `INFERENCE` at best, and the Fandom line above argues it may simply be **wrong** — recommend rewording to "removes Halas as an obstacle" / "defeats the druid's forces". (2) Mardor is a **Specter**, not a ghost: "the spectral commander of my forces, the former Sir Mardor" and "Specters don't need sleep". Per this project's naming convention, use the game's word.

### G-15 ⚠️
Claim: Gauldoth voluntarily hands the throne back to Kalibarr — "It's all yours" / "It's a start."
Label in article: T1* EXPLICIT · block `Nekorrum`
Verdict: CONFIRMED
Severity: —
Searched: transcript, block `Nekorrum` (line 816ff)
Found: "\"It's all yours,\" I told my Master when we completed the tour." / "Master Kalibarr was silent for some time.  He leaned on me for support, still too weak to exert himself for any length of time, and said, \"It's a start.\""
Reason: Verbatim, correct block, correct reading (voluntary — no coercion in the text).

### G-16
Claim: "Malvich means nothing to me, Gauldoth, because Nekross means nothing to me! Bring me the Deadwood Staff or I will find someone else to serve me!"
Label in article: T1* EXPLICIT · block `Malvich`
Verdict: CONFIRMED
Severity: —
Searched: transcript, line 1602 (inside block `Malvich`, 1560–1627)
Found: exactly as claimed, verbatim.
Reason: Confirmed, correct block.

### G-17 ⚠️
Claim: After killing Kalibarr — "I cannot think badly about my former master… I like to think that he really died during the Reckoning - not by my hand. It's easier that way."
Label in article: T1* EXPLICIT · block `Kalibarr Defeated`
Verdict: CONFIRMED
Severity: —
Searched: transcript, block `Kalibarr Defeated` (line 2380ff)
Found: "I try to muster the anger that is rightfully mine, but I cannot think badly about my former master." / "I like to think that he really died during the Reckoning - not by my hand.  It's easier that way."
Reason: Verbatim, correct block.

### G-18 ⚠️⚠️ (load-bearing)
Claim: Ray — "hands down and far ahead in this race for my love… is Gauldoth Half-Dead. I set out to make Gauldoth the opposite of every necromancer from every fantasy story…"
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: CONFIRMED
Severity: —
Searched: ray (archived page, favourite-characters answer)
Found: "But hands down and far ahead in this race for my love like a cheetah  running against sloths is Gauldoth Half-Dead. I set out to make Gauldoth the  opposite of every necromancer from every fantasy story and he became so much  more during the writing process."
Reason: Verbatim. The article's ellipsis elides only "like a cheetah running against sloths". **Not fabricated.** `T4 EXPLICIT` correct.

### G-19 ⚠️
Claim: Ray — "Despite his horrible life, he's a philosopher and probably wiser than anyone around him. He is not ruled by a quest for power like most necromancers."
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: DOWNGRADE
Severity: MINOR
Searched: ray
Found: "Despite his horrible life, he's a  philosopher and probably wiser than anyone around him. He is not ruled by a  quest for power like most necromancers, **but he sees the purpose and usefulness  of power.**"
Reason: The words quoted are genuine, but the article **ends the sentence with a full stop where the source has a comma and an adversative clause**. Ray's actual position is "not ruled by power-lust, but not power-blind either" — the truncation flattens it into simple asceticism. Either restore the clause or mark the cut with an ellipsis. Not a fabrication; a silent truncation.

### G-20 ⚠️
Claim: Ray — "He is neither good nor evil." · "I wanted him to be a metaphor for all Mankind." · "In my eyes, he is a hero."
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: CONFIRMED
Severity: —
Searched: ray
Found: "He is neither good nor evil. He sees chaos and order, creation and  destruction all as one thing dependent on each other. I wanted him to be a  metaphor for all Mankind." (favourite-characters answer) · "In my eyes, he is a hero." (script-notes answer)
Reason: All three verbatim. The article correctly treats them as three separate fragments rather than one continuous quotation — the third comes from a different answer. Good practice.

### G-21 ⚠️
Claim: Ubisoft calls Ray "Heroes IV's master bard", and the interview is dated 09/11/2015 on the official Ubisoft MMH7 site.
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: DOWNGRADE
Severity: **MAJOR** (wrong *kind* of source)
Searched: ray
Found: "were written by Heroes IV's  master bard: Terry B. Ray" (Ubisoft's editorial intro) · page byline "09/11/2015"
Reason: Both facts are verbatim and the host really is official Ubisoft (`mmh7.ubi.com`). **But neither is a developer statement.** "Master bard" is the publisher's marketing epithet and the date is site metadata — under this project's own tier table that is **`T2` (official publisher website)**, not `T4` (developer statement). Labelling publisher prose `T4` is precisely the "wrong kind of source" error the protocol grades MAJOR — and it is the mirror image of the `heroesofmightandmagic.com` precedent. Fix: split G-21 off as `T2 EXPLICIT`, keep G-18/G-19/G-20 as `T4`.

### G-22 ⚠️
Claim: Ray also wrote the Heroes Chronicles series.
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: CONFIRMED
Severity: —
Searched: ray
Found: "All told, I was hired to work on  Heroes  IV , but also wrote the  Heroes III  Chronicles  series."
Reason: Verbatim, Ray's own words, `T4 EXPLICIT` correct. Two small precisions: Ray writes "**Heroes III Chronicles**" (the shipped product is *Heroes Chronicles*); and this is a first-person authorship claim that partly conflicts with Jennifer Bullard's account of the same series in the Acid Cave interview — "So I was asked to create 8 campaigns… Each original story & maps was written by one level designer and then I cleaned and polished them until ship." Two developers each describing themselves as central. Worth a one-line `DISPUTED` note rather than presenting Ray's version as settled.

### G-23
Claim: Class = Necromancer (magic class of Necropolis); alignment Death/Necropolis; class starts with Basic Death Magic + Basic Occultism.
Label in article: T1* EXPLICIT · `aoh-h4-heroes-necromancers`
Verdict: DOWNGRADE
Severity: **MAJOR** (wrong kind of source + wrong page)
Searched: aoh-necromancers (full text); aoh-campaign-heroes; `fandom:Necromancer (H4)`; `fandom:Gauldoth`
Found: AoH `heroes_necromancers.shtml` — "Necromancers start with Basic Death Magic and Basic Occultism. Necromancer hero cost in Necropolis is 1500 Gold." AoH footer — "Thanks to Lich ( Guardian's Grove Admin, Heroes Community Moderator) for heroes data and images" · "Age of Heroes is copyrighted ©1999-2006." Fandom — "The '''Necromancer''' is the basic magic class of the [Necropolis] faction in ''Heroes of Might and Magic IV''. It starts with Basic Death Magic and Basic Occultism."
Reason: Two defects. (1) **Tier.** The gameplay figures on that page are a fan-compiled data table, explicitly credited to a community contributor — that is `T6` **community reconstruction**, not `T1*` in-game text via an intermediary. `T6` cannot carry `EXPLICIT` under this project's rule. (Contrast G-13, where AoH reproduces actual in-game prose — `T1*` is right *there*.) (2) **Wrong page.** Gauldoth is **not on `heroes_necromancers.shtml` at all** — that page lists 26 regular Necromancers (Archilus … Yxia, including Sandro) and no Gauldoth. His class assignment is on `heroes4/heroes_campaign.shtml`, under the heading "Campaign Necromancers", where his entry sits. Recite that page, and re-tier to `T6 INFERENCE` (or find real `T1`).

### G-24 ⚠️
Claim: Heroes IV has no "specialty" mechanic like Heroes III, and no source assigns a specialty to Gauldoth.
Label in article: (unlabelled) · no source
Verdict: CONFIRMED
Severity: MINOR (true but uncited — an unsourced negative)
Searched: `fandom:Specialty`; `fandom:Heroes of Might and Magic IV`; aoh-campaign-heroes; aoh-necromancers; fandom-gauldoth
Found: `fandom:Specialty` — "The '''specialty''' is a gameplay element for all heroes in ''Heroes of Might and Magic III'', ''Heroes of Might and Magic V'', ''Might & Magic: Heroes VI'', ''Might & Magic: Heroes VII'', and ''Heroes of Might and Magic: Olden Era''." (H4 is absent from that enumeration.) `fandom:Heroes of Might and Magic IV` — "all Heroes of a given class start out with the same skills" and, in the reception section, "the treatment of heroes as units with no unique specialties for each individual hero."
Reason: The negative holds, and I found no specialty assigned to Gauldoth anywhere. Per the project's first law, an unsourced negative must still carry a source — attach the two Fandom quotes above at `T6 INFERENCE`. One trap to disarm in the wording: the same Fandom page says of *The Gathering Storm*, "Each of the first five campaigns features a new specialty hero" — a different sense of the word, not a counter-example.

### G-25 ⚠️
Claim: The Age of Heroes heading says "Death/Necropolis **Might** Heroes — Necromancers", which is wrong: Necromancer is the magic class and Death's might class is Death Knight.
Label in article: (unlabelled) · `aoh-h4-heroes-necromancers`
Verdict: CONFIRMED
Severity: —
Searched: aoh-necromancers; `fandom:Necromancer (H4)`
Found (AoH, verbatim heading): "Death/Necropolis Might Heroes - Necromancers". Refutation, `fandom:Necromancer (H4)`: "The '''Necromancer''' is the basic magic class of the [Necropolis] faction… Its might counterpart is the [Death Knight (H4)]."
Reason: The heading is verbatim as claimed and is verbatim wrong; the AoH page's own sidebar even lists "Death Knight" separately. The article's correction is right. Reinforces the site's status as a fan compilation — footer: "Age of Heroes is copyrighted ©1999-2006. Unauthorised reproduction is prohibited."

### G-26 ⚠️
Claim: No source has a full stat block (Attack / Defense / Spell Power / Knowledge) for Gauldoth.
Label in article: (unlabelled, also in Open questions)
Verdict: CONFIRMED
Severity: NOTE (true as literally stated, but incomplete)
Searched: fandom-gauldoth (full wikitext); aoh-campaign-heroes; aoh-halfdead scenario 1; aoh-necromancers
Found: no Attack/Defense/Spell Power/Knowledge figures anywhere. **However Fandom does carry a partial block** the article appears not to reflect — `fandom:Gauldoth`, "Gauldoth's stats in Eater of Children", level 2, with `Basic Death Magic`, `Basic Occultism` **and `Basic Nature Magic`**, spells `Curse` and `Summon sprite`. AoH gives scenario framing only: "Victory Condition: Capture Vitross. Loss Condition: Lose Gauldoth Half-Dead. Carryover: Gauldoth and all of his spells, skills, and experience will transfer to the next map."
Reason: The four-primary-stat negative survives. But "no full stat block" should not be allowed to read as "no gameplay data at all" — the third starting skill (`Basic Nature Magic`) is Gauldoth-specific, is absent from the class default the article cites in G-23, and is thematically corroborated by the transcript's `Survival` block, where Gauldoth becomes interested in Nature Magic after Halas. Add it (at `T6`) or say explicitly why it is excluded.

### G-27 ⚠️⚠️ (load-bearing)
Claim: Fandom's infobox gives four family relations all citing the same ref to the Ray interview; and `fandom:Iduna` says Ray's script notes "revealed that she was the mother of" Lysander, Waerjak and Gauldoth.
Label in article: T6 EXPLICIT · `fandom-gauldoth` + `fandom-iduna`
Verdict: CONFIRMED
Severity: —
Searched: fandom-gauldoth and fandom-iduna raw wikitext via API
Found — `fandom:Gauldoth` infobox, verbatim:
```
|relatives = [[Nicolas Gryphonheart]] (father)<ref name=Family>[https://mmh7.ubi.com/en/blog/post/view/lost-tales-q-a-with-terry-ray MMH7 blog]</ref><br />[[Iduna]] (mother)<ref name=Family/><br/>[[Lysander (Axeoth)|Lysander]] (brother)<ref name=Family/><br />[[Waerjak]] (brother)<ref name=Family/><br />[[Catherine Gryphonheart]] (half-sister)<br />[[Nicolai Ironfist]] (nephew)<br />[[Beatrice Gryphonheart]] (half-sister)<br />
```
Found — `fandom:Iduna`, verbatim: "but [[Terry Ray]]'s script notes for ''[[Heroes of Might and Magic IV]]'' revealed that she was the mother of [[Lysander (Axeoth)|Lysander]], [[Waerjak]], and [[Gauldoth]], three of the game's protagonists" with the same `mmh7.ubi.com` ref.
Reason: Exactly as the article describes — one `ref name=Family` reused for all four relations, pointing at the Ray interview. `T6` is the right tier for "what Fandom says"; `EXPLICIT` is acceptable here because the claim is *about Fandom's own text*, which I quoted. Only nit: the article lists the four in a different order than Fandom (Fandom puts father first). **Survives the attack.**

### G-28 ⚠️⚠️ (load-bearing)
Claim: In that very source Ray says the opposite — "Not like they were all from the same mother, but all from the same bloodline" and "this idea was never completely developed."
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: CONFIRMED
Severity: —
Searched: ray (script-notes answer)
Found, verbatim: "When I looked on the future of the story line, I wanted to select three  characters that would be pivotal in future games. I wanted these characters to  share the same blood. Not like they were all from the same mother, but all from  the same bloodline. That is where Lysander, Waerjak, and Gauldoth came in. In  my defense, this idea was never completely developed. I was toying with other  options too, but these three characters were at the top of the list."
Reason: Both fragments verbatim, in a single answer, from Ray. The contradiction with G-27 is real and direct: Fandom's ref says "same mother"; the cited source says "**Not** like they were all from the same mother". `T4 EXPLICIT` correct. **Survives the attack — verified from the source side independently of the Fandom side.**

### G-29 ⚠️
Claim: The interviewer's question carried the "same mother" premise; Ray denied that detail in the next sentence; Fandom turned the question's premise into the answer.
Label in article: (unlabelled)
Verdict: CONFIRMED
Severity: —
Searched: ray
Found — the question, verbatim: "Your script notes reveal some secrets about some of Heroes IV's  characters. For instance, **the fact that** Lysander, Waerjak and Gauldoth were  actually brothers, the illegitimate sons of King Nicholas Gryphonheart with a  woman named Iduna. What was your \"master plan\" with the storyline?"
Reason: The interviewer asserts it as "the fact that", supplying both "brothers" and "with a woman named Iduna". Ray's answer opens "Ah, you caught me! Knew I should have burned those notes." (which concedes only that notes exist), then in the substantive paragraph rejects the mother detail. So the article's reconstruction is exactly right: Fandom's `ref` points at a page where the *question* contains the claim and the *answer* denies part of it. This is the article's strongest original finding and it holds on both sides. **Survives the attack.**

### G-30 ⚠️
Claim: The three second-order relations (Catherine half-sister, Nicolai Ironfist nephew, Beatrice half-sister) have no ref at all.
Label in article: (unlabelled)
Verdict: CONFIRMED
Severity: —
Searched: fandom-gauldoth raw wikitext (quoted in full under G-27)
Found: after `[[Waerjak]] (brother)<ref name=Family/>` the string runs `<br />[[Catherine Gryphonheart]] (half-sister)<br />[[Nicolai Ironfist]] (nephew)<br />[[Beatrice Gryphonheart]] (half-sister)<br />` — **zero `<ref>` tags** on any of the three.
Reason: Verbatim confirmation from the wikitext. Confirmed.

### G-31
Claim: Ubisoft's question spells the king "Nicholas", Fandom spells it "Nicolas".
Label in article: (parenthetical)
Verdict: CONFIRMED
Severity: —
Searched: ray; fandom-gauldoth
Found: ray — "King Nicholas Gryphonheart" · fandom — `[[Nicolas Gryphonheart]] (father)`
Reason: Both verbatim. Confirmed.

### G-32 ⚠️
Claim: Jennifer Bullard says Kalibarr was **held on the old planet** after the Reckoning, while game text has scenario 2 opening a portal to another world (Fiery Realm). Article resolves in favour of game text and notes Bullard said her memory "may not be perfect".
Label in article: T4 EXPLICIT + T1* EXPLICIT · `bullard-interview-2013` + `h4-death-texts-ch`
Verdict: **CONTRADICTED**
Severity: **BLOCKER**
Searched: `https://heroes.thelazy.net/api.php?action=parse&page=Jennifer%20Bullard/Acid%20Cave%20Interview&...` (republishing `https://www.acidcave.net/jennifer_bullard_interview.html`), section "Heroes of Might and Magic IV"; transcript scenario 2
Found, verbatim, question and answer together:
> "Q: Where was Kalibarr when Gauldoth came looking for him? Is it the planet after [[the Reckoning]] or a different planet conquered by [[Kreegan|Kreegans]]? If it's the planet conquered by [[Kreegan|Kreegans]], how Kalibarr got there?
>
> A: Kalibarr was held on **the planet after the Reckoning**, he was kidnapped and brought there by [[Demon|Demons]]."
Reason: **Bullard did not say "the old planet". She said "the planet after the Reckoning" — and the question's own wording makes that phrase mean the *new* world, Axeoth, as opposed to "a different planet conquered by Kreegans".** The article has inverted her answer. This is a misstatement of a `T4` source's content published under an `EXPLICIT` label, i.e. exactly the failure mode the protocol exists to catch, so it blocks regardless of the fact that the article's *conclusion* survives: game text does place Kalibarr off-world. Transcript support for that side is solid — scenario 2 blurb, "A startling vision from another realm informs Gauldoth that his Master, Kalibarr, didn't perish during the Reckoning.  Now, he must battle crusaders and demons to find a way to reach this otherworld"; block `The Kreegans`, "some retreated to the safety of another realm.  That's where I would find my Master!"; block `Kalibarr`, "\"A Kingdom needs a powerful leader, and my body is still weak from the spell I cast to save myself from the Reckoning,\" Kalibarr admitted.  This was the first hint he had given me about how he escaped and ended up in the demon realm." The "may not be perfect" hedge is also verbatim: "It has been many years since I worked on those games, so my memory may not be perfect but I will do my best."
Fix: restate as *Bullard places Kalibarr on the post-Reckoning world (Axeoth), brought there by Demons; game text places him in a separate demon realm reached through a gateway*. Keep the resolution; correct the premise. Also note the source is a fan-site interview (Acid Cave, "conducted in 2013 by Alchemik") republished on a fan wiki — the developer's words are `T4`, the access path is an intermediary.

### G-33 ⚠️
Claim: "Gauldoth went through the portal along with other refugees" is not in the transcript; the transcript only says he survived and was "Alone in this new world for years".
Label in article: T6 FAN_THEORY · `fandom-gauldoth`
Verdict: CONFIRMED
Severity: —
Searched: transcript, grep for portal / refugee / exodus / crossed over (every hit inspected); fandom-gauldoth
Found — Fandom's extrapolation, verbatim: "Now half-living and half-Undead, Gauldoth escaped the blazing library \"alive\", surviving the destruction of the world alongside countless fellow refugees by passing through one of the portals to Axeoth." — cited to `ref name="H4HDM1"`, the transcript.
Found — the transcript: every one of the 8 portal mentions concerns Kalibarr's laboratory gateway or the Plane of Death, **except** the God of Death's line at L2084: "I have visited the remains of your former world, Kalibarr.  I have seen the rubble of ancient cities, the bones of those who couldn't make it through those annoying portals!  So much gone.  It was beautiful!  But it's a pity so many escaped my reach." And L15/L5 give only "Alone in this new world for years" / "Gauldoth lost everything when the world was destroyed".
Reason: The article is right — Fandom's "passing through one of the portals" is not in the cited transcript, and `T6 FAN_THEORY` is the correct handling. One precision to add so the negative is not overstated: the transcript *does* establish that escape portals existed and that many escaped (L2084) — what it never states is that **Gauldoth** used one. Say that, not "portals are absent from the transcript".

### G-34 ⚠️
Claim: The god of death the campaign refers to is never named in game text.
Label in article: (unlabelled, in Open questions)
Verdict: CONFIRMED
Severity: NOTE (developer commentary exists and should be cited)
Searched: transcript, exhaustive grep for `god`/`gods`/`goddess`/`deity` — exactly two hits; blocks `Death`, `The Plane of Death`, `Masters`
Found: scenario 5 blurb — "when he learns that the lich actually serves a malicious **god of death** determined to destroy every living being on this new world" (no name). Only other hit, block `Creation and Destruction`: "Some would say such an inspiration came from 'the gods,'". In dialogue he is only "the dark one".
Reason: The negative holds for game text. **But this is the project's BH-3 pattern, and it recurs here:** developer commentary on this exact open question does exist, on the wiki the article already uses. `fandom:God of Death` carries a Terry Ray statement, cited to `http://www.celestialheavens.com/forum/10/14301`: "When I was writing everything, I pictured doing several heroes and slowly bringing that guy out.....however, I kept him vague just in case people wanted to do something else with him. So, Necros could certainly be the God of Death". Also relevant, Bullard on the setting: "Which is why we use things like [[Paradise]] or the Plane of Death." Restate G-34 as *never named in game text; Ray has said he deliberately kept him vague and would not rule out Necros* — with the forum URL fetched and registered, not cited at second hand. An Open question that a developer has half-answered must say so.

### G-35 ⚠️
Claim: thelazy gives the Reckoning date as 10 February 1177 AS but cites `Lost Manuscripts#11-08-1178` — not fetched, and the two numbers disagree (1177 vs 1178).
Label in article: T6 UNVERIFIED · `thelazy-the-reckoning`
Verdict: **CONTRADICTED** (in its reasoning)
Severity: **MAJOR**
Searched: `https://heroes.thelazy.net/index.php/The_Reckoning`; `https://heroes.thelazy.net/api.php?...page=Lost%20Manuscripts`
Found — thelazy, verbatim: "On February 10th, 1177 `[[AS]]`<sup>`[[Lost Manuscripts#11-08-1178|1]]`</sup>, a massive explosion is created by the clash of Gelu's Armageddon's Blade and Kilgor's Sword of Frost"
Found — `Lost Manuscripts`, the two entries that generate it. Kendal, dated `01-02-1172` … `02-04-1177`, the last reading: "A strange woman appeared to me last night… \"I haven't much time. [[Kilgor]] has found the ancient [[Sword of Frost]]…\"" Then Lysander, dated `11-08-1178`: "I will take over [[General Kendal]]'s recordings from now on… The woman's name was [[Ravenwood]], and she appeared to me at the same time she appeared to [[General Kendal]].  **Six days later** the [[Sword of Frost]] and [[Armageddon's Blade (artifact)|Armageddon's Blade]] crossed on a field of combat."
Reason: **The two numbers do not disagree.** `1177` is the date of the *event* (Kendal's entry 02-04-1177, plus "six days later" = 10 February 1177); `11-08-1178` is the date Lysander *wrote his retrospective entry*, more than a year afterwards. thelazy's derivation is arithmetically sound and its anchor points at the entry that supplies the "six days". The article asserts an internal inconsistency in a source that does not have one — the same class of error as G-27/G-28, only this time the article is the one misreading. The source is also no longer "not fetched": `Lost Manuscripts` is retrievable at the URL above and identifies itself as "In 2017 [[Jennifer Bullard]] shared various outlines for the backstory of [HoMM4], written in the early 2000s… Note that the information here might not be entirely canonical". Rewrite: thelazy's 10 Feb 1177 AS is a *derived* date (`T6 INFERENCE`) resting on a developer-released outline, and the residual uncertainty is the outline's own non-canonicity disclaimer — not a 1177/1178 conflict.

### G-36 ⚠️
Claim: Both wikis use the `AS` calendar for Axeoth, but no source says Axeoth uses it; and the Half-Dead campaign contains no absolute date at all.
Label in article: (unlabelled, in Open questions)
Verdict: CONFIRMED
Severity: NOTE
Searched: fandom-gauldoth; thelazy-reckoning; lost-manuscripts; transcript (grep for every 4-digit number, and for `A.S.`/`anno`/`calendar`/`century`)
Found — the wikis' usage, verbatim: fandom-gauldoth `|birth = ~ 1100s [[AS]]` and `|years = ca 1180s [[AS]]`; thelazy "On February 10th, 1177 `[[AS]]`".
Found — the transcript: the **only** 4-digit string in all 84 KB is `2509`, from the RTF generator header (`Msftedit 5.41.21.2509`). Zero years, zero `AS`, zero calendar references. Second half fully confirmed.
Reason: The first half also survives — neither wiki cites anything establishing that Axeoth continues the `AS` reckoning, and `Lost Manuscripts` writes bare dates (`11-08-1178`) with no era marker; the `[[AS]]` link is thelazy's editorial addition. One piece of evidence the open question should acknowledge rather than omit: the `11-08-1178` entry was written **after** the migration ("I was named king shortly after we arrived here", "The new Kingdom is called Iranese"), so a developer-released document does continue the same year-numbering on the new world. That is real evidence for continuity, still short of a source saying "Axeoth uses AS". Frame it that way.

### G-37 ⚠️
Claim: Disambiguation checked three ways: there is only ONE Gauldoth; `Gauldoth Half-Dead` is a redirect to the same entity.
Label in article: (unlabelled)
Verdict: CONFIRMED
Severity: —
Searched: `mightandmagic.fandom.com` `list=allpages&apprefix=Gauldoth`; `list=search&srsearch=Gauldoth` (30 results); `heroes.thelazy.net` `apprefix=Gauldoth`; aoh-necromancers + aoh-campaign-heroes hero rosters
Found: allpages returns exactly two titles — `Gauldoth` (pageid 12489) and `Gauldoth Half-Dead` (pageid 12691), whose entire wikitext is `#REDIRECT [[Gauldoth]]`. The 30-result full-text search surfaces no second Gauldoth (all hits are campaign/character pages of the same storyline). thelazy: `{"allpages":[]}`.
Reason: BH-2 discharged properly. No `Gauldoth (Xeen)`-style trap exists. Confirmed.

### G-38 ⚠️
Claim: He does not appear in *The Gathering Storm* or *Winds of War* — four pages scanned, 0 hits — and Ray confirms he did not work on them.
Label in article: T4 EXPLICIT · `ray-interview-ubisoft-2015`
Verdict: CONFIRMED
Severity: —
Searched: `aoh .../heroes4/tgs_heroes.shtml` (14,570 B), `tgs_campaigns.shtml` (14,512 B), `wow_heroes.shtml` (15,021 B), `wow_campaigns.shtml` (13,672 B) — case-insensitive grep for "gauldoth": **0, 0, 0, 0**; ray
Found — Ray, verbatim, in answer to a question that itself names the two expansions and says they featured "new characters, with no connection to the stories of Emilia, Gauldoth and co.": "No, I wasn't involved in those titles. That was after me. When  Heroes IV  shipped, most of the company  was let go."
Reason: Both halves independently reproduced. Ray's sentence is a genuine `T4` first-person statement, so `T4 EXPLICIT` is right for that half; the 0-hits half rests on a fan site and should be tiered `T6` separately. Corroboration from a second developer, Bullard, on why the expansions diverged: "the layoffs happened so soon after the launch I am not sure how much was utilized in the subsequent expansions."

### G-39 ⚠️
Claim: `fulton-names-2023` has no entry for `Gauldoth` — all 98,499 bytes grepped.
Label in article: (unlabelled)
Verdict: CONFIRMED
Severity: NOTE (true but evidentially empty as presented)
Searched: `https://heroes.thelazy.net/api.php?action=parse&page=Gregory%20Fulton/On%20Names%20in%20Heroes%20of%20Might%20and%20Magic%20III&prop=wikitext&...` — 99,848 bytes raw JSON (wikitext consistent with the article's 98,499); grep: Gauldoth 0, Axeoth 0
Found — the document's self-description, verbatim: "''Interview posted on 08/AUG/2023 on [Celestial Heavens], detailing Amelrix's correspondence with [[Gregory Fulton]] from 2022―2023.''" and "While studying at university at the department of philology, I chose as a topic for my research project of my thesis names from [HoMM3] (specifically town and hero names)."
Reason: 0 hits confirmed, and I verified the grep is meaningful by testing names that *are* present — `Gurnisson` 1, `Vidomina` 1, `Solmyr` 1, `Shakti` 1. **But the document is about Heroes III names only.** Gauldoth is a Heroes IV character, so his absence is expected and carries no information about Gauldoth's name at all. As written, the Open question implies a search that came up empty; in fact the source was never in scope. Either drop it or say plainly "out of scope: Fulton's document covers HoMM3 names".

### G-40 ⚠️
Claim: No character named "Nikolai" exists in the campaign transcript.
Label in article: (unlabelled)
Verdict: CONFIRMED
Severity: —
Searched: transcript, case-insensitive grep for Nikolai / Nicolai / Nicholas / Nicolas — 0, 0, 0, 0
Found: no hits.
Reason: Confirmed. Worth adding for the reader's benefit that the near-miss is on Fandom, not in game text: `fandom:Gauldoth` lists `[[Nicolai Ironfist]] (nephew)` — one of the three unreffed relations from G-30.

### G-41
Claim: The transcript is 89,002 bytes and contains 54 event blocks plus 5 quests with full `Proposal`/`Progress`/`Completion` states.
Label in article: (source table) · `h4-death-texts-ch`
Verdict: **CONTRADICTED** (byte count right, structure counts wrong) — and, on the tier question, `T1*` is vindicated
Severity: MINOR
Searched: the RTF itself, byte count and full structural enumeration
Found: **89,002 bytes exactly** — matches. `file`: "Rich Text Format data, version 1, ANSI, code page 1252". Structure: **56** `==Header==` blocks, of which **9** are `==Quest: …==` (Bone Dragons; The Angel's Blade; The Nexus Point; First Point of Power; Second and Third Points of Power; Fourth Point of Power; Fifth Point of Power; Shrine of Korbert; Suraze) and **47** are event blocks. Plus 5 `Scenario N:` headers. State keywords: 9 × `Proposal`, **8** × `Progress`, 9 × `Completion` — `Quest: Fifth Point of Power` has `Proposal` and `Completion` but **no `Progress`**.
Reason: "54 event blocks plus 5 quests" is wrong on both numbers: it is **47 event blocks and 9 quest blocks**, and "full Proposal/Progress/Completion" is true of 8 of the 9, not all. Correct the source-table row. **On the load-bearing tier question the answer is favourable:** this is verbatim in-game text, not a fan paraphrase. Proof: the shipped typo survives uncorrected ("far stronger **that** it appears"), the hero-biography string is byte-identical to the one Age of Heroes and Fandom independently reproduce, and the file preserves the game's own block/quest-state scaffolding. `T1*` is the right tier and the article's foundation is sound.

### G-42 ⚠️
Claim: The Axeoth era still has no official `T2` source — unlike Heroes III, where *Diaries of Archibald* on `3do.com` provides real `T2`.
Label in article: (unlabelled)
Verdict: **CONTRADICTED**
Severity: **MAJOR**
Searched: `http://web.archive.org/cdx/search/cdx?url=3do.com/mightandmagic/heroes4/*&...` (full page inventory: `story`, `intro`, `features`, `gameplay`, `expansions`, `expansion-tgs`, `expansion-wow`, 14 × `char_*`, galleries); `3do_story.html`; ray
Found — counterexample 1, the official publisher's own H4 storyline page, `https://web.archive.org/web/20020108023325id_/http://www.3do.com/mightandmagic/heroes4/story.html`, verbatim: "**Genesis of a New World:** Some prophecies of doom come true. Escape the flames licking at your back and jump quickly through a portal into another world for only the bold will be allowed to live. Embrace a wondrous new land. Uncover its ancient mysteries, battle its deadly creatures, and explore its forgotten past. Here lies gods who have been silent all too long." — footer "© 2001 The 3DO Company. All Rights Reserved." Same publisher, same domain, same era as the *Diaries of Archibald* the article accepts as real `T2`.
Found — counterexample 2, and the decisive one because it names the world, is on the official publisher's site, and **is a source the article already cites** (G-18/G-21): `mmh7.ubi.com`, verbatim — "Set on the  world of Axeoth, these two free bonus campaigns,  Unity  and  Every Dog Has His  Day , were written by Heroes IV's  master bard:  Terry B. Ray ."
Reason: Under this project's own tier table — "`T2` = official manual / official publisher website" — both pages are `T2` and both concern the Axeoth era; the second states the world's name outright. The claim is therefore false, and it is false against a page in the article's own source list. This is the negative-claim failure mode CLAUDE.md names as the most dangerous, "because it looks like caution". Fix: register both URLs and rewrite as *the Axeoth era has thin `T2` coverage — publisher marketing copy and a 2015 Ubisoft blog framing, with no `T2` narrative document comparable to Diaries of Archibald*. That weaker statement I could not refute. Two further Axeoth-era primaries the source inventory should carry even though they are not `T2`: `Lost Manuscripts` (Bullard's early-2000s backstory outlines, released 2017) and the `Jennifer Bullard/Acid Cave Interview`.

---

## Claim-table errors

Not article errors — defects in the claim table's own conventions and technical notes.

1. **"thelazy has no Heroes IV coverage — do not waste time there" is wrong, and it is the most costly line in the notes.** `heroes.thelazy.net` hosts `The Reckoning` (with an embedded HoMM IV intro video), `Lost Manuscripts` (Bullard's H4 backstory outlines), and `Jennifer Bullard/Acid Cave Interview` **with a dedicated `== Heroes of Might and Magic IV ==` section** — which is where the `bullard-interview-2013` material for G-32 actually lives, and where I found the error that blocks this article. A verifier obeying that instruction would have missed the BLOCKER.
2. **The thelazy URL form in the notes 404s.** `thelazy.net/wiki/<Page>` returns nginx 404. Correct: `https://heroes.thelazy.net/index.php/<Page>`, API `https://heroes.thelazy.net/api.php`. Separately, `thelazy.net` presents an untrusted certificate chain in this environment (`schannel: SEC_E_UNTRUSTED_ROOT`) — `curl -k` needed; the "0 bytes without a User-Agent" note misdiagnoses this as a UA problem.
3. **The Age of Heroes fetch recipe is incomplete.** The failure is not a "~2 KB wrapper" — `https://web.archive.org/web/<ts>/<url>` returns a **35 KB "Blocked" interstitial**. What works is the raw-content suffix plus a browser UA: `curl -sL -A "Mozilla/5.0 …" "https://web.archive.org/web/20070917000000id_/http://www.heroesofmightandmagic.com/heroes4/<page>.shtml"`. Also, `heroesofmightandmagic.com/heroes4*` times out the CDX endpoint (504); `.../heroes4/*` with `filter=original:.*shtml$` works.
4. **G-04's block attribution is wrong** (`Full Circle`, not `The Past`) — flagged under G-04; if the compiler added the block names, the error is the table's.
5. **G-21 is mis-scoped**, bundling Ubisoft's editorial epithet and the page date under a `T4` developer label — see G-21.

---

## Kết luận

**Bài này CHƯA đạt `status: verified`.** Điều kiện là không còn `BLOCKER` và không còn `MAJOR`; hiện còn **1 BLOCKER và 5 MAJOR**.

**Phải sửa trước khi verified:**

1. **G-32 — BLOCKER.** Bullard nói "the planet **after** the Reckoning" (tức Axeoth, hành tinh mới), **không** phải "hành tinh cũ". Bài đã đảo ngược lời một nguồn `T4` rồi gắn nhãn `EXPLICIT`. Kết luận cuối (nghiêng về game text) vẫn đúng, nhưng tiền đề phải viết lại: *Bullard đặt Kalibarr ở thế giới hậu-Reckoning, bị Demons bắt đưa tới; game text đặt ông ở một cõi demon riêng, tới bằng cổng phép.*
2. **G-42 — MAJOR.** "Không có nguồn `T2` chính thức cho thời Axeoth" là **sai**, và phản ví dụ nằm ngay trong danh sách nguồn của chính bài: trang Ubisoft `mmh7.ubi.com` viết "Set on the world of Axeoth…", cộng thêm `3do.com/mightandmagic/heroes4/story.html` (© 2001 The 3DO Company). Hạ xuống thành "`T2` mỏng, không có văn bản tự sự ngang *Diaries of Archibald*".
3. **G-35 — MAJOR.** 1177 và 1178 **không** mâu thuẫn: 1177 là ngày xảy ra sự kiện (02-04-1177 + "six days later"), 1178 là ngày Lysander *chép lại* hồi ký. Bài đang buộc tội một nguồn về một lỗi nó không có. `Lost Manuscripts` đã fetch được — cập nhật thành `T6 INFERENCE` và nêu rủi ro thật: chính tài liệu tự ghi "might not be entirely canonical".
4. **G-21 — MAJOR (sai *loại* nguồn).** "Master bard" là văn quảng bá của nhà phát hành và `09/11/2015` là metadata trang → `T2`, không phải `T4`. Tách khỏi G-18/G-19/G-20 (những câu này Ray tự nói, `T4` đúng).
5. **G-23 — MAJOR (sai loại nguồn + sai trang).** Số liệu gameplay trên Age of Heroes là bảng do cộng đồng dựng, có ghi công "Thanks to Lich… for heroes data" → `T6`, và `T6` không được mang `EXPLICIT`. Ngoài ra **Gauldoth không có trên `heroes_necromancers.shtml`**; lớp của ông nằm ở `heroes_campaign.shtml`, dưới đề mục "Campaign Necromancers".
6. **G-14 — MAJOR.** "Giết druid Halas" **không** có trong transcript (3 lần nhắc Halas đều chỉ là lá thư cảnh báo); `fandom:Halas` còn nói thẳng "he is not represented by an in-game unit". Hạ xuống `INFERENCE` hoặc viết lại. Và Mardor là **Specter/spectral**, không phải "ghost" — theo quy ước giữ nguyên từ của game.

**Nên sửa (MINOR/NOTE, không chặn):** G-04 sai tên block (`Full Circle`); G-19 cắt câu giữa dòng, mất "but he sees the purpose and usefulness of power"; G-24 là claim phủ định chưa có nguồn (đã có sẵn hai câu Fandom để dẫn); G-41 sai cấu trúc (47 event + 9 quest, không phải 54 + 5; một quest thiếu `Progress`); G-26 nên nhắc `Basic Nature Magic` mà Fandom có; G-34 **phải** dẫn phát biểu của Ray về Necros trên `fandom:God of Death` — đây đúng là vết BH-3 tái diễn; G-36 nên nhắc mục `11-08-1178` được viết trên Axeoth; G-39 nên nói rõ tài liệu Fulton chỉ về HoMM3 nên việc thiếu Gauldoth không mang thông tin gì; G-11 nên phân biệt "không ăn thịt người" với "vô can về chuyện trẻ con" (block `Nekorrum` và Epilogue nói ngược lại).

**Những gì đứng vững sau khi bị tấn công thật:**
- **G-07 / G-08** — trụ cột thứ nhất **giữ nguyên**. Toàn bộ sáu câu trích đúng từng chữ, đúng block. Tôi tìm được **11** chỗ khẳng định phải=chết/trái=sống, nhiều hơn con số tám bài nêu, và **không có một chỗ nào ngược lại**. `T1* EXPLICIT` đúng.
- **G-27 / G-28 / G-29** — trụ cột thứ hai **giữ nguyên**, đã kiểm hai phía độc lập. Fandom thật sự dùng một `ref name=Family` duy nhất cho cả bốn quan hệ; nguồn được ref thật sự viết "**Not** like they were all from the same mother"; và câu hỏi của phóng viên thật sự mở bằng "the fact that…". Đây là phát hiện mạnh nhất của bài và nó đúng.
- **G-41 (câu hỏi tier)** — `h4-death-texts-ch` là **text gốc trong game**, không phải bản diễn giải của fan: 89,002 byte khớp tuyệt đối, lỗi chính tả của bản phát hành còn nguyên ("far stronger **that** it appears"), chuỗi biography trùng khít với bản Age of Heroes và Fandom dựng lại độc lập. **Bài đứng trên `T1*`, không phải `T6`.**
- **Không có câu trích nào bị bịa.** Mọi câu bài gán cho transcript và cho Terry Ray đều lấy lại được nguyên văn. Sau vụ bịa nguồn gần đây, đây là kết quả cần ghi nhận rõ.

Nói gọn: nền tài liệu của bài lành mạnh và hai phát hiện gốc đều thật. Sáu lỗi phải sửa hầu hết là **lỗi nhãn nguồn và lỗi claim phủ định**, và ba trong số đó (G-32, G-35, G-42) đều cùng một hình dạng: bài khẳng định một nguồn khác sai, hoặc khẳng định một nguồn không tồn tại, mà không kiểm tới cùng. Đúng như CLAUDE.md đã ghi — loại lỗi này nguy hiểm nhất vì **nó trông giống sự cẩn trọng**.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. BLOCKER và toàn bộ MAJOR đã xử lý.

### Áp V4 — tự dựng lại hai phát hiện đảo kết luận

| Phát hiện | Kết quả tự kiểm | |
|---|---|---|
| **G-42** — có nguồn `T2` chính thức cho Axeoth | Quét lại CDX **có filter**: `3do.com` có **58 trang sạch** mục `/mightandmagic/heroes4/`. Fetch `story.html` → *"© 2001 The 3DO Company. All Rights Reserved."* | ✅ **XÁC NHẬN** |
| **G-32** — bài đọc ngược lời Bullard | Nguyên văn: *"Kalibarr was held on **the planet after the Reckoning**"*, và câu hỏi đối lập nó với *"a different planet conquered by Kreegans"* → chỉ thế giới **mới** | ✅ **XÁC NHẬN** |

⚠️ **Vì sao lần quét CDX đầu của người viết báo âm:** nó chỉ thử ba path (`3do.com/heroes4*`,
`/games/heroes4*`, `/products/pc/heroes4*`) và một lần `limit=4000` **không filter** rồi grep — bị cắt
trước khi tới `/mightandmagic/heroes4/`. **Đường dẫn đúng có thêm một tầng.** Đây là lý do `B-023`
được dựng trên một kết quả âm sai.

### Bảng xử lý

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| G-32 | Bài **đọc ngược** một nguồn `T4` rồi dựng điểm `DISPUTED` không tồn tại | **BLOCKER** | Viết lại cả mục: trích **cả câu hỏi và câu trả lời** để cho thấy "the planet after the Reckoning" nghĩa là Axeoth. Nêu rõ **không có tranh chấp** — Bullard và game text **cùng** đặt Kalibarr ở Axeoth. Ghi lại rằng kết luận cũ tình cờ đúng nhưng **lý do thì sai** |
| G-42 | "Axeoth không có nguồn `T2`" | MAJOR | Sửa thành: **có** `T2` (58 trang 3DO, `© 2001 The 3DO Company`) — **nhưng không nguồn `T2` nào phủ Gauldoth** (`story.html` chỉ ~630 ký tự, không nhắc Axeoth/Reckoning/Gauldoth). Thêm key `h4-official-3do-story`. Ghi rõ đường dẫn đúng là `/mightandmagic/heroes4/` |
| G-35 | Tự dựng ra mâu thuẫn 1177 vs 1178 | MAJOR | **Đóng câu hỏi mở.** Hai con số nói về hai việc: 1177 = năm sự kiện, 1178 = năm Lysander viết hồi cố. Ghi nhận đây là **cùng lỗi** với mục *Succession Wars* ở bài `archibald-ironfist` — đọc hai con số cạnh nhau mà không đọc chúng nói về cái gì |
| G-23 | Sai **cả trang lẫn tier** | MAJOR | Gauldoth **không có** trên `heroes_necromancers.shtml` (trang đó liệt kê 26 Necromancer thường, kể cả Sandro). Đổi sang `heroes_campaign.shtml`. Và hạ `T1*` → `T6`: số liệu class là bảng **do cộng đồng biên soạn** — trang tự ghi công *"Thanks to Lich… for heroes data"*. Bỏ key `aoh-h4-heroes-necromancers` khỏi bài |
| G-14 | "Diệt druid Halas" **không có trong transcript** | MAJOR | Bỏ hẳn. Ba lần nhắc Halas đều chỉ là **lá thư cảnh báo**; và `fandom:Halas` còn nói ông "is not represented by an in-game unit". Cũng sửa Mardor: **Specter**, không phải ghost |
| G-21 | "master bard" + ngày đăng là văn biên tập Ubisoft | MAJOR | Tách tier: văn Ubisoft = `T2`, **chỉ lời của Ray** mới là `T4` |
| G-08 | Đếm thiếu | MINOR | 8 → **11 chỗ**, và ghi rõ **không có chỗ nào ngược lại** |
| G-41 | Đếm sai số block | MINOR | 54 + 5 → **47 block sự kiện + 9 quest** (một quest thiếu `Progress`); 89.002 byte là **chính xác** |
| G-34 | **BH-3 tái diễn** | NOTE→sửa | Bài viết "không được gán tên từ nguồn ngoài" mà **chưa tìm** nguồn ngoài. Ray có nói: *"So, **Necros could certainly be the God of Death**."* Đã thêm, kèm lưu ý chữ "could certainly be" là **tự rào**, không phải xác nhận |

### Điều verifier xác nhận đứng vững

Hai phát hiện gốc của bài **đều giữ**, và một cái được củng cố:

- **G-07 / G-08** — cơ chế half-dead là game text tường minh: cả sáu trích dẫn đúng nguyên văn, đúng
  block. Verifier tìm được **11** chỗ xác nhận phải=chết/trái=sống thay vì 8, và **0 chỗ ngược lại**.
- **G-27 / G-28 / G-29** — Fandom đọc quá nguồn ở phần dòng dõi: verifier kiểm **cả hai phía** và
  xác nhận Fandom thật sự dùng **một** `ref name=Family` cho cả bốn quan hệ, Ray thật sự nói *"**Not**
  like they were all from the same mother"*, và người phỏng vấn thật sự mở bằng "the fact that…".
- **G-41** — tier `T1*` **đúng**: transcript giữ cả lỗi in gốc (*"far stronger **that** it appears"*),
  dấu hiệu bản chép trung thực.

**Không có trích dẫn nào bị bịa** — verifier lấy lại được nguyên văn mọi câu gán cho transcript và
cho Ray.

### Lỗi của bảng claim, không phải của bài

Ghi theo `VERIFY-PROTOCOL.md` mục 7:

⚠️ **"thelazy không phủ Heroes IV — đừng mất thời gian ở đó" là SAI, và nó gần như làm mất BLOCKER.**
Mục `== Heroes of Might and Magic IV ==` của bài phỏng vấn Bullard **nằm trên thelazy**. Người soạn
bảng claim suy từ "thelazy không có trang `Gauldoth_Half-Dead`" thành "thelazy không có gì về H4" —
**đúng loại suy luận từ im lặng** mà chính dự án cấm.

Hai chi tiết kỹ thuật bảng claim ghi thiếu: URL thelazy phải dạng `heroes.thelazy.net/index.php/`
(dạng khác 404), và Age of Heroes cần **suffix `id_`** + UA trình duyệt, không thì trả trang "Blocked"
35 KB.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-gauldoth-half-dead-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.
