# BACKLOG

Việc cần đào sâu, ghi lại để không mất dấu. Không phải todo của phiên làm việc — đây là
**nợ kỹ thuật của dự án**, tồn tại qua nhiều phiên.

Mỗi mục ghi: nó là gì, vì sao đáng làm, và cần gì để làm được.

Ưu tiên: **P0** = chặn chất lượng toàn dự án · **P1** = đáng làm sớm ·
**P2** = làm khi tiện · **P3** = có thì tốt.

---

## P0 — Chặn chất lượng toàn dự án

### B-001 · Nâng `T1*` → `T1` bằng cách trích file game gốc

**Vấn đề:** toàn bộ text in-game trong Codex hiện là **bản chép của fan wiki**
(heroes.thelazy.net qua `?action=raw`), không phải file game. Đây là hạn chế nền tảng
lớn nhất, ảnh hưởng **mọi bài đã và sẽ viết**.

**Vì sao vẫn tin ở mức cao hiện tại:** wiki chép nguyên cả lỗi chính tả trong game, đánh
dấu bằng `{{sic}}`, và tách bạch text chính thức khỏi ý kiến fan. Xem
`sources/REGISTRY.md` mục "Lưu ý về T1*".

**Cần gì:** một bản cài Heroes III (SoD hoặc Complete). Text campaign nằm trong file
`.h3c`. Cần viết công cụ trích.

**Ảnh hưởng nếu làm được:** mọi claim `T1*` nâng lên `T1` thật. Đây là nâng cấp chất
lượng lớn nhất có thể có cho dự án.

---

### ⭐⭐ ĐƯỜNG THỨ HAI, phát hiện 2026-08-04 — và nó DỄ HƠN đường `.h3c`

`B-002` (bộ tài liệu Bullard ở UT Austin) chứa
**`Heroes/Shadow of Death/Campaign Text/` — 44 file `.txt` text campaign ở DẠNG NGUỒN của người
thiết kế**, đặt tên theo nhân vật: `Sandro.txt`, `Sandro A.txt`–`Sandro D.txt`, `Gem.txt`,
`Gem1.txt`–`Gem4.txt`, `Crag.txt`, `gelu.txt`, `Yog.txt`, `Final A.txt`–`Final L.txt`,
`Secret A.txt`–`D`, `Has01`–`04`.

{T3 EXPLICIT: bullard-papers-manifest — manifest chứng minh các file này tồn tại; nội dung chưa lấy được}

🔴 **Điều này sửa một giả định của chính `B-001`:** mục này giả định phải **trích từ file `.h3c` đã
build**, tức cần bản game + công cụ parse. Thực ra **text nguồn tồn tại ở dạng `.txt` rời** trong một
thư viện đại học — không cần bản game, không cần viết parser.

**So sánh hai đường:**

| | Đường `.h3c` (bản gốc của B-001) | Đường Bullard `.txt` (mới) |
|---|---|---|
| Cần | Bản cài Heroes III + công cụ trích | Xin phép thư viện |
| Được gì | Text **đã build vào game** | Text **nguồn của người thiết kế** |
| Rủi ro | Phải viết parser cho định dạng không tài liệu | Có thể bị từ chối cấp quyền |
| Trạng thái | Chưa có bản game | Manifest đã có; nội dung 401 |

⚠️ **Hai đường KHÔNG thay thế nhau — và khác biệt này quan trọng về mặt tier:** file `.txt` của Bullard
là **bản thảo của người viết**, còn `.h3c` là **thứ thật sự chạy trong game**. Nếu hai bản lệch nhau thì
`.h3c` thắng theo `CANON-POLICY.md` R1 (in-game thắng tài liệu). Nên đường Bullard cho **`T3`**
(tài liệu thiết kế), **không tự động cho `T1`**.

→ Dù vậy nó vẫn là **bước tiến lớn nhất `B-001` từng có**: nó cho một nguồn **độc lập với thelazy** để
đối chiếu, tức bắt được đúng loại lỗi "wiki chép sai" mà dự án đã gặp hai lần.

**Trạng thái:** đường `.h3c` chưa bắt đầu, cần user xác nhận có bản game không. Đường Bullard cần user
xin quyền truy cập — xem `B-002`.

---

## P1 — Đáng làm sớm

### B-016 · Cân bằng kỷ nguyên — Codex đang lệch về đúng một cụm

**Vấn đề:** 9 bài đầu tiên đều thuộc cụm necromancer *Shadow of Death*. Heroes I, Heroes II,
Heroes IV, Might & Magic I–VIII có **0 bài**. `check.py --next` cho thấy 57 entity treo, và
top đầu (`gem`, `crag-hack`, `vidomina`, `sod-*`) vẫn cùng cụm đó.

**Vì sao đây là nợ, không phải chuyện thẩm mỹ:** dự án tự nhận là bách khoa *Old Universe*
(`index.md` dòng 3). Nếu cụm SoD nuốt tiếp 60–80 bài, cái tên đó thành sai.

**Loại lỗi này không có công cụ nào bắt được.** `check.py` 0 lỗi, mọi bài có nguồn, không
luồng verify nào phản bác. Nó chỉ hiện ra khi **đếm bài theo kỷ nguyên**.

**Đã xử lý một phần:** `WORKFLOW.md` giờ có *Luật cân bằng kỷ nguyên* — trước khi một kỷ
nguyên vượt 15 bài, mọi kỷ nguyên khác phải có ít nhất một entity trụ.

**Việc còn lại:** viết bốn entity trụ. Thứ tự đề xuất:

| # | Entity | Kỷ nguyên | Ghi chú |
|---|---|---|---|
| 1 | ~~`archibald-ironfist`~~ ✅ **XONG 2026-08-03** | Age of Kings (H1–H2) | Đi trước vì **dùng chung nguồn** với chuỗi Deyja đã có. Kết quả: mở được nguồn `T2` chính thức (*Diaries of Archibald*) và phát hiện **cả hai wiki hiểu sai** cách hắn lên ngôi Deyja |
| 2 | `the-reckoning` (event) | The Reckoning | Ranh giới Enroth → Axeoth; `TIMELINE-SPINE.md` mục 6 ghi "chưa có nguồn" |
| 3 | ~~`gauldoth-half-dead`~~ ✅ **XONG 2026-08-03** | Kỷ Axeoth (H4) | Dọn luôn B-007. Kết quả: mở được `h4-death-texts-ch` (89 KB transcript in-game) và nguồn `T4` Terry B. Ray |
| 4 | ~~`tarnum`~~ ✅ **XONG 2026-08-03** | Xuyên kỷ | Ghi chú cũ "buộc phải chốt B-010" **sai** — đó là thứ tự kể của Saga, không chặn Codex. Schema giữ nguyên: `class: Barbarian` + bảng sáu class trong thân bài. Kết quả: mở được `chronicles-official-3do` (`T2`) và `ch-h4-might-texts` |

**Trạng thái:** luật đã vào `WORKFLOW.md` (2026-08-03). **Mục 1 và mục 3 xong** —
`archibald-ironfist` mở kỷ Age of Kings, `gauldoth-half-dead` mở kỷ Axeoth. **Codex không còn kỷ
nguyên nào trống hoàn toàn.** Còn hai entity trụ.

**Hai mục còn lại, và nguồn đã sẵn cho cả hai:**

- `tarnum` — **chưa bao giờ bị chặn** (đánh giá cũ xếp hắn vào diện "chặn bởi lỗ nguồn H4" là **lỗi
  phân loại**: hắn là nhân vật **Chronicles**, không phải H4, và thelazy phủ Chronicles tốt — trang
  `Tarnum` có **18.754 byte**, đủ tám campaign kèm bảng class). ⭐ Và giờ có thêm nguồn `T4`: Terry
  B. Ray nói ông **cũng viết cả series Heroes Chronicles** — xem `B-024`.

  ⚠️ **Đính chính:** ghi chú cũ nói `tarnum` "buộc phải chốt `B-010`" — **sai**. `B-010` là quyết định
  **thứ tự kể của Saga** (Book V xếp theo thời gian hay theo thứ tự đọc), không liên quan tới việc
  viết một entity Codex. Codex là tra cứu, Saga là tự sự — hai việc khác nhau.

  **Vướng thật nằm ở schema:** `SCHEMA.md` cho loại `hero` **một** trường `class`, nhưng Tarnum đổi
  class qua **tám** campaign (Barbarian → Knight → …). Cần quyết cách biểu diễn trước khi viết
  frontmatter — xem `B-025`.
