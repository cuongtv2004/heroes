#!/usr/bin/env python3
"""Bắt lỗi render của MkDocs — markup lọt ra ngoài dưới dạng chữ thô.

Lý do tồn tại: cú pháp icon `:material-book-open-variant:` đã từng hiện ra thành
chữ thô trên site thật vì thiếu extension `pymdownx.emoji`. Build vẫn báo thành
công — MkDocs không coi đó là lỗi. Chỉ nhìn bằng mắt mới thấy.

Script này bắt loại lỗi đó tự động, để không phải phát hiện bằng cách mở trình duyệt.

Chạy SAU `mkdocs build`, trên thư mục `_site/`.

Dùng:
    python3 tools/lint_site.py           # kiểm _site/
    python3 tools/lint_site.py --strict  # coi cảnh báo là lỗi (dùng cho CI)
"""

import html
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"

# Markup lẽ ra phải được xử lý, nếu còn thấy trong text hiển thị thì là lỗi.
# (mẫu, mô tả, mức)
LEAKED_MARKUP = [
    (r":material-[a-z0-9-]+:", "Cú pháp icon Material chưa render — thiếu pymdownx.emoji?", "BLOCKER"),
    (r":fontawesome-[a-z0-9-]+:", "Cú pháp icon FontAwesome chưa render", "BLOCKER"),
    (r":octicons-[a-z0-9-]+:", "Cú pháp icon Octicons chưa render", "BLOCKER"),
    (r"\[\[[a-z0-9-]+\]\]", "Wikilink chưa chuyển — tools/wikilinks.py có chạy không?", "BLOCKER"),
    (r"^\s*!!!\s+\w+", "Admonition chưa render — thiếu extension `admonition`?", "MAJOR"),
    (r"\{\s*#[a-z0-9-]+\s*\}", "Attribute list chưa render — thiếu `attr_list`?", "MAJOR"),
    (r"\{\{\s*\w+", "Cú pháp template chưa xử lý", "MAJOR"),
]

# Nhãn nguồn của Codex: {T1* EXPLICIT: key}. Đây là nội dung hợp lệ, KHÔNG phải lỗi
# — nhưng dễ bị mẫu attr_list ở trên bắt nhầm, nên loại trừ trước.
CLAIM_LABEL_RE = re.compile(r"\{T\d\*?\s+[A-Z_]+:[^}]*\}")

# Codex TRÍCH DẪN cú pháp của fan wiki khi bàn về độ tin cậy của nguồn —
# ví dụ "wiki đánh dấu lỗi in-game bằng {{sic}}" hay "đoạn này nằm trong
# {{fanopinion}}". Đây là nội dung có chủ đích, không phải template chưa xử lý.
WIKI_TEMPLATE_RE = re.compile(
    r"\{\{(sic|fanopinion|user commentary|end of user commentary|gl|cn|hn|"
    r"hota|sod|mm\d|imprisoned|player|enemy|mention|Sng|Ss2|Psg|"
    r"HeroNew|CampaignHero|DungeonHeroesNew|swh|showwithhota|inhota|wll|wh|"
    r"ArtifactNewSB|CombinationArtifactNewSB|H4Story|herobios|hero row|"
    r"appear|insod|prison|Hn|Cn|Psg)\b[^}]*\}?\}?"
)

TAG_RE = re.compile(r"<script.*?</script>|<style.*?</style>|<[^>]+>", re.S)

# Nội dung trong <code> và <pre> là thứ tác giả CỐ Ý cho hiện ra nguyên dạng —
# trích cú pháp wikitext, ví dụ lệnh, đoạn YAML. Nó không bao giờ là "markup lọt".
#
# Vì sao cần loại trừ theo TẦNG này thay vì nối thêm vào WIKI_TEMPLATE_RE: báo cáo
# kiểm định trích wikitext thô của nguồn, nên tên template là **không đóng** —
# `{{An}}`, `{{SorQrow}}`, `{{BonusArt}}`, `{{encounter row}}`, `{{map object}}`...
# Duy trì allowlist theo từng tên là cuộc đua không có đích. Còn markup lọt thật thì
# **không** nằm trong <code>: icon Material lọt ra hiện thành chữ thường giữa câu.
CODE_RE = re.compile(r"<code[^>]*>.*?</code>|<pre[^>]*>.*?</pre>", re.S)

