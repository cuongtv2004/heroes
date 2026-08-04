# Dossier research thô — `tarnum`

**Ngày fetch:** 2026-08-04 (đặt tên file theo đợt research 2026-08-03).
**Vai trò:** RESEARCHER. Đây là **dossier thô**, không phải bài viết. Không xuất bản.

## Phạm vi đã làm

| Priority | Trạng thái |
|---|---|
| P1 — tám campaign, các class | ✅ XONG (kèm **đính chính tiền đề**: sáu class, không phải tám) |
| P2 — Tarnum là ai, cơ chế bất tử, kết cục | ✅ XONG — tìm được **game text tường minh** cho cả cơ chế lẫn kết cục |
| P3 — quan hệ, trục thời gian | ✅ XONG phần lớn; xem `GAPS` |
| P4 — nguồn developer T4 | ✅ XONG — Ray, Bullard **có**; Fulton `On Names` **không có** (đã săn chủ động) |
| Ngoài đề bài | ⭐ Tìm được **site chính thức 3DO cho Heroes Chronicles** (T2) và **transcript game text Heroes IV** |

## Cách fetch

```bash
UA="Mozilla/5.0 (X11; Linux x86_64) HeroesCodexResearch/1.0"

# thelazy — wikitext thô (BẮT BUỘC có User-Agent)
curl -s -A "$UA" "https://heroes.thelazy.net/index.php?title=PAGE&action=raw"

# Fandom — chỉ qua API
curl -s "https://mightandmagic.fandom.com/api.php?action=parse&page=PAGE&prop=wikitext&format=json&formatversion=2"

# Wayback CDX — DÙNG filter=, KHÔNG grep
curl -s "http://web.archive.org/cdx/search/cdx?url=DOMAIN&matchType=domain&output=text&fl=original&collapse=urlkey&filter=original:.*PATTERN.*&limit=50"
```

⚠️ **CDX trả RỖNG khi bị rate-limit, không báo lỗi.** Đợt này đã bị đúng một lần: truy vấn
`3do.com` + `filter=.*chronicle.*` trả rỗng ở lần chạy đầu, chạy lại **cùng truy vấn** thì
ra 50 kết quả kèm cả một site chính thức. **Mọi claim phủ định dựa trên CDX phải chạy kèm
một truy vấn đối chứng (sanity control) đã biết chắc có kết quả.** Đây đúng là loại lỗi
BH của dự án: claim phủ định trông giống sự cẩn trọng.

---

# PRIORITY 1 — tám campaign và các class

## ⚠️ ĐÍNH CHÍNH TIỀN ĐỀ ĐỀ BÀI: **SÁU** class, không phải tám

Đề bài giả định "đổi class qua từng campaign" → tám class. **Sai.** Tám campaign nhưng chỉ
**sáu** class, vì Barbarian dùng lại cho **ba** campaign (`Warlords of the Wasteland`,
`The World Tree`, `The Fiery Moon`).

Ba nguồn độc lập xác nhận con số 6:

1. **`h3wiki-tarnum`** — bảng class có đúng 6 cột: Barbarian · Knight · Wizard · Ranger ·
   Beastmaster · Overlord. **FETCHED-VÀ-ĐỌC.**
2. **`h3wiki-heroes-chronicles`** (văn wiki) — *"The Chronicles follow the story of `[[Tarnum]]`,
   a `[[Barbarian]]` warlord who becomes a `[[knight]]`, a `[[wizard]]`, a `[[ranger]]`,
   a `[[beastmaster]]`, and an `[[overlord]]` in various quests given to him so he might
   redeem himself."* **FETCHED-VÀ-ĐỌC.**
3. **`fandom-tarnum`** Trivia (văn wiki, không dẫn nguồn) — *"He is the only character in
   ''Heroes of Might and Magic'' series to have 6 different classes."* **FETCHED-VÀ-ĐỌC.**

## Bảng class — trích nguyên văn wikitext từ `h3wiki-tarnum`

**Đây là BẢNG WIKI TỰ LẬP** (biên tập viên dựng từ dữ liệu trong file game), **không phải
game text**. Nó nằm ngoài mọi tham số template truyện. Nội dung bên trong (specialty,
starting skill) thì đối chiếu được với file game, nhưng bố cục và cột "Equivalent Hero"
là biên tập.

```wikitext
{| class="wikitable" style="background-color:#{{Green 4}}; color:darkslategray"
|-
! width="10%" style="background-color:#{{Green 2}};"| Class
! ... | [[Barbarian]] ! ... | [[Knight]] ! ... | [[Wizard]]
! ... | [[Ranger]] ! ... | [[Beastmaster]] ! ... | [[Overlord]]
|- valign="top"
! style="background-color:#{{Green 2}};" | Aliases
| King Tarnum<br>Barbarian King<br>Barbarian Tyrant
| Sir Tarnum
| Lord Tarnum
| Tarnum Dragonfriend
| Tarnum Hopewielder
| Overlord Tarnum
|- valign="top"
! style="background-color:#{{Green 2}};" | Special Ability
| ;[[Offense]]: Receives a 5% bonus per level to [[Offense]] skill.
| ;[[Ballista]]: Increases the [[Ballista|Ballista's]] [[Attack]] and [[Defense]]
    skills by 5% for every 5 levels (rounded up).
| ;[[Enchanters]]: Can upgrade [[Monk and Zealot|Monks, Zealots]],
    [[Mage and Arch Mage|Magi, and Arch Magi]] to [[Enchanter|Enchanters]].
| ;[[Sharpshooter|Sharpshooters]]: Can upgrade [[Archer and Marksman|Archers, Marksmen]],
    [[Wood Elf and Grand Elf|Wood Elves, and Grand Elves]] to [[Sharpshooter|Sharpshooters]].
| ;[[Basilisk|Basilisks]]: Increases the [[Speed]] of allied
    [[Basilisk and Greater Basilisk|Basilisks and Greater Basilisks]] by 1 and their
    [[Attack]] and [[Defense]] skills by 5% for every 4 levels (rounded up).
| ;[[Dragon|Dragons]]: Increases allied [[Dragons|Dragons']] [[Attack]] and [[Defense]] by 5.
|- valign="top"
! style="background-color:#{{Green 2}};" | Secondary Skills
| {{Ss3|Offense|Advanced}}
|| {{Ss3|Leadership|Basic}}<br>{{Ss3|Artillery|Basic}}
|| {{Ss3|Wisdom|Advanced}}
|| {{Ss3|Archery|Basic}}<br>{{Ss3|Leadership|Basic}}
|| {{Ss3|Armorer|Basic}}<br>{{Ss3|Resistance|Basic}}
|| {{Ss3|Tactics|Basic}}<br>{{Ss3|Estates|Basic}}
|-
! style="background-color:#{{Green 2}};" | Equivalent Hero
| {{Hn|Crag Hack|0=}} || {{Hn|Christian|0=}} || {{Hn|Dracon|0=}}
|| {{Hn|Gelu|0=}} || {{Hn|Bron|0=}} || {{Hn|Mutare|0=}}
|-
! style="background-color:#{{Green 2}};" | Notes
| || Starts with {{Cn|Ballista}} || Starts ''without'' a [[spell book]]! || || ||
|-
! style="background-color:#{{Green 2}};" | Campaigns
| • [[Warlords of the Wasteland]]<br>• [[The World Tree]]<br>• [[The Fiery Moon]]
|| • [[Conquest of the Underworld]]
|| • [[Masters of the Elements]]
|| • [[Clash of the Dragons]]
|| • [[Revolt of the Beastmasters]]
|| • [[The Sword of Frost]]
|}
```

⚠️ **Phạm vi con số gameplay:** mọi con số ở trên là **Heroes Chronicles**, engine
*Shadow of Death* (`h3wiki-heroes-chronicles`: *"They are based on the `[[Armageddon's Blade]]`/`[[Shadow of Death]]` engine"*).
**Không** có phiên bản HotA của Tarnum — đã kiểm, xem `GAPS`.

⚠️ **Fandom mô tả specialty khác thelazy về mặt công thức.** `fandom-tarnum` ghi Ballista/Basilisk là
*"for each level attained after 4th level"*, thelazy ghi *"5% for every 5 levels"* (Ballista) và
*"5% for every 4 levels"* (Basilisk). Hai cách diễn đạt **không tương đương**. Bài viết nên
dùng thelazy (`T1*`, khớp mô tả in-game) và **không** trộn hai cách.

## Tám campaign — bảng tổng hợp

Nguồn cột "Mô tả" = tham số `| description =` của template `{{Campaign}}` trên thelazy.
**Đây là GAME TEXT** (văn bản màn hình chọn campaign trong game), không phải văn wiki.

| # | Campaign | Class | Town | Mô tả (game text, `| description =`) |
|---|---|---|---|---|
| 1 | Warlords of the Wasteland | Barbarian | Stronghold | *"Before Tarnum became the Immortal Hero, he was a Barbarian who threw off the shackles of his Wizard masters and returned his people to their former greatness. This is his tale, and his downfall."* |
| 2 | Conquest of the Underworld | Knight | Castle | *"The Ancestors send Tarnum to help Queen Allison rescue the soul of her father from the depth of the Underworld. But the demons and undead are the least of his worries when Tarnum faces his past crimes."* |
| 3 | Masters of the Elements | Wizard | Tower / Conflux | *"Tarnum must face down his own prejudice against magic and become a Wizard if he has any chance of saving the world from the destructive Elemental Lords."* |
| 4 | Clash of the Dragons | Ranger | Rampart | *"When the good Dragons disappear, Tarnum is drawn into an epic battle with Mutare, the Dragon Queen. His greatest struggle, however, will be learning to be human again."* |
| 5 | The World Tree | Barbarian | Stronghold | *"Tarnum is drawn to a distant region to save the World Tree, that which gives life to all living things, from the Necromancers. But a far more dangerous enemy waits for the Immortal Hero — an enemy he has no chance of defeating."* |
| 6 | The Fiery Moon | Barbarian | Stronghold | *"The Ancestors have been kidnapped by Vorr, an Ancestor who has gone mad with his power. It is up to Tarnum to rescue the Ancestors and stop Vorr's mad plan to destroy the world."* |
| 7 | Revolt of the Beastmasters | Beastmaster | Fortress | *"Tarnum was the first to drag the Mudlanders into slavery when he was the Barbarian Tyrant. Now he has the chance to make amends and lead these people to freedom."* |
| 8 | The Sword of Frost | Overlord | Dungeon | *"The Elven Hero, Gelu, sets out to find the arcane Sword of Frost despite an apocalyptic prophecy. Now, the fate of the world depends on Tarnum's ability to rekindle his darkest talents and lead the devious creatures of Nighon against his former friend."* |

