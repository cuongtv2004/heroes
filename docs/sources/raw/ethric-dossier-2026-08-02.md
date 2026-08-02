# Research dossier: Ethric — 2026-08-02

Tư liệu thô. Giữ nguyên tiếng Anh — chính xác quan trọng hơn dễ đọc.

**Cảnh báo:** tư liệu thô, **không phải nguồn**. Text "verbatim" là bản chép của fan wiki
qua `?action=raw`, không phải file game. Xem `sources/REGISTRY.md` mục "Lưu ý về T1*".

---

## 1. Dữ liệu cơ bản

### Infobox Heroes III (`h3wiki-ethric`)

| Trường | Giá trị |
|---|---|
| picture | **Ajit** (dùng portrait của hero khác) |
| town | Dungeon |
| class | **Warlock** |
| race | **Lich** |
| specialty | **Mysticism** ("Receives a 5% per level bonus to Mysticism skill.") |
| level | 6 |
| Chỉ số | atk 4 / def 3 / sp 2 / know 2 |
| Spell khởi đầu | Blind |
| Movement | 1560 |

**Tám kỹ năng Expert** — bất thường với một hero địch: Wisdom, Eagle Eye, Scholar,
Tactics, Learning, Offense, Intelligence, Sorcery.

Quân: Troglodyte 30–40 (100%), Harpy 4–6 (88%), Beholder 3–4 (25%).

### Portrait — hai tầng, đã xác minh

- Infobox ghi thẳng `picture = Ajit`
- `Master` hero row: `{{hero row|15, 9, 0|orange|Ethric|image=Ajit|Warlock}}`
- Fandom caption: "Ethric in The Shadow of Death (uses the portrait of Ajit)"

**Nhưng Ajit không phải hero nền.** Fandom: "Despite having Ajit's icon, the Ethric hero
is based on **Jaegar**, and has his specialty."

Agent đã kiểm chéo cả hai trang:
- Ajit specialty = **Beholders**
- Jaegar specialty = **Mysticism**, "Receives a 5% per level bonus to Mysticism skill" —
  **khớp chuỗi chính xác** với Ethric, và Jaegar cũng khởi đầu với Basic Mysticism

→ **Xác nhận: portrait của Ajit, template chỉ số của Jaegar.**

### Story section trên `h3wiki-ethric` (văn wiki)

> Also called '''Ethric the Mad''', described as both the world's first lich and its first
> necromancer, and Sandro's former master, who trained him to be a warlock and objected to
> him becoming a necromancer. Decades later, Ethric alerted Gem to the fact that Sandro was
> constructing powerful necromantic artifacts. In an attempt to thwart Sandro, he sent word
> to Sandro's enemies of his location and the fact that he possessed powerful artifacts.
>
> Afterwards, he became active on Enroth, based in the Tomb of Ethric the Mad, by the early
> part of 1165 AS, until he was slain by the protagonists of Might and Magic VI during their
> journey. His skull was later brought to Gabriel Cartman, an alchemist in the city of Free
> Haven. By studying the first lich's skull, Cartman hoped to discover a way to reverse the
> process of transformation into a lich.

⚠️ Trang này **không có một footnote nào**.

---

## 2. "Lich đầu tiên của thế giới" — có phân biệt quan trọng

Cả hai wiki đều **rào** claim này, nhưng không nêu lý do thật.

- `h3wiki-ethric`: "**described as** both the world's first lich and its first necromancer"
- Fandom: "**supposedly** the first lich on Enroth"

**Cơ sở in-game thật, mà cả hai wiki đều làm mờ:**

Fandom `Ritual of Endless Night`:
> "**According to rumor**, Ethric was the first sorcerer to discover the ritual, becoming
> the world's first lich and the first necromancer at the same time. Gabriel Cartman
> believed that by studying Ethric's remains, he might be able to reverse the ritual's
> effects."

MM6 in-game, dungeon `Ethric the Mad's Tomb`:
> "Ethric, the first Sorcerer seeking life after death, still walks about his tomb, the
> leader of a host of undead servants. **At least, that's how the rumor goes...**"

