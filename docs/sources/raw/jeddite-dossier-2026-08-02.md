# Research dossier: Jeddite — 2026-08-02

Tư liệu thô. Giữ nguyên tiếng Anh.

**Cảnh báo:** tư liệu thô, **không phải nguồn**. Text "verbatim" là bản chép fan wiki
qua `?action=raw`, không phải file game. Xem `sources/REGISTRY.md` mục "Lưu ý về T1*".

**Ghi chú phương pháp:** agent dùng `curl` với `action=raw`, không dùng WebFetch (vì
WebFetch tóm tắt thay vì trả nguyên văn).

---

## 1. Định danh và gameplay

Infobox dùng template `{{HeroNew}}` (hero roster chuẩn), **không phải**
`{{CampaignHero}}` như Ethric.

| Trường | Giá trị |
|---|---|
| Class | **Warlock** |
| Town | Dungeon |
| Race | **Human** |
| Hero ID | **91** |
| **Specialty** | **Resurrection** |
| Kỹ năng khởi đầu | Advanced Wisdom (chỉ một) |
| Spell khởi đầu | Resurrection |
| Movement | 1560 |

Specialty text: "Casts Resurrection with effect increased by 5% (HotA: 3%) for every N
hero levels, where N is the level of the target creature."

Quân khởi đầu: Troglodytes 20–30 (HotA 30–40), Harpies 6–8 (HotA 4–6), Beholders 3–4.

**Không có level hay chỉ số cố định** — vì là hero chuẩn. (Đối lập với Ethric: level 6,
4/3/2/2, tám kỹ năng Expert.)

### Hero chuẩn, KHÔNG phải campaign-exclusive — xác minh ba cách

1. Template `{{HeroNew}}` + `{{DungeonHeroesNew}}`
2. **Vắng mặt** trong `List of campaign heroes` (0 kết quả)
3. Trang `Dungeon` khuyến nghị hắn cho lối chơi thường: "Powerful heroes, e.g. Gunnar
   with Logistics specialty, and **Jeddite** and Alamar with Resurrection spell."

---

## 2. ⭐ Bio chính thức — KHÔNG nhắc gì tới Ethric hay Sandro

Agent fetch được **`Translation Data/HeroBios.txt`** (168.918 byte) — file string table
trích từ game, có cột EN/FR/PL/RU. Đây là nguồn tốt hơn trang wiki.

Chuỗi tiếng Anh, nguyên văn:

> "Some say that Jeddite has seen the face of **Zenofex**, but many contend that since
> Jeddite is still alive, the rumor of a meeting could not possibly be true. Jeddite has
> never confirmed nor denied the rumor."

**Xác nhận cả hai điểm nghi ngờ:**

- Bio nói về **Zenofex** (viết vậy trong game; wiki redirect sang `Xenofex` — vua Kreegan)
- **Không một chữ nào** về Ethric, Sandro, necromancy, hay sự kiện Target

→ **Hai nguồn mô tả nhân vật này hoàn toàn rời nhau.**

### Chi tiết phụ đáng ghi

Cùng file: bản dịch **Ba Lan và Nga đều để Jeddite là NỮ** ("Jeddite widziała",
"Джедитта… она еще жива"). Đây là lỗi dịch, không phải lore — text tiếng Anh và portrait
H3 đều là nam.

---

## 3. Scenario `Target` — lần xuất hiện duy nhất có cốt truyện

Campaign SoD *Rise of the Necromancer*, map 1. Người chơi = Sandro (đỏ).

Jeddite là **xanh dương**, town **Dungeon**, vị trí 55,68,0. Town của hắn ở 55,67,0.

Địch chia hai đợt: `1: green, orange` — `2: blue, tan, purple`.
→ **Jeddite là địch đợt HAI**, không phải đợt đầu.

### Thư Jeddite — Timed Event Day 2

⚠️ Câu dẫn đầu **sai địa lý một cách đáng chú ý**: game nói thư đến từ "the Barbarians
due west", nhưng Jeddite là người chơi xanh dương ở **đông nam**.

