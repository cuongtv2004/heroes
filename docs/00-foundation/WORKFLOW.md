# WORKFLOW

Quy trình viết một entity Codex, rút ra từ ba entity đầu tiên.

Tài liệu này tồn tại vì các bài học dưới đây **đã phải trả giá để có** — mỗi cái tương
ứng với một lỗi thật đã lọt vào Codex rồi bị luồng kiểm định bắt.

---

## Bảy bước

```
1. Research          → sources/raw/<entity>-dossier-<ngày>.md
2. Cập nhật registry → sources/REGISTRY.md
3. Viết bài          → codex/<loại>/<id>.md, status: draft
4. Kiểm máy          → python3 tools/check.py  (phải 0 lỗi)
5. Verify độc lập    → sources/notes/verify-<entity>-<ngày>.md
6. Xử lý + verified  → sửa hết BLOCKER/MAJOR, đặt status: verified
7. Xuất bản          → CHỈ khi có đủ cửa chặn VÀ có người cho phép (xem dưới)
```

**Không được bỏ bước 5.** Cả ba entity đầu tiên đều có lỗi mà chỉ luồng kiểm định bắt được.

**Bước 1–6 làm được không cần hỏi ai. Bước 7 thì không.**

---

## Bước 7 — Khi nào được push lên `main`

`main` là thứ GitHub Pages phục vụ cho người đọc. Push là hành động **hướng ra ngoài** và
**khó thu hồi** — nội dung đã lên Pages có thể bị cache hoặc index kể cả sau khi xóa.

Điều kiện push gồm **hai phần độc lập**, phải thỏa **cả hai**:

### Phần A — Cửa chặn kỹ thuật (cần, nhưng CHƯA đủ)

Bốn cửa, chạy đúng thứ tự này:

| # | Lệnh | Yêu cầu |
|---|---|---|
| A1 | `python3 tools/check.py` | **0 lỗi.** Cảnh báo "bài chưa tồn tại" là bình thường |
| A2 | `python3 tools/check.py --publish-gate` | **Mọi** bài phải `verified`. Một bài `draft` là dừng |
| A3 | `python3 tools/wikilinks.py --build && mkdocs build --strict` | Không lỗi cấu trúc |
| A4 | `python3 tools/lint_site.py --strict` | Không markup lọt ra thành chữ thô |

A2 áp cho **toàn bộ cây**, không chỉ bài sắp push. Một bài `draft` ở chỗ khác vẫn chặn — vì
nó cũng sẽ lên Pages. Lý do có luật này: đã có tiền lệ 6 bài `draft` bị đẩy lên `main`.

A4 tồn tại vì `mkdocs build --strict` **không** bắt được loại lỗi đó — icon `:material-xxx:`
từng hiện thành chữ trên site thật mà build vẫn báo thành công.

### Phần B — Thẩm quyền (cần, và đây là phần hay bị bỏ qua)

> **Bốn cửa xanh KHÔNG phải là lệnh push. Nó chỉ có nghĩa là push sẽ không làm hỏng site.**

Push cần **người dùng cho phép**, và sự cho phép đó phải thuộc một trong ba dạng:

1. **Yêu cầu trực tiếp** — "push đi", "đẩy lên", "xuất bản", "publish", hoặc gọi skill
   `heroes-publish`.
2. **Cho phép trước có phạm vi rõ** — ví dụ *"làm xong entity nào thì push luôn entity đó"*.
   Phạm vi đó **hết hiệu lực** khi công việc được nêu kết thúc; nó **không** mở rộng sang
   loại thay đổi khác.
3. **Được chọn trong một câu hỏi** — nếu đã hỏi và user chọn "push", thì đó là cho phép.

### ⛔ Những thứ KHÔNG phải là lý do để push

Ghi ra vì tất cả đều nghe hợp lý:

- ❌ "Bốn cửa đều xanh" — đó là Phần A, không phải Phần B.
- ❌ "Đã dồn nhiều commit ở local, trông chưa gọn" — **dồn commit chưa push là trạng thái
  bình thường và an toàn.** Nó không phải nợ kỹ thuật, và không tự sinh ra quyền push.
