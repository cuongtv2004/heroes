---
id: amulet-of-the-undertaker
type: artifact
name_vi: Amulet of the Undertaker
name_en: Amulet of the Undertaker
aliases: []
appears_in:
  - sod-new-beginning
status: verified
verify_pass: verify-amulet-of-the-undertaker-2026-08-03
slot: necklace
artifact_class: treasure
component_of_artifact: cloak-of-the-undead-king
cost: 2000
sources_used:
  - h3wiki-amulet-of-the-undertaker
  - h3wiki-cloak-undead-king
  - h3wiki-artraits-txt
  - h3wiki-vampires-cowl
  - h3wiki-dead-mans-boots
  - hota-changelog
  - sod-after-the-amulet
  - ab-taming-of-the-wild
  - hota-beyond-the-horizon
  - hota-tomb-raiders
  - hota-frontier
  - hota-apocalypse-template
  - hota-nine-day-wonder
  - fandom-h4-artifact-list
  - fandom-prelude-to-invasion
# component_of khai o cloak-of-the-undead-king (assembled_from);
# nghich dao do cong cu sinh - xem SCHEMA.md muc 3
relations: []
open_questions: 2
---

# Amulet of the Undertaker

## Tóm lược

Thành phần rẻ nhất và yếu nhất của [[cloak-of-the-undead-king]] **trong Heroes III** — nhưng là món
**mở đầu** cho toàn bộ vụ lừa [[gem]], và là món duy nhất trong ba thành phần thuộc hạng
**Treasure**.

{T1* INFERENCE: h3wiki-amulet-of-the-undertaker + h3wiki-vampires-cowl + h3wiki-dead-mans-boots — đối chiếu ba thành phần: giá 2.000 < 4.000 < 6.000; Necromancy 5% < 10% < 15%; class Treasure < Minor < Major}

⚠️ Phạm vi **Heroes III** không phải chi tiết vụn: ở Heroes IV cùng artifact này là hạng **Minor**
với **+10% Necromancy** — xem mục *Cơ chế trong Heroes IV*.

Hạng thấp đó có một hệ quả gameplay bất ngờ: nó có thể rơi ra từ Treasure Chest.

---

## Xuất xứ

**Không nguồn nào kể ai tạo ra nó — và ở một chỗ, game chủ động từ chối nói.** Text khi nhặt gợi ý
nó từng thất lạc rất lâu:

> "A dirty amulet lies next to a freshly dug grave. Upon investigation, you discover it to be
> the enchanted Amulet of the Undertaker, **long thought lost by mortals**."

{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker}
{T1 EXPLICIT: h3wiki-artraits-txt — xác nhận chuỗi mô tả từ file game}

Claim phủ định này đứng vững sau khi quét **193 trang** trỏ tới artifact trên thelazy, bảng string
table trích từ file game, và trang phỏng vấn nhóm HotA (`Team Interview 2024`, 51 KB — **không có**
phát ngôn nào về artifact này).

{T1* INFERENCE: h3wiki-amulet-of-the-undertaker — suy ra từ sự vắng mặt sau khi quét toàn bộ backlinks, không phải từ việc không tìm thấy ở một trang}

⭐ Chứng cứ dương mạnh hơn sự vắng mặt: trong `Beyond the Horizon`, vị priest bắt đầu kể về nguồn gốc
rồi **tự cắt lời mình** — "Their creator was... Bah, that doesn't matter." Xem mục *Xuất hiện trong
game*.

### Vai trò trong vụ lừa Gem

Đây là món **đầu tiên** Sandro sai Gem đi lấy, và là món thiết lập toàn bộ vỏ bọc:

> "You have agreed to help a wizard's apprentice named Sandro. Sandro's master, Ethric, needs
> an Amulet of the Undertaker to perform **anti-necromancy research**, but Ethric is an
> academician and Sandro is too inexperienced to go after the Amulet himself."

{T1* EXPLICIT: sod-after-the-amulet}

