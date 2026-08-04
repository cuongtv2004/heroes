# Báo cáo kiểm định — `the-reckoning`

**Ngày:** 2026-08-04
**Bài:** `docs/codex/events/the-reckoning.md` — entity `event` **đầu tiên** của Codex
**Số claim đưa vào kiểm:** 63 (bảng claim tiếng Anh, chia 5 `PRIORITY` theo giới hạn tài nguyên
trong `CLAUDE.md`: bảng >50 claim thì chia ưu tiên trong **một** prompt, không chia thành nhiều agent)

**Luồng:** một agent verify độc lập, **không đọc bài gốc**, không đọc `docs/`, mặc định coi mọi
claim là sai. Bảng claim là input duy nhất.

---

## Kết quả tổng

| Phán quyết | Số lượng |
|---|---|
| `CONFIRMED` | 50 |
| `DOWNGRADE` | 8 |
| `CONTRADICTED` | **2** |
| `NOT_FOUND` | 0 |

| Mức nghiêm trọng | Số lượng |
|---|---|
| `BLOCKER` | **1** |
| `MAJOR` | **4** |
| `MINOR` | 17 |
| `NOTE` | 41 |

**Tất cả `BLOCKER` và `MAJOR` đã xử lý xong trước khi đặt `verified`.**

---

## BLOCKER — claim phủ định load-bearing bị PHẢN BÁC

### B-01 · "Không bio hero H4 nào nhắc portal" — **SAI**

**Bài viết ban đầu khẳng định:** không bio nào trong 16 bio nhắc `Enroth`, `Axeoth`, `portal`,
`Gelu`, `Sword of Frost`, hay `Armageddon's Blade`; chúng chỉ nói *"the old world"* / *"the new
world"*.

**Phản ví dụ, text game:** bio hero `Fahtrim` (Heroes IV)

> "During the Reckoning, he revealed his bold selflessness by **staying behind until the last
> possible moment to help others through the portals**."

**Hai lỗi cùng lúc, và lỗi thứ hai là lỗi gốc:**

1. Chữ **"portals"** có thật trong text game — và nó là **chữ hiển thị**, không phải đích wikilink.
2. **Claim phủ định được kiểm trên tập sai.** Bài đếm **16** bio; con số thật là **45** block text
   game gọi tên "the Reckoning". Tức phủ định được dựng trên khoảng **⅓** dữ liệu.

**Hệ quả với bài — không chỉ sửa một câu:** bảng *Hai tầng bằng chứng* xếp **toàn bộ** chuyện portal
vào Tầng 2 (chỉ có tài liệu ngoài game). Sai. Đã tách lại:

- **portal tồn tại** → Tầng 1, có text game
- **ai mở và mở thế nào** → Tầng 2

✅ **Đã sửa**, và tôi tự đối chiếu độc lập trước khi sửa: fetch `Fahtrim` qua API Fandom (1.050 byte,
chữ "portals" nằm trong `{{text|…}}`), rồi quét lại toàn bộ 180 trang backlink bằng brace-matching để
đếm chính xác 45 block.

**Phần phủ định CÒN ĐỨNG được, sau khi đếm lại đúng:** trong cả 45 block, `Gelu`, `Sword of Frost`,
`Armageddon's Blade` xuất hiện **0 lần**. Đã giữ, với nhãn thu hẹp đúng phạm vi.

⭐ **Và việc đếm lại còn cho một phát hiện SẮC HƠN cả claim gốc:** tên `Enroth` và `Axeoth` **có**
trong wikitext của các block đó — nhưng **chỉ với tư cách đích wikilink do người sửa wiki thêm**:
`[[Axeoth|new world]]`, `[[Enroth (planet)|old world]]`. Text hiển thị vẫn là *"the old world"* /
*"the new world"*. Tôi đã tự kiểm cả hai ca.

> 🔴 **Bài học mới, đáng vào registry:** đọc **đích wikilink** thành **text game** là một cách
> `T1*`-hóa biên tập của wiki. Đây là biến thể mới của lằn ranh "text game vs văn wiki" mà dự án đã
> biết — nhưng ở mức **trong lòng một block text game**, không phải giữa hai đoạn văn.

---

## MAJOR

