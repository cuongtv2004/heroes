# SAGA STYLE

Quy tắc viết Heroes Saga — bộ sử thi tiểu thuyết hóa.

---

## 1. Mâu thuẫn phải giải quyết trước

Đề bài của dự án chứa một căng thẳng nội tại cần nói thẳng:

- Muốn **kể như phim HBO**: có hội thoại, có nội tâm, có cliffhanger, có nhịp.
- Muốn **không thay đổi canon**.

Hai điều này không tương thích 100%. Game không cho ta từng câu thoại của Tarnum.
Không có đoạn nào miêu tả Catherine nghĩ gì trên thuyền về Erathia. Nếu viết
tiểu thuyết mà chỉ dùng đúng những gì game nói, kết quả là bản tóm tắt campaign —
đúng thứ dự án tuyên bố không làm.

Vậy nên "không thay đổi canon" phải được định nghĩa **chính xác hơn**, thay vì để
là một ước muốn.

---

## 2. Ranh giới: bất khả xâm phạm vs được phép

### Bất khả xâm phạm (Saga KHÔNG được đổi)

| Loại | Ví dụ |
|------|-------|
| Sự kiện đã xảy ra | Steadwick thất thủ |
| Kết quả | Ai thắng, ai chết, ai sống |
| Ai tham gia | Người có mặt, người không có mặt |
| Động cơ đã nêu | Nếu game nói Sandro muốn quyền lực, Saga không được đổi thành lòng trung thành |
| Quan hệ đã xác lập | Ai là học trò ai, ai phản ai |
| Thứ tự thời gian | Không đảo trình tự sự kiện |
| Đặc tính vật phẩm | Vật phẩm làm được gì và không làm được gì |
| Địa lý | Ai giáp ai, đi từ đâu tới đâu |

### Được phép sáng tạo

| Loại | Ràng buộc |
|------|-----------|
| Thoại cụ thể | Nội dung phải suy ra được từ động cơ đã canon xác lập |
| Nội tâm | Không được tạo động cơ mới trái với canon |
| Chi tiết cảm giác | Thời tiết, mùi, ánh sáng, âm thanh — miễn không thành dữ kiện lịch sử |
| Nhân vật phụ vô danh | Một người lính giữ cổng có thể có tên — nhưng không được thành nhân vật lịch sử |
| Nhịp kể & cấu trúc | Bắt đầu ở đâu, kết chương ở đâu, kể từ góc nhìn ai |
| Cảnh chuyển tiếp | Những khoảng trống canon không nói tới |

### Vùng xám — phải ghi vào registry

Có loại chi tiết **buộc phải sáng tạo** nhưng lại **dễ bị nhầm là canon**:

- Một cuộc gặp giữa hai nhân vật mà canon chỉ hàm ý chứ không nói có
- Nguyên nhân cụ thể của một việc canon chỉ nêu kết quả
- Khoảng cách thời gian giữa hai sự kiện
- Số lượng quân, quy mô thiệt hại

Những chi tiết này được phép dùng, **nhưng bắt buộc ghi vào**
`saga/INVENTED-REGISTRY.md` với format:

```markdown
### INV-014
Chương: Book IV, Ch. 3
Chi tiết: Sandro và Vidomina gặp nhau ở Deyja trước khi lên đường
Vì sao cần: Cần thiết lập quan hệ trước khi có sự phản bội ở chương 7
Canon nói gì: Cả hai đều ở Deyja giai đoạn này {T1 EXPLICIT: <key>}, nhưng
không nguồn nào nói họ gặp nhau
Rủi ro nhầm lẫn: TRUNG BÌNH — người đọc có thể tưởng đây là canon
```

Đây là điều làm Saga khác fan-fiction: **fan-fiction không ghi lại nó đã bịa gì.**

---

## 3. Quy tắc tuyệt đối

**S1 — Không tạo ra dữ kiện lịch sử mới.**
Được viết một người lính nghĩ gì. Không được viết một trận đánh chưa từng có.

**S2 — Không giải quyết điều canon để mở.**
Nếu canon không nói Sandro chết hay sống, Saga **không được** chọn. Phải viết sao
cho vẫn mở. Đây là quy tắc khó nhất và quan trọng nhất.

