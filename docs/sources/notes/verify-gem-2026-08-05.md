# Báo cáo kiểm định — `gem`

**Ngày:** 2026-08-05
**Bài:** `docs/codex/heroes/gem.md`
**Số claim:** 40, chia 5 `PRIORITY` trong một prompt
**Luồng:** một agent verify độc lập, không đọc bài gốc, không đọc `docs/`

---

## Kết quả tổng

| Phán quyết | Số lượng |
|---|---|
| `CONFIRMED` | 33 |
| `DOWNGRADE` | 4 |
| `CONTRADICTED` | **3** |
| `NOT_FOUND` | 0 |

**1 `BLOCKER` · 3 `MAJOR` · 5 `MINOR`** — hết `BLOCKER` và `MAJOR` trước khi đặt `verified`.

---

## BLOCKER

### B-01 · Trình tự chuyển Sorceress → Druid bị bài viết ĐẢO NGƯỢC

Bài khẳng định việc chuyển thành Druid **hoàn tất trong scenario cuối, trước khi** giao artifact.
**Sai.** Ngày 52 nói ngược:

> "I also told him **I would like to finish this last quest for the Boots as a Sorcerer.** After
> that, **if the Druid High Council has approved my vows, I would swear them on the next full
> moon.** […] But first I had to get the Boots to Sandro."

Phải tách **ba** mốc: **quyết định** (ngày 37–45) · **tự nhận** *"I have evolved into a Druid"*
(ngày 48) · **tuyên thệ chính thức** (**hoãn tới sau nhiệm vụ**, ngày 52). Bài gộp cả ba làm một.

✅ Đã viết lại thành bảng ba mốc, kèm nguyên văn ngày 52.

---

## MAJOR

### M-01 · 🔴 Bài BUỘC TỘI SAI một nguồn — và nguồn đó đúng

Bài viết *"cả hai wiki tóm tắt sai trình tự"*, nhắm vào câu của thelazy:

> "Once her quest for Sandro was complete, she changed her allegiance to AvLee and became a Druid."

**Câu đó khớp với game text.** Ngày 52 xác nhận, và `Retrieving the Cowl` ngày 50 xác nhận nốt phần
AvLee: Lord Fayette mời nàng làm General *"as soon as my promise to Sandro was fulfilled"*.

⚠️ **Đây là loại lỗi tệ hơn một lỗi dữ kiện thường.** Dự án lấy việc kiểm nguồn làm cốt lõi; buộc tội
một nguồn là sai **trong khi nó đúng** làm hỏng chính thứ đó. Đã sửa, và **ghi tên lỗi trong bài**
thay vì sửa lặng lẽ.

*(Phần vẫn đúng: câu đó **thật sự** nằm ở mục `== Story ==` không dẫn nguồn, `grep -c '<ref'` = 0.)*

### M-02 · 🔴 `h3wiki-herobios-txt` bị gán tier QUÁ CAO — và lỗi này có từ 2026-08-03

Registry xếp `Translation Data/HeroBios.txt` là **`T1` thật**, lập luận rằng đó là *"file string
table trích trực tiếp từ game"*. **Đó là giả định, không phải kiểm chứng.**

Tôi tự đối chiếu hai trang trước khi sửa:

| | `Talk:Artifact/descriptions` | `Translation Data/HeroBios.txt` |
|---|---|---|
| Câu khai xuất xứ | ✅ `Information from H3Bitmap.lod > artraits.txt` | ❌ **không có gì** |
| `<ref>` | — | **0** |
| Phân loại | — | `Category:Contributor resources` |

→ Hai trang **không tương đương**, nhưng registry đối xử như nhau. `artraits` có câu tự khai xuất xứ
**tới tận tên file `.lod`**; `HeroBios` chỉ là một bảng dán lên, không chú thích.

✅ **Đã hạ `h3wiki-herobios-txt` → `T1*`**, sửa **8 nhãn** ở **3 bài** (`archibald-ironfist` 4,
`jeddite` 3, `gem` 1). ✅ **`h3wiki-artraits-txt` giữ `T1`** — nó có căn cứ.