### M-01 · "Không nguồn nào cho con số về quy mô thiệt hại" — **SAI**

Bài viết: *"Không nguồn nào, trong hay ngoài game, đưa ra số người chết, tỉ lệ sống sót, hay số
portal."*

**Con số tồn tại, cả bốn loại:**

| Đại lượng | Nguyên văn |
|---|---|
| Số portal | *"**Dozens of portals** opened up"* |
| Bán kính chết ngay | *"within **a hundred miles** died instantly"* |
| Số chết | *"**Thousands died**…"* · *"**Hundreds died** helping others"* |
| Tỉ lệ sống | *"**Most of our numbers were saved**"* |

Thêm nữa: gán `T4 EXPLICIT` cho một **claim phủ định** là lỗi loại — không có "nguyên văn" nào để
trích cho một sự vắng mặt.

✅ **Đã sửa** thành *"không nguồn nào cho con số **chính xác**"*, kèm bảng bốn ước lượng và nói rõ
chúng là **lời kể của nhân vật**, không phải thống kê.

### M-02 · Câu Gauldoth "During the first hours" — verifier nói là văn wiki

**Đây là mục duy nhất bài KHÔNG hạ nhãn.** Ghi lại đầy đủ lập luận hai phía vì đó là điều kiện để
việc không hạ nhãn là hợp lệ, không phải là "tôi khá chắc là đúng".

**Verifier lập luận:** cụm *"During the first hours of the Reckoning"* chỉ xuất hiện ở **một** trang
wiki (Fandom `Gauldoth`), ở đó là văn xuôi ngôi thứ ba có `<ref>`. Bio hero trong game thì nói khác:
*"During the Reckoning, a fire consumed most of his body, and due to an errant spell…"*. Nên nhãn
`T1* EXPLICIT` là sai.

**Bài giữ nhãn `T1*`, ba lý do:**

1. Nguồn của câu **không phải wiki** mà là `h4-death-texts-ch` — transcript 89 KB text kể chuyện
   campaign Death, dự án đã đọc **trực tiếp** ở đợt trước và đã trích theo block.
2. Câu ở **ngôi thứ nhất** (*"I returned…"*); bản Fandom ở **ngôi thứ ba**. Chiều phái sinh là
   wiki **kể lại** transcript, không phải ngược lại.
3. Bio hero **độc lập xác nhận phần thực chất**: có lửa, và xảy ra trong The Reckoning.

⚠️ **Nhưng verifier có một điểm không bác được:** nó **không đọc lại được** transcript đó
(Celestial Heavens 403, `web.archive.org` bị chặn nội dung — xem G-1 dưới). Nên câu này hiện đứng
trên **một** lần fetch, không phải hai lần độc lập.

✅ **Đã xử lý bằng cách trình bày cả hai nguồn cạnh nhau** (bio ngắn + transcript dài), ghi rõ tranh
chấp nhãn ngay trong thân bài, và mở **Q7** để đối chiếu lại khi có mạng khác. Không im lặng giữ nhãn.

### M-03 · "Cùng một người viết cả nguyên nhân lẫn hệ quả" — nói quá

Bài dùng lời tự thuật của Terry Ray (`T4`) để nói lời tiên tri Chronicles và hệ quả Heroes IV **do
cùng một người viết**. Verifier chỉ ra:

- Fandom nói Ray *"conceptualising… **along with Jennifer Bullard**"* — đồng tác giả.
- Bullard tự nói về Chronicles: *"In fact I did a majority of the work myself"* (`T4`).
- Và cả hai wiki đều **không dẫn nguồn** ở điểm phân vai này.

✅ **Đã sửa** thành: Ray **viết text cốt truyện cho cả hai sản phẩm** (tự thuật, `T4` — phần này
đứng); **mức độ đóng góp tương đối giữa Ray và Bullard thì chưa xác định được**.

⚠️ Verifier còn cho rằng nhãn `T4` là sai vì nguồn là văn xuôi wiki. **Không áp dụng ở đây:** bài
dẫn `ray-interview-ubisoft-2015` — phát biểu của chính Ray trên site Ubisoft — chứ không dẫn wiki.
Verifier không có registry nên không biết key này tồn tại. Ghi lại để không ai "sửa lại" thành `T6`.

