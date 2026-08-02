# SCHEMA

Quy định cấu trúc dữ liệu cho toàn bộ Heroes Codex.

Nguyên tắc thiết kế: **mỗi entity là một file Markdown có YAML frontmatter.**
Frontmatter chứa dữ liệu máy đọc được (quan hệ, mốc thời gian, nhãn). Thân bài
chứa văn xuôi tiếng Việt cho người đọc.

Lý do chọn cách này thay vì database: Atlas, timeline tương tác, gia phả và
infographic ở Giai đoạn 4 chỉ là chuyện **render** từ frontmatter, không phải
chuyện migrate dữ liệu. Đồng thời file Markdown vẫn đọc được bằng mắt thường và
diff được bằng git — quan trọng với một dự án kéo dài nhiều năm.

---

## 1. Mười hai loại entity

| Loại | Thư mục | Là gì | Ví dụ |
|------|---------|-------|-------|
| `hero` | `codex/heroes/` | Nhân vật xuất hiện dưới dạng hero điều khiển được trong game | Sandro, Gelu, Catherine |
| `character` | `codex/characters/` | Nhân vật có vai trò trong lore nhưng **không** là hero chơi được | Nicolas Gryphonheart (đã chết trước H3) |
| `artifact` | `codex/artifacts/` | Vật phẩm có tên riêng | Armageddon's Blade, Cloak of the Undead King |
| `kingdom` | `codex/kingdoms/` | Thực thể chính trị có chủ quyền | Erathia, Deyja, Nighon |
| `location` | `codex/locations/` | Địa điểm không phải quốc gia | Steadwick, Hall of Valhalla |
| `creature` | `codex/creatures/` | Loại sinh vật dùng làm quân | Black Dragon, Archangel |
| `race` | `codex/races/` | Chủng tộc có văn hóa riêng | Elf, Dwarf, Vampire |
| `magic` | `codex/magic/` | Trường phái phép, spell, hoặc hệ thống phép thuật | Necromancy, Armageddon |
| `event` | `codex/events/` | Sự kiện lịch sử có thể định vị trên timeline | Cuộc xâm lược Erathia (1164) |
| `campaign` | `codex/campaigns/` | Campaign của game — đơn vị tư liệu, không phải sự kiện lore | *Shadow of Death* |
| `organization` | `codex/organizations/` | Tổ chức, hội, giáo phái, triều đại | Necromancer Council, Nhà Ironfist |
| `timeline` | `codex/timeline/` | Mốc hoặc giai đoạn thời gian | Silence, Age of Kings |

**Phân biệt `hero` vs `character`:** tiêu chí là *có điều khiển được trong game
nào không*, không phải mức độ quan trọng. Nicolas Gryphonheart cực kỳ quan trọng
với lore Heroes III nhưng không phải hero chơi được → `character`.

**Phân biệt `event` vs `campaign`:** `campaign` là **nguồn tư liệu** (một sản
phẩm), `event` là **thứ đã xảy ra trong thế giới**. Một campaign kể nhiều event.
Không được lẫn — nếu lẫn, timeline sẽ bị cấu trúc theo game thay vì theo thế giới,
đúng cái điều dự án muốn tránh.

---

## 2. Frontmatter chung cho mọi entity

```yaml
---
id: sandro                      # slug, unique toàn dự án, không đổi sau khi tạo
type: hero                      # một trong 12 loại
name_vi: Sandro                 # tên dùng trong văn bản tiếng Việt
name_en: Sandro                 # tên gốc tiếng Anh — dùng để tra cứu chéo
aliases:                        # tên khác, dùng cho search
  - Sandro the Necromancer
appears_in:                     # game/campaign nào — dùng source key
  - h3-shadow-of-death
  - h3-restoration-of-erathia
status: draft                   # draft | verified | needs-rework
verify_pass: null               # ngày qua luồng kiểm định, hoặc null
sources_used:                   # mọi source key bài này dùng
  - sod-rise-of-the-necromancer
relations: []                   # xem mục 3
open_questions: 0               # số câu hỏi mở còn tồn
---
```

### Trường bắt buộc với mọi entity

`id`, `type`, `name_vi`, `name_en`, `status`, `sources_used`.

### Quy tắc đặt tên (quan trọng — quyết định ngôn ngữ)

Dự án viết **tiếng Việt**, nhưng **giữ nguyên tên riêng tiếng Anh**:

- ✅ "Sandro nắm giữ Cloak of the Undead King"
- ❌ "Sandro nắm giữ Áo Choàng Vua Bất Tử"

Lý do: người chơi lâu năm tra cứu bằng tên gốc. Dịch tên riêng làm Codex mất chức
năng tra cứu — đúng thứ nó tồn tại để làm.

Ngoại lệ được dịch: danh từ chung và chức danh khi dùng trong câu văn
("necromancer" → "pháp sư tử linh" khi là danh từ chung; nhưng "Necromancer" giữ
nguyên khi là tên class trong game).

Lần đầu một thuật ngữ xuất hiện trong bài, ghi kèm giải nghĩa trong ngoặc.

