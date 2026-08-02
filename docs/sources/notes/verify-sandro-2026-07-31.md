# Verify report: sandro — 2026-07-31

Theo `00-foundation/VERIFY-PROTOCOL.md`.

**Cấu hình:** hai agent độc lập, context riêng, **không** đọc bài viết gốc và **không**
đọc dossier research. Input duy nhất: bảng 65 claim đã trích + `CANON-POLICY.md`.

| Luồng | Nhiệm vụ | Số lượt fetch |
|---|---|---|
| Tầng 2 — kiểm nguồn đối kháng | 65 claim, mặc định coi là sai | 78 |
| Luồng lấp lỗ hổng | 6 câu hỏi đợt đầu không giải quyết được | 36 |

Tầng 3 (kiểm mâu thuẫn giữa các bài) **bỏ qua** — Codex mới có một bài.

---

## Kết quả tổng

| Phán quyết | Số lượng |
|---|---|
| `CONFIRMED` | 47 |
| `DOWNGRADE` | 10 |
| `NOT_FOUND` | 2 |
| `CONTRADICTED` | **3** |

Toàn bộ `BLOCKER` và `MAJOR` đã xử lý. Bài đủ điều kiện `verified` theo
`VERIFY-PROTOCOL.md` mục 3.

---

## BLOCKER — ba claim bị phản bác

### B-01 — "Không có developer commentary nào" → **SAI**

**Đây là sai sót nghiêm trọng nhất.** Bài viết ban đầu khẳng định điều này ở **ba chỗ**.

Verifier tìm được **ba nguồn T4** riêng biệt:

1. **Jennifer Bullard — Lead Designer của *Shadow of Death*** — trả lời trực tiếp câu hỏi
   về thầy của Sandro:
   > "Q: Ethric the Mad from Might and Magic VI... Was he the same master of Sandro...?
   > A: **Yes, we always tried to tie the different products together...**"

2. **Greg Fulton — Lead Designer Heroes III** — Fanstratics Newsletter #13, gọi Sandro là
   hero mang tính biểu tượng.

3. **Greg Fulton** — Newsletter #27, ghi lại yêu cầu thiết kế H3: "Keep specific heroes
   from HoMM2, like **Sandro the Necromancer**..."

