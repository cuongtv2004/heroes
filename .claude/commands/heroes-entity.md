---
description: Research, viết và kiểm định một entity Codex mới (chống bịa nguồn)
argument-hint: <tên entity> [loại: hero|character|artifact|kingdom|...]
allowed-tools: Read, Write, Edit, Bash, Agent, TodoWrite, Glob, Grep
---

# Viết entity Codex: $ARGUMENTS

Chạy đủ sáu bước của `docs/00-foundation/WORKFLOW.md`. **Không bỏ bước 5 (verify).**

---

## Trước khi bắt đầu — đọc nền tảng

Đọc các tài liệu này nếu chưa có trong ngữ cảnh phiên làm việc:

- `docs/00-foundation/WORKFLOW.md` — sáu bước và ba bài học kỹ thuật
- `docs/00-foundation/CANON-POLICY.md` — hệ thống nhãn hai trục, thứ tự ưu tiên nguồn
- `docs/00-foundation/SCHEMA.md` — frontmatter và khung thân bài cho loại entity này
- `docs/sources/REGISTRY.md` — nguồn đã có, và các **cảnh báo** đã ghi

Kiểm luôn `docs/00-foundation/TIMELINE-SPINE.md`: nếu entity này có mốc thời gian,
nó phải khớp xương sống hiện có — và nếu nó **mang mốc mới**, phải cập nhật ngược
lại vào timeline ở bước cuối.

---

## Bước 1 — Research (chạy subagent)

Dùng `Agent` với `subagent_type: general-purpose`. Prompt **bắt buộc** chứa:

**Access notes**

```
- heroes.thelazy.net raw wikitext: https://heroes.thelazy.net/index.php?title=PAGE&action=raw
  WebFetch tóm tắt thay vì trả nguyên văn — dùng curl khi cần chính xác từng chữ.
- Fandom chỉ vào được qua API:
  https://mightandmagic.fandom.com/api.php?action=parse&page=PAGE&prop=wikitext&format=json&formatversion=2
- web.archive.org VÀO ĐƯỢC (ghi chú cũ "bị chặn" là SAI, sửa 2026-08-03).
  Phải dùng curl -L và TIMESTAMP ĐẦY ĐỦ: web.archive.org/web/YYYYMMDDhhmmss/<url>
  Dạng /web/2005/<url> hay trả trang wrapper rỗng ~2KB. API wayback/available trả 429
  (rate limit), KHÔNG phải chặn.
  → Đây là đường vào site chính thức NWC/3DO, nguồn không-phải-wiki tốt nhất có thể có.
    Ví dụ đã dùng được: 3do.com/products/pc/mm7/story/story.htm (Diaries of Archibald, T2).
- homm.miraheze.org chặn bot (403). Và nó là FORK byte-identical của thelazy —
  không phải nguồn xác nhận độc lập.
- thelazy chép trung thực nhưng KHÔNG luôn chép ĐÚNG: đã bắt được nó ghi sai hai con số
  năm so với manual chính thức. Mọi mốc niên đại 1165–1169 phải đối chiếu nguồn 3DO.
- Trang artifact/hero trên thelazy KHÔNG chứa danh sách scenario (660–1.718 byte).
  Phải quét api.php?action=query&list=backlinks&bltitle=PAGE&bllimit=500 rồi đọc
  `| source =` của từng trang scenario để biết sản phẩm (RoE/AB/SoD/HotA/Chronicles).
- Bẫy {{swh|A|B}}: tham số ĐẦU là HotA, tham số SAU là SoD. Đọc trái-sang-phải là sai.
- Mọi claim về HotA: dùng CHANGELOG, không dùng trang artifact.
  https://heroes.thelazy.net/index.php?title=Horn_of_the_Abyss_(Changelog)&action=raw
```

**Ba bài học kỹ thuật** (viết thẳng ra, không tóm tắt — cả ba đã từng gây lỗi thật):

1. Text nằm trong block `==== Events ====` (map event theo tọa độ), **không chỉ**
   prologue/epilogue. Đọc **toàn bộ** trang scenario.
2. Kiểm **trang disambiguation** trước mọi claim "không xuất hiện ở đâu khác".
3. Claim phủ định phải **săn chủ động**, không được suy từ im lặng.

**Quy tắc bắt buộc**