> You have just received a threatening letter from **the Barbarians due west**. It reads:
>
> "Sandro,
>
> My name is Jeddite. Perhaps you remember me, if your memories are not clouded by your
> undead mind. We were students together under Ethric. By becoming Necromancer, you have
> completely shamed me, **for it was I who introduced you to Ethric**. I should have
> listened to him. **From the start, he doubted your ability to wisely endure the burden
> of magical knowledge.**
>
> Ethric told me of the two artifacts now in your possession. Know this, Sandro: you will
> not get past me on your journey to Deyja. I have allied with the Rampart town up north,
> and they stand with me against you. **I will take the artifacts from your rotting corpse
> and return them to Ethric.**"
>
> You do remember this Jeddite. Not only was he one of Ethric's best students, **he was
> also your best friend**. So, he feels guilty for introducing you to Ethric. **You will
> have to find a way use this weakness against him.**

**Lỗi gốc trong game:** "find a way use" (thiếu "to"), "By becoming Necromancer" (thiếu
mạo từ).

**Chú ý:** đoạn cuối là **lời kể cho người chơi**, không phải một event cố vấn riêng.

### Thư trả lời của Sandro — Timed Event Day 8

> Your advisors remind you it has been almost a week since you received that threatening
> letter from your old friend. They suggest you reply to it soon **if you are to use your
> friendship to your advantage**. You order for a messenger.
>
> "Deliver this message to Jeddite: I have received your letter of warning. Am I suppose
> run and hide, fearful of your vow to stop me? No, your threat only strengthens my
> resolve. I will take these artifacts to Deyja, where I shall use them rise to the top of
> the Deyja hierarchy. You and your pitiful little band cannot stop me. If you stand in my
> way, I will kill every living soul under your command and convert their undead bodies to
> my cause. **By the way, thank you for introducing me to the powers of magic. Without your
> help, I would never have achieved such greatness.**"
>
> The messenger quickly writes your message onto a scroll and goes on his way. You wonder
> to yourself if the message was perhaps a little too confident. But, hopefully, **giving
> him a glimpse of the monster he helped to create will shatter his own confidence.**

**Lỗi gốc:** "Am I suppose run", "use them rise".

**⭐ Điểm sắc sảo nhất mà agent chỉ ra:** thư Jeddite nói hắn giới thiệu Sandro **với
Ethric**. Sandro cố tình bóp méo thành giới thiệu **với sức mạnh phép thuật** — tức là
quy công cho Jeddite đã **tạo ra con quái vật**. Câu kết của đoạn nói rõ ý đồ: "giving
him a glimpse of the monster he helped to create".

### Map event 49,63,0 — mô tả Jeddite đầy đủ nhất trong toàn Old Universe

> Your neighboring town is coming into view. **Jeddite has become quite a powerful lord as
> well as a powerful warlock. You have learned he is a man of his word and has never backed
> down from a battle.** You wonder if going into combat against a former friend will affect
> his strategy. After all, **both sides have the advantage of knowing exactly what and how
> each other will act in battle.**

Bốn điều: lãnh chúa mạnh, warlock mạnh, **giữ lời**, **không bao giờ lùi**. Và chi tiết
hay nhất — hai bên **biết chính xác cách nhau đánh**.

### Map event 40,46,0 — xác nhận chuỗi mệnh lệnh từ bên thứ ba

> "Yes, sir. Ethric's message was received this morning. Sandro is in the area and does
> hold the artifacts. **We have replied to Ethric that we will retrieve the artifacts and
> give them to Jeddite.**"

→ Đường đi: **Ethric → báo động cả vùng → Ufretin (Rampart) lấy → giao cho Jeddite →
Jeddite trả về Ethric.**

### Liên minh và đối thủ

| Bên | Town | Hero | Quan hệ với Jeddite |
|---|---|---|---|
| Xanh dương | Dungeon (55,67) | **Jeddite** (55,68) | — |
| Tan | Rampart (32,38) | Ufretin the Ranger | **Đồng minh** |
| Xanh lá | Stronghold (48,16) | Shiva | Đối thủ — muốn **giữ** artifact |
| Cam | Stronghold Hoddar (6,29) | Jabarkas | Đối thủ — muốn **giữ** artifact |
| Tím | Inferno (8,11) | Ignatius | Phe Lord Jared, riêng biệt |

Timed Event Day 24 "Rumors" xác nhận liên minh chống Sandro **rạn nứt**: Jeddite muốn
trả artifact cho Ethric; Jabarkas muốn giữ.

**Đây là điều phân biệt Jeddite về mặt đạo đức** với Jabarkas và Jared: hắn không muốn
artifact cho mình.

### ⚠️ Kết cục KHÔNG được viết kịch bản