Và Fulton còn chỉ đúng người cần hỏi (Newsletter #3): "As far as I know, **Jennifer
Bullard was the project's Lead Designer, and any questions you have about SoD would best
be directed to her.**"

**Điều đáng lo nhất:** phỏng vấn Bullard được host **trên chính wiki mà bài viết dùng
xuyên suốt**, và trang Ethric của wiki đó **đã dẫn link tới nó**. Nghĩa là nguồn nằm cách
đúng một cú click từ trang mà bài viết chắc chắn đã đọc.

**Đã xử lý:** viết lại mục *Trivia & Dev Notes*, thêm hai source key mới, sửa
`REGISTRY.md` Nhóm 4, sửa `README.md`.

### B-02 — "Tuyến Tyranell không xác nhận được trong scenario text" → **SAI**

Có, và ở **hai** scenario:

`sod-gathering-the-legion`, map event (8,60,0):
> "he tells you that **Sandro was going to pay Tyranell well to find the Head and other
> pieces of Legion.**"

Xác nhận thất bại từ phía Sandro — `sod-wrath-of-sandro`, Day 9:
> "**he put together the Statue of Legion**, allowing the Erathians to gain too much
> population for you to deal with."

**Nguyên nhân bỏ sót — đáng ghi nhớ:** text nằm trong block `==== Events ====` (map
event), không phải prologue hay timed event. Đọc chỉ prologue/epilogue sẽ không thấy.

Verifier khuyến nghị: **rà lại mọi claim dựa trên "không tìm được trong scenario text"
đối chiếu với block map event.**

**Đã xử lý:** thêm mục *Mưu thứ ba* vào tiểu sử, thêm quan hệ `was_served_by → tyranell`.

### B-03 — "Sandro không xuất hiện trong game MM RPG nào khác" → **SAI**

Có **`Sandro (Xeen)`** — nhân vật riêng trong *Might and Magic V: Darkside of Xeen*, một
lich, questgiver và boss ở Necropolis.

Và liên hệ thật ở tầng sản xuất:
> "**Sandro's enemy sprite was used as the basis for his Enrothian counterpart's
> portrait**, by essentially just recoloring and throwing him into a robe."

Phần hẹp của claim (không có ở MM6, MM7) thì **đúng**. Nhưng câu tổng quát thì sai, và
việc bỏ sót là đáng kể vì portrait Sandro mà mọi người quen mắt bắt nguồn từ đó.

**Bài học:** claim phủ định dạng "không xuất hiện ở đâu khác" phải kiểm qua **trang
disambiguation**, không chỉ trang nhân vật.

**Đã xử lý:** thêm mục riêng trong *Xuất hiện trong game*, thêm `fandom-sandro-xeen`.

---

## MAJOR — ba claim gán nhãn quá mạnh

### M-01 — Jabarkas là em trai Ethric: `EXPLICIT` → `DISPUTED`

Ba vấn đề verifier nêu:

1. **Là tin nghe lại *trong* game text** — "**According to you advisors**, Lord
   Jabarkas... is Ethric's illegitimate younger brother." Cố vấn nói, không phải người kể.
2. **Xung đột với bio in-game khác** — `h3wiki-jabarkas`: "Being the **eldest son of Duke
   Boragus**", và Jabarkas là **Ogre của Krewlod**.
3. **Wiki cũng đánh giá là bịa** — `h3wiki-ethric`: "**The latter is very likely**"
   (tức là vỏ bọc).

**Đã xử lý:** thêm mục tranh chấp số 5, thêm chú thích ở phần tiểu sử.

### M-02 — Thời điểm thành lich: `DISPUTED` → `UNVERIFIED`

Bài viết trình bày như tranh chấp hai phía (Fandom nói trước, kmcgames nói sau). Verifier
**chỉ tìm được một phía** — không nguồn nào đặt mốc sau First War.

Nguồn thứ hai có thể là `homm.miraheze.org`, **chặn bot** (403) trong cả hai đợt.

**Nhận xét đáng ghi của verifier:** gọi là "tranh chấp" khi chỉ trích được một phía là
**tự tạo ra sự cân bằng không có thật**.

**Đã xử lý:** hạ xuống `UNVERIFIED`.

### M-03 — Ảnh Sandro trên vỏ hộp Heroes I: `T1*` → `T6`

Sai **tier**, không sai nội dung. Một claim về **vỏ hộp** không liên quan gì tới text
in-game.

Thêm nữa: chỉ một wiki khẳng định, không dẫn nguồn; Fandom — nguồn chi tiết nhất về vai
trò H1 của Sandro — **không nhắc gì**, và mô tả mặt trước hộp là "a radiant storybook
adorned with imagery of a Knight." Không lấy được bản scan (MobyGames bị Cloudflare chặn,
archive.org bị chặn).

**Đã xử lý:** hạ tier, ghi rõ Fandom im lặng.

---

## MINOR — bốn chỗ diễn đạt quá mạnh

| # | Vấn đề | Xử lý |
|---|---|---|
| m-01 | "Cả hai đều không được trả tiền" quá tuyệt đối — Gem **có** nhận tiền các đợt trước ("if I hadn't taken my payment"), chỉ bị lừa món cuối | Thêm chú thích chính xác hóa |
| m-02 | Finneas "làm hỏng" nghi thức — chữ đó **không có** trong nguồn nào. Game text chỉ nói "met with an unfortunate accident" | Trích nguyên văn, bỏ chữ "làm hỏng" |
| m-03 | Roster *Duke Alarice* được dùng làm "bằng chứng chứng minh" hai class khác nhau — quá mạnh, map đó còn 3 Necromancer khác | Dùng định nghĩa class làm bằng chứng, roster chỉ là minh họa |
| m-04 | MM8 "Twilight Necromancers' Guild" — **sai tên**. Twilight là một **thành phố** dưới chân núi; tổ chức là Necromancers' Guild của Shadowspire | Sửa tên |

---

## Sai sót về tier có ảnh hưởng nhiều bài sau này

