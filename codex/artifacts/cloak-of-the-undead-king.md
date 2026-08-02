---
id: cloak-of-the-undead-king
type: artifact
name_vi: Cloak of the Undead King
name_en: Cloak of the Undead King
aliases:
  - Cloak of the Undead King
appears_in:
  - sod-new-beginning
  - sod-rise-of-the-necromancer
  - sod-unholy-alliance
status: draft
verify_pass: null
slot: cape
artifact_class: relic
combo_parts:
  - amulet-of-the-undertaker
  - vampires-cowl
  - dead-mans-boots
blocks_slots:
  - necklace
  - feet
cost: 12000
sources_used:
  - h3wiki-cloak-undead-king
  - h3wiki-amulet-of-the-undertaker
  - h3wiki-vampires-cowl
  - h3wiki-dead-mans-boots
  - h3wiki-armor-of-the-damned
  - h3wiki-angelic-alliance
  - h3wiki-necromancy
  - h3wiki-shadow-of-death
  - hota-changelog
  - sod-after-the-amulet
  - sod-retrieving-the-cowl
  - sod-driving-for-the-boots
  - sod-target
  - sod-fall-of-sandro
  - sod-a-tough-start
  - sod-manual-p14
relations:
  - type: assembled_from
    target: amulet-of-the-undertaker
    certainty: EXPLICIT
    source: h3wiki-cloak-undead-king
  - type: assembled_from
    target: vampires-cowl
    certainty: EXPLICIT
    source: h3wiki-cloak-undead-king
  - type: assembled_from
    target: dead-mans-boots
    certainty: EXPLICIT
    source: h3wiki-cloak-undead-king
  # owns → cloak khai ở codex/heroes/sandro.md; nghịch đảo do công cụ sinh
  - type: appears_in
    target: sod-new-beginning
    certainty: EXPLICIT
    source: sod-after-the-amulet
open_questions: 4
---

# Cloak of the Undead King

## Tóm lược

Combination artifact mạnh nhất của phe Necropolis, và là một trong số ít artifact bị
**cấm ghép** trong bản mod lớn nhất của Heroes III vì quá mạnh.

Nhưng điều làm nó đáng nhớ không phải chỉ số. Đây là artifact mà **Sandro lừa một người
tử tế đi thu thập hộ** — bằng cách nói với nàng rằng nó dùng để **chống lại** necromancy.

Về mặt cơ chế, nó biến Necromancy từ một kỹ năng phụ thành cỗ máy chiến tranh: thay vì
hồi sinh Skeleton, hero đủ trình độ hồi sinh thẳng **Lich**.

---

## Xuất xứ

### Ai tạo ra — không ai biết

Cần nói thẳng: **không nguồn nào kể ai làm ra Cloak of the Undead King, hay ba thành phần
của nó.** Chúng chỉ đơn giản tồn tại trong thế giới, nằm trong tay nhiều người giữ khác
nhau.

⚠️ Có một claim lưu hành rằng cả Cloak lẫn Armor of the Damned "từng thuộc về Ethric,
thầy cũ của Sandro". **Claim này bị game text phản bác** — xem *Điểm tranh chấp* mục 1.

