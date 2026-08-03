---
name: heroes-publish
description: >-
  Commit và push nội dung Heroes Codex lên main, kèm cửa chặn chất lượng.
  Dùng khi user YÊU CẦU xuất bản — "publish", "đẩy lên", "push", "commit đi",
  "xuất bản" — hoặc khi user đã cho phép trước với phạm vi rõ ràng.
  KHÔNG tự gọi skill này chỉ vì một entity vừa đạt status:verified hay vì
  các cửa chặn đều xanh: đó là điều kiện CẦN, không phải giấy phép.
  Xem WORKFLOW.md bước 7 để biết định nghĩa đầy đủ.
  CHỈ dùng trong dự án /home/cuongtv/heroes — không dùng ở repo khác.
---

# Xuất bản Heroes Codex

Đẩy nội dung lên `main`, GitHub Action sẽ tự build và deploy Pages.

## ⚠️ Trước hết: kiểm xem có được phép push chưa

Skill này chỉ lo **cửa chặn kỹ thuật**. Nó **không** trả lời câu hỏi "đã được phép
push chưa". Định nghĩa đầy đủ ở `docs/00-foundation/WORKFLOW.md` **bước 7**, gồm hai
phần phải thỏa cả hai:

- **Phần A — cửa chặn kỹ thuật:** bốn cửa ở dưới. Cần, nhưng **chưa đủ**.
- **Phần B — thẩm quyền:** user yêu cầu trực tiếp, hoặc đã cho phép trước với phạm vi rõ.

> **Bốn cửa xanh không phải là lệnh push.** Nó chỉ có nghĩa là push sẽ không làm hỏng site.

Nếu được gọi mà **không** có Phần B — ví dụ chỉ vì một entity vừa `verified`, hoặc vì
đã dồn nhiều commit ở local — thì **dừng và hỏi user**, đừng push.

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

### Bước 2 — Cửa chặn `verified` (BẮT BUỘC, không có ngoại lệ)

```bash
python3 tools/check.py --publish-gate
```

**Nếu có BẤT KỲ bài nào ở `draft` hoặc `needs-rework` → DỪNG. Không push.**

Đây là quy tắc **cứng**, do user đặt ra sau khi 6 bài draft bị đẩy lên `main`:

> **Phải verify xong mới đẩy lên GitHub.**

`main` là thứ GitHub Pages phục vụ cho người đọc. Nội dung chưa qua luồng kiểm định
độc lập **không được xuất hiện ở đó** — kể cả khi "bài đó không liên quan tới lần
push này".

**Không có ngoại lệ nào cho quy tắc này.** Nếu đang viết dở nhiều bài, verify hết
rồi push một lượt; hoặc để chúng ở máy cho tới khi verify xong.

Nếu user **chủ động yêu cầu** push nội dung chưa verify, hỏi lại một lần để chắc
chắn, rồi nói rõ trong commit message rằng có bài chưa verify.

### Bước 3 — Kiểm build và render

```bash
python3 tools/wikilinks.py --build
mkdocs build --strict
python3 tools/lint_site.py
```

**Hai lớp kiểm khác nhau, cần cả hai:**

- `mkdocs build --strict` bắt lỗi **cấu trúc** — link hỏng, anchor không tồn tại
- `lint_site.py` bắt lỗi **hiển thị** — markup lọt ra thành chữ thô

Lớp thứ hai tồn tại vì có tiền lệ: cú pháp icon `:material-xxx:` hiện thành chữ
trên site thật, **build vẫn báo thành công**. Chỉ nhìn bằng mắt mới thấy — hoặc
chạy `lint_site.py`.

Nếu máy chưa có mkdocs, bỏ qua — CI sẽ bắt. Nhưng **báo trước cho user** rằng
build chưa được kiểm tại chỗ.

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
