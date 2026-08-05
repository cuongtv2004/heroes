# Heroes Codex

Bách khoa toàn thư tra cứu về Old Universe. Mở đâu đọc đó.

Mỗi bài tuân theo [SCHEMA.md](../00-foundation/SCHEMA.md) và phải qua
[luồng kiểm định độc lập](../00-foundation/VERIFY-PROTOCOL.md) trước khi đạt
`verified`.

---

## Đang có

### Hero

Nhân vật điều khiển được trong game.

- [**Sandro**](heroes/sandro.md) — necromancer nổi tiếng nhất Old Universe. Protagonist chơi
  được của hai campaign trọn vẹn, và là kẻ thao túng bị thao túng.
- [**Jeddite**](heroes/jeddite.md) — người đã giới thiệu Sandro với Ethric, và không tha thứ
  cho mình được. Bio chính thức của hắn **không nhắc một chữ nào** về điều đó.
- [**Tarnum**](heroes/tarnum.md) — *The Immortal Hero*, nhân vật chính của **cả tám** campaign
  Heroes Chronicles và mang **sáu class**. Bị Ancestors từ chối cho vào Paradise — và chính lòng
  nhân từ của hắn dẫn tới The Reckoning.
- [**Gauldoth Half-Dead**](heroes/gauldoth-half-dead.md) — necromancer nửa sống nửa chết, vua của
  Nekross trên Axeoth. Nhân vật duy nhất trong Codex mà **chính tác giả gọi là "hero"**, và bài đầu
  tiên của kỷ nguyên *Axeoth*.
- [**Archibald Ironfist**](heroes/archibald-ironfist.md) — vua tiếm ngôi của Enroth, bị hóa đá
  khoảng mười năm, rồi lên ngôi một vương quốc **thứ hai**. Bài đầu tiên của kỷ nguyên
  *Age of Kings*, và là bài duy nhất có nguồn **Archibald tự kể ở ngôi thứ nhất**.

- [**Gem**](heroes/gem.md) — nữ Sorceress trở thành Druid, và là người [[sandro]] lừa. Gốc gác của
  nàng — **cả làng bị skeleton giết, nàng là người sống sót duy nhất** — nằm trong một timed event
  ngày 1, không có ở bio hay prologue.

### Nhân vật

Nhân vật có vai trò lore nhưng không chơi được.

- [**Ethric**](characters/ethric.md) — "Ethric the Mad", lich đầu tiên của thế giới, thầy của
  Sandro. Và là nhân vật **không nói một câu nào** trong toàn bộ Heroes III.

### Sự kiện

Thứ đã xảy ra trong thế giới — định vị được trên timeline.

- [**Vụ đầu độc Nicolas Gryphonheart**](events/vu-dau-doc-nicolas-gryphonheart.md) — vụ ám sát mở
  màn Restoration Wars. Gỡ được một mục `DISPUTED` của dự án bằng cách phát hiện nó là **lỗi tier**,
  và truy ra mốc `27/9` lưu hành khắp nơi thực chất là **dateline xuất bản năm 1998**.
- [**The Reckoning**](events/the-reckoning.md) — thảm họa làm hành tinh Enroth không còn ở được,
  đường biên giữa Heroes III và Heroes IV. Bài `event` **đầu tiên** của Codex, và là bài mà **cấu
  trúc bằng chứng quan trọng hơn nội dung**: tường thuật mà mọi wiki kể lại hóa ra nằm trong một
  tài liệu **chưa bao giờ vào game**.

### Quốc gia

- [**Deyja**](kingdoms/deyja.md) — vương quốc necromancer, nơi **ám sát là thủ tục kế vị**.
  Sự cằn cỗi của nó không phải điều kiện có sẵn mà là **thứ nó tự tạo ra**.

### Vật phẩm

- [**Cloak of the Undead King**](artifacts/cloak-of-the-undead-king.md) — combination artifact
  mạnh nhất phe Necropolis, bị cấm ghép trong HotA. Artifact mà Sandro lừa một người tử tế đi
  thu thập hộ.
    - Thành phần: [Amulet of the Undertaker](artifacts/amulet-of-the-undertaker.md) ·
      [Vampire's Cowl](artifacts/vampires-cowl.md) ·
      [Dead Man's Boots](artifacts/dead-mans-boots.md)
- [**Armor of the Damned**](artifacts/armor-of-the-damned.md) — artifact đối xứng, và là món
  Sandro lừa Crag Hack bằng cách hứa sẽ **phá hủy** nó.

---

## Cách đọc một bài Codex

**Nhãn hai trục.** Mỗi khẳng định trong thân bài mang nhãn dạng
`{T1* EXPLICIT: source-key}`:

| Trục | Ý nghĩa |
|---|---|
| **Cấp nguồn** | `T1` in-game text · `T2` manual · `T3` game data · `T4` developer · `T5` ngoài Old Universe · `T6` wiki cộng đồng |
| **Độ chắc** | `EXPLICIT` nói thẳng · `INFERENCE` suy ra · `DISPUTED` nguồn mâu thuẫn · `FAN_THEORY` giả thuyết · `UNVERIFIED` chưa kiểm được |

**Dấu hoa thị (`T1*`)** nghĩa là tiếp cận **qua trung gian** — bản chép fan wiki, không
phải file game gốc. Xem [CANON-POLICY.md](../00-foundation/CANON-POLICY.md) mục 2.

**Bố cục chuẩn.** Mọi bài đều có các mục này, và chúng có ý nghĩa cố định:

- **Điểm tranh chấp canon** — nơi các nguồn nói khác nhau. Dự án trình bày cả hai
  phía, **không chọn ngầm**.
- **Giả thuyết cộng đồng** — claim không có nguồn T1–T4. Tách riêng để không lẫn vào
  phần tiểu sử.
- **Câu hỏi mở** — điều dự án **chưa** trả lời được. Ghi ra để không tự lừa mình.

---

## Mười hai loại entity

Loại đã dùng được đánh dấu ✅.

| Loại | Là gì | Trạng thái |
|---|---|---|
| `hero` | Nhân vật điều khiển được | ✅ |
| `character` | Nhân vật lore, không chơi được | ✅ |
| `artifact` | Vật phẩm có tên riêng | ✅ |
| `kingdom` | Thực thể chính trị | ✅ |
| `location` | Địa điểm không phải quốc gia | — |
| `creature` | Loại sinh vật dùng làm quân | — |
| `race` | Chủng tộc có văn hóa riêng | — |
| `magic` | Trường phái phép, spell | — |
| `event` | Sự kiện lịch sử | ✅ |
| `campaign` | Campaign game (đơn vị tư liệu) | — |
| `organization` | Tổ chức, triều đại | — |
| `timeline` | Mốc hoặc giai đoạn thời gian | — |

Phân biệt quan trọng: `event` là **thứ đã xảy ra trong thế giới**; `campaign` là
**nguồn tư liệu kể về nó**. Không được lẫn — nếu lẫn thì timeline sẽ bị cấu trúc theo
game thay vì theo thế giới.