errors: list[str] = []
warnings: list[str] = []


def visible_text(raw_html: str) -> str:
    """Lấy phần chữ người đọc thật sự nhìn thấy, bỏ thẻ và script."""
    return html.unescape(TAG_RE.sub(" ", raw_html))


def check_leaked_markup(page: Path, text: str) -> None:
    text = CLAIM_LABEL_RE.sub(" ", text)
    text = WIKI_TEMPLATE_RE.sub(" ", text)
    for pattern, desc, level in LEAKED_MARKUP:
        for m in re.finditer(pattern, text, re.MULTILINE):
            snippet = m.group(0)[:60]
            msg = f"{rel(page)}: {desc}\n      → {snippet!r}"
            (errors if level == "BLOCKER" else warnings).append(msg)
            break  # một lỗi mỗi loại mỗi trang là đủ để đi sửa


def check_degraded_cards(page: Path, raw: str) -> None:
    """`grid cards` cần <ul> lồng bên trong. Không có nghĩa là nó âm thầm hỏng."""
    for m in re.finditer(r'<div class="grid cards">(.{0,300})', raw, re.S):
        if "<ul>" not in m.group(1):
            warnings.append(
                f"{rel(page)}: `grid cards` không có <ul> lồng trong — "
                f"thẻ card đã hỏng thành div thường (thiếu dòng trống, hoặc thiếu `md_in_html`?)"
            )


def check_frontmatter_leak(page: Path, text: str) -> None:
    """Frontmatter YAML hỏng sẽ hiện thành chữ trên trang."""
    head = text[:600]
    if re.search(r"^\s*(id|type|name_vi|status|sources_used):\s", head, re.MULTILINE):
        errors.append(
            f"{rel(page)}: frontmatter lọt ra thành chữ hiển thị — "
            f"YAML có thể bị hỏng cú pháp"
        )


def check_css_loaded(page: Path, raw: str) -> None:
    if "assets/extra.css" not in raw:
        warnings.append(f"{rel(page)}: không nạp assets/extra.css")


def rel(p: Path) -> str:
    try:
        return str(p.relative_to(SITE))
    except ValueError:
        return str(p)


def main() -> int:
    strict = "--strict" in sys.argv

    if not SITE.exists():
        print(f"Chưa có {SITE.relative_to(ROOT)}/ — chạy `mkdocs build` trước.")
        return 1

    pages = sorted(SITE.rglob("*.html"))
    if not pages:
        print("Không tìm thấy trang HTML nào.")
        return 1

    checked = 0
    for page in pages:
        if page.name == "404.html":
            continue
        raw = page.read_text(encoding="utf-8", errors="replace")
        text = visible_text(raw)
        checked += 1

        # Bỏ <code>/<pre> TRƯỚC khi tìm markup lọt — xem ghi chú ở CODE_RE.
        # Các kiểm khác vẫn dùng `text` đầy đủ: frontmatter hỏng có thể lọt ra
        # bên trong <pre>, nên ở đó không được loại trừ.
        check_leaked_markup(page, visible_text(CODE_RE.sub(" ", raw)))
        check_degraded_cards(page, raw)
        check_frontmatter_leak(page, text)
        if page.name == "index.html" and page.parent == SITE:
            check_css_loaded(page, raw)

    print(f"Đã kiểm {checked} trang trong _site/.\n")

    if errors:
        print(f"LỖI ({len(errors)}):")
        for e in errors:
            print(f"  ✗ {e}")
        print()
    if warnings:
        print(f"CẢNH BÁO ({len(warnings)}):")
        for w in warnings:
            print(f"  ! {w}")
        print()

    if not errors and not warnings:
        print("✓ Không thấy markup nào lọt ra ngoài.")

    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
