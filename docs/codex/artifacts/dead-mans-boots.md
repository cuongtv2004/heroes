---
id: dead-mans-boots
type: artifact
name_vi: Dead Man's Boots
name_en: Dead Man's Boots
aliases: []
appears_in:
  - sod-new-beginning
  - roe-long-live-the-king
status: verified
verify_pass: verify-dead-mans-boots-2026-08-03
slot: feet
artifact_class: major
component_of_artifact: cloak-of-the-undead-king
cost: 6000
sources_used:
  - h3wiki-dead-mans-boots
  - h3wiki-cloak-undead-king
  - h3wiki-sandals-of-the-saint
  - h3wiki-artraits-txt
  - h3wiki-artifact-events
  - h3wiki-amulet-of-the-undertaker
  - h3wiki-vampires-cowl
  - hota-changelog
  - sod-driving-for-the-boots
  - roe-from-day-to-night
  - ab-taming-of-the-wild
  - sod-viking-we-shall-go
  - hc-jorms-ambush
  - hota-dead-or-alive
  - hota-the-life-guard
  - hota-apocalypse-template
  - hota-blacknblue-template
# component_of khai o cloak-of-the-undead-king (assembled_from)
relations: []
open_questions: 1
---

# Dead Man's Boots

## Tóm lược

Thành phần đắt nhất và mạnh nhất của [[cloak-of-the-undead-king]] — và là món được canh giữ
bởi **215 quân undead**, sau một cánh cổng chỉ mở được bằng một artifact của phe Thiện.

Đây cũng là món cuối cùng [[gem]] lấy về, và là món [[sandro]] cướp rồi biến mất.

---

## Xuất xứ

**Game chủ động để trống nguồn gốc** — và tự nói ra điều đó. Text khi nhặt:

> "Discovering a pair of beautifully beaded boots made from the finest and softest leather, you
> thank the **anonymous donor** and add the boots to your inventory."

{T1 EXPLICIT: h3wiki-artraits-txt}
{T1* EXPLICIT: h3wiki-artifact-events — xác nhận độc lập ở trang `Artifact Events`}

"Anonymous donor" — người tặng vô danh, với một đôi giày tên là *giày người chết*.

Đây không phải chuyện "chúng tôi không tìm được nguồn". Sau khi quét toàn bộ 200+ trang trỏ tới
artifact trên thelazy, hai bản dump string trích từ file game, và kiểm cả trang redirect để loại
khả năng trùng tên, kết luận là: **không nguồn nào nêu người tạo, và chính game viết ra sự vô
danh đó.**

{T1* INFERENCE: h3wiki-dead-mans-boots — suy ra từ sự vắng mặt sau khi quét toàn bộ backlinks; chứng cứ dương là chữ "anonymous donor" trong game text}

Mảnh duy nhất tồn tại nói về **người giữ**, không phải người tạo — nằm trong block
`=== Timed events ===` của `Driving for the Boots`, Day 4:

> "I tried to scry the location of the Dead Man's Boots but could not divine anything useful. My
> scrying abilities are more closely tied to living things. However, according to **Sandro**, the
> Boots are in the possession of a **Wizard south of here**."

{T1* EXPLICIT: sod-driving-for-the-boots — timed event Day 4}

⭐ Câu này nối wizard giữ cổng với đôi giày: hắn **không phải người gác ngẫu nhiên** — hắn là
người đang giữ artifact, và Sandro đã biết trước điều đó.

### Nơi tìm thấy — và cánh cổng nghịch lý

Trong `Driving for the Boots`, đôi giày nằm tại **(2, 103, 0)**:

> "In the middle of a small mountain glade sits a pair of Dead Man's Boots. **The hair rises on
> the back of your neck.** A gentle breeze carries the faint odor of decay. Do you wish to pick
> up the Boots?"

{T1* EXPLICIT: sod-driving-for-the-boots}

