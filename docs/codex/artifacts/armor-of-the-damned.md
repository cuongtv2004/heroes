---
id: armor-of-the-damned
type: artifact
name_vi: Armor of the Damned
name_en: Armor of the Damned
aliases: []
appears_in:
  - sod-hack-and-slash
  - sod-rise-of-the-necromancer
  - sod-unholy-alliance
status: verified
verify_pass: verify-armor-of-the-damned-2026-08-03
slot: torso
artifact_class: relic
combo_parts:
  - skull-helmet
  - rib-cage
  - blackshard-of-the-dead-knight
  - shield-of-the-yawning-dead
blocks_slots:
  - helmet
  - weapon
  - shield
cost: 12000
sources_used:
  - h3wiki-armor-of-the-damned
  - h3wiki-skull-helmet
  - h3wiki-rib-cage
  - h3wiki-blackshard
  - h3wiki-shield-yawning-dead
  - h3wiki-orb-of-inhibition
  - h3wiki-trivia
  - h3wiki-weakness
  - h3wiki-ethric
  - h3wiki-artraits-txt
  - h3wiki-cuthbert
  - h3wiki-olema
  - h3wiki-mirlanda
  - h3wiki-eanswythe
  - h3wiki-ironfist-of-the-ogre
  - h3wiki-shield-of-the-damned
  - hota-changelog
  - sod-hack-and-slash
  - sod-unholy-alliance
  - sod-bashing-skulls
  - sod-black-sheep
  - sod-a-cage-in-the-hand
  - sod-grave-robber
  - sod-target
  - sod-wrath-of-sandro
  - sod-fall-of-sandro
relations:
  - type: assembled_from
    target: skull-helmet
    certainty: EXPLICIT
    source: h3wiki-armor-of-the-damned
  - type: assembled_from
    target: rib-cage
    certainty: EXPLICIT
    source: h3wiki-armor-of-the-damned
  - type: assembled_from
    target: blackshard-of-the-dead-knight
    certainty: EXPLICIT
    source: h3wiki-armor-of-the-damned
  - type: assembled_from
    target: shield-of-the-yawning-dead
    certainty: EXPLICIT
    source: h3wiki-armor-of-the-damned
  - type: appears_in
    target: sod-hack-and-slash
    certainty: EXPLICIT
    source: sod-bashing-skulls
open_questions: 5
---

# Armor of the Damned

## Tóm lược

Combination artifact thứ hai của [[sandro]], và là artifact mà hắn lừa **[[crag-hack]]** đi
thu thập hộ — bằng cách nói rằng hắn sẽ **phá hủy** nó.

Về cơ chế, nó có một đặc điểm bất thường: **bộ hoàn chỉnh không cho thêm một điểm chỉ số nào
so với bốn phần rời.** Toàn bộ giá trị nằm ở hiệu ứng — bốn spell cấp Expert, miễn phí, ngay
đầu trận.

Và về mặt kể chuyện, nó có một cái kết mỉa mai: lời nói dối của Sandro **cuối cùng thành sự
thật** — nhưng do kẻ thù của hắn thực hiện.

---

## Xuất xứ

### Không ai biết ai tạo ra nó

**Không game text nào nêu người tạo ra hay chủ sở hữu gốc của Armor of the Damned.**
Đây là kết luận sau khi săn chủ động, không phải suy từ im lặng.

