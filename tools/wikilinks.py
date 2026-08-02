#!/usr/bin/env python3
"""Chuyển [[wikilink]] thành liên kết Markdown thật, cho MkDocs.

Codex dùng cú pháp `[[entity-id]]` để liên kết chéo. Cú pháp đó ngắn gọn khi viết
và cho phép trỏ tới bài **chưa tồn tại** — điều quan trọng ở giai đoạn đầu, vì nó
đánh dấu việc cần làm thay vì báo lỗi.

Nhưng MkDocs không hiểu cú pháp đó. Script này chuyển:

    [[sandro]]           →  [Sandro](../heroes/sandro.md)
    [[chua-viet]]        →  Chua Viet          (in nghiêng + tooltip, không phải link)

Bài chưa tồn tại **không** thành link chết — chúng hiện dưới dạng chữ nghiêng mờ,
báo cho người đọc biết đây là entity đã được nhắc nhưng chưa viết.

Dùng:
    python3 tools/wikilinks.py --check    # chỉ báo cáo, không sửa file
    python3 tools/wikilinks.py --build    # ghi vào _build/ để MkDocs dùng
"""

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
BUILD = ROOT / "_build"

WIKILINK_RE = re.compile(r"\[\[([a-z0-9][a-z0-9\-]*)\]\]")
FM_ID_RE = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
FM_NAME_RE = re.compile(r"^name_vi:\s*(.+?)\s*$", re.MULTILINE)


def build_index() -> dict[str, tuple[Path, str]]:
    """Quét docs/ và trả về {entity_id: (đường dẫn, tên hiển thị)}."""
    index: dict[str, tuple[Path, str]] = {}
    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        m = FM_ID_RE.search(text)
        if not m:
            continue
        eid = m.group(1).strip().strip('"').strip("'")
        name_m = FM_NAME_RE.search(text)
        name = name_m.group(1).strip().strip('"').strip("'") if name_m else eid
        index[eid] = (md, name)
    return index


def humanise(eid: str) -> str:
    """`cloak-of-the-undead-king` → `Cloak Of The Undead King` (dự phòng)."""
    return " ".join(w.capitalize() for w in eid.split("-"))


def convert(text: str, source: Path, index: dict) -> tuple[str, set[str]]:
    """Trả về (text đã chuyển, tập id chưa tồn tại)."""
    missing: set[str] = set()

    def replace(m: re.Match) -> str:
        eid = m.group(1)
        if eid in index:
            target, name = index[eid]
            rel = _relative(source, target)
            return f"[{name}]({rel})"
        missing.add(eid)
        # Chưa viết: hiện nghiêng, kèm tooltip. Không tạo link chết.
        return f'<span class="wl-todo" title="Chưa viết: {eid}">*{humanise(eid)}*</span>'

    return WIKILINK_RE.sub(replace, text), missing


def _relative(source: Path, target: Path) -> str:
    """Đường dẫn tương đối từ file nguồn tới file đích."""
    src_dir = source.parent
    try:
        return str(target.relative_to(src_dir))
    except ValueError:
        up = [".."] * len(src_dir.relative_to(DOCS).parts)
        return "/".join(up + list(target.relative_to(DOCS).parts))


def main() -> int:
    mode = "--check"
    for arg in sys.argv[1:]:
        if arg in ("--check", "--build"):
            mode = arg

    index = build_index()
    all_missing: dict[str, set[str]] = {}
    converted = 0

    if mode == "--build":
        if BUILD.exists():
            shutil.rmtree(BUILD)
        shutil.copytree(DOCS, BUILD)

    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        if "[[" not in text:
            continue
        new_text, missing = convert(text, md, index)
        if missing:
            all_missing[str(md.relative_to(ROOT))] = missing
        if new_text != text:
            converted += 1
            if mode == "--build":
                out = BUILD / md.relative_to(DOCS)
                out.write_text(new_text, encoding="utf-8")

    print(f"{len(index)} entity trong index, {converted} bài có wikilink.")

    if all_missing:
        total = len(set().union(*all_missing.values()))
        print(f"\n{total} entity được nhắc nhưng chưa viết:")
        counts: dict[str, int] = {}
        for ids in all_missing.values():
            for i in ids:
                counts[i] = counts.get(i, 0) + 1
        for eid, n in sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:15]:
            mark = " ←ưu tiên" if n >= 2 else ""
            print(f"  {n}×  {eid}{mark}")

    if mode == "--build":
        print(f"\nĐã ghi sang {BUILD.relative_to(ROOT)}/")

    return 0


if __name__ == "__main__":
    sys.exit(main())
