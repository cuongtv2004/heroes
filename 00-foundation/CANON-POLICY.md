# CANON POLICY

Tài liệu này quy định **cách dự án xác định điều gì là thật** trong Old Universe
(Heroes I–IV, Heroes Chronicles, Might and Magic I–VIII).

Đây là tài liệu có quyền lực cao nhất trong dự án. Khi bất kỳ bài viết nào trong
Codex hoặc chương nào trong Saga xung đột với tài liệu này, tài liệu này thắng.

---

## 1. Vấn đề cần giải quyết

Old Universe **không có** một canon nhất quán. Đây không phải khiếm khuyết của
dự án mà là thực tế của tư liệu gốc:

- New World Computing thay đổi lore giữa các bản game.
- Manual đôi khi mâu thuẫn với nội dung in-game của chính bản game đó.
- Heroes Chronicles kể lại các sự kiện Heroes I–II qua góc nhìn Tarnum,
  đôi khi lệch chi tiết.
- Might and Magic RPG và Heroes chia sẻ thế giới nhưng viết bởi các nhóm khác nhau.
- Sau khi 3DO sụp đổ (2003), một phần tư liệu phát triển bị thất lạc hoặc chỉ còn
  qua lời kể của developer trong phỏng vấn.

Do đó dự án **không** đặt mục tiêu "tìm ra canon duy nhất". Mục tiêu là:

> Mọi thông tin đưa ra đều nói rõ **nó đến từ đâu** và **chắc chắn đến mức nào**.

Người đọc luôn phân biệt được đâu là dữ kiện, đâu là suy luận, đâu là giả thuyết.

---

## 2. Hệ thống nhãn hai trục

Mỗi thông tin (claim) trong Codex mang **hai nhãn độc lập**.
Không được gộp hai trục này lại.

### Trục A — Cấp nguồn (Source Tier)

Nguồn thông tin đến từ đâu. Cấp thấp hơn về số thì có quyền cao hơn.

| Tier | Tên | Nội dung | Ví dụ |
|------|-----|----------|-------|
| **T1** | In-game text | Văn bản xuất hiện trực tiếp khi chơi: campaign briefing, dialogue, cutscene, quest log, item description | Briefing các map trong *Shadow of Death*; thoại NPC trong MM7 |
| **T2** | Official print | Manual, strategy guide chính thức do NWC/3DO phát hành, novelization được cấp phép | *Heroes III Manual*; *Heroes IV Manual* |
| **T3** | Game data | Dữ liệu trích từ file game không hiển thị trực tiếp cho người chơi: map editor string, file lore chưa dùng, tên nội bộ | String trong `.h3m`; text unused trong game archive |
| **T4** | Developer statement | Phát ngôn của developer NWC/3DO ngoài sản phẩm: phỏng vấn, post trên forum, thư trả lời fan | Phỏng vấn Jon Van Caneghem; post của developer trên Celestial Heavens |
| **T5** | Licensed adjacent | Sản phẩm được cấp phép nhưng ngoài dòng chính, hoặc thuộc universe khác nối vào | Ubisoft-era retcon (Ashan) khi nói về Old Universe |
| **T6** | Community reconstruction | Tổng hợp của cộng đồng, wiki, fan research — **không** phải nguồn gốc | Fandom wiki; Celestial Heavens article |

**Quy tắc quan trọng:** T6 **không bao giờ** là nguồn cuối cùng cho một claim
được gắn nhãn CANON. T6 chỉ dùng để *dẫn đường tới* nguồn T1–T4. Nếu một claim
chỉ có T6 chống lưng, nó tối đa là `INFERENCE` hoặc `UNVERIFIED`.

### Trục B — Độ chắc (Certainty)

Thông tin được rút ra như thế nào từ nguồn đó.

| Nhãn | Ý nghĩa | Điều kiện |
|------|---------|-----------|
| `EXPLICIT` | Nguồn nói thẳng ra | Có thể trích nguyên văn câu chống lưng cho claim |
| `INFERENCE` | Suy luận từ một hoặc nhiều nguồn | Nguồn không nói trực tiếp, nhưng kết luận theo được từ dữ kiện đã nêu. **Bắt buộc** ghi rõ suy luận theo bước nào |
| `DISPUTED` | Các nguồn mâu thuẫn nhau | Có ≥2 nguồn nói khác nhau. **Bắt buộc** trình bày cả các phương án, không được chọn ngầm một cái |
| `FAN_THEORY` | Giả thuyết cộng đồng | Không có nguồn T1–T4 chống lưng. Được ghi lại vì có giá trị thảo luận, nhưng phải tách khỏi phần thân bài |
| `UNVERIFIED` | Chưa kiểm được | Dự án chưa truy được về nguồn gốc. Trạng thái tạm thời — cần xử lý, không được để tồn đọng |

### Cách viết nhãn

Trong thân bài, dùng cú pháp inline:

```
Sandro từng là học trò của Ethric. {T1 EXPLICIT: sod-birth-of-a-barbarian}
```