### M-04 · Nhãn `EXPLICIT` cho các claim phủ định dựng bằng survey

Ba claim bị hạ nhãn cùng một lý do: chúng là **kết quả quét**, không phải câu nào trong nguồn tự nói
ra. `EXPLICIT` đòi trích được nguyên văn; một sự vắng mặt thì không trích được.

| Claim | Cũ | Mới |
|---|---|---|
| "the Reckoning" xuất hiện lần đầu ở Heroes IV | `T1* EXPLICIT` | **`T1* INFERENCE`** |
| Không text game H3/AB/Chronicles nào diễn ra vụ nổ | `T1* EXPLICIT` | **tách**: "book 8 kết thúc trước vụ nổ" = `EXPLICIT`; "không scenario nào diễn ra" = `INFERENCE` (quét 172 trang) |
| Cảnh báo H3:AB có điều kiện ngược | `T1* DISPUTED` | **`T1* INFERENCE`** — đây là suy luận đối chiếu của bài, hai nguồn không tự tuyên bố mâu thuẫn |

✅ Đã sửa cả ba.

---

## MINOR đã sửa (17) — nhóm theo loại

**Sai chỗ / sai loại trong nguồn:**

- Lời tiên tri nằm trong `=== Timed events ===` (khóa theo **ngày**), **không** phải khối
  `==== Events ====` khóa theo **tọa độ**. Scenario có cả hai. `BH-1` áp cho cả hai, nhưng phải gọi
  đúng tên.
- *"born of Chaos, shaped by Magic"* là **tin quán trọ / Thieves' Guild rumour**, không phải mô tả
  artifact → trong truyện là **lời truyền miệng**. Đã ghi rõ.
- *"brought the Barbarian people to the brink of extinction"* là **văn giới thiệu campaign**
  Stronghold H4, **không** phải bio hero. Đã sửa quy thuộc.

**Trích thiếu / trích chọn lọc:**

- Text nhặt Armageddon's Blade thiếu câu cuối *"Inside, you find Armageddon's Blade."* → đã bổ sung.
- Trích `Lost Lore` dừng ở chữ *"non-canonical"*, **bỏ** câu đối trọng *"However, most of the
  information in them does fit with the canonical lore."* → **đã trả lại**. Đây là trích chọn lọc và
  nó làm nguồn trông tệ hơn thực tế.
- Nguyên văn Fulton có ngoặc đơn quanh *'steel-haired woman'* → đã giữ.

**Nói quá / thiếu ngữ cảnh:**

- Fulton là *"**One of** the lead designers of Heroes III"*, không phải "the Lead Designer".
- Câu Bullard *"convoluted and hard to manage"* trả lời câu hỏi về lịch sử **Might and Magic I–V**,
  không phải về cơ chế The Reckoning → không được trình bày như câu trả lời cho "vì sao có Reckoning".
- Ravenwood vs Corak: hai nguồn **không loại trừ nhau tuyệt đối** (Ravenwood có thể là người thực thi
  cho Guardian) → đã đổi từ "mâu thuẫn" sang "chưa nguồn nào nói ra quan hệ giữa hai nhân vật".
- "Gelu chết là claim **không nguồn**" → quá mạnh. Fandom **có** gắn `<ref>`, chỉ là ref dẫn tới
  **cả game** chứ không tới scenario nào → đổi thành **"không dẫn được về một câu cụ thể nào"**.
- Game **rào** về dòng máu Gelu: *"He is **believed to be** half Human, half Vori Elf"* — không nói
  thẳng.
- Danh sách quốc gia Axeoth trong bài thiếu vài tên → đổi thành "gồm…".

**Chỗ lệch được xác định lại cho đúng:**

- Mâu thuẫn nội tại của `Lost Manuscripts` **không** nằm giữa *"last night"* (Kendal) và *"three
  nights ago"* (Lysander) — hai câu đó đo từ hai ngày khác nhau nên không xung đột. Chỗ lệch thật là
  **"three nights" vs "six days"** giữa hai bản của **cùng** Lysander. Bài ban đầu chỉ sai chỗ này.
- Danh sách người chết của Fandom **tự phản bác chính nó**: chú thích "(revived - Immortal)" ngay
  trong dòng Gavin Magnus, và Magnus là phản diện **còn sống** của campaign Order H4. Bài ban đầu
  bỏ mất ngoặc đó.