**Thứ tự trên là thứ tự PHÁT HÀNH**, do `h3wiki-heroes-chronicles` gọi từng cái là
"first/second/…/eighth episode". **Không phải** thứ tự niên đại — xem P3 và mâu thuẫn MT-1.

### Prologue của Historian cho mỗi campaign (GAME TEXT, đã fetch từng trang)

Nhân vật **`The Historian`** là người dẫn chuyện của toàn bộ Chronicles. Đây là thiết bị
khung truyện: Tarnum viết thư cho ông ta (xem "Letters from Tarnum" dưới đây).

1. **WOTW** — *"Tarnum was a barbarian king before he became the Immortal Hero. For years, no one could stop his reign of terror, but all things must come to an end. Upon his death, he entered the legendary hall of judgment, to stand before the ancient council. There, the ancestors found him unworthy of entering paradise, so they cast him back among the mortals where... Ah, but I get ahead of myself. You wanted to know how he became king."*
2. **COTU** — *"Ever have a dream you can't quite shake? It's called a vision, and Queen Allison had a nasty one. Her father's soul was torn from Paradise and dragged into the Underworld. Allison called for a hero to champion her. But only one responded: Tarnum."*
3. **MOTE** — *"The Elemental Lords, masters of Air, Earth, Water, and Fire, were free to tear the world apart now that a ten thousand year truce had come to an end. Only one with a powerful command over magic could stand a chance against them. So why did the Ancestors call on a Barbarian who hates magic to save us all?"*
4. **COTD** — *"Immortality has a drawback. Loneliness. But Tarnum found friendship with the long-lived dragons. And happiness in the joy they drew from each day. Then, one bleak morning, the dragons disappeared. Gone without explanation. And it was up to Tarnum to find out why."*
5. **TWT** — *"Somewhere in the dark tunnels beneath the earth was the World Tree. The wellspring of life. Tarnum had to find it before the insane ancestor Vorr and his minions, the necromancers, destroyed it. But how does one kill a god?"*
6. **TFM** — *"Tarnum's defeat of Vorr's allies, the necromancers, saved the World Tree from destruction but as long as Vorr was still out there Tarnum's task was far from over. What worried him most was the silence of the ancestors. Had they forsaken him? Or was it something more sinister?"*
7. **ROTB** — *"Tarnum awoke chained to the dank wall of an Erathian dungeon. A slave. The ancestors had sent him here to free the mudlanders and lead them back to their homeland. His were the first bonds to be broken. But they would certainly not be the last."*
8. **TSOF** — *"If Tarnum had known beforehand how things would end, he would not have held back. He would have surrendered his soul completely to his darkest desires. Nothing would have kept him from claiming the Sword of Frost."*

### Số map và cách bán (văn wiki `h3wiki-heroes-chronicles`, KHÔNG dẫn nguồn)

- WOTW 8 map · COTU 8 · MOTE 8 · COTD 8 · **TWT 5** · **TFM 5** · ROTB 8 · TSOF 8.
- WOTW/COTU/MOTE/COTD bán độc lập. **TWT tặng miễn phí** cho ai mua ≥2 tựa, **TFM** cho ai
  mua ≥3. ROTB + TSOF bán gộp thành ***The Final Chapters***.
- ⚠️ Đây là văn wiki. Nhưng **có nguồn T2 xác nhận một phần**: xem `chronicles-official-3do-features`
  ở P4 — tháng 02/2001 site chính thức 3DO chỉ liệt kê **bốn** tựa "Available Now".

---

# PRIORITY 2 — Tarnum là ai, vì sao sống lâu như vậy

## 2.1. ⭐ Cơ chế bất tử — GAME TEXT TƯỜNG MINH (không phải văn wiki)

Đề bài yêu cầu "tìm game text tường minh, đừng nhận văn wiki". **Tìm được.** Nằm trong
`=== Timed events ===` của scenario `Tunnels of Ice` (campaign *The Sword of Frost*) —
đúng như **BH-1**: nếu chỉ đọc prologue/epilogue thì trượt hoàn toàn.

**Nguồn:** `hc-tunnels-of-ice` · `heroes.thelazy.net/index.php?title=Tunnels_of_Ice&action=raw`
· GAME TEXT (nằm trong `{{TErow| … }}`).

**Day 23** — Tarnum tự đâm mình trước mặt tù binh Ufretin để chứng minh:

> *"I am immortal, Ufretin. I am not just long-lived like the Elves and Dragons. I am
> immortal - I can't die!"*
>
> *"You're a fool!"*
>
> *"I was a fool once, a cruel one, and I've been paying for my brutality ever since. I
> will probably pay for it until the end of time. That's why I am here! That's why I must
> stop Gelu! Gelu is about to destroy the entire world, and no matter what disgusting
> things I have to do I will not let him do it!"*
>
> *Before Ufretin could respond, I plunged my unseen dagger deep into my own heart.*

**Day 24** — hồi phục không để lại sẹo, và **giải thích cơ chế**:

> *"How do you feel today?" I asked.*
> *"Let me see your chest," he said.*
> *I opened my shirt. There wasn't even a scar where I had stabbed myself.*
> *"You just stood back up," the Dwarf said. "I watched it go in, I saw the blood myself,
> and then you just stood back up. How?"*
> *"Like I said, I am immortal."*
> […]
> *Finally, I told him how I died, and how the **Ancestors** refused to allow me to enter
> **Paradise**.*
> *"**I do what they ask - I am their servant until I can redeem myself.** But they have
> never asked me to fight against my friends before. I couldn't convince anyone else to
> fight Gelu!"*

**Kết luận có nguồn:** cơ chế **không phải** undead, **không phải** Ancients can thiệp.
Là **Ancestors** — hội đồng phán xét người Barbarian — từ chối cho vào Paradise và **giữ
hắn sống** như người hầu của họ cho tới khi chuộc xong tội. Hắn **hồi phục hoàn toàn** khỏi
vết thương chí mạng, không để lại sẹo.

⚠️ **Điểm tinh tế đáng ghi:** hắn **chết đi chết lại nhiều lần** (xem 2.4) rồi **quay lại**,
chứ không phải "không thể bị thương". Tự-mô-tả *"I can't die"* là lời **nhân vật**, không
phải mô tả cơ chế của người kể chuyện. Nên gán `INFERENCE` nếu bài muốn nói "hồi sinh"
thay vì "bất tử".

## 2.2. Ancestors là ai — có nguồn T4 trực tiếp

`h3wiki-ancestors` (văn wiki): *"The three Ancestors are powerful creatures who guard the
gates to Paradise… They are all mystically connected in some way - should one die, they
would all perish."* — **KHÔNG DẪN NGUỒN** cho vế "should one die, they would all perish".

Nhưng phần "Clarification" của trang này dẫn thẳng `bullard-interview-2013`, và bản mirror
đầy đủ có trên thelazy tại `Jennifer_Bullard/Acid_Cave_Interview`. **FETCHED-VÀ-ĐỌC** (13.712 byte):

> **Q:** *"Gods and Ancients - How are Ancestors and Ancients related?"*
> **A:** *"Ancestors were the biological start of the current crop of heroes. Ancients were
> often other powers who dabbled in the lives of mortals."*

> **A:** *"Think of the Ancestors as super powerful humans who have become legends to their
> descendants. Many people can view their ancestors as god-like, having done something truly
> heroic. Those are what the Ancestors were - people who went above and beyond with
> extraordinary skill and talent to do great things. **They had never been written into the
> Might & Magic Universe before the Heroes Chronicles. The "Gods" were more powerful than
> the Ancients.** Jon Van Caneghem was not involved in the Heroes Chronicles series - In
> fact I did a majority of the work myself."*

⚠️ **MÂU THUẪN MT-4 — wiki sửa lời phát biểu.** Trang `Ancestors` viết lại câu trên thành:
*"These 'Gods' could **potentially** be more powerful than the Ancients."* Bản transcript
gốc **không có** chữ "potentially" — nó là câu khẳng định: *"The 'Gods' **were** more
powerful than the Ancients."* Đây là **văn wiki làm mềm nguồn T4**. Bài viết phải dùng
bản transcript, không dùng bản tóm tắt.

## 2.3. Hắn bắt đầu là ai — Barbarian nổi dậy chống Bracaduun. ✅ ĐÚNG

`h3wiki-tarnum`, mục `==Biography==`. ⚠️ **Đây là GAME TEXT**: hai đoạn "Before his death"
/ "After his death" là **tiểu sử hero in-game** (biography), không phải văn biên tập:

> **'''Before his death:'''** *Tarnum is a young Barbarian who has spent his entire life
> under the oppression of the Wizard-Kings of Bracaduun, but he has always dreamed that
> life could be better - should be better.*
>
> **'''After his death:'''** *Judged by the Ancestors as unworthy of entering Paradise,
> Tarnum wanders the land seeking redemption for the crimes of his past. He is the Immortal
> Hero, a timeless protector, but personally troubled by the doubt that he can ever make up
> for the tremendous wrongs that he performed in his youth.*

Bối cảnh Bracaduun (`h3wiki-bracaduun`, **văn wiki, không dẫn nguồn**):

> *"Bracaduun was a powerful wizard empire which imposed its domination over other cultures…
> The wizards rose to dominance in Antagarich after Jarg's death, forming the Empire of
> Bracaduun. It was ruled by the Wizard-Kings, who oppressed the barbarians of the
> Wastelands… Bracaduun was eventually toppled by Tarnum. Some of the empire's former
> territories were soon united by Rion Gryphonheart into a new kingdom called Erathia."*

Xác nhận từ GAME TEXT — epilogue scenario `Steelhorn` (map cuối WOTW), `hc-steelhorn`:

> *The Historian: With the defeat of Castle Steelhorn, Tarnum shattered the power of the
> Wizard-Kings, but his tyrannical rule was short. Out of the ruins of the Empire of
> Bracaduun climbed the upstart nation of Erathia, and one day its king would defeat
> Tarnum, sending him before the Ancestors to be judged. But that is another story.*