🔴 **Đây là lần thứ hai trong hai ngày một tier bị gán quá cao vì suy từ HÌNH THỨC trang thay vì
bằng chứng bên trong nó** — lần trước là `h3wiki-lord-haart`. Quy tắc đã ghi vào registry:

> **Một bảng dữ liệu trông giống file game KHÔNG phải là file game.** Chỉ nâng `T1` khi trang **tự
> khai xuất xứ** (tên file gốc, archive, hoặc hash).

### M-03 · Đếm sai số scenario

*New Beginning* có **bốn** scenario (Gem chơi được cả bốn), không phải ba. ✅ Đã sửa.

---

## MINOR đã sửa (5)

- **Claim `{{sic}}` quá mạnh.** "Lỗi ngữ pháp là **nguyên văn trong game**" → chưa ai đối chiếu file
  `.h3c`. Wiki **có** đánh dấu lỗi game ở chỗ khác (`<!-- in-game mistake -->`), nên đó là bằng chứng
  gián tiếp tốt — nhưng là `INFERENCE`, không phải `EXPLICIT`. Sửa hai chỗ.
- **Quote `Clearing the Border` ngày 29** thực ra nằm ở **hai mục timed event riêng** (`29` và
  `29 (cont)`); dấu `…` của bài nối chúng lại. Đã ghi rõ.
- **Lời cảnh báo ngày 27** là của **Amanda**, trong một **giấc mơ** — bài không nêu người nói.
- **"Tên campaign nói về chuyển hóa của Gem"** là **diễn giải**, không nguồn nào nói thẳng →
  tách `EXPLICIT` (câu trích) khỏi `INFERENCE` (cách đọc).
- **`Gem (Ashan)` "cố ý nhại"** — chữ "cố ý" không nguồn nào nói. Đổi thành mô tả **ba điểm trùng**
  quan sát được, và bổ sung: class trong game của nàng là **Mystic**, không phải Druid.

---

## ⭐ Verifier tìm được thứ bài BỎ SÓT — phần giá trị nhất

### V-01 · 🔴 Bài CẮT MẤT chính câu gọi tên nàng

Bài trích Fulton dừng ở *"…Lord Haart…"* và dùng nó làm bằng chứng chung chung về "nhân vật kế thừa".
**Mệnh đề ngay sau đó gọi đích danh nàng:**

> "Keep specific heroes from HoMM2, like Sandro the Necromancer, Halon the Wizard, Lord Haart,
> Crag Hack the Barbarian, **Gem the Druid**, Yog the Barbarian, and Alamar the Warlock."

Đây là **Lead Designer Heroes III ghi lại rằng giữ Gem là một yêu cầu THÀNH VĂN** chốt ở buổi họp
khởi động — phát ngôn first-party, gọi thẳng tên. ✅ Đã nâng thành nguồn chính, không còn là footnote.

### V-02 · Và vì thế một phủ định của bài suýt thành SAI HẲN

Bài viết *"Fulton KHÔNG bình luận về tên Gem"*. Đúng về tài liệu `On Names` — nhưng nếu đọc thành
"Fulton không nói gì về Gem" thì **sai hoàn toàn** (xem V-01).

⚠️ Và lý do vắng mặt là **cấu trúc, không phải thiếu sót**: tài liệu đó liệt kê những tên **Fulton tự
đặt cho Heroes III**; tên Gem có từ **H1/H2**. Sandro, Crag Hack, Yog, Gelu, Clancy cũng vắng mặt vì
**cùng lý do**.

🔴 **Đây là `BH-3` suýt tái diễn** — đúng sai lầm nặng nhất trong lịch sử dự án. ✅ Đã viết lại toàn
mục, nêu rõ lý do cấu trúc.

*(Quét **45** newsletter Fanstratics, 739.447 ký tự: "Gem" xuất hiện **đúng một lần** — dòng trên.)*

### V-03 · Phạm vi tranh chấp class hẹp hơn bài nói