Điều game text **có** nói: các thành phần nằm rải rác, được canh giữ bởi quái vật và các
lãnh chúa. Amulet of the Undertaker chôn trong kho báu của bầy Ghost Dragon
{T1* EXPLICIT: sod-after-the-amulet — "Buried under the gems and gold of the Ghost
Dragons' hoard you find the Amulet of the Undertaker"}; Dead Man's Boots được canh bởi một
đội quân undead nhiều tầng. {T1* EXPLICIT: sod-driving-for-the-boots}

### Vụ lừa — cách Sandro có được nó

Sandro không tự đi lấy. Hắn thuê **Gem**, một nữ druid, và dựng một vỏ bọc tinh vi hơn
người ta thường kể.

Hắn **không** đóng vai một wizard đơn thuần. Hắn đóng vai **học trò của một wizard** —
làm việc cho **thầy mình là Ethric**, một học giả ở Bracada:

> "You have agreed to help a wizard's apprentice named Sandro. Sandro's master, Ethric,
> needs an Amulet of the Undertaker to perform anti-necromancy research, but Ethric is an
> academician and Sandro is too inexperienced to go after the Amulet himself."

{T1* EXPLICIT: sod-after-the-amulet}

Chi tiết này quan trọng: **thiện cảm của Gem hướng về Ethric, không phải Sandro.** Nàng
được bán cho hình ảnh một học giả già đang cố chống lại cái ác — và Sandro chỉ là cậu học
trò vụng về không tự đi lấy đồ được.

Vỏ bọc còn trớ trêu hơn: món đồ được giới thiệu là **artifact áp chế necromancy**.

> "He believes he has found a way to construct a necromancy suppressing artifact, but to do
> this he needs three lesser artifacts: an Amulet of the Undertaker, a Vampire's Cowl and a
> pair of Dead Man's Boots."

{T1* EXPLICIT: sod-after-the-amulet — Day 21, "Letter from Sandro"}

Gem tin. Tin đến mức muốn góp tiền:

> "I decided to look up Ethric upon the completion of my quests and persuade him to let me
> donate money towards his research. **I admire his values.**"

{T1* EXPLICIT: sod-after-the-amulet}

Và câu này, đọc lại sau khi biết sự thật, là chỗ đau nhất:

> "I could tell Sandro wouldn't have known how to deal with me if I hadn't taken my
> payment; he was so certain he could buy my loyalty. **The funny thing is I would have
> helped his anti-necromancy research for free.**"

{T1* EXPLICIT: sod-after-the-amulet — Day 49}

Sandro tưởng mình mua được lòng trung thành bằng vàng. Gem đã cho không nếu hắn chỉ cần
hỏi thật.

Có một chi tiết ít người để ý: Gem **được cảnh báo**. Trong một giấc mơ, Amanda "advised
me to be careful, very careful about what I was doing." {T1* EXPLICIT:
sod-retrieving-the-cowl — Day 27} Nàng vẫn đi tiếp, vì "needed to finish gathering the
items Ethric wanted first." {T1* EXPLICIT: sod-retrieving-the-cowl — Day 42}

### Sự vỡ lẽ — chỉ một nửa

Epilogue của Gem thường bị trích cụt. Đọc đủ thì nó buồn hơn nhiều:

> "Sandro has tricked me! But to what purpose? Why would he run off with the Dead Man's
> Boots without paying me? Did he keep the money for himself? **Did he give Ethric the
> other artifacts?** He certainly couldn't have been an agent for Deyja — the undead troops
> I destroyed to get the artifacts were worth more than the artifacts themselves. None of
> this makes sense! **I will have to write to Ethric in Bracada** and tell Lord Fayette
> about this immediately."

{T1* EXPLICIT: sod-driving-for-the-boots — epilogue}

Gem biết mình bị lừa, nhưng **không hiểu bị lừa cái gì.** Nàng vẫn tin Ethric là một học
giả có thật đang chờ nhận đồ, và định viết thư cho ông. Nàng còn suy luận rằng Sandro
*không thể* là người của Deyja — vì lý do hoàn toàn hợp lý (hắn đã phá quá nhiều quân
undead để lấy đồ).

Sự thật thì Ethric có thật — nhưng ông là **kẻ đang truy sát Sandro**, không phải người
thuê nàng. {T1* EXPLICIT: sod-target}

*(Về cách Sandro giữ được vỏ bọc: hắn dùng ảo ảnh phủ lên bộ xương để trông như người
sống. Xem [[sandro]].)*

---

## Lịch sử sở hữu

| Giai đoạn | Ai giữ | Nguồn |
|---|---|---|
| Trước SoD | Ba thành phần rải rác, nhiều người giữ khác nhau | {T1* EXPLICIT: sod-target — "those who lost these two precious artifacts"} |
| *New Beginning* | Gem thu thập, tưởng là cho Ethric | {T1* EXPLICIT: sod-after-the-amulet} |
| *Rise of the Necromancer* | **Sandro** — mang bộ đã ghép | {T1* EXPLICIT: sod-target} |
| *Unholy Alliance* | Sandro, cho tới khi bị bốn anh hùng đánh bại | {T1* EXPLICIT: sod-fall-of-sandro} |
| Sau đó | **Tháo rời, phân tán khắp Antagarich** | {T1* EXPLICIT: sod-fall-of-sandro} |

### Kết cục

Bốn anh hùng nhận ra không thể chỉ đánh bại Sandro:

> "The only certain way is to destroy the artifact that gave him his power and disperse the
> pieces throughout the world."

{T1* EXPLICIT: sod-fall-of-sandro}

Epilogue của Yog:

> "After realizing how corrupting these artifacts are, we decided to split them up into
> less powerful components and disperse them throughout Antagarich. As for us, we decided
> to separate as well, to distance our thoughts from a disaster history may never record."

