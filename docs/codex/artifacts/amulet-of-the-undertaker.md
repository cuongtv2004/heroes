---
id: amulet-of-the-undertaker
type: artifact
name_vi: Amulet of the Undertaker
name_en: Amulet of the Undertaker
aliases: []
appears_in:
  - sod-new-beginning
status: draft
verify_pass: null
slot: necklace
artifact_class: treasure
component_of_artifact: cloak-of-the-undead-king
cost: 2000
sources_used:
  - h3wiki-amulet-of-the-undertaker
  - h3wiki-cloak-undead-king
  - fandom-artifact-list
  - hota-changelog
  - sod-after-the-amulet
# component_of khai o cloak-of-the-undead-king (assembled_from);
# nghich dao do cong cu sinh - xem SCHEMA.md muc 3
relations: []
open_questions: 2
---

# Amulet of the Undertaker

## Tóm lược

Thành phần rẻ nhất và yếu nhất của [[cloak-of-the-undead-king]] — nhưng là món **mở đầu** cho
toàn bộ vụ lừa [[gem]], và là món duy nhất trong ba thành phần thuộc hạng **Treasure**.

Hạng thấp đó có một hệ quả gameplay bất ngờ: nó có thể rơi ra từ Treasure Chest.

---

## Xuất xứ

Không nguồn nào kể ai tạo ra nó. Text khi nhặt gợi ý nó từng thất lạc rất lâu:

> "A dirty amulet lies next to a freshly dug grave. Upon investigation, you discover it to be
> the enchanted Amulet of the Undertaker, **long thought lost by mortals**."

{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker}

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

⚠️ **Một điểm dễ nhầm:** ô chứa Amulet **không có lính canh nào**. Việc canh giữ do một stack
Ghost Dragon **liền kề** tại (38, 8, 0) đảm nhiệm — và **số lượng không được nêu**.

Riêng biệt, có một **event phục kích** tại (32, 5, 0) với 20 Bone Dragon + 20 Ghost Dragon +
20 Bone Dragon. **Stack 60 con đó không phải lính canh artifact** — gộp hai thứ là lỗi thường gặp.
{T1* EXPLICIT: sod-after-the-amulet}

---

## Gameplay

### Cơ chế gốc

| Thuộc tính | Giá trị |
|---|---|
| Slot | Necklace |
| Class | **Treasure** |
| Giá | 2.000 |
| Hiệu ứng | **+5% Necromancy** |

{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker}

**Mô tả in-game:** "Worn about the neck, this amulet increases your Necromancy skill by 5%."
{T6 EXPLICIT: fandom-artifact-list — Fandom **không dẫn nguồn**}

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

Ngoài `After the Amulet`, Amulet còn xuất hiện rải rác:

| Scenario | Cách xuất hiện |
|---|---|
| `Taming of the Wild` | Nhặt tự do. Text riêng: "**A strange man dressed in black throws an amulet to you, bows and then vanishes.**" |
| `Beyond the Horizon` | Một trong bốn artifact Seer's Hut đòi → Golden Bow |
| `Tomb Raiders` (HotA) | Seer's Hut lặp lại → +1 primary skill; Quest Guard cần nó để sửa Skeleton Transformer |
| `Frontier` | Seer's Hut → Ring of Vitality |
| `Apocalypse` (HotA template) | Một trong ba artifact **duy nhất** được cho phép |

{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker}

---

## Câu hỏi mở

**Q1. Số lượng Ghost Dragon canh Amulet trong `After the Amulet`?**
Trang wiki **không nêu**. {T1* UNVERIFIED: sod-after-the-amulet — **không nêu số lượng**}

**Q2. Mô tả in-game chính xác?**
Hiện chỉ có từ bảng Fandom, **không dẫn nguồn**. thelazy không có trường mô tả riêng cho
artifact — chỉ có text khi nhặt.

---

## Liên kết

**Bộ hoàn chỉnh:** [[cloak-of-the-undead-king]]

**Thành phần cùng bộ:** [[vampires-cowl]] · [[dead-mans-boots]]

**Nhân vật:** [[gem]] · [[sandro]] · [[ethric]]

**Campaign:** [[sod-new-beginning]]