- ❌ "Entity vừa đạt `verified`" — `verified` là điều kiện của Phần A, không phải giấy phép.
- ❌ "User đang ở chế độ tự động, nói làm tiếp cho tới xong" — cho phép tự động áp cho công
  việc **trong repo**. Nó **không** tự bao gồm hành động hướng ra ngoài.
- ❌ "Lần trước user đã cho push" — cho phép **không** tự động kéo sang lần sau.
- ❌ "Thay đổi chỉ là tooling / tài liệu nền, không phải bài viết" — vẫn cần Phần B, và vẫn
  phải qua A2 (vì push mang theo **toàn bộ** trạng thái cây).

**Tiền lệ (2026-08-03):** một phiên tích **12 commit** ở local — 10 entity `verified`, bốn cửa
xanh. Vẫn **không** push, vì trước đó user được hỏi và **đã không chọn** mục push. Đó là xử lý
đúng: trạng thái sạch, chờ người quyết.

### Khi nào phải DỪNG và hỏi, dù đã có Phần B

- `check.py` còn lỗi, hoặc còn bài `needs-rework` chưa xử lý
- Đang có luồng verify chạy dở cho chính entity sắp push
- Thay đổi động tới `mkdocs.yml`, `.github/workflows/`, hoặc `tools/` mà **chưa build thử được**
  tại chỗ
- Máy chưa cài `mkdocs` nên A3 không chạy được → nói rõ với user rằng chỉ CI sẽ bắt

### Nếu user chủ động muốn push nội dung chưa `verified`

Hỏi lại **một lần** để chắc chắn. Nếu user xác nhận, đó là quyết định của họ — làm, và **ghi rõ
trong commit message** rằng có bài chưa verify. Không tranh luận tiếp.

### Cách thực hiện

Dùng skill `heroes-publish` — nó chạy đúng bốn cửa trên rồi commit và push. Đừng `git push` tay,
vì như vậy sẽ bỏ qua cửa chặn.

---

## Ba bài học kỹ thuật — đưa vào MỌI prompt research

Ba lỗi này đã làm hỏng đợt research đầu tiên. Chúng **không hiển nhiên** và sẽ lặp lại nếu
không nhắc rõ.

### BH-1 — Text nằm trong block `==== Events ====`, không chỉ prologue

Đợt đầu kết luận tuyến Tyranell "không tồn tại trong game text". Sai — nó nằm trong một
**map event tại tọa độ**, không phải prologue hay epilogue.

Cùng lỗi đó làm bỏ sót:
- Map event (15,27,0) — động cơ thật của Jabarkas
- `sod-master` Day 15 — người dwarf là chủ cũ artifact
- `sod-invasion` Day 17 — cảnh dấu ngón tay xương trên ngực Finneas

**Quy tắc: đọc TOÀN BỘ trang scenario, kể cả block Events.**

### BH-2 — Kiểm trang disambiguation trước mọi claim phủ định

Đợt đầu viết "Sandro không xuất hiện ở game MM RPG nào khác". Sai — có `Sandro (Xeen)`
trong *Might and Magic V*, và **sprite của nhân vật đó chính là gốc portrait Sandro Enroth**.

Ngược lại, khi kiểm đúng cách thì claim tương tự về Ethric **đứng vững**: 7 tiêu đề trên
Fandom đều là redirect về một bài.

**Quy tắc: claim "không xuất hiện ở đâu khác" phải kiểm qua trang disambiguation + full-text
search, không chỉ trang nhân vật.**

### BH-3 — Với HotA, dùng changelog, không dùng trang artifact

Trang artifact ghi lệnh cấm HotA 1.7.2 kèm **ba** template ngoại lệ. Changelog cho thấy
1.7.2 chỉ có **hai**; cái thứ ba đến ở 1.7.3.

Nghiêm trọng hơn: **giá trị Necromancy đã đổi hai lần** (5/10/15/30% → 2,5/5/7,5/15% ở
1.3.0 → khôi phục ở 1.8.0). Trang artifact không phản ánh điều này.

**Quy tắc: mọi claim về HotA lấy từ `hota-changelog`. Mọi con số gameplay ghi rõ phạm vi
phiên bản.**

