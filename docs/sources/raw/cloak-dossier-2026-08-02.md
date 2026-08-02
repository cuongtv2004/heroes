# Research dossier: Cloak of the Undead King — 2026-08-02

Tư liệu thô. Giữ nguyên tiếng Anh — độ chính xác quan trọng hơn dễ đọc.

**Cảnh báo:** đây là **tư liệu thô, không phải nguồn**. Mọi text "verbatim" là bản chép
của heroes.thelazy.net qua `?action=raw`, không phải file game. Xem
`sources/REGISTRY.md` mục "Lưu ý về T1*".

**Ghi chú phương pháp của agent:** WebFetch tóm tắt thay vì trả wikitext nguyên văn, nên
các trang scenario được kéo bằng `curl` và đọc từ đĩa. Mọi số liệu và trích dẫn dưới đây
lấy từ file thô.

---

## 1. Cơ chế — Cloak of the Undead King

| Trường | Giá trị |
|---|---|
| Slot | Cape |
| Class | Combo (`Relic artifacts` + `Combination artifacts`) |
| Cost | 12000 |
| Chặn slot | Necklace, Feet |
| Thành phần | Amulet of the Undertaker, Vampire's Cowl, Dead Man's Boots |

**Pickup text:**
> "You trip over the Cloak of the Undead King, dust it off, and stick it in your pack."

**Mô tả in-game (`effect`):**
> "No Necromancy: Functions as Expert Necromancy. Basic Necromancy: Raise Walking Dead.
> Advanced Necromancy: Raise Wights. Expert Necromancy: Raise Liches"

**`ceffect`:** "+30% Necromancy"

**Bảng hồi sinh:**

| Cấp Necromancy | Quân hồi sinh |
|---|---|
| Không có | Skeletons (100%) / Skeleton Warriors (66,6%) |
| Basic | Walking Dead (100%) / Zombies (66,6%) |
| Advanced | Wights (100%) / Wraiths (66,6%) |
| Expert | Liches (100%) / Power Liches (66,6%) |

Ghi chú trên trang:
> "Upgraded creatures are raised at a reduced rate in relation to the quantity of
> unupgraded troops that could have been raised in their stead."

### Điểm tinh tế — cái gì cộng dồn, cái gì không

Đây là chỗ dễ viết sai nhất:

- **Hero KHÔNG có Necromancy:** hồi sinh Skeletons/Skeleton Warriors ở mức **cố định
  30%**. Sức mạnh artifact **"cannot be increased at all"**.
- **Hero CÓ Necromancy:** tăng được bằng "the Necromancy Amplifier, Soul Prison, and the
  Necromancy specialty (**but not the Cloak's components' effects**)."

Tức là hiệu ứng +5/+10/+15% của ba thành phần **không** cộng lên trên +30% của bộ hoàn
chỉnh.

⚠️ Trang wiki **không dẫn nguồn** cho hai quy tắc này. Hợp lý về cơ chế và nhất quán nội
bộ, nhưng lý tưởng nên xác nhận trong game.

**Luật giải:**
> "If tournament rules are turned on, this artifact can still be assembled and will
> display its description, but it does not work."

### Ba thành phần

Mỗi thành phần đều có: "If the equipped hero does not have the Necromancy secondary
skill, [it] has no effect."

| Thành phần | Class | Slot | Cost | Hiệu ứng |
|---|---|---|---|---|
| Amulet of the Undertaker | Treasure | Necklace | 2000 | +5% Necromancy |
| Vampire's Cowl | Minor | Cape | 4000 | +10% Necromancy |
| Dead Man's Boots | Major | Feet | 6000 | +15% Necromancy |

**Pickup text từng món:**

- Amulet: "A dirty amulet lies next to a freshly dug grave. Upon investigation, you
  discover it to be the enchanted Amulet of the Undertaker, long thought lost by
  mortals."
- Cowl: "You manage to find a Vampire's resting place during the day, and are able to
  slay him easily. Just for good measure, you take his cowl."
- Boots: "Discovering a pair of beautifully beaded boots made from the finest and softest
  leather, you thank the anonymous donor and add the boots to your inventory."

### Giới hạn của Necromancy nói chung

- Số quân hồi sinh **không bao giờ vượt** số quân đã giết
- Tổng HP hồi sinh **không bao giờ vượt** HP đã giết
- Necromancy hiệu dụng **giới hạn ở 100%**
- **SoD:** tính theo từng stack bị giết · **HotA:** tính trên tổng số quân bị giết
- Amplifier: +5% (SoD) / +10% (HotA) · Soul Prison: +20% · cả hai cộng dồn qua nhiều town

---

## 2. Trạng thái cân bằng HotA — nghi ngờ của đợt trước là ĐÚNG