`sod-birth-of-a-barbarian` là **source key**, trỏ tới một entry trong
`sources/REGISTRY.md`. Không được ghi nhãn mà thiếu source key.

Với `INFERENCE`, ghi thêm bước suy luận:

```
Sandro có thể đã ở Deyja trước năm 1170. {T1 INFERENCE: sod-m1 + h3-manual-deyja
 — vì hắn xuất hiện với chức vị đã có sẵn, không phải người mới đến}
```

---

## 3. Thứ tự ưu tiên khi mâu thuẫn

Khi hai nguồn nói khác nhau, áp dụng **theo thứ tự** các quy tắc sau. Quy tắc
trước thắng quy tắc sau.

**R1 — Cùng game, in-game thắng manual.**
Nội dung hiển thị khi chơi phản ánh sản phẩm cuối; manual thường viết trước khi
game hoàn thiện và không được cập nhật.

**R2 — Game sau thắng game trước, TRỪ khi game sau là spin-off.**
Heroes III thắng Heroes II về các sự kiện chung. Nhưng Chronicles (spin-off) không
tự động thắng Heroes II.

**R3 — Nguồn kể trực tiếp thắng nguồn kể lại.**
Heroes II kể sự kiện Heroes II tại thời điểm đó; Chronicles kể lại các sự kiện đó
qua ký ức Tarnum, cách hàng trăm năm. Với sự kiện Heroes I–II, Heroes I–II thắng.

**R4 — Heroes và MM RPG ngang quyền; mâu thuẫn thì ghi DISPUTED.**
Không có cơ sở nào để nói dòng nào "chính thống hơn". Không được ngầm chọn.

**R5 — Ubisoft-era (Ashan) không có quyền gì với Old Universe.**
Ashan là universe tách biệt (reboot). Mọi thông tin từ đó chỉ được nhắc tới như
tham chiếu ngoại vi, không bao giờ là canon Old Universe.

**R6 — Developer statement không ghi đè in-game text.**
T4 giải thích *ý định*, không sửa được *sản phẩm*. Nếu dev nói X nhưng game thể
hiện Y, thì Y là canon và X được ghi ở mục Trivia hoặc Dev Intent.

**R7 — Nếu không quy tắc nào giải quyết được: `DISPUTED`.**
Đây là kết quả hợp lệ và thường xuyên. Không cưỡng ép ra một câu trả lời.

---

## 4. Nguyên tắc về năm tháng

Old Universe không có một hệ lịch thống nhất áp được cho toàn bộ. Do đó:

- **Xương sống của timeline là quan hệ tương đối** (trước / sau / đồng thời),
  không phải năm tuyệt đối.
- **Năm tuyệt đối là một thuộc tính có nhãn**, giống mọi claim khác.
- Một sự kiện có thể có năm `DISPUTED` mà vị trí tương đối vẫn `EXPLICIT`.

Chi tiết xem `TIMELINE-SPINE.md`.

Lý do: nếu chờ chốt được toàn bộ năm tuyệt đối mới viết, dự án sẽ không bao giờ
qua được Giai đoạn 1. Quan hệ tương đối là đủ để kể chuyện.

---

## 5. Ràng buộc bắt buộc với mọi bài Codex

Một bài Codex chỉ được coi là hoàn thành khi thỏa **toàn bộ**:

1. Mọi claim trong thân bài có nhãn hai trục + source key.
2. Mọi source key tồn tại trong `sources/REGISTRY.md`.
3. Không claim nào ở trạng thái `UNVERIFIED` trong thân bài
   (chuyển xuống mục *Câu hỏi mở* nếu chưa giải quyết được).
4. Đã qua **luồng kiểm định độc lập** (xem `VERIFY-PROTOCOL.md`) và không còn
   phát hiện mức `BLOCKER`.
5. `FAN_THEORY` nằm trong mục riêng, không trộn vào phần tiểu sử.

---

## 6. Điều dự án tự nhận là hạn chế

Ghi ra đây để không tự lừa mình:

- Dự án **không** có bản sao file game gốc. T1 và T3 tiếp cận qua trung gian
  (transcript cộng đồng, wiki trích dẫn). Điều này làm T1 của dự án yếu hơn T1
  thật. Khi một claim quan trọng chỉ dựa vào transcript chưa đối chiếu được, ghi
  `T1* ` (có dấu hoa thị) để đánh dấu là "T1 qua trung gian".
- Trí nhớ của mô hình AI **không phải nguồn**. Không claim nào được chống lưng
  bằng "theo tôi biết". Nếu không fetch được nguồn, claim đó là `UNVERIFIED`.
- Một số tư liệu 3DO đã thất lạc vĩnh viễn. Có những câu hỏi sẽ không bao giờ có
  đáp án, và dự án ghi nhận điều đó thay vì lấp bằng suy đoán.

---

## 7. Lịch sử sửa đổi policy

| Ngày | Thay đổi | Lý do |
|------|----------|-------|
| 2026-07-31 | Bản đầu | Khởi tạo dự án |