⚠️ Claim "từng thuộc về [[ethric]]" **không có nguồn** — xem
[Điểm tranh chấp](#tranh-chap-ethric).

### Điều game text CÓ nói — và mỗi lần Sandro đều nói dối

Game không kể nguồn gốc Armor, nhưng nó kể **lai lịch gần đây của từng thành phần**. Và đây là
chỗ thú vị: **mỗi lần, lời của người đang giữ mới là lời đáng tin, còn lời Sandro là lời dối.**

| Thành phần | Sandro nói | Phía đối diện nói | Ai nói |
|---|---|---|---|
| Skull Helmet | Barshon "**unearthed**" nó | "It is **a family heirloom** handed down from generations" | **Barshon**, map event (54, 12, 0) |
| Blackshard | Marzeth **trộm** từ mộ anh hùng | Marzeth **thừa kế** nó; thanh kiếm bóp méo linh hồn hắn | ⚠️ **Tin đồn trinh sát**, timed event Day 14 — **không phải Marzeth** |
| Rib Cage | Necromancer **đốt Sanctuary** và trộm | "**We know nothing about a Sanctuary**, Mister Hack" | **Ebon Hand**, timed event Day 30 |
| Shield | Bị chiếm từ một vampire slayer | "the Shield of the Yawning Dead is **our relic**. It has been a part of our graveyard for many years" | **Hand of Death**, Day 15 |

{T1* EXPLICIT: sod-bashing-skulls + sod-black-sheep + sod-a-cage-in-the-hand + sod-grave-robber}

⚠️ **Dòng Blackshard không cùng loại với ba dòng kia.** Marzeth **không có một câu thoại nào** trong
toàn bộ `Black Sheep`. Phiên bản "thừa kế" là **tin đồn do trinh sát báo về**, và chính game text
**tự rào lại**:

> "Supposedly Marzeth was a Knight of the Blade who **inherited** the Blackshard, but the cursed sword
> twisted his soul until he became a Death Knight. This would explain why the humans are protecting
> him, but **it goes against Sandro's story** that Marzeth stole the sword from a warrior's tomb.
> **At best the rumor must be only half-true.**"

{T1* EXPLICIT: sod-black-sheep — timed event Day 14}

Nghĩa là ở ba dòng kia, người đang giữ **trực tiếp phản bác** Sandro; còn ở dòng Blackshard, game chỉ
đưa ra một tin đồn **và tự nói nó nhiều nhất là nửa đúng**. Bản đầu của bài xếp cả bốn vào cùng một
cột "người giữ nói", làm mất sự phân biệt đó.

Không lời nào trong số đó mô tả việc **tạo ra** Armor — chỉ là quyền giữ gần đây.

### Vụ lừa Crag Hack

Sandro không tự đi lấy. Hắn thuê một barbarian, và vỏ bọc là **ngược hoàn toàn** với sự thật:
hắn nói sẽ dùng bốn món để **phá hủy** Armor.

Mô tả campaign nói rõ khung: Crag Hack được thuê "to find the four pieces of the Armor of the
Damned **so he can destroy the cursed thing**". {T1* EXPLICIT: sod-hack-and-slash}

*(Câu này nằm ở trang **campaign** `Hack and Slash`, không ở trang scenario `Bashing Skulls` — bản đầu
của bài dẫn sai trang.)*

Giá: **500.000 vàng và một mảnh đất phong**.

> "Not only will I give you five hundred thousand gold pieces and a small land grant when you
> bring me these four items, but once they are assembled **I will be able to destroy The Armor
> of the Damned**, a magic artifact of unspeakable power and evil. NOW are you interested?"

{T1* EXPLICIT: sod-bashing-skulls — Day 1, quán Wingtail Tavern}

⭐ **Câu này đúng theo kiểu luật sư.** "Together, they can be assembled into a great weapon,
**a weapon that I desperately require**" — đó là **sự thật nguyên vẹn nằm bên trong lời nói
dối**. Sandro không nói sai điều gì về việc hắn *muốn* món đồ; hắn chỉ nói sai về việc hắn sẽ
*làm gì* với nó.

### ⭐ "Chúng sẽ nói dối anh" — thủ đoạn lặp lại ba lần

Đây là kỹ thuật đặc trưng của Sandro: **tiêm chủng trước** cho Crag Hack chống lại sự thật.

⚠️ **Ba trong bốn scenario, không phải cả bốn.** `A Cage in the Hand` **không có** thủ đoạn này —
grep độc lập trên trang đó cho `will lie`, `would lie`, `lies like`, `do not listen`, `lying`: **0
kết quả**. Lời Sandro ở scenario ấy chỉ cảnh báo về sự cản đường, không cáo buộc nói dối:

> "They will do everything in their power to stop you from obtaining it."

{T1* EXPLICIT: sod-a-cage-in-the-hand}

Bản đầu của bài ghi "cả bốn" và dẫn cả bốn source key — trong đó một key trỏ vào chỗ trống.

Và trong ba lần có thủ đoạn, **kẻ bị gọi là "nói dối" phần lớn đang nói thật** — nhưng đây là nhận
định của người viết, không phải điều game khẳng định. Với Marzeth thì game **tự phủ định** (xem bảng
trên: "at best the rumor must be only half-true").

{T1* INFERENCE: sod-bashing-skulls + sod-black-sheep + sod-grave-robber — đối chiếu lời Sandro với lời/tin đồn phía người giữ}

**Lần 1** (`sod-bashing-skulls`): "do not listen to anything he tells you... he has no honor
and **lies like a snake**."

Rồi Barshon gửi thư nói Helmet là gia bảo. Phản ứng của Crag Hack:
> "As you tear up the scroll you remember that Sandro said Barshon **FOUND** the Helmet. You
> shrug. Barshon is a lying snake."

**Lần 2** (`sod-black-sheep`) — Sandro dùng lại thủ đoạn để phủ nhận lời trăng trối:
> "**See, didn't I warn you he would lie to protect a mere possession?** And he dared to call
> himself a Barbarian! The coward had no honor. **I hope his death was a most painful one.**"
>
> "**Never before have you heard a Wizard talk so brutally.**"

⭐ Cùng scenario có một chi tiết rợn người — bằng chứng Sandro đang **thao túng tâm trí** cả
"đồng minh" của Crag Hack:
> "As you embrace your fellow Barbarian in a bear hug, **you notice that his eyes look
> vacant**. Although he has only kind words to say about Sandro, you wonder how the puny wizard
> really managed to persuade this stout Barbarian to assist you."

{T1* EXPLICIT: sod-black-sheep — map event 64,9,0}

**Lần 3** (`sod-grave-robber`) — phát biểu rõ nhất:
> "And one last thing. **Like the others you have battled, the Necromancers will lie to you.
> Do not listen to them.**"

{T1* EXPLICIT: sod-bashing-skulls + sod-black-sheep + sod-grave-robber}

*(Vỏ bọc "Sanctuary bị đốt" ở `A Cage in the Hand` **cũng** bị phản bác thẳng — "We know nothing
about a Sanctuary" — nhưng ở scenario đó Sandro **không** dùng thủ đoạn tiêm chủng trước. Xem bảng
đối chiếu ở mục trên.)*

### Sự nghi ngờ của Crag Hack — dựng theo ba giai đoạn

Game không để hắn ngu ngốc. Nghi ngờ được xây từng bước:

**Giai đoạn 1** — vết nứt đầu tiên, và nó rất hợp với nhân vật:
> "However, doing battle for this wizard is turning out not to be as much fun as you had hoped.
> **Sandro makes you think too much.**"

{T1* EXPLICIT: sod-a-cage-in-the-hand — Day 1}

**Giai đoạn 2** — nghi ngờ đã thành hành động:
> "As you leave the tavern you think about all the lies you have encountered on Sandro's tasks.
> **Maybe you should collect your rewards BEFORE handing over the last artifact.**"

{T1* EXPLICIT: sod-grave-robber — Day 1}

**Giai đoạn 3** — khoảnh khắc quyết định:
> "More lies, you think as you tear up the scroll, but still doubts remain. **Is Sandro the one
> who cannot be trusted?**"

{T1* EXPLICIT: sod-grave-robber — Day 15}

⭐ **Chi tiết cấu trúc đáng chú ý:** hành động **xé cuộn giấy** lặp lại đúng hai lần — ở
`sod-bashing-skulls` và ở đây. Cùng một cử chỉ, nhưng **lần thứ hai sự nghi ngờ sống sót qua
nó**.

Cũng trong lá thư đó, Hand of Death gọi Sandro là "**an acquaintance of ours**" — họ biết hắn
là đồng nghiệp necromancer. Vỏ bọc đang rạn từ phía bên kia.

### Epilogue

> "I've been tricked! The thieving Wizard took off with the artifacts and didn't give me my
> gold! When I find Sandro I'm going to rip his arms off and shove them down his lying throat!
> Argggggggggggggh!"

{T1* EXPLICIT: sod-grave-robber}

---

## Lịch sử sở hữu

| Giai đoạn | Ai giữ | Nguồn |
|---|---|---|
| Trước SoD | Bốn thành phần rải rác: Barshon, Marzeth, Ebon Hand, Hand of Death | {T1* EXPLICIT: sod-bashing-skulls + sod-black-sheep + sod-a-cage-in-the-hand + sod-grave-robber} |
| *Hack and Slash* | Crag Hack thu thập, tưởng là để phá hủy | {T1* EXPLICIT: sod-bashing-skulls} |
| *Rise of the Necromancer* | **Sandro** — mang bộ đã ghép | {T1* EXPLICIT: sod-target} |
| *Unholy Alliance* | Sandro | {T1* EXPLICIT: sod-wrath-of-sandro} |
| Sau đó | **Tháo rời, phân tán khắp Antagarich** | {T1* EXPLICIT: sod-fall-of-sandro} |

Game text xác nhận Sandro sở hữu **cả hai** artifact khi hắn là người chơi:

> "With the **Armor of the Damned** and the **Cloak of the Undead King** in your possession, you will
> easily overtake them and force these invaders out of your lands."

{T1* EXPLICIT: sod-wrath-of-sandro — timed event Day 4}

⭐ Có một chi tiết đáng chú ý về giai đoạn cuối: khi Sandro **trở lại làm địch** ở các map cuối, hắn
mang Armor of the Damned nhưng **không có** Cloak of the Undead King.

{T6 EXPLICIT: sod-unholy-alliance — mục `Important information`, **văn biên tập viên wiki**, không phải game text}

⚠️ Bản đầu của bài gán claim này `T1* EXPLICIT` và dẫn `sod-wrath-of-sandro`. Cả hai đều sai: câu đó
nằm ở trang campaign *Unholy Alliance* trong mục `== Important information ==`, tức **văn biên tập
viên** nằm ngoài mọi template → `T6`. Đây là quan sát cơ chế của người chơi, có thể đúng, nhưng không
phải điều game nói.

### Kết cục — và một sự mỉa mai hoàn hảo

Epilogue của Yog:

> "After realizing how corrupting **these artifacts** are, we decided to split them up into
> less powerful components and disperse them throughout Antagarich."

{T1* EXPLICIT: sod-fall-of-sandro}

"These artifacts" là **số nhiều và không nêu tên** — bao gồm cả Armor lẫn
[[cloak-of-the-undead-king]]. Epilogue **không bao giờ gọi tên** artifact nào.

⭐ **Chúng bị tháo rời và phân tán — không bị phá hủy.**

Đây là cái kết mỉa mai của toàn campaign: các thành phần trở về đúng trạng thái ban đầu — rải
rác khắp Antagarich, trong tay những người giữ khác nhau. Và **lời nói dối của Sandro với Crag
Hack — rằng Armor sẽ bị phá hủy — cuối cùng được thực hiện, dưới dạng biến thể, bởi chính kẻ
thù của hắn.**

---

## Gameplay

### Cơ chế gốc

| Thuộc tính | Giá trị |
|---|---|
| Slot | Torso |
| Class | Combination (Relic) |
| Giá | 12.000 |
| Chặn slot | Helmet, Weapon, Shield |
| Chỉ số | +3 Attack, +3 Defense, +2 Power, +2 Knowledge |

{T1* EXPLICIT: h3wiki-armor-of-the-damned}

**Mô tả in-game, nguyên văn từ file game:**

> "All opponents have these spells effective on them for fifty turns: **Slow, Curse, Weakness, and
> Misfortune**."

{T1 EXPLICIT: h3wiki-artraits-txt}

⭐ **Đây là `T1` thật, không dấu sao** — `H3Bitmap.lod > artraits.txt`, string table trích trực tiếp
từ file game. **Bốn spell.** Không phải năm, không có biến thể "Mass" — xem *Điểm tranh chấp*.

⚠️ **Bản đầu của bài dẫn một câu Fandom và gọi đó là "mô tả in-game". Câu đó không phải mô tả
in-game.** Đối chiếu:

| | Chuỗi thật (`artraits.txt`) | Câu Fandom |
|---|---|---|
| Thứ tự spell | Slow, **Curse**, Weakness, **Misfortune** | Slow, **Weakness**, **Misfortune**, Curse |
| Chủ thể | "**All opponents** have these spells effective on them" | "casts ... **on the enemy**" |
| Thêm vào | — | "**Worn on the torso**", "at the start of **every battle**" |
| Trùng khớp | "fifty turns" | "fifty turns" |

Chỉ hai chữ "fifty turns" là trùng. Câu Fandom là **diễn giải**, không phải chuỗi game — nên
`fandom-artifact-list` đã được bỏ khỏi bài này.

⚠️ **Trường `| effect =` trên trang wiki cũng KHÔNG phải in-game text.** Câu "Casts Expert Slow,
Curse, Weakness, and Misfortune for 50 rounds at the start of combat" là cách biên tập viên tóm tắt
cơ chế, không phải chuỗi nào trong game. Vế "bốn spell" của nó vẫn đúng và khớp `artraits.txt`.

**Text khi nhặt:**
> "You trip over the Armor of the Damned, dust it off, and stick it in your pack."

### ⭐ Bộ hoàn chỉnh không cho thêm chỉ số nào

Đây là điểm bất thường đáng ghi:

| | Attack | Defense | Power | Knowledge |
|---|---|---|---|---|
| Skull Helmet | — | — | — | +2 |
| Rib Cage | — | — | +2 | — |
| Blackshard | +3 | — | — | — |
| Shield of the Yawning Dead | — | +3 | — | — |
| **Cộng lại** | **+3** | **+3** | **+2** | **+2** |
| **Bộ hoàn chỉnh** | **+3** | **+3** | **+2** | **+2** |

Giá cũng khớp: 4 × 3.000 = 12.000.

→ **Ghép bộ không cho thêm một điểm nào.** Toàn bộ giá trị nằm ở bốn spell.

{T1* INFERENCE: h3wiki-skull-helmet + h3wiki-rib-cage + h3wiki-blackshard +
h3wiki-shield-yawning-dead — phép cộng trên số liệu đã fetch}

### Bốn thành phần

| Thành phần | Class | Slot | Giá | Hiệu ứng |
|---|---|---|---|---|
| [[skull-helmet]] | **Treasure** | Helmet | 3.000 | +2 Knowledge |
| [[rib-cage]] | Minor | Torso | 3.000 | +2 Power |
| [[blackshard-of-the-dead-knight]] | Minor | Weapon | 3.000 | +3 Attack |
| [[shield-of-the-yawning-dead]] | Minor | Shield | 3.000 | +3 Defense |

{T1* EXPLICIT: h3wiki-skull-helmet + h3wiki-rib-cage + h3wiki-blackshard +
h3wiki-shield-yawning-dead}

Text khi nhặt của từng món có giọng riêng đáng chú ý:

- **Skull Helmet:** "A brief stop at an improbable rural inn yields an exchange of money, tales,
  and **accidentally, luggage**."
- **Blackshard:** "**The widow of a former Captain of the Guard** admires your quest and gives
  you the enchanted Sword that her husband relied on during his tour of duty."
- **Shield:** "Your troops discover an eerie shrine dedicated to the Undead. You bless the
  shrine, causing the stone shield emblem above the altar to crack."

⚠️ **`Shield of the Yawning Dead` khác hoàn toàn với `Shield of the Damned`** — artifact riêng
biệt, không liên quan. Dễ nhầm vì tên.

### Cơ chế chiến đấu

⚠️ Toàn bộ phần này là **văn wiki, không dẫn nguồn** — nhiều khả năng đúng (quan sát của người
chơi) nhưng không phải game text.

**Thời điểm kích hoạt:**
> "The Armor of the Damned only casts its opening combat spells **once an allied creature is
> able to take its turn**; if a creature misses a turn due to low morale, the Armor of the
> Damned does not cast its spells until the next one is able to do so."

{T6 INFERENCE: h3wiki-armor-of-the-damned — văn biên tập viên, ngoài mọi template; **không dẫn nguồn**}

Hệ quả chiến thuật: nếu địch đi trước và làm chậm quân bạn, Armor có thể **chưa kịp kích hoạt**.

**Cái gì chặn được:** immunity của quân địch, Cursed Ground, và "anti-magic artifacts".

{T6 INFERENCE: h3wiki-armor-of-the-damned + h3wiki-ironfist-of-the-ogre — xem cảnh báo dưới}

⚠️ **Câu này là boilerplate của biên tập viên, không phải game text.** Nó lặp **nguyên văn** trên
trang `Ironfist of the Ogre` và trang `Angelic Alliance` — cùng một câu dùng cho ba artifact khác
nhau. Bản đầu của bài gán `T1*`, tức sai **loại** nguồn: `T1*` nghĩa là in-game text qua trung gian,
mà không có chuỗi nào trong game nói điều này.

**Nhưng hoạt động bình thường trong Anti-Magic Garrison** — điều này được xác nhận **độc lập**
ở một trang thứ hai: "Armor of the Damned, Angelic Alliance, and Ironfist of the Ogre spells
still work in an Anti-Magic Garrison." {T1* EXPLICIT: h3wiki-trivia}

⚠️ Cách nói "anti-magic artifacts" bị một nguồn khác phản bác — xem *Điểm tranh chấp*.

### Bốn hero tăng hiệu quả Weakness

| Hero | Class | Chỉ có ở HotA? |
|---|---|---|
| Cuthbert | Cleric | Không |
| Olema | Heretic | Không |
| Mirlanda | Witch | Không |
| **Eanswythe** | Artificer (Factory) | **Có** |

{T1* EXPLICIT: h3wiki-weakness + h3wiki-cuthbert + h3wiki-olema + h3wiki-mirlanda + h3wiki-eanswythe — kiểm từng trang hero, không tin danh sách}

Specialty của cả bốn giống nhau:

| Bậc quân | SoD gốc | HotA |
|---|---|---|
| Cấp 1–2 | +3 | +4 |
| Cấp 3–4 | +2 | +6 |
| Cấp 5–6 | +1 | +8 |
| Cấp 7 | — | +10 |

{T1* EXPLICIT: h3wiki-cuthbert + h3wiki-olema + h3wiki-mirlanda + h3wiki-eanswythe}

⚠️ **Con số này nằm ở bốn trang hero, không ở trang `Weakness`** — trang `Weakness` không có con số
nào. Bản đầu của bài dẫn `h3wiki-weakness` cho cả khối.

⭐ **Chiều SoD/HotA ở đây đã được xác minh riêng**, vì nguồn dùng cú pháp `{{swh}}` mà trong đó tham số
đầu là HotA — một bẫy đã gây lỗi thật ở bài khác. Mốc xác nhận độc lập: **Eanswythe** là hero
**chỉ có ở HotA**, nên con số của hero đó **không cần** `{{swh}}` — và nó là dãy 4/6/8/10. Vậy dãy
4/6/8/10 đúng là HotA.

Đáng chú ý: Armor of the Damned là **artifact duy nhất trong game cast được Weakness**.
{T1* EXPLICIT: h3wiki-weakness}

### Thay đổi qua các bản

**Không có thay đổi nào nêu tên riêng artifact này.**

Kết luận sau khi grep toàn bộ changelog HotA (201.529 byte) cho cả năm cái tên — Armor và bốn thành
phần. **Không một kết quả nào.** Luồng kiểm định đã grep lại độc lập và xác nhận con số 0.

{T1* INFERENCE: hota-changelog — suy ra từ sự vắng mặt trong changelog, không từ một câu nào nói "không đổi"}

⚠️ **Nhưng "không có thay đổi nào" thì mạnh hơn điều nguồn cho phép.** Changelog **có** những thay đổi
**chung** áp cho mọi combination artifact — tùy chọn cấm ghép, và việc ghi chú thành phần trong mô tả
artifact — và chúng **chạm tới** Armor of the Damned dù không nêu tên nó.

⭐ **Đáng chú ý:** [[cloak-of-the-undead-king]] **bị cấm ghép mặc định** trong HotA. Armor of the
Damned **không nằm trong lệnh cấm đó** — dù cùng là combination artifact của phe Necropolis.

*(Ý kiến fan cho rằng hiệu ứng Armor mới là thứ mạnh, còn chỉ số thì yếu. Nhưng Cloak mới là
cái bị cấm — điều đó gợi ý HotA đánh giá khả năng hồi sinh Lich nguy hiểm hơn bốn debuff.)*

---

## Điểm tranh chấp canon

### 1. Bốn spell hay năm? — đã giải quyết { #tranh-chap-so-spell }

Các nguồn nói khác nhau: 4 spell, 5 spell (thêm Disrupting Ray), hoặc biến thể "Mass".

**Mô tả in-game nói rõ — bốn:**
> "Casts Expert Slow, Curse, Weakness, and Misfortune for 50 rounds at the start of combat."

Xác nhận **ba cách độc lập**: mô tả Fandom liệt kê cùng bốn spell; trang `Weakness` ghi Armor
là artifact duy nhất cast Weakness; và chính đoạn fan-opinion cũng đếm "a total of four spells".

**Nguồn của lỗi "5" đã tìm ra** — nó nằm trong đoạn `{{fanopinion}}` trên chính trang đó:

> "casting a total of **four** spells at Expert level, at no cost, and leaving the hero free to
> cast another spell on their action (**so potentially 5 spells in a single turn**)."

{T6 FAN_THEORY: h3wiki-armor-of-the-damned}

Bốn của armor + một của chính hero. Người đọc lướt qua đếm thành 5.

**Về "Mass":** Slow/Curse/Weakness/Misfortune ở cấp Expert **vốn đã** ảnh hưởng toàn bộ quân
địch — nhưng game text **không dùng** chữ đó. Grep toàn trang: 0 kết quả cho cả "Mass" lẫn
"Disrupting".

### 2. "Anti-magic artifacts" chặn được — cách nói lỏng lẻo

Trang Armor nói "anti-magic artifacts" làm giảm hiệu ứng. Nhưng trang
**Orb of Inhibition** liệt kê rõ dưới mục **"Does not prevent"**:

> "Artifact spell casting (i.e. **Armor of the Damned**, Angelic Alliance or Ironfist of the
> Ogre)."

