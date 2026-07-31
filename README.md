# Heroes Saga & Heroes Codex

Bộ tài liệu tiếng Việt về **Heroes of Might and Magic – Old Universe**
(Heroes I–IV, Heroes Chronicles, Might and Magic I–VIII).

Hai sản phẩm, một nền dữ liệu:

- **Heroes Codex** — bách khoa toàn thư để tra cứu. Đây là **nền tảng**.
- **Heroes Saga** — sử thi tiểu thuyết hóa, đọc từ đầu đến cuối. Xây **dựa trên** Codex.

> Codex là *sự thật của thế giới*. Saga là *câu chuyện được kể từ sự thật đó*.

---

## Đọc gì trước

Nếu bạn (hoặc một AI agent) sắp đóng góp vào dự án, đọc theo thứ tự:

| # | File | Nội dung |
|---|------|----------|
| 1 | [CANON-POLICY.md](00-foundation/CANON-POLICY.md) | Cách xác định điều gì là thật. Hệ thống nhãn hai trục. Thứ tự ưu tiên nguồn |
| 2 | [SCHEMA.md](00-foundation/SCHEMA.md) | Cấu trúc 12 loại entity, frontmatter, bộ quan hệ |
| 3 | [VERIFY-PROTOCOL.md](00-foundation/VERIFY-PROTOCOL.md) | Luồng kiểm định độc lập. **Không bỏ qua** |
| 4 | [SAGA-STYLE.md](00-foundation/SAGA-STYLE.md) | Ranh giới canon vs sáng tạo khi viết truyện |

`CANON-POLICY.md` có quyền lực cao nhất. Bài viết nào xung đột với nó thì bài viết sai.

---

## Ba nguyên tắc không thương lượng

**1. Mọi thông tin có nhãn nguồn.**
Không claim nào được đứng trơ trọi. Mỗi khẳng định ghi rõ đến từ đâu (T1–T6) và
chắc chắn đến mức nào (EXPLICIT / INFERENCE / DISPUTED / FAN_THEORY).

**2. Trí nhớ không phải nguồn.**
"Theo tôi biết" không phải nguồn — kể cả với người, kể cả với AI. Không fetch được
nguồn thì claim đó là `UNVERIFIED`, không được vào thân bài.

**3. Người viết không tự kiểm bài của mình.**
Mọi bài qua luồng verify độc lập, do một agent riêng chạy, mặc định coi claim là
sai cho đến khi tìm được nguồn phản bác được.

---

## Cấu trúc thư mục

```
00-foundation/     Tài liệu nền — đọc trước khi làm gì
codex/             Bách khoa toàn thư, chia theo 12 loại entity
  heroes/          Nhân vật điều khiển được trong game
  characters/      Nhân vật lore, không chơi được
  artifacts/       Vật phẩm có tên riêng
  kingdoms/        Quốc gia
  locations/       Địa điểm
  creatures/       Sinh vật
  races/           Chủng tộc
  magic/           Phép thuật, trường phái, spell
  events/          Sự kiện lịch sử
  campaigns/       Campaign game (đơn vị tư liệu, không phải sự kiện)
  organizations/   Tổ chức, triều đại
  timeline/        Mốc & giai đoạn thời gian
saga/              Sử thi, chia theo Book
sources/
  REGISTRY.md      Sổ nguồn — mọi source key phải có ở đây
  raw/             Tư liệu thô đã fetch
  notes/           Báo cáo verify
tools/             Công cụ kiểm toàn vẹn & sinh quan hệ nghịch đảo
```

---

## Quy ước ngôn ngữ

Viết **tiếng Việt**, **giữ nguyên tên riêng tiếng Anh**.

- ✅ "Sandro nắm giữ Cloak of the Undead King"
- ❌ "Sandro nắm giữ Áo Choàng Vua Bất Tử"

Lý do: người chơi lâu năm tra cứu bằng tên gốc. Dịch tên riêng làm Codex mất đúng
chức năng nó tồn tại để làm.

---

## Bảy Book của Saga

| Book | Nội dung |
|------|----------|
| I | The Ancients |
| II | Age of Kings |
| III | Rise of Erathia |
| IV | Heroes III |
| V | Heroes Chronicles |
| VI | The Reckoning |
| VII | Axeoth |

Saga chỉ được viết sau khi entity Codex liên quan đạt `status: verified`.

---

## Trạng thái hiện tại

**Giai đoạn 1 — Xây nền.**

- [x] Bốn tài liệu nền
- [ ] `sources/REGISTRY.md`
- [ ] Entity mẫu (Sandro) — thử lửa cho schema
- [ ] `TIMELINE-SPINE.md`
- [ ] Công cụ kiểm toàn vẹn

Chưa bắt đầu viết Codex hàng loạt. Chưa bắt đầu Saga.