**NHƯNG — một text in-game khẳng định thẳng, không phải tin đồn.** Mô tả item MM7
**Ethric's Staff**:
> "Much more a tool than a weapon, Ethric's Staff was fashioned by **the world's first
> Lich - Ethric the Mad**. The staff magnifies Dark magic, drawing from the life force of
> its user. Since Ethric's life force was magically sustained, this wasn't a problem for
> him."

**Kết luận có sắc thái:**
- "**Lich đầu tiên**" — được MM7 khẳng định **thẳng**, không rào
- "**Lich đầu tiên VÀ necromancer đầu tiên**" (gộp) — MM6 đóng khung là **tin đồn**

Đây là phân biệt đáng giữ. Không nguồn nào dẫn citation cho claim gộp.

**Thêm một mảnh MM6 độc lập** — mô tả item **Shadow Dagger**:
> "Commissioned by Ethric the Mad **while still a human**, it is said these daggers have a
> link to the Land of the Dead."

→ xác nhận độc lập quá trình người → lich, từ chính trong MM6.

---

## 3. Câu hỏi Jabarkas — ba text, và một phát hiện mới

### 3a. `sod-target` Day 24 — nguyên văn

> A spy returns with word has come about internal conflicts among your enemies. Your old
> friend Jeddite and his allies want to seize the artifacts and promptly return them to
> Ethric. However, two other allied stronghold towns to the North and to the Northeast want
> the artifacts to remain in their possession. **According to you advisors**, Lord Jabarkas,
> the leader of these two towns, **is Ethric's illegitimate younger brother suffers from
> Little Man's Syndrome**. It seems that Jabarkas has always been envious of his older
> brother's prestige...

**Bốn quan sát của agent:**

1. Câu **sai ngữ pháp trong chính game text**: "is Ethric's illegitimate younger brother
   suffers from Little Man's Syndrome" — thiếu "and who". Lỗi của NWC, có trong wikitext
   thô. **Không được lặng lẽ sửa khi trích.**
2. "you advisors" (sic) — lỗi thứ hai
3. **Claim được gán cho cố vấn của Sandro** ("According to you advisors"), không phải lời
   kể. Là **tin nghe lại ngay trong khung của game.**
4. Game text nói "**brother**". Wiki nâng thành "**half-brother**" — từ này **không xuất
   hiện** trong scenario. Đây là wiki tự thêm.

### 3b. Bio chính thức của Jabarkas (`h3wiki-jabarkas`)

Infobox: town Stronghold, class Barbarian, **race = Ogre**, specialty Orcs.

Bio (game data):
> "Being the **eldest son of Duke Boragus**, Jabarkas knows that he will one day rule the
> lands of Krewlod."

**Mâu thuẫn rõ:** Jabarkas là **Ogre**, con trai cả **Duke Boragus** xứ Krewlod. Ethric là
**người** Bracada thành lich, hàng thế kỷ tuổi. Bio chính thức **không nhắc Ethric một
chữ nào**.

Story section của wiki đặt cả hai thân thế cạnh nhau trong hai câu liên tiếp **mà không
ghi nhận sự bất khả dung hòa.**

### 3c. Wiki tự đánh giá

> "It is not made clear whether Jabarkas is Ethric's actual brother, or if this is part of
> the cover story. **The latter is very likely**, since lore implies that, as the first
> necromancer, Ethric should be centuries old."

### 3d. ⭐ PHÁT HIỆN MỚI — động cơ thật của Jabarkas

Map event `sod-target` (15, 27, 0) — tìm được nhờ đọc block `==== Events ====`:

> "Sir, Lord Jabarkas knows you are in the area and is planning to kill you. He has not
> forgotten you kidnapping his daughter and violating her. He has recruited a large army
> from another Stronghold in the northeast and plans to attack you shortly."
>
> "**Did he make mention of the artifacts?**" you ask.
>
> "**No, sir.**"
>
> "Well done. Dismissed."

**Đây là mảnh quyết định.** Động cơ thật của Jabarkas là **thù riêng vì con gái** — không
phải ghen tị với anh trai về artifact. Nó **phản bác trực tiếp** cách Day 24 mô tả hắn là
"em trai ghen tị".

Và chi tiết Sandro hỏi "Có nhắc gì tới artifact không?" → "Không" — chính game text tự
tách hai động cơ ra.

---

## 4. Hai cái chết — mâu thuẫn KHÔNG có lời giải

