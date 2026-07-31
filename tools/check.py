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
CODEX = ROOT / "codex"
REGISTRY = ROOT / "sources" / "REGISTRY.md"

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

# Nhãn inline trong thân bài: {T1* EXPLICIT: source-key ...}
CLAIM_RE = re.compile(r"\{(T\d\*?)\s+([A-Z_]+):\s*([^}]+)\}")

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
        err("sources/REGISTRY.md không tồn tại")
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


def main() -> int:
    strict = "--strict" in sys.argv

    registry = load_registry_keys()
    if not registry:
        warn("registry rỗng — mọi source key sẽ báo thiếu")

    files = sorted(CODEX.rglob("*.md"))
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

        # (5)(6) nhãn trong thân bài
        claims = CLAIM_RE.findall(body)
        if not claims:
            warn(f"{rel(path)}: thân bài không có nhãn claim nào")

        for tier, certainty, payload in claims:
            if certainty not in CERTAINTY:
                err(f"{rel(path)}: nhãn certainty không hợp lệ trong thân bài: {certainty}")
            # (6) không UNVERIFIED trong thân bài khi đã verified
            if certainty == "UNVERIFIED" and status == "verified":
                err(f"{rel(path)}: bài `verified` nhưng còn claim UNVERIFIED")

            # source key là token đầu của payload
            first = payload.strip().split()[0].rstrip(",;")
            if first and first not in registry and not first.startswith("("):
                warn(f"{rel(path)}: nhãn dùng source key ngoài registry: {first}")

    # Báo cáo
    print(f"Đã kiểm {len(entities)} bài, {len(registry)} source key trong registry.\n")

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