Scenario **không có epilogue**, không có event nào mô tả Jeddite bị đánh bại hay chết.

**Không được viết rằng Sandro giết hắn.** Game không nói vậy.

Event Day 36 (mưu ám sát, thư không ký tên, -10003 vàng) **không được game quy cho
Jeddite** — quy cho hắn là bịa.

---

## 4. Số phận qua các game

### Bio Heroes IV — xác nhận nguyên văn

Có trên cả thelazy (`{{H4Story|Sorcerer|...}}`) và Fandom `Jeddite (Enroth)`:

> "Some sorcerers may enjoy causing destruction, but **Jeddite worships it**. He is a dark
> fanatic wholly committed to the ultimate dissolution of the universe. **No one knows why
> he adopted such insane beliefs**, but neither can anyone convince him to turn to another
> path."

Ở H4: class **Sorcerer**, phe **Asylum**. Infobox Fandom ghi trạng thái "Alive (as of
Heroes IV)" → sống sót qua Reckoning, sang Axeoth.

### ⭐ Khoảng trống H3 → H4: KHÔNG được giải thích — và game NÓI THẲNG điều đó

Đây là phát hiện quan trọng nhất của phần này, và **không phải lỗ hổng nghiên cứu** mà
là đặc điểm có chủ đích của tư liệu.

Chính bio H4 tuyên bố nguyên nhân là bất khả tri: **"No one knows why he adopted such
insane beliefs."**

Không campaign, scenario, hay manual nào nối được từ *học trò trung thành và biết xấu hổ*
của Ethric sang *kẻ cuồng tín tôn thờ sự hủy diệt* ở Axeoth.

**Mọi câu chuyện nhân quả** — rằng Reckoning làm hắn vỡ vụn, rằng sự phản bội của Sandro
làm hắn đổi, rằng mất Ethric làm hắn điên — đều là **bịa**.

Cách viết trung thực: H3 cho ta một người trọng danh dự, định hình bởi lòng trung thành
và mặc cảm tội lỗi; H4 cho ta một kẻ cuồng tín định hình bởi sự tôn thờ hủy diệt; và game
**cố ý** để trống khoảng giữa.

**Không có vai trò campaign nào ở H4.**

---

## 5. ⚠️ CÓ HAI JEDDITE — kiểm disambiguation

thelazy **không có** trang `Jeddite (disambiguation)`. Fandom **có**, và nó quan trọng:

| Trang | Là ai |
|---|---|
| `Jeddite (Enroth)` | Warlock (H3) / Sorcerer (H4). **Chủ thể của bài này** |
| `Jeddite (Ashan)` | Warlock và **Demon cultist** trong *Might & Magic: Heroes VI* |

**Nhân vật khác, continuity khác** (New Universe / Ashan) — chỉ trùng tên. Ngoài phạm vi
Old Universe, **không được gộp vào**.

⚠️ Trang `Heroes from other games` của thelazy xếp portrait H3 và H6 cùng một hàng —
đó là **bảng so sánh portrait**, KHÔNG phải claim về đồng nhất danh tính.

---

## 6. Danh sách xuất hiện đầy đủ

Agent chạy search API ("Jeddite", **51 kết quả**) rồi **mở từng trang scenario** để kiểm,
thay vì tin danh sách của wiki.

| Game/campaign | Scenario | Vai trò |
|---|---|---|
| SoD — Rise of the Necromancer | `Target` | Địch — **lần duy nhất có cốt truyện** |
| SoD — Clash of the Dragons | `The Dragon Mothers` | Địch (chỉ roster) |
| SoD — Clash of the Dragons | `Dragons of Deepest Blue` | Địch (chỉ roster) |
| SoD — The Sword of Frost | `Tarnum the Overlord` | Địch (chỉ roster) |
| SoD — Contested Underworld | `Old Wounds` | Địch (chỉ roster) |
| AB — Armageddon's Blade | `A Friendly Visit` | Địch (chỉ roster) |
| HotA — Terror of the Seas | `Homecoming (HotA)` | Địch (chỉ roster) |
| H4 | Roster Asylum | Sorcerer, còn sống |

**Sáu scenario ngoài `Target` đều chỉ có ĐÚNG MỘT lần xuất hiện** — dòng
`{{hero row|...}}` đặt hero lên map. **Không thoại, không event, không prologue nào.**

**Không có lần xuất hiện nào trong Restoration of Erathia.**