{T1* EXPLICIT: sod-fall-of-sandro}

Lưu ý "these artifact**s**" — số nhiều, bao gồm cả [[armor-of-the-damned]].

---

## Ý nghĩa trong lore

**Phân tán là cách chuẩn để vô hiệu hóa một combination artifact trong Old Universe.**

Đây không phải trường hợp cá biệt. Chính Yog — người ra quyết định tháo rời Cloak — trước
đó **đã từng làm đúng việc này** với [[angelic-alliance]]:

> "I must take the magical Angelic Alliance sword, break it apart and distribute the pieces
> throughout Tatalia, Erathia and Bracada."

{T1* EXPLICIT: sod-a-tough-start}

Đó là bài kiểm tra lòng trung thành mà Boragus đặt ra cho hắn.
{T2* EXPLICIT: sod-manual-p14 — Yog "must pass the second test – disperse the pieces of the
Angelic Alliance"}

Sự đối xứng này là một trong những chi tiết cấu trúc đẹp nhất của *Shadow of Death*:
**người từng phân tán artifact thiện, cuối cùng phân tán artifact ác** — và chính việc
hắn từng làm điều đó là lý do bốn anh hùng biết chỗ tìm các mảnh Angelic Alliance để
chống lại Sandro.

---

## Gameplay

### Cơ chế gốc

Đây là phần **ổn định** — bản Heroes III / Shadow of Death gốc, không đổi.

| Thuộc tính | Giá trị |
|---|---|
| Slot | Cape |
| Class | Combination (Relic) |
| Giá | 12.000 |
| Chặn slot | Necklace, Feet |

{T1* EXPLICIT: h3wiki-cloak-undead-king}

**Mô tả in-game:**

> "No Necromancy: Functions as Expert Necromancy. Basic Necromancy: Raise Walking Dead.
> Advanced Necromancy: Raise Wights. Expert Necromancy: Raise Liches"

**Hiệu ứng khi ghép đủ:** +30% Necromancy.

**Bảng hồi sinh:**

| Cấp Necromancy của hero | Quân hồi sinh |
|---|---|
| Không có | Skeletons (100%) / Skeleton Warriors (66,6%) |
| Basic | Walking Dead (100%) / Zombies (66,6%) |
| Advanced | Wights (100%) / Wraiths (66,6%) |
| **Expert** | **Liches (100%) / Power Liches (66,6%)** |

{T1* EXPLICIT: h3wiki-cloak-undead-king}

Quân nâng cấp hồi sinh với số lượng ít hơn, tương ứng với số quân chưa nâng cấp lẽ ra hồi
sinh được. {T1* EXPLICIT: h3wiki-cloak-undead-king}

**Text khi nhặt:**
> "You trip over the Cloak of the Undead King, dust it off, and stick it in your pack."

### Quy tắc cộng dồn — chỗ dễ hiểu sai nhất

Hành vi của Cloak **khác nhau** tùy hero có Necromancy hay không:

**Hero KHÔNG có Necromancy:** hồi sinh Skeleton ở mức **cố định 30%**. Sức mạnh artifact
**không tăng được bằng bất cứ thứ gì.**

**Hero CÓ Necromancy:** tăng được bằng Necromancy Amplifier, Soul Prison, và specialty
Necromancy — **nhưng không phải bằng hiệu ứng của chính ba thành phần.**

{T1* EXPLICIT: h3wiki-cloak-undead-king}

Nghĩa là: +5%/+10%/+15% của Amulet, Cowl, Boots **không** cộng thêm lên +30% của bộ hoàn
chỉnh. Ghép bộ **thay thế** hiệu ứng lẻ, không cộng dồn.

⚠️ Wiki **không dẫn nguồn** cho hai quy tắc này. Chúng hợp lý về cơ chế và nhất quán nội
bộ, nhưng lý tưởng nên xác nhận trực tiếp trong game. Xem *Câu hỏi mở*.

### Giới hạn chung của Necromancy

Áp dụng cho mọi cách hồi sinh, không riêng Cloak:

- Số quân hồi sinh **không vượt** số quân đã giết
- Tổng HP hồi sinh **không vượt** HP đã giết
- Necromancy hiệu dụng **giới hạn 100%**

{T1* EXPLICIT: h3wiki-necromancy}

**Khác biệt SoD vs HotA:** SoD tính theo **từng stack** bị giết; HotA tính trên **tổng số**
quân bị giết. {T1* EXPLICIT: h3wiki-necromancy}

### Ba thành phần

| Thành phần | Class | Slot | Giá | Hiệu ứng |
|---|---|---|---|---|
| [[amulet-of-the-undertaker]] | Treasure | Necklace | 2.000 | +5% Necromancy |
| [[vampires-cowl]] | Minor | Cape | 4.000 | +10% Necromancy |
| [[dead-mans-boots]] | Major | Feet | 6.000 | +15% Necromancy |

{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker + h3wiki-vampires-cowl +
h3wiki-dead-mans-boots}

Cả ba đều **vô tác dụng nếu hero không có kỹ năng Necromancy**.

Text khi nhặt từng món cho thấy tính cách khác nhau của chúng:

- **Amulet:** "A dirty amulet lies next to a freshly dug grave..."
- **Cowl:** "You manage to find a Vampire's resting place during the day, and are able to
  slay him easily. **Just for good measure, you take his cowl.**"
- **Boots:** "...you thank the **anonymous donor** and add the boots to your inventory."

{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker + h3wiki-vampires-cowl +
h3wiki-dead-mans-boots}

### Luật giải đấu

> "If tournament rules are turned on, this artifact can still be assembled and will display
> its description, but it does not work."

{T1* EXPLICIT: h3wiki-cloak-undead-king}

Ghép được, hiện mô tả, nhưng **không có tác dụng**.

### Thay đổi qua các bản

⚠️ Phần này **có ngày tháng và sẽ lỗi thời**. Mọi con số ghi rõ phiên bản.

Nguồn của mục này là **changelog HotA**, không phải trang artifact — trang artifact có sai
sót, xem *Điểm tranh chấp* mục 2.

**Giá trị Necromancy đã thay đổi hai lần:**

| Phiên bản | Giá trị (Amulet / Cowl / Boots / Cloak) |
|---|---|
| SoD gốc | 5% / 10% / 15% / **30%** |
| HotA 1.3.0 → 1.7.x | 2,5% / 5% / 7,5% / **15%** (giảm một nửa) |
| HotA 1.8.0 trở đi | 5% / 10% / 15% / **30%** (khôi phục) |

{T1* EXPLICIT: hota-changelog}

HotA 1.3.0 (01/01/2014): "The number of Skeletons raised by necromancy is reduced by half,
as well as bonuses to it from artifacts and a Necromancy Amplifier"

HotA 1.8.0 (31/12/2025): "5/10/15/30% Necromancy boost values are **back**... (instead of
2.5/5/7.5/15%)"

