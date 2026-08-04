# Báo cáo kiểm định — `vu-dau-doc-nicolas-gryphonheart`

**Ngày:** 2026-08-05
**Bài:** `docs/codex/events/vu-dau-doc-nicolas-gryphonheart.md` — entity `event` **thứ hai** của Codex
**Số claim:** 48, chia 5 `PRIORITY` trong **một** prompt (theo trần tài nguyên `CLAUDE.md`)
**Luồng:** một agent verify độc lập, **không đọc bài gốc**, không đọc `docs/`, mặc định coi mọi claim
là sai.

---

## Kết quả tổng

| Phán quyết | Số lượng |
|---|---|
| `CONFIRMED` | 41 |
| `DOWNGRADE` | 4 |
| `CONTRADICTED` | **3** |
| `NOT_FOUND` | 0 |

| Mức | Số lượng |
|---|---|
| `BLOCKER` | **1** |
| `MAJOR` | **3** |
| `MINOR` | 4 |

**Hết `BLOCKER` và `MAJOR` trước khi đặt `verified`.**

---

## BLOCKER — claim phủ định của bài bị PHẢN BÁC, và lập luận của nó SAI VỀ CÔNG CỤ

### B-01 · "Goblet of poisoned wine" — bài loại claim này bằng một lập luận vô giá trị

**Bài viết ban đầu** xếp claim *"goblet of poisoned wine"* vào *Câu hỏi mở*, với lý do: citation của
Fandom trỏ tới một URL `3do.com` mà **"bản lưu chỉ có 1.333 byte — quá nhỏ để chứa câu đó"**.

🔴 **Lập luận đó sai về mặt công cụ.** Con số `length` trong CDX API là **kích thước record WARC đã
NÉN**, không phải kích thước trang HTML. Dùng nó để suy ra nội dung trang là **đọc sai định dạng của
chính công cụ mình dùng**. Trang thật khoảng 3.855 byte và **có** chứa câu đó.

**Verifier trích được từ website chính thức 3DO:**

> "Rescuing Erathia's besieged capitol, Catherine learns her father was **poisoned with a goblet of
> wine**."

**Tôi tự kiểm lại, và đây là chỗ phải nói thật:** cả **ba** timestamp verifier nêu
(`20000525045621`, `20001027222129`, `20001207135100`) đều trả **403 FortiGuard** khi tôi thử —
35.321 byte, có chữ `FortiGuard`. Nên **tôi không đọc trực tiếp được trang đó**.

**Nhưng cái tôi kiểm được thì đủ để chấp nhận phán quyết:**

1. Fandom **có** dẫn nguồn cụ thể cho câu đó — `web.archive.org/web/20000818055205/http://www.3do.com/products/pc/heroes3/story/story.htm`,
   ghi nhãn *"Heroes of Might and Magic III" at 3DO.com*. Tôi đã fetch wikitext Fandom và đọc thấy
   `<ref name="HIIIStory">`. Vậy claim **không phải** "không dẫn nguồn".
2. Lập luận byte-size của tôi **tự sụp** bất kể trang nói gì.

✅ **Đã xử lý:** chuyển từ *Câu hỏi mở* sang **`Điểm tranh chấp canon` mục 6** như một `DISPUTED`
thật, có hai phía:

- **"thức ăn"** — `T1*` in-game **hai lần** (`For King and Country`: *"poisoning King Gryphonheart's
  **food**"*; rumor `Homecoming`: *"poison **in his food**"*), cộng `T2*`
- **"rượu"** — `T2` website chính thức 3DO

⭐ **Và verifier đưa một lập luận TỐT HƠN thay cho lập luận sai của tôi:** loạt truyện tiền phát hành
ghi **người thử thức ăn riêng của vua cũng chết** — *"the King's **personal food taster** also died
in his sleep! Since **none of the other guests at last night's feast took ill**…"*. Tôi đã tự đối
chiếu verbatim trên thelazy. **Một người thử thức ăn chết là bằng chứng khẳng định cho độc trong thức
ăn**, và việc không khách nào khác bị gì thì loại đồ uống chung. Đây là cách bác "rượu" **trên nội
dung**, không phải trên kích thước file.

Xử lý theo `CANON-POLICY.md` R1 (in-game thắng văn bản ngoài game) ⇒ bài dùng **"thức ăn"**, nhưng
ghi cả hai phía và **nói rõ dự án không tự đọc được phía `T2`**.

> **Bài học công cụ, đáng nhớ ngang bài học nguồn:** `length` trong CDX là **record đã nén**. Đừng
> suy nội dung trang từ nó. Và **thử vài timestamp** trước khi kết luận một trang archive không lấy
> được — chặn là **per-URL** và không ổn định giữa các lần thử.

---

## MAJOR

### M-01 · 🔴 `BH-2` sập lần thứ hai: có HAI nhân vật tên Haart trong Old Universe

Bài viết: *"chỉ có MỘT Lord Haart trong Old Universe, không phải hai"*.

**Phản ví dụ:** `Haart (Cron)` — nhân vật *Might and Magic II*, **lãnh chúa** của Haart Hold ở Ice
Tundra trên **CRON**. Và CRON **thuộc Old Universe**: trang của nó gắn bản mẫu *"Worlds in the
Ancient Universe"*, còn `CANON-POLICY.md` mục 1 xếp Might and Magic I–VIII trong phạm vi.

✅ **Tôi tự fetch cả hai trang Fandom để xác nhận trước khi sửa** — đúng cả hai.

⚠️ **Đây chính xác là `BH-2`**, và là lần **thứ hai** nó sập theo cùng một kiểu: lần đầu là
`Sandro (Xeen)`, lần này là `Haart (Cron)`. Cả hai lần đều là **claim phủ định về việc "không xuất
hiện ở đâu khác"** đưa ra mà chưa đọc hết trang phân định.

✅ **Đã sửa:** thêm hẳn một tiểu mục cảnh báo trong *Nguyên nhân*, và thu hẹp claim còn lại về đúng
điều kiểm được: **nhân vật Erathia không bị tách thành hai người** — `Lord Haart` và
`Lord Haart the Death Knight` là cùng một người trước/sau khi chết, và điều đó có **bio trong game**
chống lưng (*"Resurrected by his cult of necromantic followers…"*), không cần dựa vào văn xuôi wiki.

### M-02 · Claim "không có mâu thuẫn nào" quá rộng

Bài dùng chuỗi ba tầng để nói *"không tầng nào phủ định tầng khác"* và gọi mục `DISPUTED` cũ là được
gỡ. Verifier chỉ ra hai vấn đề:

1. Việc **hòa giải** ba sản phẩm là **suy luận của bài**, không nguồn nào tuyên bố. Từng tầng
   `EXPLICIT`; **phép ghép** thì `INFERENCE`.
2. Nó được viết **ngay cạnh một mâu thuẫn thật tồn tại** (thức ăn vs rượu).

Thêm một chỗ căng verifier tìm được mà research bỏ sót: manual in *Shadow of Death* tr.16 gán kế
hoạch cho **Sandro** — *"With a little help from **the corrupted Lord Haart**"* — trong khi RoE nói
Haart theo lệnh **Vilmar**. Hòa giải được, nhưng **không tự hòa giải**.

✅ **Đã sửa:** thu hẹp phạm vi "gỡ `DISPUTED`" về **đúng câu hỏi *ai ra lệnh***, hạ nhãn phép ghép ba
tầng xuống `INFERENCE`, và nêu thẳng chỗ căng của manual tr.16.

### M-03 · Fandom `Haart` disambiguation — kết luận sai chiều

Bài viết *"chỉ `Haart (Enroth)` thuộc Old Universe"*. Sai: **hai trong ba** mục thuộc Old Universe
(Enroth và Cron); chỉ `Haart (Ashan)` là ngoài. ✅ Đã sửa cùng M-01.

---

## MINOR đã sửa (4)

- **Đếm scenario sai.** Bài ghi *"năm scenario nhắc vụ đầu độc"*. Thật ra **bốn** nhắc vụ đầu độc;
  scenario thứ năm (`Steadwick's Liberation`) chỉ nhắc **cái chết** (*"after King Gryphonheart's
  death, command of Erathia fell to Morgan Kendal"*), không nhắc chất độc.
- **"Nimbus đào ngũ" không có nguồn.** Game text gọi đây là hành động **chính thức** của phía
  necromancer: *"**As a gesture of good faith**, they send a messenger"*, và Catherine nói *"We have
  confirmed the information the necromancers gave to us."* Fandom gọi hắn *"traitorous"* nhưng **không
  dẫn nguồn**. Đã bỏ chữ "đào ngũ".
- **"thelazy tự mâu thuẫn" quá mạnh.** Năm trang **lệch trọng tâm về tác nhân**, không phải tuyên bố
  ngược nhau — và trang `Sandro` thực ra **mơ hồ về đại từ**: *"He smuggles poison to Lord Haart with
  which **he** assassinates…"*, chữ "he" thứ hai đọc tự nhiên hơn là **Haart**. Hạ xuống
  `T6 INFERENCE`.
- **Lập luận niên đại cần nêu chỗ yếu.** Loạt truyện **không bao giờ nêu năm**, nên việc chuyển ngày
  vào **1164 AS** vẫn không có nguồn; và mùa trong truyện có chỗ lỏng (thelazy ghi *"early days of
  spring in 1165"* trong khi truyện nói triều đình đóng cửa *"for the last month"*). Chân đứng mạnh
  là **đồng hồ xuất bản**, không phải mùa. Đã ghi vào bài.

---

## ⭐ Verifier tìm được thứ research bỏ sót

### V-01 · Lập luận `27/9` được CỦNG CỐ, không phải bị bác

Cụm *"southern-hemisphere spring day"* — một cách nói **kỳ lạ** cho một truyện fantasy — chính là
cách tác giả **hoà giải dateline mùa thu bắc bán cầu (tháng 9–10/1998) với mùa xuân trong truyện**.
Đó là bằng chứng **trực tiếp** cho đồng hồ thực 1:1, và verifier gọi nó là chân mạnh nhất của lập
luận. Bài đã dùng.

### V-02 · Loạt truyện 1998 âm thầm chống lưng cả TUỔI của nhà vua

Fandom **tự lệch** về năm sinh Nicolas: infobox `1100-1101 AS`, văn xuôi cùng trang *"either 1110 or
1111"*. **Chỉ 1110** khớp con số *"54 years"* của loạt truyện nếu vua chết 1164.

⭐ Nghĩa là **con số tuổi cũng truy về loạt truyện diễn đàn 1998** — đúng cơ chế bài này cho rằng đã
sinh ra ngày `27/9`. **Hai ca độc lập, cùng một nguồn ngầm.** Đã thêm vào *Trivia*.

### V-03 · Tên "Finneas Vilmar" gần như chắc do Vanover đặt

Fulton liệt kê tên **không** phải ông đặt, có **Finneas Vilmar**; và nhiệm vụ của Vanover là *"Come up
with names for the eight leaders of Erathia"*. ⇒ người đặt tên con rối, người viết loạt truyện triều
đình, và người viết bio hero **có thể là cùng một người**. Đã thêm vào *Trivia*; là lead cho `B-020`.

### V-04 · Trang story 3DO còn chứa một xác nhận độc lập về Haart

*"Catherine continues her murder investigation and learns **one of her most trusted generals** was
responsible"* — xác nhận vị thế của Haart trong bộ chỉ huy Erathia, từ nguồn official. Đã thêm key
`roe-story-3do` vào registry kèm ghi chú **không đọc trực tiếp được**.

### V-05 · 🔴 Bẫy grep phải nêu tên trong bài

Cụm *"ordered his poisoning"* **CÓ** trong game text Heroes III và **gắn với Sandro** —
`Search for a Killer` ngày 36 — nhưng là về **Lord Falorel**, không phải nhà vua. Ai grep cụm đó rồi
quy về vụ Gryphonheart sẽ sai. Đã nêu thẳng trong bài **và** trong registry.

### V-06 · Phủ định về manual được kiểm mạnh hơn cả claim

Verifier fetch **toàn bộ 144 trang** transcribe của manual RoE (301.394 ký tự): `poison` chỉ xuất
hiện trong text **gameplay** (nọc wyvern tr.94, hơi rồng tr.107, miễn nhiễm elemental tr.116), và
`Haart` chỉ trong **bảng chỉ số hero** tr.127. Câu duy nhất về cái chết là tr.5:
*"the possibility foul play was involved"*. → Phủ định *"manual không nói poison"* là **thật, đã truy
cạn**.

---

## Hai chỗ bài KHÔNG hạ nhãn, và lý do

### S-01 · `P-25` — lập luận về gốc ngày `27/9`

Verifier `CONFIRMED` nó **như một `INFERENCE`**, đúng nhãn bài đã dùng. Giữ nguyên, kèm phần nêu chỗ
yếu đã thêm.

### S-02 · `P-31` — Lord Haart ngồi trong hội đồng điều tra

Verifier không chỉ xác nhận mà còn làm nó **sắc hơn**: *"The fair-haired one was Lord Haart, who had
served Roland Ironfist in Enroth"* — Haart là một trong bảy người của hội đồng, và Kendal nói *"he was
poisoned"* **với kẻ bỏ độc đứng trong phòng**. Giữ, và bài đã dùng đúng mức.

---

## Kết luận

Hết `BLOCKER`, hết `MAJOR`. Bài đặt `status: verified`.

**Điều đáng nhớ nhất của đợt này — khác hẳn đợt `the-reckoning`:**

Ở `the-reckoning`, năm trên năm phát hiện nặng nhất là **claim phủ định**. Ở đợt này, `BLOCKER` cũng
là một claim phủ định — nhưng nó sai **không phải vì quét thiếu dữ liệu** (lỗi của đợt trước), mà vì
**đọc sai định dạng của một công cụ**: dùng `length` của CDX như thể là kích thước trang.

> Hai đợt liền cho hai cơ chế khác nhau của **cùng một loại lỗi**: claim phủ định sai vì **đếm thiếu**
> (đợt trước), và claim phủ định sai vì **suy từ metadata thay vì từ nội dung** (đợt này).
>
> Cả hai đều **trông giống sự cẩn trọng**. Đó là điều làm chúng nguy hiểm.

Và `BH-2` sập lần thứ hai theo đúng kiểu cũ (`Sandro (Xeen)` → `Haart (Cron)`). Điều đó nói rằng ghi
`BH-2` thành quy tắc là **chưa đủ**: nó cần thành **bước bắt buộc trong prompt research**, không phải
một lời nhắc.
