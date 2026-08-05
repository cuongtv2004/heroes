# Heroes Codex & Saga — hướng dẫn cho Claude

Bách khoa toàn thư tiếng Việt về Heroes of Might and Magic Old Universe, xuất bản qua
GitHub Pages bằng MkDocs Material.

---

## Ba luật không được phá

**1. Trí nhớ không phải nguồn.**
Không claim nào trong Codex được chống lưng bằng "theo tôi biết" — kể cả với người, kể
cả với AI. Không fetch được nguồn thì claim đó là `UNVERIFIED` và không được vào thân bài.

**2. Không tự kiểm bài của mình.**
Mọi entity phải qua luồng verify độc lập: một agent riêng, **không đọc bài gốc**, mặc
định coi mọi claim là sai. Xem `docs/00-foundation/VERIFY-PROTOCOL.md`.

**3. Mọi khẳng định có nhãn hai trục.**
`{T1* EXPLICIT: source-key}` — cấp nguồn (T1–T6) tách rời độ chắc
(EXPLICIT/INFERENCE/DISPUTED/FAN_THEORY/UNVERIFIED).

---

## Bố cục

```
docs/                 ← MkDocs xuất bản từ đây
  index.md
  00-foundation/      Tài liệu nền — CANON-POLICY có quyền cao nhất
  codex/              Bài viết, chia theo 12 loại entity
  sources/
    REGISTRY.md       Sổ nguồn — mọi source key phải có ở đây
    raw/              Dossier research thô (không xuất bản)
    notes/            Báo cáo kiểm định
  saga/               Chưa bắt đầu
tools/
  check.py            Kiểm toàn vẹn 3 tầng
  wikilinks.py        [[wikilink]] → link Markdown, sinh _build/
.claude/
  commands/           /heroes-entity
  skills/             heroes-publish
_build/ _site/        Sinh tự động, KHÔNG commit
```

**Lưu ý:** MkDocs đọc `_build/`, không đọc `docs/` trực tiếp. Luôn chạy
`python3 tools/wikilinks.py --build` trước khi `mkdocs build`.

---

## Lệnh thường dùng

```bash
python3 tools/check.py           # kiểm toàn vẹn dữ liệu — PHẢI 0 lỗi trước khi push
python3 tools/check.py --next    # entity nào được nhắc nhiều nhất mà chưa viết
python3 tools/wikilinks.py --check   # liệt kê liên kết treo
python3 tools/wikilinks.py --build   # sinh _build/ cho MkDocs
.venv/bin/mkdocs build --strict  # kiểm cấu trúc site
python3 tools/lint_site.py       # kiểm hiển thị — markup lọt ra thành chữ thô
```

⚠️ **`mkdocs` KHÔNG có trên PATH — nó nằm trong `.venv/`.** Gõ `mkdocs` trơn sẽ ra
`command not found`, và điều đó **không** có nghĩa là máy thiếu mkdocs. Đừng kết luận
"cửa A3 không chạy được" rồi dừng lại hỏi user; dùng `.venv/bin/mkdocs`.

**Ba lớp kiểm, mỗi lớp bắt loại lỗi khác nhau — không thay thế nhau được:**

| Công cụ | Bắt gì |
|---|---|
| `check.py` | Dữ liệu: source key ma, quan hệ sai, mâu thuẫn giữa hai bài |
| `mkdocs build --strict` | Cấu trúc site: link hỏng, anchor không tồn tại |
| `lint_site.py` | Hiển thị: icon/wikilink/admonition lọt ra thành chữ thô |

Lớp thứ ba tồn tại vì có tiền lệ: cú pháp icon hiện thành chữ trên site thật mà
**build vẫn báo thành công**.

---

## Quy trình

Viết entity mới: dùng `/heroes-entity <tên>`. Nó chạy đủ sáu bước của
`docs/00-foundation/WORKFLOW.md`.

Xuất bản: dùng skill `heroes-publish`. **Định nghĩa đầy đủ điều kiện push ở
`docs/00-foundation/WORKFLOW.md` bước 7.**

Tóm lại, push cần thỏa **hai** phần độc lập:

- **A — cửa chặn kỹ thuật:** `check.py` 0 lỗi · `check.py --publish-gate` (mọi bài
  `verified`) · `mkdocs build --strict` · `lint_site.py --strict`.
- **B — thẩm quyền:** user **yêu cầu** push, hoặc đã cho phép trước với phạm vi rõ.

✅ **Cho phép thường trực của dự án (user đặt 2026-08-03):**

> **"Entity nào `verified` thì push luôn, không cần hỏi."**