---

## 3. Quan hệ (Relations)

Quan hệ là thứ biến Codex từ tập hợp bài viết thành **knowledge graph**.

### Cú pháp

```yaml
relations:
  - type: student_of
    target: ethric
    certainty: EXPLICIT
    source: sod-birth-of-a-barbarian
    note: ""
  - type: belongs_to
    target: deyja
    certainty: INFERENCE
    source: h3-manual-deyja
    note: "Suy ra từ chức vị, game không nói thẳng"
```

**Mỗi quan hệ bắt buộc có `certainty` và `source`.** Một quan hệ không có nguồn
là một quan hệ không tồn tại.

### Bộ quan hệ được phép

Danh sách này là **đóng**. Muốn thêm loại quan hệ mới phải sửa file này trước.
Lý do: nếu ai cũng tự đặt tên quan hệ, graph sẽ không query được.

**Quan hệ thuộc về:**

| type | Từ → Đến | Nghịch đảo |
|------|----------|-----------|
| `belongs_to` | hero/character → kingdom/organization | `has_member` |
| `rules` | hero/character → kingdom | `ruled_by` |
| `located_in` | location → kingdom/location | `contains` |
| `member_of_race` | hero/character → race | `has_member` |

**Quan hệ nhân vật:**

| type | Từ → Đến | Nghịch đảo |
|------|----------|-----------|
| `parent_of` | character → character | `child_of` |
| `sibling_of` | character → character | đối xứng |
| `spouse_of` | character → character | đối xứng |
| `student_of` | character → character | `teacher_of` |
| `ally_of` | character → character | đối xứng |
| `enemy_of` | character → character | đối xứng |
| `served` | character → character/organization | `was_served_by` |
| `betrayed` | character → character | `was_betrayed_by` |
| `killed` | character → character | `was_killed_by` |

**Quan hệ vật phẩm:**

| type | Từ → Đến | Nghịch đảo |
|------|----------|-----------|
| `owns` | character → artifact | `owned_by` |
| `created` | character → artifact | `created_by` |
| `component_of` | artifact → artifact | `assembled_from` |
| `wielded_in` | artifact → event | `featured_artifact` |

**Quan hệ sự kiện & tư liệu:**

| type | Từ → Đến | Nghịch đảo |
|------|----------|-----------|
| `participated_in` | character → event | `involves` |
| `caused` | event → event | `caused_by` |
| `occurred_at` | event → location | `site_of` |
| `appears_in` | bất kỳ → campaign | `features` |
| `depicted_in` | event → campaign | `depicts` |

**Quan hệ phép thuật:**

| type | Từ → Đến | Nghịch đảo |
|------|----------|-----------|
| `practices` | character → magic | `practiced_by` |
| `school_of` | magic → magic | `has_spell` |

### Nghịch đảo tự sinh

Không viết tay quan hệ nghịch đảo. Chỉ ghi một chiều, công cụ ở
`tools/` sẽ sinh chiều còn lại khi build. Viết tay hai chiều → sớm muộn lệch nhau.

---

## 4. Cấu trúc thân bài theo loại

### `hero` / `character`

```markdown
## Tóm lược
(3–5 câu. Ai, quan trọng vì sao. Không nhãn ở đây — đây là phần dẫn.)

## Tiểu sử
### Xuất thân
### (các giai đoạn theo thứ tự thời gian)

## Quan hệ
(Diễn giải bằng văn xuôi những gì frontmatter đã ghi. Vì sao quan hệ đó quan trọng.)

## Xuất hiện trong game
### <Tên game / campaign>
(Vai trò trong lore, không phải hướng dẫn chơi.)

## Gameplay
(Class, specialty, chỉ số khởi đầu. Tách riêng vì đây là thông tin cơ chế,
không phải lore.)

## Điểm tranh chấp canon
(Mọi claim DISPUTED. Trình bày các phương án, không chọn ngầm.)

## Giả thuyết cộng đồng
(FAN_THEORY. Bắt buộc tách khỏi phần trên.)

## Trivia & Dev Notes

## Câu hỏi mở
(Những gì dự án chưa trả lời được. Ghi ra để không tự lừa mình.)

## Nguồn
(Bảng source key → mô tả → độ tin cậy.)

## Liên kết
(Điều hướng sang entity liên quan.)
```

### `artifact`

```markdown
## Tóm lược
## Xuất xứ
### Ai tạo ra
### Được tạo như thế nào
## Lịch sử sở hữu
(Theo thứ tự thời gian. Mỗi lần đổi chủ là một mốc.)
## Ý nghĩa trong lore
## Gameplay
### Hiệu ứng
### Cân bằng game
## Xuất hiện trong game
## Điểm tranh chấp canon
## Giả thuyết cộng đồng
## Trivia & Dev Notes
## Câu hỏi mở
## Nguồn
## Liên kết
```

### `kingdom`

