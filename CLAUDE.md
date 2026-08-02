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
python3 tools/check.py           # kiểm toàn vẹn — PHẢI 0 lỗi trước khi push
python3 tools/check.py --next    # entity nào được nhắc nhiều nhất mà chưa viết
python3 tools/wikilinks.py --check   # liệt kê liên kết treo
python3 tools/wikilinks.py --build   # sinh _build/ cho MkDocs
```

---

## Quy trình

Viết entity mới: dùng `/heroes-entity <tên>`. Nó chạy đủ sáu bước của
`docs/00-foundation/WORKFLOW.md`.

Xuất bản: dùng skill `heroes-publish`. Chỉ push khi entity đã `verified` và
`check.py` 0 lỗi.

**Không tự ý push** nội dung `draft` lên `main` — `main` là thứ Pages phục vụ.

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

**Quan hệ:** chỉ khai **một chiều**; công cụ sinh chiều nghịch đảo. Khai cả hai chiều
sẽ bị `check.py` cảnh báo, và nếu hai bên gán độ chắc khác nhau thì đó là **lỗi**.

---

## Trạng thái

Giai đoạn 1 (xây nền) đã xong. Codex có 3 entity `verified` trên 3 loại schema khác
nhau. Saga chưa bắt đầu — theo `SAGA-STYLE.md` S6, chỉ được viết khi entity Codex liên
quan đã `verified`.

Việc còn tồn: `docs/00-foundation/BACKLOG.md`. Ưu tiên cao nhất là `B-001` — nâng
`T1*` lên `T1` thật bằng cách trích text từ file game gốc.