**Lính canh — bảy stack, tổng 215 quân:**

| Stack | Quân |
|---|---|
| 1 & 7 | 35 Power Liches (mỗi bên) |
| 2 & 6 | 30 Dread Knights |
| 3 & 5 | 30 Vampire Lords |
| 4 | 25 Ghost Dragons |

{T1* EXPLICIT: sod-driving-for-the-boots — nguồn liệt kê bảy stack theo thứ tự; con số tổng 215 là phép cộng của người viết}

Bảy stack xếp **đối xứng gương** quanh stack Ghost Dragon ở giữa: 35 – 30 – 30 – **25** – 30 – 30
– 35.

⭐ **Nghịch lý ở cánh cổng.** Để tới được chỗ đó, người chơi phải qua một Quest Guard tại
(3, 104, 0) — và thứ nó đòi là **Sandals of the Saint**, một artifact của phe Thiện.

Cổng (3, 104, 0) và đôi giày (2, 103, 0) nằm **kề nhau chéo** — nghĩa là cánh cổng này là cửa
duy nhất vào chỗ đặt giày, không phải một chướng ngại giữa đường.

{T1* EXPLICIT: sod-driving-for-the-boots}

Sandals lấy từ một Seer's Hut tại (74, 3, 0), đổi bằng **25 Ghost Dragon**. Lời của bà seer
đáng nhớ:

> "I am a seer. I have foreseen you will need the Sandals of the Saint. I have a pair I am
> willing to give you in return for 25 Ghost Dragons. **She laughs when you grit your teeth.
> 'You'll be back.'**"

Và khi giao đủ:

> "At last, the 25 Ghost Dragons! It took you long enough. Here, take the Sandals. **Their aura
> of goodness sickens me.**"

{T1* EXPLICIT: sod-driving-for-the-boots}

→ Chuỗi: giết 25 Ghost Dragon → đổi lấy Sandals of the Saint → dùng artifact phe Thiện để mở
cổng → đánh 215 quân undead → lấy giày cho một necromancer.

⭐ **Vòng lặp đóng kín mà bà seer đã báo trước.** Seer đòi **đúng 25 Ghost Dragon** — bằng đúng
stack Ghost Dragon canh đôi giày. Nhưng 25 con đó **không lấy được từ đám lính canh**: muốn qua
cổng thì phải có Sandals trước, mà muốn có Sandals thì phải nộp dragon trước. Người chơi buộc
phải tự nuôi quân từ một Necropolis khác.

Câu "**You'll be back**" của bà seer, kèm tiếng cười khi người chơi nghiến răng, vì thế không
phải lời đe dọa suông — đó là mô tả chính xác cấu trúc của map.

{T1* EXPLICIT: sod-driving-for-the-boots}

Text khi chưa nộp đủ giữ đúng giọng đó:

> "No 25 Ghost Dragons? Well then, no Sandals for you."

{T1* EXPLICIT: sod-driving-for-the-boots}

Chi tiết đầy đủ về vụ lừa: xem [[cloak-of-the-undead-king]].

### Món cuối — và cú lừa

Đây là món thứ ba và cuối cùng. Ngay khi có nó, Sandro biến mất:

> "**Sandro has tricked me!** But to what purpose? Why would he run off with the Dead Man's
> Boots without paying me? Did he keep the money for himself? Did he give Ethric the other
> artifacts? **He certainly couldn't have been an agent for Deyja — the undead troops I destroyed
> to get the artifacts were worth more than the artifacts themselves.** None of this makes sense!
> I will have to write to Ethric in Bracada and tell Lord Fayette about this immediately."

{T1* EXPLICIT: sod-driving-for-the-boots — epilogue}

⭐ **Gem tự loại một giả thuyết bằng lý lẽ kinh tế**, và lý lẽ đó đúng: 215 quân undead cấp cao
đáng giá hơn ba artifact Necromancy hạng Treasure/Minor/Major. Nếu Sandro làm cho [[deyja]] thì
vụ này là **lỗ**. Suy luận của Gem hợp lý — nhưng vẫn dẫn tới kết luận sai, vì Sandro không làm
cho ai ngoài chính hắn.