{T1* EXPLICIT: h3wiki-orb-of-inhibition}

→ **Orb of Inhibition KHÔNG chặn Armor.** Cách nói tổng quát của trang Armor là **sai với ít
nhất một trường hợp**.

**Xử lý:** không lặp lại cụm "anti-magic artifacts" mà không nêu ngoại lệ. Recanter's Cloak và
Cape of Silence có thể là thứ được ám chỉ, nhưng **chưa kiểm** — xem *Câu hỏi mở*.

### 3. Claim "từng thuộc về Ethric" — không có nguồn { #tranh-chap-ethric }

Trang Ethric, mục Trivia:
> "Armor of the Damned and Cloak of the Undead King once belonged to Ethric, **since** Jeddite's
> stated goal in Target is to return them to him."

{T6 FAN_THEORY: h3wiki-ethric}

Wiki **tự rào** bằng chữ "since" — đánh dấu đây là suy luận, không phải dữ kiện. Và phần tiếp
theo còn tự rào mạnh hơn: "It is also **possible, though not confirmed**, that the two
artifacts... were originally created by Ethric."

**Suy luận đó không đứng vững.** `sod-target` Day 1 nói rõ chủ cũ là ai:

> "Ethric has spread word of your whereabouts to **those who lost these two precious
> artifacts**..."

