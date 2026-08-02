# Verify report: ethric + cloak-of-the-undead-king — 2026-08-02

Theo `00-foundation/VERIFY-PROTOCOL.md`.

**Cấu hình:** agent độc lập, context riêng, **không** đọc bài viết gốc và **không** đọc
dossier research. Input duy nhất: bảng 57 claim đã trích.

| Phần | Số claim |
|---|---|
| A — Ethric | 29 |
| B — Cloak of the Undead King | 28 |

43 lượt fetch.

---

## Kết quả tổng

| Phán quyết | Số lượng |
|---|---|
| `CONFIRMED` | **55** |
| `DOWNGRADE` | 2 |
| `NOT_FOUND` | 0 |
| `CONTRADICTED` | 0 |
| **`BLOCKER`** | **0** |

Tốt hơn hẳn đợt Sandro (3 BLOCKER, 3 MAJOR). Nguyên nhân: bài viết lần này đã áp dụng
sẵn các bài học từ đợt trước — đọc block `==== Events ====`, kiểm trang disambiguation,
và dùng changelog thay vì trang artifact cho claim về HotA.

---

## MAJOR — một claim của mình nói mạnh hơn nguồn cho phép

### C-19 — "bị game text phản bác" → `INFERENCE`

Bài Cloak viết rằng claim "artifact từng thuộc về Ethric" **bị game text phản bác**, dẫn
`sod-target` Day 1:

> "Ethric has spread word of your whereabouts to those **who lost these two precious
> artifacts**"

**Verifier hạ xuống, và đúng.** Câu này phân biệt Ethric (người tung tin) với "những kẻ đã
mất artifact" (người nhận tin) — nhưng đó là **hàm ý từ cấu trúc câu**, không phải lời
khẳng định rằng Ethric chưa từng sở hữu. Game không bao giờ nói "Ethric did not own these".

**"Không có nguồn và rất có thể sai"** khác với **"bị phản bác"**. Đây là đúng loại phân
biệt mà hệ thống nhãn hai trục tồn tại để giữ.

**Bù lại — verifier tìm được bằng chứng MẠNH HƠN mà cả hai đợt research đều bỏ sót:**

`sod-master` Day 15 nêu một chủ cũ **có thật và khác hẳn**:

> "...when they learned that **one of your artifacts was stolen from their people**"

Đó là **người dwarf**. Đây là chủ cũ duy nhất game nêu đích danh — và nó cũng giải thích
vì sao các tộc dwarf vốn thù nhau lại lần đầu hợp lực chống Sandro.

**Đã xử lý:** hạ nhãn xuống `INFERENCE`, viết lại mục tranh chấp, và **thêm bằng chứng
dwarf vào phần Xuất xứ** — nó vừa chính xác hơn vừa hay hơn về mặt kể chuyện.

---

## MINOR — một chỗ nói tuyệt đối quá

### E-05 — "nguồn duy nhất" → cần chính xác hơn

Bài Ethric viết Gem's epilogue là **nguồn duy nhất** cho việc Ethric sống công khai như
một wizard.

Verifier chỉ ra: đó là nguồn duy nhất **nêu tên Bracada**, nhưng danh tính học giả công
khai còn được xác lập độc lập ở `sod-after-the-amulet`:

> "**Ethric is an academician**"

**Đã xử lý:** tách hai claim, dẫn cả hai nguồn.

---

## Bốn claim phủ định — đều được kiểm nghiêm và đều đứng vững

Đây là phần đáng chú ý nhất, vì **claim phủ định chính là chỗ đợt Sandro sai ba lần**.

### E-01 — "Ethric không nói một câu nào trong Heroes III" ✅

Verifier chủ động săn lời thoại Ethric qua **bảy** scenario. Kết quả:

> "Every reference is indirect. The strongest near-miss is Agents of Vengeance, Day 9,
> which is Gem paraphrasing a letter... reported speech, no quotation marks, no direct
> line."

**Không có lời thoại nào tồn tại.** Claim đứng vững sau khi bị tấn công có chủ đích.

### E-09 / E-10 — "không có cảnh chết trong *Master*" ✅

