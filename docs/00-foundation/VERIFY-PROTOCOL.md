# VERIFY PROTOCOL

Luồng kiểm định độc lập cho mọi nội dung Codex và Saga.

Tài liệu này tồn tại vì một lý do thẳng thắn: **không tin được người viết tự
kiểm bài của mình.** Điều này đúng với người, và đúng hơn nữa với AI — mô hình
ngôn ngữ có xu hướng tạo ra chi tiết nghe hợp lý mà không có nguồn, rồi khi được
hỏi lại thì tự xác nhận chính mình.

---

## 1. Nguyên tắc cốt lõi

> **Luồng verify không được đọc bài viết như một nguồn tin.**

Bài viết chỉ là **danh sách các claim cần bị thử phá.** Verifier phải tự đi tới
nguồn gốc và đối chiếu.

Ba quy tắc chống tự-xác-nhận:

**V1 — Verifier không được là người viết.**
Trong thực thi bằng AI: phải là một agent riêng, context riêng, không nhìn thấy
quá trình viết bài.

**V2 — Verifier mặc định claim là SAI cho đến khi tìm được nguồn.**
Không phải "tìm lý do để tin". Nhiệm vụ là **phản bác**. Nếu không phản bác được
sau khi thật sự cố gắng, claim mới sống.

**V3 — Verifier phải trích được nguyên văn.**
"Wiki có nói điều này" là không đủ. Phải dẫn được câu nào, ở đâu. Nếu không trích
được, claim tối đa là `INFERENCE`, không bao giờ là `EXPLICIT`.

---

## 2. Ba tầng kiểm định

### Tầng 1 — Kiểm tra máy (Structural)

Chạy tự động bằng công cụ trong `tools/`. Không cần AI.

Kiểm 8 điều kiện toàn vẹn ở `SCHEMA.md` mục 6. Đây là cửa chặn đầu tiên: bài
không qua Tầng 1 thì không đưa vào Tầng 2 (đừng tốn công verify một bài có source
key hỏng).

### Tầng 2 — Kiểm định nguồn (Source Adversarial)

Đây là tầng quan trọng nhất. Một agent độc lập nhận:

- Danh sách claim đã trích ra từ bài (dạng bảng, **không** phải bài viết hoàn chỉnh)
- `CANON-POLICY.md`
- **Không** nhận: bài viết bản đầy đủ, ghi chú của người viết, dossier research gốc

Với mỗi claim, verifier phải trả về một trong bốn phán quyết:

| Phán quyết | Nghĩa | Điều kiện |
|-----------|-------|-----------|
| `CONFIRMED` | Tìm được nguồn độc lập, trích được nguyên văn | Có URL + câu trích + tier đúng |
| `DOWNGRADE` | Claim có thật nhưng nhãn bị gán quá cao | Ví dụ bài ghi `EXPLICIT` nhưng thực tế chỉ suy ra được → phải hạ xuống `INFERENCE` |
| `NOT_FOUND` | Không tìm được nguồn nào chống lưng | Verifier phải nói đã tìm ở đâu |
| `CONTRADICTED` | Tìm được nguồn nói **ngược lại** | Bắt buộc trích cả nguồn ngược |

Verifier **không được** trả về "có lẽ đúng". Bốn phán quyết trên là đóng.

### Tầng 3 — Kiểm định logic nội tại (Consistency)

Một agent thứ ba, chỉ đọc Codex (không fetch web), tìm mâu thuẫn **giữa các bài**:

- Hai bài nói khác nhau về cùng một sự kiện
- Timeline không khả thi (A xảy ra sau B, nhưng B lại được ghi là hệ quả của A)
- Quan hệ một chiều không có nghịch đảo hợp lý (X `killed` Y, nhưng bài Y ghi Y
  chết vì nguyên nhân khác)
- Nhân vật xuất hiện ở hai nơi cùng lúc

Tầng 3 chỉ chạy được khi Codex đã có đủ bài. Với entity đơn lẻ đầu tiên, bỏ qua.

---

## 3. Mức độ nghiêm trọng

Mọi phát hiện được gán một mức:

| Mức | Nghĩa | Xử lý |
|-----|-------|-------|
| `BLOCKER` | Claim sai, hoặc `EXPLICIT` không có nguồn, hoặc bị nguồn khác phản bác | **Phải sửa.** Bài không được `verified` |
| `MAJOR` | Nhãn gán quá cao, nguồn yếu hơn ghi nhận, thiếu mặt tranh chấp | Phải sửa hoặc hạ nhãn |
| `MINOR` | Diễn đạt gây hiểu sai, thiếu liên kết, source key mô tả chưa rõ | Nên sửa |
| `NOTE` | Gợi ý mở rộng, không phải lỗi | Tùy chọn |

**Điều kiện để `status: verified`:** không còn `BLOCKER` và không còn `MAJOR`.

---

## 4. Định dạng báo cáo

Verifier trả về bảng, lưu tại `sources/notes/verify-<entity-id>-<ngày>.md`:

```markdown
# Verify report: sandro — 2026-07-31

Verifier: agent độc lập, không đọc bài gốc
Số claim kiểm: 24
CONFIRMED: 15 | DOWNGRADE: 5 | NOT_FOUND: 3 | CONTRADICTED: 1

## Chi tiết

### C-01
Claim: Sandro là học trò của Ethric
Nhãn bài gán: T1 EXPLICIT
Phán quyết: DOWNGRADE → T6 INFERENCE
Mức: MAJOR
Đã tìm ở: <URL 1>, <URL 2>, <URL 3>
Tìm thấy: <trích nguyên văn hoặc "không có">
Lý do: Nguồn duy nhất là fan wiki, không dẫn được về in-game text.
```

Mỗi claim một block. Không được gộp.

---

## 5. Xử lý sau kiểm định

Người viết (hoặc agent viết) nhận báo cáo và **không được tranh luận bằng trí
nhớ**. Chỉ có ba cách phản hồi hợp lệ:

1. **Sửa bài** theo phán quyết.
2. **Đưa nguồn mới** — phải là URL fetch được, kèm trích nguyên văn.
3. **Chuyển claim** xuống mục *Câu hỏi mở* hoặc *Giả thuyết cộng đồng*.

Cách **không** hợp lệ: "tôi khá chắc là đúng", "điều này ai cũng biết",
"trong game có mà".

---

## 6. Đối với Saga

Saga cần một luồng riêng vì bản chất khác: Saga **được phép sáng tạo**, nên không
kiểm bằng "có nguồn hay không" mà kiểm bằng "có phá canon hay không".

Verifier cho Saga nhận: chương truyện + các entity Codex liên quan. Nhiệm vụ:

| Kiểm | Câu hỏi |
|------|---------|
| Dữ kiện | Chương có khẳng định điều gì trái với Codex? |
| Dữ kiện mới | Chương có tạo ra dữ kiện mới nghe như canon mà Codex không có? |
| Động cơ | Nhân vật hành động trái với động cơ đã được canon xác lập? |
| Thời gian | Trình tự sự kiện có khớp timeline? |
| Vượt phép | Có sáng tạo vượt ranh giới ở `SAGA-STYLE.md` mục 2? |

Phát hiện loại "dữ kiện mới" **không tự động là lỗi** — nhưng bắt buộc phải được
ghi vào `saga/INVENTED-REGISTRY.md`. Chi tiết ở `SAGA-STYLE.md`.

---

## 7. Hạn chế của chính luồng này

Ghi ra để trung thực:

- Verifier cũng là AI, cũng có thể sai. Luồng này **giảm** lỗi, không **loại bỏ**.
- Verifier và người viết có thể fetch cùng một nguồn sai giống nhau. Nếu cả cộng
  đồng Heroes truyền nhau một thông tin sai, luồng này không phát hiện được.
- Sức mạnh thật của luồng nằm ở chỗ bắt được **claim không có nguồn** — đó là loại
  lỗi phổ biến nhất và nguy hiểm nhất khi dùng AI viết lore.
- Không có bản game gốc để đối chiếu là hạn chế cấu trúc, không sửa được bằng
  quy trình.

---

## 8. Lịch sử sửa đổi

| Ngày | Thay đổi | Lý do |
|------|----------|-------|
| 2026-07-31 | Bản đầu | Theo yêu cầu: phải có luồng verdict độc lập, không tin kết quả một chiều |
