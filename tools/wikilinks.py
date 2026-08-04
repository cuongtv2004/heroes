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

Script này CŨNG sinh **chiều nghịch đảo của quan hệ**.

`SCHEMA.md` mục 3 và `CLAUDE.md` từ đầu đã hứa "chỉ khai một chiều, công cụ sinh chiều
nghịch đảo", và `check.py` còn cảnh báo khi ai đó viết tay cả hai chiều. Nhưng **trước
2026-08-04 không công cụ nào sinh gì cả** — lời hứa đó không có thật, nên chiều nghịch
đơn giản là **không hiện ra cho người đọc**.

Việc đó đặc biệt tai hại với loại `event`: một sự kiện khai `before: [x]` thì bài `x`
không hề biết có gì đứng trước nó. Trục thời gian chỉ đi được một chiều.

Giờ `--build` chèn vào **bản `_build/`** (không bao giờ vào `docs/`) một mục sinh tự động
liệt kê mọi quan hệ trỏ *tới* bài đó.

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

# Nhãn tiếng Việt cho chiều NGHỊCH của mỗi quan hệ. Khóa là `type` khai trong
# frontmatter; giá trị là cách bài ĐÍCH nên đọc quan hệ đó.
#
# Giữ khớp với INVERSE trong tools/check.py và bảng ở SCHEMA.md mục 3. Quan hệ đối
# xứng (ally_of, enemy_of, sibling_of, spouse_of) KHÔNG có ở đây: check.py đã bắt hai
# bài phải cùng khai, nên sinh thêm sẽ thành trùng lặp.
REVERSE_LABEL = {
    "belongs_to": "Có thành viên",
    "rules": "Được cai trị bởi",
    "located_in": "Chứa",
    "member_of_race": "Có thành viên",
    "parent_of": "Là con của",
    "student_of": "Là thầy của",
    "served": "Được phục vụ bởi",
    "betrayed": "Bị phản bội bởi",
    "killed": "Bị giết bởi",
    "owns": "Được sở hữu bởi",
    "created": "Được tạo bởi",
    "component_of": "Được ghép từ",
    "wielded_in": "Vật phẩm xuất hiện",
    "participated_in": "Có sự tham gia của",
    "caused": "Gây ra bởi",
    "occurred_at": "Là nơi diễn ra",
    "appears_in": "Có xuất hiện",
    "depicted_in": "Mô tả",
    "practices": "Được thực hành bởi",
    "school_of": "Có phép",
    # Trục thời gian — lý do chính khiến mục này tồn tại.
    "before": "Xảy ra sau",
    "after": "Xảy ra trước",
}

# Quan hệ thời gian khai ở cấp frontmatter (danh sách phẳng), không nằm trong
# `relations:`. `concurrent_with` là đối xứng nên không sinh chiều nghịch.
TIME_RELS = ("before", "after")

GENERATED_MARK = "<!-- SINH TU DONG boi tools/wikilinks.py - KHONG sua tay -->"


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


def _frontmatter(text: str) -> str:
    """Trả về phần giữa hai dấu `---` đầu file. Rỗng nếu không có frontmatter."""
    if not text.startswith("---"):
        return ""
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else ""


def collect_reverse(index: dict) -> dict[str, list[tuple[str, str]]]:
    """Quét mọi bài, trả về {entity_đích: [(nhãn_chiều_nghịch, entity_nguồn), …]}.

    Đọc cả `relations:` (list of dict) lẫn quan hệ thời gian khai phẳng
    (`before:` / `after:`). Chỉ giữ quan hệ trỏ tới entity ĐÃ CÓ BÀI — trỏ tới bài
    chưa viết thì không có chỗ nào để hiện.
    """
    reverse: dict[str, list[tuple[str, str]]] = {}

    for eid, (path, _name) in index.items():
        fm = _frontmatter(path.read_text(encoding="utf-8"))
        if not fm:
            continue

        # relations: — list of dict, đọc theo cặp `- type:` … `target:`
        for block in re.finditer(
            r"^\s*-\s*type:\s*(\S+)\s*$(.*?)(?=^\s*-\s*type:|\Z)",
            fm,
            re.MULTILINE | re.DOTALL,
        ):
            rtype = block.group(1).strip().strip('"').strip("'")
            tm = re.search(r"^\s*target:\s*(\S+)\s*$", block.group(2), re.MULTILINE)
            if not tm:
                continue
            target = tm.group(1).strip().strip('"').strip("'")
            label = REVERSE_LABEL.get(rtype)
            if label and target in index and target != eid:
                reverse.setdefault(target, []).append((label, eid))

        # before: / after: — danh sách phẳng, cả dạng inline lẫn gạch đầu dòng
        for rel_name in TIME_RELS:
            m = re.search(
                rf"^{rel_name}:\s*(?:\[(?P<inline>[^\]]*)\]\s*$|$(?P<block>(?:\n\s+-\s*\S+)*))",
                fm,
                re.MULTILINE,
            )
            if not m:
                continue
            raw = m.group("inline") or ""
            targets = [x.strip().strip('"').strip("'") for x in raw.split(",") if x.strip()]
            for bm in re.finditer(r"^\s+-\s*(\S+)\s*$", m.group("block") or "", re.MULTILINE):
                targets.append(bm.group(1).strip().strip('"').strip("'"))
            label = REVERSE_LABEL[rel_name]
            for target in targets:
                if target in index and target != eid:
                    reverse.setdefault(target, []).append((label, eid))

    return reverse


def render_reverse(entries: list[tuple[str, str]], source: Path, index: dict) -> str:
    """Dựng mục Markdown cho chiều nghịch của một bài."""
    by_label: dict[str, list[str]] = {}
    for label, src_eid in entries:
        by_label.setdefault(label, []).append(src_eid)

    lines = [
        "",
        "---",
        "",
        GENERATED_MARK,
        "",
        "## Quan hệ nghịch đảo",
        "",
        "*Sinh tự động từ frontmatter của các bài khác — theo `SCHEMA.md` mục 3, quan hệ chỉ"
        " khai **một chiều**.*",
        "",
    ]
    for label in sorted(by_label):
        targets = sorted(set(by_label[label]))
        rendered = []
        for t in targets:
            tpath, tname = index[t]
            rendered.append(f"[{tname}]({_relative(source, tpath)})")
        lines.append(f"- **{label}:** " + " · ".join(rendered))
    lines.append("")
    return "\n".join(lines)


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

    reverse = collect_reverse(index) if mode == "--build" else {}
    by_path = {p: eid for eid, (p, _n) in index.items()}
    injected = 0

    for md in DOCS.rglob("*.md"):
        text = md.read_text(encoding="utf-8")
        new_text, missing = (convert(text, md, index) if "[[" in text else (text, set()))
        if missing:
            all_missing[str(md.relative_to(ROOT))] = missing
        if new_text != text:
            converted += 1

        if mode == "--build":
            # Chiều nghịch chỉ chèn vào _build/, KHÔNG BAO GIỜ vào docs/ —
            # nó là dữ liệu sinh ra, không phải nội dung người viết.
            entries = reverse.get(by_path.get(md, ""), [])
            if entries:
                new_text = new_text.rstrip() + "\n" + render_reverse(entries, md, index)
                injected += 1
            if new_text != text:
                out = BUILD / md.relative_to(DOCS)
                out.write_text(new_text, encoding="utf-8")

    print(f"{len(index)} entity trong index, {converted} bài có wikilink.")
    if mode == "--build":
        print(f"Đã chèn mục 'Quan hệ nghịch đảo' vào {injected} bài.")

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