**Cấm ghép:**

| Phiên bản | Thay đổi |
|---|---|
| **1.7.2** (31/12/2024) | Cấm ghép mặc định. Ngoại lệ: template **Anarchy**, **Clash of Dragons**, và "a number of single player scenarios" |
| **1.7.3** (08/06/2025) | Thêm ngoại lệ thứ ba: template **Default Random Map (Legacy)** |

{T1* EXPLICIT: hota-changelog}

Cơ chế nền cho việc cấm này cũng đến ở 1.7.2: "The option of banning combination artifacts,
which influences the possibility to assemble and disassemble them, is added."

**Necromancy Amplifier:** +5% ở SoD, **+10%** ở HotA. Soul Prison: +20%. Cả hai cộng dồn
qua nhiều town. {T1* EXPLICIT: h3wiki-necromancy}

---

## Điểm tranh chấp canon

### 1. "Artifact từng thuộc về Ethric" — bị game text phản bác

Trang tổng quan *Shadow of Death* trên wiki viết:

> "...two powerful artifacts **that once belonged to his former mentor Ethric**."

{T6 FAN_THEORY: h3wiki-shadow-of-death — văn wiki, **không dẫn nguồn**}

**Game text nói ngược.** `sod-target` Day 1:

> "You have also learned Ethric has spread word of your whereabouts to those **who lost
> these two precious artifacts**..."

{T1* EXPLICIT: sod-target}

Chủ cũ là **những bên khác, không được nêu tên** — được phân biệt rõ với Ethric. Trong
toàn bộ scenario, Ethric xuất hiện với **hai** vai: thầy cũ, và kẻ truy đuổi. Không lần
nào là chủ sở hữu.

**Nguồn của hiểu nhầm có lẽ là thư Jeddite:**

> "I will take the artifacts from your rotting corpse and **return them to Ethric**."

{T1* EXPLICIT: sod-target}

Nhưng đó là **ý định giao nộp trong tương lai** của một bên thù địch — không nói gì về sở
hữu quá khứ. Tương tự, Jabarkas "wants the artifacts to remain in their possession" cũng
là chuyện quyền giữ về sau.