Đáng chú ý: Gem định viết thư cho **Ethric** — người mà cô tưởng là khách hàng thật sự. Xem
[[ethric]] và [[cloak-of-the-undead-king]].

---

## Gameplay

### Cơ chế gốc

| Thuộc tính | Giá trị |
|---|---|
| Slot | Feet |
| Class | **Major** |
| Giá | 6.000 |
| Hiệu ứng | **+15% Necromancy** |

{T1* EXPLICIT: h3wiki-dead-mans-boots}

**Mô tả in-game:** "Worn on the feet, these boots increase your Necromancy skill by 15%."
{T1 EXPLICIT: h3wiki-artraits-txt}

⭐ **Nguồn của câu này là `T1` thật, không dấu sao.** Nó đến từ `H3Bitmap.lod > artraits.txt` —
string table **trích trực tiếp từ file game**, không phải bản chép của người viết wiki. Bản đầu
của bài dẫn Fandom (`T6`, không dẫn nguồn) cho cùng câu này; Fandom chỉ là bản chép lại của chính
chuỗi đó. Xem `REGISTRY.md` → `h3wiki-artraits-txt`.

Đây là thành phần **mạnh nhất** trong ba — một mình nó bằng Amulet cộng Cowl.
{T1* INFERENCE: h3wiki-dead-mans-boots + h3wiki-amulet-of-the-undertaker + h3wiki-vampires-cowl — phép cộng của người viết: 5% + 10% = 15%}

"Mạnh nhất" đúng theo **cả ba** thước đo độc lập: % Necromancy (15 > 10 > 5), giá
(6.000 > 4.000 > 2.000), và class (Major > Minor > Treasure).

⭐ Quan hệ này **bất biến qua phiên bản**. Trong HotA 1.3.0–1.7.x cả ba giá trị bị chia đôi
*theo tỷ lệ* (2,5 + 5 = 7,5), nên "một mình nó bằng hai cái kia cộng lại" vẫn đúng. Đó là dấu
hiệu một lựa chọn thiết kế có ý, không phải trùng hợp số học.

⚠️ **Điều khoản "vô tác dụng nếu hero không có Necromancy" là văn wiki, không phải game text.**

Câu trên wiki: "If the equipped hero does not have the Necromancy secondary skill, the Dead Man's
Boots **has** no effect."

Ba bằng chứng cho thấy đây là văn người viết wiki, không phải chuỗi trong game:

1. **Vị trí trong wikitext.** Câu nằm **ngoài** template `{{ArtifactNewSB}}`, ở thân bài trần.
   Mọi game text trên wiki này đều bị bọc trong tham số template (`| event =`, `| effect =`).
2. **Vắng mặt khỏi cả hai bản dump string trích từ file game.** `artraits.txt` chỉ có câu
   "Worn on the feet..." — không kèm điều kiện nào.
