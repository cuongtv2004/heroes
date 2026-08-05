# Heroes Codex & Saga

Bộ tài liệu tiếng Việt về **Heroes of Might and Magic – Old Universe**
(Heroes I–IV, Heroes Chronicles, Might and Magic I–VIII).

Hai sản phẩm, một nền dữ liệu:

<div class="grid cards" markdown>

- :material-book-open-variant: **Heroes Codex**

    Bách khoa toàn thư để tra cứu. Mở đâu đọc đó.
    Đây là **nền tảng** của dự án.

    [Vào Codex](codex/index.md)

- :material-script-text: **Heroes Saga**

    Sử thi tiểu thuyết hóa, đọc từ đầu đến cuối.
    Xây **dựa trên** Codex.

    *Chưa bắt đầu — chờ Codex đủ dày.*

</div>

> Codex là *sự thật của thế giới*. Saga là *câu chuyện được kể từ sự thật đó*.

---

## Ba nguyên tắc không thương lượng

!!! warning "1. Mọi thông tin có nhãn nguồn"
    Không claim nào được đứng trơ trọi. Mỗi khẳng định ghi rõ đến từ đâu
    (**T1**–**T6**) và chắc chắn đến mức nào (`EXPLICIT` / `INFERENCE` /
    `DISPUTED` / `FAN_THEORY`).

!!! warning "2. Trí nhớ không phải nguồn"
    "Theo tôi biết" không phải nguồn — kể cả với người, kể cả với AI. Không
    fetch được nguồn thì claim đó là `UNVERIFIED`, không được vào thân bài.

!!! warning "3. Người viết không tự kiểm bài của mình"
    Mọi bài qua luồng kiểm định độc lập, do một agent riêng chạy, **mặc định coi
    claim là sai** cho đến khi tìm được nguồn phản bác được.

---

## Đọc gì trước

Nếu bạn (hoặc một AI agent) sắp đóng góp:

| # | Tài liệu | Nội dung |
|---|---|---|
| 1 | [Chính sách canon](00-foundation/CANON-POLICY.md) | Cách xác định điều gì là thật. Hệ thống nhãn hai trục |
| 2 | [Cấu trúc dữ liệu](00-foundation/SCHEMA.md) | 12 loại entity, frontmatter, bộ quan hệ |
| 3 | [Luồng kiểm định](00-foundation/VERIFY-PROTOCOL.md) | **Không bỏ qua** |
| 4 | [Quy trình làm việc](00-foundation/WORKFLOW.md) | Sáu bước, và ba bài học đã trả giá để có |
| 5 | [Quy tắc viết Saga](00-foundation/SAGA-STYLE.md) | Ranh giới canon vs sáng tạo |

[Chính sách canon](00-foundation/CANON-POLICY.md) có quyền lực cao nhất. Bài viết
nào xung đột với nó thì bài viết sai.

---

## Điều làm dự án khác một wiki

**Wiki chép. Dự án này giải thích, và nói rõ mình biết chắc đến đâu.**

Ví dụ thật từ [bài về Sandro](codex/heroes/sandro.md):

- Bio chính thức Heroes III nói Ethric dạy Sandro *Necromancy*. Nhưng mọi campaign
  text nói Ethric dạy **warlock** và nổi giận vì Sandro thành necromancer. Dự án
  ghi cả hai và nói rõ đây là mâu thuẫn trong chính tư liệu chính thức.
- Sandro trong Heroes Chronicles **gần như chắc chắn là người trùng tên** — lệch
  hàng trăm năm. Một wiki lớn liệt kê thẳng không cảnh báo; dự án này ghi
  `DISPUTED` và trình bày cả hai phía.
- Claim "artifact từng thuộc về Ethric" lưu hành rộng — dự án truy ra nó **không
  có nguồn**, và tìm được chủ cũ thật mà game nêu đích danh: **người dwarf**.

---

## Trạng thái

!!! info "Giai đoạn 1 — Xây nền: đã xong"
    Sáu tài liệu nền · [Sổ nguồn](sources/REGISTRY.md) **243 key** · công cụ kiểm 3 tầng

**Codex hiện có 15 bài trên 5 loại schema — và mọi bài đều đã qua kiểm định độc lập.**

| Bài | Loại | Trạng thái |
|---|---|---|
| [Sandro](codex/heroes/sandro.md) | hero | ✅ verified |
| [Jeddite](codex/heroes/jeddite.md) | hero | ✅ verified |
| [Archibald Ironfist](codex/heroes/archibald-ironfist.md) | hero | ✅ verified |
| [Gauldoth Half-Dead](codex/heroes/gauldoth-half-dead.md) | hero | ✅ verified |
| [Tarnum](codex/heroes/tarnum.md) | hero | ✅ verified |
| [Gem](codex/heroes/gem.md) | hero | ✅ verified |
| [Ethric](codex/characters/ethric.md) | character | ✅ verified |
| [The Reckoning](codex/events/the-reckoning.md) | event | ✅ verified |
| [Vụ đầu độc Nicolas Gryphonheart](codex/events/vu-dau-doc-nicolas-gryphonheart.md) | event | ✅ verified |
| [Deyja](codex/kingdoms/deyja.md) | kingdom | ✅ verified |
| [Cloak of the Undead King](codex/artifacts/cloak-of-the-undead-king.md) | artifact | ✅ verified |
| [Armor of the Damned](codex/artifacts/armor-of-the-damned.md) | artifact | ✅ verified |
| [Amulet of the Undertaker](codex/artifacts/amulet-of-the-undertaker.md) | artifact | ✅ verified |
| [Vampire's Cowl](codex/artifacts/vampires-cowl.md) | artifact | ✅ verified |
| [Dead Man's Boots](codex/artifacts/dead-mans-boots.md) | artifact | ✅ verified |

**Cả năm kỷ nguyên đều đã có bài trụ** — Age of Kings, Antagarich, The Reckoning, Axeoth,
và tuyến xuyên kỷ của Heroes Chronicles.

Saga chưa bắt đầu — theo `SAGA-STYLE.md` **S6**, một chương chỉ được viết khi các entity
Codex **mà nó dựa vào** đã `verified`. Đó là điều kiện **theo từng chương**, không phải
"chờ xong cả Codex": cụm *Shadow of Death* hiện đã đủ nền cho Book IV.

---

## Hạn chế — nói thẳng

**Toàn bộ text in-game trong Codex mang tier `T1*`** — nghĩa là **bản chép của fan
wiki, không phải file game gốc**.

Vẫn tin ở mức cao vì wiki nguồn chép nguyên cả lỗi chính tả trong game và đánh dấu
bằng `{{sic}}` — dấu hiệu bản chép trung thực. Nhưng vẫn cách nguồn gốc một bước.

Xem [Sổ nguồn](sources/REGISTRY.md) mục "Lưu ý về T1*", và
[Việc còn tồn](00-foundation/BACKLOG.md) `B-001`.