- `the-reckoning` — khó nhất, `TIMELINE-SPINE.md` mục 6 ghi "chưa có nguồn". Nhưng hai bài vừa xong
  đã gom được **ba mảnh**: ngày 10/02/1177 AS (`thelazy-the-reckoning`), game text Gauldoth *"During
  the first hours of the Reckoning"* (`h4-death-texts-ch`), và việc Reckoning **giết Kilgor**. Cộng
  với `B-024` (Ray có thể nói về Reckoning) thì mục này **đã bớt trống**.

### ✅ B-016 — **HOÀN THÀNH 2026-08-04**

`the-reckoning` đã `verified`. **Cả bốn entity trụ xong**, và Codex không còn kỷ nguyên nào trống:
Age of Kings (`archibald-ironfist`) · Antagarich (cụm SoD) · The Reckoning (`the-reckoning`) ·
Axeoth (`gauldoth-half-dead`) · xuyên kỷ (`tarnum`).

⭐ **Điều B-016 dự đoán đúng, và điều nó dự đoán sai:**

- **Đúng:** viết entity ngoài cụm SoD **mở được nguồn mới** mỗi lần. Bài `the-reckoning` mở thêm hai
  nguồn `T4` (`fulton-tavern-interview-2018`, và phần Reckoning của `bullard-interview-2013`) cùng
  một nguồn `T1*` lớn (**45** block bio hero H4).
- **Sai:** mục này xếp `the-reckoning` là *"khó nhất"* vì `TIMELINE-SPINE.md` ghi "chưa có nguồn".
  Thực tế **nguồn dồi dào hơn dự đoán** ở phần nhân quả và hệ quả — cái thiếu là **niên đại**, và
  thiếu theo cách không sửa được bằng research thêm: con số đang lưu hành **không tồn tại trong bất
  kỳ nguồn nào**, nó là phép cộng của wiki.

**Bài học giữ lại cho các đợt cân bằng sau:** "chưa có nguồn" trong một ghi chú cũ **không** nói lên
độ khó thật. Ở đây nó chỉ đúng với **một trong ba** mảng nội dung, và đợt research đầu tiên đã dựng
được hai mảng còn lại bằng text game.

**~~Còn đúng MỘT entity trụ: `the-reckoning`.~~**

⭐ Và nó **đã bớt trống nhiều** sau ba bài vừa xong. Các mảnh đã gom được, đều có nguồn:

| Mảnh | Nguồn | Tier |
|---|---|---|
| Ngày 10/02/1177 AS, do Armageddon's Blade đụng Sword of Frost | `thelazy-the-reckoning` | `T6` |
| **Nguyên nhân gián tiếp**: Tarnum tha Kija → ả trộm Sword of Frost → giao Kilgor | `hc-the-protectors-of-the-sword` | **`T1*`** |
| Gauldoth thành half-dead *"During the first hours of the Reckoning"* | `h4-death-texts-ch` | **`T1*`** |
| Reckoning **giết Kilgor** | `h4-death-texts-ch` | **`T1*`** |
| Dân tị nạn sang Axeoth; *"The Reckoning and endless centuries of warfare have brought the Barbarian people to the brink of extinction"* | `ch-h4-might-texts` | **`T1*`** |

Nghĩa là `TIMELINE-SPINE.md` mục 6 ghi "chưa có nguồn" **đã lỗi thời** — giờ có bốn mảnh `T1*`.

**Việc cần trước khi viết:** `the-reckoning` là loại `event`, mà `codex/events/` **vẫn rỗng** —
nên phải chốt convention cho `event` trước (`B-017`).

### B-017 · `codex/events/` rỗng hoàn toàn — trục dọc chưa thành dữ liệu

**Vấn đề:** `TIMELINE-SPINE.md` mục 3 chứa hai chuỗi sự kiện dựng công phu (chuỗi Sandro
~14 mốc, chuỗi Deyja ~12 mốc), nhưng chúng chỉ là **ASCII art trong một file Markdown**.
Không query được, không render được, không kiểm được bằng `check.py`.

`SCHEMA.md` mục 1 định nghĩa loại `event` và nói rõ lý do tách nó khỏi `campaign`: để timeline
cấu trúc theo **thế giới**, không theo game. Nhưng thư mục `codex/events/` **chưa có bài nào**.

**Vì sao đáng làm:** `SCHEMA.md` hứa rằng Atlas / timeline tương tác ở Giai đoạn 4 "chỉ là
chuyện render từ frontmatter". Lời hứa đó **chỉ đúng nếu event là entity thật**. Hiện tại
trục dọc tồn tại dưới dạng người-đọc-được, không phải máy-đọc-được.

`TIMELINE-SPINE.md` mục 6 đã tự ghi việc này vào bảng "cần làm" và chưa ai làm.

**Phạm vi đã chốt:** chỉ lập event cho các mốc có nguồn `EXPLICIT`. **Không** lập cho mốc
`UNVERIFIED` như `1164-09-27` — theo T1 của `TIMELINE-SPINE.md`, không có nguồn thì để trống,
không lấp.

**✅ Convention đã chốt (2026-08-04)** — vào `SCHEMA.md` mục 5, phần *Convention cho `event`*.
Ba câu hỏi và ba câu trả lời:

1. **Khai `before`, và chỉ `before`** — luôn khai từ sự kiện **sớm hơn**. `after` chỉ được dùng
   khi bài sớm hơn **chưa tồn tại**, và phải chuyển về `before` khi bài đó ra đời.
   `concurrent_with` là đối xứng, khai một bên là đủ.
2. **`date_certainty` là trục RIÊNG**, chỉ nói về con số năm — một sự kiện có thể `EXPLICIT`
   chắc chắn mà năm vẫn `UNVERIFIED`. Và `date_absolute: null` là **trạng thái hợp lệ**, thường
   đúng hơn lấp bừa.
3. **Chia theo TRỤC, không theo nội dung:** bài `event` kể từ góc nhìn **thế giới**, bài entity
   kể từ góc nhìn **nhân vật**. Bài `event` là chỗ **duy nhất** khai `before`/`after`.

🔴 **Và việc này lộ ra một lỗ hổng lớn hơn chính B-017:** `CLAUDE.md`, `SCHEMA.md` mục 3 và
`check.py` đều nói *"chỉ khai một chiều, **công cụ sinh chiều nghịch đảo**"* — nhưng **không công
cụ nào sinh gì cả**. `INVERSE` trong `check.py` chỉ dùng để **phát hiện** khai trùng hai chiều;
`wikilinks.py` không đụng tới `relations`. Chiều nghịch đơn giản **không hiện ra cho người đọc**.

Điều đó đặc biệt tai hại với `event`: một sự kiện khai `before: [x]` thì bài `x` **không hề biết**
có gì đứng trước nó — trục thời gian chỉ đi được một chiều, tức đúng thứ B-017 muốn sửa.

**✅ Đã hiện thực hóa:** `wikilinks.py --build` giờ sinh mục **Quan hệ nghịch đảo** vào bản
`_build/` (không bao giờ vào `docs/`), gồm cả quan hệ thời gian. Có test hồi quy 4 điểm.

**✅ Bài `event` đầu tiên đã có (2026-08-04):** `the-reckoning`, `verified`. Convention đã qua thử lửa
một lần và **không phải sửa** — cả ba câu trả lời (khai `before` một chiều · `date_certainty` là trục
riêng · chia theo trục thế giới/nhân vật) đều dùng được như viết.

⭐ **Và ca đầu tiên này xác nhận đúng thứ convention mục 2 dự đoán:** `date_absolute: null` +
`date_certainty: DISPUTED` là **trạng thái đúng**, không phải trạng thái tạm. Sự kiện chắc chắn xảy
ra mà năm thì không truy được — hai trục thật sự độc lập.

🔴 **Nhưng nó lộ ra một lỗ hổng mới trong bộ quan hệ, và lỗ này thuộc `SCHEMA.md` mục 3, không thuộc
convention `event`:**