### 4a. Trong `sod-master` — KHÔNG CÓ CẢNH CHẾT

**Phát hiện phủ định quan trọng.** Agent đọc toàn bộ trang kể cả block Events. Việc Ethric
bị đánh bại **chỉ tồn tại dưới dạng điều kiện thắng**, không có đoạn kể nào.

Mô tả scenario:
> "Defeat Ethric and all of his allies to win the scenario."

Region text:
> "Sandro now faces Ethric and one of his allies. He must defeat the old Warlock before
> moving on to Deyja."

Agent kiểm tiếp scenario **sau** đó (`sod-finneas-vilmar`): **Ethric không bao giờ được
nhắc lại nữa.** Campaign đơn giản là bỏ rơi ông.

→ Fandom ghi "was able to defeat the opposing army and **eradicate** Ethric" và infobox
`status = Eradicated` là **wiki suy từ điều kiện thắng**, không từ text kể nào.

### 4b. Trong MM6

Quest Fandom: "Retrieve Ethric's skull from his tomb west of Free Haven for Gabriel
Cartman". Phần thưởng: 15000 XP, 7500 gp, 60 fame.

Walkthrough: "Kill Ethric (**he will look like a Power lich**), and click on his body to
take his skull."

Chỉ số MM6: lich cấp 40, 280 HP, AC 25, 5D8+20 sát thương năng lượng tầm xa, 2000 XP.

### 4c. Mâu thuẫn — hai wiki giải quyết NGƯỢC NHAU

Niên đại: MM6 khoảng 1165 AS; *Rise of the Necromancer* muộn hơn. Nên nhóm MM6 giết Ethric
**trước**, rồi Sandro đánh bại ông **sau**.

| Nguồn | Cách xử lý |
|---|---|
| **Bullard (T4)** | Xác nhận **hai Ethric là một người**, nhưng **không nói gì** về hai cái chết. Giải quyết *danh tính*, không giải quyết *niên đại* |
| **Fandom** | Lấp bằng một câu không dẫn nguồn: "**Somehow surviving** his encounter in Enroth, Ethric returned to Antagarich in his human guise..." Chữ "Somehow" gánh toàn bộ |
| **thelazy** | **Đảo ngược thứ tự hẳn.** Đặt sự kiện SoD trước ("Decades later, Ethric alerted Gem..."), rồi "**Afterwards**, he became active on Enroth... slain by MM6 protagonists" → MM6 thành cái chết cuối |

**Hai wiki mâu thuẫn nhau về thứ tự, cả hai đều không dẫn nguồn.**

Agent ghi rõ: một cách dung hòa in-game **mà cả hai wiki không viện tới** là Ethric là lich,
được duy trì bằng Ritual of Endless Night, và cú giết ở MM6 để lại **hộp sọ** mà Cartman
nghiên cứu hòng **đảo ngược** lichdom — hàm ý di hài còn ý nghĩa. **Nhưng không text nào
nói Ethric tái hợp.** Agent đánh dấu đây là suy luận của chính nó, không phải lore.

**Kết luận trung thực: mâu thuẫn chưa được giải quyết trong canon.**

---

## 5. Developer commentary — Bullard

`bullard-interview-2013`. **Toàn bộ phần về Ethric chỉ có hai dòng:**

> **Q:** Ethric the Mad from Might and Magic VI - The Mandate of Heaven. Was he the same
> master of Sandro from Heroes of Might and Magic III - Shadow of Death storyline?
>
> **A:** Yes, we always tried to tie the different products together so people who played
> everything could see a theme.

**Cảnh báo của agent:** câu trả lời xác nhận danh tính nhưng được đóng khung như **triết lý
thiết kế chung** ("we always tried to tie the different products together"), không phải
phán quyết chi tiết về continuity. Nó **không** đề cập việc chết hai lần, tuổi tác, Jabarkas,
hay ông "thật sự" thuộc class nào.

> **Wiki dựa vào câu này nặng hơn hai mệnh đề của nó cho phép.**

Agent đã tìm "Ethric", "lich", "necroman" trong toàn văn phỏng vấn — **đây là kết quả duy
nhất cho cả ba từ.** Không có thảo luận nào khác về lich hay nguồn gốc necromancy.

