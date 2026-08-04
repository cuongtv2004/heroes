# Verify report: tarnum — 2026-08-03

Verifier: independent agent, did not read the article
Claims checked: 32
CONFIRMED: 26 | DOWNGRADE: 3 | NOT_FOUND: 0 | CONTRADICTED: 3

BLOCKER: 1 (T-24) · MAJOR: 5 (T-01, T-03, T-22, T-28, T-29) · MINOR: 5 · NOTE: rest

All quotes below were retrieved during this session. Where a quote is reproduced from
raw wikitext, wiki markup has been stripped or the string is fenced; nothing is
reconstructed from memory.

---

## Details

### T-01
Claim: Tarnum is protagonist of all eight Heroes Chronicles campaigns, and the only Old
Universe character with six different classes.
Label in article: unlabelled in summary; sourced in Gameplay — `h3wiki-tarnum`
Verdict: **DOWNGRADE**
Severity: **MAJOR** (conditional — see Reason)
Searched:
- `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw`
- `https://mightandmagic.fandom.com/api.php?action=parse&page=Tarnum&prop=wikitext&format=json&formatversion=2`
Found (part A, thelazy, opening line):
> "'''Tarnum''' is the main hero throughout the eight campaigns of the Heroes Chronicles."

Found (part B, Fandom, `== Trivia ==`):
> "He is the only character in ''Heroes of Might and Magic'' series to have 6 different classes."

Reason: Part A is solidly supported (and independently corroborated — see T-16). Part B,
the **exclusivity** claim, rests on a single **uncited Trivia line on Fandom** — a `T6`
source, which by project rule can never support `EXPLICIT`. I found no `T1`/`T1*`/`T2`/`T4`
statement of exclusivity anywhere. It must carry `T6 UNVERIFIED` (or `FAN_THEORY`) and be
attributed to Fandom in the body, not asserted bare in the summary. **If the Gameplay
section already labels it `T6 UNVERIFIED`, downgrade this finding to NOTE**; if it is
labelled anything stronger, or if the summary states it without hedge, it is a MAJOR.

---

### T-02
Claim: What defines Tarnum is *why* he is immortal — he was a tyrant, the Ancestors refused
him Paradise, and keep him alive as their servant until he redeems himself.
Label in article: unlabelled in summary — `hc-tunnels-of-ice`
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=Tunnels_of_Ice&action=raw`
- `https://heroes.thelazy.net/index.php?title=Warlords_of_the_Wasteland&action=raw`
- `https://web.archive.org/web/20010410194637/http://www.3do.com/products/pc/chronicles/main.html`
Found (Tunnels of Ice, Day 24 timed event):
> "Finally, I told him how I died, and how the Ancestors refused to allow me to enter Paradise."
> "I do what they ask - I am their servant until I can redeem myself."

Found (Warlords of the Wasteland prologue, The Historian):
> "Upon his death, he entered the legendary hall of judgment, to stand before the ancient
> council. There, the ancestors found him unworthy of entering paradise, so they cast him
> back among the mortals"

Found (3DO official site, `main.html`, "The Epic Tales of Tarnum, the Immortal Hero"):
> "Judged by the Ancestors to be unworthy to enter Paradise"
> "Seeking redemption for the crimes of his bloody past"
> "Tarnum is sent on a succession of quests"

Reason: Triply supported — `T1*` game text (two independent scenarios) plus `T2` official
3DO copy. This is one of the strongest claims in the table. Note the article may upgrade
its confidence here: the 3DO page gives a genuine `T2 EXPLICIT` anchor for the summary.

---

### T-03
Claim: His own act of mercy caused The Reckoning.
Label in article: unlabelled in summary; sourced later — `hc-the-protectors-of-the-sword`
Verdict: **DOWNGRADE**
Severity: **MAJOR**
Searched: `https://heroes.thelazy.net/index.php?title=The_Protectors_of_the_Sword&action=raw`
Found (campaign-8 epilogue, verbatim):
> "Then he prayed, "Ancestors, please don't let my compassion destroy the world!""

Reason: Game text has Tarnum **fearing** that his compassion will destroy the world — it
never states that it did. The completion of the chain (Kija → Kilgor → Gelu → Reckoning)
is inference across three pages, and the article itself labels that chain `T1* INFERENCE`
at T-15. A bald unlabelled causal assertion in the summary therefore **states an
INFERENCE as fact**, which violates the two-axis labelling rule. Fix: hedge the summary
("hành động khoan dung của ông là mắt xích đầu tiên trong chuỗi dẫn tới The Reckoning")
and carry the `INFERENCE` label up from T-15.

---

### T-04
Claim: The campaign-1 description is game text (campaign-select screen), not wiki prose.
Label in article: `T1* EXPLICIT` — `h3wiki-heroes-chronicles`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: `https://heroes.thelazy.net/index.php?title=Warlords_of_the_Wasteland&action=raw`
Found (the `| description =` field, verbatim, glossary templates expanded):
> "Before Tarnum became the Immortal Hero, he was a Barbarian who threw off the shackles
> of his Wizard masters and returned his people to their former greatness. This is his
> tale, and his downfall."

Reason: Verbatim match including the load-bearing final sentence. On the provenance
question the article is right, and I can show *why*: the template keeps `description`
and `information` as **separate fields**, and `information` is unmistakably wiki prose
("It was sold as a stand-alone game using the Shadow of Death version of the engine…"),
while `description` is not. Decisive corroboration comes from the scenario-level
`description` fields, which contain pure in-game selection-screen content — e.g. Truth
Within Nightmares: "All Heroes are limited to level 18, but Tarnum and two of his best
Captains will transfer over to the next scenario." Wiki editors do not write level caps
in the second person. `T1*` is correct.

NOTE: the source key is wrong. This text is on the **Warlords of the Wasteland** page,
not on `Heroes_Chronicles`. Same issue at T-19.

---

### T-05
Claim: He began as a Barbarian rebelling against the wizard empire Bracaduun; his title in
that period was Barbarian Tyrant.
Label in article: `T1* EXPLICIT` — `h3wiki-tarnum`
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=Revolt_of_the_Beastmasters&action=raw`
- `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw`
- `https://heroes.thelazy.net/api.php?action=query&list=backlinks&bltitle=Bracaduun&bllimit=60&format=json`
Found ("Barbarian Tyrant" — **in-game** campaign description of Revolt of the Beastmasters):
> "Tarnum was the first to drag the Mudlanders into slavery when he was the Barbarian
> Tyrant. Now he has the chance to make amends and lead these people to freedom."

Found (the alias row of the Tarnum class table, Barbarian column): `King Tarnum`,
`Barbarian King`, `Barbarian Tyrant`.

Reason: "Barbarian Tyrant" is better sourced than the article claims — it is not merely a
wiki alias row, it is verbatim in an in-game campaign description, so `T1* EXPLICIT` holds
and the source key can be upgraded to the ROTB campaign page. "Bracaduun" is confirmed to
be in-game vocabulary: the backlinks query returns the Chronicles scenario pages
`A Barbarian King`, `The Criminal King`, `The War for the Mudlands`,
`Siege of the Wallpeaks`, `Trapped!`, `Steelhorn`, `Truth Within Nightmares`,
`Never Deal with a Demon`, `The Magic that Binds`, `The World Within`, `Hopewielder`,
`By Royal Decree` — i.e. it occurs inside transcribed scenario text, not only in editor
prose. NOTE: the article omits "Barbarian King", the third alias in the same cell.

---

