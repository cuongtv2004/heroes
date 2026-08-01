# BACKLOG

Việc cần đào sâu, ghi lại để không mất dấu. Không phải todo của phiên làm việc — đây là
**nợ kỹ thuật của dự án**, tồn tại qua nhiều phiên.

Mỗi mục ghi: nó là gì, vì sao đáng làm, và cần gì để làm được.

Ưu tiên: **P0** = chặn chất lượng toàn dự án · **P1** = đáng làm sớm ·
**P2** = làm khi tiện · **P3** = có thì tốt.

---

## P0 — Chặn chất lượng toàn dự án

### B-001 · Nâng `T1*` → `T1` bằng cách trích file game gốc

**Vấn đề:** toàn bộ text in-game trong Codex hiện là **bản chép của fan wiki**
(heroes.thelazy.net qua `?action=raw`), không phải file game. Đây là hạn chế nền tảng
lớn nhất, ảnh hưởng **mọi bài đã và sẽ viết**.

**Vì sao vẫn tin ở mức cao hiện tại:** wiki chép nguyên cả lỗi chính tả trong game, đánh
dấu bằng `{{sic}}`, và tách bạch text chính thức khỏi ý kiến fan. Xem
`sources/REGISTRY.md` mục "Lưu ý về T1*".

**Cần gì:** một bản cài Heroes III (SoD hoặc Complete). Text campaign nằm trong file
`.h3c`. Cần viết công cụ trích.

**Ảnh hưởng nếu làm được:** mọi claim `T1*` nâng lên `T1` thật. Đây là nâng cấp chất
lượng lớn nhất có thể có cho dự án.

**Trạng thái:** chưa bắt đầu. Cần user xác nhận có bản game không.

---

## P1 — Đáng làm sớm

### B-002 · Fetch tài liệu thiết kế gốc của Jennifer Bullard (UT Austin)

**Là gì:** Bullard — Lead Designer và người viết cốt truyện *Shadow of Death* — đã gửi
một bộ tài liệu làm việc cho **Dolph Briscoe Center for American History, University of
Texas**.

`repositories.lib.utexas.edu/items/e3abd6e5-b6be-4547-8900-17b2c9e237da`
(mục lục ghi "Heroes [of Might and Magic] documents")

**Vì sao đáng làm:** đây là **nguồn T3 thật** — tài liệu thiết kế gốc, không qua trung
gian. Có thể chứa phần tiểu sử chưa từng phát hành, kể cả câu trả lời cho **Q1 của
Sandro** (quá trình thành lich — điều không nguồn nào hiện có trả lời được).

**Lead phụ:**
- `heroes3wog.net` được cho là có tư liệu phục hồi từ bộ này ("General Kendal's Diary")
- Thread cộng đồng: `celestialheavens.com/forum/topic/16558`
  ("Jennifer Bullard - Lost manuscript files")

**Cần gì:** thử fetch trực tiếp. Nếu không được, có thể phải liên hệ thư viện.

**Trạng thái:** chưa fetch. **Lead giá trị nhất chưa khai thác của dự án.**

### B-003 · Rà lại mọi claim phủ định trong Codex

**Vấn đề:** luồng kiểm định bài Sandro phản bác **ba** claim, và cả ba đều cùng một
dạng — **claim phủ định** ("không tồn tại", "không tìm được", "không xác nhận được")
đưa ra quá sớm.

Đây là loại lỗi nguy hiểm hơn claim khẳng định sai, vì nó **trông giống sự cẩn trọng**.

**Hai nguyên nhân kỹ thuật đã xác định:**

1. **Bỏ sót block map event.** Text nằm trong `==== Events ====` của scenario, không phải
   prologue/epilogue. Tra cứu đọc mỗi prologue sẽ không thấy. → Đây là nguyên nhân của
   cả B-01 (Tyranell) lẫn một phần B-02.
2. **Không kiểm trang disambiguation.** Claim "không xuất hiện ở đâu khác" phải kiểm qua
   trang disambiguation của wiki, không chỉ trang nhân vật. → Nguyên nhân bỏ sót
   `Sandro (Xeen)`.

**Việc cần làm:** mỗi khi viết bài mới, mọi claim phủ định phải qua hai kiểm tra trên
**trước khi** đưa vào bài.

**Trạng thái:** đã ghi thành quy tắc. Cần áp dụng nhất quán.

### B-004 · Tìm đường vào `homm.miraheze.org`

**Vấn đề:** site này **chặn bot** (403 với cả curl và fetch) trong **cả hai** đợt
research. Có thể là nguồn của một số claim đang lưu hành mà dự án không kiểm được.

**Ảnh hưởng cụ thể:** claim "thời điểm Sandro thành lich" hiện là `UNVERIFIED` thay vì
`DISPUTED` **chỉ vì** không vào được site này để tìm phía thứ hai.

**Trạng thái:** chưa có giải pháp.