Nghĩa là entity đạt `verified` + bốn cửa xanh → **push, không hỏi**. Không cần chờ dồn.
Lần push đó đi kèm mọi thay đổi đang chờ (tooling, tài liệu, registry) — bình thường,
vì A2 đã bảo đảm không có bài `draft` nào lọt lên.

⚠️ **Cho phép này làm Phần B nhẹ đi, KHÔNG làm nhẹ Phần A.** Bốn cửa vẫn phải chạy
**mỗi lần** và vẫn phải xanh.

**Vẫn phải hỏi khi:** còn bài `draft`/`needs-rework` trong cây · một cửa Phần A không
chạy được (ví dụ thiếu `mkdocs`) · thay đổi động tới `mkdocs.yml`, `.github/workflows/`,
`tools/` mà chưa build thử được · bất kỳ `--force` hay sửa lịch sử đã push.

---

## ⚠️ Giới hạn tài nguyên — TỐI ĐA 2 AGENT SONG SONG

Máy dev là WSL2 trên host ~16 GB RAM. **Không được chạy quá 2 agent cùng lúc.**

Tiền lệ (2026-08-03): chạy 4 agent song song (3 verify + 1 research) làm `VmmemWSL`
phình lên **7,6 GB RAM và 432 MB/s disk** — treo cả máy Windows, phải bỏ dở toàn bộ
bốn luồng.

**Vì sao không có cách nào khác:** agent không phải process riêng biệt — chúng là các
lượt gọi API trong cùng một process, và mọi việc chúng sinh ra (curl, python, đọc/ghi
file) chạy trong **một** VM WSL2 dùng chung pool. **Không thể giới hạn tài nguyên cho
từng agent.** Chỉ điều khiển được **số luồng song song**.

Quy tắc thực hành:

- Verify nhiều bài → chạy **tuần tự**, từng bài một. Không gom thành nhiều luồng song song.
- Research + verify → **không chạy đồng thời**. Xong cái này mới tới cái kia.
- Bảng claim lớn (>50 claim) → chia theo `PRIORITY` trong prompt, không chia thành nhiều agent.

Lưới an toàn tầng hệ thống: `C:\Users\cuongtv\.wslconfig` đặt trần
`memory=6GB` · `processors=6` · `autoMemoryReclaim=gradual` · `sparseVhd=true`.
Sửa file đó phải `wsl --shutdown` mới có hiệu lực.

---

## Ba bài học đã trả giá để có

Cả ba đều tương ứng với lỗi thật đã lọt vào Codex rồi bị luồng kiểm định bắt.

**BH-1 — Text nằm trong block `==== Events ====`.**
Không chỉ prologue/epilogue. Một đợt research kết luận sai rằng cả một tuyến truyện
"không tồn tại" vì chỉ đọc prologue.

**BH-2 — Kiểm trang disambiguation trước mọi claim phủ định.**
"Sandro không xuất hiện ở game MM RPG nào khác" là **sai** — có `Sandro (Xeen)`, và
sprite nhân vật đó chính là gốc portrait Sandro Enroth.

**BH-3 — Với HotA, dùng changelog, không dùng trang artifact.**
Trang artifact gộp nhầm hai phiên bản. Và giá trị Necromancy đã đổi hai lần qua các
bản — mọi con số gameplay phải ghi rõ phạm vi phiên bản.

**Bài học lớn nhất:** ba claim bị phản bác đều là claim **phủ định** ("không tồn tại",
"không tìm được"). Loại lỗi này nguy hiểm hơn claim khẳng định sai vì **nó trông giống
sự cẩn trọng**. Sai lầm nặng nhất: kết luận "không có developer commentary nào" —
trong khi phỏng vấn Lead Designer nằm ngay trên wiki đang dùng.

---

## Quy ước viết

**Tiếng Việt, giữ nguyên tên riêng tiếng Anh.**
✅ "Sandro nắm giữ Cloak of the Undead King" · ❌ "Áo Choàng Vua Bất Tử"
Lý do: người chơi lâu năm tra cứu bằng tên gốc.

**Commit message:** tiếng Việt **không dấu**. Dòng đầu nói cái gì thay đổi; thân nói vì
sao, và ghi lại phát hiện đáng chú ý nếu có. Kết thúc bằng
`Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>`.

**Liên kết chéo:** `[[entity-id]]`, kể cả tới bài chưa viết — chúng render thành chữ
nghiêng có tooltip, không phải link chết.

**Quan hệ:** chỉ khai **một chiều**. `wikilinks.py --build` sinh chiều nghịch đảo thành mục
*Quan hệ nghịch đảo* trong `_build/` — **không bao giờ** ghi vào `docs/`. Khai cả hai chiều
sẽ bị `check.py` cảnh báo, và nếu hai bên gán độ chắc khác nhau thì đó là **lỗi**.