⚠️ Bản gốc trên acidcave.net **chưa fetch** — chỉ đọc bản chép của thelazy.

---

## 6. Dạy Sandro cái gì — mâu thuẫn có thật

**Bio chính thức của Sandro** (game data, `HEROBIOS.TXT`):
> "Sandro first studied **Necromancy** under the tutelage of the wizard, and later the lich,
> Ethric."

**Campaign text nói ngược.** `sod-target` prologue:
> "It seems Ethric, my old master, has finally tracked me down. He hasn't been too happy
> about me becoming a Necromancer and wants to remove the blight from his career."

`sod-target` Day 1:
> "Ethric, your old master, **became furious** when he received word you became a
> Necromancer."

Thư Jeddite: Ethric "**doubted your ability** to wisely endure the burden of magical
knowledge" ngay từ đầu.

**Cách wiki xử lý — và một điểm bất nhất đáng ghi:**

Wiki khẳng định Ethric "trained him to be a warlock and objected to him becoming a
necromancer" — một tổng hợp **hợp với campaign nhưng mâu thuẫn thẳng với bio chính thức**,
và wiki trình bày mà **không ghi nhận xung đột**.

Nhưng ở mục trivia, wiki lại **dùng chính bio đó làm bằng chứng**: "The fact that Sandro's
bio remains unchanged all throughout Shadow of Death... stating that he was a pupil of the
lich Ethric, corroborates the above hints."

→ **Wiki coi bio là có thẩm quyền khi nó ủng hộ giả thuyết lich, nhưng gạt đi khi nó mâu
thuẫn về việc dạy gì.** Phương pháp bất nhất.

**Danh sách class của Ethric theo wiki** (5 tham chiếu khác nhau):
- Wizard/Lich: bio Sandro
- Wizard: `sod-driving-for-the-boots` — Gem định viết thư cho Ethric ở Bracada
- Warlock: `sod-poison-fit-for-a-king` — Sandro gọi ông là Warlock
- Warlock: `sod-master` — xuất hiện với class Warlock
- Lich: MM6, MM7, Olden Era

---

## 7. ⭐ ETHRIC KHÔNG BAO GIỜ NÓI

**Phát hiện đáng chú ý nhất của đợt này, và không wiki nào ghi.**

Agent tìm qua mọi nguồn — `Ethric` (cả hai wiki), `Target`, `Master`,
`Poison Fit for a King`, `Driving for the Boots`, `Rise of the Necromancer`,
`Finneas Vilmar`, `Jeddite`, `Sandro`:

> **Ethric never speaks a single line of dialogue.**

Ông chỉ được **mô tả**, được **trích dẫn gián tiếp**, hoặc được **kể lại**. Thư Jeddite
diễn giải ý ông ("he doubted your ability..."); thuộc cấp của Ufretin nói đã nhận "Ethric's
message" nhưng không trích.

**Mọi mô tả về Ethric trong SoD đều lọc qua: lời kể thù địch của Sandro, cố vấn của Sandro,
hoặc kẻ địch của Sandro.**

---

## 8. Đoạn mô tả Ethric đầy đủ nhất — cơn ác mộng

`sod-poison-fit-for-a-king`, Day 69 "Nightmare":

> The nightmare began as usual. Ethric was chasing you, waving his sword like the lunatic he
> was. Screaming battle cries, he rushes headlong forward, threatening to overtake and kill
> you. There is no doubt in your mind this **Warlock** would rip your head from your
> shoulders and use it to play kickball. **He was mad**, insane with jealousy and unable to
> control the power he already had. His screaming turned to a maddening chanting and
> lightning ripped from his hands, searing your tender flesh and throwing you to the ground.
>
> Bony hands shake you before you die in the dream. "I'm sorry, sir," the Zombie apologizes.
> "I was just waking you as you ordered." Shaking, you spend the rest of the night pouring
> over rosters.

**Ghi chú:** "**He was mad**" — thì quá khứ, trong giấc mơ của Sandro, **sau** *Master*.
Đây là chỗ Heroes III tiến gần nhất tới việc gọi ông là "the Mad", và là cầu nối text
in-game mạnh nhất tới Ethric the Mad của MM6.