---

## P2 — Làm khi tiện

### B-005 · Thử lại `heroesofmightandmagic.com` (site chính thức NWC)

Connection refused — có thể đã chết hẳn. `web.archive.org` bị chặn trong môi trường này
nên không lấy được bản lưu.

Đây là **nguồn không-phải-wiki tốt nhất** có thể có cho mô tả campaign chính thức.

### B-006 · Thử lại kho phỏng vấn Celestial Heavens

Trả 403 trong cả hai đợt. Có thể còn phỏng vấn NWC khác ngoài Bullard và Fulton.

Lưu ý: nội dung gần đây của CH thuộc thời Ubisoft/Ashan — **không liên quan** Old
Universe. Cần tìm phần archive cũ.

### B-007 · Kiểm quote Gauldoth Half-Dead (Heroes IV)

Hiện chỉ là quote-box trên Fandom, **không dẫn nguồn**:

> "When others like the powerful necromancer, Sandro, sought to control the world, the
> force of destruction supported them temporarily..."

Câu rất đáng dùng, nhưng chưa xác minh được. Cần nguồn Heroes IV độc lập.

### B-008 · Kiểm số liệu XP/level của Sandro bằng map editor

Fandom đưa số cụ thể (200.933 / 3.066.455 / **5.555.555** / 28.000) nhưng không dẫn
nguồn. Đọc như dữ liệu trích từ file map thật — số 5.555.555 quá gọn để là ngẫu nhiên.

**Kiểm được bằng map editor** nếu có bản game (xem B-001).

### B-009 · Tìm ảnh scan vỏ hộp Heroes I

Claim "ảnh Sandro in trên một mặt vỏ hộp Heroes I" chỉ có **một** wiki khẳng định, không
dẫn nguồn. Fandom — nguồn chi tiết nhất về vai trò H1 của Sandro — **im lặng**.

MobyGames bị Cloudflare chặn, archive.org bị chặn.

---

## P3 — Có thì tốt

### B-010 · Quyết định cấu trúc Book V của Saga

Heroes Chronicles **không nằm gọn** trong một khoảng thời gian — Tarnum xuyên nhiều kỷ
nguyên. Xếp thành Book V (sau Heroes III) là **thứ tự đọc**, không phải thứ tự thời gian.

Hai phương án: kể theo thời gian (rải vào các Book khác) hay theo thứ tự đọc (giữ Book V).

Chưa đủ dữ liệu để chốt. Xem `TIMELINE-SPINE.md` mục 5.

### B-011 · Tìm nguồn cho hệ lịch "AS"

Dự án đang dùng ký hiệu năm "AS" mà chưa biết nó viết tắt của gì và bắt nguồn từ đâu.

### B-012 · Fetch timeline trong manual Heroes III

`h3-manual-timeline` được nhắc tới trong nhiều nguồn nhưng **chưa fetch được**. Sẽ giúp
nhiều cho `TIMELINE-SPINE.md`, hiện chỉ có **hai** mốc năm tuyệt đối.

### B-013 · Nội dung ChatGPT share của user

Link `chatgpt.com/share/6a6c0766-b3ac-83ec-9c93-ae2c52175d50` **không fetch được** —
trang render bằng JavaScript, chỉ lấy được title: **"ChatGPT - HoMM3 Chiến Thuật"**.

Title gợi ý đây là nội dung về **chiến thuật chơi game**, không phải lore — nếu đúng thì
thuộc mục Gameplay, không phải phần canon.

**Cần:** user paste nội dung trực tiếp hoặc lưu vào `sources/raw/`.

**Xử lý khi có:** output của một AI khác **không phải nguồn**. Trích claim ra bảng, cho
verifier độc lập tìm nguồn T1–T4 cho từng cái — đúng luồng đã dùng cho Sandro.

---

## Đã xong

| # | Việc | Kết quả |
|---|---|---|
| ✅ | Tìm developer commentary | 4 nguồn T4: Bullard (Lead Designer SoD) + Fulton (Lead Designer H3) ×3 |
| ✅ | Kiểm tuyến Tyranell / Statue of Legion | Là game text thật, ở `sod-gathering-the-legion` |
| ✅ | Kiểm cảnh dấu ngón tay xương trên ngực Finneas | Tìm được ở `sod-invasion` Day 17 |
| ✅ | Tìm nguồn MM8 độc lập | `mm8-guide-walkthrough`; sửa được lỗi "đồng lãnh đạo" |
| ✅ | Làm rõ tranh chấp Chronicles | Lập luận niên đại mạnh, lập luận sinh tử yếu |
| ✅ | Sửa tier bio hero | `T2*` → `T1*` (chép từ `HEROBIOS.TXT`) |

---

## Lịch sử

| Ngày | Thay đổi |
|---|---|
| 2026-07-31 | Lập backlog sau khi Sandro đạt `verified` |