⚠️ Lời hứa này **mới thành thật từ 2026-08-04**. Trước đó `CLAUDE.md` và `check.py` đều nói
"công cụ sinh chiều nghịch đảo" nhưng **không công cụ nào sinh gì cả** — chiều nghịch chỉ đơn
giản không hiện ra. Xem `B-017`.

---

## Trạng thái

Giai đoạn 1 (xây nền) đã xong. Codex có **15/15 entity `verified`** trên 5 loại schema khác
nhau (`hero` ×6, `artifact` ×5, `event` ×2, `character` ×1, `kingdom` ×1). Saga chưa bắt đầu —
theo `SAGA-STYLE.md` S6, chỉ được viết khi entity Codex liên quan đã `verified`.

✅ **`B-016` (cân bằng kỷ nguyên) ĐÃ XONG 2026-08-04** — cả bốn entity trụ đều `verified`:
`archibald-ironfist` (Age of Kings), `gauldoth-half-dead` (Axeoth), `tarnum` (xuyên kỷ),
`the-reckoning` (ranh giới Enroth → Axeoth).

✅ **`B-017` cũng xong** — convention cho loại `event` đã vào `SCHEMA.md` mục 5, `wikilinks.py --build`
thật sự sinh *Quan hệ nghịch đảo*, và `codex/events/` đã có **hai** bài `verified`.

Việc còn tồn: `docs/00-foundation/BACKLOG.md`. Ưu tiên cao nhất vẫn là `B-001` — nâng
`T1*` lên `T1` thật. **Đường vào đã đổi:** không còn chỉ trông vào file `.h3c` nữa, vì bộ tài liệu
Bullard ở UT Austin có **44 file text campaign SoD ở dạng nguồn** (`B-002`).

**Hai việc lớn nhất hiện tại đều CẦN USER, không cần thêm công cụ:**

| # | Việc | Cần gì |
|---|---|---|
| `B-002` | Nội dung `Heroes.zip` (21,7 MB) trả **401** — manifest đã lấy, biết rõ bên trong có gì | User quyết định có liên hệ Dolph Briscoe Center (số hiệu `2012-212`) hay dùng luồng "Request a Copy" |
| `B-025` | FortiGuard chặn **mọi** nguồn official qua wayback | Một mạng khác (hotspot/VPN) để fetch **một lô 63 URL đã có sẵn timestamp** |

**Bốn điều phải biết trước khi viết bài mới:**

1. 🔴 **`web.archive.org` — nội dung BỊ CHẶN từ 2026-08-04.** FortiGuard chặn theo **domain đích**
   (`3do.com`, `heroesofmightandmagic.com` xếp category "Games"), **không** phải rate limit và
   **không** phải chặn archive.org. CDX index vẫn chạy → vẫn enumerate được, chỉ không đọc được.
   ⚠️ **Bẫy im lặng:** trang chặn trả **HTTP 200**, **~35,3 KB** HTML, strip tag còn **~370 ký tự** —
   `curl` báo thành công. Nhận diện bằng **kích thước + grep chữ `FortiGuard`**, đừng nhận diện bằng
   mã HTTP. Xem `B-025`.
   *(Ghi chú cũ ở đây từng nói "KHÔNG bị chặn" — đúng vào 2026-08-03, sai từ 2026-08-04.)*
2. ⚠️ **thelazy chép trung thực nhưng KHÔNG luôn chép đúng.** Đã bắt được nó ghi sai hai con số năm
   so với manual chính thức. Mọi mốc niên đại 1165–1169 phải đối chiếu nguồn 3DO — **hiện không đối
   chiếu được**, xem mục 1.
3. ⚠️ **Trang artifact/hero trên thelazy KHÔNG chứa danh sách scenario** (660–1.718 byte). Mọi bảng
   "Xuất hiện trong game" phải dựng bằng `api.php?action=query&list=backlinks`, dẫn **key riêng cho
   từng dòng**, và đọc `| source =` để ghi đúng sản phẩm.
4. 🔴 **`list=search` của thelazy KHÔNG dùng được cho claim phủ định** — index bị cũ, đã đo được
   `0 hit` cho một cụm nằm ngay trên trang đang xét. Enumerate bằng `list=categorymembers` /
   `list=allpages` rồi grep tại chỗ. Đây là **V5** của `VERIFY-PROTOCOL.md`.

Nguồn đáng khai thác tiếp: `fulton-names-2023` (`T4`, ~200 câu hỏi — `B-020`),
`ray-interview-ubisoft-2015` (`T4` cho kỷ Axeoth — `B-024`), `h3wiki-artraits-txt` (`T1` thật),
và **214 trang manual in `T2*`** mở được trong đợt 2026-08-04.