{T1* EXPLICIT: sod-target}

Ethric là **kẻ loan tin**, không phải người đòi lại. Và region text cho thấy các lãnh chúa
không đồng lòng: "Some of the lords want these artifacts for their own use; others want to
destroy them" — mâu thuẫn với cách đọc một-chủ-sở-hữu.

"Return them to Ethric" hợp lý nhất là **[[jeddite]] giao lại cho thầy để cất giữ hoặc tiêu
hủy** — đúng như cách người ta đưa vật nguy hiểm cho pháp sư cao tay hơn.

**Xử lý:** Codex không dùng claim này.

---

## Câu hỏi mở

**Q1. Ai tạo ra Armor of the Damned?**
Không nguồn nào nêu. Khoảng trống lore lớn nhất của bài.

**Q2. Recanter's Cloak và Cape of Silence có chặn được không?**
Chưa kiểm. Đã bác bỏ Orb of Inhibition, nhưng hai artifact kia chưa fetch.
{T1* UNVERIFIED: h3wiki-armor-of-the-damned — **chưa xác minh**}

**Q3. Cursed Ground thật sự chặn được không?**
Chỉ có trang Armor khẳng định, chưa xác minh độc lập.
{T1* UNVERIFIED: h3wiki-armor-of-the-damned — **không dẫn nguồn**}