### T-06 ⚠️ load-bearing
Claim: The immortality mechanic has explicit game text, located in `=== Timed events ===`
of `Tunnels of Ice` (The Sword of Frost) — **not** prologue/epilogue. Day 23 quotes.
Label in article: `T1* EXPLICIT` — `hc-tunnels-of-ice`
Verdict: **CONFIRMED**
Severity: NOTE (dash/spacing only)
Searched: `https://heroes.thelazy.net/index.php?title=Tunnels_of_Ice&action=raw`
Found (Day 23 row, inside `=== Timed events ===`, verbatim):
> "I am immortal, Ufretin. I am not just long-lived like the Elves and Dragons. I am
> immortal - I can't die!"
> "I was a fool once, a cruel one, and I've been paying for my brutality ever since. I
> will probably pay for it until the end of time."
> "Before Ufretin could respond, I plunged my unseen dagger deep into my own heart."

Reason: I attacked the **location** claim specifically, because that is what makes this
finding original. The page's section structure is: `== Prologue ==`, `== Scenario ==`,
`=== Timed events ===`, `=== Objects ===` (Towns / Heroes). There is **no
`== Epilogue ==` section on this page at all**, and the Prologue is three sentences of
Historian narration that never touch immortality. The immortality text sits exclusively in
the Day 23 and Day 24 timed-event rows. The article's location claim is correct and is a
direct instance of project lesson BH-1.

Two cosmetic discrepancies, both harmless but worth fixing so the quote is byte-exact: the
source uses a **hyphen** `-`, not an em dash, in "I am immortal - I can't die!" and in "I
do what they ask - I am their servant"; and the source separates sentences with **two
spaces**.

---

### T-07 ⚠️ load-bearing
Claim: Day 24 quotes — no scar, "You just stood back up", Ancestors refused Paradise,
"their servant until I can redeem myself".
Label in article: `T1* EXPLICIT` — `hc-tunnels-of-ice`
Verdict: **CONFIRMED**
Severity: NOTE (dash only)
Searched: `https://heroes.thelazy.net/index.php?title=Tunnels_of_Ice&action=raw`
Found (Day 24 row, verbatim):
> "I opened my shirt. There wasn't even a scar where I had stabbed myself."
> ""You just stood back up," the Dwarf said. "I watched it go in, I saw the blood myself,
> and then you just stood back up. How?""
> "Finally, I told him how I died, and how the Ancestors refused to allow me to enter Paradise."
> "I do what they ask - I am their servant until I can redeem myself. But they have never
> asked me to fight against my friends before."

Reason: All four fragments verified verbatim in the correct order in the same timed-event
row. Same hyphen-vs-em-dash note as T-06.

---

### T-08 ⚠️ load-bearing
Claim: The mechanic is NOT undead/lich/necromancy and NOT Ancients intervention — it is the
Ancestors (the Barbarian judging council) refusing him Paradise.
Label in article: table, sourced above — `hc-tunnels-of-ice`
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=Tunnels_of_Ice&action=raw`
- `https://heroes.thelazy.net/index.php?title=Ancestors&action=raw`
- `https://heroes.thelazy.net/index.php?title=Jennifer_Bullard/Acid_Cave_Interview&action=raw`
- `https://heroes.thelazy.net/index.php?title=Warlords_of_the_Wasteland&action=raw`
Found (Bullard, Acid Cave interview 2013 — a **`T4` developer statement that explicitly
separates the two**):
> "Ancestors were the biological start of the current crop of heroes. Ancients were often
> other powers who dabbled in the lives of mortals."
> "Think of the Ancestors as super powerful humans who have become legends to their
> descendants. … They had never been written into the Might & Magic Universe before the
> Heroes Chronicles."

Found ("judging council", Warlords of the Wasteland prologue):
> "he entered the legendary hall of judgment, to stand before the ancient council"

Found (H4 Might texts, Waerjak narrating):
> "When a Barbarian dies, they are forced to stand before the Ancestors to have their life
> judged. If they are found unworthy, they are cast into oblivion."

Reason: This is a **negative claim**, so I hunted for the opposite rather than inferring
from silence. Result: the negative survives, and is stronger than the article states. The
"not the Ancients" half is not merely absent from the text — it is **affirmatively denied
by the writer herself** in a `T4` source. The article should cite `bullard-interview-2013`
here; that turns an argument-from-silence into a positive `T4 EXPLICIT`.

The one thing I could **not** confirm is a "lich/undead Tarnum" being ruled out by text.
Related trap the article should be aware of: thelazy's `Heroes Chronicles` page carries an
`== Unofficial Content ==` section describing a **fan ERA mod**, "The Glory of War", in
which "Tarnum [is] reincarnated as an undead Death Knight by the Lich King Archon". That is
fanmade and clearly flagged as such on the wiki, but it is exactly the kind of passage a
future reader could mistake for canon. If the article asserts "not undead", it should name
and dismiss this mod explicitly.

---

### T-09
Claim: "Immortal" follows the character's own words, not the mechanic — he dies repeatedly
and returns; "I can't die" is Tarnum speaking, not narration.
Label in article: `T1* INFERENCE` — `h3wiki-tarnum` + `hc-tunnels-of-ice`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: as T-06, T-07, plus `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw`
Found: the Day 23 row is first-person journal in Tarnum's voice, addressed to Ufretin
("…I said."). The Deaths list on the Tarnum page enumerates six separate deaths. In H4:
"Vogel flung Tarnum's limp form into the ravine" followed later by his return.
Reason: The speaker attribution is correct and demonstrable, and the "dies and returns"
reading is exactly what the H4 texts show. `INFERENCE` is the right strength — the game
never defines the mechanism, only its effects.

---

### T-10
Claim: His most fully narrated death is after the Reckoning, on Axeoth, narrated by Waerjak.
Label in article: `T1* EXPLICIT` — `ch-h4-might-texts`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: `https://web.archive.org/web/20130209054746/http://www.celestialheavens.com/homm4/texts/H4-MightTexts.rtf`
(live URL `celestialheavens.com/homm4/texts/H4-MightTexts.rtf` returns **403**, as the claim
table warned; the archive copy downloads cleanly, 61 771 bytes, RTF v1)
Found, verbatim:
> "First, Vogel took a large mallet and shattered my father's knees. Then he did the same
> to Tarnum's arms. Those who watched agree that Tarnum never screamed. He gritted his
> teeth and writhed in agony, but he didn't give Vogel the satisfaction of a single scream."
> ""Wait 'til you meet the Ancestors.""
> "Those were my father's last words."
> "This time, however, Vogel flung Tarnum's limp form into the ravine."
> "Tarnum didn't scream. And as far as anyone knows, his body still lies down there, unburied."

Reason: Every fragment verified verbatim, in order, in the H4 Might (Waerjak) campaign
transcript. The article's ellipses elide only "Then he did the same to Tarnum's arms." and
"Tarnum didn't scream. And as far as anyone knows," — neither elision changes meaning.

---

### T-11
Claim: He returns; the Ancestors **offer** him Paradise and he **refuses**.
Label in article: `T1* EXPLICIT` — `ch-h4-might-texts`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: as T-10
Found, verbatim (Tarnum speaking to Waerjak):
> "They're not punishing me. In fact, everything you have done here has freed me from my
> debt. For my part in raising you, the Ancestors have offered me Paradise, but I turned
> them down."

Reason: Exact match. (My RTF de-control-word pass initially mangled "part" into "t" because
`\par` is an RTF control word; the underlying file reads "For my part in raising you". I
flag this so nobody mistakes it for a source discrepancy.)

---

### T-12
Claim: His final line in the whole series is "…This new world still needs heroes."
Label in article: `T1* EXPLICIT` — `ch-h4-might-texts`
Verdict: **CONFIRMED**
Severity: MINOR
Searched: as T-10; plus `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw`
Found, verbatim — and it is the **last text block in the file**:
> "Until now, I thought all I wanted was the opportunity to enter Paradise and rest, but I
> feel these people have become my community. And I don't just mean Barbarians, but
> Palaedrans and Elves and all the others. I've been protecting them for so long, I feel
> like I'll be letting them down if I leave.
> This new world still needs heroes."