⚠️ Chú ý: **campaign WOTW KHÔNG chứa cảnh Tarnum chết.** Nó dừng ở chiến thắng Steelhorn.
Cái chết được **thuật lại** trong epilogue và **chiếu** trong video intro
(`HC-01 … vid-Intro-smk-Intro.webm`, wiki chú thích *"King Tarnum duels Rion Gryphonheart"`).
Bất kỳ claim "trong WOTW ta thấy hắn chết" đều **sai**.

## 2.4. Danh sách các lần chết (văn wiki `h3wiki-tarnum`, mục `== Deaths ==`)

**KHÔNG DẪN NGUỒN** — biên tập viên tự tổng hợp. Nhưng 4/6 mục đối chiếu được với game text:

| # | Nội dung (nguyên văn) | Đối chiếu |
|---|---|---|
| 1 | *Killed by Rion Gryphonheart in a duel, thus ending the Barbarian Empire and beginning Erathia.* | ✅ khớp `hc-steelhorn` epilogue |
| 2 | *Killed by the forces of Duke Deezelisk when he betrayed Queen Allison.* | ⬜ chưa đối chiếu game text |
| 3 | ***Possibly*** *slain with his army on The Fiery Moon during an assault by Vorr, the insane Ancestor.* | ⚠️ wiki tự gắn "Possibly" |
| 4 | *Killed (and slew) Mad King Gryphonheart in a duel, thus winning the freedom of Tatalia.* | ⬜ chưa đối chiếu |
| 5 | *Killed himself to convince a captured Ufretin that Gelu needed to be stopped…* | ✅ khớp `hc-tunnels-of-ice` day 23 nguyên văn |
| 6 | *Slain on Axeoth by Vogel Backbreaker when Waerjak is attempting to unite the Barbarians.* | ✅ khớp `ch-h4-might-texts` (xem 2.5) |

## 2.5. ⭐ KẾT CỤC — có chết không, ở đâu? GAME TEXT ĐẦY ĐỦ

**Nguồn mới, chưa có trong REGISTRY:** `ch-h4-might-texts` —
`web.archive.org/web/2013/http://www.celestialheavens.com/homm4/texts/H4-MightTexts.rtf`
(61.771 byte RTF). Đây là **transcript text in-game của campaign Might Heroes IV
"Glory of Days Past"**. **FETCHED-VÀ-ĐỌC toàn bộ.**
⚠️ URL sống trả **403**; phải qua archive. Site này Celestial Heavens có **6 file
`H4-*Texts.rtf`** (Chaos/Death/Life/Might/Nature/Order) + H1 + H2. **Không có file
Chronicles** — xem `GAPS`.

Campaign giới thiệu (game text): *"The Reckoning and endless centuries of warfare have
brought the Barbarian people to the brink of extinction…"*

### Cái chết trên Axeoth — mục `==The Mortal Hero==`, scenario 3 `A King's Choice`

> *At the break of dawn, Vogel Backbreaker dragged Tarnum through Boernberg's main gate
> behind a horse. My foster father's hands and feet were chained. He was naked, bruised,
> and bloody. Vogel pulled him over the rocky landscape for more than three miles to a
> nearby ravine where a crowd waited.*
>
> *First, Vogel took a large mallet and shattered my father's knees. Then he did the same
> to Tarnum's arms. Those who watched agree that **Tarnum never screamed**.*
> […]
> *"Wait 'til you meet the Ancestors."*
> *Those were my father's last words.*
> […]
> *Vogel flung Tarnum's limp form into the ravine. Tarnum didn't scream. And as far as
> anyone knows, **his body still lies down there, unburied**.*

### Trở lại và TỪ CHỐI Paradise — mục `==The Immortal Hero==`, scenario 4 `One Tribe`

> *"Some call me the Immortal Hero," Tarnum explained. The Ancestors have kept him alive
> all this time so he could redeem himself for the horrible crimes of his distant past.*
>
> *"There is at least one historian recording my activities," Tarnum interrupted…*
>
> *"How can the Ancestors deny you Paradise now? You are the greatest man I have ever known."*
> […]
> *"They're not punishing me. In fact, everything you have done here has freed me from my
> debt. **For my part in raising you, the Ancestors have offered me Paradise, but I turned
> them down.**"*
>
> ***After more than a thousand years of life, why would Tarnum refuse that which he had
> been fighting for?***
>
> *"…**For the first time in a thousand years**, the Barbarian people have a real chance
> at a good life!… I am proud of you, son."*
>
> *That was the first time Tarnum called me son.*

**Câu thoại cuối cùng của Tarnum trong toàn series (game text, tag `Tarnum:`):**

> *"Until now, I thought all I wanted was the opportunity to enter Paradise and rest, but
> I feel these people have become my community. And I don't just mean Barbarians, but
> Palaedrans and Elves and all the others. I've been protecting them for so long, I feel
> like I'll be letting them down if I leave.*
>
> ***This new world still needs heroes.***"

**Trả lời P2 đầy đủ:**
- Có chết không? **Có, nhiều lần.** Lần cuối được kể chi tiết: bị Vogel Backbreaker tra tấn
  và giết trên **Axeoth**, xác ném xuống một khe núi gần **Boernberg**, không chôn.
- Kết cục cuối cùng? **Không phải chết.** Hắn **được xóa nợ**, được Ancestors **mời vào
  Paradise, và TỪ CHỐI**, tự chọn ở lại làm người bảo hộ trên Axeoth.
- ⭐ **Con số tuổi thọ có nguồn:** *"more than a thousand years of life"* — game text, đếm
  từ góc nhìn Waerjak. Đây là **neo tuổi thọ duy nhất bằng số** tìm được.

---

# PRIORITY 3 — quan hệ và trục thời gian

## 3.1. ⚠️ SANDRO — KIỂM LẠI CẢNH BÁO DISPUTED. Kết luận: **cảnh báo ĐÚNG, và mạnh hơn dự kiến**

Đã fetch lại **toàn bộ** `hc-truth-within-nightmares` (28.553 byte, đọc cả `=== Timed events ===`,
`==== Events ====`, roster hero).

**Bằng chứng khẳng định (GAME TEXT):**
- `| description =` (game text): *"Tarnum must **kill Sandro** to get the key to the next level."*
- `| victory =` (game text): *"Defeat Hero `{{gl|Sandro}}` the `{{gl|Necromancer}}`."*
- Timed event Day 1 (game text): *"Now, I must face Sandro, the Necromancer, who holds the key
  to the next level of the Underworld. He's not likely to give it up freely. Sandro dwells in a
  deepest, most vile parts of these caverns."*
- Map event (8, 46, 0) (game text): *"If you continue south you will find the path to the
  Necromancer known as Sandro, thus ending your quest."*
- Roster hero: `{{hero row|65, 47, 1|blue|Sandro|Necromancer}}` — phe **blue**, tầng ngầm.

**Ba phát hiện MỚI, phản bác cách đọc lười:**

1. ⭐ **Scenario này KHÔNG CÓ Epilogue.** Đã tìm `sed -n '/== Epilogue/,$p'` → rỗng. Nghĩa là
   **không có game text nào tuyên bố Sandro chết**. Mọi claim "Tarnum giết Sandro" chỉ dựa vào
   `| description =` và `| victory =`, tức **điều kiện thắng của người chơi**, không phải tường
   thuật. Điều này khớp chính xác với ghi chú `INFERENCE` đã có trong REGISTRY.
2. ⭐ **Không có timed event nào sau Day 85 nhắc Sandro.** Toàn bộ 20+ timed event từ Day 4
   trở đi là **hồi ức của Tarnum về gia đình và về Bracaduun** — nội dung thật của scenario là
   Tarnum nhận ra Allison là cháu ruột mình, không phải cuộc đối đầu với Sandro. Sandro chỉ
   xuất hiện ở **Day 1** rồi biến mất khỏi văn bản.
3. **Trang `Sandro` trên thelazy tự nêu vấn đề** — mục `=== Historical counterpart ===`,
   **VĂN WIKI, KHÔNG DẪN NGUỒN, dùng chữ "probably"**:

   > *"A character named Sandro was `[[Truth Within Nightmares|defeated]]` by `[[Tarnum]]`'s
   > Erathian forces in the `[[Underworld]]`. Although represented by Sandro in-game, **he is
   > probably only a namesake**, since according to Ethric and Jeddite, their Sandro became a
   > necromancer decades before the `[[Restoration Wars]]`, and those events happened centuries
   > prior. Also, the scenario description strongly hints that Tarnum killed the Underworld Sandro."*

**Mảnh T4 củng cố (mới, từ `bullard-interview-2013`):** Bullard nói rõ Chronicles được đặt hàng
làm sản phẩm **độc lập**, *"without any reference to each other or the other products in
development"*, mỗi truyện do **một level designer** viết rồi bà biên tập lại. Đây là lời giải
thích quy trình cho việc một cái tên bị tái sử dụng mà không nhất quán với dòng thời gian chính.

⚠️ Nhưng **Bullard không nói gì về Sandro cụ thể** → dùng nó là `INFERENCE`, không phải `EXPLICIT`.

**Đề xuất nhãn cho bài `tarnum`:**
`{T1* EXPLICIT: hc-truth-within-nightmares}` cho "có một hero tên Sandro the Necromancer là
mục tiêu chiến thắng của Tarnum ở tầng thứ ba của Underworld" ·
`{T1* INFERENCE: hc-truth-within-nightmares}` cho "Tarnum giết hắn" ·
`{T6 DISPUTED: h3wiki-sandro}` cho "có thể chỉ là trùng tên".

## 3.2. Jeddite — bốn key đã có trong REGISTRY: **xác nhận đúng, và Tarnum KHÔNG tương tác**

Bốn scenario `hc-tarnum-the-overlord`, `hc-the-dragon-mothers`, `hc-dragons-of-deepest-blue`,
`hc-old-wounds` đều là Chronicles và **Jeddite chỉ có mặt trong roster hero** (một dòng đặt hero
lên bản đồ), **không có text truyện nào**. Đã xác nhận lại `hc-tarnum-the-overlord`: fetch trang,
`| source = hc`, `| cback = chronicles 8`, không có Jeddite trong bất kỳ `{{TErow}}` hay
`{{Erow}}` nào.

⚠️ **Vì vậy: KHÔNG ĐƯỢC viết "Tarnum đối đầu Jeddite".** Quan hệ Codex đúng là **đồng-xuất-hiện
cơ học** (cùng file scenario), không phải quan hệ truyện. Nếu bài `tarnum` khai quan hệ tới
`jeddite`, nó phải nói rõ tính chất này, nếu không `check.py` sẽ đối lập với bài `jeddite`.

## 3.3. Gelu — quan hệ truyện THẬT, và là quan hệ quan trọng nhất

Toàn bộ campaign 8 là Tarnum chống Gelu. **Game text từ `| description =` và Historian prologue**
(đã trích ở P1). Thêm, từ `hc-tarnum-the-overlord` (`=== Timed events ===`, Day 1, GAME TEXT):

> *"If the Sword of Frost and Armageddon's Blade should ever meet, it would mean the end of the
> world!"*
>
> *How can that fool of an Elf go looking for the Sword of Frost? **I met Gelu once, and I found
> him to be an inspiring leader and dedicated fighter.**… But I've never known him to be stupid.*
>
> *So, I've come to Nighon in search of a force to battle Gelu and his Elves. Unfortunately, the
> Elf King will not lift a finger against AvLee's greatest hero. And the Erathians consider
> themselves allies… **My only resort is to don the dark armour of an Overlord** and somehow use
> the troops of Nighon for a good cause.*

Và từ **thư trong manual** (xem 3.6), Tarnum gọi Gelu là **bạn**: *"Do not assume our friendship
will restrain me."*

## 3.4. Kilgor — quan hệ GIÁN TIẾP qua Kija, có game text

`hc-a-new-enemy` (Historian prologue, GAME TEXT):
> *"Another set her eyes on the Sword of Frost… **Kija, the wife of the brutal Barbarian King
> Kilgor**, came to possess this dangerous blade. More than ever, Tarnum had to succeed."*

`hc-a-new-enemy` (timed event, GAME TEXT — lời Tarnum về dân tộc cũ của mình):
> *"**Kilgor now rules my people, and he's turned them into the blood thirstiest bunch of savages
> in all the land.** But still I had hope for my people."*

`hc-the-barbarians-wife` (timed event, GAME TEXT):
> *"…Kilgor, King of the Barbarians, she's a powerful warrior. She may not be insane like her
> husband, but she is driven by her ambition and her taste for cruelty."*
> — và ở chỗ khác: *"So, I was dealing with the **third wife** of Kilgor himself."*

⭐ **Tarnum và Kilgor KHÔNG BAO GIỜ gặp nhau.** Đối thủ trực tiếp là **Kija**. Đây là claim phủ
định đã săn chủ động: đã đọc toàn bộ 8 mô tả map của TSOF + prologue/epilogue + timed events của
`Tarnum the Overlord`, `A New Enemy`, `The Barbarian's Wife`, `The Capture`, `Tunnels of Ice`,
`The Protectors of the Sword`; Kilgor **chỉ được nhắc tới**, không xuất hiện.

## 3.5. ⭐ THE RECKONING — Tarnum là NGUYÊN NHÂN GIÁN TIẾP, do THẤT BẠI của hắn

Đây là phát hiện lớn nhất của P3. Chuỗi nhân quả **hoàn toàn bằng game text**:

`hc-the-protectors-of-the-sword` — epilogue campaign 8, tức **epilogue của toàn bộ Heroes
Chronicles**, GAME TEXT:

> *The Historian: Tarnum's hard-fought victory over the City of Volee was for naught. When he
> reached the resting place of the Sword of Frost he found that someone had already chipped it
> from its icy sheath. Among the broken ice was a discarded Barbarian Axe. Tarnum closed his fist
> around its hilt and screamed the name of the thief.*
> *"**Kija!**"*
> ***Why didn't he kill her when he held her captive?***
> *Then he prayed, "**Ancestors, please don't let my compassion destroy the world!**"*

Nối vào `thelazy-the-reckoning` (đã có trong REGISTRY): *"On February 10th, 1177 AS, a massive
explosion is created by the clash of Gelu's Armageddon's Blade and Kilgor's Sword of Frost…"*

**Chuỗi:** Tarnum bắt được Kija → **tha mạng** (hành động nhân từ, đúng bản chất "đã cải tà") →
Kija trộm Sword of Frost → giao cho Kilgor → Kilgor gặp Gelu → **The Reckoning** → Enroth bị hủy
diệt → dân chạy sang **Axeoth**.

⭐ **Đây là câu chuyện bi kịch trung tâm của nhân vật**, và nó là **thứ nối `tarnum` với
`the-reckoning`, `gelu`, `kilgor` bằng một sợi dây duy nhất.** Ghi chú `h3wiki-tarnum` (văn wiki)
cũng nói đúng ý này: *"Tarnum fails in this quest as the Sword of Frost is stolen by Kija and
given to her husband Kilgor, thus setting Gelu and Kilgor on a collision course that would end
with The Reckoning."*

## 3.6. "Letters from Tarnum" — text từ MANUAL chính thức, đã transcribe

`h3wiki-tarnum` mục `== Letters from Tarnum ==`: *"These letters appeared in the game manuals for
several of the `{{hc}}` games."* **Sáu thư**, mỗi thư ghi rõ manual nào. Đây là **text sản phẩm
chính thức**, không phải văn wiki — nhưng là bản chép lại trên wiki nên tier `T1*`.

| Thư gửi | Manual | Ký tên |
|---|---|---|
| the Historian | Warlords of the Wasteland | *Tarnum / The Immortal Hero* |
| Allison Gryphonheart | Conquest of the Underworld | *Sir Tarnum* |
| Gavin Magnus | Masters of the Elements | *Lord Tarnum / The Immortal Hero* |
| the Elf King | Clash of the Dragons | *Tarnum Dragonfriend / The Immortal Hero* |
| Erathia | Revolt of the Beastmasters | *Tarnum* |
| Gelu | The Sword of Frost | *Tarnum Dragonfriend* |

⚠️ **Không có thư cho The World Tree và The Fiery Moon** — khớp với việc hai tựa đó là bản tải
miễn phí, không có hộp/manual riêng.

⚠️ Wiki **tự gắn hai cảnh báo** vào các thư này (VĂN WIKI, đọc kỹ trước khi trích):
- Thư gửi Allison: *"'''NOTE:''' This letter is cut off at the end. **The final words are
  inferred.**"* — câu `"for Erathia ne[eds you]"` có phần trong ngoặc vuông là **wiki suy ra**.
- Thư gửi Gavin Magnus: *"'''NOTE''': As alluded to `[[The Trouble with Magic]]`, **this letter
  was actually sent by the Ancestors, not Tarnum**, who was initially unaware of the elemental
  threat…"* — đây là **suy luận của wiki**, chưa đối chiếu scenario `The Trouble with Magic`.

Thư gửi Historian là **khung truyện của cả series** — đáng trích trong bài:

> *"You say you are a historian - a noble pursuit… I was even more stunned that you know my
> secret… And yes, there is a hole in your records. My first reaction was to tear up your letter.
> That is a period of my life I would rather not conjure up again… So, I've agreed to help you on
> one condition - **leave nothing out, and change nothing, especially if it makes me look better.
> My story should be told as is, or not at all.**"*

Thư gửi Gelu (đối chiếu trực tiếp với 3.5):

> *"You must think your quest is for the benefit of us all, but you are misguided. Turn back now
> before you open a hornet's nest. Listen to me! **I will not allow you to succeed, no matter the
> cost. Do not assume our friendship will restrain me.**"*

## 3.7. Gia đình (văn wiki `h3wiki-tarnum` mục `== Relationships ==`, KHÔNG DẪN NGUỒN)

- **Hai chị/em gái:** `Anada` và một người không tên. Bracaduun cấm gia đình Barbarian có hơn một
  con nên hai người bị đưa đi. Tarnum ra lệnh tận diệt một bộ tộc Barbarian "phản bội" mà không
  biết hai chị em mình ở đó. **Anada bị chính quân của hắn giết**; người kia được **Rion
  Gryphonheart** cứu kịp.
- **Anh rể:** `Rion Gryphonheart` — chính người đã giết hắn.
- **Cháu gái:** `Allison`.
- **Người tình:** `Yalla`, `Adrienne`, `Valita`.

✅ **Phần lớn nội dung này ĐƯỢC XÁC NHẬN bằng game text** trong `hc-truth-within-nightmares`
(`=== Timed events ===`, đúng BH-1):

> **Day 68:** *"…Just as their clubs are about to smash her head to a pulp, a man on horseback
> comes out of nowhere. She's saved!… my sister's belly is plump with child - his child… Then the
> man finally turns in my direction and I can see his face. **It's Rion Gryphonheart!**"*
>
> **Day 71:** *"There she is, Queen Allison… The red hair, the sharp eyes - they are the same as
> my mother's, and the same as my sister's. How could I have missed it?… **My family!**"*
>
> **Day 85:** *"I've decided not to tell Allison who I am… I'm afraid if she learns that I used
> to be the Barbarian King that she will no longer trust me… I would love to embrace her as my
> niece."*

## 3.8. Waerjak — ⚠️ MÂU THUẪN GIỮA HAI WIKI

| Nguồn | Claim |
|---|---|
| `h3wiki-waerjak` (văn wiki, không dẫn nguồn) | *"**Foster son** of Tarnum and Adrienne."* |
| `fandom-tarnum` infobox (không dẫn nguồn) | `relatives = [[Waerjak]] - **son**` |
| `ch-h4-might-texts` (**GAME TEXT**) | Waerjak luôn gọi *"my **foster** father"*; Tarnum gọi *"son"* **lần đầu tiên** ở cảnh cuối, và Waerjak ghi nhận đó là **lần đầu** |

**Phán quyết đề xuất:** game text ủng hộ **foster son** (con nuôi), và khoảnh khắc Tarnum gọi
"son" là **điểm nhấn cảm xúc có chủ ý**, không phải khai báo huyết thống. Fandom sai.

⚠️ **Adrienne KHÔNG xuất hiện trong `ch-h4-might-texts`.** Đã grep toàn file: 0 kết quả cho
"Adrienne". Claim "Foster son of Tarnum and **Adrienne**" của thelazy **không có chỗ dựa** trong
text campaign Might H4. Ghi vào `SUSPECTED WIKI-ONLY CLAIMS`.

⚠️ `h3wiki-waerjak` còn nhắc lại claim *"Terry Ray mentioned in his notes that Waerjak, Lysander
and Gauldoth Half-Dead are brothers and illegitimate sons whom Nicolas Gryphonheart had by a woman
named Idune."* — REGISTRY đã có **cảnh báo về dòng dõi Gauldoth** liên quan chính claim này.
**Không dùng lại.**

---

# PRIORITY 4 — nguồn developer (T4) và nguồn chính thức (T2)

## 4.1. ⭐ Terry B. Ray — `ray-interview-ubisoft-2015` (T4, đã có trong REGISTRY)

**FETCHED-VÀ-ĐỌC toàn bộ** (49.048 byte HTML → 22.541 byte text) qua
`web.archive.org/web/20151020063103/http://mmh7.ubi.com/en/blog/post/view/lost-tales-q-a-with-terry-ray`.

**Cả bài chỉ có HAI câu nhắc Chronicles/Tarnum.** Đã grep case-insensitive toàn văn — không sót.

**(a) Xác lập thẩm quyền:**
> *"All told, I was hired to work on Heroes IV, but **also wrote the Heroes III Chronicles
> series**. I wrote for other games produced by 3DO too. It was a really busy time but I remember
> it fondly."*

**(b) ⭐ Nguồn gốc nhân vật — quan trọng nhất, xác nhận Trivia của wiki bằng chính lời tác giả:**
> *"Number three was Solmyr. Actually, I wish I had done more with him. He surprised me sometimes.
> **Tarnum from the Heroes Chronicles series is a close second. He is my Crag Hack, my very first
> D&D character that I brought to life in many tales.**"*

Đối chiếu: `h3wiki-tarnum` mục `== Trivia ==` (văn wiki, không dẫn nguồn) ghi *"'Tarnum' was
originally the name of Terry Ray's Dungeons & Dragons character."* → **XÁC NHẬN bằng T4**, và
Ray nói mạnh hơn: không chỉ cái tên mà **cả nhân vật**, và ông đã dùng nó *"in many tales"*
trước cả game.

⚠️ **Câu "He is my Crag Hack" là ẩn dụ về sự yêu quý** (Crag Hack là hero Barbarian biểu tượng
của H3), **không** phải claim rằng Tarnum và Crag Hack là một. Đừng đọc sai. (Ngẫu nhiên: bảng
"Equivalent Hero" ở P1 cũng ghép Tarnum-Barbarian với Crag Hack, nhưng đó là tương đương **cơ
chế game** — trùng hợp, không phải xác nhận.)

⚠️ **Ray KHÔNG nói gì về:** cơ chế bất tử, Ancestors, thứ tự niên đại, Sandro, hay bất kỳ chi
tiết cốt truyện Chronicles nào. Bài viết **không được** dùng nguồn này cho các điểm đó.

⚠️ **MÂU THUẪN MT-2 — ai viết Heroes Chronicles?**
Ray (T4, 2015): *"I… **also wrote the Heroes III Chronicles series**"*.
Bullard (T4, 2013): *"Jon Van Caneghem was not involved in the Heroes Chronicles series - **In
fact I did a majority of the work myself**"* và *"Each original story & maps was written by **one
level designer** and then **I** cleaned and polished them until ship."*
→ Hai nhà phát triển đều nhận công. **Có thể dung hòa** (Bullard = biên tập/chỉ đạo, Ray = một
trong các người viết) nhưng **không nguồn nào nói vậy**. Bài phải trình bày **cả hai lời**, gán
`DISPUTED`, **không được tự dung hòa**.

## 4.2. Jennifer Bullard — `bullard-interview-2013` (T4, đã có trong REGISTRY)

Mirror đầy đủ trên thelazy: `heroes.thelazy.net/index.php/Jennifer_Bullard/Acid_Cave_Interview`
(13.712 byte). **FETCHED-VÀ-ĐỌC.** Mục `== Heroes Chronicles ==` có **ba** cặp Q&A. Hai cặp đã
trích ở 2.2. Cặp thứ ba là **quan trọng nhất cho trục thời gian**:

> **Q:** *"…did you write Heroes Chronicles more like a stand-alone story of the immortal hero
> Tarnum or was it meant mostly to expand the history of the lands and worlds…?"*
>
> **A:** *"The Heroes Chronicles were meant to be more stand-alone than anything. Honestly, it
> was marketing who had the greatest hand in driving the products. **We were slipping on Heroes
> IV and they wanted our fan base to have more maps to play. So I was asked to create 8 campaigns
> that could stand alone and be played in any order, without any reference to each other or the
> other products in development.** So we created a series of titles that could do just that. Each
> original story & maps was written by one level designer and then I cleaned and polished them
> until ship. **Each one was supposed to take place in 'the distant past' and we didn't create a
> specific order to their events.**"*

⭐ Câu cuối là **T4 EXPLICIT bác bỏ sự tồn tại của một niên đại chính thức cho Chronicles**.
Nó **trực tiếp mâu thuẫn** với bảng niên đại fan dựng ở 5.x. Xem MT-1.

⚠️ Bullard cũng cảnh báo trong câu hỏi rằng fan *"are even finding references which may not
exist"* — nhưng lưu ý: **đó là lời NGƯỜI PHỎNG VẤN trong phần Q, không phải lời Bullard trong
phần A.** REGISTRY hiện có thể đang gán nhầm. **Kiểm lại trước khi trích.**

## 4.3. Gregory Fulton — `fulton-names-2023`: **KHÔNG CÓ GÌ VỀ TARNUM** (đã săn chủ động)

Fetch `Gregory_Fulton/On_Names_in_Heroes_of_Might_and_Magic_III` từ thelazy: **98.499 byte**,
khớp con số trong REGISTRY.

```
grep -n -i "tarnum\|chronicles" fulton.wiki   →   0 kết quả
```

**Kết luận phủ định có căn cứ:** tài liệu ~200 câu hỏi của Fulton về nguồn gốc tên **không hề
nhắc tới Tarnum, cũng không nhắc tới Heroes Chronicles**. Phù hợp với lời Bullard rằng Chronicles
là dự án tách biệt mà Fulton (Lead Designer H3) không tham gia. **Đây là "không tìm thấy" hợp lệ,
đã tìm ở đúng chỗ.**

## 4.4. ⭐⭐ SITE CHÍNH THỨC 3DO CHO HEROES CHRONICLES — **TÌM ĐƯỢC** (nguồn T2 mới)

Access note dặn "KIỂM XEM CÓ MỤC HEROES CHRONICLES KHÔNG" và cảnh báo "đường dẫn có thể có
THÊM MỘT TẦNG". **Cảnh báo đó đúng.**

**Đường đi tìm ra (ghi lại để lần sau khỏi mò):**
1. Index `3do.com/mightandmagic/` (bản `20011015110926`) — liệt kê Heroes IV, Heroes Dragon Bone,
   Legends, MM6, heroes3 (+complete/expansion/shadow/heroes2gold), MM7, arcomage, gameboy.
   **KHÔNG có link Chronicles.** ← nếu dừng ở đây thì báo âm nhầm, y như tiền lệ.
2. CDX toàn domain `3do.com` với `filter=original:.*chron.*` → ra `3do.com/chroniclesoffer/`.
3. Trang `chroniclesoffer/` (bản `20010124052100`) chứa link tới **`3do.com/products/pc/chronicles/`**
   — `main.html`, `story.html`, `features.html`, `gallery.html`, `downloads.html`, `boards.html`.

### `chronicles-official-3do-main` — T2, **FETCHED**

`web.archive.org/web/20010213215410/http://www.3do.com/products/pc/chronicles/main.html`

**BH-4 — dòng bản quyền trích nguyên văn từ chính trang:**
> *"© 2000 The 3DO Company. All Rights Reserved. Game specifications subject to change without
> notice."*

**Toàn bộ text hiển thị của trang (rất ngắn, nhưng là T2 thuần):**
> ***The Epic Tales of Tarnum, the Immortal Hero***
> - *Judged by the Ancestors to be unworthy to enter Paradise*
> - *Seeking redemption for the crimes of his bloody past*
> - *Tarnum is sent on a succession of quests*
> - *Combating evil to earn a reprieve from the gods*
> - *These classic adventures are recorded in the Heroes™ Chronicles*

⭐ Đây là **định nghĩa nhân vật do nhà phát hành viết**, tier `T2`. Nó xác nhận toàn bộ tiền đề
của P2 mà không cần dựa vào wiki.

### `chronicles-official-3do-features` — T2, **FETCHED**

`web.archive.org/web/20010303172743/http://www.3do.com/products/pc/chronicles/features.html`
(bản 03/03/2001). Bản quyền: *"© 2000 The 3DO Company. All Rights Reserved."*

> **Available Now**
> *Warlords of the Wasteland · Conquest of the Underworld · Masters of the Elements · Clash of the Dragons*
>
> **Features**
> - *A unique new series from the creators of Might and Magic® -- **four games** of challenge and
>   exploration with **interconnected storylines***
> - *Exclusive previews of every title on each CD in the form of playable mini-levels, so you can
>   try the others before you buy*
> - *Traditional addictive turn-based Heroes gameplay allows you to play at your own pace*
> - *Interactive preview and new-user training session on each game*

⚠️ **MÂU THUẪN MT-3 — "interconnected" vs "stand-alone".**
3DO (T2, 2000–2001, marketing chính thức): *"four games… with **interconnected storylines**"*.
Bullard (T4, 2013, người làm): *"8 campaigns that could **stand alone** and be played in **any
order**, **without any reference to each other**"*.
→ Đây là mâu thuẫn **marketing vs thực tế phát triển**, và nó rất đáng viết vào bài vì nó giải
thích **vì sao cộng đồng cứ cố dựng niên đại cho Chronicles**: chính bao bì sản phẩm hứa như vậy.

### `chronicles-official-3do-story` — T2, **FETCHED nhưng VÔ DỤNG**

`web.archive.org/web/20010216103413/http://www.3do.com/products/pc/chronicles/story.html`
(13.857 byte, bản quyền *"© 2000 The 3DO Company"*).
❌ **Toàn bộ nội dung truyện nằm trong ẢNH GIF** (`purple_text.gif`, `red_text.gif`,
`blue_text.gif`, `green_text.gif`, `t-warlords.gif`, `t-conquest.gif`, `t-masters.gif`,
`t-clash.gif`). Mọi `alt=""` đều **rỗng**. **Không trích được chữ nào.**
→ Về lý thuyết đọc được bằng OCR các GIF. Xem `GAPS`.

---

# SOURCE LIST

⚠️ Không key nào bắt đầu bằng số.

## Nguồn MỚI — đề xuất thêm vào `REGISTRY.md`

| Key đề xuất | Tier | Trạng thái | Nội dung |
|---|---|---|---|
| `h3wiki-tarnum` | `T1*` | **FETCHED** | Trang `Tarnum` thelazy, 18.754 byte — bảng 6 class, biography in-game, 6 thư từ manual, mục Deaths/Relationships/Story/Trivia |
| `h3wiki-heroes-chronicles` | `T6` | **FETCHED** | Trang series — 8 campaign, số map, mô hình bán hàng, tóm tắt class |
| `chronicles-official-3do-main` | **`T2`** | **FETCHED** | ⭐ Site **chính thức 3DO** `3do.com/products/pc/chronicles/main.html` qua archive `20010213215410`. *"© 2000 The 3DO Company"*. Định nghĩa Tarnum: *"The Epic Tales of Tarnum, the Immortal Hero"* |
| `chronicles-official-3do-features` | **`T2`** | **FETCHED** | ⭐ `…/features.html` (`20010303172743`). Bốn tựa "Available Now", claim *"interconnected storylines"* — **mâu thuẫn Bullard** |
| `chronicles-official-3do-story` | `T2` | **FETCHED (vô dụng)** | `…/story.html` (`20010216103413`) — nội dung truyện **nằm trong GIF**, `alt` rỗng, 0 ký tự trích được |
| `ch-h4-might-texts` | `T1*` | **FETCHED** | ⭐⭐ Transcript **text in-game campaign Might Heroes IV "Glory of Days Past"** — `celestialheavens.com/homm4/texts/H4-MightTexts.rtf` (61.771 byte) qua archive. URL sống trả **403**. Chứa cái chết cuối, cảnh từ chối Paradise, câu *"more than a thousand years of life"* |
| `hc-tunnels-of-ice` | `T1*` | **FETCHED** | ⭐⭐ Scenario TSOF #6 — **game text tường minh về cơ chế bất tử** (day 23–24). Nguồn xương sống của P2 |
| `hc-the-capture` | `T1*` | **FETCHED** | Scenario TSOF #5 — Tarnum bắt Ufretin; day-events cho thấy hắn trượt dần về con người cũ |
| `hc-a-new-enemy` | `T1*` | **FETCHED** | Scenario TSOF #3 — giới thiệu Kija; game text về Kilgor cai trị dân Barbarian |
| `hc-the-barbarians-wife` | `T1*` | **FETCHED** | Scenario TSOF #7 — Kija là **vợ thứ ba** của Kilgor; Tarnum bắt rồi tha |
| `hc-the-protectors-of-the-sword` | `T1*` | **FETCHED** | ⭐ Scenario TSOF #8 — **epilogue của toàn bộ Heroes Chronicles**. Kija cướp Sword of Frost |
| `hc-steelhorn` | `T1*` | **FETCHED** | Scenario WOTW #8 — epilogue nối Bracaduun sụp đổ → Erathia → Tarnum bị phán xét |
| `hc-warlords-of-the-wasteland-campaign` | `T1*` | **FETCHED** | Trang campaign 1 — `description` + prologue Historian + 8 mô tả map |
| `hc-conquest-of-the-underworld-campaign` | `T1*` | **FETCHED** | Trang campaign 2 |
| `hc-masters-of-the-elements-campaign` | `T1*` | **FETCHED** | Trang campaign 3 — prologue nêu "ten thousand year truce" |
| `hc-clash-of-the-dragons-campaign` | `T1*` | **FETCHED** | Trang campaign 4 — prologue nêu **cô đơn là cái giá của bất tử** |
| `hc-the-world-tree-campaign` | `T1*` | **FETCHED** | Trang campaign 5 |
| `hc-the-fiery-moon-campaign` | `T1*` | **FETCHED** | Trang campaign 6 |
| `hc-revolt-of-the-beastmasters-campaign` | `T1*` | **FETCHED** | Trang campaign 7 |
| `hc-the-sword-of-frost-campaign` | `T1*` | **FETCHED** | Trang campaign 8 — 8 tên map |
| `h3wiki-ancestors` | `T6` | **FETCHED** | ⚠️ Làm mềm lời Bullard: thêm chữ "potentially" không có trong transcript |
| `h3wiki-hall-of-judgment` | `T6` | **FETCHED** | Nơi Barbarian bị phán xét. Ngắn, không dẫn nguồn |
| `h3wiki-paradise` | `T6` | **FETCHED** | Cõi sau của Enroth; mục Trivia nối tới Ancients — **suy đoán, đánh dấu rõ** |
| `h3wiki-bracaduun` | `T6` | **FETCHED** | Đế chế Wizard-King. Không dẫn nguồn |
| `h3wiki-talk-timeline` | `T6` | **FETCHED** | ⭐ `Talk:Timeline`, 81.324 byte — niên đại fan dựng, **tự đánh màu** Explicit/Inferred/Conflicting/Likely-error/Best-guess. Mục Chronicles ở dòng 160–196 |
| `h3wiki-waerjak` | `T6` | **FETCHED** | ⚠️ Claim "foster son of Tarnum **and Adrienne**" không có chỗ dựa trong `ch-h4-might-texts` |
| `h3wiki-vogel-backbreaker` | `T6` | **FETCHED** | Hai câu, không dẫn nguồn |
| `fandom-tarnum` | `T6` | **FETCHED** | Infobox + gameplay + danh sách scenario H4. ⚠️ Ghi Waerjak là "son" (**sai**), ngày sinh/mất "ca first or second century AS" (**không dẫn nguồn**), công thức specialty **khác** thelazy |

## Nguồn ĐÃ CÓ trong REGISTRY — đợt này khai thác thêm

| Key | Tier | Trạng thái | Bổ sung mới |
|---|---|---|---|
| `ray-interview-ubisoft-2015` | **`T4`** | **FETCHED** | ⭐ Trích được **cả hai** câu về Chronicles/Tarnum. Câu *"He is my Crag Hack, my very first D&D character"* **xác nhận** Trivia của wiki bằng nguồn tác giả |
| `bullard-interview-2013` | **`T4`** | **FETCHED** | ⭐ Trích đầy đủ 3 cặp Q&A mục Chronicles. Câu *"we didn't create a specific order to their events"* là **T4 EXPLICIT bác bỏ niên đại Chronicles** |
| `fulton-names-2023` | **`T4`** | **FETCHED** | ❌ **KHÔNG có "Tarnum", KHÔNG có "Chronicles"** trong 98.499 byte. Phủ định đã săn chủ động |
| `hc-truth-within-nightmares` | `T1*` | **FETCHED** | Đọc lại toàn bộ 28.553 byte. ⭐ Phát hiện mới: **không có Epilogue**, và **không timed event nào sau Day 1 nhắc Sandro** |
| `hc-tarnum-the-overlord` | `T1*` | **FETCHED** | Đọc toàn bộ. Day-1 event là **game text quan trọng** về động cơ khoác áo Overlord |
| `h3wiki-sandro` | `T1*` | **FETCHED** | Mục `=== Historical counterpart ===` — văn wiki dùng chữ "probably", **không dẫn nguồn** |
| `thelazy-the-reckoning` | `T6` | **FETCHED** | Nối `The Protectors of the Sword` epilogue → 10/02/1177 AS |

## FAILED / NOT_FETCHED

| Key | Trạng thái | Lý do |
|---|---|---|
| `ch-h4-might-texts` (bản sống) | **FAILED** | `celestialheavens.com/homm4/texts/H4-MightTexts.rtf` trả **HTTP 403** khi truy cập trực tiếp. Phải qua `web.archive.org/web/2013/…` |
| `chronicles-official-3do-story-gifs` | **NOT_FETCHED** | Nội dung truyện T2 nằm trong GIF; cần OCR |
| `bullard-papers-ut-austin` | **NOT_FETCHED** | Đã có trong REGISTRY, vẫn chưa fetch |

---

# GAPS — tìm mà không thấy (ghi rõ đã tìm ở đâu)

1. **Không có transcript text in-game cho Heroes Chronicles ở Celestial Heavens.**
   Tìm bằng CDX toàn domain `celestialheavens.com`:
   - `filter=original:.*[Cc]hronicle.*` → **0 kết quả**
   - Đối chứng `filter=original:.*viewpage.*` → **10 kết quả** (rate-limit đã loại trừ)
   - `filter=original:.*\.rtf` → **10 file**: `homm1/texts/H1-Texts.rtf`,
     `homm2/texts/H2-Texts.rtf`, `homm4/texts/H4-{Chaos,Death,Life,Might,Nature,Order}Texts.rtf`,
     `homm4/usefulfiles/howtouseh4util.rtf`, `homm6/MMH6Readme.rtf`.
     **Không có H3, không có Chronicles.**
   → Nguồn game text tốt nhất cho Chronicles vẫn là **thelazy từng trang scenario**.

2. **Chưa đọc từng trang scenario của 6/8 campaign.** Mới đọc đủ: `Steelhorn` (WOTW #8),
   `Truth Within Nightmares` (COTU #3), và 5 scenario của TSOF. **Chưa đọc**: toàn bộ MOTE,
   COTD, TWT, TFM, ROTB, và 7/8 map của WOTW, 7/8 của COTU.
   → **Hệ quả cụ thể:** các lần chết #2 (Deezelisk) và #4 (Mad King Gryphonheart) trong bảng 2.4
   **chưa có game text chống lưng**. Muốn dùng phải đọc `Deezelisk`-scenario trong COTU và
   scenario cuối ROTB.

3. **Chưa fetch scenario H4 riêng lẻ** (`A New Way`, `A Necessary War`, `A King's Choice`,
   `One Tribe`). Nhưng `ch-h4-might-texts` **đã chứa toàn bộ text của cả bốn** nên gap này
   ít ảnh hưởng.

4. **Text truyện T2 trên `3do.com/products/pc/chronicles/story.html` chưa đọc được** — nằm trong
   4 file GIF (`purple_text.gif` = WOTW?, `red_text.gif`, `blue_text.gif`, `green_text.gif`).
   Cần OCR. Đây là **T2 duy nhất còn sót về cốt truyện** → đáng làm backlog.

5. **Không tìm được manual gốc dạng file** cho bất kỳ tựa Chronicles nào. Sáu lá thư hiện chỉ có
   qua bản chép trên thelazy (`T1*`, không phải `T1`). Liên quan `B-001`.

6. **Chưa xác định niên đại tuyệt đối cho WOTW.** `h3wiki-talk-timeline` để trống
   (`{{unk}}-1176`). `fandom-tarnum` đoán "ca first or second century AS" **không dẫn nguồn**.
   Game text `ch-h4-might-texts` cho *"more than a thousand years"* — nếu Reckoning là 1177 AS
   thì suy ra WOTW rơi vào khoảng **thế kỷ 1–2 AS**, khớp Fandom, nhưng đó là **INFERENCE của
   dossier này**, không nguồn nào nói.

7. **Heroes VII "Lost Tales of Axeoth: Every Dog Has His Day"** — cả thelazy lẫn Fandom đều nói
   Tarnum xuất hiện, **không nguồn nào dẫn game text**. Bài phỏng vấn Ray (chính là bài về
   Lost Tales!) **không nhắc Tarnum trong ngữ cảnh đó**. Chưa fetch nội dung campaign này.

## Claim phủ định ĐÃ SĂN CHỦ ĐỘNG và xác nhận (không suy từ im lặng)

| Claim phủ định | Cách săn | Kết quả |
|---|---|---|
| **Chỉ có MỘT Tarnum** (BH-2) | `list=allpages&apprefix=Tarnum` trên **cả hai** wiki | thelazy: `Tarnum` + 6 trang ảnh `Tarnum (Class)` + `Tarnum Dragonfriend`/`Tarnum Hopewielder` (**cả hai là `#REDIRECT [[Tarnum]]`**, đã fetch xác minh) + `Tarnum the Overlord` (**tên scenario**). Fandom: `Tarnum` + `Tarnum the Overlord`. **Không có trang disambiguation, không có Tarnum thứ hai, không có Tarnum (Ashan)** |
| **Không có phiên bản HotA của Tarnum** (BH-3) | Mục `== Appearances ==` của `h3wiki-tarnum` dùng `{{appear}}` với `nochrono=`; chỉ hai mục HotA là **`{{mention}}`** ở `The Life Guard` (`ai=`) và `Tomb Raiders` (`fif=`) | Tarnum **chỉ được NHẮC TỚI** trong HotA, **không là hero chơi được**. Không có changelog HotA nào cần đọc cho entity này |
| **Fulton không viết gì về Tarnum** | grep `-i "tarnum\|chronicles"` trên 98.499 byte `fulton-names-2023` | 0 kết quả |
| **Tarnum chưa từng gặp Kilgor** | Đọc toàn bộ 8 mô tả map TSOF + prologue/epilogue + timed events của 5 scenario TSOF | Kilgor chỉ được nhắc; đối thủ là Kija |
| **Không có Epilogue trong `Truth Within Nightmares`** | `sed -n '/== Epilogue/,$p'` | rỗng |
| **`3do.com` không có mục Chronicles** | ❌ **CLAIM NÀY SAI** — index `/mightandmagic/` không có link, nhưng CDX toàn domain **tìm ra** `/chroniclesoffer/` → `/products/pc/chronicles/` | Đây là tiền lệ mới: **index trang không phải là bằng chứng vắng mặt** |

---

# SUSPECTED WIKI-ONLY CLAIMS

Các claim dưới đây **chỉ tồn tại trong văn wiki**, không dẫn nguồn, và chưa đối chiếu được game
text. **Không được đưa vào thân bài** nếu không tìm thêm nguồn; nếu dùng phải gán `T6` và độ chắc
tương ứng.

1. `h3wiki-ancestors`: *"They are all mystically connected in some way - should one die, they
   would all perish."* — **không nguồn**, và không có trong transcript Bullard.
2. `h3wiki-ancestors`: *"These 'Gods' could **potentially** be more powerful…"* — **sai lệch so
   với transcript**, xem MT-4.
3. `h3wiki-waerjak`: *"Foster son of Tarnum **and Adrienne**."* — Adrienne **0 lần xuất hiện**
   trong `ch-h4-might-texts`.
4. `fandom-tarnum` infobox: `[[Waerjak]] - **son**` — **mâu thuẫn game text** ("foster father").
5. `fandom-tarnum` infobox: `birth = ca first or second century AS`, `death = ca first or second
   century AS (various successive deaths)` — **không nguồn**, là suy luận.
6. `fandom-tarnum` infobox: `status = Alive (as of Heroes IV)` — cùng loại lỗi mà REGISTRY đã bắt
   ở `fandom-jeddite-enroth` (*"suy luận từ roster"*). Ở đây thì game text **có** ủng hộ, nhưng
   Fandom không dẫn.
7. `h3wiki-tarnum` mục `== Deaths ==` — toàn bộ 6 mục là tổng hợp của biên tập viên; mục #3 wiki
   tự gắn chữ *"Possibly"*.
8. `h3wiki-tarnum` mục `== Story ==` và các danh sách `* Associates:` / `* Enemies:` — **văn biên
   tập viên**, nằm **ngoài** mọi template. Đây chính là ranh giới mà dự án quan tâm nhất: cùng
   một trang, phần trong `{| class="wikitable" |}` và các `{{TErow}}` là dữ liệu game, phần
   `== Story ==` là tóm tắt của người viết wiki.
9. `h3wiki-tarnum` NOTE về thư gửi Gavin Magnus (*"this letter was actually sent by the
   Ancestors, not Tarnum"*) — **suy luận của wiki**, chưa đối chiếu `The Trouble with Magic`.
10. `h3wiki-paradise` mục Trivia (*"Paradise may be connected to the Ancients…"*) — wiki tự dùng
    chữ "may", đây là `FAN_THEORY`.
11. `h3wiki-heroes-chronicles` mục `== Tarnum ==` (bảng so sánh với Crag Hack/Christian/…) — trùng
    nội dung bảng trên `h3wiki-tarnum`, không phải nguồn độc lập. **Đừng đếm là hai nguồn.**
12. `h3wiki-clash-of-the-dragons-campaign` trường `| information =`: *"Chronologically, it happens
    after `{{gl|Dragon's Blood}}` from `{{gl|Armageddon's Blade}}`"* — ⚠️ **claim niên đại nằm
    TRONG template nhưng KHÔNG phải game text**; `| information =` là trường mô tả của wiki, khác
    hẳn `| description =`. Dễ nhầm. Và nó **mâu thuẫn với T4 Bullard** (MT-1).

---

# TIMELINE

**Cảnh báo bao trùm — đọc trước khi dùng bất kỳ dòng nào dưới đây:**

> `{T4 EXPLICIT: bullard-interview-2013}` — *"Each one was supposed to take place in 'the distant
> past' and **we didn't create a specific order to their events**."*

Nghĩa là: **không tồn tại niên đại chính thức cho Heroes Chronicles.** Mọi thứ tự dưới đây là
**tái dựng của cộng đồng** (`h3wiki-talk-timeline`, `T6`) hoặc suy luận từ game text rời rạc.

| Mốc | Loại | Nguồn | So với Heroes I–IV |
|---|---|---|---|
| Jarg và Horde chinh phục Bracaduun, "near the Silence" | **tương đối**, văn wiki | `h3wiki-bracaduun` | rất lâu trước H1 |
| Wizard-Kings lập Empire of Bracaduun sau khi Jarg chết | **tương đối**, văn wiki | `h3wiki-bracaduun` | trước H1 |
| **WOTW** — Tarnum nổi dậy, lật Bracaduun, chiếm Steelhorn | **không có ngày** | `hc-warlords-of-the-wasteland-campaign`; `h3wiki-talk-timeline` để `{{unk}}` | trước H1 hàng thế kỷ |
| Rion Gryphonheart giết Tarnum trong đấu tay đôi; **Erathia ra đời** | **tương đối**, game text | `hc-steelhorn` epilogue | ⭐ **đây là mốc lập quốc Erathia** — nền cho toàn bộ H3 |
| Tarnum bị Ancestors phán xét, trở thành Immortal Hero | **tương đối**, game text | `hc-warlords-of-the-wasteland-campaign` prologue | — |
| **COTU** — Allison là Nữ hoàng, Rion đã chết | **tương đối** | `h3wiki-talk-timeline` (fan): *"story of Tarnum's niece Allison, so it is the second Tarnum scenario"* | trước H1 |
| **MOTE** | **tương đối** | fan: sau COTU vì Tarnum nhắc đã đánh Dungeon/demon | — |
| **ROTB** — lập quốc **Tatalia** | **tương đối** | fan: sau COTU (`The Ransom` kể chuyện Allison/Rion); trước TWT/TFM | ⭐ **Tatalia là một trong 8 quốc gia của H3** |
| **TWT** → **TFM** (nối tiếp trực tiếp) | **tương đối** | fan | — |
| ~1173–1174 AS: Mutare tấn công AvLee | **tuyệt đối** (Lost Lore) | `h3wiki-talk-timeline` màu ĐỎ | trong/sau H3 *Armageddon's Blade* |
| **COTD** ≈ 1173–1174 AS | **tuyệt đối (suy)** | fan, màu CAM | ⭐ **sau `Dragon's Blood` của AB** |
| 1175 AS: Mutare bị Dracon giết | **tuyệt đối** (Lost Lore) | `h3wiki-talk-timeline` màu ĐỎ | — |
| **TSOF** ≈ 1176 AS | **tuyệt đối (suy)** | fan, màu CAM. Neo: `Tarnum the Overlord` day 1 nói hắn tiếp quản Nighon trong khoảng trống quyền lực **sau khi Mutare chết**, và Gelu **đã có** Armageddon's Blade | ⭐ **sau H3 AB, ngay trước H4** |
| Kija cướp Sword of Frost giao cho Kilgor | **tương đối**, GAME TEXT | `hc-the-protectors-of-the-sword` epilogue | ngay trước Reckoning |
| **10/02/1177 AS — THE RECKONING** | **tuyệt đối** | `thelazy-the-reckoning` (⚠️ REGISTRY đã ghi mâu thuẫn 1177 vs 1178) | ⭐ **ranh giới H3 ↔ H4**; Enroth hủy diệt |
| Tarnum sang **Axeoth** cùng người tị nạn | **tương đối**, văn wiki | `h3wiki-tarnum` mục H4 | sau Reckoning |
| **"Glory of Days Past"** (H4, Might) — Tarnum bị Vogel giết ở Boernberg | **tương đối**, GAME TEXT | `ch-h4-might-texts` | ⭐ **trong Heroes IV bản gốc** |
| Tarnum trở lại, được xóa nợ, **TỪ CHỐI Paradise** | **tương đối**, GAME TEXT | `ch-h4-might-texts` scenario 4 `One Tribe` | **kết thúc cung nhân vật** |
| *"more than a thousand years of life"* | ⭐ **khoảng thời lượng, GAME TEXT** | `ch-h4-might-texts` | **neo tuổi thọ duy nhất bằng số** |
| Heroes VII *Lost Tales of Axeoth: Every Dog Has His Day* | **không có ngày** | `h3wiki-tarnum`, `fandom-tarnum` — **cả hai không dẫn game text** | sau H4 |

## Vị trí so với Heroes I–IV — tóm gọn

- **Heroes I & II** (Enroth, nhà Ironfist): xảy ra trên **lục địa/hành tinh khác nhánh truyện**;
  Chronicles diễn ra ở **Antagarich**. Không nguồn nào đặt Tarnum vào H1/H2.
- **Heroes III**: WOTW/COTU/MOTE/ROTB/TWT/TFM nằm ở **quá khứ xa** trước H3 (Erathia và Tatalia
  — hai quốc gia H3 — **do sự kiện Chronicles sinh ra**). COTD và TSOF thì **đồng thời/sau**
  H3 *Armageddon's Blade*.
- **Heroes IV**: TSOF dẫn thẳng vào Reckoning; Tarnum sang Axeoth và đóng vai người dẫn dắt
  Waerjak trong campaign Might.

---

# GHI CHÚ CHO NGƯỜI VIẾT BÀI

## A. ⚠️ Sửa tiền đề trước khi viết một chữ

Đề bài research nói "tám class". **Sai: sáu class / tám campaign.** Nếu bài mở đầu bằng "tám
class" thì luồng verify sẽ bắt ngay. Cách nói đúng: **"tám campaign, sáu class, vì Barbarian
dùng lại ba lần."**

## B. Biểu diễn nhiều class trong frontmatter — `SCHEMA.md` chỉ cho `hero` MỘT trường `class`

Ba phương án, xếp theo mức khuyến nghị:

**B1 — Khuyến nghị. Không đổi schema.**
```yaml
type: hero
class: Barbarian          # class GỐC và class hắn quay về, 3/8 campaign
```
rồi trong thân bài dựng **bảng sáu class** (bảng đã có sẵn ở P1, chỉ cần dịch tiêu đề cột).
Lý do chọn B1: `class` trong schema hiện mô tả **hero H3 chơi được**, và Barbarian là class
**duy nhất lặp lại**, cũng là danh tính gốc mà toàn bộ cung truyện xoay quanh ("một Barbarian
phải học làm Knight/Wizard/Ranger…"). ⚠️ **Phải chú thích ngay dòng đầu thân bài** rằng
frontmatter chỉ ghi class gốc, nếu không sẽ trông như thiếu sót.

**B2 — Nếu chấp nhận sửa schema.** Thêm trường **tùy chọn** `classes:` (số nhiều) chỉ áp dụng
cho `hero`, giữ `class:` bắt buộc như cũ:
```yaml
type: hero
class: Barbarian
classes:
  - { class: Barbarian,   campaigns: [warlords-of-the-wasteland, the-world-tree, the-fiery-moon] }
  - { class: Knight,      campaigns: [conquest-of-the-underworld] }
  - { class: Wizard,      campaigns: [masters-of-the-elements] }
  - { class: Ranger,      campaigns: [clash-of-the-dragons] }
  - { class: Beastmaster, campaigns: [revolt-of-the-beastmasters] }
  - { class: Overlord,    campaigns: [the-sword-of-frost] }
```
Ưu: dữ liệu máy đọc được, `check.py` kiểm chéo được. Nhược: **đụng schema và `tools/check.py`**
→ theo `CLAUDE.md` thì **phải hỏi user** trước khi push, vì đây là "thay đổi động tới `tools/`".
**Chỉ chọn B2 nếu Tarnum không phải trường hợp duy nhất** — hiện tại theo `fandom-tarnum` thì
hắn **là** duy nhất (*"the only character… to have 6 different classes"*), nên sửa schema cho
một entity là **quá tay**.

**B3 — Không khuyến nghị.** `class: Barbarian / Knight / Wizard / Ranger / Beastmaster / Overlord`
(chuỗi ghép). Làm hỏng mọi thứ dùng `class` để nhóm/lọc.

## C. Cấu trúc thân bài đề xuất

Nhân vật này **quá lớn cho bố cục tiểu sử tuyến tính**. Đề xuất:

1. **Ai là Tarnum** — mở bằng trích T2 chính thức (`chronicles-official-3do-main`), không mở bằng
   wiki. Đây là lần đầu Codex có nguồn `T2` mở bài cho một hero.
2. **Cơ chế bất tử** — dựng quanh cảnh `Tunnels of Ice` day 23–24. Đây là **đoạn game text mạnh
   nhất tìm được cho toàn entity**: hắn tự đâm mình để chứng minh với một tù binh. Vừa giải thích
   cơ chế, vừa cho thấy tính cách.
3. **Bảng tám campaign / sáu class** — bảng ở P1, cột "Mô tả" là game text.
4. **Bi kịch trung tâm: lòng nhân từ gây ra tận thế** — 3.5. Đây là **thứ nối bài này với
   `the-reckoning`, `gelu`, `kilgor`** và là lý do entity này đáng viết.
5. **Kết cục** — 2.5, cảnh từ chối Paradise.
6. **Vấn đề nguồn** — mục riêng cho MT-1…MT-4. Bài này **bắt buộc** phải có mục đó.

## D. Quan hệ nên khai (một chiều, theo quy ước dự án)

| Tới | Tính chất | Độ chắc đề xuất |
|---|---|---|
| `gelu` | đối thủ trong TSOF, **và là bạn cũ** | `T1* EXPLICIT` |
| `the-reckoning` | **nguyên nhân gián tiếp** qua việc tha Kija | `T1* EXPLICIT` (chuỗi có game text đủ) |
| `kilgor` | gián tiếp qua Kija; **chưa từng gặp mặt** | `T1* EXPLICIT` cho "gián tiếp"; ⚠️ **đừng khai là đối đầu trực tiếp** |
| `sandro` | mục tiêu chiến thắng trong `Truth Within Nightmares` | `T1* EXPLICIT` cho sự kiện; `T6 DISPUTED` cho danh tính |
| `jeddite` | ⚠️ **chỉ đồng-xuất-hiện trong file scenario**, không có tương tác truyện | nếu khai thì phải nói rõ; cân nhắc **không khai** |

⚠️ Bài `sandro` và bài `jeddite` **đã `verified`**. Mọi thứ bài `tarnum` nói về hai người này phải
**khớp** với những gì hai bài đó đã nói, nếu không `check.py` sẽ báo mâu thuẫn giữa hai bài.
**Đọc lại hai bài đó trước khi viết.**

## E. Cạm bẫy cụ thể của entity này

- **`| description =` là game text; `| information =` là văn wiki.** Cả hai nằm trong cùng
  template `{{Campaign}}`. Nhầm hai cái này sẽ biến một suy đoán niên đại của wiki thành "game
  text" — xem mục 12 của `SUSPECTED WIKI-ONLY CLAIMS`.
- **`The Historian` không phải người kể chuyện toàn tri.** Ông ta là **nhân vật** trong khung
  truyện, người mà Tarnum viết thư cho. Lời ông ta là game text, nhưng ông ta biết những gì
  Tarnum kể.
- **Timed events viết ở ngôi thứ nhất, giọng Tarnum** — đó là **nhật ký nhân vật**, không phải
  người kể chuyện khách quan. Khi Tarnum nói *"I can't die"*, đó là **hắn tự nhận**.
- **Đừng dùng "eight campaigns" và "eight classes" hoán đổi.**
- **Mọi con số gameplay phải ghi phạm vi:** "Heroes Chronicles (engine *Shadow of Death*)".
  Không có bản HotA của Tarnum.

---

# MÂU THUẪN GIỮA CÁC NGUỒN — tổng hợp

| Mã | Mâu thuẫn | Bên A | Bên B | Đề xuất |
|---|---|---|---|---|
| **MT-1** | **Chronicles có niên đại không?** | `bullard-interview-2013` (**T4**): *"we didn't create a specific order to their events"* | `h3wiki-talk-timeline` (T6): bảng niên đại chi tiết, TSOF ≈ 1176 AS, có neo `Lost Lore` màu đỏ | ⭐ **Không dung hòa được ở cấp nguồn.** T4 nói về **ý định thiết kế**; T6 tái dựng từ **văn bản đã ship**. Bài phải nói cả hai: *"Nhà thiết kế nói không có thứ tự; cộng đồng dựng được một thứ tự từ chi tiết trong game."* Gán `DISPUTED`. **Đây là mâu thuẫn quan trọng nhất của entity.** |
| **MT-2** | **Ai viết Heroes Chronicles?** | `ray-interview-ubisoft-2015` (**T4**): *"I… also wrote the Heroes III Chronicles series"* | `bullard-interview-2013` (**T4**): *"I did a majority of the work myself"*, mỗi truyện do *"one level designer"* viết rồi bà biên tập | Hai T4 chọi nhau. **Có thể** cùng đúng (Ray là một trong các level designer/writer) nhưng **không nguồn nào nói vậy**. **Trình bày cả hai, gán `DISPUTED`, KHÔNG tự dung hòa.** |
| **MT-3** | **"Interconnected" hay "stand-alone"?** | `chronicles-official-3do-features` (**T2**, 2000–01): *"four games… with **interconnected storylines**"* | `bullard-interview-2013` (**T4**, 2013): *"stand alone… played in any order, without any reference to each other"* | Marketing đương thời vs. hồi tưởng của người làm. **Đáng viết** — nó giải thích vì sao fan cứ cố dựng niên đại. Gán `DISPUTED`. |
| **MT-4** | **Ancestors mạnh hơn Ancients?** | `bullard-interview-2013` transcript: *"The 'Gods' **were** more powerful than the Ancients."* | `h3wiki-ancestors` diễn giải: *"These 'Gods' **could potentially** be more powerful…"* | **Wiki làm mềm nguồn T4.** Dùng transcript. Đây là ví dụ mẫu cho quy tắc "phân biệt game text với văn wiki" mở rộng sang "phân biệt transcript với tóm tắt". |
| **MT-5** | **Sandro trong `Truth Within Nightmares` có phải Sandro của Codex?** | Game text: tên, class Necromancer, là mục tiêu chiến thắng | `h3wiki-sandro` (T6, "probably"): niên đại lệch hàng thế kỷ; Sandro còn sống sau đó | **Cảnh báo DISPUTED cũ của dự án ĐÚNG.** Củng cố thêm: scenario **không có epilogue**, nên **không game text nào tuyên bố hắn chết**. |
| **MT-6** | **Waerjak là con ruột hay con nuôi?** | `ch-h4-might-texts` (**T1\***): *"my foster father"* xuyên suốt | `fandom-tarnum` infobox: `Waerjak - son` | Game text thắng: **con nuôi**. Fandom sai. |
| **MT-7** | **Công thức specialty** | `h3wiki-tarnum`: Ballista *"5% for every 5 levels"*; Basilisk *"5% for every 4 levels"* | `fandom-tarnum`: cả hai *"for each level attained after 4th level"* | Dùng thelazy (`T1*`). **Không trộn.** |
| **MT-8** | **Ngày The Reckoning** | `thelazy-the-reckoning`: *"February 10th, **1177** AS"* | Nguồn wiki tự dẫn là `Lost Manuscripts#11-08-**1178**` | ⚠️ **Mâu thuẫn CŨ, đã có trong REGISTRY, VẪN CHƯA GIẢI.** Chưa fetch `Lost Manuscripts`. |