Verifier kiểm cấu trúc trang: có Prologue / Scenario / Timed events / Objects / Events /
Towns / Heroes / Seer's Huts — **không có mục Epilogue**. Timed event cuối là Day 23. Không
gì kể cái chết.

Và `grep -c "Ethric"` trên scenario kế tiếp trả về **0**.

Đây là claim đã kích hoạt Tầng 3 bắt lỗi bài Sandro. Giờ được xác nhận độc lập.

### E-24 — "chỉ có một Ethric duy nhất" ✅

Verifier gọi đây là "highest-risk negative claim" và kiểm rất kỹ — đúng bài học từ ca
`Sandro (Xeen)`.

Fandom `allpages` trả về **7 tiêu đề** bắt đầu bằng "Ethric", thoạt nhìn như nhiều nhân
vật. Verifier fetch **từng cái**: bốn biến thể tên nhân vật đều là **redirect trơ** về một
bài duy nhất.

Verifier còn kiểm thêm: wiki **có** bao phủ Ashan (các trang `Ashan`, `Demon (Ashan)`,
`Stephan (Ashan)` đều tồn tại) nhưng **không có Ethric bản Ashan**.

**Claim đứng vững, và lần này được kiểm chứ không phải giả định.**

---

## Bốn chi tiết verifier bổ sung

| # | Nội dung | Xử lý |
|---|---|---|
| 1 | **Timeline của chính Fandom mâu thuẫn với văn xuôi của Fandom.** Timeline đặt SoD ~1155–1164 AS, MM6 **1165 AS** — ủng hộ thứ tự của thelazy, chống lại prose của Fandom | ✅ Đã thêm vào mục tranh chấp |
| 2 | **Cơn ác mộng lặp lại ở Day 71**, không chỉ Day 69: "you know **his sword** is about to slice through you" | ✅ Đã thêm |
| 3 | `sod-target` Day 24 có **hai** lỗi ngữ pháp, không phải một — còn "According to **you** advisors" | ✅ Đã ghi trong bài |
| 4 | `sod-agents-of-vengeance` là một lần xuất hiện đáng kể của Ethric mà bảng claim không khai thác | ✅ Đã thêm vào `sources_used` |

Về C-11 (giá trị Necromancy qua các bản), verifier lưu ý: entry changelog 1.3.0 chỉ nói
**bằng lời** ("reduced by half"); con số cụ thể 2,5/5/7,5/15% chỉ xuất hiện **hồi cố** ở
entry 1.8.0. Claim vẫn đúng, nhưng con số cho 1.3.0 là **tái dựng** từ dòng 1.8.0.

---

## Vì sao đợt này ít lỗi hơn hẳn

Đợt Sandro: 3 BLOCKER + 3 MAJOR. Đợt này: 0 BLOCKER + 1 MAJOR.

Khác biệt không phải may mắn — là do **ba bài học đã được đưa vào quy trình**:

1. **Đọc block `==== Events ====`** — không chỉ prologue/epilogue. Đây là chỗ tìm ra map
   event Jabarkas (15,27,0) và chi tiết dwarf ở `sod-master` Day 15.
2. **Kiểm trang disambiguation** trước mọi claim "không xuất hiện ở đâu khác".
3. **Dùng changelog thay vì trang artifact** cho mọi claim về HotA.

Cả ba đều được viết thẳng vào prompt research và prompt verify.

---

## Điều kiện `verified`

Theo `VERIFY-PROTOCOL.md` mục 3: không còn `BLOCKER`, không còn `MAJOR`.

- 0 `BLOCKER`
- 1 `MAJOR` (C-19) → đã xử lý
- 1 `MINOR` (E-05) → đã xử lý
- 4 chi tiết bổ sung → đã đưa vào

**Cả hai bài đủ điều kiện `status: verified`.**

Và **Sandro được phục hồi `verified`** — luồng này xác nhận độc lập rằng việc hạ
`killed → ethric` xuống `DISPUTED` là đúng (E-09, E-10 đều `CONFIRMED`).

Kèm điều kiện thường lệ: cả ba bài vẫn mang hạn chế nền tảng `T1*`.