Reason: Quote verbatim, position confirmed. **MINOR**: "final line in the whole series"
needs a scope qualifier. thelazy's own Tarnum page has a section
`=== Might & Magic: Heroes VII ===` stating "Tarnum appears in the 'Lost Tales of Axeoth:
Every Dog Has His Day' campaign", so he speaks again in a later-produced Old Universe
product. Say "câu thoại cuối của Tarnum trong H4 / trong mạch Chronicles–H4" rather than
"trong cả series".

---

### T-13
Claim: The only numeric lifespan anchor is "After more than a thousand years of life".
Label in article: `T1* EXPLICIT` — `ch-h4-might-texts`
Verdict: **CONFIRMED**
Severity: MINOR
Searched: as T-10
Found, verbatim (Waerjak's narration):
> "After more than a thousand years of life, why would Tarnum refuse that which he had been
> fighting for?"

Reason: Verbatim. Two refinements. (a) It is **Waerjak's rhetorical question**, not a
statement by Tarnum or a narrator of record — worth saying, since the article elsewhere is
careful about who speaks (T-09). (b) "The only" is very slightly overstated: eleven lines
later Tarnum says "For the first time in a thousand years, the Barbarian people have a
real chance at a good life!" That figure describes the Barbarian people, not his lifespan,
so the claim survives — but if the article says "duy nhất", scope it to "mốc duy nhất nói
về tuổi thọ của Tarnum".

---

### T-14 ⚠️ load-bearing
Claim: The Reckoning causal chain comes from the epilogue of campaign 8 — i.e. the epilogue
of all Heroes Chronicles.
Label in article: `T1* EXPLICIT` — `hc-the-protectors-of-the-sword`
Verdict: **CONFIRMED**
Severity: MINOR (meaning-changing ellipsis)
Searched:
- `https://heroes.thelazy.net/index.php?title=The_Protectors_of_the_Sword&action=raw`
- `https://heroes.thelazy.net/index.php?title=The_Sword_of_Frost&action=raw`
- `https://heroes.thelazy.net/index.php?title=Heroes_Chronicles&action=raw`
Found (`== Epilogue ==`, The Historian, verbatim and complete):
> "Tarnum's hard-fought victory over the City of Volee was for naught. When he reached the
> resting place of the Sword of Frost he found that someone had already chipped it from its
> icy sheath. Among the broken ice was a discarded Barbarian Axe. Tarnum closed his fist
> around its hilt and screamed the name of the thief.
> "Kija!"
> Why didn't he kill her when he held her captive?
> Then he prayed, "Ancestors, please don't let my compassion destroy the world!""

Reason: The **placement** claim checks out on two independent axes: `The Protectors of the
Sword` is the **eighth and last** map row on the `The Sword of Frost` campaign page, and
that campaign's `| information =` reads "The Sword of Frost is the **eighth episode** in
Heroes Chronicles". So this really is the closing epilogue of the whole series.

**MINOR but fix it:** the article's ellipsis deletes "Among the broken ice was a discarded
Barbarian Axe." That sentence is the antecedent of "**its** hilt". Without it, a reader
takes "its hilt" to mean the Sword of Frost's — i.e. that Tarnum held the sword. He does
not; he picks up the **axe**, and the axe is the clue that identifies the thief as a
Barbarian. Restore the sentence.

---

### T-15
Claim: Chain — captures Kija → spares her → she steals the Sword → gives it to Kilgor →
Kilgor meets Gelu → Reckoning → Enroth destroyed → refugees to Axeoth.
Label in article: `T1* INFERENCE` — `hc-the-protectors-of-the-sword` + `thelazy-the-reckoning`
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=The_Protectors_of_the_Sword&action=raw`
- `https://heroes.thelazy.net/index.php?title=The_Barbarian%27s_Wife&action=raw`
- `https://heroes.thelazy.net/index.php?title=The_Reckoning&action=raw`
Found (captivity + escape — Protectors, Day 27):
> "A messenger arrived this morning to inform me that the Barbarian King's wife, Kija,
> escaped from her Dungeon prison. … Even if she convinces Kilgor himself to search for
> the Sword of Frost, it will be too late."

Found (Kija↔Kilgor is **in-game**, not editor inference — The Barbarian's Wife, Day 15):
> "For the wife of Kilgor, King of the Barbarians, she's a powerful warrior. She may not be
> insane like her husband, but she is driven by her ambition and her taste for cruelty."

Found (the terminal event — The Reckoning page):
> "a massive explosion is created by the clash of Gelu's Armageddon's Blade and Kilgor's
> Sword of Frost, which in turn starts a chain of thousands of earthquakes and volcano
> eruptions."

Reason: Every link is attested; the single un-narrated step is the physical handover from
Kija to Kilgor, which is why `INFERENCE` — not `EXPLICIT` — is the correct label. The label
is right as written. Bonus: the Kija–Kilgor marriage does **not** need to lean on wiki
prose, it is stated in a timed event; the article can cite `hc-the-barbarians-wife` for it.

---

### T-16 ⚠️ load-bearing
Claim: **Six** classes, not eight — Barbarian repeats three times; full 8-campaign mapping.
Label in article: `T1* EXPLICIT` — `h3wiki-tarnum`
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw`
- the eight campaign pages on thelazy (`| information =` fields)
- Fandom `Tarnum` infobox
- `https://web.archive.org/cdx/search/cdx?url=3do.com/products/pc/chronicles*`
Found: I counted the class table's header row directly. It has exactly **six** class columns:
> `! Class` · `! Barbarian` · `! Knight` · `! Wizard` · `! Ranger` · `! Beastmaster` · `! Overlord`

Found (the table's `Campaigns` row, verbatim): Barbarian → "Warlords of the Wasteland /
The World Tree / The Fiery Moon"; Knight → "Conquest of the Underworld"; Wizard →
"Masters of the Elements"; Ranger → "Clash of the Dragons"; Beastmaster → "Revolt of the
Beastmasters"; Overlord → "The Sword of Frost".

Found (town alignment, each campaign's `| information =`): Stronghold / Castle /
"Tower / Conflux" / Rampart / Stronghold / Stronghold / Fortress / Dungeon.

Reason: **All eight mappings in the article, including every town, are correct.** Three
independent corroborations, which matters because a bare wiki table is thin support for a
`T1*` label:
1. Fandom's infobox encodes the same thing with campaign icons — Barbarian `HC1 HC5 HC6`,
   Knight `HC2`, Wizard `HC3`, Ranger `HC4`, Beastmaster `HC7`, Overlord `HC8`.
2. thelazy's `Heroes Chronicles` page prose: "a Barbarian warlord who becomes a knight, a
   wizard, a ranger, a beastmaster, and an overlord".
3. **`T2` official**: the 3DO Chronicles site hosts exactly six Tarnum art pages —
   `tarnumbarbarian.html`, `tarnumknight.html`, `tarnumwizard.html`, `tarnumranger.html`,
   `tarnumrevolt.html`, `tarnumsword.html`. Six, for eight campaigns.

NOTE on tier: the class table itself is a wiki compilation, so `T1*` is generous in kind;
but the underlying facts (hero class, specialty strings, starting skills) are game data and
the specialty descriptions in the table are verbatim in-game strings. I would keep `T1*`
and add corroboration (3) as a second source key — that converts the weakest part of the
label into the strongest.

---

### T-17
Claim: Each class carries its own title — King Tarnum / Barbarian Tyrant, Sir Tarnum, Lord
Tarnum, Tarnum Dragonfriend, Tarnum Hopewielder, Overlord Tarnum.
Label in article: `T1* EXPLICIT` — `h3wiki-tarnum`
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw` (alias row + manual letters)
- `https://heroes.thelazy.net/index.php?title=Hopewielder&action=raw`
- `https://heroes.thelazy.net/index.php?title=Tunnels_of_Ice&action=raw`
- `https://heroes.thelazy.net/index.php?title=The_Protectors_of_the_Sword&action=raw`
Reason: I did not accept the alias table alone; I hunted each title in text.
- **Sir Tarnum / Lord Tarnum / Tarnum Dragonfriend** — signatures on the manual letters
  reproduced on the Tarnum page ("Your Humble Servant, Sir Tarnum"; "Sincerely, Lord
  Tarnum / The Immortal Hero"; "Sincerely, Tarnum Dragonfriend / The Immortal Hero").
  These come from the printed game manuals, i.e. `T2`, which is *stronger* than `T1*`.
- **Tarnum Dragonfriend** also in game text — Tunnels of Ice Day 2: ""Tarnum
  Dragonfriend!" … That was my Elven name."
- **Tarnum Hopewielder** in game text — Revolt of the Beastmasters, scenario `Hopewielder`,
  the Witch's dialogue: "My people are strangers to hope, Tarnum Hopewielder. Proceed with
  care!"
- **Overlord Tarnum** in game text — The Protectors of the Sword, Quest Guard: ""You're
  Overlord Tarnum, aren't you?" the Harpy asks."
- **Barbarian Tyrant** — see T-05, in-game campaign description.
All six survive. NOTE: the article omits "Barbarian King", the third Barbarian-column alias.

---

### T-18
Claim: The listed order is release order, not chronological order.
Label in article: unlabelled — no source key
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=Heroes_Chronicles&action=raw`
- `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw`
- `https://heroes.thelazy.net/index.php?title=Clash_of_the_Dragons&action=raw`
Found: the campaign pages number themselves "first / second / third / fourth / fifth /
sixth / seventh / eighth episode", in the article's order, and the `Heroes Chronicles` page
ties that order to how they shipped ("WOTW, COTU, MATE, and COTD were sold independently.
TWT was a free download… ROTB and TSOF were bundled together as 'The Last Chapters'.").
Decisively, thelazy's own Tarnum page lists the **Story** sections in a *different*
order — Warlords, Conquest, **Revolt of the Beastmasters**, Masters, World Tree, Fiery
Moon, Clash, Sword of Frost — i.e. the wiki itself distinguishes narrative order from
episode order. And `Clash of the Dragons` carries an explicit chronology note:
> "Chronologically, it happens after Dragon's Blood from Armageddon's Blade."

Reason: Correct as stated. It is `T6 INFERENCE` in strength (the wiki nowhere says the word
"release order"); the claim being unlabelled is acceptable only if it is framed as an
editorial note about the article's own table rather than a claim about the games. Given
T-21 (Bullard: no fixed order), this claim is also doing real work and deserves a label.

---

### T-19
Claim: Class changes are narrative, not mechanical — campaign 3's description says Tarnum
must face his prejudice against magic.
Label in article: `T1* EXPLICIT` — `h3wiki-heroes-chronicles`
Verdict: **CONFIRMED**
Severity: NOTE (wrong source key)
Searched: `https://heroes.thelazy.net/index.php?title=Masters_of_the_Elements&action=raw`
Found (the `| description =` field, verbatim):
> "Tarnum must face down his own prejudice against magic and become a Wizard if he has any
> chance of saving the world from the destructive Elemental Lords."

Reason: Verbatim match. NOTE: the text is on the **Masters of the Elements** page, not on
`Heroes_Chronicles`; the source key needs correcting (same defect as T-04). Supporting
material for the "narrative not mechanic" reading is on the campaign's prologue, also game
text: "So why did the Ancestors call on a Barbarian who hates magic to save us all?"

---

### T-20
Claim: Tarnum is the only character with six classes, per Fandom.
Label in article: cited as reason not to change schema — `fandom-tarnum`
Verdict: **CONFIRMED** (as an accurate report of what Fandom says)
Severity: NOTE — but see T-01
Searched: `https://mightandmagic.fandom.com/api.php?action=parse&page=Tarnum&prop=wikitext&format=json&formatversion=2`
Found (`== Trivia ==`, verbatim):
> "He is the only character in ''Heroes of Might and Magic'' series to have 6 different classes."

Reason: The attribution is exact. What Fandom says, Fandom says. Two cautions: the line is
**uncited on Fandom**, and Fandom's scope is "Heroes of Might and Magic series" whereas the
article narrows it to "Old Universe" — the narrowing is safe, but it means the article is
no longer quoting, it is paraphrasing. Keep the claim attributed and at `T6`; see T-01 for
the label consequence.

---

### T-21 ⚠️ load-bearing
Claim: Bullard says the campaigns have no fixed chronological order.
Label in article: `T4 EXPLICIT` vs `T6 INFERENCE` — `bullard-interview-2013` + `h3wiki-heroes-chronicles`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: `https://heroes.thelazy.net/index.php?title=Jennifer_Bullard/Acid_Cave_Interview&action=raw`
(page header: "This interview was conducted in 2013 by Alchemik for Acid Cave."; original
at `https://www.acidcave.net/jennifer_bullard_interview.html`)
Found, verbatim, closing sentence of the answer:
> "Each one was supposed to take place in 'the distant past' and we didn't create a specific
> order to their events."

Reason: The attributed fragment is real, in context, and the 2013 date in the source key is
confirmed on the page itself. NOTE on tier hygiene: this is a developer statement reached
**through a wiki transcription of a third-party site**. It is genuinely `T4` in kind, but
`REGISTRY.md` should record the acidcave.net original as the primary and thelazy as the
accessible mirror, so a future reader is not surprised that a `T4` key resolves to a wiki URL.

---

### T-22 ⚠️ load-bearing
Claim: Two `T4` sources both claim authorship of Chronicles — Ray vs Bullard.
Label in article: `T4 EXPLICIT` (both) — `ray-interview-ubisoft-2015` + `bullard-interview-2013`
Verdict: **DOWNGRADE**
Severity: **MAJOR**
Searched:
- `https://web.archive.org/web/20151020063103/http://mmh7.ubi.com/en/blog/post/view/lost-tales-q-a-with-terry-ray`
- `https://heroes.thelazy.net/index.php?title=Jennifer_Bullard/Acid_Cave_Interview&action=raw`
Found (Terry Ray, verbatim — quote is real, I retrieved it):
> "All told, I was hired to work on Heroes IV, but also wrote the Heroes III Chronicles
> series. I wrote for other games produced by 3DO too. It was a really busy time but I
> remember it fondly."

Found (Bullard, verbatim, **with the sentence the article omits**):
> "Jon Van Caneghem was not involved in the Heroes Chronicles series - In fact I did a
> majority of the work myself."
> "Each original story & maps was written by one level designer and then I cleaned and
> polished them until ship."

Reason: **Both quotes are genuine** — nothing fabricated here. But the framing is wrong,
and the omitted sentence is what breaks it. Bullard's "majority of the work myself" is the
answer to a question about **Jon Van Caneghem's** involvement, not a claim to sole
authorship; and in the same answer she states that the original stories were written by
level designers whom she then edited. Terry Ray describing himself as having "wrote the
Heroes III Chronicles series" is precisely the role Bullard describes. The two statements
are **complementary, not contradictory**. Presenting them as a canon dispute manufactures a
conflict that the sources do not support.

Fix: either drop the claim from *Canon disputes*, or restate it as what it actually is —
two developers describing a division of labour (designers drafted, Bullard edited and
shipped), with Ray as one of those writers. If the article keeps a dispute framing, it must
quote Bullard's "Each original story & maps was written by one level designer" alongside.

Corroboration found while checking, worth adding to the article's Trivia: thelazy's Tarnum
page says "*Tarnum* was originally the name of Terry Ray's *Dungeons & Dragons* character",
and Ray confirms it himself in the same interview — "Tarnum from the Heroes Chronicles
series is a close second. He is my Crag Hack, my very first D&D character that I brought to
life in many tales." That upgrades a `T6` trivia line to `T4 EXPLICIT`.

---

### T-23 ⚠️ load-bearing
Claim: 3DO official says "interconnected storylines"; Bullard says they "stand alone…
without any reference to each other".
Label in article: `T2 EXPLICIT` + `T4 EXPLICIT` — `chronicles-official-3do` + `bullard-interview-2013`
Verdict: **CONFIRMED**
Severity: MINOR
Searched:
- `https://web.archive.org/web/20010410194637/http://www.3do.com/products/pc/chronicles/features.html`
- `https://heroes.thelazy.net/index.php?title=Jennifer_Bullard/Acid_Cave_Interview&action=raw`
Found (3DO `features.html`, first bullet, verbatim and complete):
> "A unique new series from the creators of Might and Magic® -- four games of challenge and
> exploration with interconnected storylines"

Found (Bullard, verbatim, complete sentence):
> "So I was asked to create 8 campaigns that could stand alone and be played in any order,
> without any reference to each other or the other products in development."

Reason: Both halves retrieved; both attributed correctly. **MINOR, two qualifiers the
article should carry.** (a) 3DO says "**four** games", not eight — this is early-2001
marketing copy written when only Warlords, Conquest, Masters and Clash existed, so it
cannot be read as a statement about the whole series. (b) It sits on `features.html`, a
bullet list of selling points, not on a story or lore page. The tension with Bullard is
real and belongs in *Canon disputes*, but it is marketing copy versus a designer's
recollection — not two canon authorities. Quote the "four games" clause in full.

---

### T-24 ⚠️ load-bearing
Claim: "Tarnum killed Sandro" **cannot be concluded** — because (1) the scenario has no
Epilogue, (2) no timed event after Day 1 mentions Sandro, (3) thelazy's Sandro page hedges
with "probably".
Label in article: `T1* INFERENCE` — `hc-truth-within-nightmares`
Verdict: **CONTRADICTED**
Severity: **BLOCKER**
Searched:
- `https://heroes.thelazy.net/index.php?title=Truth_Within_Nightmares&action=raw`
- `https://heroes.thelazy.net/index.php?title=Conquest_of_the_Underworld&action=raw`
- `https://heroes.thelazy.net/index.php?title=Sandro&action=raw`

**Sub-claim (1) — CONFIRMED.** The page's complete section list is `== Prologue ==`,
`== Scenario ==`, `=== Timed events ===`, `=== Objects ===`, `==== Events ====`,
`==== Towns ====`, `===== Town timed events =====`, `==== Heroes ====`,
`==== Monsters ====`, `==== Seer's Huts ====`, `==== Quest Guards ====`,
`==== Artifacts ====`, `==== Resources ====`. There is **no `== Epilogue ==`**.

**Sub-claim (2) — CONFIRMED.** "Sandro" occurs six times on the page: the `| description =`
field, the `| victory =` field, twice in the Day 1 timed event, once in a map Event at
`8, 46, 0`, and once in the Heroes table. The timed-event rows run Day 1, 4, 6, 9, 11, 14,
18, 22, 27, 31, 35, 39, 43, 47, 51, 55, 60, 62, 66, 68, 71, 72, 79, 85 — and **none after
Day 1 mentions Sandro**. The last five rows are entirely about Allison.

**Sub-claim (3) — mischaracterised.** The word "probably" is present, but it hedges the
wrong thing, and the article stops one sentence too early. Verbatim, thelazy `Sandro`,
`=== Historical counterpart ===`:
> "A character named Sandro was defeated by Tarnum's Erathian forces in the Underworld.
> Although represented by Sandro in-game, he is probably only a namesake, since according
> to Ethric and Jeddite, their Sandro became a necromancer decades before the Restoration
> Wars, and those events happened centuries prior. **Also, the scenario description strongly
> hints that Tarnum killed the Underworld Sandro.**"

"Probably" qualifies whether this Sandro is the *same character* as the Shadow of Death
Sandro. It does **not** hedge the killing — the very next sentence asserts the opposite of
what the article uses the page for.

**The conclusion is refuted.** The scenario's `| description =` field reads, verbatim:
> "Tarnum must kill Sandro to get the key to the next level. All Heroes are limited to level
> 18, but Tarnum and two of his best Captains will transfer over to the next scenario. The
> Sword of Judgement will also carry over to the next scenario. Tarnum, of course, must not
> die."

Reason: This is a **BLOCKER for an internal-consistency reason, not merely an evidentiary
one.** At T-04 and T-19 the article treats the `| description =` field as in-game text and
labels it `T1* EXPLICIT`. If that is true — and I verified that it is — then "Tarnum must
kill Sandro" is in-game text stating the killing, and the article cannot simultaneously
claim no game text supports it. The article uses one field as `T1* EXPLICIT` in one section
and silently ignores the same field in another. Either the negative claim goes, or T-04 and
T-19 lose their tier.

What survives and is worth keeping: sub-claims (1) and (2) are genuine, verified findings.
The defensible version of this claim is narrower — *no narrative game text depicts or
confirms Sandro's death; the only textual support is the objective line "Tarnum must kill
Sandro", which states a **goal**, not an outcome, and the identity of this Sandro is
disputed on thelazy.* That is a real and interesting `T1* INFERENCE`. "Cannot be concluded"
is not.

**Second, independent error in this claim — genealogy.** The claim table describes the
scenario's real content as "Tarnum realising Allison is **his own descendant**". Game text
says the opposite relation, repeatedly and explicitly. Day 71: "by the time Gryphonheart
formed the Kingdom of Erathia my sister was pregnant with their first child - **my niece,
Allison**." Day 85: "I would love to embrace her as **my niece**." Allison is his sister's
daughter — his **niece**, not his descendant. This sits in the compiler's unquoted prose,
so it may be a **claim-table error**; but if the word "descendant" (hậu duệ) appears in the
article, it is a second BLOCKER and must become "cháu gái (con của chị/em gái)".

---

### T-25
Claim: The `== Deaths ==` list has six entries, is uncited, three match game text, two are
unchecked, one is hedged "Possibly".
Label in article: `T6 FAN_THEORY` — `h3wiki-tarnum`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw`
Found: exactly **six** bullets, no references anywhere in the section, and the third reads:
> "Possibly slain with his army on The Fiery Moon during an assault by Vorr, the insane Ancestor."

Reason: Count, absence of citations, and the "Possibly" hedge all verified. `T6 FAN_THEORY`
is the correct label. For the record, of the six I independently confirmed two in game text
during this pass — the Ufretin self-stabbing (Tunnels of Ice Day 23) and the Vogel
Backbreaker killing (H4 Might texts) — consistent with the article's "three match".

---

### T-26
Claim: Fandom calls Waerjak his "son"; game text says "foster father" throughout; the only
time Tarnum calls him son is near the very end.
Label in article: `T6 FAN_THEORY` + `T1* EXPLICIT` — `fandom-tarnum` + `ch-h4-might-texts`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: Fandom API (`page=Tarnum`); H4-MightTexts.rtf via archive
Found (Fandom infobox, verbatim): `|relatives =[[Waerjak]] - son` — and in the scenario
list, "Tarnum teaches his son about the barbarian culture".
Found (H4 Might texts): "foster father" occurs **17 times** in Waerjak's narration —
e.g. "Waerjak and his foster father, Tarnum"; "My foster father insisted that I know how to
read"; "Tarnum had been much more than a foster father and a teacher."
Found (the closing beat, verbatim):
> ""Just be satisfied that I am here now," he said … "I am proud of you, son.""
> "That was the first time Tarnum called me son. I almost wept."

Reason: All three parts hold, and the "only time" is stated by the text itself rather than
inferred. One nuance the article should not trip over: earlier, at the reveal, **Waerjak**
refers to himself as Tarnum's son — "I felt betrayed because Tarnum hadn't shared this
secret with me, his son." That is Waerjak's own phrasing about himself, not Tarnum
addressing him, so the claim is intact — but a future reader grepping for "son" will hit it
and should be told why it does not count.

---

### T-27
Claim: Celestial Heavens has six `H4-*Texts.rtf` files plus H1 and H2, but **no** Chronicles
transcript file.
Label in article: unlabelled, Open questions — no source key
Verdict: **CONFIRMED**
Severity: NOTE
Searched (CDX, with a control query run first — see Reason):
- `https://web.archive.org/cdx/search/cdx?url=celestialheavens.com/homm4/texts/*&fl=original&collapse=urlkey`
- `https://web.archive.org/cdx/search/cdx?url=celestialheavens.com&matchType=domain&fl=original&collapse=urlkey&filter=urlkey:.*rtf.*`
Found — the **complete** archived `.rtf` inventory of the domain:
```
http://www.celestialheavens.com/homm1/texts/H1-Texts.rtf
http://www.celestialheavens.com/homm2/texts/H2-Texts.rtf
http://www.celestialheavens.com/homm4/texts/H4-ChaosTexts.rtf
http://www.celestialheavens.com/homm4/texts/H4-DeathTexts.rtf
http://www.celestialheavens.com/homm4/texts/H4-LifeTexts.rtf
http://www.celestialheavens.com/homm4/texts/H4-MightTexts.rtf
http://www.celestialheavens.com/homm4/texts/H4-NatureTexts.rtf
http://www.celestialheavens.com/homm4/texts/H4-OrderTexts.rtf
http://www.celestialheavens.com/homm4/usefulfiles/howtouseh4util.rtf
http://www.celestialheavens.com/homm6/MMH6Readme.rtf
```
Reason: Six H4 transcripts, plus H1 and H2 — exactly as claimed. No Chronicles file, and no
H3 file either. Because this is a **negative claim**, I did not accept an empty CDX response
at face value: the technical notes warn CDX can return empty on rate-limit without erroring,
and indeed two of my narrower queries **did** come back empty spuriously. I therefore ran a
control query against `homm4/texts/*` immediately before and after, which returned 6 rows
both times, proving the endpoint was live when the domain-wide query returned this list. The
absence is real, not an artefact.

---

### T-28
Claim: The official 3DO Chronicles section has 80 pages, including **a page per campaign**.
Label in article: unlabelled, Open questions — `chronicles-official-3do`
Verdict: **CONTRADICTED**
Severity: **MAJOR**
Searched: `https://web.archive.org/cdx/search/cdx?url=3do.com/products/pc/chronicles*&fl=original&collapse=urlkey&limit=500`
Found: 89 non-image URLs under the path, of which **82** are `.htm`/`.html`. The
campaign-level pages present are exactly five:
```
warlords.html   conquest.html   masters.html   clash.html   fc.html
```
Reason: The **"80 pages"** figure is fine — 82 by my count, and any reasonable counting rule
lands near 80; I would write "khoảng 80". The **"a page per campaign"** half is false. 3DO
built one page per **retail product**, not per campaign: `fc.html` ("The Final Chapters")
covers *both* Revolt of the Beastmasters and The Sword of Frost, and **there is no page at
all** for The World Tree or The Fiery Moon — consistent with those two having been free
downloads rather than products. Five product pages, eight campaigns. Fix to "một trang cho
mỗi **sản phẩm bán lẻ** (5 trang), không phải mỗi campaign".

Worth salvaging from the same listing: the six `tarnum*.html` art pages that independently
corroborate T-16 (see there).

---

### T-29
Claim: Only ONE Tarnum exists across both wikis — **two other pages are `#REDIRECT`**, one
is a scenario name.
Label in article: unlabelled, Open questions — no source key
Verdict: **CONTRADICTED**
Severity: **MAJOR**
Searched:
- `https://heroes.thelazy.net/api.php?action=query&list=allpages&apprefix=Tarnum&aplimit=50&format=json`
- `https://heroes.thelazy.net/api.php?action=query&list=search&srsearch=Tarnum&srlimit=20&format=json`
- `https://mightandmagic.fandom.com/api.php?action=query&list=allpages&apprefix=Tarnum&aplimit=50&format=json`
Found (thelazy, `allpages` prefix `Tarnum`): `Tarnum`, `Tarnum (Barbarian)`,
`Tarnum (Beastmaster)`, `Tarnum (Knight)`, `Tarnum (Overlord)`, `Tarnum (Ranger)`,
`Tarnum (Wizard)`, `Tarnum Dragonfriend`, `Tarnum Hopewielder`, `Tarnum the Overlord`.
Found (thelazy, `list=search`, `totalhits: 14`) two further titles that a prefix query
misses because they do not begin with "Tarnum": `King Tarnum` and `Overlord Tarnum` — both
20 bytes, both `#REDIRECT [[Tarnum]]`.
Found (Fandom): `Tarnum` and `Tarnum the Overlord` only.

Reason: The **substantive** claim survives — there is exactly one Tarnum article per wiki,
and `Tarnum the Overlord` is indeed a scenario (the first map of The Sword of Frost,
confirmed on the campaign page). But the enumeration is badly wrong: **at least nine**
redirects exist on thelazy (`Tarnum (Barbarian|Beastmaster|Knight|Overlord|Ranger|Wizard)`,
`Tarnum Dragonfriend`, `Tarnum Hopewielder`, `King Tarnum`, `Overlord Tarnum`), not two.

I grade this MAJOR rather than BLOCKER because the load-bearing half is correct and the fix
is a one-line correction. But it must be fixed: this claim is presented as evidence that a
disambiguation sweep was done, and a wrong count is exactly the failure mode of project
lesson **BH-2**. Note also the methodological trap for whoever fixes it — `apprefix=` alone
misses `King Tarnum` and `Overlord Tarnum`; you need `list=search` as well.

---

### T-30
Claim: In HotA, Tarnum is only a `{{mention}}` — not a playable hero.
Label in article: unlabelled, Open questions — no source key
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php?title=Tarnum&action=raw` (Appearances template)
- `https://heroes.thelazy.net/index.php?title=The_Life_Guard&action=raw`
- `https://heroes.thelazy.net/index.php?title=Tomb_Raiders&action=raw`
Found: Tarnum's Appearances template lists two non-Chronicles entries, both marked as
mentions — `The Life Guard` and `Tomb Raiders`. I then opened both scenario pages and read
the `| source =` field directly rather than trusting the template's parameter names:
```
| source         = hota
```
on both.
Reason: The two scenarios in which Tarnum appears outside Chronicles/H4 are confirmed HotA
scenarios by their own `| source =` field, and in both he is flagged `{{mention}}`. No
`{{player}}` or `{{enemy}}` HotA entry exists for him, and he is absent from the HotA hero
roster templates on his page. The negative holds.

---

### T-31
Claim: `fulton-names-2023` has nothing about Tarnum — actively hunted.
Label in article: unlabelled, Open questions — no source key
Verdict: **CONFIRMED**
Severity: NOTE
Searched:
- `https://heroes.thelazy.net/index.php/Gregory_Fulton/On_Names_in_Heroes_of_Might_and_Magic_III`
- `https://homm.miraheze.org/wiki/Gregory_Fulton/On_Names_in_Heroes_of_Might_and_Magic_III` (byte-identical mirror)
- `https://www.celestialheavens.com/forum/topic/17752` (original; 403 to automated fetch)
Found: the document is Gregory Fulton (NWC producer/designer on HoMM3, manual author)
answering questions compiled by Amelrix. Header: "Interview posted on 08/AUG/2023 on
Celestial Heavens, detailing Amelrix's correspondence with Gregory Fulton from 2022―2023."
Scale, verbatim: "Gregory Fulton provided exhaustive (to the best of his ability) answers to
around 200 questions." Full raw wikitext is 98 499 bytes / 1 199 lines / 220 marked replies.
Case-insensitive grep of the complete text: **Tarnum — 0 hits.** Also 0 for "Chronicl*",
"Immortal", "Waerjak", "Kilgor". "Gelu" — 2 hits, both about **pronunciation**, not names'
origins, e.g. "after I published the name 'Gelu' (je-lu or jel-u), I found myself continually
correcting the Map Makers".
Reason: The negative is real and was tested against the full text, not a sample. It is also
a *meaningful* negative rather than a vacuous one: the document does cover Stronghold hero
names, Erathia (10×), Antagarich (10×) and "Barbarian" (13×), so the subject area is present
and Chronicles characters are simply never touched. That is the right way to state it in the
article — "the relevant sections exist and Tarnum is absent from them", not merely "not found".

---

### T-32
Claim: `chronicles-official-3do` is genuinely official — "Heroes Chronicles © 2000 The 3DO
Company. All Rights Reserved."
Label in article: `T2` — `chronicles-official-3do`
Verdict: **CONFIRMED** (tier) / MINOR (quote accuracy)
Severity: MINOR
Searched (I read the footer myself, per the `heroesofmightandmagic.com` precedent):
- `https://web.archive.org/web/20010410194637/http://www.3do.com/products/pc/chronicles/index.html`
- `.../main.html`, `.../features.html`, `.../fc.html`
Found — the footer, identical on all four pages, inside `<... class="legal">`:
> "© 2000 The 3DO Company. All Rights Reserved. Game specifications subject to change
> without notice."

Reason: **`T2` is correct.** This is the publisher's own domain (`www.3do.com`), the
copyright is asserted by 3DO itself, and the page links to `3do.com/corporate/copyframe.htm`
and `store.3do.com`. There is no third-party byline anywhere — nothing resembling the
"©2005 Valera Koltsov" footer that unmasked `heroesofmightandmagic.com`. The tier survives
the precedent test.

**MINOR, and I flag it only because of the recent fabricated-quote incident:** the string
the article presents — "Heroes Chronicles © 2000 The 3DO Company. All Rights Reserved." —
is **not a contiguous string on any page**. "Heroes Chronicles" is the `<title>` element;
the copyright line begins at "©". The article has spliced two separate page elements into
one quotation. The claim is true and the tier is right, but the quotation marks are not
earned. Either quote the footer alone, or drop the quotation marks and describe it.

---

## Kết luận

**Bài `tarnum` CHƯA đủ điều kiện `status: verified`.** Điều kiện là không còn `BLOCKER` và
không còn `MAJOR`; hiện còn **1 BLOCKER và 5 MAJOR**.

Phải sửa trước khi đặt `verified`:

1. **T-24 — BLOCKER.** Bỏ khẳng định phủ định "không thể kết luận Tarnum giết Sandro". Nó bị
   chính trường `| description =` của `Truth Within Nightmares` bác: *"Tarnum must kill
   Sandro to get the key to the next level."* Đây là **mâu thuẫn nội bộ**: T-04 và T-19 dùng
   đúng trường đó làm `T1* EXPLICIT`, nên bài không thể vừa công nhận vừa bỏ qua nó. Thêm
   nữa, trang `Sandro` của thelazy nói ngược lại điều bài trích: *"Also, the scenario
   description strongly hints that Tarnum killed the Underworld Sandro."* Chữ "probably" ở đó
   dè dặt về việc **có phải cùng một nhân vật Sandro hay không**, không dè dặt về cái chết.
   Giữ lại hai phát hiện thật (không có Epilogue; không timed event nào sau Day 1 nhắc
   Sandro) và viết lại thành: *không có văn bản tường thuật nào mô tả cái chết; chỗ dựa duy
   nhất là câu mục tiêu, mà mục tiêu ≠ kết quả.*
   **Kèm theo:** nếu trong bài có chữ "hậu duệ"/"descendant" cho Allison thì đó là lỗi thứ
   hai cùng mức. Game text nói rõ **"my niece, Allison"** — cháu gái, con của chị/em gái.
2. **T-03 — MAJOR.** "Hành động khoan dung của ông gây ra The Reckoning" đang là khẳng định
   trần trong Summary, trong khi chuỗi nhân quả được chính bài gán `INFERENCE` ở T-15. Game
   text chỉ cho thấy Tarnum **sợ** điều đó ("please don't let my compassion destroy the
   world!"). Phải hạ giọng và mang nhãn `INFERENCE` lên Summary.
3. **T-22 — MAJOR.** Hai câu trích đều **có thật** (tôi đã lấy được cả hai), nhưng khung
   "hai nguồn `T4` tranh nhau quyền tác giả" là đọc sai. Bullard nói "majority of the work
   myself" để trả lời câu hỏi về **Jon Van Caneghem**, và ngay trong cùng câu trả lời bà
   nói *"Each original story & maps was written by one level designer and then I cleaned and
   polished them until ship."* — tức đúng vai trò Terry Ray mô tả. Hai lời khai **bổ sung
   nhau**, không mâu thuẫn. Bỏ khỏi *Canon disputes* hoặc viết lại thành phân công công việc.
4. **T-28 — MAJOR.** "Một trang cho mỗi campaign" sai. 3DO làm **năm** trang theo sản phẩm
   bán lẻ (`warlords`/`conquest`/`masters`/`clash`/`fc`); The World Tree và The Fiery Moon
   **không có trang nào**. Con số ~80 trang thì chấp nhận được (tôi đếm 82 file `.html`).
5. **T-29 — MAJOR.** "Hai trang khác là `#REDIRECT`" sai — có **ít nhất chín** redirect trên
   thelazy. Phần cốt lõi (chỉ một Tarnum) thì đúng. Lưu ý cho người sửa: `apprefix=Tarnum`
   bỏ sót `King Tarnum` và `Overlord Tarnum`, phải chạy thêm `list=search`.
6. **T-01 — MAJOR có điều kiện.** "Nhân vật duy nhất có sáu class" chỉ dựa vào **một dòng
   Trivia không nguồn trên Fandom** = `T6`, mà `T6` không bao giờ đỡ được `EXPLICIT`. Nếu mục
   Gameplay đã ghi `T6 UNVERIFIED` và Summary có dẫn "theo Fandom" thì hạ xuống NOTE; nếu
   không, phải sửa.

Nên sửa nhưng không chặn (`MINOR`):

- **T-14** — dấu `…` đang xoá câu *"Among the broken ice was a discarded Barbarian Axe."*,
  làm "its hilt" đọc thành chuôi **Sword of Frost**. Thực ra Tarnum nhặt **cây rìu** — và
  chính cây rìu mới là manh mối chỉ ra kẻ trộm là người Barbarian. Khôi phục câu đó.
- **T-32** — câu trích "Heroes Chronicles © 2000 The 3DO Company…" **không phải một chuỗi
  liền** trên trang: "Heroes Chronicles" là thẻ `<title>`, dòng bản quyền bắt đầu từ "©".
  Tier `T2` thì đúng (tôi đã tự đọc footer; không có byline bên thứ ba nào). Bỏ ngoặc kép
  hoặc chỉ trích đúng dòng footer.
- **T-12** — "câu thoại cuối trong cả series" cần thu hẹp phạm vi: Tarnum còn xuất hiện
  trong "Lost Tales of Axeoth: Every Dog Has His Day" (H7).
- **T-13** — nói rõ đây là câu hỏi tu từ của **Waerjak**, và thu hẹp "duy nhất" thành "mốc
  duy nhất về tuổi thọ của Tarnum".
- **T-23** — trích đủ mệnh đề "**four games** … with interconnected storylines"; đây là
  marketing copy đầu 2001, khi mới có bốn tựa.
- **T-04 / T-19** — sai source key: hai câu `| description =` nằm ở trang
  `Warlords_of_the_Wasteland` và `Masters_of_the_Elements`, không phải `Heroes_Chronicles`.

**Những gì bài làm đúng và nên giữ nguyên** — các claim gánh nặng nhất đều đứng vững:

- **T-06 / T-07 / T-08** — đúng hoàn toàn, kể cả claim về **vị trí** trong
  `=== Timed events ===`. Trang `Tunnels of Ice` **không hề có** mục `== Epilogue ==`, và
  Prologue không nhắc gì tới bất tử. Đây là một ca đúng sách của bài học **BH-1**.
  Phần phủ định "không phải Ancients" còn **mạnh hơn** bài đang viết: Bullard bác thẳng
  trong phỏng vấn (`T4`) — *"Ancestors were the biological start of the current crop of
  heroes. Ancients were often other powers who dabbled in the lives of mortals."* Nên thêm
  `bullard-interview-2013` vào đây để biến lập luận-từ-im-lặng thành `T4 EXPLICIT`.
  ⚠️ Cảnh báo kèm theo: trang `Heroes Chronicles` của thelazy có mục
  `== Unofficial Content ==` mô tả mod fan "The Glory of War" với Tarnum "reincarnated as an
  undead Death Knight". Là fanmade, nhưng nếu bài khẳng định "không phải undead" thì nên gọi
  tên và loại trừ nó rõ ràng.
- **T-14** — vị trí epilogue đúng trên hai trục độc lập: `The Protectors of the Sword` là
  map thứ **tám/cuối** của The Sword of Frost, và campaign đó tự ghi là "the **eighth
  episode** in Heroes Chronicles".
- **T-16** — tôi đếm trực tiếp: header có đúng **sáu** cột class, và **cả tám** ánh xạ
  campaign + town trong bài đều chính xác. Có ba nguồn độc lập chống lưng, trong đó một là
  `T2`: site 3DO có đúng **sáu** trang tranh Tarnum (`tarnumbarbarian`, `tarnumknight`,
  `tarnumwizard`, `tarnumranger`, `tarnumrevolt`, `tarnumsword`). Nên thêm key này.
- **T-10 / T-11 / T-12 / T-13 / T-26** — mọi câu trích H4 đều khớp verbatim với
  `H4-MightTexts.rtf` lấy qua archive (URL live trả **403** đúng như ghi chú kỹ thuật).
- **T-27 / T-30 / T-31** — cả ba claim phủ định đều đứng vững, và tôi đã săn chủ động thay
  vì suy từ im lặng. Riêng T-27 tôi chạy **control query** trước và sau vì hai truy vấn CDX
  hẹp hơn đã trả rỗng giả — đúng cái bẫy ghi trong technical notes.

**Không có câu trích nào bị bịa.** Cả hai phỏng vấn `T4` đều lấy được và cả hai câu gán cho
Ray và Bullard đều có thật, nguyên văn — vấn đề ở T-22 là **cách diễn giải**, không phải
nguồn. Không có claim nào rơi vào `NOT_FOUND`.

**Ba nguồn nên bổ sung vào `REGISTRY.md` sau đợt này:**
`hc-the-barbarians-wife` (`T1*` — quan hệ Kija–Kilgor là game text, không cần dựa prose wiki),
`3do-chronicles-features` (`T2` — bullet "four games … interconnected storylines"), và ghi
nhận bản gốc `acidcave.net/jennifer_bullard_interview.html` làm primary cho
`bullard-interview-2013` (thelazy chỉ là bản mirror truy cập được).

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. BLOCKER và toàn bộ MAJOR đã xử lý.

### Áp V4 — tự dựng lại BLOCKER trước khi sửa

| Bằng chứng | Kết quả tự kiểm | |
|---|---|---|
| `| description =` của `Truth Within Nightmares` nói thẳng "Tarnum must **kill** Sandro" | Fetch lại: *"Tarnum must kill Sandro to get the key to the next level."* | ✅ **XÁC NHẬN** |
| Trang `Sandro` nói ngược với cách bài dùng nó | *"Also, **the scenario description strongly hints that Tarnum killed** the Underworld Sandro."* | ✅ **XÁC NHẬN** |
| Scenario **không có** Epilogue | `'Epilogue' in wikitext` → `False` | ✅ **XÁC NHẬN** |

### Bảng xử lý

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| T-24 | "Không kết luận được việc giết Sandro" — **và bài tự mâu thuẫn** | **BLOCKER** | Viết lại cả mục. Bài dùng `\| description =` làm `T1* EXPLICIT` ở hai mục khác rồi **gạt chính trường đó** ở đây — không thể vừa coi là game text vừa bỏ qua. Sửa thành: **việc giết là `EXPLICIT`**; tranh chấp thật nằm ở **DANH TÍNH** (Sandro đó có phải Sandro của H3 không) — đúng điều cảnh báo registry vẫn luôn nói. Chữ "probably" trên wiki rào **danh tính**, không rào việc giết |
| T-03 | *Tóm lược* nói chuỗi nhân quả như **dữ kiện** | MAJOR | Hạ xuống: game text chỉ có Tarnum **sợ** điều đó (*"please don't let my compassion destroy the world"*); chuỗi tới Reckoning là `INFERENCE`. Sửa cả câu mở |
| T-22 | Dựng ra một "tranh chấp tác giả" không có thật | MAJOR | Câu của Bullard trả lời một câu hỏi về **Van Caneghem**, và bà nói rõ cách chia việc: *"Each original story & maps was written by **one level designer**"* — đúng vai của Ray. **Bổ sung nhau, không loại trừ.** Đã viết lại mục |
| T-01 | "duy nhất có sáu class" dựa vào Trivia Fandom **không dẫn nguồn** | MAJOR | Bỏ chữ "duy nhất" khỏi *Tóm lược*; hạ xuống `T6 UNVERIFIED` và tách thành ghi chú, **không** dùng làm lý do giữ schema |
| T-28 | "trang riêng cho từng campaign" | MAJOR | Sai — 3DO chỉ làm **năm** trang sản phẩm; *The World Tree* và *The Fiery Moon* **không có trang nào**. Sửa số trang thành ~82 |
| T-29 | "hai trang khác là redirect" | MAJOR | Ít nhất **chín** trên thelazy. Claim lõi (chỉ một Tarnum) vẫn đúng |
| T-14 | Lược mất một câu làm đọc sai | MINOR | Khôi phục *"Among the broken ice was a discarded Barbarian Axe"* — nếu thiếu nó thì "its hilt" đọc thành chuôi **thanh kiếm**, trong khi thật ra là chuôi **cây rìu** |

### Điều verifier xác nhận đứng vững

- **T-06 / T-07 / T-08** — cơ chế bất tử là game text tường minh, **và cả claim vị trí cũng đúng**:
  `Tunnels of Ice` **không có** mục Epilogue, nên đoạn đó chỉ tồn tại trong timed event Day 23/24.
  Đúng như BH-1 dự báo. ⭐ Verifier còn làm **mạnh thêm** vế phủ định "không phải Ancients":
  Bullard phủ nhận trực tiếp trong một nguồn `T4`.
- **T-14** — vị trí epilogue xác minh hai lần.
- **T-16** — đếm được đúng **sáu** cột class, và **cả tám** cặp campaign+town đều đúng.
- **T-21 / T-22 / T-23** — lấy lại được **cả hai** bài phỏng vấn. **Không có trích dẫn nào bị bịa.**

### Lỗi của bảng claim, không phải của bài

- Người soạn mô tả Allison là "**cháu ruột**" (descendant) của Tarnum; game text nói **niece** —
  **cháu gái** — và nói rõ hai lần. Bài đã dùng đúng chữ "cháu gái".
- Trích dẫn ở T-32 là **ghép** `<title>` với footer. Tier `T2` vẫn đứng: người kiểm tự đọc footer
  3DO và xác nhận **không có** dòng ghi công bên thứ ba.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-tarnum-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.