Nhưng đây cũng là **giấc mơ chủ quan của Sandro**, và mô tả Ethric vung **kiếm** — không
hợp với một wizard/warlock.

---

## 9. Nguồn duy nhất cho "Ethric ở Bracada"

`sod-driving-for-the-boots`, epilogue của Gem:
> "Did he give Ethric the other artifacts? ...I will have to **write to Ethric in Bracada**
> and tell Lord Fayette about this immediately."

Đây là **nguồn duy nhất** cho danh tính công khai "wizard còn sống ở Bracada" — và nó khớp
chính xác với tiểu sử Olden Era ("reclusive wizard of Bracada").

---

## 10. Olden Era — NGOÀI Old Universe, chỉ ghi để tham chiếu

⚠️ *Heroes of Might and Magic: Olden Era* là sản phẩm **hiện đại**, chưa phát hành. Theo
`CANON-POLICY.md` R5, **không phải canon Old Universe**. Ghi lại vì nó là tiểu sử duy nhất
kể nguồn gốc Ethric.

> "Once a brilliant but reclusive wizard of Bracada, Ethric delved too deeply into death
> magic - secrets no mortal was meant to wield. In his attempt to conceal his findings, he
> became the target of betrayal that nearly cost him his life. Ethric embraced undeath to
> survive and became a lich. Yet he still clings to the pretence of life, walking among
> mortals with cryptic purpose."

Gameplay OE: Necromancer, Necropolis, khởi đầu basic Necromancy + basic Wisdom.
Specialty **Tomb-bound Will**.

**Đây là sản phẩm chưa phát hành — có thể đổi.**

---

## 11. Xuất hiện — đã kiểm disambiguation

**Kiểm disambiguation (quy tắc phương pháp 2):** agent thử `Ethric (disambiguation)` trên
**cả hai** wiki — **0 byte / không có trang**. Chạy thêm full-text search trên Fandom
(30 kết quả). **Chỉ có đúng một nhân vật Ethric**; không có bản Ashan, không có người trùng
tên. Tên gần giống nhất là `Edric (Enroth)` và `Zanthora the Mad` — không liên quan.

→ **Claim "không xuất hiện ở đâu khác" là AN TOÀN, và đã được kiểm chứ không phải giả định.**

| Game | Vai trò |
|---|---|
| MM6 | Quái/boss độc nhất |
| MM7 | **Chỉ được nhắc** — qua mô tả item Ethric's Staff |
| H3 SoD | Hero **địch** |
| Olden Era | Hero chơi được (ngoài Old Universe) |

**Scenario H3:**
- `Target`: **được nhắc** (prologue, Day 1/2/18/24, event 40,46,0)
- `Master`: **hero địch**, orange, town Dungeon
- `After the Amulet`, `Retrieving the Cowl`, `Driving for the Boots`: được nhắc
- `Agents of Vengeance`, `Wrath of Sandro`: được nhắc
- `Poison Fit for a King`: được nhắc

**Không bao giờ chơi được ở H3.**

---

## 12. Text khác đáng dùng

`sod-target` region text:
> "Ethric is a sly old Warlock. He has spread word of Sandro and the artifacts he carries to
> the lords of this region. Some of the lords want these artifacts for their own use; others
> want to destroy them."

`sod-target` event (40, 46, 0) — Ethric xây liên minh:
> "Yes, sir. Ethric's message was received this morning. Sandro is in the area and does hold
> the artifacts. We have replied to Ethric that we will retrieve the artifacts and give them
> to Jeddite."

`sod-target` Day 18:
> "You suspect that latter explanation and wonder what Ethric was thinking when he enlisted
> these people in his cause."

`sod-master` Day 1 — Vidomina:
> "You explain to her your quest, the powerful artifacts you possess, and why Ethric wants
> your head."

Thư Jeddite (`sod-target` Day 2) — đầy đủ ở dossier Sandro.

---

## Lỗ hổng

1. **Bản gốc Acid Cave chưa fetch.** Chỉ đọc bản chép thelazy.
2. **Không có dialogue MM6.** Ethric là boss không thoại; lời thoại của Gabriel Cartman
   chưa lấy được (Fandom chỉ diễn giải).