Câu trên trang artifact **gộp nhầm hai phiên bản**.

**1.7.2 (31/DEC/2024)**, mục Gameplay — nguyên văn changelog:
> "The Cloak of the Undead King is not allowed to be assembled by default. It remains
> allowed on the Anarchy and Clash of Dragons templates, as well as in a number of single
> player scenarios"

**Không nhắc Legacy.** (changelog dòng 253, trong block 1.7.2 từ dòng 167–341.)

**1.7.3 (08/JUN/2025)**, mục Miscellaneous:
> "Added the 'Default Random Map (Legacy)' template, which contains a number of elements
> excluded from the standard HotA gameplay: allowed Cloak of the Undead King, monsters
> joining for free, Resistance instead of Interference, allowed Galthran and Sir Mullich,
> etc."

(dòng 162, trong block 1.7.3 từ dòng 86–166.)

**Kết luận:** lệnh cấm đến ở **1.7.2** với **hai** template ngoại lệ; ngoại lệ **thứ ba**
(Default Random Map (Legacy)) đến ở **1.7.3**. Trang artifact ghi cả ba như thể là trạng
thái 1.7.2 — **sai như đang viết**. Codex không được chép nguyên câu đó.

Cũng ở 1.7.3: "Fixed a bug: HotA-original combination artifacts were not included in the
list of combination artifacts banned from assembly".

Cơ chế nền đến ở 1.7.2: "The option of banning combination artifacts, which influences
the possibility to assemble and disassemble them, is added."

### ⚠️ Phát hiện ngoài yêu cầu — CON SỐ ĐÃ ĐỔI QUA CÁC BẢN

Đây là phát hiện quan trọng nhất về gameplay:

- **HotA 1.3.0 (01/JAN/2014):** "The number of Skeletons raised by necromancy is reduced
  by half, as well as bonuses to it from artifacts and a Necromancy Amplifier"
- **HotA 1.8.0 (31/DEC/2025):** "5/10/15/30% Necromancy boost values are back for the
  Amulet of the Undertaker, Vampire's Cowl, Dead Man's Boots, and Cloak of the Undead King
  (**instead of 2.5/5/7.5/15%**)"

**Nghĩa là:** trong HotA từ 1.3.0 đến 1.7.x, giá trị là **2,5/5/7,5/15%**. Con số chuẩn
SoD 5/10/15/30% chỉ **trở lại ở 1.8.0**.

**Mọi phát biểu "+30%" phải ghi rõ phạm vi: SoD, hoặc HotA 1.8.0 trở lên.**

---

## 3. Nguồn gốc lore — vụ lừa Gem

**Điểm tinh tế mà bản tóm tắt thường bỏ:** vỏ bọc không chỉ là "nghiên cứu chống
necromancy". Sandro đóng vai **học trò của một wizard**, làm việc cho **thầy mình là
Ethric**, một học giả ở Bracada. Thiện cảm của Gem hướng về **Ethric**, không phải Sandro.
Đó là điều làm epilogue đau.

**`After_the_Amulet`, region text:**
> "You have agreed to help a wizard's apprentice named Sandro. Sandro's master, Ethric,
> needs an Amulet of the Undertaker to perform anti-necromancy research, but Ethric is an
> academician and Sandro is too inexperienced to go after the Amulet himself."

**Prologue (Gem):**
> "I have met a Wizard named Sandro who is conducting research to combat necromancy. He is
> creating a magical amulet, which will ward off the undead and wants to pay me a large
> sum of gold to find the pieces he needs to construct it. He seems to think me quite the
> mercenary."

**Day 21, "Letter from Sandro" — yêu cầu đủ ba món:**
> "It seems that Ethric is doing more than just research. He believes he has found a way
> to construct a necromancy suppressing artifact, but to do this he needs three lesser
> artifacts: an Amulet of the Undertaker, a Vampire's Cowl and a pair of Dead Man's Boots."

Gem đáp rằng "Ethric's project was a worthwhile one" và quyết định "to look up Ethric upon
the completion of my quests and persuade him to let me donate money towards his research.
**I admire his values.**"

**Day 49 — sự trớ trêu:**
> "I could tell Sandro wouldn't have known how to deal with me if I hadn't taken my
> payment; he was so certain he could buy my loyalty. **The funny thing is I would have
> helped his anti-necromancy research for free.**"

**`Retrieving_the_Cowl`** — tuyến Terek, tiền chuộc 40.000 vàng.

Day 27, giấc mơ: "I told her I had recovered the Amulet for Sandro and agreed to help his
master, Ethric, find a Vampire's Cowl and a pair of Dead Man's Boots." Amanda "advised me
to be careful, very careful about what I was doing."

Day 42: "needed to finish gathering the items Ethric wanted first."

