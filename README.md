# Heroes Codex & Saga

Bộ tài liệu tiếng Việt về **Heroes of Might and Magic – Old Universe**
(Heroes I–IV, Heroes Chronicles, Might and Magic I–VIII).

📖 **[Đọc bản web →](https://cuongtv2004.github.io/heroes/)**

---

## Hai sản phẩm, một nền dữ liệu

- **Heroes Codex** — bách khoa toàn thư để tra cứu. Đây là **nền tảng**.
- **Heroes Saga** — sử thi tiểu thuyết hóa. Xây **dựa trên** Codex. *Chưa bắt đầu.*

> Codex là *sự thật của thế giới*. Saga là *câu chuyện được kể từ sự thật đó*.

---

## Ba nguyên tắc

**1. Mọi thông tin có nhãn nguồn.** Mỗi khẳng định ghi rõ đến từ đâu (`T1`–`T6`) và chắc
chắn đến mức nào (`EXPLICIT` / `INFERENCE` / `DISPUTED` / `FAN_THEORY`).

**2. Trí nhớ không phải nguồn.** "Theo tôi biết" không phải nguồn — kể cả với người, kể
cả với AI.

**3. Người viết không tự kiểm bài của mình.** Mọi bài qua luồng kiểm định độc lập, do một
agent riêng chạy, **không đọc bài gốc**, mặc định coi mọi claim là sai.

---

## Bố cục

```
docs/                    Nội dung xuất bản
  00-foundation/         Tài liệu nền — đọc trước khi đóng góp
  codex/                 Bài viết, 12 loại entity
  sources/               Sổ nguồn, dossier thô, báo cáo kiểm định
  saga/                  Chưa bắt đầu
tools/
  check.py               Kiểm toàn vẹn 3 tầng
  wikilinks.py           [[wikilink]] → link Markdown
.claude/                 Skill và slash command cho Claude Code
```

---

## Chạy tại chỗ

```bash
pip install -r requirements.txt

python3 tools/check.py              # kiểm toàn vẹn Codex
python3 tools/check.py --next       # entity nào nên viết tiếp
python3 tools/wikilinks.py --build  # sinh _build/
mkdocs serve                        # xem thử tại localhost:8000
```

CI chạy `check.py` trước khi build — site không được deploy từ Codex có lỗi cấu trúc.

---

## Trạng thái

**Giai đoạn 1 — Xây nền: xong.** Sáu tài liệu nền, sổ nguồn 77 key, công cụ kiểm 3 tầng.

Codex có **3 entity `verified`** trên 3 loại schema:
[Sandro](docs/codex/heroes/sandro.md) ·
[Ethric](docs/codex/characters/ethric.md) ·
[Cloak of the Undead King](docs/codex/artifacts/cloak-of-the-undead-king.md)

---

## Hạn chế — nói thẳng

Toàn bộ text in-game trong Codex mang tier **`T1*`**: bản chép của fan wiki, **không phải
file game gốc**.

Vẫn tin ở mức cao vì wiki nguồn chép nguyên cả lỗi chính tả trong game và đánh dấu bằng
`{{sic}}` — dấu hiệu bản chép trung thực. Nhưng vẫn cách nguồn gốc một bước.

Xem [`BACKLOG.md`](docs/00-foundation/BACKLOG.md) `B-001`.

---

## Đóng góp

Đọc theo thứ tự: [CANON-POLICY](docs/00-foundation/CANON-POLICY.md) →
[SCHEMA](docs/00-foundation/SCHEMA.md) →
[VERIFY-PROTOCOL](docs/00-foundation/VERIFY-PROTOCOL.md) →
[WORKFLOW](docs/00-foundation/WORKFLOW.md).

`CANON-POLICY.md` có quyền lực cao nhất — bài viết nào xung đột với nó thì bài viết sai.

---

## Giấy phép

Heroes of Might and Magic là tài sản của Ubisoft. Đây là tài liệu phi thương mại do người
hâm mộ biên soạn. Nội dung do dự án viết: CC BY-SA 4.0.