Chi tiết đầy đủ về vụ lừa: xem [[cloak-of-the-undead-king]].

### Nơi tìm thấy

Trong `After the Amulet`, Amulet nằm tại toạ độ **(39, 8, 0)**:

> "**Buried under the gems and gold of the Ghost Dragons' hoard** you find the Amulet of the
> Undertaker."

{T1* EXPLICIT: sod-after-the-amulet}

Có một stack **Ghost Dragon** tại (38, 8, 0) — ô **liền kề** chỗ đặt Amulet:

> "Despite the pleasant surroundings, the unmistakable odor of death permeates the area. You see a
> group of Ghost Dragons ahead."

{T1* EXPLICIT: sod-after-the-amulet}

⚠️ **Số lượng stack đó không nêu được, và đó là giới hạn của nguồn chứ không phải của game.** Bảng
`==== Monsters ====` chỉ có ba cột `Location / Type / Message`, ô Type dùng `Template:Cram2` —
template này **không có tham số số lượng nào**, nó chỉ vẽ icon creature. Text cũng chỉ nói "a
**group** of Ghost Dragons".

{T1* EXPLICIT: sod-after-the-amulet}

⚠️ **Không kết luận được ô chứa Amulet "có" hay "không có" lính canh.** Bảng `==== Artifacts ====`
của thelazy cũng chỉ có ba cột và **không có trường guardian nào** — đã đối chiếu ba scenario khác
nhau, format y hệt. Nghĩa là bảng này **im lặng về lính canh dù có hay không**, nên không suy ra
được gì từ sự im lặng đó.

Bản đầu của bài này ghi "ô chứa Amulet **không có lính canh nào**" và gán `EXPLICIT`. Đó là
`EXPLICIT` không nguồn: cùng một lối suy luận sẽ cho ra kết luận "không lính canh" cho **mọi**
artifact trên **mọi** trang scenario của thelazy.

Điều nói được, ở mức suy luận có ghi bước:

{T1* INFERENCE: sod-after-the-amulet — stack Ghost Dragon nằm ở ô liền kề (38, 8, 0) và Amulet ở (39, 8, 0); vai trò canh giữ suy ra từ vị trí, không phải từ câu nào trong nguồn}

Riêng biệt, có một **event phục kích** tại (32, 5, 0) với 20 Bone Dragon + 20 Ghost Dragon +
20 Bone Dragon. **Stack 60 con đó không phải lính canh artifact** — gộp hai thứ là lỗi thường gặp.
{T1* EXPLICIT: sod-after-the-amulet}

---

## Gameplay

### Cơ chế trong Heroes III

| Thuộc tính | Giá trị |
|---|---|
| Slot | Necklace |
| Class | **Treasure** |
| Giá | 2.000 |
| Hiệu ứng | **+5% Necromancy** |

{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker}

**Mô tả in-game:** "Worn about the neck, this amulet increases your Necromancy skill by 5%."
{T1 EXPLICIT: h3wiki-artraits-txt}

⭐ Nguồn câu này là `T1` **thật, không dấu sao** — `H3Bitmap.lod > artraits.txt`, string table trích
trực tiếp từ file game. Bản đầu của bài dẫn Fandom (`T6`, không dẫn nguồn) cho cùng câu; Fandom chỉ
chép lại chính chuỗi đó, **y hệt từng chữ**.

Là thành phần của [[cloak-of-the-undead-king]], cùng với [[vampires-cowl]] và
[[dead-mans-boots]].

⚠️ **Điều khoản "vô tác dụng nếu hero không có Necromancy"** lưu hành trên wiki **là văn wiki,
không phải game text** — xem [[cloak-of-the-undead-king]] mục *Điểm tranh chấp*.

### Hạng Treasure — hệ quả bất ngờ

Vì là hạng **Treasure** (hạng thấp nhất), Amulet có thể xuất hiện từ Treasure Chest. Cộng đồng
ghi nhận điều này có thể rút ngắn scenario:

> "If you are lucky enough, you can win this scenario by opening Treasure Chests. That's because
> Amulet of the Undertaker is a treasure."

{T6 FAN_THEORY: sod-after-the-amulet — nằm trong `{{user commentary}}`, là ý kiến người chơi}

### Cơ chế trong Heroes IV — cùng tên, khác thông số

⚠️ **Artifact này cũng tồn tại trong Heroes IV, với thông số khác.** Mọi câu so sánh nhất ở trên chỉ
đúng trong phạm vi Heroes III.

| Thuộc tính | Heroes III | **Heroes IV** |
|---|---|---|
| Class | Treasure | **Minor** |
| Slot | Necklace | **Neck** |
| Hiệu ứng | +5% Necromancy | **+10% Necromancy** |
| Khi hero không có skill Necromancy | Vô tác dụng *(văn wiki, không phải game text)* | **Hoạt động như Basic Necromancy** |

Mô tả ở Heroes IV: "Increases the hero's Necromancy skill by 10% if the hero has the skill.
Otherwise, it acts as the Basic Necromancy skill."

{T6 EXPLICIT: fandom-h4-artifact-list — Fandom **không dẫn nguồn**}

Nó cũng có vai trò quest thật ở H4, không chỉ là một dòng dữ liệu. Trong `Prelude to Invasion` —
scenario đầu của campaign *Death March* (*Winds of War*) — Amulet là một trong **năm** artifact đem
đổi:

> "In return for an Amulet of Fear, a Wand of Animating Dead, a Hideous Mask, an **Amulet of the
> Undertaker**, and a Wand of Curses, he will give Von Tarkin a Dwarven Hammer, Dwarven Shield, and
> Ring of Protection that carry over to the next map."

{T6 EXPLICIT: fandom-prelude-to-invasion — Fandom **không dẫn nguồn**}

⚠️ **Cả mục này chỉ có nguồn `T6`.** thelazy gần như chỉ phủ Heroes III, nên phần H4 hiện không có
nguồn nào tốt hơn Fandom. Đây là **lỗ nguồn thật của dự án**, đã ghi thành `B-019` trong
`BACKLOG.md` — không phải chuyện của riêng bài này.

### Thay đổi qua các bản

⚠️ Con số +5% **không ổn định qua các bản HotA**:

| Phiên bản | Giá trị |
|---|---|
| SoD gốc | **+5%** |
| HotA 1.3.0 → 1.7.x | **+2,5%** |
| HotA 1.8.0 trở đi | **+5%** (khôi phục) |

{T1* EXPLICIT: hota-changelog}

⚠️ Dòng changelog 1.3.0 chỉ nói "reduced by half" — **không nêu tên artifact này và không nêu
con số**. Giá trị 2,5% chỉ được **chứng thực hồi cố** qua dòng 1.8.0.
{T1* INFERENCE: hota-changelog}

---

## Xuất hiện trong game

Ngoài `After the Amulet`, Amulet còn xuất hiện rải rác. ⚠️ **Bốn trong năm mục dưới đây là HotA** —
expansion do fan làm, không phải New World Computing:

| Scenario | Sản phẩm | Cách xuất hiện |
|---|---|---|
| `Taming of the Wild` | **AB** | Nhặt tự do, (68, 4, 0). Text riêng: "A strange man dressed in black throws an amulet to you, bows and then vanishes." {T1* EXPLICIT: ab-taming-of-the-wild} |
| `Beyond the Horizon` | **HotA** | Một trong **bốn** artifact Seer's Hut (2, 27, 0) đòi → Golden Bow {T1* EXPLICIT: hota-beyond-the-horizon} |
| `Tomb Raiders` | **HotA** | Seer's Hut **lặp lại** (16, 172, 0) → +1 primary skill tự chọn; và Quest Guard (12, 178, 0) đòi nó để sửa **Skeleton Transformer** {T1* EXPLICIT: hota-tomb-raiders} |
| `Frontier` | **HotA** | Seer's Hut (70, 18, 0) → Ring of Vitality {T1* EXPLICIT: hota-frontier} |
| `Apocalypse` (template) | **HotA** | Nằm trong danh sách `Allowed artifacts` — xem cảnh báo dưới {T6 INFERENCE: hota-apocalypse-template} |
| `Nine-day Wonder` (template) | **HotA** | ⛔ **BỊ CẤM** — nằm trong `Banned artifacts` {T6 EXPLICIT: hota-nine-day-wonder} |