---

## Bài học lớn nhất — về claim phủ định

Đợt Sandro có **ba** claim bị phản bác. Cả ba đều cùng một dạng:

> "không tồn tại", "không tìm được", "không xác nhận được"

Đây là loại lỗi **nguy hiểm hơn** claim khẳng định sai, vì nó **trông giống sự cẩn trọng**.
Viết "không có nguồn" nghe như đang trung thực, trong khi thực chất chỉ là **chưa tìm đủ**.

Sai lầm nặng nhất: kết luận "không có developer commentary nào" — trong khi phỏng vấn
Jennifer Bullard (Lead Designer của Shadow of Death) nằm **trên chính wiki đang dùng**, cách
đúng một cú click từ trang đã đọc.

**Quy tắc: claim phủ định phải bị kiểm nghiêm như claim khẳng định.** Trong prompt verify,
luôn đánh dấu chúng là "load-bearing, try hard to refute".

Kết quả khi áp dụng: đợt Ethric + Cloak có 4 claim phủ định, **cả 4 đều đứng vững** sau khi
bị tấn công có chủ đích.

---

## Prompt research — khung chuẩn

```
Research <ENTITY> ... RESEARCH ONLY — do not write the article.

[Access notes: thelazy raw wikitext + curl, Fandom API, archive.org blocked,
 miraheze blocks bots]

[Ba bài học BH-1, BH-2, BH-3 viết thẳng ra]

Collect with exact URL + verbatim quote:
  [danh sách theo loại entity]

RULES:
- Label every item: fetched-and-read vs. model knowledge.
  If not fetched: "NOT FETCHED — unverified".
- Never invent quotes or numbers.
- Flag wiki claims that cite no source.
- Distinguish game text from wiki narration — the single most important distinction.
- "Not found" is a valid answer.

Return: dossier by section + SOURCE LIST + GAPS + SUSPECTED WIKI-ONLY CLAIMS.
```

**Với entity dài, thêm:** đánh số PRIORITY 1..N và dặn *"report what you have even if you
run out of time"*. Một luồng đã chết giữa chừng vì lỗi API — chia ưu tiên giúp thu được
phần đầu thay vì mất trắng.

---

## Prompt verify — khung chuẩn

Ba quy tắc chống tự-xác-nhận (xem `VERIFY-PROTOCOL.md`):

1. **Verifier KHÔNG đọc bài gốc.** Ghi thẳng: *"Do not read anything in /home/cuongtv/heroes/.
   The claims table is your ONLY input."*
2. **Mặc định mọi claim là SAI.** *"Your job is refutation, not confirmation."*
3. **Phải trích được nguyên văn.** *"If you cannot quote it, it cannot be EXPLICIT."*

Bốn phán quyết đóng: `CONFIRMED` / `DOWNGRADE` / `NOT_FOUND` / `CONTRADICTED`.
Không có "có lẽ đúng".

**Đánh dấu riêng các claim rủi ro cao** trong prompt — đặc biệt là claim phủ định và claim
mang nhãn `EXPLICIT` cho điều chỉ suy ra được.

---

## Bảng claim — cách trích

Verifier nhận **bảng claim**, không nhận bài viết. Mỗi dòng:

```
| # | Claim | Label |
|---|-------|-------|
| E-01 | Ethric NEVER SPEAKS a single line anywhere in Heroes III | T1* EXPLICIT |
```

Viết claim bằng **tiếng Anh** — verifier làm việc với nguồn tiếng Anh, dịch qua lại làm mất
độ chính xác.

Tách claim đủ nhỏ để mỗi cái **đúng hoặc sai độc lập**. Claim gộp hai ý sẽ nhận phán quyết
mơ hồ.

---

## Khi nào một bài mất `verified`

Đặt về `needs-rework` khi:

- Sửa nội dung thân bài sau khi đã verify
- Tầng 3 phát hiện mâu thuẫn với một bài khác
- Một nguồn được chứng minh là không đáng tin

**Ví dụ thật:** bài Sandro mất `verified` khi bài Ethric ra đời — Tầng 3 phát hiện hai bài
gán độ chắc khác nhau cho cùng quan hệ `killed`. Phục hồi sau khi luồng verify Ethric xác
nhận độc lập rằng hạ xuống `DISPUTED` là đúng.