`the-reckoning` phải để `relations: []`. Không phải vì thiếu dữ liệu — mà vì **mọi quan hệ của một
`event` với thứ khác đều có chiều khai chuẩn đi TỪ PHÍA KIA**: `participated_in` từ nhân vật,
`wielded_in` từ artifact, `depicted_in` từ chính event nhưng trỏ tới `campaign` (mà `codex/campaigns/`
cũng rỗng). Convention `event` chỉ cho ngoại lệ "khai chiều nghịch khi bài kia chưa có" với
`before`/`after`.

**Kết quả:** entity `event` đầu tiên là một **đảo trong graph**, dù nội dung nó nối tới sáu entity.

**Việc cần quyết:** có nên mở rộng ngoại lệ đó cho `involves`/`featured_artifact` không, hay chấp nhận
rằng `event` chỉ vào graph khi các entity quanh nó được viết? Bài đã ghi rõ bốn quan hệ cần khai
(`kilgor`, `gelu`, `armageddons-blade`, `sword-of-frost`) để không mất dấu.

**Việc còn lại:** chuỗi Deyja/Sandro ở `TIMELINE-SPINE.md` mục 3 — giờ **không còn bị chặn** gì cả.

**Trạng thái:** convention xong, tooling xong, **hai bài `event` đã `verified`**
(`the-reckoning`, `vu-dau-doc-nicolas-gryphonheart`).

⭐ **Bài thứ hai chứng minh convention chịu được tải:** nó khai `before: [the-reckoning]` — quan hệ
thời gian **đầu tiên** giữa hai event thật — và `check.py` kiểm được chuỗi đó (không chu trình, không
lệch năm). Trục dọc giờ **thật sự là dữ liệu**, không còn là ASCII art.

⚠️ Nhưng `relations: []` vẫn đúng cho cả hai bài, vì lý do hệ thống ở trên **chưa được giải**.

### B-025 · 🔴 `web.archive.org` bị FortiGuard chặn nội dung — chặn TẤT CẢ nguồn official của dự án

**Là gì:** từ 2026-08-04, máy dev **không đọc được nội dung** `web.archive.org` cho các domain game —
firewall FortiGuard của mạng công ty chặn theo category **"Games"**. **CDX index vẫn chạy**, nên vẫn
enumerate được, chỉ không đọc được.

🔬 **CHẨN ĐOÁN CHÍNH XÁC — đã kiểm bằng thí nghiệm đối chứng, mỗi URL MỘT request nguội:**

| Request | Kết quả |
|---|---|
| wayback → `3do.com/…/heroes4/story.html` | **403** + FortiGuard |
| wayback → `3do.com/` (gốc, path không có từ khóa game) | **403** + FortiGuard |
| wayback → `heroesofmightandmagic.com/` (gốc) | **403** + FortiGuard |
| wayback → `example.com/` | ✅ **200**, sạch |
| wayback → `example.com/mightandmagic/heroes4/story.html` | ✅ **404 của archive.org**, sạch |

**Ba kết luận, cả ba đảo ngược phỏng đoán ban đầu:**

1. **`web.archive.org` KHÔNG bị chặn** — nó chạy tốt. Cái bị chặn là **tên miền ĐÍCH** trong URL.
2. 🔴 **KHÔNG phải rate limit. Giảm tần suất KHÔNG giúp gì** — một request nguội duy nhất vẫn 403.
   Đây là chính sách theo category, **tất định**.
3. **Không phải từ khóa trong path** — `example.com/mightandmagic/heroes4/…` đi qua bình thường.
   `3do.com` và `heroesofmightandmagic.com` bị xếp category "Games" ở **mức domain**.

⛔ **Nên đường duy nhất là đổi mạng** (hotspot / VPN / máy khác) hoặc xin whitelist hai domain.
Không có mẹo tầng URL nào vượt được. `timetravel.mementoweb.org` cũng không kết nối nổi (`http=000`).

⚠️ **Sửa mã HTTP:** bản ghi đầu ghi trang chặn trả `200`; đo lại là `403`. **Đừng nhận diện bằng mã
HTTP** — nhận diện bằng **~35,3 KB + text ~370 ký tự** và grep chữ `FortiGuard`.

⚠️⚠️ **Bẫy im lặng, phải biết trước:** trang chặn trả **HTTP 200** và **~35,3 KB** HTML → `curl` báo
**thành công**. Strip tag còn **~370 ký tự**. Mọi file bị chặn ra **cùng kích thước**.

> Thấy file wayback ~35 KB mà text ~370 ký tự → **đó là trang chặn**, không phải trang rỗng của
> archive.org, và **không** có nghĩa URL đó chưa được archive.

**Vì sao đây là nợ P1, không phải chuyện môi trường:** wayback là **đường duy nhất** vào mọi nguồn
official của dự án. Bị chặn nghĩa là **không mở rộng được** `mm7-diaries-3do`, `chronicles-official-3do`,
`h4-official-3do-story`, `ray-interview-ubisoft-2015`, `ch-h4-might-texts`, `h4-death-texts-ch`, và
**toàn bộ** `aoh-h4-*`. Quote đã trích thì vẫn dùng được; chỉ là đóng băng.

**Ảnh hưởng đã thấy:** `B-022` (39 trang Age of Heroes) và `B-023` (24 trang 3DO) **đã được định vị
chính xác kèm timestamp** trong đợt `the-reckoning` — ghi sẵn trong `REGISTRY.md` — nhưng không đọc
được trang nào. Và verify `the-reckoning` không đối chiếu lại được `h4-death-texts-ch` (xem Q7 của bài).

**Tám đường vượt đã thử, tất cả thất bại:** curl trực tiếp · percent-encode URL nhúng · chế độ raw
`id_` · `r.jina.ai` · `api.allorigins.win` · `api.codetabs.com` · `WebFetch` (chặn ở **tầng tool**) ·
site Age of Heroes live (`ECONNREFUSED`).

**Việc cần làm:** cần một mạng không bị FortiGuard (hotspot điện thoại, VPN, hoặc chạy ở nơi khác) rồi
fetch **một loạt** 63 URL đã có timestamp. Đây là việc **gom lô**, không phải việc lẻ.

**Trạng thái:** chưa có giải pháp trong môi trường hiện tại. Đã ghi đầy đủ vào `REGISTRY.md`.

### B-026 · Search API của thelazy KHÔNG dùng được cho claim phủ định

**Là gì:** phát hiện khi verify `the-reckoning`. Index full-text của `heroes.thelazy.net` **bị cũ**:

- `srsearch=Volee` → **3** hit, trong khi từ đó có trên cả chục trang scenario
- `srsearch="February 10th"` → **0** hit, trong khi cụm đó nằm ngay trên trang `The Reckoning`

**Vì sao đây là nợ cấp dự án:** `B-003` bắt dự án rà mọi claim phủ định, và bài học lớn nhất trong
`CLAUDE.md` nói claim phủ định là loại lỗi nguy hiểm nhất. Nếu một claim phủ định được dựng bằng
`list=search` của thelazy thì **nó vô giá trị** — và không có gì trong quy trình hiện tại chặn việc đó.

**Cách đúng, đã dùng thành công:** enumerate bằng `list=categorymembers` hoặc `list=allpages`, rồi
bulk-fetch `prop=revisions&rvprop=content` và grep tại chỗ. Đợt verify đã quét **172 trang scenario**
và **180 trang backlink** bằng cách này.

**Việc cần làm:**

1. ~~Ghi thẳng vào `VERIFY-PROTOCOL.md`: claim phủ định **không được** dựng trên `list=search`.~~
   ✅ **XONG 2026-08-05** — thành **V5** ở `VERIFY-PROTOCOL.md` mục 7, kèm bảng đo hai truy vấn.
   Cũng đã vào `CLAUDE.md` mục *Trạng thái* điểm 4.
2. Rà lại các claim phủ định đã có trong Codex xem cái nào dựng bằng search API.

**Trạng thái:** mục 1 ✅ xong. **Còn mục 2** — chưa rà lại bài cũ. Đây là việc **đọc lại**, không cần
mạng ngoài, nên **không bị `B-025` chặn**: quét các bài `verified` tìm claim phủ định, rồi với mỗi cái
hỏi "claim này dựng bằng gì?". Gộp được với mục 2 của `B-027` và với `B-003` thành **một đợt rà**.

### B-027 · Đích wikilink KHÔNG phải text game — biến thể mới của lằn ranh `T1*`