⛔ **Hai template HotA đi NGƯỢC chiều nhau.** Trên `Apocalypse` Amulet được cho phép; trên
`Nine-day Wonder` nó **bị cấm**. Đừng suy từ một template sang template khác.

⚠️ **"Một trong ba artifact *duy nhất*" là cách đọc sai.** Trang `Apocalypse` ghi `Allowed
artifacts:` rồi liệt kê ba — đúng là ba thành phần Cloak — nhưng **không có chữ "only"**. Bằng
chứng ngược: bản HotA **1.7.1** cấm thêm *Wanderer's Boots* khỏi chính template này. Nếu template
chỉ cho phép ba artifact thì lệnh cấm đó **vô nghĩa**. Cách đọc dung hòa: "allowed" = được cho phép
**thêm**, ngoài các lệnh cấm mặc định.

{T1* EXPLICIT: hota-changelog — 1.5.0 và 1.7.1 là hai lần duy nhất changelog nhắc Apocalypse; không lần nào là danh sách artifact}

📅 **Phạm vi phiên bản:** trang `Apocalypse` sửa lần cuối **2025-05-14** ≈ HotA 1.7.2–1.7.3, **trước
1.8.0**. Trang tự nó không ghi phiên bản nào.

⭐ **Text ở `Beyond the Horizon` cố ý bỏ lửng nguồn gốc artifact.** Vị priest kể về "cursed
artifacts" trong vùng rồi tự cắt lời mình:

> "We believe that these lands have been home to cursed artifacts since the last century. **Their
> creator was... Bah, that doesn't matter.**"

{T1* EXPLICIT: hota-beyond-the-horizon}

Đây là chứng cứ dương cho mục *Xuất xứ*: không phải Codex thiếu nguồn, mà **văn bản game chủ động
từ chối nói ra**.

---

## Câu hỏi mở

**Q1. Stack Ghost Dragon tại (38, 8, 0) có bao nhiêu con?**

Trang nguồn không ghi số lượng, và đó là **giới hạn cấu trúc của nguồn**: bảng `Monsters` chỉ có ba
cột, ô Type dùng `Template:Cram2` — template không có tham số số lượng. Chỉ giải được bằng cách mở
file map gốc (liên quan `B-001`).

*(Câu hỏi này cố ý **không** gọi stack đó là "lính canh Amulet" — quan hệ canh giữ chưa chứng minh
được, xem mục* Nơi tìm thấy*.)*

**~~Q2. Mô tả in-game chính xác?~~ — ✅ ĐÃ GIẢI QUYẾT (2026-08-03)**

Tìm được nguồn `T1` thật: `Talk:Artifact/descriptions` trên thelazy, tự ghi đầu bảng `Information
from H3Bitmap.lod > artraits.txt`. Xem mục *Cơ chế trong Heroes III*.

**Q3. Thông số Heroes IV có nguồn nào tốt hơn Fandom không?**

Toàn bộ mục *Cơ chế trong Heroes IV* hiện chỉ dựa vào Fandom (`T6`, không dẫn nguồn). thelazy gần
như chỉ phủ Heroes III. Đây là lỗ nguồn cấp dự án — xem `B-019`.

---

## Liên kết

**Bộ hoàn chỉnh:** [[cloak-of-the-undead-king]]

**Thành phần cùng bộ:** [[vampires-cowl]] · [[dead-mans-boots]]

**Nhân vật:** [[gem]] · [[sandro]] · [[ethric]]

**Campaign:** [[sod-new-beginning]]