Không phải "sách in vs game". Nhãn `Sorceress` **chỉ có trong *New Beginning***; ở *Unholy Alliance*
**chính engine** gán Druid (`hero row … |Gem|Druid`) và **text game** cũng vậy (*"A Ranger and a
Druid, Gelu and Gem"*).

→ Đúng hơn: **một bản ghi hero của MỘT campaign lệch với tất cả phần còn lại, kể cả phần còn lại của
chính game đó.** Cộng thêm chi tiết Fandom: Gem là **hero duy nhất có tên class riêng**. ✅ Đã dùng.

### V-04 · Hai đoạn game text có sức nặng mà bài bỏ qua

- **Specialty First Aid có lý do trong truyện** — `Clearing the Border` ngày 1: nàng vượt đại dương
  vì *"the nightmares that have plagued me"*, đi tìm một **First Aid Tent**. Nối thẳng về vụ thảm sát
  làng. ✅ Đã thêm.
- **Câu tự định nghĩa nhân vật** — `Retrieving the Cowl` ngày 30: *"I don't think it's wrong to hate
  the Hateful… What I think is wrong is to let that hating turn a person into the thing they hate…
  I won't be like them."* ✅ Đã thêm.

### V-05 · Game text phân xử được vụ Clancy

Bài chỉ ghi "hai trang wiki bất đồng". Game text đứng hẳn về một phía: *"he surprised me by
**offering** to help me with the quest"* → trang `Gem` **mâu thuẫn với game**, không chỉ với trang
`Clancy`. ✅ Đã nâng cấp cách diễn đạt.

### V-06 · Ghi chú truy cập cho registry

`fanstratics.com` **ECONNREFUSED**, `homm.miraheze.org` **403** — nhưng **`homm.fandom.com` chạy
tốt** và có đủ **45** newsletter Fulton, lấy bằng `action=query&prop=revisions&rvslots=main`, 20
title mỗi lô. Đây là **mirror duy nhất vào được** cho nguồn `T4` này.

---

## Ba claim phủ định ĐỨNG VỮNG, và cách chúng được dựng

Không claim nào dùng full-text search — tất cả bằng enumerate rồi grep tại chỗ:

| Claim | Cách kiểm | Kết quả |
|---|---|---|
| Gốc gác chỉ có ở timed event | Bulk-fetch **172/172** scenario, grep `doll\|only survivor\|my village` | 26 hit, **tất cả ở scenario nhân vật khác**; đoạn của Gem chỉ ở **một** chỗ |
| Gem không có trong campaign H4 nào | Enumerate `Category:Heroes IV campaigns` + 8 subcategory → **105 trang** | Đúng **một** hit "Gem", và đó là **tài nguyên** (đá quý), không phải nhân vật |
| H1/H2 không có bio hero | Fetch **11** trang `Heroes II Sorceresses` | Hero **chỉ có ở H1/H2** đều **không có mục Biography**; chỉ hero **đi tiếp sang H3/H4** mới có |

---

## Kết luận

Hết `BLOCKER`, hết `MAJOR`. Bài đặt `status: verified`.

**Điều đáng nhớ nhất của đợt này, và nó khác hai đợt trước:**

Hai đợt trước, lỗi nặng nhất là **claim phủ định sai**. Đợt này, lỗi nặng nhất là **claim khẳng định
sai về một nguồn khác** — bài buộc tội thelazy ghi sai trình tự, trong khi thelazy đúng.

> Dự án đã học cách nghi ngờ **điều mình khẳng định về thế giới**. Đợt này cho thấy còn phải nghi ngờ
> **điều mình khẳng định về nguồn** — nhất là khi lời khẳng định đó có dạng "wiki sai, ta đúng", vì
> nó **tâng bốc chính mình** và vì thế dễ lọt.

Và `M-02` cho thấy cùng một mẫu ở tầng registry: hai lần trong hai ngày, một tier bị gán quá cao vì
**suy từ hình thức** thay vì kiểm bằng chứng bên trong nguồn.

✅ **Mặt tích cực:** đây là đợt đầu tiên `BH-2` chạy như **bước bắt buộc trước mọi fetch khác**, và nó
**bắt được ba bẫy** (`Gem (Ashan)`, `Dryope` dùng chung chân dung, `Dargem`) thay vì sập như hai lần
trước. Việc chuyển bài học thành **bước trong prompt** có tác dụng đo được.