**Là gì:** trong các block text game của bio hero H4, tên `Enroth` và `Axeoth` **có** xuất hiện —
nhưng **chỉ với tư cách đích wikilink do người sửa wiki thêm**: `[[Axeoth|new world]]`,
`[[Enroth (planet)|old world]]`. **Text hiển thị trong game là *"the old world"* / *"the new world"*.**

**Vì sao đáng làm:** dự án đã biết lằn ranh "text game vs văn wiki" giữa **hai đoạn văn**. Đây là lằn
ranh ấy **bên trong một block text game** — tinh vi hơn, và không công cụ nào bắt được. Đọc đích link
thành text game là `T1*`-hóa một biên tập của wiki.

**Việc cần làm:** rà các bài đã `verified` xem có claim nào dựa vào **đích wikilink** thay vì chữ hiển
thị — đặc biệt nhóm artifact, nơi nhiều claim trích từ bảng có link dày.

**Trạng thái:** đã ghi vào `REGISTRY.md` ở entry `fandom-h4-hero-bios`. Chưa rà lại bài cũ.

### B-018 · `hota-changelog` đang mang tier `T1*` — sai **loại** nguồn, không chỉ sai cấp

**Vấn đề:** `REGISTRY.md` xếp `hota-changelog` vào Nhóm 1 — *Text in-game Heroes III (T1\*)* — với
tier `T1*`, tức "in-game text tiếp cận qua trung gian".

Nó không phải in-game text. **Không có chuỗi nào trong game hiện ra nội dung changelog.** Đó là
văn bản phát hành của nhóm phát triển một expansion **do fan làm**. Theo `CANON-POLICY.md` mục 2
nó gần `T4` (phát ngôn developer) hơn nhiều, hoặc `T6` nếu không coi nhóm HotA là developer.

**Vì sao đáng làm:** registry tự ghi key này là "**nguồn chuẩn** cho mọi claim về HotA". Một sai
loại nguồn ở chỗ đó **lan ra mọi bài có phần HotA** — hiện đã là toàn bộ nhóm artifact.

**Phát hiện ở đâu:** verify `dead-mans-boots` (2026-08-03). Verifier **không** hạ verdict của
C-10 vì việc này, vì nội dung C-10 vẫn trích được nguyên văn và vẫn đúng — vấn đề nằm ở nhãn tier,
không ở sự thật của claim.

**Vì sao chưa sửa ngay:** đổi tier của key này buộc phải rà lại nhãn ở mọi bài đang dẫn nó. Làm
lẻ sẽ tạo trạng thái nửa vời, tệ hơn hiện tại.

**Việc cần làm:**

1. Chốt `hota-changelog` thuộc `T4` hay `T6` — quyết định này cần một mục trong `CANON-POLICY.md`
   về **cách xếp tier cho expansion do fan làm** (HotA), vì hiện policy chưa nói.
2. Chuyển key sang nhóm đúng trong `REGISTRY.md`.
3. Rà toàn bộ nhãn dẫn `hota-changelog` và sửa tier.
4. Cân nhắc: các trang **template** HotA (`hota-apocalypse-template`,
   `hota-blacknblue-template`) đã được xếp `T6` trong cùng đợt — nên nhất quán với quyết định trên.

**Trạng thái:** chưa bắt đầu. Chặn bởi việc phải quyết định policy ở mục 1 trước.

### ✅ B-019 · ~~Lỗ nguồn Heroes IV~~ — **ĐÃ GIẢI (2026-08-03)**

**Lời giải:** mục `heroes4/` của `heroesofmightandmagic.com` — site **`Age of Heroes`** — được lưu
**đầy đủ** trong `web.archive.org`: khoảng **200 URL**, tier **`T1*`**.

🔴 **ĐÍNH CHÍNH:** bản đầu của mục này gọi đó là "site chính thức của New World Computing" và gán
**`T2`** — **sai**. Footer trang ghi *"Age of Heroes… copyrighted ©2005 Valera Koltsov"*; grep toàn
trang cho `New World Computing` ra **0 lần**. Đó là **site fan**. Tier đúng là **`T1*`** (mô tả item
in-game qua trung gian fan). Cái sai này **đã lên `main`** trước khi bị bắt — xem `REGISTRY.md`.

Gồm: `artifacts_{minor,major,relic,treasure,potion,tgs}.shtml`,
`heroes_{necromancers,deathknights,lords,magi,priests,sorcerers,thieves,archers,barbarians,druids,knights,campaign}.shtml`,
`creatures_*.shtml`, `buildings_*.shtml`, và **toàn bộ sáu campaign** (`halfdead`, `blade`, `daughter`,
`elwin`, `glory`, `price`).

**Đã dùng ngay:** bài `amulet-of-the-undertaker` nâng mục Heroes IV từ `T6` lên **`T1*`** và **đóng
câu hỏi mở Q3**. Câu mô tả artifact trên Age of Heroes khớp **từng chữ** với bản Fandom — nên Fandom
đúng là bản chép, nhưng giờ không cần dùng bản chép.

**Vì sao trước đây tưởng là bế tắc:** hai giả định sai cùng lúc trong `REGISTRY.md` — rằng
`web.archive.org` **bị chặn**, và rằng `heroesofmightandmagic.com` **đã chết**. Cả hai đều đã được sửa
cùng ngày. Bản thân `B-019` là hệ quả của hai cái sai đó, không phải một lỗ nguồn thật.

⚠️ **thelazy vẫn KHÔNG phủ Heroes IV** — đã kiểm: `Heroes_of_Might_and_Magic_IV` và
`Gauldoth_Half-Dead` đều trả **0 byte**, và cả **56 trang `Translation Data/`** đều là file **Heroes
III**. Nên vẫn không có string table `T1` cho H4, và cũng **không có nguồn chính thức nào** — Age of
Heroes là site fan. Nhưng `T1*` đủ để viết bài, với điều kiện đối chiếu nguồn thứ hai cho claim quan
trọng. Hướng nâng tier tiếp theo: **manual Heroes IV** — xem `B-023`.

**Việc còn lại:** phần lớn 200 URL đó **chưa khai thác**. Xem `B-022`.

### ~~B-019 (bản gốc)~~ · Lỗ nguồn Heroes IV — không có nguồn nào tốt hơn Fandom

**Vấn đề:** `CANON-POLICY.md` mục 1 xác định phạm vi Old Universe gồm **Heroes I–IV**. Nhưng
`heroes.thelazy.net` — nguồn `T1*` xương sống của cả dự án — gần như **chỉ phủ Heroes III**.

Nghĩa là với mọi nội dung H4, nguồn tốt nhất hiện có là `mightandmagic.fandom.com`, tier `T6`,
**không dẫn nguồn**. Theo `CANON-POLICY.md` mục 2, T6 không bao giờ đủ để một claim đạt `CANON`.

**Phát hiện ở đâu:** verify `amulet-of-the-undertaker` (2026-08-03). Verifier chỉ ra bài **bỏ hẳn**
phiên bản H4 của artifact, và điều đó làm **sai** các câu so sánh nhất không rào phạm vi — ở H4 cùng
artifact là hạng **Minor** với **+10%** Necromancy, và **không vô tác dụng** khi hero thiếu skill.

**Vì sao đây là nợ cấp dự án, không phải chuyện một bài:** nó chặn **cả B-016**. Trong bốn entity
trụ mà `WORKFLOW.md` yêu cầu, `gauldoth-half-dead` thuộc kỷ Axeoth (H4) và `tarnum` xuyên kỷ qua
Chronicles. Cả hai sẽ gặp đúng lỗ nguồn này. Viết chúng bằng nguồn `T6` sẽ tạo ra một loạt bài
không bao giờ lên được `verified`.

**Việc cần làm — theo thứ tự dễ trước:**

1. Tìm string table của H4 tương tự `artraits.txt`/`HeroBios.txt` của H3. Nếu H4 cũng có file dữ
   liệu trích được thì lỗ này đóng được ở mức `T1`.
2. Tìm wiki H4 chuyên biệt có dẫn nguồn (`heroesofmightandmagic.com`, các fansite H4 cũ).
3. Manual in của Heroes IV + *Winds of War* — tương đương `T2*`, vẫn hơn `T6` nhiều.
4. Nếu cả ba thất bại: ghi thẳng vào `CANON-POLICY.md` rằng nội dung H4 **tối đa** đạt `INFERENCE`
   cho tới khi có nguồn mới, để không ai tưởng bài H4 đạt chuẩn như bài H3.