**`Driving_for_the_Boots` — epilogue, câu quan trọng nhất:**
> "Sandro has tricked me! But to what purpose? Why would he run off with the Dead Man's
> Boots without paying me? Did he keep the money for himself? Did he give Ethric the other
> artifacts? He certainly couldn't have been an agent for Deyja — the undead troops I
> destroyed to get the artifacts were worth more than the artifacts themselves. None of
> this makes sense! **I will have to write to Ethric in Bracada** and tell Lord Fayette
> about this immediately."

**Chú ý:** Gem **không hiểu** chuyện gì đã xảy ra. Nàng vẫn tin Ethric là có thật và định
viết thư cho ông. Sự vỡ lẽ chỉ là **một phần**.

---

## 4. ⚠️ CLAIM "ARTIFACT TỪNG THUỘC VỀ ETHRIC" — BỊ GAME TEXT PHẢN BÁC

**Xuất hiện ở đâu** — trang `The_Shadow_of_Death`, văn wiki, **không dẫn nguồn**:
> "The storyline revolves around Sandro the Necromancer, who ten-year plot to reassemble
> two powerful artifacts **that once belonged to his former mentor Ethric**."

(lỗi ngữ pháp "who ten-year plot" có trong bản gốc)

**`Target` thật sự nói gì** — Ethric xuất hiện nhiều lần, **không lần nào với tư cách chủ
cũ**:

- Region text: "Ethric is a sly old Warlock. He has spread word of Sandro and the
  artifacts he carries to the lords of this region. Some of the lords want these artifacts
  for their own use; others want to destroy them."
- Sandro: "It seems Ethric, my old master, has finally tracked me down."
- **Day 1 — dòng quyết định:** "You have also learned Ethric has spread word of your
  whereabouts to those **who lost these two precious artifacts**..."
  → chủ cũ là **những bên khác, không được nêu tên**, phân biệt rõ với Ethric.
- Thư Jeddite: "I will take the artifacts from your rotting corpse and **return them to
  Ethric**." → ý định **giao nộp trong tương lai** của một bên thù địch. Không nói gì về
  sở hữu quá khứ. **Đây có lẽ là nguồn của hiểu nhầm.**
- Jabarkas "wants the artifacts to remain in their possession" → cũng về quyền giữ trong
  tương lai.

**Kết luận:** Ethric là **thầy cũ** của Sandro (có game text, chính Sandro nói) và là
**kẻ truy đuổi** huy động kẻ thù chống hắn (có game text). Nhưng việc artifact **"từng
thuộc về"** Ethric **không có game text nào chống lưng, và bị dòng Day 1 phản bác**.

**Khuyến nghị:** không đưa claim này vào Codex. Cách diễn đạt an toàn: Ethric là thầy cũ
đã truy đuổi Sandro vì các artifact; các thành phần được lấy từ nhiều necromancer và
người giữ khác nhau, qua tay Gem và Crag Hack.

Bối cảnh thêm: cùng trang đó ghi Sandro "uses illusionary magic to take the form of a
living human" — giải thích vì sao vỏ bọc "học trò wizard" lừa được Gem.

---

## 5. Kết cục

**`Fall_of_Sandro`, region text:**
> "Sandro must be conquered to ensure that he will never rise to power and threaten
> Antagarich again. The only certain way is to destroy the artifact that gave him his power
> and disperse the pieces throughout the world."

**Epilogue (Yog):**
> "After realizing how corrupting these artifacts are, we decided to split them up into
> less powerful components and disperse them throughout Antagarich. As for us, we decided
> to separate as well, to distance our thoughts from a disaster history may never record."

**Chú ý:** "these artifacts" là **số nhiều** — bao gồm cả Cloak lẫn Armor of the Damned.

Điều kiện thắng: cả bốn hero (Gelu, Gem, Crag Hack, Yog) phải sống, trong 4 tháng, độ khó
Impossible.

---

## 6. Armor of the Damned — tranh chấp số spell ĐÃ GIẢI QUYẾT

Slot Torso; Combo; 12000; chặn Helmet, Weapon, Shield.
Thành phần: Skull Helmet, Rib Cage, Blackshard of the Dead Knight, Shield of the Yawning
Dead. `ceffect`: +3 Attack, +3 Defense, +2 Power, +2 Knowledge.

**Hiệu ứng in-game nguyên văn:**
> "Casts Expert Slow, Curse, Weakness, and Misfortune for 50 rounds at the start of
> combat."

→ **BỐN spell, 50 lượt. thelazy đúng.**

**Nguồn của lỗi "5 spell" đã tìm ra — là ý kiến fan.** Đoạn đó nằm trong wrapper
`{{fanopinion|...}}`:
> "casting a total of four spells at Expert level, at no cost, and leaving the hero free
> to cast another spell on their action (so potentially 5 spells in a single turn)."