```
- Gắn nhãn từng mục: đã fetch-và-đọc vs. trí nhớ mô hình.
  Nếu chưa fetch: "NOT FETCHED — unverified".
- KHÔNG BAO GIỜ bịa trích dẫn hay số liệu.
- Đánh dấu claim nào của wiki không dẫn nguồn.
- Phân biệt game text với văn wiki — đây là phân biệt quan trọng nhất.
- "Không tìm thấy" là câu trả lời hợp lệ.
```

Yêu cầu trả về: dossier + `SOURCE LIST` + `GAPS` + `SUSPECTED WIKI-ONLY CLAIMS`.

**Với entity lớn:** đánh số `PRIORITY 1..N` và dặn *"report what you have even if you
run out of time"* — một luồng đã từng chết vì lỗi API, chia ưu tiên thì vẫn thu được
phần đầu.

Lưu kết quả vào `docs/sources/raw/<id>-dossier-<YYYY-MM-DD>.md`.

---

## Bước 2 — Cập nhật registry

Thêm mọi source key mới vào `docs/sources/REGISTRY.md`:

- Tier đúng (`T1*` cho text in-game qua fan wiki — **không phải** `T1`)
- Ghi rõ `FETCHED` / `FAILED` / `NOT_FETCHED`
- **Ghi cảnh báo** nếu nguồn có vấn đề đã phát hiện

Bio hero từ `HEROBIOS.TXT` là **`T1*`**, không phải `T2*` — đó là file dữ liệu
in-game, không phải manual in.

---

## Bước 3 — Viết bài

`docs/codex/<loại>/<id>.md`, theo đúng khung ở `SCHEMA.md`. Bắt đầu với
`status: draft`.

**Kiểm tra khi viết:**

- Mọi khẳng định có nhãn `{Tn ĐỘCHẮC: source-key}`
- Quan hệ nghịch đảo **chỉ khai một chiều** (công cụ sinh chiều còn lại)
- `DISPUTED` thì trình bày **cả hai phía**, không chọn ngầm
- `FAN_THEORY` tách sang mục riêng, không trộn vào tiểu sử
- Mục *Câu hỏi mở* ghi thật những gì chưa trả lời được
- Con số gameplay **ghi rõ phạm vi phiên bản** (SoD? HotA nào?)

Liên kết chéo bằng `[[entity-id]]` — kể cả tới bài chưa viết.

---

## Bước 4 — Kiểm máy

```bash
python3 tools/check.py
```

**Phải 0 lỗi** mới đi tiếp. Cảnh báo "bài chưa tồn tại" là bình thường.

---

## Bước 5 — Verify độc lập (KHÔNG BỎ QUA)

Đây là bước khiến Codex đáng tin. Cả ba entity đầu tiên đều có lỗi mà **chỉ** bước
này bắt được.

**5a.** Trích claim ra bảng, lưu vào scratchpad (không lưu trong repo):

```
| # | Claim | Label |
|---|-------|-------|
| X-01 | <claim bằng TIẾNG ANH> | T1* EXPLICIT |
```

Viết claim bằng **tiếng Anh** — verifier làm việc với nguồn tiếng Anh. Tách đủ nhỏ
để mỗi claim đúng/sai độc lập.

**5b.** Chạy `Agent` verify. Prompt **bắt buộc** có ba quy tắc chống tự-xác-nhận:

```
1. Bạn CHƯA đọc bài viết mà các claim này lấy ra, và KHÔNG được tìm đọc.
   Không đọc bất cứ thứ gì trong /home/cuongtv/heroes/.
   Bảng claim là input DUY NHẤT.
2. Mặc định MỌI claim là SAI cho tới khi tìm được nguồn.
   Nhiệm vụ là PHẢN BÁC, không phải xác nhận.
3. Phải TRÍCH được nguyên văn. Không trích được thì không thể là EXPLICIT.
```

Bốn phán quyết đóng: `CONFIRMED` / `DOWNGRADE` / `NOT_FOUND` / `CONTRADICTED`.
Không có "có lẽ đúng".

Mức nghiêm trọng: `BLOCKER` / `MAJOR` / `MINOR` / `NOTE`.

**Đánh dấu riêng các claim rủi ro cao** — đặc biệt claim **phủ định** và claim gán
`EXPLICIT` cho điều chỉ suy ra được. Ghi rõ *"load-bearing, try hard to refute"*.

---

## Bước 6 — Xử lý và đóng

Với mỗi phát hiện, chỉ có **ba** cách phản hồi hợp lệ:

1. Sửa bài theo phán quyết
2. Đưa nguồn mới — phải là URL fetch được, kèm trích nguyên văn
3. Chuyển claim xuống *Câu hỏi mở* hoặc *Giả thuyết cộng đồng*

**Không hợp lệ:** "tôi khá chắc là đúng", "trong game có mà".

Nếu verifier hạ nhãn của bạn — **thường là nó đúng**. Đã có tiền lệ: claim
"bị game text phản bác" bị hạ xuống `INFERENCE`, và verifier còn tìm được bằng
chứng mạnh hơn mà research bỏ sót.

Sau khi hết `BLOCKER` và `MAJOR`:

- Lưu báo cáo: `docs/sources/notes/verify-<id>-<YYYY-MM-DD>.md`
- Đặt `status: verified` + `verify_pass: <ngày>`
- Chạy lại `python3 tools/check.py` — **Tầng 3 giờ có thể phát hiện mâu thuẫn với
  bài khác**. Nếu có, sửa và cân nhắc đặt bài liên quan về `needs-rework`.
- Cập nhật `docs/00-foundation/TIMELINE-SPINE.md` nếu có mốc thời gian mới
- Cập nhật `docs/codex/index.md` và `nav:` trong `mkdocs.yml`
- Nếu phát hiện việc cần đào sâu: ghi vào `docs/00-foundation/BACKLOG.md`

---

## Bước 7 — Rà site

Bài mới có thể làm hỏng phần hiển thị mà `check.py` không thấy — `check.py` kiểm
**dữ liệu**, không kiểm **giao diện**.

**7a. Kiểm tự động** (luôn chạy, rẻ):

```bash
python3 tools/wikilinks.py --build
mkdocs build --strict
python3 tools/lint_site.py
```

`lint_site.py` bắt loại lỗi mà `mkdocs build` **không** bắt: markup lọt ra ngoài
thành chữ thô. Đã có tiền lệ — cú pháp icon `:material-xxx:` hiện thành chữ trên
site thật, build vẫn báo thành công, chỉ nhìn bằng mắt mới thấy.

Nếu chưa cài mkdocs tại chỗ, bỏ qua và **nói rõ với user** rằng CI sẽ bắt.

**7b. Agent rà định kỳ** — chạy khi:

- Sửa `mkdocs.yml`, `nav:`, hoặc thêm loại entity mới
- Thêm cú pháp Markdown chưa dùng bao giờ (icon, tab, grid, biểu đồ)
- Mỗi ~5 entity mới, kể cả khi không có gì bất thường

Dùng `Agent` với `subagent_type: general-purpose`, prompt yêu cầu rà:

| Ưu tiên | Rà gì |
|---|---|
| P1 | Markup lọt ra thành chữ thô — icon, template, admonition, wikilink, attribute list, `grid cards` thiếu `<ul>` |
| P2 | Link và anchor hỏng; trang tồn tại nhưng **không có trong `nav:`** (mồ côi); mục `nav:` trỏ file không tồn tại |
| P3 | Tiếng Việt — search index có index được dấu không, anchor có đụng slug không, có mojibake không |
| P4 | Frontmatter lọt ra thành chữ; bảng dài có cuộn được không; CSS có nạp không |
| P5 | Extension dùng trong nội dung nhưng **chưa khai** trong config (âm thầm không render) |

Ghi rõ trong prompt: **read-only, không sửa file**, và **không báo cáo ý kiến thẩm
mỹ** — chỉ báo thứ hỏng, gây hiểu sai, không truy cập được, hoặc sẽ vỡ khi Codex
lớn lên.

Cũng dặn: *"nếu thấy có vẻ sai nhưng kiểm ra vẫn render đúng thì nói rõ, đừng báo
— dương tính giả tốn thời gian."*

**7c. Cập nhật `nav:`** trong `mkdocs.yml` cho bài mới. Bài không có trong `nav:`
vẫn build được nhưng **không ai tìm thấy từ sidebar**.

---

## Bước 8 — Xuất bản

Dùng skill `heroes-publish`. Nó có cửa chặn riêng và sẽ từ chối push nếu còn lỗi.

---

## Nhắc cuối

Điều làm dự án này khác một wiki **không phải** là viết hay hơn — mà là **nói rõ
mình biết chắc đến đâu**. Khi phân vân giữa một câu văn đẹp và một nhãn chính xác,
**chọn nhãn**.