**Q4. Cơ chế "chỉ kích hoạt khi quân đồng minh được đi" có đúng không?**
Văn wiki chi tiết nhưng **không dẫn nguồn**. Gần như chắc chắn là quan sát đúng của người chơi,
nhưng không phải game text.
{T1* UNVERIFIED: h3wiki-armor-of-the-damned — **không dẫn nguồn**}

**~~Q5. Mô tả in-game chính xác là gì?~~ — ✅ ĐÃ GIẢI QUYẾT (2026-08-03)**

Trang `Talk:Artifact/descriptions` **đã fetch**, và đúng như dự đoán của câu hỏi này: nó tự ghi ở đầu
bảng `Information from H3Bitmap.lod > artraits.txt` — **string table trích từ file game**, tier `T1`
thật.

Và phát hiện đi kèm quan trọng hơn câu trả lời: **câu Fandom mà bài từng dùng không phải mô tả
in-game** — nó khác cả thứ tự spell lẫn chủ thể. Xem mục *Gameplay*.

---

## Trivia & Dev Notes

### ⭐ Ba lỗi text trong cùng một scenario

`sod-grave-robber` chứa **ba** lỗi khác nhau, và lỗi đầu tiên được chứng minh chắc chắn vì
**chính trang đó tự mâu thuẫn**.