Armor cast **4**; cái thứ 5 là lượt của chính hero. **Disrupting Ray không thuộc bộ này**
— không nguồn nào nhắc. Không có biến thể "Mass"; là single cast cấp Expert.

Cơ chế đáng ghi: spell chỉ kích hoạt khi một quân đồng minh được đi lượt (bị trì hoãn nếu
morale thấp); bị vô hiệu bởi immunity, Cursed Ground, artifact kháng phép; **hoạt động
bình thường trong Anti-Magic Garrison**. Cuthbert, Olema, Mirlanda (và Eanswythe ở HotA)
tăng hiệu quả Weakness của nó.

---

## 7. Angelic Alliance

Slot Weapon; **84000** (artifact đắt nhất SoD); chặn Helmet, Necklace, Torso, Feet, Shield.

Sáu thành phần: Helm of Heavenly Enlightenment, Celestial Necklace of Bliss,
Armor of Wonder, Sandals of the Saint, Sword of Judgement, Lion's Shield of Courage.

`ceffect`: **+21 cả bốn primary skill** (cao nhất game).

Hiệu ứng: trộn quân phe good/neutral không bị phạt morale + Expert Prayer 10 lượt đầu
trận. Thêm quân Inferno/Dungeon/Necropolis hoặc neutral thì mất bonus.

**Tuyến Yog phân tán — XÁC NHẬN:**

Manual tr.14: Yog "must pass the second test – disperse the pieces of the Angelic
Alliance."

Yog trong `A_Tough_Start`: "I must take the magical Angelic Alliance sword, break it apart
and distribute the pieces throughout Tatalia, Erathia and Bracada."

Đây là bài kiểm tra lòng trung thành của Boragus. Đáng chú ý về mặt cấu trúc: **phân tán
là cách chuẩn để vô hiệu hóa một combination artifact** — đúng như số phận của Cloak.

---

## 8. Nơi xuất hiện (chưa đầy đủ)

- Amulet tại (39,8,0) trong `After_the_Amulet`, canh bởi Ghost Dragon tại (38,8,0) —
  "Buried under the gems and gold of the Ghost Dragons' hoard you find the Amulet of the
  Undertaker."
- Cowl lấy qua việc chuộc Terek (40.000 vàng, quest guard tại 54,44,1), giao ở Leafhall
- Boots tại (2,103,0) — canh bởi 35 Power Liches, 30 Dread Knights, 30 Vampire Lords,
  25 Ghost Dragons, 30 Vampire Lords, 30 Dread Knights, 35 Power Liches; cần
  Sandals of the Saint (từ Seer's Hut đòi 25 Ghost Dragons) để qua quest guard
- Sandro mang Cloak đã ghép trong `Target`

⚠️ **Chưa quét đầy đủ toàn bộ campaign.** Xem Lỗ hổng.

---

## Lỗ hổng

1. **Chưa quét hết nơi xuất hiện.** Chưa liệt kê mọi map có Cloak hoặc thành phần
   (`Unholy_Alliance`, map lẻ, scenario HotA).
2. **"a number of single player scenarios"** (ngoại lệ 1.7.2) — changelog **không nêu tên**.
   Không giải quyết được từ nguồn này.
3. **Không có text in-game HotA cho Cloak** — chưa rõ HotA có đổi chuỗi mô tả không.
4. **Phần Crag Hack (thành phần Armor of the Damned) chưa fetch** — đợt này chỉ làm tuyến
   Gem/Cloak.
5. Không kiểm file ảnh render chính thức.

---

## Claim chỉ có wiki chống lưng

| # | Claim | Mức |
|---|---|---|
| 1 | **"artifacts that once belonged to his former mentor Ethric"** (`The_Shadow_of_Death`) | **BỊ GAME TEXT PHẢN BÁC.** Ưu tiên sửa cao nhất |
| 2 | Câu 1.7.2 trên trang Cloak liệt kê ba template ngoại lệ | **Sai** — gộp nhầm 1.7.2 và 1.7.3 |
| 3 | "5 spell" cho Armor of the Damned | Trong `{{fanopinion}}`. Không chính thức |
| 4 | Armor of the Damned "một trong những combo artifact yếu nhất… Misfortune kém" | `{{fanopinion}}`, ý kiến |
| 5 | Mẹo Treasure Chest trong `After_the_Amulet` | Trong `{{user commentary}}` |
| 6 | Lời khuyên chiến thuật trên trang `Necromancy` | Văn editorial **không** có wrapper, nhưng đọc như lời khuyên fan |
| 7 | Quy tắc "cannot be increased at all" và thành phần không cộng dồn | **Không dẫn nguồn.** Hợp lý và nhất quán, nhưng lý tưởng nên xác nhận trong game |
