# Verify report: archibald-ironfist — 2026-08-03

Verifier: independent agent, did not read the article
Claims checked: 35
CONFIRMED: 30 | DOWNGRADE: 1 | NOT_FOUND: 0 | CONTRADICTED: 4

BLOCKER: 3 (A-05, A-17, A-26) · MAJOR: 12 · MINOR: 7 · NOTE: 6

Primary sources reached in this pass:

- `web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`
  — official 3DO MM7 story page, "The Diaries of Archibald" (T2)
- `heroes.thelazy.net` raw wikitext: `Archibald`, `Nimbus`, `Alamar`, `Gem`,
  `Clearing the Border`, `Succession Wars`, `Morglin Ironfist`, `Beyond the Horizon`,
  `Horn of the Abyss (Changelog)`, `Gregory Fulton/On Names in Heroes of Might and Magic III`
- `mightandmagic.fandom.com/api.php` wikitext: `Archibald Ironfist`, `Archibald`,
  `Archibald Dawnsglow`, `Morglin Ironfist`, `Deyja`, `Kastore`, `Kastore (Terra)`,
  `Nimbus`, `Necromancers' Guild`, `Final Justice`, `First Blood`, `Apocalypse`,
  `Archibald's campaign`, `Path of Darkness`, `First War of Enrothian Succession`,
  `User talk:Nicko Budkov`, Heroes I hero categories
- `homm.fandom.com/api.php` wikitext: `Greg Fulton/Fanstratics Newsletters/4` and `/5`,
  `Gregory Fulton/Tavern of Might and Magic Interview`, `Alamar`

Blocked / unavailable: `fanstratics.com` (connection refused), `homm.miraheze.org`
(bot challenge), `celestialheavens.com` (HTTP 403). Newsletter text was reached through
the `homm.fandom.com` mirror, which links the `web.archive.org` capture of the original.

---

## Details

### A-01
Claim: Archibald spent roughly ten years petrified, was freed, then took the throne of a
second kingdom (Deyja).
Label in article: (unlabelled, Summary)
Verdict: CONFIRMED
Severity: NOTE
Searched: `web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`
Found: Entry 1 — "so much has changed in the ten years I have been my brother's coat
rack-made an insensate stone statue by his pet wizard, Tanir. If it wasn't for those fool
"adventurers" I'd still be there now." Entry 143 — "For as the lich, Gryphonheart,
replaced Deathknell, so have I replaced Gryphonheart."
Reason: Every component is separately sourced below (A-10, A-12, A-14). "Second kingdom"
is correct ordering: Enroth first, Deyja second. As a summary line it needs no tier.

### A-02
Claim: Roland calls him "Brother Archibald" in the sentencing text, establishing the
sibling relation.
Label in article: `T1* EXPLICIT` — `h2-final-justice`
Verdict: CONFIRMED
Severity: —
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Final%20Justice&prop=wikitext`
Found: inside a quote template on the `Final Justice` page —
"Brother Archibald, for your crimes against the kingdom and myself…"
The same page's opening briefing template also has Roland saying: "My brother refuses to
surrender in the face of your army…"
Reason: Correct kind of source: the text sits inside `{{quote|…}}`, which per the project's
own convention marks in-game briefing dialogue, not editor prose. `T1*` is right, and the
sibling relation is doubly attested on the one page.

### A-03
Claim: Their father is Morglin Ironfist, winner of the first war of succession.
Label in article: `T6 INFERENCE` — article states no game text calls him the father —
`h1-morglin-ironfist`
Verdict: CONFIRMED
Severity: MINOR
Searched: `heroes.thelazy.net/index.php?title=Morglin%20Ironfist&action=raw` ·
`mightandmagic.fandom.com/api.php?action=parse&page=Morglin%20Ironfist`
Found: thelazy — "King of Enroth. Main character of Heroes I. Father of Archibald and
Roland Ironfist." Fandom infobox relatives field lists "Archibald Ironfist (son)"; Fandom
prose — "His eventual death acts as the catalyst for the events of Heroes II: The
Succession Wars, during which his sons Roland and Archibald wage a bloody war for the
throne."
Reason: `T6 INFERENCE` is the correct, appropriately cautious label. One flag: Fandom's
`Archibald Ironfist` page opens its "First Blood" section with a `{{Text|…}}` block reading
"Archibald is one of the two sons of King Morglin Ironfist." If that block faithfully
reproduces in-game campaign-selection text, then game text *does* name the father — but the
same wiki's `First Blood` editor prose pipes the link as "Lord Ironfist", which suggests the
in-game wording is "Lord Ironfist" and an editor substituted "Morglin". Unresolved without
the H2 game files; worth a line in *Open questions* rather than silent omission.

### A-04
Claim: Archibald does NOT appear in Heroes I. The four lords are Morglin, Lamanda, Slayer
and Alamar, and none of them is a named controllable hero in the Heroes-II-onward sense.
Label in article: `T6 EXPLICIT` — `h1-morglin-ironfist` + `thelazy-succession-wars`
Verdict: CONFIRMED
Severity: MAJOR (label)
Searched: `mightandmagic.fandom.com/api.php?action=query&list=categorymembers` for
`Category:Heroes I Knights` / `Warlocks` / `Barbarians` / `Sorceresses` ·
`heroes.thelazy.net/index.php?title=Succession%20Wars&action=raw` ·
`mightandmagic.fandom.com/api.php?action=parse&page=First%20War%20of%20Enrothian%20Succession`
Found: The complete Heroes I hero roster, 36 heroes over four factions, contains no
Archibald — Knights: Ambrose, Arturius, Dimitri, Ector, Gallant, Haart, Kilburn, Maximus,
Tyro. Warlocks: Agar, Arie, Barok, Crodo, Falagar, Kastore, Sandro, Vesper, Wrathmont.
Barbarians: Antoine, Atlas, Crag Hack, Ergon, JoJosh, Kelzen, Thundax, Tsabu, Yog.
Sorceresses: Ariel, Astra, Carlawn, Gem, Luna, Natasha, Rebecca, Troyan, Vatawna.
And Fandom `Morglin Ironfist`, verbatim: "Lord Ironfist is the leader of the Knight faction
in ''Heroes I'', and canonically acts as the player's avatar during the game; events are
unveiled through his perspective. However, like his three counterparts, he does not appear
as a hero during the game at any point, and makes no playable appearance in the series."
thelazy `Succession Wars` names the other three: "he found himself in bitter combat for the
crown against three local rulers: Queen Lamanda, Lord Slayer, and Lord Alamar."
Reason: I hunted this actively rather than inferring from silence: I enumerated the full
roster instead of searching for the absent name, and I found an explicit positive statement
of the negative ("does not appear as a hero during the game at any point"). The claim
survives on substance. **The label does not.** Per `CANON-POLICY`, `T6` cannot carry
`EXPLICIT`; relabel `T6 INFERENCE`. Note also that Heroes I *does* have named recruitable
heroes (Kastore, Sandro, Crag Hack…), so the article must keep the qualifier "none of the
four lords" — dropping it would make the sentence false.

### A-05
Claim: The father's in-game name in Heroes I is "Jerico"; the name "Morglin" appears only
in the manual.
Label in article: `T6 EXPLICIT` — `h1-morglin-ironfist`
Verdict: **CONTRADICTED**
Severity: **BLOCKER**
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=User%20talk:Nicko%20Budkov` ·
`mightandmagic.fandom.com/api.php?action=parse&page=Morglin%20Ironfist` ·
`mightandmagic.fandom.com/api.php?action=parse&page=First%20War%20of%20Enrothian%20Succession` ·
web search for the MM8 Herald's Boots description
Found: The contradicting source is the very talk-page discussion that Fandom's own rename
banner cites as its evidence. `User talk:Nicko Budkov`, section "Lord Ironfist", by editor
XEL Lore — the same editor credited with the annotations on the Fulton interviews:

> "All in all, the only direct mention of his first name is Jerico in MM8. and Morglin is
> only indirectly implied via the name of his abode being Morglin's Keep (and Morglin also
> being the name of a river in that area)."

And in the Russian portion of the same thread:

> "Нигде помимо ММ8 и косвенного упоминания в мануале HoMM1 имя лорда Айронфиста не
> упоминается, в остальных играх он просто Lord Ironfist или old King Ironfist."
> ("Nowhere apart from MM8 and the indirect mention in the HoMM1 manual is Lord Ironfist's
> first name mentioned; in the other games he is simply Lord Ironfist or old King
> Ironfist.")

The name "Jerico" comes from a **Might and Magic VIII** item description (Herald's Boots):
"When Jerico Ironfist secured the throne in the First War of Enrothian Succession, he sent
forth heralds to spread the news."
Reason: Two independent errors, both load-bearing:
1. **"Jerico" is not the Heroes I in-game name.** In Heroes I he is only "Lord Ironfist".
   "Jerico" originates in MM8, three games later. The article attributes it to the wrong
   game entirely.
2. **"Morglin appears in the manual" overstates the manual.** Fandom `Morglin Ironfist`
   trivia: "Lord Ironfist's name being Morglin is not given anywhere in any of the games,
   and is only implied in the Heroes I manual." The manual never states the name; it is
   inferred from the place-names "Morglin's Keep" and the River Morglin.
The Fandom rename banner the article most likely leaned on — `{{rename|Jerico Ironfist|…
It is referred to in the game as "Jerico".}}` — says "in the game" without naming which
game. That ambiguity is exactly where the error entered. Required rewrite: in Heroes I he
is "Lord Ironfist"; "Morglin" is implied only, via place-names in the Heroes I manual;
"Jerico" is stated directly only in Might and Magic VIII. And `T6 EXPLICIT` must go
regardless.

### A-06
Claim: Archibald's opening briefing in `First Blood`, quoted through "No one can stand
before me and refuse to serve."
Label in article: `T1* EXPLICIT` — `h2-first-blood`
Verdict: CONFIRMED
Severity: MINOR
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=First%20Blood&prop=wikitext`
Found: inside the page's quote template, attributed to Archibald — "Thank you for choosing
to serve me. You will find I can be a very generous lord to vassals who remain faithful,
which is more than I can say for the cowardly lords who refuse to take the oath from me.
I am King! Not Roland. No one can stand before me and refuse to serve. Go! I have allocated
a sum of gold for the purposes of making an example of the lords closest to my castle.
Crush them, and report back to me by means of the magical amulet I have sent you."
Reason: Word-for-word match over the quoted span, inside `{{quote|…}}`, so `T1*` is the
right kind. MINOR only: the article's quotation ends at "refuse to serve." with no ellipsis,
though the source sentence continues. Add a trailing ellipsis.

### A-07
Claim: End of Archibald's own campaign, he spares Roland and appoints him monarch of the
Western Tower.
Label in article: `T1* EXPLICIT` — `h2-apocalypse`
Verdict: CONFIRMED
Severity: —
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Apocalypse&prop=wikitext`
Found: inside the page's second quote template — "Well, Roland, it seems I've won our
little contest. But don't worry. Not only have I decided to spare your life, but I am
appointing you monarch of the Western Tower. You will be the ruler of a mighty empire, one
who's every crack and crevice you will know... in ten minutes. Perhaps I will come and
visit your splendid court, when you are not entertaining important rats and spiders.
(laughs, trailing away)"
Reason: Exact match over the quoted span, including the ellipsis before "in ten minutes".
The article stops at "in ten minutes." which is a clean sentence boundary. `T1*` correct.

### A-08
Claim: The grammatical error "one who's every crack" (should be *whose*) is in the original
game text.
Label in article: (parenthetical note) — `h2-apocalypse`
Verdict: DOWNGRADE
Severity: MINOR
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Apocalypse&prop=wikitext` ·
`heroesofmightandmagic.com/heroes2/storyline.shtml` (page fetched, 35 KB, does not carry
this line) · web search for independent transcriptions
Found: Fandom's transcription does read "one who's every crack and crevice you will know".
Reason: What is verified is that **the wiki's transcription** contains "who's". The claim
asserts something stronger — that the typo is in the *original* game text — and that
requires reading the Heroes II dialogue script or campaign files, which I could not reach.
A wiki transcription is exactly the kind of place a typo gets introduced or silently
corrected. Restate as "as transcribed on Fandom" and move the "in the original game text"
assertion to `BACKLOG` under `B-001`, or drop the parenthetical until the H2 files are
extracted. Not a `BLOCKER` because it carries no tier and sits in a parenthetical.

### A-09
Claim: Canon outcome: Archibald LOSES, on three independent game-text sources.
Label in article: `T1 EXPLICIT` (a,b) + `T1* EXPLICIT` (c) — `h3wiki-herobios-txt` +
`sod-clearing-the-border`
Verdict: CONFIRMED
Severity: MINOR
Searched: `heroes.thelazy.net/index.php?title=Alamar&action=raw` ·
`…?title=Gem&action=raw` · `…?title=Clearing%20the%20Border&action=raw` ·
`homm.fandom.com/api.php?action=parse&page=Alamar`
Found, each separately as the claim table demanded:
(a) Alamar's Heroes III hero biography — "Alamar served Archibald Ironfist during the
Succession Wars, and was barely able to escape Enroth following Archibald's defeat."
Reproduced identically on thelazy and on `homm.fandom.com`.
(b) Gem's Heroes III hero biography — "Gem was one of the greatest sorceresses that Enroth
had ever seen, serving King Roland Ironfist during the Succession Wars. Shortly after
Roland had secured the throne of Enroth, Gem left for Erathia, finding a new home in
AvLee."
(c) thelazy `Clearing the Border`, section "Prologue", Gem speaking — "It is hard to
believe a year has passed since Archibald and his Necromancer allies were defeated, ending
the Succession Wars."
Reason: The claim survives, but the claim table's suspicion was well aimed at (b):
**(b) does not say Archibald lost.** It says Roland secured the throne. Reaching "Archibald
lost" from (b) is `INFERENCE`, not `EXPLICIT`. (a) and (c) *are* explicit — "following
Archibald's defeat" and "were defeated" — so the headline holds on two explicit legs.
Split the label: (a) explicit, (b) inference, (c) explicit.
Second point, a tier caveat I cannot resolve from outside: I reached (a) and (b) only
through fan wikis, which makes them `T1*` on my path. `T1` is legitimate only if the
researcher genuinely extracted `HeroBios.txt`. I cannot audit that. Flagging, not
penalising — the file is real and the text is in hero-bio format. But see A-26, where the
same source key is used to assert something incompatible with (a).

### A-10
Claim: The petrification sentence, verbatim.
Label in article: `T1* EXPLICIT` — `h2-final-justice`
Verdict: CONFIRMED
Severity: —
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Final%20Justice&prop=wikitext`
Found: inside the page's second quote template — "Brother Archibald, for your crimes
against the kingdom and myself, I give you a mercy you surely would not have shown me: I
sentence you to be turned to stone and locked in the west tower until future generations
should take pity upon you and restore you to life. If they ever do. In any case, you may
rest assured you will never lay eyes upon the crown again."
Reason: Word-for-word, punctuation included, over the whole quoted passage. Inside
`{{quote|…}}`, so `T1*` is the right kind. Nothing to fix.

### A-11
Claim: For most of MM6 Archibald is a non-interactive stone statue in the library of Castle
Ironfist; revived in *Free Archibald* because the party needs `Ritual of the Void` to
destroy The Hive.
Label in article: `T6 EXPLICIT` — article states this is wiki prose, not verified against
game files — `fandom-archibald-ironfist`
Verdict: CONFIRMED
Severity: MAJOR (label)
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Archibald%20Ironfist&prop=wikitext`
Found: "For the majority of ''Might and Magic VI'', Archibald is a non-interactive stone
statue seen in the Library of Castle Ironfist. However, he is revived during the quest to
Free Archibald, appearing briefly as an NPC. Once the player has retrieved the Third Eye
and entered the Library, Archibald will return to life and provide the party with the
Ritual of the Void scroll before disappearing." And in the biography: "Melian ordered them
to free Archibald so that they might use one of his self-made spells to successfully
destroy the Kreegan Hive without endangering Enroth."
Reason: Content matches, and the article is commendably honest that this is wiki prose.
But `T6 EXPLICIT` is a label violation — relabel `T6 INFERENCE`. Two MINOR precision
points: Fandom says *scroll*, not spell, in the gameplay section (the biography says
"spells"); and the motive chain runs through Melian's order, which is worth keeping because
it is what makes the revival make sense.

### A-12
Claim: Diaries Entry 1, dated 11 June 1165: "Free at last! Never again will I take for
granted what it means to bend limb and breathe air."
Label in article: `T2 EXPLICIT` — `mm7-diaries-3do`
Verdict: CONFIRMED
Severity: —
Searched: `web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`
Found: "The Diaries of Archibald / Entry 1 / 11 June 1165 / Free at last! Never again will
I take for granted what it means to bend limb and breathe air."
Reason: Exact, on the official 3DO publisher site. `T2 EXPLICIT` is the correct tier and
the correct kind. The `curl -sL` with full timestamp method noted in the claim table works.

### A-13
Claim: In Entry 1 he calls the people who freed him "those fool adventurers".
Label in article: `T2 EXPLICIT` — `mm7-diaries-3do`
Verdict: CONFIRMED
Severity: MINOR
Searched: same 3DO capture as A-12
Found: "If it wasn't for those fool "adventurers" I'd still be there now."
Reason: Confirmed, but the source has scare quotes around *adventurers* and the article's
rendering drops them. The scare quotes are the sneer — they are the point. Restore them:
those fool "adventurers".

### A-14 ⚠️⚠️
Claim: TWO SEPARATE EVENTS. (1) Winning the Challenge of Dominance against Nimbus gained
him only "this little mission" and happened BEFORE Gryphonheart was destroyed (Entry 37).
(2) He became king of Deyja later and separately (Entry 143).
Label in article: `T2 EXPLICIT` — `mm7-diaries-3do`
Verdict: **CONFIRMED**
Severity: —
Searched: `web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`
Found, Entry 37, 23 October 1167 — Gryphonheart alive and at war with Catherine at the time
of the Challenge:
> "Now Gryphonheart has called the Necromancer Guild to his aid, and I and the Necromancers
> of Enroth are heeding the call. He fights his daughter, Catherine. That is a cause I can
> hearken to, indeed! **Incidentally, this little mission is now my mission. I took it from
> Nimbus in the guild Challenge of Dominance. Needless to say, I won.**"

And what the mission *was*, from the same entry:
> "Nimbus returned to his estates bringing with him a small party of Necromancers -
> apparently all of any power that remained in Enroth - he was gathering to take to Deyja
> in Erathia so that they might serve the lich-king, Nicolas Gryphonheart."

Found, Entry 143, 5 August 1168 — after Catherine's victory speech and Gryphonheart's final
death:
> "For as the lich, Gryphonheart, replaced Deathknell, so have I replaced Gryphonheart."

Reason: This is the article's central finding and it is **correct on the primary source**,
verified verbatim on the official 3DO site. The two events are ten months and two diary
entries apart, and the ordering is unambiguous: at the Challenge (Entry 37) Gryphonheart is
alive and Archibald is sailing to serve him; the replacement of Gryphonheart is reported in
Entry 143. What the Challenge won is stated in Archibald's own words as "this little
mission", and the mission is defined in the preceding paragraph of the same entry as the
Enrothian necromancer contingent bound for Deyja. The article's gloss "command of the
Enrothian Necromancer contingent going to Deyja" is a faithful paraphrase, and it is
independently corroborated by thelazy's own `Nimbus` page (see A-16). `T2 EXPLICIT` is the
correct tier and kind. Nothing to fix.

### A-15 ⚠️⚠️
Claim: Both major wikis merge those two events and assert causation the source does not
have; both also place the Challenge after Gryphonheart's destruction.
Label in article: `T6 EXPLICIT` + `T2 EXPLICIT` —
`fandom-archibald-ironfist` + `mm7-diaries-3do`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: `heroes.thelazy.net/index.php?title=Archibald&action=raw` ·
`mightandmagic.fandom.com/api.php?action=parse&page=Archibald%20Ironfist&prop=wikitext`
Found, thelazy `Archibald`, MM7 section, first sentence — merge and wrong order in one
sentence:
> "After the lich form of King Nicolas Gryphonheart is put to rest, Archibald battles
> Nimbus for the title of King of Deyja, and wins."

Found, Fandom `Archibald Ironfist`, section "The Usurper Usurped" — the preceding paragraph
ends "In a matter of months, Catherine infiltrated Gryphonheart's citadel and killed him,
along with the traitor." The next paragraph then opens:
> "Defeating Nimbus in the guild Challenge of Dominance, Archibald assumed control over the
> now-vacant throne of Deyja."

Reason: Both quotes are verbatim as the article gives them (the article silently drops
Fandom's link piping around "Challenge of Dominance", which is correct practice for
readability). Both wikis do exactly what the article says: they fuse the guild contest with
the accession, they invent a causal link ("for the title of King of Deyja" / "assumed
control over the now-vacant throne"), and both place the Challenge after Gryphonheart's
death — inverting Entry 37. Verified against the primary source in A-14. This is a genuine,
correctly documented finding and it is the strongest thing in the article.
NOTE on the label, not a defect: the project rule that `T6` cannot carry `EXPLICIT` exists
to stop uncited wiki prose being passed off as fact. Here the claim is *about the wiki's own
text*, for which the wiki is the primary source. `T6 EXPLICIT` is defensible in this narrow
meta-use. Recommend the article say so in one clause so a future verifier does not flag it.

### A-16 ⚠️⚠️
Claim: thelazy contradicts itself — its `Nimbus` page separates the two events correctly,
describing what was won as leadership of "the Enrothian necromancers who joined the forces
of Deyja", while its `Archibald` page merges them.
Label in article: `T6 EXPLICIT` — `thelazy-nimbus`
Verdict: **CONFIRMED**
Severity: NOTE
Searched: `heroes.thelazy.net/index.php?title=Nimbus&action=raw` ·
`heroes.thelazy.net/index.php?title=Archibald&action=raw`
Found, thelazy `Nimbus`, Story section — correct separation, correct order, and the phrase
the article quotes:
> "Archibald battled Nimbus for the title of guildmaster and won, becoming the new leader
> of the Enrothian necromancers who joined the forces of Deyja."

and then, only after the Lich King is overthrown:
> "Following the victory, Archibald became the new ruler of Deyja."

Reason: Confirmed exactly. The `Nimbus` page gets it right twice over — the title contested
is "guildmaster", not King of Deyja, and the accession is placed after the Lich King's fall,
in a separate sentence, matching Entry 37 and Entry 143. The `Archibald` page on the same
wiki says the opposite. The self-contradiction is real and the quoted fragment is verbatim.
NOTE, and it is an addition rather than a correction: **Fandom contradicts itself too, and
the article does not say so.** Fandom `Nimbus` — "Archibald defeated Nimbus in a Challenge
of Dominance, becoming the new guildmaster." Fandom `Necromancers' Guild` — "Archibald
defeated Nimbus in a duel, taking control of the guild." Both describe winning the *guild*,
not the throne, while Fandom `Archibald Ironfist` says he "assumed control over the
now-vacant throne of Deyja". So the pattern the article found on thelazy holds on Fandom as
well: the character-hub pages merge the events, the supporting pages get them right. Adding
this makes the finding markedly stronger, and it also supplies the counter-source that sinks
A-17. Same narrow-meta-use label note as A-15.

### A-17 ⚠️
Claim: There is no "duel". The sources say only *Challenge of Dominance*; no text describes
the format of the contest.
Label in article: (unlabelled, Biography)
Verdict: **CONTRADICTED**
Severity: **BLOCKER**
Searched: `mightandmagic.fandom.com/api.php?action=query&list=search&srsearch=Archibald%20Nimbus%20duel` ·
`…&srsearch=%22Challenge+of+Dominance%22` ·
`mightandmagic.fandom.com/api.php?action=parse&page=Necromancers%27%20Guild&prop=wikitext` ·
`mightandmagic.fandom.com/api.php?action=parse&page=Nimbus&prop=wikitext` ·
`heroes.thelazy.net/index.php?title=Challenge%20of%20Dominance&action=raw` (redirect to
`Necromancer's Guild`) · `heroes.thelazy.net/index.php?title=Necromancer%27s%20Guild&action=raw`
Found: the contradicting source, Fandom `Necromancers' Guild`, Enroth section:
> "The new guild leader was Nimbus, but there was little necromantic talent to be found in
> either him or his apprentices. **Archibald defeated Nimbus in a duel, taking control of
> the guild.**"

Reason: A source does call it a duel, and it describes the format. The claim as written —
"There is no 'duel'" — is refuted. This is the project's signature failure mode, and it
failed in precisely the documented way: the negative was asserted after checking the two
obvious character pages (`Archibald`, `Nimbus`) and the primary Diaries, and the
counter-example sat one page over on the same wiki, on the institution page. `BH-2` says
check the disambiguation page before any negative claim; the generalisation this incident
demands is *check the institution/faction page too*.
What survives, and is worth keeping, is the narrower and more useful statement: **no game
text describes the format.** That I did verify — Entry 37 says only "I took it from Nimbus
in the guild Challenge of Dominance. Needless to say, I won," with no format, and neither
thelazy `Nimbus`, thelazy `Archibald`, Fandom `Nimbus` nor Fandom `Archibald Ironfist`
supplies one. Required rewrite, roughly: "No game text describes the format of the contest;
the Diaries say only *Challenge of Dominance*. Fandom's `Necromancers' Guild` page calls it
'a duel' without citation — an uncited embellishment, and one its own `Nimbus` page does not
repeat." That converts a refuted negative into a sourced observation, and it belongs
alongside A-15/A-16 as another instance of the same wiki-embellishment pattern.

### A-18
Claim: Kastore — one of four Terrans Archibald himself chose as advisors — staged a coup;
Archibald was not killed but ousted and fled.
Label in article: `T6 EXPLICIT` — `fandom-archibald-ironfist`
Verdict: CONFIRMED
Severity: MAJOR
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Archibald%20Ironfist&prop=wikitext` ·
`…&page=Kastore%20(Terra)` · `…&page=Deyja` ·
`mightandmagic.fandom.com/api.php?action=query&list=search&srsearch=%22Science%20arm%22` ·
`…&srsearch=%22ousted%20Archibald%22`
Found: **both quoted sentences are on the Fandom `Deyja` page, not on `Archibald Ironfist`.**
A site search for each quoted phrase returns exactly one page: `Deyja`. Verbatim there:
> "Thanks to several missions carried out by the Lords of Harmondale, Deyja was losing the
> war, and Kastore staged a coup and ousted Archibald from Deyja's throne. Archibald fled
> Deyja along with the necromancers from the Science arm."

The "four Terrans Archibald himself chose" half *is* on `Archibald Ironfist`: "These were
Kastore, Maximus, Dark Shade and Tolberti. Archibald chose them as his new advisors."
Reason: Content confirmed; two defects in how it is sourced.
1. **Wrong source key.** The two quotes are attributed to `fandom-archibald-ironfist` but
   live on `Deyja`. That page says something materially different from
   `Archibald Ironfist`, which words the same event as "Finally, the time came when Kastore
   asserted his claim to Deyja's throne… Archibald and his few loyalists bitterly departed
   Deyja". A reader following the citation will not find the quoted text. Add a
   `fandom-deyja` key to `REGISTRY.md` and re-point both quotes.
2. **Inserted word inside a quotation.** The article quotes "Kastore **later** staged a
   coup…". The source reads "and Kastore staged a coup…". "later" is not in the source. The
   meaning is unchanged, but a word silently added inside quotation marks is a quotation-
   integrity failure, and this project's whole method rests on quotations being exact.
   Delete it.
Also `T6 EXPLICIT` → `T6 INFERENCE`. One free gain: the `Deyja` page supplies the "Science
arm" / "Military arm" split that makes the coup intelligible — "The former Ultimate
Adventurers became Archibald's advisors and the leaders of the Military arm of Deyja, with
Archibald being at the head of the Science arm."

### A-19 ⚠️
Claim: There are TWO entities named `Kastore` in Old Universe sources.
Label in article: (unlabelled, flagged as open question)
Verdict: CONFIRMED
Severity: —
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Kastore&prop=wikitext` ·
`heroes.thelazy.net/index.php?title=Kastore&action=raw` ·
`mightandmagic.fandom.com/api.php?action=parse&page=Kastore%20(Terra)&prop=wikitext`
Found: Fandom `Kastore` disambiguation lists three, of which exactly two are Old Universe —
`Kastore (Terra)`, "the sorcerer from Might and Magic III and Might and Magic VII", and
`Kastore (Enroth)`, "the warlock from Heroes I and Heroes II". The third,
`Kastore (Ashan)`, is New Universe and out of scope.
Independently on thelazy `Kastore`, trivia: "A different Elven sorcerer also named Kastore
but hailing from Enroth was featured in Heroes I and Heroes II as a Warlock."
And Fandom `Kastore (Terra)` trivia adds why it matters: "A character named Kastore appears
as a playable Warlock hero in Heroes I and II, utilizing the portrait of Seymour from World
of Xeen. His presence here is non-canonical, as the Ultimate Adventurers did not reach
Enroth until a decade after the game's events."
Reason: Two Old Universe Kastores, confirmed on two independent wikis. The count of *two*
is right and the exclusion of the Ashan Kastore is right — a looser wording would have made
it three and been wrong. The claim carries no tier and sits in *Open questions*, which is
the correct placement, so no label defect. Note the structural echo of `BH-2`: as with
Sandro, the Heroes I/II hero portrait is recycled from a World of Xeen character. Worth a
cross-reference.

### A-20 ⚠️
Claim: Fulton: the MM7 team gave Archibald an undefined 'behind the scenes' role in the
Seeds of Discontent, so yes, Archibald did play a role in the Contested Lands becoming
independent.
Label in article: `T4 EXPLICIT` — `fulton-fanstratics-nl5`
Verdict: CONFIRMED
Severity: —
Searched: `homm.fandom.com/api.php?action=parse&page=Greg%20Fulton/Fanstratics%20Newsletters/5&prop=wikitext`
(`fanstratics.com` refused connection; `celestialheavens.com` returned 403; `miraheze`
served a bot challenge — the Fandom mirror carries the full text and links the
`web.archive.org` capture of the original at
`web.archive.org/web/…/https://www.fanstratics.com/fstnewsletter05`)
Found, Fanstratics Newsletter #5 (January 2021), Fulton answering question 24 about the
conclusion of `Seeds of Discontent`:
> "There was no planned 'official' story conclusion for the campaign. So, like many lore
> threads, we laid down enough story to satisfy the design requirements, then left the
> various elements to be possibly picked up by someone else at a later time. **This occurred
> when the MM7 team decided to give Archibald an undefined 'behind the scenes' role in the
> Seeds of Discontent. So, yes, Archibald did play a role in the Contested Lands becoming
> independent.**"

Reason: Verbatim match. Greg Fulton was HoMM3's lead designer and is the author of the
newsletter, so this is a developer statement — `T4 EXPLICIT`, correct tier and correct kind.
This is also the answer to the project's worst historical error: developer commentary on
Archibald exists, it is findable, and the article found it.

### A-21
Claim: Fulton uses the word "former": "Archibald's former 'Advisors' restored production
to… the 'Heavenly Forge'."
Label in article: `T4 EXPLICIT` — `fulton-fanstratics-nl4`
Verdict: CONFIRMED
Severity: NOTE
Searched: `homm.fandom.com/api.php?action=parse&page=Greg%20Fulton/Fanstratics%20Newsletters/4&prop=wikitext`
Found, Fanstratics Newsletter #4 (December 2020), Fulton answering question 12, "Can you
tell us more about the original version of AB with the Forge? What was the story and its key
characters?" — "Conceptually, the story went something like this… Following M&M7,
**Archibald's former 'Advisors'** restored production to an ancient wonder called the
'Heavenly Forge'. Using the Heavenly Forge, these Advisors could fashion any manner of
artifact or technology."
Reason: "former" is verbatim in Fulton's own words. `T4 EXPLICIT` correct. The article's
ellipsis elides "an ancient wonder called", which is fair.
NOTE on context the article should carry: this passage describes the **cancelled** Forge
storyline for `Armageddon's Blade`, prefaced by Fulton with "Conceptually, the story went
something like this…". So "former" is solid evidence that Fulton regarded Archibald as
having been displaced by his advisors — the word choice is what matters and it stands — but
the surrounding narrative is cut content and must not be cited as canon. One clause of
framing prevents a future reader mistaking the Forge plot for canon.

### A-22
Claim: On the Ironfist/Gryphonheart lineage contradiction, Fulton says it "looks like a
simple mistake".
Label in article: `T4 EXPLICIT` — `fulton-tavern-interview`
Verdict: CONFIRMED
Severity: —
Searched: `homm.fandom.com/api.php?action=parse&page=Gregory%20Fulton/Tavern%20of%20Might%20and%20Magic%20Interview&prop=wikitext`
Found: XEL quotes the pre-release 3DO short story — "The History of Erathia is long indeed,
and like the Ironfists of Enroth, the Gryphonhearts have been the ruling family since before
the Silence." — then sets it against the Heroes I manual letters establishing Lord Ironfist
arriving from another world, and Heroes II being 25 years later with Roland and Archibald as
his sons, "That makes Ironfists ruling from around 1126 A.S." He asks: "Was that backstory
subtly retconned…? Was it just a mistake? Or something else entirely?"
Fulton's reply, verbatim:
> "**GF**: To me, this looks like a simple mistake."

Reason: Exact quote, and the question is unambiguously the Ironfist/Gryphonheart lineage
contradiction the article describes. `T4 EXPLICIT` correct in tier and kind. A useful
adjacent detail on the same page for the article's dating discussion: Fulton states "I was
not involved in the conception or creation of SoD… Jennifer Bullard was the project's Lead
Designer" — so his authority does not extend to Shadow of Death content.

### A-23 ⚠️
Claim: `fulton-names-2023` contains NO entry for `Archibald`, `Ironfist`, or `Roland` — the
whole 98 KB was grepped.
Label in article: `T4 EXPLICIT` (negative result) — `fulton-names-2023`
Verdict: CONFIRMED
Severity: MINOR
Searched: `heroes.thelazy.net/index.php?title=Gregory%20Fulton/On%20Names%20in%20Heroes%20of%20Might%20and%20Magic%20III&action=raw`
Found: the document is **98,499 bytes** — the article's "98 KB" is exact. Header: "Interview
posted on 08/AUG/2023 on Celestial Heavens, detailing Amelrix's correspondence with Gregory
Fulton from 2022―2023." Case-insensitive counts over the whole file: `Archibald` **0**,
`Roland` **0**, `Morglin` 0, `Gryphonheart` 0, `Alamar` 0, `Ironfist` **2**.
Reason: The claim as *worded* is correct — no **entry** for any of the three. I reproduced
the byte count and the zero counts independently. Two things to note:
1. **The article's wording is load-bearing and must not be loosened.** A bare grep for
   `Ironfist` returns 2 hits, both the lowercase idiom in Fulton's own list of submitted
   names: "Lord Straker (knight); tough, **ironfist in velvet glove**, in your face to right
   a wrong." Neither is the Ironfist family. If the article ever restates this as "0
   occurrences of Ironfist" it becomes false. Recommend the article record the 2 idiom hits
   explicitly, so the distinction is preserved rather than depending on the reader parsing
   "entry" strictly.
2. **Label.** `EXPLICIT` means the source states the claim. No source states "Archibald has
   no name entry" — this is a verified absence, which is inference from silence, however
   well bounded. `T4 INFERENCE`, or a dedicated notation for verified-absence results, would
   be more honest. Same applies to A-26 and A-28; see the conclusion.

### A-24
Claim: Archibald appears as a hero in two Heroes II scenarios, with the stated stats for
`Apocalypse` and `Final Justice`.
Label in article: `T6 EXPLICIT` — `fandom-archibald-ironfist`
Verdict: CONFIRMED
Severity: MAJOR (label)
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Archibald%20Ironfist&prop=wikitext` ·
cross-checked against the `Apocalypse` and `Final Justice` scenario pages
Found: "Archibald makes appearances as a hero in two scenarios in ''Heroes of Might and
Magic II'': he is the main playable hero (red player) in Apocalypse… and is the main enemy
hero (red player) in Final Justice…"
Apocalypse — "he begins by default with a single Green Dragon, the Expert Scouting, Expert
Leadership and Advanced Wisdom secondary skills, and 6000 experience points (level 6).
Losing Archibald in battle results in defeat."
Final Justice — "Archibald starts at level 20 with 90000 experience points, possessing five
Black Dragons… His secondary skills include Expert Wisdom, Expert Luck, Expert Archery,
Expert Leadership and Expert Estates. Archibald cannot leave his starting zone."
Reason: Every figure in the claim matches — two scenarios, red in both, 6/6,000/1 Green
Dragon/Expert Scouting+Expert Leadership+Advanced Wisdom/loss-on-death, and
20/90,000/5 Black Dragons/the five Expert skills/cannot leave. Substance is clean.
`T6 EXPLICIT` → `T6 INFERENCE`. Worth noting these are map-file facts that could be raised
to real `T1` by reading the H2 scenario files — a natural `B-001` extension. Two MINOR
completeness points from the same source: Final Justice also gives him the Ultimate Shield,
an Arcane Necklace of Magic and a Foremost Scroll of Knowledge; and in Apocalypse he starts
with either the Ultimate Crown or Corlagon's army depending on whether the player played
`The Crown` or `Greater Glory`, which the claim mentions nowhere and which materially
changes the fight.

### A-25
Claim: His hero class in both scenarios is Warlock.
Label in article: `T6 EXPLICIT` — `fandom-archibald-ironfist`
Verdict: CONFIRMED
Severity: MAJOR (label)
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Archibald%20Ironfist&prop=wikitext`
Found: "In both scenarios, Archibald belongs to the Warlock hero class." Corroborated by the
page infobox — `class =[[Warlock (H2)|Warlock]]` — and by the `Final Justice` walkthrough,
"the player is required to battle him in his Warlock castle to win the scenario."
Reason: Explicit and triply corroborated on the page. `T6 EXPLICIT` → `T6 INFERENCE`;
same `B-001` note as A-24.

### A-26 ⚠️⚠️
Claim: Archibald is NOT a hero in Heroes III — verified by grepping seven Heroes III string
tables (~630 KB): 0 occurrences of `Archibald`.
Label in article: `T1 EXPLICIT` (negative result) — `h3wiki-herobios-txt`
Verdict: **CONTRADICTED**
Severity: **BLOCKER**
Searched: `heroes.thelazy.net/index.php?title=Alamar&action=raw` ·
`homm.fandom.com/api.php?action=parse&page=Alamar&prop=wikitext` ·
`heroes.thelazy.net/index.php?title=Gem&action=raw` ·
`heroes.thelazy.net/index.php?title=List%20of%20heroes&action=raw` ·
Fandom `Archibald Ironfist` infobox and categories
Found: the contradicting text is **inside the very file the claim cites**. Alamar is a
Dungeon Warlock present in Heroes III: Restoration of Erathia, and his in-game hero
biography reads, identically on thelazy and on `homm.fandom.com`:
> "Alamar served **Archibald** Ironfist during the Succession Wars, and was barely able to
> escape Enroth following **Archibald's** defeat. He has since taken up residence in Nighon
> where he secretly serves the Dungeon Overlords."

That is two occurrences of `Archibald` in `HeroBios.txt`.
Reason: The stated evidence is false, and **the article refutes itself**: A-09(a) cites
"Alamar's bio in `HeroBios.txt` — 'barely able to escape Enroth following Archibald's
defeat'" under the same source key, `h3wiki-herobios-txt`. A-09(a) and A-26 cannot both be
true. Either the grep did not actually cover `HeroBios.txt`, or it covered it and the "0
occurrences" figure is wrong; either way the claim as published is indefensible, and the
`~630 KB` / `seven string tables` / `0 occurrences` triple gives it a false air of rigour.
I could not audit the file set from outside, but the contradiction is internal and does not
depend on my file access.
**The headline survives on other evidence.** Archibald is genuinely not a Heroes III hero:
he appears in no town hero table on thelazy's `List of heroes` (Castle, Rampart, Tower,
Inferno, Necropolis, Dungeon, Stronghold, Fortress, Conflux, Cove, Factory, Bulwark), and
Fandom's `Archibald Ironfist` infobox places H3 under `mentioned`, not `appearances`, with
the prose "he was mentioned in Heroes of Might and Magic III: The Shadow of Death, …
Restoration of Erathia, … Armageddon's Blade".
Required fix: delete the "0 occurrences" evidence entirely and rest the claim on the hero
roster instead — an enumeration, which is the same technique that made A-04 sound. Then
state positively that `Archibald` *does* occur in H3 string data, in Alamar's bio, and
reconcile with A-09(a) and A-27 rather than contradicting them. As written this is the
mirror image of A-04: same negative claim, but evidenced by absence-search instead of
enumeration, and the absence-search was wrong.

### A-27 ⚠️
Claim: He is referenced in Heroes III game text — a HotA rumor: "Zog named his powerful
artifact in memory of Archibald. The usurper king and the Jackal were allies during the
Succession Wars."
Label in article: `T1* EXPLICIT` — `hota-beyond-the-horizon-rumors`
Verdict: CONFIRMED
Severity: —
Searched: `heroes.thelazy.net/index.php?title=Beyond%20the%20Horizon&action=raw`
Found: in the scenario's `=== Rumors ===` section, the row keyed to the artifact
`Ironfist of the Ogre` — "Zog named his powerful artifact in memory of Archibald. The
usurper king and the Jackal were allies during the Succession Wars."
Reason: Verbatim, in the rumor table of a HotA scenario, so it is in-game text reached
through a fan wiki — `T1*`, correct kind. The surrounding page confirms Zog is "the Jackal"
and the ogre High Chieftain, and that the enchanted hammer is the artifact in question.
This claim is also the natural anchor for repairing A-26, since it already establishes that
`Archibald` occurs in Heroes III–family game text.

### A-28 ⚠️
Claim: Grepping the entire HotA changelog (201 KB) gives 0 occurrences of `Archibald`, so
the project rule "for HotA use the changelog" is insufficient for lore.
Label in article: `T1* EXPLICIT` (negative result) — `hota-changelog`
Verdict: CONFIRMED
Severity: MINOR
Searched: `heroes.thelazy.net/index.php?title=Horn%20of%20the%20Abyss%20(Changelog)&action=raw`
(the `/Changelog` form 404s, as the claim table warns)
Found: file size **201,529 bytes** — the article's "201 KB" is exact. Case-insensitive
`Archibald`: **0**. For contrast, `Roland`: 1.
Reason: Independently reproduced, byte count and zero count both. The methodological point
is correct and useful: `BH-3` tells the project to prefer the changelog for HotA, and this
shows the changelog is a *gameplay-versioning* document that carries no lore, so `BH-3`
governs gameplay numbers only and lore must come from scenario text — which is precisely
where A-27 found it. Recommend `BH-3` be amended in `CLAUDE.md` to say so, since this is a
real limit on a rule the project treats as general.
MINOR, two label points: (1) `T1*` means in-game text via a fan wiki, and a changelog is
not in-game text — it is a developer-authored release document, closer to `T4`/`T2` in kind;
(2) as with A-23, `EXPLICIT` is wrong for a verified absence.

### A-29 ⚠️
Claim: Appearance table — H1 does not appear; H2 main antagonist, hero in 2 scenarios,
playable in his own campaign; MM6 stone statue, gives `Ritual of the Void`; MM7 King of
Deyja, Grandmaster trainer of Dark Magic, invites party to The Pit; H3 referenced in game
text only.
Label in article: `T6` + `T1 EXPLICIT` — `fandom-archibald-ironfist` +
`fandom-path-of-darkness` + `h3wiki-herobios-txt`
Verdict: CONFIRMED
Severity: MAJOR (label) + MINOR (incomplete)
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Archibald%20Ironfist&prop=wikitext` ·
`…&page=Path%20of%20Darkness` · Heroes I hero categories (see A-04) ·
thelazy `List of heroes`
Found: H1 — see A-04, absent from the full 36-hero roster. H2 — "He was first introduced as
the main antagonist of Heroes of Might and Magic II" plus the two-scenario statement quoted
at A-24. MM6 — quoted at A-11. MM7 — "He is the Grandmaster trainer of Dark Magic", and on
`Path of Darkness`, "You are thereafter invited to The Pit by Archibald Ironfist". H3 —
infobox `mentioned` field carries the H3 icons while `appearances` does not.
Reason: Every listed cell is supported. Two defects:
1. `T6 EXPLICIT` → `T6 INFERENCE` for the Fandom-sourced cells; and the `T1` cell inherits
   the A-26 problem, since `h3wiki-herobios-txt` is the key whose contents A-26 misreports.
   Re-derive the H3 row from the hero roster.
2. **Incomplete.** Fandom's infobox `mentioned` field also carries MM8 and Legends of Might
   and Magic, and the prose confirms: "he was mentioned in … Might and Magic VIII: Day of
   the Destroyer and in Legends of Might and Magic". The claim does not assert exclusivity,
   so it is not false — but an appearance table that silently omits two Old Universe titles
   invites the reader to conclude he is absent from them, which is the same shape of error
   as A-17. Add both rows, or state the table's scope. (Fandom's H6 `Reaper` class entry is
   correctly excluded as New Universe.)

### A-30 ⚠️
Claim: Archibald is NOT one of the two figures the party chooses between on the Path of
Darkness — those are Devon Sleen and Brandis Fairweather. Archibald invites the party to
The Pit after Sleen has been chosen.
Label in article: `T6 EXPLICIT` — `fandom-path-of-darkness`
Verdict: CONFIRMED
Severity: MAJOR (label)
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Path%20of%20Darkness&prop=wikitext` ·
`…&page=Deyja` · `…&page=Archibald%20Ironfist`
Found, Fandom `Path of Darkness`, opening sentences — the claim's three components in
order, in one passage:
> "The Path of Darkness is one of two branching paths in the main quest of Might and Magic
> VII: For Blood and Honor. **After choosing Devon Sleen over Brandis Fairweather** to
> replace Judge Grey, the party become close allies to the Necromancers of Deyja and
> permanently hostile to the Wizards of Bracada. **You are thereafter invited to The Pit by
> Archibald Ironfist** and tasked with escaping the Breeding Zone before becoming fully
> initiated."

Independently corroborated on Fandom `Deyja`, which describes the same choice from the other
branch: "Deyja's ambassador Scale recommended Judge Sleen as Grey's replacement… That plan
failed, however, as the Lords of Harmondale chose Bracada's Judge Fairweather as Grey's
replacement."
Reason: The negative is verified positively rather than by absence — the source names the
two candidates explicitly and assigns Archibald a distinct, later role, and a second page
independently names the same pair. This is the right way to evidence an exclusivity claim
and is the model A-26 should have followed. Only defect is `T6 EXPLICIT` → `T6 INFERENCE`.

### A-31 ⚠️⚠️
Claim: Diaries dates — official 3DO gives Entry 1 = 11 June 1165, Entry 37 = 23 October
1167, Entry 143 = 5 August 1168; thelazy gives 1165, 1166, 1167, off by exactly one year on
two of three.
Label in article: `T2 EXPLICIT` — `mm7-diaries-3do`
Verdict: CONFIRMED
Severity: MINOR
Searched, both sets independently as the claim table required:
`web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm` ·
`heroes.thelazy.net/index.php?title=Archibald&action=raw` · also checked
`web/20010401000000` (same content) and looked for a third witness on Fandom
(`The Diaries of Archibald` and `Diaries of Archibald` — neither page exists)
Found, 3DO: "Entry 1 / 11 June 1165"; "Entry 37 / 23 October **1167**"; "Entry 143 /
5 August **1168**".
Found, thelazy `Archibald`: "Entry 1 / 11 June 1165"; "Entry 37 / 23 October **1166**";
"Entry 143 / 5 August **1167**".
Reason: Both sets verified independently. The discrepancy is real, it is exactly one year,
and it affects exactly Entries 37 and 143 — every specific in the claim checks out.
MINOR, on framing rather than fact: the claim presents thelazy as the party in error
("thelazy gives… off by exactly one year"), but thelazy prefaces the Diaries with "''The
following is from the Might and Magic VII manual.''" — it claims to reproduce the printed
manual, while the 3DO page is the publisher's website. Those are two different artefacts,
and I found no third witness to adjudicate. The honest statement is that the 3DO website and
thelazy's transcription of the manual disagree by one year on two of three entries, with the
direction of the error undetermined. This matters downstream: A-14's chronology is
order-based, not year-based, so it is unaffected either way — but A-32's arithmetic is
year-based, so the article should not silently privilege one set. Getting a scan of the MM7
manual's diary pages would settle it; a `BACKLOG` item.

### A-32
Claim: Entry 1 says he was petrified ten years. 1154 + 10 = 1164 but Entry 1 is dated 1165,
so the article says "about ten years" and fixes no liberation year.
Label in article: `T2 EXPLICIT` + `T6 UNVERIFIED` — `mm7-diaries-3do` +
`thelazy-succession-wars`
Verdict: CONFIRMED
Severity: —
Searched: `web.archive.org/web/20001017212754/…/story.htm` ·
`heroes.thelazy.net/index.php?title=Succession%20Wars&action=raw`
Found, 3DO Entry 1: "so much has changed in **the ten years** I have been my brother's coat
rack". Dated 11 June 1165. thelazy `Succession Wars`: "A period in Enrothian history from
around the 1110s to **1154** AS".
Reason: The arithmetic is right and the handling is right. The `T2 EXPLICIT` / `T6
UNVERIFIED` split is exactly correct: the ten years and the 1165 date are explicit on the
official site, the 1154 endpoint is uncited wiki content and is properly marked
`UNVERIFIED`. Declining to fix a liberation year is the correct call — and note it is also
robust to the A-31 ambiguity, since Entry 1's date is the one date both sources agree on.
This is the best-labelled claim in the table.

### A-33 ⚠️
Claim: Succession Wars dating conflict — thelazy says "around the 1110s to 1154 AS", Fandom
`Archibald's campaign` infobox says 1151–1154 AS; the two differ by about forty years at the
start.
Label in article: `T6 EXPLICIT` — `thelazy-succession-wars` + `h2-archibalds-campaign`
Verdict: **CONTRADICTED**
Severity: MAJOR
Searched: `heroes.thelazy.net/index.php?title=Succession%20Wars&action=raw` ·
`mightandmagic.fandom.com/api.php?action=parse&page=Archibald%27s%20campaign&prop=wikitext` ·
`mightandmagic.fandom.com/api.php?action=parse&page=First%20War%20of%20Enrothian%20Succession`
Found: both quoted figures are accurate. thelazy — "from around the 1110s to 1154 AS".
Fandom infobox — `|date = 1151-1154 [[AS]]`.
But the contradicting text is the remainder of thelazy's own opening sentence, which the
claim truncates:
> "A period in Enrothian history from around the 1110s to 1154 AS when rulership of the
> Kingdom of Enroth **was contested twice**."

The page then splits into two headed sections, `== First War of Enrothian Succession ==`
("Depicted in Heroes I") and `== The Succession Wars ==` ("25 years later, after Morglin
Ironfist's death… Depicted in Heroes II").
Reason: There is no conflict to dispute. thelazy's 1110s–1154 span deliberately covers
**both** wars, Heroes I and Heroes II; Fandom's 1151–1154 covers **only** Archibald's
Heroes II campaign. The two are measuring different intervals and are mutually consistent —
1151–1154 sits inside 1110s–1154, and thelazy's own "25 years later" reconciles them.
Independently, Fandom's `First War of Enrothian Succession` page dates that first war to
"1110s-1120s AS", matching thelazy's start.
Presenting this in *Disputes* as a forty-year discrepancy misreads the source by quoting
half its first sentence. The "forty years" figure is arithmetically true and substantively
meaningless. Required fix: remove this from *Disputes*. If anything is worth keeping it is
the opposite observation — that the two wikis **agree**, and that the apparent gap is a
scope difference between "the Succession Wars period" (both wars) and "Archibald's campaign"
(the second war only). Note the article gets this distinction right elsewhere: A-04 and
A-32 both rely on the two-war reading. So this is a local slip, not a systematic
misunderstanding — but it is a slip that manufactures a dispute, which is worse than
omitting one. `T6 EXPLICIT` → `T6 INFERENCE` also applies.

### A-34
Claim: "Roland's campaign is the canonically true one" is widely repeated on Fandom and
carries no citation.
Label in article: `T6 FAN_THEORY` (in *Community theories*) — `h2-archibalds-campaign`
Verdict: CONFIRMED
Severity: —
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Archibald%27s%20campaign&prop=wikitext`
Found: "The two campaigns contradict each other, and Roland's campaign is the canonically
true one." The sentence is bare editor prose — no `<ref>`, no citation, no reference section
on the page.
Reason: Verbatim, and the absence of a citation is verifiable by inspection of the wikitext
rather than inferred. `T6 FAN_THEORY` in *Community theories* is exactly the right tier,
certainty and placement — the claim is about what the community repeats, not about canon.
Worth noting the underlying proposition is separately supported by A-09's game text, so the
article is right to keep the *uncited assertion* in `FAN_THEORY` while the *outcome* rests
on A-09. That separation is well judged.

### A-35 ⚠️
Claim: `Archibald Dawnsglow` exists — an expert Light Magic trainer in MM8, a different
character. Archibald Ironfist is a Grandmaster Dark Magic trainer in MM7.
Label in article: `T6 EXPLICIT` — `fandom-archibald-disambig`
Verdict: CONFIRMED
Severity: MAJOR (label)
Searched: `mightandmagic.fandom.com/api.php?action=parse&page=Archibald&prop=wikitext` ·
`…&page=Archibald%20Dawnsglow` · `…&page=Archibald%20Ironfist`
Found: Fandom `Archibald` disambiguation, both entries — "Archibald Ironfist, the evil
brother of Roland that appears in Heroes II, Might and Magic VI, and Might and Magic VII"
and "Archibald Dawnsglow, the expert light magic trainer in Might and Magic VIII".
On `Archibald Dawnsglow`: "Archibald Dawnsglow is a skill trainer in Might and Magic VIII:
Day of the Destroyer. He can be found in his home in Ravenshore and teaches expert Light
Magic." The `Archibald Ironfist` page carries `{{for|other characters of the same name|Archibald}}`
and is categorised `Might and Magic VII grandmaster trainers`.
Reason: Confirmed, and the Light/Dark contrast is exact — Dawnsglow expert Light in MM8,
Ironfist Grandmaster Dark in MM7. This is the `BH-2` discipline applied correctly: the
disambiguation page was checked and a genuine same-name collision was found and reported in
*Open questions*. Only defect is `T6 EXPLICIT` → `T6 INFERENCE`.
One connection the article should draw: the same disambiguation page is what would have
caught A-05, since the ambiguity there is also "which Archibald/which game". And A-19 is a
third instance of the same collision pattern. Three same-name collisions in one entity is
itself worth a line — it suggests the Old Universe recycled given names freely, and that
every name-based negative claim in this project needs a disambiguation check first.

---

## Kết luận

**Bài này CHƯA đạt `status: verified`.** Điều kiện là không còn `BLOCKER` và không còn
`MAJOR`; hiện còn **3 `BLOCKER`** và **12 `MAJOR`**.

Trước hết, phải nói rõ điều quan trọng nhất: **phát hiện trung tâm của bài là ĐÚNG.**
A-14, A-15, A-16 — cả ba đều `CONFIRMED`, kiểm verbatim trên nguồn gốc. Entry 37 và Entry
143 trên trang 3DO chính thức xác nhận hai sự kiện tách rời, đúng thứ tự, và cái thắng được
ở Challenge of Dominance đúng là "this little mission" chứ không phải ngai vàng Deyja. Cả
hai wiki lớn đều gộp hai sự kiện và đảo thứ tự, đúng như bài nói, và trang `Nimbus` của
thelazy đúng là tự mâu thuẫn với trang `Archibald` của chính nó. Đây là nghiên cứu nguồn gốc
thật, làm đúng cách. Ba `BLOCKER` bên dưới không chạm tới nó.

### `BLOCKER` — phải sửa

1. **A-05 — "Jerico" không phải tên in-game trong Heroes I.** Trong Heroes I ông chỉ là
   "Lord Ironfist". "Jerico" xuất hiện lần đầu ở **Might and Magic VIII**, trong mô tả vật
   phẩm Herald's Boots — cách Heroes I ba game. Và "Morglin" không *xuất hiện* trong manual,
   mà chỉ được *hàm ý* qua địa danh "Morglin's Keep" và sông Morglin. Nguồn phản bác chính
   là trang thảo luận mà banner rename của Fandom dẫn làm bằng chứng. Nguyên nhân lọt lỗi:
   banner viết "referred to in the game as 'Jerico'" mà không nói game nào.
2. **A-17 — "There is no 'duel'" bị phản bác.** Trang Fandom `Necromancers' Guild` viết
   thẳng: "Archibald defeated Nimbus in a duel, taking control of the guild." Đây đúng kiểu
   lỗi mà `BH-2` cảnh báo, và lọt theo đúng cơ chế đó: đã kiểm hai trang nhân vật hiển nhiên
   và nguồn Diaries, nhưng nguồn phản bác nằm ở **trang tổ chức/guild** ngay trên cùng wiki.
   Phần đáng giữ là mệnh đề hẹp hơn và mạnh hơn: *không có game text nào* mô tả thể thức —
   điều này tôi đã kiểm và nó đứng vững.
3. **A-26 — bằng chứng "0 occurrences of `Archibald`" là sai, và bài tự mâu thuẫn.** Bio
   in-game của Alamar trong `HeroBios.txt` chứa "Archibald" hai lần — và chính A-09(a) trích
   đúng câu đó, dưới đúng source key `h3wiki-herobios-txt`. A-09(a) và A-26 không thể cùng
   đúng. Kết luận đầu bài ("Archibald không phải hero Heroes III") vẫn đúng và có thể chống
   lưng bằng cách khác: liệt kê toàn bộ hero table — đúng kỹ thuật đã làm A-04 vững.

### `MAJOR` — phải sửa

4. **A-33 — bài tự tạo ra một tranh chấp không tồn tại.** Câu mở đầu của thelazy bị trích
   mất nửa sau: "…when rulership of the Kingdom of Enroth **was contested twice**". Con số
   1110s bao cả hai cuộc chiến (Heroes I + Heroes II); 1151–1154 của Fandom chỉ là campaign
   Heroes II. Hai bên **nhất quán**, không lệch. Bỏ khỏi *Disputes*.
5. **A-18 — sai source key + thêm chữ vào trong ngoặc kép.** Hai câu trích nằm ở trang
   Fandom `Deyja`, không phải `Archibald Ironfist`; cần thêm key `fandom-deyja` vào
   `REGISTRY.md`. Và bài viết "Kastore **later** staged a coup" trong khi nguồn không có chữ
   "later" — nghĩa không đổi nhưng đây là lỗi toàn vẹn trích dẫn, thứ mà cả phương pháp của
   dự án dựa vào.
6. **Chín nhãn `T6 EXPLICIT`** — A-04, A-05, A-11, A-24, A-25, A-29, A-30, A-33, A-35.
   Theo `CANON-POLICY`, `T6` không bao giờ chống lưng được `EXPLICIT`; hạ hết xuống
   `T6 INFERENCE`. Đây là một lần sửa cơ học. **Ngoại lệ có lý:** A-15, A-16 và A-34 nói *về
   chính chữ trên wiki*, nên ở đó wiki là nguồn sơ cấp cho văn bản của nó và `EXPLICIT` giữ
   được — nên ghi rõ một cụm để verifier sau không cắm cờ lại.

### `MINOR` / `NOTE` — nên sửa

7. A-09: tách nhãn — (a) và (c) `EXPLICIT`, nhưng **(b) chỉ là `INFERENCE`**, vì bio của Gem
   nói "Roland had secured the throne", không nói Archibald thua.
8. A-23 / A-26 / A-28: `EXPLICIT` không đúng cho *negative result* — không nguồn nào *phát
   biểu* sự vắng mặt. Nên dùng `INFERENCE`, hoặc thống nhất một ký hiệu riêng cho
   "verified absence".
9. A-31: đừng mặc định thelazy là bên sai. thelazy tự nhận trích **manual** MM7, còn 3DO là
   website nhà phát hành — hai artefact khác nhau, không có nhân chứng thứ ba. Chiều lệch
   chưa xác định. (Không ảnh hưởng A-14, vốn dựa trên thứ tự chứ không dựa trên năm.)
10. A-13 trả lại ngoặc kép châm biếm: those fool "adventurers". A-06 thêm dấu ba chấm khi
    cắt câu. A-08 hạ xuống "theo bản chép của Fandom" — chưa kiểm được lỗi *whose/who's* có
    trong file game gốc hay không.
11. A-29 thiếu MM8 và Legends of Might and Magic (Fandom xếp cả hai vào `mentioned`). A-24
    thiếu Ultimate Shield / Arcane Necklace / Foremost Scroll ở `Final Justice`, và thiếu
    nhánh Ultimate Crown-hoặc-quân-Corlagon ở `Apocalypse`.
12. A-03: cảnh báo mở — block `{{Text|…}}` trên trang Fandom `Archibald Ironfist` hiện
    "King Morglin Ironfist". Nếu đó là game text trung thực thì *có* game text gọi Morglin là
    cha, ngược với ghi chú thận trọng của bài. Chưa giải được nếu không đọc file H2.

### Ba điểm nên đưa vào `BACKLOG` / `CLAUDE.md`

- **Ba lỗi nặng nhất lần này lại đúng khuôn cũ.** A-05, A-17, A-26 đều là claim **phủ định
  hoặc độc quyền**, và cả ba đều trông giống sự cẩn trọng. Đối chiếu: A-04 và A-30 là claim
  phủ định *đúng*, và cả hai đều được chứng minh bằng **liệt kê đầy đủ** hoặc bằng **một câu
  khẳng định trực tiếp cho điều phủ định**, không phải bằng tìm-không-thấy. Đó là ranh giới
  cần thành luật: **claim phủ định chỉ được vào thân bài nếu chống lưng bằng liệt kê hoặc
  bằng phát biểu khẳng định — không bao giờ bằng kết quả grep rỗng.**
- **`BH-2` cần mở rộng.** Không chỉ trang disambiguation: nguồn phản bác A-17 nằm ở **trang
  tổ chức/định chế** (`Necromancers' Guild`). Và mô hình A-15/A-16 giải thích tại sao —
  trang nhân vật hay gộp và thêu dệt, trang phụ trợ thường chính xác hơn. Trước mọi claim
  phủ định: kiểm cả disambiguation **và** trang tổ chức liên quan.
- **`BH-3` cần giới hạn phạm vi.** A-28 chứng minh changelog HotA (201 KB) không chứa lore.
  Vậy "với HotA dùng changelog" chỉ đúng cho **số liệu gameplay/phiên bản**; lore phải lấy từ
  text scenario — đúng nơi A-27 tìm được. Nên ghi rõ giới hạn này vào `CLAUDE.md`.
- Ba trùng tên trong một entity (A-05 Jerico/Morglin, A-19 hai Kastore, A-35 Archibald
  Dawnsglow) cho thấy Old Universe dùng lại tên riêng rất thoải mái — thêm một lý do để
  bước disambiguation thành bắt buộc.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. Cả 3 BLOCKER và các MAJOR đã xử lý.

### Áp V4 — tự fetch lại bốn bằng chứng quyết định trước khi sửa

`VERIFY-PROTOCOL.md` mục 7 (V4, thêm cùng ngày sau sự cố verifier bịa trích dẫn ở bài `deyja`) buộc
người điều phối tự kiểm mọi trích dẫn verifier dùng làm bằng chứng quyết định. Kết quả:

| Bằng chứng | Kết quả tự kiểm | |
|---|---|---|
| `HeroBios.txt` chứa `Archibald` **5 lần** (bio Alamar, 4 cột ngôn ngữ + EN) | fetch 168.918 byte, đếm được **5** | ✅ |
| Fandom `Necromancers' Guild`: "Archibald defeated Nimbus in **a duel**" | có, nguyên văn | ✅ |
| thelazy `Succession Wars` câu đầy đủ có "**contested twice**" | có, nguyên văn | ✅ |
| Banner Fandom "referred to in the game as 'Jerico'" **không ghi game nào** | có; xác nhận banner không nêu game | ✅ |

*(Việc truy chữ "Jerico" về **MM8** (`Herald's Boots`) thì **chưa tự dựng lại được** — API trả lỗi cho
trang đó. Nên bài chỉ ghi "nguồn không nói game nào", không khẳng định MM8.)*

### Bảng xử lý

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| A-26 | "0 lần xuất hiện `Archibald`" trong string table — **và bài tự mâu thuẫn** | **BLOCKER** | Sửa hẳn. `HeroBios.txt` có **5 lần**, và **chính bài** trích đúng câu đó ở mục *Kết cục canon* dưới cùng source key. Đổi lập luận sang **liệt kê roster** (`INFERENCE`), và ghi rõ tên hắn **có** trong string table nhưng chỉ trong bio của hero khác |
| A-17 | "không có đấu tay đôi" | **BLOCKER** | Tách hai mệnh đề: **không game text nào** mô tả hình thức (`T2 EXPLICIT`, vẫn đúng) — nhưng **có một wiki nói "a duel"**, nên không được viết "không nguồn nào nói vậy". Đây là BH-2 điển hình: nguồn ngược nằm cách một trang trên **cùng** wiki |
| A-05 | "tên in-game ở Heroes I là Jerico" | **BLOCKER** | Cụ thể hơn điều nguồn cho phép. Banner Fandom chỉ nói "in the game", **không nói game nào**; trong Heroes I nhân vật chỉ được gọi "Lord Ironfist". Viết lại thận trọng, và bỏ claim gán "Jerico" cho Heroes I. Sửa cả ghi chú trong frontmatter |
| A-33 | Dựng ra một tranh chấp **không tồn tại** | MAJOR | Bài cắt câu nguồn giữa dòng. Câu đầy đủ có "**contested twice**" → khoảng 1110s–1154 phủ **cả hai** cuộc chiến, còn 1151–1154 chỉ là cuộc thứ hai. Hai nguồn **khớp nhau**. Đổi mục thành ghi nhận rằng đây **không** phải tranh chấp, kèm bài học |
| A-18 | Sai source key + chèn chữ vào trong ngoặc kép | MAJOR | Trích dẫn thuộc Fandom `Deyja`; và chữ "later" bị đặt **bên trong** dấu ngoặc. Đã sửa |
| 9× | `T6 EXPLICIT` — tổ hợp nhãn không hợp lệ | MAJOR | Hạ **năm** nhãn về `INFERENCE` (claim **về thế giới**). Giữ `EXPLICIT` cho các claim **về chính nội dung wiki** — xem ghi chú dưới |

### Một phân biệt cần đưa vào policy

`CANON-POLICY.md` mục 2 nói nguồn `T6` tối đa chỉ đạt `INFERENCE`. Quy tắc đó đúng khi wiki được dùng
làm **bằng chứng về thế giới truyện**.

Nhưng bài này có một loại claim khác: claim **về chính nội dung wiki** — ví dụ *"thelazy trang
`Archibald` viết X, còn trang `Nimbus` viết Y, nên nó tự mâu thuẫn"*. Ở đó, wiki **là đối tượng nghiên
cứu**, không phải nguồn tin, và trích dẫn nó **là** `EXPLICIT` theo nghĩa chặt: câu đó thật sự nằm ở đó.

Bài giữ `T6 EXPLICIT` cho bốn claim loại này và hạ năm claim loại kia. Sự phân biệt hiện **chưa có
trong policy** — đã ghi thành `B-021`.

### Phát hiện của verifier làm mạnh thêm luận điểm chính

Verifier xác nhận cả A-14/A-15/A-16 (phát hiện gốc của bài: hai wiki gộp sai hai sự kiện), và tìm
thêm: **Fandom cũng tự mâu thuẫn** — trang `Nimbus` và `Necromancers' Guild` chỉ trao **chức guild**,
còn trang `Archibald Ironfist` trao **ngai vàng**. Vậy **cả hai** wiki đều tự mâu thuẫn, không chỉ
thelazy. Đã bổ sung vào bài.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-archibald-ironfist-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.