Giữ `verify_history` trong frontmatter để không mất dấu.

---

## Thứ tự ưu tiên viết bài

Nguyên tắc: **đi theo cụm, không đi theo mức độ nổi tiếng.**

Lý do: research một cụm dùng chung nguồn. Viết Sandro xong thì Ethric, Cloak, Jeddite,
Deyja gần như đã có sẵn tư liệu — chỉ cần bổ sung.

Thứ tự đã dùng:

```
Sandro (hero)
  → Ethric (character)      — quan hệ trực tiếp, có nguồn T4
  → Cloak (artifact)        — thử loại schema mới
  → 3 thành phần Cloak      — nhỏ, dọn liên kết treo
  → Armor of the Damned     — artifact đối xứng
  → Deyja (kingdom)         — thử loại schema mới, nhiều timeline anchor
  → Jeddite (hero)          — kiểm quan hệ ba chiều
```

**Mẹo:** ưu tiên entity xuất hiện nhiều trong mục *Liên kết* của các bài đã viết. Chúng dọn
được nhiều cảnh báo "bài chưa tồn tại" nhất.

### ⚠️ Luật cân bằng kỷ nguyên — cửa chặn cho chính nguyên tắc trên

"Đi theo cụm" hiệu quả về research, nhưng **nó không có điều kiện dừng.** Chín bài đầu tiên
của Codex đều nằm trong đúng một cụm — necromancer của *Shadow of Death*. Cụm đó có thể nuốt
60–80 bài trước khi cạn, và khi đó dự án là *bách khoa về Sandro*, không phải *bách khoa Old
Universe*.

> **Trước khi một kỷ nguyên vượt quá 15 bài, mọi kỷ nguyên khác phải có ít nhất một entity
> trụ.**

Entity trụ là entity **mở được một kỷ nguyên đang trống** — nó vừa nới chiều rộng Codex, vừa
xây móng cho trục dọc của Saga.

| Kỷ nguyên | Entity trụ | Mở được gì |
|---|---|---|
| Age of Kings (H1–H2) | `archibald-ironfist` | Toàn bộ H1–H2; nối sẵn vào chuỗi Deyja (làm vua Deyja 1168) |
| Xuyên kỷ | `tarnum` | Heroes Chronicles — buộc phải giải quyết B-010 (cấu trúc Book V) |
| The Reckoning | `the-reckoning` (event) | Ranh giới Enroth → Axeoth, hiện chưa có nguồn |
| Kỷ Axeoth (H4) | `gauldoth-half-dead` | H4; dọn luôn B-007 |

**Vì sao `archibald-ironfist` đi trước:** nó là entity trụ duy nhất **vẫn dùng chung nguồn**
với cụm đã có — chuỗi kế vị Deyja đã dẫn tới hắn. Mở kỷ nguyên mới mà không mất lợi thế cụm.

**Bài học đằng sau luật này:** lệch trục không biểu hiện thành lỗi. `check.py` vẫn 0 lỗi,
mọi bài vẫn có nguồn, không luồng verify nào bắt được. Nó chỉ hiện ra khi đếm xem mỗi kỷ
nguyên có bao nhiêu bài — nên phải đếm chủ động, định kỳ.

---

## Lịch sử sửa đổi

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 2026-08-03 | Thêm **bước 7 — điều kiện push**, tách *cửa chặn kỹ thuật* khỏi *thẩm quyền* | WORKFLOW trước đó **không nhắc push một lần nào**: sáu bước kết thúc ở `verified` rồi im lặng. Điều kiện push rải ở ba nơi (CLAUDE.md, skill `heroes-publish`, không nơi nào ở đây) và **không nơi nào định nghĩa ai được quyết**. Mô tả skill còn ghi "dùng khi một entity vừa đạt `verified`" — đọc như agent được tự push |

## Lịch sử

| Ngày | Thay đổi |
|---|---|
| 2026-08-02 | Bản đầu — rút từ 3 entity đầu tiên và 3 luồng kiểm định |
