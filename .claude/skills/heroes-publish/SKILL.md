---
name: heroes-publish
description: >-
  Commit và push nội dung Heroes Codex lên main, kèm cửa chặn chất lượng.
  Dùng khi một entity vừa đạt status:verified, hoặc khi user nói "publish",
  "đẩy lên", "push", "commit đi", "xuất bản". CHỈ dùng trong dự án
  /home/cuongtv/heroes — không dùng ở repo khác.
---

# Xuất bản Heroes Codex

Đẩy nội dung lên `main`, GitHub Action sẽ tự build và deploy Pages.

## Nguyên tắc: chỉ push thứ đã qua kiểm

Người dùng đã chọn mức **"sau mỗi entity verified"**. Nghĩa là:

> Không đẩy bản `draft` hay bản còn lỗi lên `main` — vì `main` là thứ Pages
> phục vụ cho người đọc.

## Quy trình

### Bước 1 — Cửa chặn (bắt buộc, không bỏ qua)

```bash
python3 tools/check.py
```

**Phải 0 lỗi.** Cảnh báo dạng "bài chưa tồn tại" là bình thường — đó là liên kết
tới entity chưa viết, không phải lỗi.

Nếu có lỗi: **dừng lại, sửa, chạy lại.** Không được push đè lỗi.

### Bước 2 — Kiểm trạng thái entity

```bash
grep -l "^status: draft\|^status: needs-rework" docs/codex/*/*.md
```

Nếu có bài chưa `verified`:

- **Bài đó là mục đích của lần push này** → dừng. Chạy verify trước
  (xem `/heroes-entity` hoặc `00-foundation/VERIFY-PROTOCOL.md`).
- **Bài đó không liên quan** (đang viết dở, sẽ verify sau) → được phép push,
  nhưng **nói rõ với user** rằng có bài draft đang nằm trên `main`.

### Bước 3 — Kiểm build (khi có thay đổi cấu trúc)

Chỉ cần khi sửa `mkdocs.yml`, thêm thư mục mới, hoặc đổi tên file:

```bash
python3 tools/wikilinks.py --build && mkdocs build --strict
```

Nếu máy chưa có mkdocs, bỏ qua — GitHub Action sẽ bắt lỗi. Nhưng khi đó **báo
trước cho user** rằng build chưa được kiểm tại chỗ.

### Bước 4 — Commit

Xem thay đổi trước khi commit:

```bash
git status --short && git diff --stat
```

**Quy ước commit message của dự án này:**

- Tiếng Việt **không dấu** (tránh lỗi encoding trên các terminal khác nhau)
- Dòng đầu: nói **cái gì thay đổi**, không phải "update files"
- Thân: nói **vì sao**, và nêu rõ **phát hiện đáng chú ý** nếu có
- Nếu luồng kiểm định phản bác điều gì, **ghi lại** — đó là thông tin có giá trị
  cho phiên sau

Ví dụ tốt (lấy từ lịch sử thật của dự án):

```
Ethric + Cloak dat verified. Sandro phuc hoi verified.

Verify doc lap 57 claim: 55 CONFIRMED / 2 DOWNGRADE / 0 BLOCKER.

MAJOR duy nhat - verifier ha chinh claim manh nhat cua minh, va dung:
'artifact tung thuoc ve Ethric' -> minh viet 'bi game text phan bac',
nhung sod-target Day 1 chi HAM Y qua cau truc cau. Ha xuong INFERENCE.
```

Kết thúc mọi commit bằng:

```
Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>
```

Dùng `git -c user.email=tran.van.cuong@sun-asterisk.com -c user.name="cuongtv"`
nếu git chưa cấu hình sẵn.

### Bước 5 — Push

```bash
git push origin main
```

Nhánh mặc định của dự án này là `main` (không phải `master`).

### Bước 6 — Báo cáo

Nói cho user biết:

- Đã push bao nhiêu entity, tên gì
- URL Pages: `https://cuongtv2004.github.io/heroes/`
- Nhắc rằng deploy mất **1–2 phút** sau khi push
- Nếu còn bài `draft` trên `main`, nói rõ bài nào

## Khi KHÔNG được push

Dừng và hỏi user nếu:

- `tools/check.py` còn lỗi
- Có bài `needs-rework` mà chưa xử lý
- Đang có luồng verify chạy dở cho chính entity sắp push
- Thay đổi động tới `mkdocs.yml`, `.github/workflows/`, hoặc `tools/` mà chưa
  build thử được

## Lưu ý về file sinh tự động

`_build/` và `_site/` **không được commit** — đã có trong `.gitignore`. Nếu thấy
chúng trong `git status`, kiểm tra lại `.gitignore` thay vì `git add` thủ công.