3. **Mô tả item `Ethric's Skull` chưa lấy.**
4. **Olden Era chưa phát hành** — dữ liệu có thể đổi.
5. **Bốn scenario "được nhắc" chỉ kiểm một phần.** `After the Amulet`,
   `Retrieving the Cowl`, `Agents of Vengeance`, `Wrath of Sandro` **chưa fetch** —
   phần nhắc Ethric lấy từ danh sách của wiki, chưa xác minh.
6. **Tuổi Ethric / thời điểm thành lich: không nguồn nào có.** "Hàng thế kỷ" là suy luận
   của wiki.
7. `homm.miraheze.org` không vào được (403). `web.archive.org` bị chặn.
8. **Wiki tiếng Nga** (`[[ru:Этрик]]`) chưa fetch — có thể có nguồn thêm.

---

## Claim chỉ có wiki chống lưng

| # | Claim | Đánh giá |
|---|---|---|
| 1 | "**Somehow surviving** his encounter in Enroth..." (Fandom) | Mô liên kết thuần túy. Không nguồn. Chữ "Somehow" là lời thú nhận |
| 2 | "eradicate Ethric" + `status = Eradicated` (Fandom) | **Suy từ điều kiện thắng.** Không text nào kể cái chết hay số phận Ethric trong SoD |
| 3 | "took command of a small force of **Nighon** troops" (Fandom) | "Nighon" không xuất hiện trong text nào; suy từ việc town là Dungeon |
| 4 | "Illegitimate younger **half-brother**" (thelazy) | Game nói "**brother**". Wiki tự thêm "half-" |
| 5 | Toàn bộ mục `== Ethric the Mad ==` của thelazy | Tự rào ("It can be surmised", "apparently", "very likely"). Lập luận hợp lý, **zero citation** |
| 6 | "lich đầu tiên VÀ necromancer đầu tiên" không kèm rào "theo tin đồn" | Cả hai wiki đều **không nêu** rằng MM6 đóng khung là tin đồn. MM7 khẳng định thẳng "lich đầu tiên" — nên vế này mạnh hơn vế "necromancer đầu tiên" |
| 7 | "A force of liches attacks Sandro in Master" (thelazy trivia) | **Đọc sai rõ ràng.** Event (24,10,0): các Power Lich canh một **sawmill** — quái trung lập, không phải quân của Ethric |
| 8 | "Armor of the Damned và Cloak từng thuộc về Ethric" | Suy từ "return them to Ethric" của Jeddite. Nói chắc hơn text cho phép. *(Xem dossier Cloak — bị `sod-target` Day 1 phản bác)* |
| 9 | Niên đại thelazy "Afterwards... slain by MM6 protagonists" | **Mâu thuẫn thẳng** với thứ tự của Fandom. Cả hai không dẫn nguồn |
| 10 | "MM6, MM7, và Olden Era đều **khắc họa** Ethric là necromancer lich" | MM7 **không khắc họa** — chỉ xuất hiện trong mô tả item. Nói quá |
| 11 | "trained him to be a warlock and objected to him becoming a necromancer" | Tổng hợp mâu thuẫn với bio chính thức, trình bày mà không ghi nhận xung đột |

---

## Ba điều agent đánh dấu cho bài viết

1. **Khung "advisors" của claim Jabarkas là phát hiện hữu ích nhất.** Chính game đánh dấu
   đó là tin nghe lại — cộng với việc Jabarkas là Ogre xứ Krewlod con Duke Boragus, cách
   đọc "vỏ bọc" được chống lưng **mạnh hơn nhiều** so với lập luận của wiki (dựa trên tuổi
   Ethric). Và **giữ nguyên lỗi ngữ pháp gốc khi trích.**

2. **Mâu thuẫn hai cái chết không có lời giải canon**, và hai wiki giải quyết theo **hai
   hướng ngược nhau**. Quote của Bullard chỉ giải quyết danh tính. Bài trung thực phải
   **trình bày mâu thuẫn** thay vì chọn bên.

3. **Ethric không bao giờ nói.** Mọi lời về ông trong Heroes III đến từ Sandro (kẻ kể thù
   địch, không đáng tin), cố vấn của Sandro, hoặc kẻ địch. **Đây có lẽ là điều quan trọng
   nhất cần truyền đạt về nhân vật này, và không wiki nào ghi.**