**Lỗi 1 — prologue nhắc sai thành phần.**

Prologue:
> "Now that I gave him **the Death Knight's Sword**, Sandro wants me to fight some more
> Necromancers for a shield."

Nhưng Day 1 event của **chính scenario đó** mở đầu:
> "**You have the Rib Cage!** Excellent work, Mister Hack"

{T1* EXPLICIT: sod-grave-robber}

**Rib Cage mới đúng.** Blackshard ("Death Knight's Sword") đã giao **một scenario trước**, ở
đầu `A Cage in the Hand`: "I got Sandro his cursed sword, and now he wants me to fight more
moldy Necromancers to get some kind of armor made out of bones."

Chuỗi prologue đối chiếu:

| Scenario | Prologue nói vừa giao gì | Đúng? |
|---|---|---|
| Bashing Skulls | (chưa giao gì) | ✓ |
| Black Sheep | "this ugly **Helmet**" | ✓ |
| A Cage in the Hand | "his cursed **sword**" | ✓ |
| **Grave Robber** | "**the Death Knight's Sword**" | ✗ — phải là Rib Cage |

**Chẩn đoán:** prologue Grave Robber có vẻ **bị lệch một scenario** — nó nhắc lại thứ đáng lẽ
thuộc về prologue trước đó. {T1* INFERENCE: sod-grave-robber — suy từ việc trang tự mâu thuẫn}

