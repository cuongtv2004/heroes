#!/usr/bin/env python3
"""Kiểm tra tính toàn vẹn của Heroes Codex.

Kiểm 8 điều kiện ở 00-foundation/SCHEMA.md mục 6. Đây là Tầng 1 của
VERIFY-PROTOCOL.md — cửa chặn trước khi tốn công verify bằng AI.

Dùng:
    python3 tools/check.py          # kiểm tất cả
    python3 tools/check.py --strict # coi cảnh báo là lỗi (dùng cho CI)

Không phụ thuộc thư viện ngoài — chỉ stdlib. Frontmatter parse bằng tay
để không cần cài PyYAML.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
CODEX = DOCS / "codex"
REGISTRY = DOCS / "sources" / "REGISTRY.md"

ENTITY_TYPES = {
    "hero", "character", "artifact", "kingdom", "location", "creature",
    "race", "magic", "event", "campaign", "organization", "timeline",
}

# Bộ quan hệ đóng — SCHEMA.md mục 3. Thêm loại mới phải sửa SCHEMA.md trước.
RELATION_TYPES = {
    "belongs_to", "has_member", "rules", "ruled_by", "located_in", "contains",
    "member_of_race",
    "parent_of", "child_of", "sibling_of", "spouse_of", "student_of",
    "teacher_of", "ally_of", "enemy_of", "served", "was_served_by",
    "betrayed", "was_betrayed_by", "killed", "was_killed_by",
    "owns", "owned_by", "created", "created_by", "component_of",
    "assembled_from", "wielded_in", "featured_artifact",
    "participated_in", "involves", "caused", "caused_by", "occurred_at",
    "site_of", "appears_in", "features", "depicted_in", "depicts",
    "practices", "practiced_by", "school_of", "has_spell",
}

CERTAINTY = {"EXPLICIT", "INFERENCE", "DISPUTED", "FAN_THEORY", "UNVERIFIED"}

# Cặp nghịch đảo — SCHEMA.md mục 3. Dùng để phát hiện quan hệ mâu thuẫn giữa hai bài
# (Tầng 3 của VERIFY-PROTOCOL.md). Quan hệ đối xứng ánh xạ về chính nó.
INVERSE = {
    "belongs_to": "has_member", "rules": "ruled_by", "located_in": "contains",
    "member_of_race": "has_member",
    "parent_of": "child_of", "student_of": "teacher_of",
    "served": "was_served_by", "betrayed": "was_betrayed_by",
    "killed": "was_killed_by",
    "owns": "owned_by", "created": "created_by",
    "component_of": "assembled_from", "wielded_in": "featured_artifact",
    "participated_in": "involves", "caused": "caused_by",
    "occurred_at": "site_of", "appears_in": "features", "depicted_in": "depicts",
    "practices": "practiced_by", "school_of": "has_spell",
}
SYMMETRIC = {"sibling_of", "spouse_of", "ally_of", "enemy_of"}

# Cặp không thể cùng đúng giữa hai nhân vật.
CONFLICTING = [("ally_of", "enemy_of")]

# Nhãn inline trong thân bài: {T1* EXPLICIT: source-key ...}
CLAIM_RE = re.compile(r"\{(T\d\*?)\s+([A-Z_]+):\s*([^}]+)\}")

# SCHEMA.md điều kiện 6 — các mục được phép chứa UNVERIFIED.
# Lý do: có những điều thật sự không xác minh được (nguồn không dẫn nguồn, site chặn
# bot). Cấm tuyệt đối thì buộc phải xóa thông tin hữu ích, hoặc không bao giờ đạt
# `verified`. Cả hai đều tệ hơn là ghi rõ "chưa kiểm được" ở đúng chỗ.
UNVERIFIED_OK_SECTIONS = {
    "Câu hỏi mở",
    "Giả thuyết cộng đồng",
    "Điểm tranh chấp canon",
    "Trivia & Dev Notes",
}

errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def split_frontmatter(text: str, path: Path) -> tuple[str, str]:
    """Tách frontmatter YAML khỏi thân bài."""
    if not text.startswith("---"):
        err(f"{rel(path)}: thiếu frontmatter")
        return "", text
    end = text.find("\n---", 3)
    if end == -1:
        err(f"{rel(path)}: frontmatter không đóng")
        return "", text
    return text[3:end], text[end + 4:]


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_frontmatter(raw: str) -> dict:
    """Parse tối thiểu đủ cho schema của dự án.

    Hỗ trợ: scalar, list phẳng, và list of dict (dùng cho relations).
    Không hỗ trợ nested sâu hơn — schema không cần.
    """
    data: dict = {}
    key = None
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()

        if indent == 0 and ":" in stripped and not stripped.startswith("- "):
            key, _, val = stripped.partition(":")
            key = key.strip()
            val = val.strip()
            data[key] = val if val else []
        elif stripped.startswith("- ") and key:
            item = stripped[2:].strip()
            if ":" in item and not item.startswith("http"):
                # bắt đầu một dict trong list
                k, _, v = item.partition(":")
                entry = {k.strip(): v.strip()}
                if isinstance(data.get(key), list):
                    data[key].append(entry)
            else:
                if isinstance(data.get(key), list):
                    data[key].append(item)
        elif indent >= 4 and ":" in stripped and key:
            # trường tiếp theo của dict cuối trong list
            lst = data.get(key)
            if isinstance(lst, list) and lst and isinstance(lst[-1], dict):
                k, _, v = stripped.partition(":")
                lst[-1][k.strip()] = v.strip()
    return data


def load_registry_keys() -> set[str]:
    """Lấy mọi source key khai báo trong sources/REGISTRY.md.

    Key nằm trong cột đầu của bảng, bọc bằng backtick.
    """
    if not REGISTRY.exists():
        err("docs/sources/REGISTRY.md không tồn tại")
        return set()
    keys = set()
    for line in REGISTRY.read_text(encoding="utf-8").splitlines():
        if line.startswith("|"):
            first = line.split("|")[1].strip() if line.count("|") > 1 else ""
            m = re.fullmatch(r"`([a-z0-9\-\*]+)`", first)
            if m:
                keys.add(m.group(1))
    return keys


def strip_quotes(val: str) -> str:
    return val.strip().strip('"').strip("'")


# Nhãn INFERENCE thường dẫn nhiều nguồn: {T1* INFERENCE: key-a + key-b — lý do}
# Phần sau dấu gạch dài là văn giải thích, không phải key.
SOURCE_KEY_RE = re.compile(r"\b([a-z][a-z0-9]*(?:-[a-z0-9]+){1,})\b")


def extract_source_keys(payload: str) -> list[str]:
    """Lấy mọi source key trong phần payload của một nhãn.

    Cắt ở dấu gạch dài (—) hoặc " - " vì phần sau là lời giải thích bằng tiếng Việt,
    có thể chứa từ gạch nối không phải key.
    """
    head = re.split(r"—|\s-\s", payload, maxsplit=1)[0]
    return SOURCE_KEY_RE.findall(head)


def check_relation_consistency(entities: list) -> None:
    """Tầng 3 — phát hiện mâu thuẫn quan hệ GIỮA các bài.

    Chỉ chạy có ý nghĩa khi Codex đã có nhiều bài. Bắt ba loại lỗi:

    1. Quan hệ đối xứng khai một chiều (A ally_of B nhưng bài B không nhắc A)
    2. Cặp loại trừ nhau (A ally_of B trong khi B enemy_of A)
    3. Quan hệ nghịch đảo khai tay ngược chiều nhau, gây trùng lặp
    """
    # (entity_id, rel_type) -> set các target
    graph: dict[tuple[str, str], set[str]] = {}
    # (entity_id, rel_type, target) -> certainty, để so độ chắc hai chiều
    certainty_of: dict[tuple[str, str, str], str] = {}
    paths: dict[str, str] = {}

    for path, fm, _ in entities:
        eid = strip_quotes(str(fm.get("id", "")))
        if not eid:
            continue
        paths[eid] = rel(path)
        for r in fm.get("relations", []) or []:
            if not isinstance(r, dict):
                continue
            rtype = strip_quotes(r.get("type", ""))
            target = strip_quotes(r.get("target", ""))
            if rtype and target:
                graph.setdefault((eid, rtype), set()).add(target)
                certainty_of[(eid, rtype, target)] = strip_quotes(r.get("certainty", ""))

    known = set(paths)

    for (eid, rtype), targets in graph.items():
        for target in targets:
            if target not in known:
                continue  # bài chưa viết — đã cảnh báo ở nơi khác

            # (1) đối xứng phải khai hai chiều
            if rtype in SYMMETRIC and eid not in graph.get((target, rtype), set()):
                warn(
                    f"{paths[eid]}: `{rtype}` → {target} là quan hệ đối xứng "
                    f"nhưng {paths[target]} không khai ngược lại"
                )

            # (2) cặp loại trừ nhau
            for a, b in CONFLICTING:
                if rtype == a and eid in graph.get((target, b), set()):
                    err(
                        f"{paths[eid]}: `{eid} {a} {target}` mâu thuẫn với "
                        f"`{target} {b} {eid}` trong {paths[target]}"
                    )

            # (3) nghịch đảo viết tay hai chiều — sinh tự động, không viết tay
            inv = INVERSE.get(rtype)
            if inv and eid in graph.get((target, inv), set()):
                # (3b) Nếu đã viết tay cả hai chiều, ít nhất hai bên phải khớp
                # độ chắc. Lệch nhau nghĩa là hai bài đang nói hai điều khác nhau
                # về cùng một sự thật — lỗi nghiêm trọng hơn việc trùng lặp.
                c_fwd = certainty_of.get((eid, rtype, target), "")
                c_inv = certainty_of.get((target, inv, eid), "")
                if c_fwd and c_inv and c_fwd != c_inv:
                    err(
                        f"{paths[eid]}: `{eid} {rtype} {target}` gán `{c_fwd}` "
                        f"nhưng {paths[target]} gán `{c_inv}` cho chiều ngược "
                        f"`{inv}` — hai bài mâu thuẫn về độ chắc của cùng một claim"
                    )
                else:
                    warn(
                        f"{paths[eid]}: `{rtype}` → {target} đã có nghịch đảo `{inv}` "
                        f"viết tay ở {paths[target]} — nghịch đảo do công cụ sinh, "
                        f"không viết tay (SCHEMA.md mục 3)"
                    )


NAV_ENTRY_RE = re.compile(r"^\s+-\s+(?:[^:\n]+:\s*)?([\w./-]+\.md)\s*$", re.MULTILINE)
# Trang không cần có trong nav: index của từng mục (Material tự gắn qua
# navigation.indexes), và dossier thô (đã loại khỏi site bằng plugin exclude).
NAV_EXEMPT = ("index.md", "sources/raw/")


def check_nav_coverage() -> None:
    """Đối chiếu `nav:` trong mkdocs.yml với file thực tế.

    Hai lỗi khác nhau, đều âm thầm:
    - Bài có file nhưng KHÔNG trong nav → build được nhưng không ai tìm thấy
      từ sidebar. Bài mồ côi.
    - nav trỏ tới file không tồn tại → mkdocs build --strict sẽ bắt, nhưng
      bắt ở đây thì biết sớm hơn.
    """
    cfg = ROOT / "mkdocs.yml"
    if not cfg.exists():
        return

    text = cfg.read_text(encoding="utf-8")
    nav_start = text.find("\nnav:")
    if nav_start == -1:
        return
    # nav kết thúc ở key top-level tiếp theo
    rest = text[nav_start + 1:]
    m = re.search(r"\n(?=[a-z_]+:)", rest[4:])
    nav_block = rest[: m.start() + 4] if m else rest

    in_nav = set(NAV_ENTRY_RE.findall(nav_block))

    on_disk = {
        str(p.relative_to(DOCS))
        for p in DOCS.rglob("*.md")
        if not any(str(p.relative_to(DOCS)).startswith(e) or p.name == e
                   for e in NAV_EXEMPT)
    }

    for orphan in sorted(on_disk - in_nav):
        warn(f"mkdocs.yml: `{orphan}` có file nhưng KHÔNG trong nav — "
             f"không ai tìm thấy từ sidebar")

    for ghost in sorted(in_nav - on_disk):
        if not (DOCS / ghost).exists():
            err(f"mkdocs.yml: nav trỏ tới `{ghost}` nhưng file không tồn tại")


WIKILINK_RE = re.compile(r"\[\[([a-z0-9][a-z0-9\-]*)\]\]")


def report_missing_entities(entities: list, known: set[str]) -> None:
    """Liệt kê entity được nhắc nhiều nhất nhưng chưa viết.

    Dùng để quyết định viết gì tiếp: entity xuất hiện trong nhiều bài nhất sẽ dọn
    được nhiều liên kết treo nhất. Chạy bằng `python3 tools/check.py --next`.
    """
    counts: dict[str, int] = {}
    where: dict[str, set[str]] = {}

    for path, fm, body in entities:
        eid = strip_quotes(str(fm.get("id", "")))
        seen_here = set()

        for link in WIKILINK_RE.findall(body):
            seen_here.add(link)
        for r in fm.get("relations", []) or []:
            if isinstance(r, dict):
                t = strip_quotes(r.get("target", ""))
                if t:
                    seen_here.add(t)

        for target in seen_here:
            if target in known or target == eid:
                continue
            counts[target] = counts.get(target, 0) + 1
            where.setdefault(target, set()).add(eid)

    if not counts:
        print("Không có liên kết treo. Codex nhất quán.")
        return

    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    print(f"Entity được nhắc nhưng chưa viết ({len(ranked)}):\n")
    print(f"  {'lần':>4}  {'id':<32} nhắc bởi")
    print(f"  {'-'*4}  {'-'*32} {'-'*30}")
    for target, n in ranked[:25]:
        src = ", ".join(sorted(where[target]))
        print(f"  {n:>4}  {target:<32} {src}")

    if len(ranked) > 25:
        print(f"\n  ... còn {len(ranked) - 25} entity nữa")

    top = [t for t, n in ranked if n >= 2]
    if top:
        print(f"\nƯu tiên (được ≥2 bài nhắc): {', '.join(top[:10])}")


def main() -> int:
    strict = "--strict" in sys.argv

    registry = load_registry_keys()
    if not registry:
        warn("registry rỗng — mọi source key sẽ báo thiếu")

    # index.md là trang điều hướng cho MkDocs, không phải entity — bỏ qua.
    files = sorted(p for p in CODEX.rglob("*.md") if p.name != "index.md")
    if not files:
        print("Chưa có bài nào trong codex/.")
        return 0

    ids: dict[str, Path] = {}
    entities: list[tuple[Path, dict, str]] = []

    for path in files:
        text = path.read_text(encoding="utf-8")
        raw_fm, body = split_frontmatter(text, path)
        if not raw_fm:
            continue
        fm = parse_frontmatter(raw_fm)
        entities.append((path, fm, body))

        # (1) id unique
        eid = strip_quotes(str(fm.get("id", "")))
        if not eid:
            err(f"{rel(path)}: thiếu `id`")
        elif eid in ids:
            err(f"{rel(path)}: `id` trùng với {rel(ids[eid])} — id={eid}")
        else:
            ids[eid] = path

        # (7) type hợp lệ
        etype = strip_quotes(str(fm.get("type", "")))
        if etype not in ENTITY_TYPES:
            err(f"{rel(path)}: `type` không hợp lệ: {etype!r}")

        for field in ("name_vi", "name_en", "status"):
            if not fm.get(field):
                err(f"{rel(path)}: thiếu trường bắt buộc `{field}`")

    # Kiểm theo từng bài, cần bảng ids đầy đủ trước
    for path, fm, body in entities:
        status = strip_quotes(str(fm.get("status", "")))

        # (4) sources_used có trong registry
        for key in fm.get("sources_used", []) or []:
            if isinstance(key, dict):
                continue
            k = strip_quotes(str(key))
            if k and k not in registry:
                err(f"{rel(path)}: `sources_used` có key không trong registry: {k}")

        # (2)(3)(8) relations
        for r in fm.get("relations", []) or []:
            if not isinstance(r, dict):
                continue
            rtype = strip_quotes(r.get("type", ""))
            target = strip_quotes(r.get("target", ""))
            cert = strip_quotes(r.get("certainty", ""))
            src = strip_quotes(r.get("source", ""))

            if rtype not in RELATION_TYPES:
                err(f"{rel(path)}: quan hệ không thuộc bộ đóng: {rtype!r}")
            if cert not in CERTAINTY:
                err(f"{rel(path)}: `certainty` không hợp lệ: {cert!r} (quan hệ {rtype})")
            if not src:
                err(f"{rel(path)}: quan hệ {rtype} → {target} thiếu `source`")
            elif src not in registry:
                err(f"{rel(path)}: quan hệ {rtype} có source ngoài registry: {src}")
            if not target:
                err(f"{rel(path)}: quan hệ {rtype} thiếu `target`")
            elif target not in ids:
                # Bài chưa viết là chuyện bình thường ở giai đoạn đầu
                warn(f"{rel(path)}: quan hệ {rtype} → `{target}` (bài chưa tồn tại)")

        # (5)(6) nhãn trong thân bài — theo dõi mục hiện tại để áp điều kiện 6
        claims = CLAIM_RE.findall(body)
        if not claims:
            warn(f"{rel(path)}: thân bài không có nhãn claim nào")

        section = ""
        for line in body.splitlines():
            if line.startswith("## "):
                section = line[3:].strip()
                continue

            for tier, certainty, payload in CLAIM_RE.findall(line):
                if certainty not in CERTAINTY:
                    err(f"{rel(path)}: nhãn certainty không hợp lệ: {certainty}")

                # (6) UNVERIFIED chỉ được ở mục dành riêng.
                # Trong thân bài chính, chỉ chấp nhận khi đang CẢNH BÁO về claim của
                # người khác — dấu hiệu: payload nói rõ nguồn không đáng tin.
                if certainty == "UNVERIFIED" and status == "verified":
                    if section not in UNVERIFIED_OK_SECTIONS:
                        is_warning = any(
                            kw in payload
                            for kw in ("không dẫn nguồn", "chưa fetch", "không xác minh")
                        )
                        if not is_warning:
                            err(
                                f"{rel(path)}: bài `verified` có UNVERIFIED chống lưng "
                                f"cho khẳng định trong mục '{section}' — "
                                f"chuyển xuống Câu hỏi mở hoặc ghi rõ vì sao không tin được"
                            )

                for key in extract_source_keys(payload):
                    if key not in registry:
                        warn(f"{rel(path)}: nhãn dùng source key ngoài registry: {key}")

    check_relation_consistency(entities)

    # Báo cáo
    print(f"Đã kiểm {len(entities)} bài, {len(registry)} source key trong registry.\n")

    check_nav_coverage()

    if "--next" in sys.argv:
        report_missing_entities(entities, set(ids))
        return 0

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
        print("✓ Không có vấn đề gì.")
    elif not errors:
        print("✓ Không có lỗi. Cảnh báo ở trên là bình thường khi Codex chưa đầy.")

    return 1 if errors or (strict and warnings) else 0


if __name__ == "__main__":
    sys.exit(main())