**S3 — Không dùng thông tin từ Ashan (Ubisoft-era).**
Xem `CANON-POLICY.md` R5.

**S4 — Góc nhìn hạn chế là công cụ chính.**
Kể qua mắt một nhân vật cho phép sự thật bị bóp méo *một cách trung thực* — nhân
vật tin điều sai vẫn là canon, vì canon nói nhân vật đó tin thế. Đây là cách
xử lý các điểm `DISPUTED` mà không phải chọn bên.

**S5 — Mọi chương phải khai báo entity nó dựa vào.**
Frontmatter chương ghi rõ, để khi Codex sửa thì biết chương nào cần rà lại.

**S6 — Không được viết chương trước khi entity Codex liên quan đạt `verified`.**
Đây là hệ quả trực tiếp của kiến trúc Codex-làm-nền. Vi phạm quy tắc này là quay
về đúng cái vấn đề dự án muốn tránh.

---

## 4. Frontmatter cho chương Saga

```yaml
---
book: 4
chapter: 3
title_vi: "Cái giá của lời thề"
pov: sandro                     # góc nhìn
timeline_span: "1173 – 1174"
timeline_certainty: DISPUTED
based_on:                       # entity Codex — nền của chương
  - sandro
  - vidomina
  - deyja
  - cloak-of-the-undead-king
depicts_events:
  - event-rise-of-the-necromancer
invented_details:               # trỏ tới INVENTED-REGISTRY
  - INV-014
  - INV-015
verify_pass: null
---
```

---

## 5. Giọng văn

Tiếng Việt. Giữ nguyên tên riêng tiếng Anh (xem `SCHEMA.md` mục 2).

**Hướng tới:**
- Câu có nhịp. Dài ngắn xen kẽ.
- Miêu tả cụ thể, không hoa mỹ chung chung.
- Nhân vật bộc lộ qua hành động và lời nói, không qua lời tác giả giải thích.
- Nghiêm trọng nhưng không nặng nề. Có chỗ thở.

**Tránh:**
- Văn phong wiki lọt vào truyện ("Sandro, một necromancer đến từ Deyja, đã...").
- Giải thích lore giữa cảnh. Nếu người đọc cần biết bối cảnh, dựng cảnh cho họ
  thấy, đừng dừng lại thuyết trình.
- Nhân vật nói ra động cơ của mình thành lời.
- Chú thích nhãn canon trong thân truyện. Saga không mang nhãn — Saga trỏ về Codex.

**Về từ Hán-Việt:** dùng khi đúng chỗ và tăng độ trang trọng, nhưng không lạm dụng
tới mức khó đọc. Người đọc mục tiêu bao gồm người chưa từng chơi Heroes.

---

## 6. Xử lý điểm tranh chấp canon trong truyện

Khi Codex ghi một điểm là `DISPUTED`, Saga có ba cách xử lý — **không** có cách
thứ tư là "chọn một bên và viết như thật":

**Cách 1 — Góc nhìn hạn chế.** Kể qua mắt nhân vật chỉ biết một phiên bản.

**Cách 2 — Mơ hồ chủ động.** Viết cảnh sao cho cả hai phiên bản đều còn khả năng.

**Cách 3 — Nhắc tới sự bất đồng.** Nếu người kể là sử gia trong thế giới, có thể
nói thẳng rằng các ghi chép khác nhau. Cách này mạnh nhưng dùng nhiều thì mất nhịp
truyện.

---

## 7. Quan hệ với Codex

```
Codex (sự thật của thế giới)
   │
   │  entity đạt verified
   ▼
Saga (câu chuyện kể từ sự thật đó)
   │
   │  phát hiện chi tiết cần sáng tạo
   ▼
INVENTED-REGISTRY (ghi lại đã bịa gì)
```

Khi một entity Codex được sửa, mọi chương có entity đó trong `based_on` phải được
rà lại. Công cụ ở `tools/` sinh danh sách này.

---

## 8. Lịch sử sửa đổi

| Ngày | Thay đổi | Lý do |
|------|----------|-------|
| 2026-07-31 | Bản đầu | Giải quyết mâu thuẫn "kể như HBO" vs "không đổi canon" |