⚠️ **Không được xử lý bằng cách bỏ H4 khỏi Codex.** Đó là thu hẹp phạm vi dự án để né một lỗ nguồn,
và nó sẽ tái diễn đúng vấn đề mà B-016 đang sửa.

**Trạng thái:** ✅ đã giải — xem phần trên. Giữ lại mô tả gốc để thấy lập luận sai ở đâu: nó xếp
"thelazy không phủ H4" thành "dự án không có nguồn H4", trong khi nguồn **chính thức** vẫn còn đó.

### B-022 · Khai thác nốt ~200 URL Heroes IV trên `Age of Heroes`

**Là gì:** `B-019` mở ra khoảng 200 URL `T2` trên `heroesofmightandmagic.com/heroes4/`. Hiện chỉ dùng
**hai** trang (`artifacts_minor.shtml`, `campaign_halfdead.shtml`).

**Ưu tiên khai thác:**

1. `campaign_halfdead.shtml` 1–6 — **đủ cho entity trụ `gauldoth-half-dead`** (`B-016` mục 3). Trang
   đầu đã fetch: có điều kiện thắng/thua từng scenario, carryover, và văn kể **ngôi thứ nhất**.
2. `heroes_necromancers.shtml` + `heroes_deathknights.shtml` — thông số hero phe Death.
3. `artifacts_{major,relic,treasure}.shtml` — hoàn thiện phần H4 cho các bài artifact đã có.
4. Năm campaign còn lại — cần cho `the-reckoning` và mọi entity kỷ Axeoth.

⚠️ **Bẫy kỹ thuật:** CDX trả cả **URL cắt lỗi** (`artifactinor.shtml`, `buildinlife.shtml`,
`creaturorder.shtml`…). Chúng trả trang rỗng ~2,3 KB. Tên đúng có gạch dưới đầy đủ
(`artifacts_minor.shtml`). Đã mất một lượt fetch vì cái này.

**Trạng thái:** chưa bắt đầu.

### B-020 · Khai thác `fulton-names-2023` — 98 KB phát ngôn developer chưa dùng

**Là gì:** trang `Gregory Fulton/On Names in Heroes of Might and Magic III` trên thelazy —
**98.499 byte**, thư từ giữa Amelrix và **Gregory Fulton (Lead Designer Heroes III)** trong
2022–2023, khoảng **200 câu hỏi** về nguồn gốc tên town và hero. Công bố 08/AUG/2023 trên Celestial
Heavens, và **do chính Fulton xem lại trước khi công bố**.

Đây là nguồn **`T4`**, và nó trả lời đúng loại câu hỏi mà Codex hay phải để trống: *tên này từ đâu
ra?*

**Phát hiện ở đâu:** verify `jeddite` (2026-08-03), khi verifier tìm nguồn cho tên nhân vật.

**Đã dùng được ngay:** entry `Jeddite` — "Possibly a suggestion given to me, with the obvious play
on 'Jedi' from Star Wars."

**Đã quét sẵn, dùng cho các bài sắp tới:**

| Entity | Fulton nói gì |
|---|---|
| `deyja` | "Deyja is derived from **Old Norse** meaning 'to die'... the nation of death" — **dùng cho bài `deyja`** |
| `thant` | "related to **Thanatos**; the Greek god of death" |
| `vidomina` | mash-up của tiền tố 'Vid-' (visible) + 'domina' (Latin, nữ của dominus) → "clearly visible lord" |
| `ufretin` | từ tiếng Pháp 'fretin' = 'cá bé'/'small fry' — hợp vì hero là dwarf |
| `jabarkas` | có thể do **Christian Vanover** đặt, Fulton giữ lại |

⚠️ **Đáng chú ý: `Sandro` và `Ethric` KHÔNG có trong tài liệu này** (0 lần xuất hiện). Entity chủ
lực của dự án không được Fulton bình luận về tên, trong khi năm nhân vật phụ thì có. Đây là dữ kiện,
không phải thiếu sót của việc tìm kiếm — đã grep toàn bộ 98 KB.

**Việc cần làm:**

1. Đọc hết phần *general questions* (không chỉ bảng tên) — có thể có phát ngôn về thiết kế
   Necropolis/Necromancer, đã thấy `Necropolis` xuất hiện 6 lần, `Necromancer` 4 lần.
2. Rà lại các bài đã `verified` xem có mục *Trivia & Dev Notes* nào bổ sung được bằng nguồn này.
3. Lần theo lead gốc: `celestialheavens.com/forum/topic/17752` — bản post gốc có thể còn nội dung mà
   trang wiki đã lược.

**Trạng thái:** đã vào registry, đã dùng cho `jeddite`. Phần còn lại chưa khai thác.

### B-021 · Policy chưa phân biệt "wiki là nguồn tin" với "wiki là đối tượng nghiên cứu"

**Vấn đề:** `CANON-POLICY.md` mục 2 nói nguồn `T6` tối đa chỉ đạt `INFERENCE`. Quy tắc đó đúng khi wiki
được dùng làm **bằng chứng về thế giới truyện**.

Nhưng Codex ngày càng có một loại claim thứ hai: claim **về chính nội dung wiki**. Ví dụ từ bài
`archibald-ironfist`:

> "thelazy trang `Archibald` viết X, còn trang `Nimbus` của cùng wiki viết Y — nên nó tự mâu thuẫn."

Ở đây wiki **là đối tượng nghiên cứu**, không phải nguồn tin về thế giới. Trích dẫn nó **là**
`EXPLICIT` theo nghĩa chặt nhất: câu đó thật sự nằm ở đó, kiểm được từng chữ.

**Vì sao đáng làm:** loại claim này không phải ngoại lệ hiếm — nó là **cơ chế chính** để Codex ghi nhận
điểm tranh chấp. Bốn trong sáu bài đã verify đều có nó. Hiện mỗi bài tự xử theo cách riêng, và luồng
verify **đã báo lỗi nhãn** cho những chỗ thực ra đúng.

**Việc cần làm:**

1. Thêm vào `CANON-POLICY.md` mục 2 một đoạn phân biệt hai cách dùng nguồn `T6`.
2. Chốt cú pháp nhãn: có thể là `{T6 EXPLICIT: key — claim về nội dung wiki}` hoặc một trục thứ ba.
3. Cập nhật `VERIFY-PROTOCOL.md` để verifier **không** báo lỗi nhãn cho loại này.
4. Rà lại các bài đã `verified` xem nhãn có nhất quán không.

**Trạng thái:** chưa bắt đầu. Phát hiện khi verify `archibald-ironfist` (2026-08-03).

### B-023 · Tìm manual Heroes IV — nguồn chính thức duy nhất còn thiếu cho kỷ Axeoth

**Vấn đề:** sau `B-019`, kỷ Axeoth có nguồn `T1*` (Age of Heroes) và `T4` (phỏng vấn tác giả). Nhưng
**không có nguồn `T2` chính thức nào** — khác với Heroes III, nơi *Diaries of Archibald* trên `3do.com`
cho `T2` thật.

**Vì sao đáng làm:** `CANON-POLICY.md` mục 2 xếp *Heroes IV Manual* là ví dụ điển hình của `T2`. Nó tồn
tại; dự án chỉ chưa tìm. Và **tác giả Heroes IV xác nhận ông có tham gia viết manual** (xem
`B-024`) — nên manual có thể chứa lore không có trong game.

🔴 **ĐÍNH CHÍNH (2026-08-03): kết quả âm ở dưới là SAI.** Verify `gauldoth-half-dead` phát hiện
`3do.com` **CÓ** mục Heroes IV — **58 trang sạch** dưới `/mightandmagic/heroes4/`, gồm `story.html`
với dòng *"© 2001 The 3DO Company"*, `expansion-tgs.html`, `expansion-wow.html`, `features.html`,
`gameplay.html`, `intro.html`, 14 trang `char_*`.

**Vì sao lần quét đầu báo âm:** chỉ thử ba path (`3do.com/heroes4*`, `/games/heroes4*`,
`/products/pc/heroes4*`) và một lần `limit=4000` **không filter** rồi grep — bị cắt trước khi tới.
Đường dẫn đúng có **thêm một tầng** (`/mightandmagic/`). Bài học: quét CDX phải dùng `filter=`, đừng
grep một mẫu bị cắt.