3. ⭐ **Lỗi ngữ pháp truy được về nguyên nhân.** Câu y hệt có trên trang Amulet ("the Amulet of
   the Undertaker **has** no effect") và Cowl ("the Vampire's Cowl **has** no effect") — ở đó
   `has` **đúng** vì chủ ngữ số ít. Trên trang Boots chủ ngữ là "Boots" (số nhiều) nên `has`
   **sai**. Đó là dấu vết **copy-paste giữa ba trang** — bằng chứng gần như quyết định.

{T1* INFERENCE: h3wiki-dead-mans-boots + h3wiki-artraits-txt — suy ra theo ba bước trên}

⚠️ **Ba wiki cùng lỗi này không phải ba nguồn.** `homm.fandom.com` và `homm.miraheze.org` trả về
wikitext **giống hệt từng byte** với thelazy, kể cả lỗi `has`. Chúng là **fork**, không phải xác
nhận độc lập.

Bản thân **cơ chế** thì đúng — không có skill Necromancy thì không hồi sinh skeleton — nhưng đó
là mô tả do wiki suy ra, không phải câu game nói.

### Thay đổi qua các bản

| Phiên bản | Giá trị |
|---|---|
| SoD gốc | **+15%** |
| HotA 1.3.0 → 1.7.x | **+7,5%** |
| HotA 1.8.0 trở đi | **+15%** (khôi phục) |

{T1* EXPLICIT: hota-changelog}

---

## Xuất hiện trong game

⚠️ **Cột *Sản phẩm* không phải chi tiết vụn.** Đôi giày xuất hiện trong **năm** sản phẩm khác
nhau, trong đó ba mục là **HotA** — expansion do fan làm, không phải New World Computing — và
một mục là *Heroes Chronicles*. Gộp phẳng cả danh sách sẽ khiến người đọc tưởng tất cả là SoD.

| Scenario | Sản phẩm | Cách xuất hiện |
|---|---|---|
| `Driving for the Boots` | SoD | Sau Quest Guard, 215 quân undead canh {T1* EXPLICIT: sod-driving-for-the-boots} |
| `From Day to Night` | **RoE** | **Bonus khởi đầu, trên Thant** {T1* EXPLICIT: roe-from-day-to-night} |
| `Taming of the Wild` | **AB** | Nhặt tự do, (67, 3, 0) {T1* EXPLICIT: ab-taming-of-the-wild} |
| `Viking We Shall Go!` | SoD | Seer's Hut (53, 116, 0) → Statesman's Medal {T1* EXPLICIT: sod-viking-we-shall-go} |
| `Viking We Shall Go! (Allies)` | SoD | Trang scenario **riêng**, cùng toạ độ, cùng phần thưởng {T1* EXPLICIT: sod-viking-we-shall-go} |
| `Jorm's Ambush` | **Heroes Chronicles** | Seer's Hut (3, 7, 1) → 13.349 vàng {T1* EXPLICIT: hc-jorms-ambush} |
| `Dead or Alive` | **HotA** | Quest Guard (56, 30, 0) — cùng mẫu text tháp wizard {T1* EXPLICIT: hota-dead-or-alive} |
| `The Life Guard` | **HotA** | Từ Shipwreck Survivor (35, 25, 1) {T1* EXPLICIT: hota-the-life-guard} |
| `Apocalypse` (template) | **HotA** | Nằm trong danh sách `Allowed artifacts` — xem cảnh báo dưới {T6 INFERENCE: hota-apocalypse-template} |
| `Black'n'Blue` (template) | **HotA** | ⛔ **BỊ CẤM** — nằm trong `Banned artifacts` {T6 EXPLICIT: hota-blacknblue-template} |

⛔ **Hai template HotA đi NGƯỢC chiều nhau.** Trên `Apocalypse` đôi giày được cho phép; trên
`Black'n'Blue` nó **bị cấm**. Hai template này hay được nhắc cạnh nhau nên rất dễ đọc thành cùng
một chiều — bản đầu của bài này đã mắc đúng lỗi đó, ghi `Black'n'Blue` là "cho phép".

⚠️ **"Một trong ba artifact *duy nhất*" là cách đọc sai.** Trang `Apocalypse` liệt kê ba artifact
— đúng là ba thành phần Cloak — nhưng dưới đầu đề `Allowed artifacts:`, và **không hề có chữ
"only"**. Ba lý do không được đọc thành "duy nhất":

- **Changelog không chống lưng.** `Apocalypse` chỉ xuất hiện **hai lần** trong toàn bộ 201.529
  byte changelog, không lần nào là danh sách artifact.
- **Có bằng chứng ngược.** Bản 1.7.1 cấm thêm *Wanderer's Boots* — nếu template chỉ cho phép ba
  artifact thì lệnh cấm đó **vô nghĩa**, vì nó đã bị cấm sẵn. Cách đọc dung hòa: "allowed" =
  được cho phép **thêm**, ngoài các lệnh cấm mặc định.
- **Trang luật chính thức không có danh sách này.** `h3hota.com/en/rules` có mục Apocalypse
  nhưng không liệt kê artifact cho phép hay bị cấm nào.

{T1* EXPLICIT: hota-changelog — 1.5.0 và 1.7.1 là hai lần duy nhất changelog nhắc Apocalypse}

📅 **Phạm vi phiên bản:** trang `Apocalypse` sửa lần cuối **2025-05-14** ≈ HotA 1.7.2–1.7.3,
**trước 1.8.0**. Trang tự nó không ghi phiên bản nào.

⭐ **`Taming of the Wild` là map đáng chú ý nhất trong bảng.** Cả **ba** thành phần Cloak nằm kề
nhau và đều nhặt tự do, không một lính canh: Boots (67, 3, 0), Amulet (68, 4, 0), Cowl
(69, 4, 0). Nghĩa là map này cho ghép trọn [[cloak-of-the-undead-king]] gần như miễn phí — trái
ngược hoàn toàn với `Driving for the Boots`, nơi chỉ một thành phần đã ngốn 215 quân undead và
một artifact phe Thiện.

{T1* EXPLICIT: ab-taming-of-the-wild}

Map này cũng có text riêng cho đôi giày:

> "A note on the boots reads: **"Dead men tell no tales"**."

{T1* EXPLICIT: ab-taming-of-the-wild}

*(Dấu chấm nằm **ngoài** ngoặc kép — đúng như game viết.)*

---

## Câu hỏi mở

**~~Q1. Mô tả in-game chính xác?~~ — ✅ ĐÃ GIẢI QUYẾT (2026-08-03)**

Câu hỏi cũ đặt ra vì mô tả in-game chỉ lấy được từ bảng Fandom (`T6`, không dẫn nguồn). Luồng
verify tìm ra nguồn tốt hơn hẳn: `Talk:Artifact/descriptions` trên thelazy, tự ghi ở đầu bảng
`Information from H3Bitmap.lod > artraits.txt` — **string table trích từ file game**, tức `T1`
thật. Xem mục *Gameplay*.

**Q2. Vì sao cần Sandals of the Saint để qua cổng?**

Text của Quest Guard:

> "A powerful wizard owns this tower. He refuses to let you pass unless you bring him the Sandals
> of the Saint."

{T1* EXPLICIT: sod-driving-for-the-boots}

Sau khi đọc hết cả 12.995 byte của scenario — prologue, 14 timed event, objects, hero, artifact,
Seer's Hut, Quest Guard, epilogue — **không đoạn nào giải thích vì sao phải là *Sandals of the
Saint*** cụ thể, chứ không phải vật gì khác.

{T1* INFERENCE: sod-driving-for-the-boots — suy ra từ sự vắng mặt sau khi đọc toàn bộ scenario, không phải chỉ prologue/epilogue}

Mảnh gần nhất với một lời giải thích là câu của bà seer khi giao Sandals — nó xác lập Sandals là
**vật thuộc phe Thiện**, nhưng không nói vì sao wizard đòi nó:

> "Here, take the Sandals. **Their aura of goodness sickens me.**"

{T1* EXPLICIT: sod-driving-for-the-boots}

---

## Liên kết

**Bộ hoàn chỉnh:** [[cloak-of-the-undead-king]]

**Thành phần cùng bộ:** [[amulet-of-the-undertaker]] · [[vampires-cowl]]

**Artifact liên quan:** [[sandals-of-the-saint]]

**Nhân vật:** [[gem]] · [[sandro]] · [[thant]]

**Campaign:** [[sod-new-beginning]] · [[roe-long-live-the-king]]