**Xử lý:** Codex không dùng claim này.

### 2. Trang artifact ghi sai về HotA 1.7.2

Trang `h3wiki-cloak-undead-king` liệt kê **ba** template ngoại lệ như thể tất cả đều có từ
1.7.2. Đối chiếu changelog cho thấy template thứ ba (**Default Random Map (Legacy)**) chỉ
xuất hiện ở **1.7.3**. {T1* EXPLICIT: hota-changelog}

**Bài học cho toàn dự án:** với mọi claim về HotA, **dùng changelog làm nguồn**, không
dùng trang artifact.

### 3. Armor of the Damned cast mấy spell? — đã giải quyết

Các nguồn nói khác nhau: 4 spell, 5 spell (thêm Disrupting Ray), hoặc các biến thể "Mass".

**Mô tả in-game nói rõ — bốn:**

> "Casts Expert Slow, Curse, Weakness, and Misfortune for 50 rounds at the start of combat."

{T1* EXPLICIT: h3wiki-armor-of-the-damned}

**Nguồn của lỗi "5" đã tìm ra.** Nó nằm trong một đoạn `{{fanopinion}}` trên chính trang
đó:

> "casting a total of four spells at Expert level, at no cost, and leaving the hero free to
> cast another spell on their action (so potentially 5 spells in a single turn)."

{T6 FAN_THEORY: h3wiki-armor-of-the-damned}

Artifact cast **4**; cái thứ năm là lượt của chính hero. Người đọc lướt qua đếm thành 5.

**Disrupting Ray không thuộc bộ này** — không nguồn nào nhắc. Và không có biến thể "Mass";
đây là single cast cấp Expert.

---

## Câu hỏi mở

**Q1. Ai tạo ra Cloak of the Undead King và ba thành phần?**
Không nguồn nào kể. Chúng chỉ tồn tại. Đây là khoảng trống lore lớn nhất của bài.

**Q2. Quy tắc cộng dồn có đúng như wiki mô tả không?**
Hai quy tắc quan trọng — "không tăng được gì" khi hero không có Necromancy, và thành phần
không cộng dồn lên bộ hoàn chỉnh — **không được wiki dẫn nguồn**.
{T1* UNVERIFIED: h3wiki-cloak-undead-king — **không dẫn nguồn**, cần xác nhận trong game}

**Q3. "A number of single player scenarios" là những scenario nào?**
Changelog HotA 1.7.2 nêu ngoại lệ này nhưng **không liệt kê tên**.
{T1* UNVERIFIED: hota-changelog — **không nêu tên**}

**Q4. HotA có đổi chuỗi mô tả in-game của Cloak không?**
Chưa kiểm được. {T1* UNVERIFIED: hota-changelog — **chưa xác minh**}

### Chưa quét đầy đủ

Bài này **chưa liệt kê hết** mọi map có Cloak hoặc thành phần của nó. Phần đã biết chỉ
gồm các scenario trong tuyến Gem và `sod-target`. Chưa quét `Unholy Alliance`, map lẻ, và
scenario HotA.

### Hạn chế nền tảng

Toàn bộ text in-game trong bài mang tier **`T1*`** — bản chép fan wiki, không phải file
game gốc. Xem `sources/REGISTRY.md`.

---

## Nguồn

| Loại | Số lượng | Ghi chú |
|---|---|---|
| `T1*` — text in-game qua trung gian | 15 | heroes.thelazy.net (`?action=raw`) |
| `T2*` — manual chính thức | 1 | `sod-manual-p14` |
| `T6` — wiki cộng đồng / ý kiến fan | 2 | Chỉ dùng để **cảnh báo**, không chống lưng claim nào |

Nguồn quan trọng nhất: **`hota-changelog`** — với mọi claim về HotA, đây là nguồn chuẩn.
Trang artifact trên wiki đã được chứng minh là có sai sót.

---

## Liên kết

**Thành phần:** [[amulet-of-the-undertaker]] · [[vampires-cowl]] · [[dead-mans-boots]]

**Artifact liên quan:** [[armor-of-the-damned]] · [[angelic-alliance]] ·
[[statue-of-legion]]

**Nhân vật:** [[sandro]] · [[gem]] · [[ethric]] · [[yog]] · [[crag-hack]] · [[gelu]]

**Phép thuật:** [[necromancy]]

**Campaign:** [[sod-new-beginning]] · [[sod-rise-of-the-necromancer]] ·
[[sod-unholy-alliance]]