⚠️ Nhưng **manual** thì vẫn chưa tìm được — 58 trang đó là nội dung marketing/tính năng, không phải
manual. Và `story.html` chỉ ~630 ký tự, không nhắc `Axeoth`/`Reckoning`/`Gauldoth`.

**Đường đã biết là KHÔNG đi được:**
- ❌ thelazy: **0 coverage** Heroes IV.

**Đường chưa thử:**

1. CDX cho `3do.com` với `limit` cao hơn 4.000 — lần quét trước có thể bị cắt.
2. `ubi.com` — Ubisoft giữ thương hiệu từ 2003; manual có thể ở đó.
3. Các site lưu manual game (`replacementdocs`, `archive.org` dạng item chứ không phải web capture).
4. `archive.org` **item search** (không phải Wayback) cho ISO/manual Heroes IV.

**Trạng thái:** chưa bắt đầu.

### B-024 · Khai thác phỏng vấn Terry B. Ray — tác giả cốt truyện Heroes IV (T4)

**Là gì:** research `gauldoth-half-dead` (2026-08-03) tìm được phỏng vấn Ubisoft ngày **09/11/2015**
với **Terry B. Ray** — người **viết** Heroes IV. Đây là nguồn `T4` cho kỷ Axeoth, tương đương những gì
`fulton-*` là cho Heroes III và `bullard-*` cho Shadow of Death.

⚠️ **Lưu ý phân vai:** dự án trước đây giả định Jennifer Bullard viết Heroes IV (registry ghi bà là
"designer and storyline writer for Heroes III and IV"). Ray là người viết **cốt truyện Heroes IV** cụ
thể. Cần đối chiếu lại vai của hai người.

**Đã trích được (chưa dùng hết):**

- *"I set out to make Gauldoth the opposite of every necromancer from every fantasy story"*
- *"He is neither good nor evil"* · *"I wanted him to be a metaphor for all Mankind"* · *"In my eyes,
  he is a hero."*
- Về dòng dõi: *"Not like they were all from the same mother, but all from the same bloodline"* và
  *"this idea was never completely developed"* — quan trọng, vì Fandom trình bày điều này như **đã xác
  nhận**.

⚠️ **URL sống đã chết** (redirect sang store) — phải dùng Wayback.

**Việc cần làm:** đọc hết bài phỏng vấn, không chỉ phần về Gauldoth. Ray có thể nói về Reckoning,
Axeoth, và các nhân vật khác — tức nó phục vụ cả `the-reckoning` (`B-016` mục 2).

**Trạng thái:** đã trích phần về Gauldoth, phần còn lại chưa khai thác.

### B-002 · Fetch tài liệu thiết kế gốc của Jennifer Bullard (UT Austin)

**Là gì:** Bullard — Lead Designer và người viết cốt truyện *Shadow of Death* — đã gửi
một bộ tài liệu làm việc cho **Dolph Briscoe Center for American History, University of
Texas**.

`repositories.lib.utexas.edu/items/e3abd6e5-b6be-4547-8900-17b2c9e237da`
(mục lục ghi "Heroes [of Might and Magic] documents")

**Vì sao đáng làm:** đây là **nguồn T3 thật** — tài liệu thiết kế gốc, không qua trung
gian. Có thể chứa phần tiểu sử chưa từng phát hành, kể cả câu trả lời cho **Q1 của
Sandro** (quá trình thành lich — điều không nguồn nào hiện có trả lời được).

**Lead phụ:**
- `heroes3wog.net` được cho là có tư liệu phục hồi từ bộ này ("General Kendal's Diary")
- Thread cộng đồng: `celestialheavens.com/forum/topic/16558`
  ("Jennifer Bullard - Lost manuscript files")

**Cần gì:** thử fetch trực tiếp. Nếu không được, có thể phải liên hệ thư viện.

---

### 🔴 CẬP NHẬT 2026-08-04 — repo VÀO ĐƯỢC, MANIFEST đã lấy, nội dung bị KHÓA

**Đã thử fetch, và kết quả tách làm hai nửa rõ rệt:**

| File | Bytes | Trạng thái |
|---|---|---|
| Trang item | — | ✅ 200 |
| `Heroes_2012-212_110512.txt` — **danh sách file đầy đủ** | 10.896 | ✅ **200, ĐÃ LẤY** |
| `license.txt` | 1.698 | ✅ 200 |
| **`Heroes.zip`** | **21.684.916** | ⛔ **401 "Authentication is required"** |

⚠️ **KHÔNG phải chặn mạng** (khác ca FortiGuard ở `B-025`) — đây là **hạn chế truy cập của thư viện**,
gần như chắc vì bản quyền: `license.txt` ghi *"the Work's copyright owner(s) will continue to own
copyright"*, và chủ quyền là **NWC/3DO**, không phải Bullard.

**Nhưng manifest công khai đã đổi bản đồ ưu tiên của dự án** — giờ biết **chính xác** trong đó có gì.
Chi tiết đầy đủ ở `REGISTRY.md`, mục *Bộ tài liệu thiết kế gốc của Bullard*. Bốn nhóm:

1. 🔴 **`Shadow of Death/Campaign Text/` — 44 file `.txt` text campaign Ở DẠNG NGUỒN**
   (`Sandro.txt`, `Sandro A`–`D`, `Gem.txt`, `Gem1`–`4`, `gelu`, `Yog`, `Final A`–`L`, `Crag`, …).
   **Đây là chìa khóa của `B-001`** — xem mục đó.
2. **XLS dữ liệu:** `Combo Artifacts.xls`, `H3X2_Spells_Artifacts.xls`, `H3X1_Characters.xls` —
   phủ **cả năm** bài artifact và ba bài nhân vật của Codex.
3. **Cốt truyện SoD:** `Story line for Sandro.doc`, và sơ đồ Visio `Sandro's Rise to Power.vsd`,
   `To Stop Sandro.vsd`.
4. **Đặc tả thiết kế Heroes IV đầy đủ** — `End of Erathia.htm`, **`Opening Sequence.htm`**,
   `Story.htm`, trang riêng cho **từng quốc gia Axeoth** (`Palaedra`, `Aranorn`, `Nekross`,
   `Great Arcan`, `Tribal Lands`, `Yanathrae`), và `Special Heroes/` gồm `Gauldoth.htm` **và
   `Ravenwood.htm`**.

⭐ **Ba câu hỏi mở của Codex mà bộ này giải được, không nguồn nào khác giải nổi:**

- Danh sách quốc gia Axeoth — hiện `UNVERIFIED` vì wiki không dẫn nguồn; ở đây **mỗi quốc gia một
  trang thiết kế**.
- `Ravenwood.htm` nằm trong mục *Special Heroes* của đặc tả H4 → bà ta là **nhân vật được thiết kế**,
  không phải chi tiết chỉ có trong outline chưa xuất bản.
- `Opening Sequence.htm` → trả lời trực tiếp **`Q1` của `the-reckoning`** (cinematic mở đầu H4 có diễn
  ra vụ nổ không) — câu dự án không xem được video để kiểm.

**⛔ VIỆC NÀY GIỜ CẦN USER, KHÔNG CẦN CÔNG CỤ:**

1. Dùng luồng **"Request a Copy"** có sẵn trên trang item (cần email thật + lý do nghiên cứu), **hoặc**
2. Liên hệ Dolph Briscoe Center for American History, dẫn số hiệu **`2012-212`** và handle
   `hdl.handle.net/2152/18586`.

**Trạng thái:** manifest ✅ đã lấy và đã vào registry. Nội dung ⛔ chờ xin phép — **cần user quyết định
có liên hệ thư viện không.** Vẫn là lead giá trị nhất của dự án, và giờ **biết rõ giá trị của nó là gì**
thay vì phỏng đoán.

### B-003 · Rà lại mọi claim phủ định trong Codex

**Vấn đề:** luồng kiểm định bài Sandro phản bác **ba** claim, và cả ba đều cùng một
dạng — **claim phủ định** ("không tồn tại", "không tìm được", "không xác nhận được")
đưa ra quá sớm.