⚠️ **Wiki âm thầm che lỗi này** bằng cách pipe link: `[[Blackshard of the Dead Knight|Death
Knight's Sword]]`. Biên tập viên link tới Blackshard — đúng với chữ, nhưng **sai với cốt
truyện**, và wiki không đánh dấu đây là lỗi ở đâu cả.

Dự án **ghi nhận lỗi thay vì che nó**.

**Lỗi 2 — mô tả nói sai về carry-over.** Mô tả scenario ghi Crag Hack "will carry his
experience, skills and spells on to his next campaign". Chính wiki phải ghi chú: "Although the
description states that Crag Hack carries over to the next campaign, **that is not accurate**."

**Lỗi 3 — tên artifact viết ngược.** Mô tả gọi là "the **Yawning Shield of the Dead**", trong
khi tên thật và điều kiện thắng là "**Shield of the Yawning Dead**".

### Thứ tự scenario không giống thứ tự liệt kê

Thứ tự thu thập **không** khớp thứ tự các thành phần được liệt kê trên trang artifact:

| # | Scenario | Thành phần | Độ khó |
|---|---|---|---|
| 1 | Bashing Skulls | Skull Helmet | Hard |
| 2 | Black Sheep | **Blackshard** | Hard |
| 3 | A Cage in the Hand | **Rib Cage** | Expert |
| 4 | Grave Robber | Shield of the Yawning Dead | Expert |

