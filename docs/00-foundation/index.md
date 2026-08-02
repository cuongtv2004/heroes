# Nền tảng

Sáu tài liệu quy định **cách dự án làm việc**. Đọc theo thứ tự dưới đây.

---

## Thứ tự đọc

| # | Tài liệu | Trả lời câu hỏi |
|---|---|---|
| 1 | [CANON-POLICY](CANON-POLICY.md) | Điều gì là thật? Nguồn nào thắng khi mâu thuẫn? |
| 2 | [SCHEMA](SCHEMA.md) | Dữ liệu tổ chức thế nào? Quan hệ nào được phép? |
| 3 | [VERIFY-PROTOCOL](VERIFY-PROTOCOL.md) | Làm sao biết bài viết không bịa? |
| 4 | [WORKFLOW](WORKFLOW.md) | Các bước cụ thể để viết một bài |
| 5 | [TIMELINE-SPINE](TIMELINE-SPINE.md) | Sự kiện xếp theo thứ tự nào? |
| 6 | [SAGA-STYLE](SAGA-STYLE.md) | Được sáng tạo tới đâu khi viết truyện? |

Kèm theo: [BACKLOG](BACKLOG.md) — việc còn tồn, tồn tại qua nhiều phiên làm việc.

---

## Bốn quyết định thiết kế đáng chú ý

### Nhãn hai trục, không phải một

Nguồn (`T1`–`T6`) và độ chắc (`EXPLICIT`/`INFERENCE`/`DISPUTED`/…) là **hai trục độc
lập**. Một chi tiết trong manual có thể là nguồn cấp thấp hơn in-game text nhưng vẫn
`EXPLICIT` chứ không phải suy luận.

Gộp hai trục lại sẽ không diễn đạt được những ca như: *claim này có trong game text,
nhưng game trình bày nó dưới dạng tin đồn.*

### Timeline dựa trên quan hệ tương đối

Old Universe **không có** một hệ lịch nhất quán. Nếu chờ chốt hết năm tuyệt đối mới
viết, dự án sẽ không bao giờ ra khỏi Giai đoạn 1.

Nên xương sống là **trước/sau/đồng thời**; năm tuyệt đối chỉ là một thuộc tính có nhãn.

### Verifier không đọc bài gốc

Đây là điều làm luồng kiểm định có giá trị thật. Verifier nhận **bảng claim đã trích**,
không nhận bài viết — rồi tự đi tìm nguồn và **mặc định coi claim là sai**.

Nếu verifier đọc bài gốc, nó sẽ tự xác nhận chính mình. Đó là thất bại phổ biến nhất khi
dùng AI để kiểm tra AI.

### Bộ quan hệ đóng

~30 loại quan hệ được định nghĩa cố định trong [SCHEMA](SCHEMA.md). Muốn thêm phải sửa
tài liệu trước.

Nếu ai cũng tự đặt tên quan hệ, knowledge graph sẽ không query được — và Atlas, gia phả,
timeline tương tác ở Giai đoạn 4 sẽ không dựng được.

---

## Bài học đắt nhất

Ba claim **phủ định** đã lọt vào Codex rồi bị luồng kiểm định phản bác:

- "Không có developer commentary nào" → **sai**, có phỏng vấn Lead Designer, nằm ngay
  trên wiki đang dùng
- "Tuyến Tyranell không xác nhận được" → **sai**, là game text thật
- "Không xuất hiện ở game MM RPG nào khác" → **sai**, có một nhân vật trùng tên

Cả ba cùng một dạng: *"không tồn tại", "không tìm được", "không xác nhận được"* — đưa ra
quá sớm.

**Đây là loại lỗi nguy hiểm hơn claim khẳng định sai, vì nó trông giống sự cẩn trọng.**
Viết "không có nguồn" nghe như đang trung thực, trong khi thực chất chỉ là chưa tìm đủ.

Chi tiết và cách phòng: [WORKFLOW](WORKFLOW.md).