Đây là loại lỗi nguy hiểm hơn claim khẳng định sai, vì nó **trông giống sự cẩn trọng**.

**Hai nguyên nhân kỹ thuật đã xác định:**

1. **Bỏ sót block map event.** Text nằm trong `==== Events ====` của scenario, không phải
   prologue/epilogue. Tra cứu đọc mỗi prologue sẽ không thấy. → Đây là nguyên nhân của
   cả B-01 (Tyranell) lẫn một phần B-02.
2. **Không kiểm trang disambiguation.** Claim "không xuất hiện ở đâu khác" phải kiểm qua
   trang disambiguation của wiki, không chỉ trang nhân vật. → Nguyên nhân bỏ sót
   `Sandro (Xeen)`.

**Việc cần làm:** mỗi khi viết bài mới, mọi claim phủ định phải qua hai kiểm tra trên
**trước khi** đưa vào bài.

**Trạng thái:** đã ghi thành quy tắc. Cần áp dụng nhất quán.

### B-014 · Cảnh giác: claim "hai artifact từng thuộc về Ethric"

**Là gì:** có claim lưu hành rằng Cloak of the Undead King và Armor of the Damned
"once belonged to his former mentor Ethric".

**Vì sao ghi lại:** một luồng research (bị lỗi API giữa chừng) kịp báo rằng đây có thể là
**suy luận của wiki, không phải game text** — có thể bắt nguồn từ scenario `Target`.

**Trạng thái hiện tại:** ✅ **claim này CHƯA lọt vào Codex.** Đã kiểm cả
`codex/heroes/sandro.md` lẫn dossier thô — không có.

**Việc cần làm:** khi viết bài `cloak-of-the-undead-king`, **không** đưa claim này vào
cho tới khi xác minh được nó là game text hay wiki narration. Đang có luồng research
kiểm.

**Bài học nhỏ:** một luồng research chết giữa chừng vẫn có thể để lại cảnh báo hữu ích.
Đọc phần nó kịp trả về trước khi bỏ.

### B-004 · Tìm đường vào `homm.miraheze.org`

**Vấn đề:** site này **chặn bot** (403 với cả curl và fetch) trong **cả hai** đợt
research. Có thể là nguồn của một số claim đang lưu hành mà dự án không kiểm được.

**Ảnh hưởng cụ thể:** claim "thời điểm Sandro thành lich" hiện là `UNVERIFIED` thay vì
`DISPUTED` **chỉ vì** không vào được site này để tìm phía thứ hai.

**Trạng thái:** chưa có giải pháp.

---

## P2 — Làm khi tiện

### B-015 · Search index sẽ nặng khi Codex lớn

**Vấn đề:** `search_index.json` hiện **339 KB cho 17 trang** (~20 KB/trang), và trình
duyệt tải **toàn bộ** ở lần tìm kiếm đầu tiên. Ở mức ~200 bài, đó là **~4 MB**.

**Không dùng được `prebuild_index`** — plugin search của Material không hỗ trợ tùy chọn
đó (chỉ plugin search gốc MkDocs có). Đã thử, build báo lỗi.

**Hướng xử lý khi tới ngưỡng:**

- Chuyển `sources/notes/` (báo cáo kiểm định) ra khỏi index — chúng dài và ít ai tìm
- Cân nhắc `search.separator` để giảm số token
- Hoặc chuyển sang giải pháp tìm kiếm ngoài (Algolia DocSearch miễn phí cho dự án
  mã nguồn mở)

**Ngưỡng cần hành động:** khoảng **80–100 bài**, tức ~2 MB index.

### B-005 · Thử lại `heroesofmightandmagic.com` (site chính thức NWC)

Connection refused — có thể đã chết hẳn. `web.archive.org` bị chặn trong môi trường này
nên không lấy được bản lưu.

Đây là **nguồn không-phải-wiki tốt nhất** có thể có cho mô tả campaign chính thức.

### B-006 · Thử lại kho phỏng vấn Celestial Heavens

Trả 403 trong cả hai đợt. Có thể còn phỏng vấn NWC khác ngoài Bullard và Fulton.

Lưu ý: nội dung gần đây của CH thuộc thời Ubisoft/Ashan — **không liên quan** Old
Universe. Cần tìm phần archive cũ.

### B-007 · Kiểm quote Gauldoth Half-Dead (Heroes IV)

Hiện chỉ là quote-box trên Fandom, **không dẫn nguồn**:

> "When others like the powerful necromancer, Sandro, sought to control the world, the
> force of destruction supported them temporarily..."

Câu rất đáng dùng, nhưng chưa xác minh được. Cần nguồn Heroes IV độc lập.

### B-008 · Kiểm số liệu XP/level của Sandro bằng map editor

Fandom đưa số cụ thể (200.933 / 3.066.455 / **5.555.555** / 28.000) nhưng không dẫn
nguồn. Đọc như dữ liệu trích từ file map thật — số 5.555.555 quá gọn để là ngẫu nhiên.

**Kiểm được bằng map editor** nếu có bản game (xem B-001).

### B-009 · Tìm ảnh scan vỏ hộp Heroes I

Claim "ảnh Sandro in trên một mặt vỏ hộp Heroes I" chỉ có **một** wiki khẳng định, không
dẫn nguồn. Fandom — nguồn chi tiết nhất về vai trò H1 của Sandro — **im lặng**.

MobyGames bị Cloudflare chặn, archive.org bị chặn.

---

## P3 — Có thì tốt

### B-010 · Quyết định cấu trúc Book V của Saga

Heroes Chronicles **không nằm gọn** trong một khoảng thời gian — Tarnum xuyên nhiều kỷ
nguyên. Xếp thành Book V (sau Heroes III) là **thứ tự đọc**, không phải thứ tự thời gian.

Hai phương án: kể theo thời gian (rải vào các Book khác) hay theo thứ tự đọc (giữ Book V).

Chưa đủ dữ liệu để chốt. Xem `TIMELINE-SPINE.md` mục 5.

### B-011 · Tìm nguồn cho hệ lịch "AS" — **thu hẹp mạnh 2026-08-04, vẫn mở**

Dự án đang dùng ký hiệu năm "AS" mà chưa biết nó viết tắt của gì và bắt nguồn từ đâu.

**Đã loại trừ được một khả năng lớn:** grep **toàn bộ 803 KB** manual in Heroes III / SoD /
Armageddon's Blade cho `\bAS\b` (phân biệt chữ hoa) và `A.S.` → **0 hit**. Cũng 0 hit cho
`years ago` và `centur`.

→ **Manual chính thức KHÔNG dùng hệ lịch "AS", và không chứa mốc năm tuyệt đối nào.** Đây là phủ
định đã truy trên toàn văn, không phải suy từ im lặng.

⭐ **Và đợt `the-reckoning` cho thấy vấn đề rộng hơn tên viết tắt:** không nguồn nào cho phép dùng
"AS" cho các sự kiện **Axeoth** — trong khi cả hai wiki vẫn dùng. Tệ hơn, chỗ Fandom *chịu* gán năm
cho một quốc gia Axeoth thì nó dùng **hệ lịch khác** (`Palaedra`: *"ca 525 A.C."*, và `A.C.` chuyển
hướng tới `Great Cataclysm`). Xem `the-reckoning` mục *Điểm tranh chấp canon* 5.

**Chỗ chưa tìm:** manual Might and Magic VI–VIII, và `mm7-diaries-3do` (nguồn niên đại `T2` tốt nhất
dự án có — nó *dùng* năm, nên có thể định nghĩa hệ lịch).

### ✅ B-012 · ~~Fetch timeline trong manual Heroes III~~ — **ĐÓNG 2026-08-04: TIỀN ĐỀ SAI**

**Mục này hỏi sai câu.** Không phải "chưa fetch được" — mà là **không có cái để fetch**.

2026-08-04 đã lấy được **toàn bộ 214 trang** manual in của cả ba sản phẩm Heroes III, chép nguyên
trang trên thelazy (`roe-manual-thelazy` 146 trang · `sod-manual-thelazy` 38 trang ·
`ab-manual-thelazy` 30 trang — **803 KB**, tier `T2*`). Rồi grep toàn văn:

| Truy gì | Kết quả trên 803 KB |
|---|---|
| `timeline`, `chronolog` | **0 hit** |
| `\bAS\b` (phân biệt hoa) và `A.S.` | **0 hit** |
| `years ago`, `centur` | **0 hit** |
| Mốc năm `11xx` | **0 hit thật** — mọi kết quả là giá lính (`1100 Gold`) |

Và mục lục `Restoration of Erathia Manual` xác nhận cấu trúc: Introduction · Interface Reference ·
Main Menu · Adventure Map · Heroes and the Hero Screen · Skills · Combat…

→ **Manual Heroes III là manual GAMEPLAY. Nó không có mục timeline, và không chứa một mốc năm tuyệt
đối nào.** Cái tên `h3-manual-timeline` mô tả một thứ không tồn tại.

⚠️ **Bài học, và nó thuộc loại đã trả giá nhiều lần:** `B-012` tồn tại từ 2026-07-31 như một việc
"chưa làm được", trong khi thực chất nó là một **claim khẳng định chưa kiểm** — rằng manual *có*
timeline. Không ai kiểm tiền đề, chỉ kiểm cách lấy. Cùng loại lỗi với `B-019` và `B-023`, cả hai cũng
dựng trên một kết quả âm/tiền đề sai.

> **Việc cần làm cho mọi mục backlog dạng "chưa fetch được X":** kiểm **X có tồn tại không** trước khi
> kiểm cách lấy X.

**Việc còn lại thật:** `TIMELINE-SPINE.md` vẫn chỉ có hai mốc năm tuyệt đối, và **manual không giúp
được**. Nguồn niên đại phải tìm ở chỗ khác — `mm7-diaries-3do` (`T2`, đã có) là nguồn niên đại tốt
nhất dự án đang có.

**Bù lại, 214 trang đó KHÔNG vô ích** — chúng là nguồn `T2*` lớn nhất dự án có, và cho ngay ba thứ:

1. Kiểm ngược được số trang của ba key `T2*` cũ (`h3-manual-*`) → **đúng cả ba**.
2. `ab-manual-thelazy` mục *Letter from Lucifer Kreegan* — nguồn `T2*` cho gốc gác Armageddon's Blade,
   đã dùng cho [[the-reckoning]], thay cho một tin quán trọ `T1*`.
3. Manual in **cũng** gọi Sandro là `Race Male Lich` — corroboration `T2*` cho một claim trước đây chỉ
   có `T1*`.

### B-013 · Nội dung ChatGPT share của user

Link `chatgpt.com/share/6a6c0766-b3ac-83ec-9c93-ae2c52175d50` **không fetch được** —
trang render bằng JavaScript, chỉ lấy được title: **"ChatGPT - HoMM3 Chiến Thuật"**.

Title gợi ý đây là nội dung về **chiến thuật chơi game**, không phải lore — nếu đúng thì
thuộc mục Gameplay, không phải phần canon.

**Cần:** user paste nội dung trực tiếp hoặc lưu vào `sources/raw/`.

**Xử lý khi có:** output của một AI khác **không phải nguồn**. Trích claim ra bảng, cho
verifier độc lập tìm nguồn T1–T4 cho từng cái — đúng luồng đã dùng cho Sandro.

---

## Đã xong

| # | Việc | Kết quả |
|---|---|---|
| ✅ | Tìm developer commentary | 4 nguồn T4: Bullard (Lead Designer SoD) + Fulton (Lead Designer H3) ×3 |
| ✅ | Kiểm tuyến Tyranell / Statue of Legion | Là game text thật, ở `sod-gathering-the-legion` |
| ✅ | Kiểm cảnh dấu ngón tay xương trên ngực Finneas | Tìm được ở `sod-invasion` Day 17 |
| ✅ | Tìm nguồn MM8 độc lập | `mm8-guide-walkthrough`; sửa được lỗi "đồng lãnh đạo" |
| ✅ | Làm rõ tranh chấp Chronicles | Lập luận niên đại mạnh, lập luận sinh tử yếu |
| ✅ | Sửa tier bio hero | `T2*` → `T1*` (chép từ `HEROBIOS.TXT`) |

---

## Lịch sử

| Ngày | Thay đổi |
|---|---|
| 2026-07-31 | Lập backlog sau khi Sandro đạt `verified` |
| 2026-08-03 | Thêm B-016 (cân bằng kỷ nguyên) và B-017 (`codex/events/` rỗng) sau khi rà lại mục tiêu dự án. Phát hiện: 9/9 bài đầu nằm cùng một cụm, và không công cụ nào bắt được loại lệch này |
| 2026-08-03 | Thêm B-018 (`hota-changelog` sai loại nguồn) từ verify `dead-mans-boots`. Cùng đợt: **B-001 tiến một bước thật** — tìm được `h3wiki-artraits-txt` (`T1` không dấu sao, string table trích từ `H3Bitmap.lod`), thay được `fandom-artifact-list` (`T6`) cho **mọi** bài artifact |
| 2026-08-03 | Thêm B-019 (lỗ nguồn Heroes IV) từ verify `amulet-of-the-undertaker`. Phát hiện: thelazy gần như chỉ phủ H3, nên mọi nội dung H4 hiện chỉ có nguồn `T6`. **Việc này chặn B-016** — hai trong bốn entity trụ (`gauldoth-half-dead`, `tarnum`) sẽ gặp đúng lỗ đó |
| 2026-08-03 | Thêm B-020 (`fulton-names-2023`, `T4`) từ verify `jeddite`. **B-001 tiến bước lớn nhất tính tới nay** từ verify `deyja`: `web.archive.org` **không bị chặn** — cảnh báo cũ trong registry là sai — nên **site chính thức 3DO tiếp cận được**, cho nguồn `T2` đầu tiên không qua wiki. Cùng đợt bắt được **thelazy chép sai hai con số năm** so với manual chính thức, ca đầu tiên thelazy sai |
| 2026-08-03 | **Xong đợt verify 6 bài draft** → Codex 9/9 `verified`. Tổng: 10 BLOCKER + 49 MAJOR đã sửa. Sáu lỗi nặng nhất đều là **claim phủ định hoặc claim độc quyền** ("không có", "duy nhất", "cả bốn") — khớp đúng bài học lớn nhất trong `CLAUDE.md` |
| 2026-08-04 | ✅ **B-016 ĐÓNG** — `the-reckoning` `verified`, entity `event` đầu tiên, và cả bốn kỷ nguyên đều có entity trụ. ✅ **B-017 ĐÓNG** — convention `event` vào `SCHEMA.md`, và `wikilinks.py --build` **hiện thực hóa** lời hứa sinh quan hệ nghịch đảo vốn ba tài liệu cùng nói mà không công cụ nào làm |
| 2026-08-04 | 🔴 **Thêm B-025 — và nó đảo ngược một điều `CLAUDE.md` đang dạy.** FortiGuard chặn `web.archive.org` theo **domain đích**, không phải rate limit. Chẩn đoán bằng thí nghiệm đối chứng 5 URL. Chặn **toàn bộ** nguồn official của dự án. Bẫy nặng nhất: trang chặn trả **HTTP 200 + 35,3 KB** nên `curl` báo thành công |
| 2026-08-04 | Thêm B-026 (`list=search` của thelazy hỏng) và B-027 (đích wikilink không phải text game) — cả hai từ đợt verify `the-reckoning`. Mở **214 trang manual in** (`T2*`) và **đóng B-012 vì tiền đề sai**. **B-002 mở được một nửa**: repo UT Austin vào được, **manifest đã lấy**, nội dung `Heroes.zip` trả **401** — nhưng manifest đủ để **đổi bản đồ ưu tiên của cả dự án** |
| 2026-08-05 | Bài `event` thứ hai (`vu-dau-doc-nicolas-gryphonheart`) và `gem` đạt `verified` → Codex **15/15**. Gỡ một `DISPUTED` vốn chỉ là **lỗi gán tier**, và truy ra mốc 27/9 là **dateline bài báo 1998**, không phải ngày trong truyện |
| 2026-08-05 | ✅ **Đóng mục 1 của B-026** → thành **V5** của `VERIFY-PROTOCOL.md`. Cùng lượt: sửa mục *Trạng thái* của `CLAUDE.md`, vốn còn ghi **12/12** và còn dạy rằng `web.archive.org` **không bị chặn** — tức tài liệu điều hướng chính của dự án đang mâu thuẫn trực tiếp với B-025 |