{T1* EXPLICIT: sod-bashing-skulls + sod-black-sheep + sod-a-cage-in-the-hand + sod-grave-robber}

---

## Nguồn

| Loại | Số lượng | Ghi chú |
|---|---|---|
| **`T1`** — string table trích từ file game | **1** | ⭐ `h3wiki-artraits-txt` — mô tả in-game thật. Thay `fandom-artifact-list`, vốn là **diễn giải** chứ không phải chuỗi game |
| `T1*` — text in-game qua trung gian | 22 | heroes.thelazy.net |
| `T6` — văn biên tập viên / wiki cộng đồng | 3 | Cơ chế chiến đấu, mục *Important information*, và đoạn `{{fanopinion}}` |

⚠️ **Toàn bộ mục *Cơ chế chiến đấu* là `T6`, không phải `T1*`.** Câu về "cái gì chặn được" lặp nguyên
văn trên ba trang artifact khác nhau → boilerplate biên tập viên. Bản đầu của bài gán `T1*` cho nó,
tức sai **loại** nguồn.

Nguồn giá trị nhất: bốn scenario `Hack and Slash` — toàn bộ tuyến lừa Crag Hack nằm ở đó, và
phần lớn chi tiết hay nhất nằm trong **map event**, không phải prologue.

---

## Liên kết

**Thành phần:** [[skull-helmet]] · [[rib-cage]] · [[blackshard-of-the-dead-knight]] ·
[[shield-of-the-yawning-dead]]

**Artifact liên quan:** [[cloak-of-the-undead-king]] · [[angelic-alliance]] ·
[[statue-of-legion]]

**Nhân vật:** [[sandro]] · [[crag-hack]] · [[ethric]] · [[jeddite]] · [[yog]] · [[gem]]

**Campaign:** [[sod-hack-and-slash]] · [[sod-rise-of-the-necromancer]] ·
[[sod-unholy-alliance]]