```markdown
## Tóm lược
## Địa lý
## Lịch sử
### (theo giai đoạn)
## Chính thể & các đời quân chủ
## Chiến tranh & liên minh
## Văn hóa & tôn giáo
## Xuất hiện trong game
## Điểm tranh chấp canon
## Câu hỏi mở
## Nguồn
## Liên kết
```

### `event`

```markdown
## Tóm lược
## Định vị thời gian
(Quan hệ tương đối là chính. Năm tuyệt đối kèm nhãn riêng.)
## Nguyên nhân
## Diễn biến
## Kết quả & ảnh hưởng
## Các bên tham gia
## Được kể trong
(Campaign nào kể sự kiện này, kể từ góc nhìn ai — quan trọng vì góc nhìn
ảnh hưởng độ tin cậy.)
## Điểm tranh chấp canon
## Câu hỏi mở
## Nguồn
## Liên kết
```

### Khác biệt `character` so với `hero`

Dùng cùng khung với `hero`, **bỏ** mục *Gameplay* (nhân vật không chơi được thì không
có class/specialty), và **thêm**:

```markdown
## Vì sao không phải hero chơi được
(Ngắn. Giải thích tiêu chí phân loại cho người đọc — vì nhiều `character` quan trọng
hơn phần lớn `hero`.)
```

Nếu nhân vật **có** xuất hiện dưới dạng hero ở một game nào đó nhưng không phải game
chính đang bàn, ghi ở mục *Xuất hiện trong game*, không tạo mục Gameplay riêng.

### Lưu ý riêng cho `artifact`

Mục *Gameplay* của artifact **phải tách hai phần**, vì hai loại thông tin này có tuổi
thọ khác nhau:

```markdown
## Gameplay
### Cơ chế gốc
(Bản Heroes III/SoD gốc. Đây là phần ổn định, không đổi.)

### Thay đổi qua các bản
(HotA, các bản mod lớn. Phần này **có ngày tháng** và sẽ lỗi thời — ghi rõ số phiên bản.)
```

Lý do tách: cơ chế gốc là canon vĩnh viễn; thay đổi của HotA là trạng thái tại một thời
điểm. Trộn chung thì hai năm sau không biết cái nào còn đúng.

Với artifact ghép (combination), **mỗi thành phần cần một bảng thông số riêng** — người
tra cứu thường tìm thành phần chứ không tìm bộ hoàn chỉnh.

Các loại còn lại (`creature`, `race`, `magic`, `location`, `campaign`,
`organization`, `timeline`) dùng khung tương tự, điều chỉnh theo nội dung. Bổ sung
khi viết bài đầu tiên của mỗi loại.

---

## 5. Trường riêng theo loại

### `hero`

```yaml
class: Necromancer              # class trong game
specialty: ""                   # specialty hero
faction: necropolis             # town type
first_appearance: h2            # game xuất hiện đầu
playable_in:
  - game: h3
    campaigns: [sod-rise-of-the-necromancer]
```

### `artifact`

```yaml
slot: cloak                     # vị trí trang bị
artifact_class: relic           # treasure | minor | major | relic | combo
combo_parts: []                 # nếu là combo artifact
```

### `event`

```yaml
date_absolute: 1164             # có thể null
date_certainty: DISPUTED        # nhãn riêng cho năm
date_source: h3-manual-timeline
before: [event-x]               # quan hệ tương đối — xương sống thật
after: [event-y]
concurrent_with: []
```

### `kingdom`

```yaml
capital: steadwick
existed_from: null
existed_until: null
successor_of: []
```

---

## 6. Kiểm tra tính toàn vẹn

Công cụ trong `tools/` phải kiểm được các điều kiện sau. Bài nào vi phạm thì
không được đặt `status: verified`:

1. Mọi `id` là unique toàn dự án.
2. Mọi `target` trong `relations` trỏ tới một `id` có thật.
3. Mọi `source` trong `relations` tồn tại trong `sources/REGISTRY.md`.
4. Mọi `sources_used` tồn tại trong registry.
5. Mọi claim trong thân bài có nhãn — không có câu khẳng định nào trơ trọi.
6. `UNVERIFIED` chỉ được xuất hiện ở **mục dành riêng**: *Câu hỏi mở*,
   *Giả thuyết cộng đồng*, *Điểm tranh chấp canon*, *Trivia & Dev Notes*.
   Trong các mục thân bài chính (*Tiểu sử*, *Quan hệ*, *Xuất hiện trong game*,
   *Gameplay*), `UNVERIFIED` chỉ được dùng khi **đang cảnh báo** rằng một claim lưu
   hành là không đáng tin — không bao giờ để **chống lưng** cho một khẳng định của bài.
7. `type` thuộc 12 loại đã định.
8. Mọi `relations[].type` thuộc bộ quan hệ đóng ở mục 3.

---

## 7. Lịch sử sửa đổi

| Ngày | Thay đổi | Lý do |
|------|----------|-------|
| 2026-07-31 | Bản đầu | Khởi tạo. Sẽ điều chỉnh sau khi viết entity mẫu Sandro — schema chưa qua thử lửa thì chưa đáng tin |