> **Đây là một nhân vật thật sự mỏng.** Một scenario có text, một bio chính thức 40 chữ về
> một tin đồn không liên quan, một bio H4 45 chữ. **Sự mỏng đó chính là phát hiện, không
> phải thất bại nghiên cứu.**

---

## 7. Quan hệ

**Ethric** — thầy cũ. Trang Ethric liệt kê "Jeddite: Former pupil", cùng trạng thái với
Sandro. Mọi thứ khác đến từ chính lá thư: cùng học; Ethric nghi ngờ Sandro từ đầu và đã
cảnh báo Jeddite ("I should have listened to him"); Ethric đích thân báo cho Jeddite về
artifact; mục tiêu của Jeddite là trả lại cho Ethric.

**Sandro** — hạt nhân cảm xúc. Cấu trúc đầy đủ từ game text:

- Cùng học dưới Ethric; Jeddite là "one of Ethric's best students"
- **Jeddite giới thiệu Sandro với Ethric** — hắn là nguyên nhân trực tiếp của việc Sandro
  được học phép, và do đó, trong mắt chính hắn, của mọi thứ Sandro trở thành
- Từng là **bạn thân nhất**
- Cảm xúc chủ đạo là **xấu hổ và tội lỗi**, tự nói ra
- Sandro **vũ khí hóa** đúng cảm giác đó

**Ufretin** — đồng minh Rampart. Trang Ufretin: "In Target, Ufretin tried, but failed,
with Ethric and Jeddite to retrieve..." ⚠️ "tried, but failed" là **văn wiki giả định kết
quả người chơi thắng**; scenario không viết kịch bản thất bại nào.

**Jabarkas** — **không** phải đồng minh. Đối thủ tranh artifact. Không có tương tác trực
tiếp nào được mô tả.

**Không liên hệ trong bất kỳ nguồn nào:** Vidomina, Finneas, Gelu, Crag Hack, Gem, Yog.

---

## Lỗ hổng

1. **Không có mô tả ngoại hình.** Chỉ có file portrait, không có mô tả bằng chữ.
2. **Kết cục trong `Target` không được viết kịch bản** — sống hay chết là kết quả gameplay,
   không phải canon.
3. **Chuyển biến H3 → H4 không được giải thích, và đó là CÓ CHỦ ĐÍCH.** Không phải lỗ
   hổng lấy được.
4. **Đầu mối Zenofex/Xenofex là ngõ cụt.** Tin đồn trong bio không bao giờ được nhắc lại.
5. **Câu "Barbarians due west" mâu thuẫn với vị trí hắn** (xanh dương, Dungeon, đông nam).
   Nhiều khả năng là lỗi copy-paste trong game gốc. **Đáng ghi chú thích, không được lặng
   lẽ "sửa".**
6. **Không nguồn nào nói vì sao Ethric chọn Jeddite** làm người nhận artifact thay vì tự đi lấy.
7. Chỉ số/kỹ năng khởi đầu ở H4 chưa lấy được.

---

## Claim chỉ có wiki chống lưng

| # | Claim | Đánh giá |
|---|---|---|
| 1 | "Former pupil of Ethric. Former best friend of Sandro." | **Đúng nội dung** nhưng là văn wiki. Game nói "he **was** also your best friend", không dùng cụm "former best friend" |
| 2 | Ufretin "tried, but failed" | Văn wiki giả định kết quả người chơi thắng. Scenario không viết |
| 3 | Artifact "từng thuộc về Ethric" | Wiki **tự đánh dấu là suy luận**, suy từ thư Jeddite. Hợp lý nhưng là suy luận |
| 4 | "có thể artifact do Ethric tạo ra" | Wiki tự ghi "though not confirmed". Suy đoán |
| 5 | Fandom "Alive (as of Heroes IV)" | Suy từ việc có mặt trong roster H4; không text nào khẳng định |
| 6 | `Heroes from other games` xếp H3 và H6 cùng hàng | **Bảng portrait, KHÔNG phải claim danh tính** |

---

## ⚠️ Cảnh báo khi viết

Hai đoạn đáng trích nhất (thư và thư trả lời) **chứa lỗi chính tả gốc**: "find a way use",
"Am I suppose run", "use them rise", "By becoming Necromancer".

Nếu trích nguyên văn: **giữ nguyên kèm `[sic]`, hoặc diễn giải.** Lặng lẽ sửa là xuyên tạc
nguồn.
