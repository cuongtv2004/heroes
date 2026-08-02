# Research dossier: ba thành phần Cloak of the Undead King — 2026-08-02

Tư liệu thô. Giữ nguyên tiếng Anh. **Không phải nguồn** — xem `sources/REGISTRY.md`.

Agent dùng `curl` với `action=raw`.

---

## 1. Amulet of the Undertaker

| Trường | Giá trị |
|---|---|
| Slot | Necklace |
| Class | **Treasure** |
| Cost | 2000 |
| Effect | +5% Necromancy |

**Mô tả in-game** (Fandom): "Worn about the neck, this amulet increases your Necromancy
skill by 5%."

**Pickup text** (thelazy `event`): "A dirty amulet lies next to a freshly dug grave. Upon
investigation, you discover it to be the enchanted Amulet of the Undertaker, long thought
lost by mortals."

---

## 2. Vampire's Cowl

| Trường | Giá trị |
|---|---|
| Slot | Cape |
| Class | **Minor** |
| Cost | 4000 |
| Effect | +10% Necromancy |

**Mô tả in-game**: "Worn about the shoulders, this cowl increases your Necromancy skill
by 10%."

**Pickup text**: "You manage to find a Vampire's resting place during the day, and are
able to slay him easily. **Just for good measure, you take his cowl.**"

Trang thelazy có gallery dẫn video prologue `Retrieving the Cowl` — Gem dùng Seeing Pool
để dò tìm Cowl.

---

## 3. Dead Man's Boots

| Trường | Giá trị |
|---|---|
| Slot | Feet |
| Class | **Major** |
| Cost | 6000 |
| Effect | +15% Necromancy |

**Mô tả in-game**: "Worn on the feet, these boots increase your Necromancy skill by 15%."

**Pickup text**: "Discovering a pair of beautifully beaded boots made from the finest and
softest leather, you thank the **anonymous donor** and add the boots to your inventory."

---

## ⚠️ Điều khoản "vô tác dụng nếu không có Necromancy" — LÀ VĂN WIKI, KHÔNG PHẢI GAME TEXT

Đây là phát hiện quan trọng, và nó **sửa một điều bài Cloak hiện đang nói**.

Cả ba trang thelazy đều có câu dạng: "If the equipped hero does not have the Necromancy
secondary skill, the [X] has no effect."

**Nhưng đây là văn wiki, không dẫn nguồn, không phải chuỗi in-game.** Agent không tìm
được nguồn nào trình bày nó như game text.

Thêm nữa: **Fandom không hề nhắc điều khoản này cho bản Heroes III.** Fandom chỉ nêu cơ
chế dự phòng cho bản **Heroes IV**, và bản đó hoạt động **khác hẳn**:

> "Increases the hero's Necromancy skill by 10% **if the hero has the skill. Otherwise,
> it acts as the Basic Necromancy skill.**"

→ **Không được khẳng định điều khoản này như game text.**

---

## 4. Thay đổi HotA — có một sửa đổi cho brief

Từ changelog (nguồn chuẩn):

| Phiên bản | Nội dung nguyên văn |
|---|---|
| **1.3.0** (01/01/2014) | "The number of Skeletons raised by necromancy is reduced by half, as well as bonuses to it from artifacts and a Necromancy Amplifier" |
| **1.7.2** (31/12/2024) | "The Cloak of the Undead King is not allowed to be assembled by default. It remains allowed on the **Anarchy and Clash of Dragons** templates, as well as in a number of single player scenarios" |
| **1.7.3** (08/06/2025) | "Added the 'Default Random Map (Legacy)' template... allowed Cloak of the Undead King..." |
| **1.8.0** (31/12/2025) | "**5/10/15/30%** Necromancy boost values are back for the Amulet of the Undertaker, Vampire's Cowl, Dead Man's Boots, and Cloak of the Undead King (instead of **2.5/5/7.5/15%**)" |

**Hai điểm cần chính xác hóa:**

1. **Dòng 1.3.0 KHÔNG nêu tên ba artifact và KHÔNG nêu con số 2,5/5/7,5%.** Việc giảm một
   nửa thì được xác nhận; các con số cụ thể **chỉ được chứng thực hồi cố** qua dòng 1.8.0.
2. **Bản thân Cloak đi theo chuỗi 30% → 15% → 30%** — giá trị thứ tư mà bài hiện tại chưa
   ghi rõ.

---

## 5. Nơi xuất hiện trong campaign SoD

### `After_the_Amulet` — Amulet

Điều kiện thắng: "Acquire Artifact Amulet of the Undertaker."

**Amulet tại (39, 8, 0).** Text khi lấy:
> "Buried under the gems and gold of the Ghost Dragons' hoard you find the Amulet of the
> Undertaker."