**Bio hero chính thức là `T1*`, không phải `T2*`.**

Bài viết gán bio H3 và H4 là `T2*` (manual in). Sai — wiki ghi rõ chúng chép từ
**`HEROBIOS.TXT`**, một **file dữ liệu trong game**.

Kiểm chứng ngược: manual in SoD trang 15 có thông số Sandro nhưng **không có đoạn bio
nào**.

**Điều này quan trọng vì nó là nền của "mâu thuẫn" C-04/C-05.** Nếu cả hai đều là in-game
text thì `CANON-POLICY.md` R1 (in-game thắng manual) **không áp dụng được** — và "mâu
thuẫn" yếu đi đáng kể.

Thêm nữa, verifier chỉ ra wiki **tự dung hòa** hai Ethric ("alter-ego of a mortal
Bracadan wizard"), và **Bullard xác nhận ở tầng developer** rằng đó là cùng một người.

**Đã xử lý:** sửa tier, viết lại mục tranh chấp số 3 từ "mâu thuẫn trong tư liệu chính
thức" thành "lệch giọng, không lệch dữ kiện". Ghi cảnh báo tier vào `REGISTRY.md`.

---

## Claim mạnh nhất — sống sót qua tấn công đối kháng

Verifier nêu riêng những claim này là **được chống lưng tốt và gán nhãn đúng**:

| Claim | Vì sao mạnh |
|---|---|
| **Sandro không bao giờ được nói là chết** | Verifier "tìm rất kỹ" một nguồn nói hắn chết và **chỉ tìm được các nguồn khẳng định hắn sống**: "was defeated in battle, **though escaped destruction**", `status = Active (as of Heroes IV)` |
| Tranh chấp về Lord Haart | Xung đột hai phía **trích được cả hai**, đúng nghĩa `DISPUTED` |
| Thant không có quan hệ với Sandro | Wiki khẳng định **chủ động** ("does not appear in the story text of any campaign levels"), không phải suy từ im lặng |
| Armor of the Damned có **4** spell | Verifier còn tìm được **nguồn gốc của lỗi "5 spell"**: một đoạn fan-opinion nói "potentially 5 spells in a single turn" (4 của armor + 1 của hero) — người đọc nhanh nhầm thành 5 |
| Specialty Sorcery kém phù hợp là ý kiến fan | Verifier xác nhận nó nằm **trong** wrapper `{{user commentary}}` của wiki |

---

## Nhận xét về chính luồng kiểm định

**Điều luồng này làm tốt:** bắt được ba claim **phủ định** sai. Cả ba cùng một dạng —
"không tồn tại", "không tìm được", "không xác nhận được" — đưa ra quá sớm.

Đây là loại lỗi nguy hiểm hơn claim khẳng định sai, vì nó **trông giống sự cẩn trọng**.
Ghi "không có nguồn" nghe như đang trung thực, trong khi thực chất chỉ là chưa tìm đủ.

**Điều luồng này không làm được:** cả người viết và verifier đều fetch cùng một hệ nguồn.
Nếu cả cộng đồng Heroes truyền nhau một thông tin sai, luồng này không phát hiện được.
Đây là hạn chế cấu trúc đã ghi ở `VERIFY-PROTOCOL.md` mục 7.

**Một hạn chế mới phát hiện:** `homm.miraheze.org` chặn bot trong cả hai đợt. Có thể đây
là nguồn của một số claim đang lưu hành mà dự án không kiểm được.

---

## Điều kiện `verified`

Theo `VERIFY-PROTOCOL.md` mục 3: không còn `BLOCKER`, không còn `MAJOR`.

- 3 `BLOCKER` → đã xử lý
- 3 `MAJOR` → đã xử lý
- 4 `MINOR` → đã xử lý
- Sai sót tier → đã xử lý

**Kết luận: đủ điều kiện `status: verified`.**

Kèm điều kiện: bài vẫn mang hạn chế nền tảng `T1*` (bản chép fan wiki, không phải file
game gốc) và 5 câu hỏi mở. `verified` nghĩa là **đã qua kiểm định theo quy trình**, không
phải "hoàn hảo".