---

## ⭐ Verifier tìm được thứ research BỎ SÓT — và đây là phần giá trị nhất

### V-01 · Wiki TỰ NHẬN ngày 1177 là suy ra, bằng chính hệ ký hiệu của nó

Trên `Talk:Timeline`, `02-04-1177` được tô **đỏ**, `February 10th, 1177` được tô **cam** — và bảng
chú giải của chính trang định nghĩa **đỏ = "Explicit Dates", cam = "Inferred Dates"**.

Mạnh hơn hẳn lập luận cũ của bài ("wiki cộng nhẩm"): **wiki nhượng bộ điểm này bằng ký hiệu của
chính nó.** Đã đưa vào bài.

### V-02 · Fandom KHÔNG dùng lịch "AS" cho Axeoth — nó dùng lịch khác

Bài lập luận từ **sự vắng mặt** (trang `Axeoth` không có mốc năm nào). Verifier tìm được **bằng chứng
khẳng định**: trang `Palaedra` đề *"ca 525 **A.C.**"*, và `A.C.` chuyển hướng tới `Great Cataclysm`.

Tức ở chỗ Fandom **chịu** gán năm cho một quốc gia Axeoth, nó dùng hệ lịch **khác**. Đã thêm key
`fandom-palaedra` và đưa vào bài.

### V-03 · Lệch 1175 vs 1177 là lệch HỆ THỐNG, không phải một trang

`death = 1175 AS` xuất hiện đồng loạt trên `Kilgor`, `Gelu`, `Catherine Ironfist`, `Roland Ironfist`,
`Eldrich Parson`. Bài trình bày như con số của một trang; thật ra là **lệch hai năm giữa hai wiki**
trên toàn bộ nhóm nhân vật liên quan. Đã sửa.

### V-04 · 🔴 Search API của thelazy KHÔNG DÙNG ĐƯỢC cho claim phủ định

`srsearch=Volee` trả **3** hit trong khi từ đó xuất hiện trên cả chục trang scenario.
`srsearch="February 10th"` trả **0** hit trong khi cụm đó nằm ngay trên trang `The Reckoning`.

> **Index full-text của thelazy bị cũ.** Mọi claim phủ định dựng trên `list=search` của thelazy là
> **vô giá trị**. Cách đúng: enumerate bằng `list=categorymembers` / `list=allpages` rồi bulk-fetch
> `prop=revisions`.

Đây là bài học **tooling** cấp dự án, không riêng bài này. Đã ghi vào `REGISTRY.md` và `BACKLOG.md`.

### V-05 · Hai cụm "reckoning" chữ thường CÓ trước Heroes IV

- *Fall of Sandro* (SoD), prologue, Gem: *"The time of reckoning has come"*
- HotA *Dargem's Diary*: *"dispense the reckoning"*

Không phải sự kiện này — nhưng theo đúng tinh thần `BH-3`, bài **phải tự nêu** hai ca này, để người
đọc sau không tưởng mình vừa bác được claim. Đã đưa vào bài.

### V-06 · Infobox Fandom khẳng định sự kiện được "nhắc tới" trong H3:AB / MM8 / HC8 / MM9

Không dẫn nguồn, và **không khớp** kết quả đọc trực tiếp: ở Chronicles 8 sự kiện **được báo trước**
nhưng **cái tên thì không có ở đó**. Đã đưa vào bài kèm nhãn `UNVERIFIED`.

---

## Hai chỗ verifier SAI — đã tự kiểm lại trước khi bỏ qua

Ghi lại vì `WORKFLOW.md` bước 6 nói "nếu verifier hạ nhãn thì **thường** là nó đúng" — *thường*,
không *luôn*. Cả hai ca dưới tôi đều tự fetch để quyết định, không dựa vào trí nhớ.

### S-01 · Quy thuộc câu về Volee — bài ĐÚNG, verifier sai

Verifier gán đoạn *"Volee was the first city of the Vori Elves…"* cho scenario `Tunnels of Ice`.
Tôi tự fetch cả hai trang:

- `The_Barbarian's_Wife` (10.163 byte): **chứa đủ** đoạn đó, khớp từng chữ, 4 lần nhắc `Volee`.
- `Tunnels_of_Ice` (11.905 byte): chỉ **1** lần nhắc `Volee`, và là một câu khác của Ufretin.

→ Nhãn `hc-the-barbarians-wife` của bài **giữ nguyên**.

### S-02 · Nhãn `T4` cho lời tự thuật của Terry Ray — bài ĐÚNG

Xem M-03. Verifier không có quyền đọc registry nên không biết `ray-interview-ubisoft-2015` tồn tại,
và kết luận nguồn là văn xuôi wiki. Nguồn thật là phát biểu của chính Ray trên site Ubisoft → `T4`.

---

## Chặn tầng mạng phát hiện trong đợt này

### G-1 · 🔴 `web.archive.org` — nội dung bị chặn, index thì không

**Cả research agent và verify agent đều gặp độc lập.** FortiGuard của mạng công ty chặn theo
category **"Games"**.

⚠️ **Bẫy im lặng:** trang chặn trả **HTTP 200** và **~35,3 KB** HTML → `curl` báo **thành công**.
Strip tag còn **~370 ký tự**. Mọi file bị chặn ra **cùng một kích thước**.

> Thấy file wayback ~35 KB mà text ~370 ký tự → **đó là trang chặn**, không phải trang rỗng của
> archive.org, và **không** có nghĩa URL đó chưa được archive.

**Vẫn chạy được:** CDX API (enumerate được, không đọc được) · `archive.org` không có tiền tố `web.`
· thelazy · Fandom API · `acidcave.net`.

**Hệ quả với bài:** 24 trang chính thức 3DO và 39 trang Age of Heroes đã được **định vị chính xác
kèm timestamp** nhưng **không đọc được**. Nên kết quả về nguồn `T2` là **"chưa đọc được"**, KHÔNG
phải **"đã đọc và không có"** — đúng loại phủ định mà bài học lớn nhất của dự án cảnh báo. Đã ghi
timestamp vào `REGISTRY.md` để đợt sau không phải quét lại.

### G-2 · Celestial Heavens — 403 Cloudflare

Hệ quả: **toàn bộ Tầng 2** của bài đứng trên **một** bản chép của thelazy, chưa đối chiếu bản gốc.
Đã ghi thành Q6.

---

## Đối chiếu bản gốc thành công — điều đáng ghi ngược lại

`bullard-interview-2013`: verifier fetch được **bản gốc** `acidcave.net` (HTTP 200, 36 KB) và đối
chiếu với bản chép trên thelazy — **khớp từng chữ**.

⭐ Đây là **corroboration hai domain thật sự độc lập**, loại tốt nhất dự án có. Nghĩa là hai nguồn
`T4` của bài **không cùng độ chắc**: phỏng vấn Bullard đã đối chiếu tận gốc, `Lost Manuscripts` thì
chưa. Bài đã nói rõ điều này ở mục *Nguồn* thay vì đối xử với chúng như nhau.

---

## Kết luận

Hết `BLOCKER`, hết `MAJOR`. Bài đặt `status: verified`, `verify_pass: verify-the-reckoning-2026-08-04`.

**Điều đáng nhớ nhất của đợt này:** cả `BLOCKER` **và** một trong bốn `MAJOR` đều là **claim phủ
định** — *"không bio nào nhắc portal"*, *"không nguồn nào cho con số"*. Cộng với ba claim phủ định bị
hạ nhãn ở M-04, tổng là **năm** trên năm phát hiện nặng nhất đều cùng một dạng.

Khớp chính xác bài học lớn nhất trong `CLAUDE.md`, và lần này ở dạng gọn nhất từng thấy:

> Claim phủ định nguy hiểm hơn claim khẳng định sai **vì nó trông giống sự cẩn trọng.**

Và đợt này thêm được một **cơ chế** cụ thể cho nó: cả hai claim phủ định sai đều sai **không phải vì
đọc sai nguồn**, mà vì **quét trên tập dữ liệu chưa đủ** (16 bio thay vì 45). Phủ định đúng đòi hai
việc tách biệt — đọc đúng, **và** đếm đủ. Bài này ban đầu làm việc thứ nhất mà bỏ việc thứ hai.