⚠️ **Sắc thái mà cách hiểu thông thường bỏ sót:** ô chứa Amulet **không liệt kê guardian
nào**. Việc canh giữ do một quái vật **liền kề** tại **(38, 8, 0)** đảm nhiệm — một stack
Ghost Dragon: "Despite the pleasant surroundings, the unmistakable odor of death permeates
the area. You see a group of Ghost Dragons ahead." **Số lượng không được nêu.**

Riêng biệt, có một **Event phục kích** tại (32, 5, 0): "Suddenly, the smell of death is
overwhelming. 'Ambush!' screams one of your troops, pointing at the sky." —
**Guardians: 20 Bone Dragons, 20 Ghost Dragons, 20 Bone Dragons; Contents: Morale +2.**

→ **Stack 60 con đó là event phục kích, KHÔNG phải lính canh artifact.** Gộp hai thứ này
là lỗi dễ mắc.

Day 3 định vị: "the Amulet of the Undertaker is located to the North Northeast of
Clifftree Castle in a Ghost Dragon horde."

**Ý kiến fan** (`{{user commentary}}`): "If you are lucky enough, you can win this scenario
by opening Treasure Chests. That's because Amulet of the Undertaker is a treasure."

### `Retrieving_the_Cowl` — Cowl, và toàn bộ tuyến Terek

**Terek là ai:** class **Barbarian / Battle Mage**, tay sai Sandro thuê. Trang `Terek`:
"In Retrieving the Cowl, Terek was the first hero Sandro hired to retrieve the Vampire's
Cowl. He was captured and imprisoned by bandits until Gem arrived and ransomed him and the
cowl."

**Ai bắt:** cướp ở Contested Lands.

Day 1:
> "A Barbarian named Terek has located the Vampire's Cowl for Sandro. Unfortunately,
> Bandits in the Contested Lands captured Terek on his way back from Deyja. Terek convinced
> the bandits that his friends would pay handsomely for his return with his possessions
> intact. My scrying has shown he is being held in an underground prison near the Deyjan
> border."

**Vị trí Terek:** hero bị giam tại **(54, 43, 1)** — dưới hầm.

**Quest Guard tiền chuộc tại (54, 44, 1)** — "Return with: 40000 Gold":
- Đề nghị: "A group of bandits man this tower. They say, 'If you want Terek and his
  equipment, you have to pay his ransom of 40,000 gold.'"
- Chưa đủ: "No 40,000 gold, no Terek."
- Hoàn thành: "Terek is in the prison north of here. His ransom is 40,000 Gold. Do you wish
  to pay the ransom?"

**Giao ở đâu:** điều kiện thắng "Transport Artifact Vampire's Cowl to Leafhall" — Leafhall
là town Rampart trung lập tại **(9, 11, 0)**. Mất Cowl cũng là thua.

⚠️ **Lỗ hổng:** bảng Artifacts của scenario **không** có Cowl như một object trên map. Nó
đi kèm Terek khi được chuộc ("his possessions intact"). **Không tìm được text nào mô tả
Cowl thật sự đổi tay.**

### `Driving_for_the_Boots` — Boots

**Boots tại (2, 103, 0):**
> "In the middle of a small mountain glade sits a pair of Dead Man's Boots. The hair rises
> on the back of your neck. A gentle breeze carries the faint odor of decay. Do you wish to
> pick up the Boots?"

**Lính canh chính xác — bảy slot:**
35 Power Liches · 30 Dread Knights · 30 Vampire Lords · 25 Ghost Dragons ·
30 Vampire Lords · 30 Dread Knights · 35 Power Liches (**tổng 215**)

**Cổng Sandals — HAI object, không phải một:**

1. **Seer's Hut (74, 3, 0)** — "Return with: 25 Ghost Dragons", thưởng **Sandals of the
   Saint**. Đề nghị: "I am a seer. I have foreseen you will need the Sandals of the Saint.
   I have a pair I am willing to give you in return for 25 Ghost Dragons. **She laughs when
   you grit your teeth. 'You'll be back.'**" Hoàn thành: "At last, the 25 Ghost Dragons! It
   took you long enough. Here, take the Sandals. **Their aura of goodness sickens me.**"
2. **Quest Guard (3, 104, 0)** — liền kề Boots, "Return with: Sandals of the Saint". "A
   powerful wizard owns this tower. He refuses to let you pass unless you bring him the
   Sandals of the Saint."

→ Chuỗi: giết 25 Ghost Dragon → Seer cho Sandals → Sandals mở Quest Guard → đánh stack 215
undead → lấy Boots.

Giao về Rampart tại (53, 16, 0).

### `Target` — ba thành phần KHÔNG xuất hiện

Đến `Target`, Sandro đã có bộ hoàn chỉnh. Day 1: "At last! You have the Cloak of the Undead
King and the Armor of the Damned!"

### `Unholy Alliance` — ba thành phần KHÔNG xuất hiện

Ghi chú đáng lưu ý từ trang campaign: "After you have played for Sandro, he appears in
final scenarios as your enemy **with Armor of the Damned, but without Cloak of the Undead
King**."

---

## 6. ⭐ `Master` Day 15 — TEXT KHÔNG NÓI LÀ ARTIFACT NÀO

Trả lời câu hỏi cụ thể. Nguyên văn, thư của Vidomina:

> "Master, there are two Rampart towns in this region. Ethric sent word to them explaining
> the incredible danger posed by you because of the artifacts you carry. Unfortunately,
> dwarves populate one of these towns, and when they learned that **one of your artifacts**
> was stolen from their people, they agreed to join Ethric's fight against you. Be wary when
> passing through this area. Signed, Vidomina."

**KHÔNG. Text chỉ nói "one of your artifacts".**

Day 23 tiếp theo cũng không nêu tên:
> "When the artifact was stolen, **each dwarven tribe thought the other one stole it, and
> they have been at war in the years since.** However, when Ethric's letter arrived, they
> have joined forces **for the first time**."

→ Mọi claim xác định đó là artifact cụ thể nào đều là **suy luận, không phải text**.

---

## 7. Xuất hiện NGOÀI campaign SoD — lỗ hổng thật của đợt trước

Agent chạy backlink query cho cả ba artifact rồi fetch từng scenario.

| Scenario / template | Artifact | Cách xuất hiện |
|---|---|---|
| `Taming_of_the_Wild` | **cả ba**, ô liền kề (67,3)/(68,4)/(69,4) | Nhặt tự do. Text riêng: Boots — "A note on the boots reads: **'Dead men tell no tales'**"; Amulet — "A strange man dressed in black throws an amulet to you, bows and then vanishes"; Cowl — "It looks like a careless vampire left this lying about" |
| `Undead_Unrest` (AB) | Cowl | **Là điều kiện thắng**: "Many undead from Castle Nightmare have broken loose and are rallying around the 'Vampire's Cowl'" |
| `Here_There_Be_Pirates` (AB) | Cowl | Trên map (31,37,0), 26 Dragon Flies canh |
| `Beyond_the_Horizon` | Amulet + Cowl | Seer's Hut đòi Skull Helmet + Rib Cage + Amulet + Cowl → Golden Bow |
| `Tomb_Raiders` (HotA) | Amulet + Cowl | Seer lặp lại; Quest Guard cần Amulet để sửa Skeleton Transformer |
| `Frontier` | Amulet | Seer's Hut → Ring of Vitality |
| `Season_of_Harvest` | Cowl | **Bonus khởi đầu** |
| `From_Day_to_Night` | Boots | **Bonus khởi đầu, trên Thant** |
| `All_for_One` | Cowl | Seer's Hut → +5 Attack |
| `All_Hands_on_Board!` | Cowl | Seer → 50 Vampire Lords |
| `Dead_or_Alive` | Boots | Quest Guard — cùng mẫu text tháp wizard |
| `Viking_We_Shall_Go!` | Boots | Seer → Statesman's Medal |
| `Jorm's_Ambush` | Boots | Seer → 13.349 vàng |
| `The_Life_Guard` | Boots | Shipwreck Survivor |
| `Apocalypse` (HotA template) | **cả ba** | Là artifact **duy nhất** trong danh sách cho phép |

---

## Lỗ hổng

1. **thelazy không có trường "description" riêng** — template `ArtifactNewSB` chỉ có
   `event` (pickup text). Mô tả in-game lấy từ **Fandom**, là nguồn yếu hơn và **không dẫn
   nguồn**. Nhất quán với giá trị của thelazy nhưng không được xác nhận độc lập.
2. **Điều khoản "vô tác dụng nếu không có Necromancy" là văn wiki**, không phải game text.
3. **Số lượng Ghost Dragon canh tại (38,8,0) không được nêu.**
4. **Cowl không có object trên map** trong `Retrieving_the_Cowl`; cơ chế chuyển từ Terek chỉ
   được mô tả bằng văn xuôi.
5. **HotA 1.3.0 không nêu tên ba artifact hay con số 2,5/5/7,5%.**

## Claim chỉ có wiki chống lưng

1. Câu "has no effect without Necromancy" trên cả ba trang — **không dẫn nguồn**, là văn wiki
2. Trang Cloak: "cannot be increased at all" và "(but not the Cloak's components' effects)" —
   không dẫn nguồn
3. Trang Cloak: bảng tỉ lệ 100%/66,6% — không dẫn nguồn
4. Trang Cloak: câu về HotA 1.7.2 — **gộp nhầm hai entry changelog**. Dùng changelog
5. Trang Cloak: hành vi trong luật giải — không dẫn nguồn
6. Mô tả in-game trên Fandom — Fandom không dẫn nguồn ở đâu cả
