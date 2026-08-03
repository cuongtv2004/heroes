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

**Trạng thái:** chưa bắt đầu. Cần user xác nhận có bản game không.

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
| 3 | `gauldoth-half-dead` | Kỷ Axeoth (H4) | Dọn luôn B-007 |
| 4 | `tarnum` | Xuyên kỷ | Buộc phải chốt B-010 (cấu trúc Book V) |

**Trạng thái:** luật đã vào `WORKFLOW.md` (2026-08-03). **Mục 1 xong** — `archibald-ironfist` đã
`verified`, kỷ nguyên Age of Kings không còn trống. Còn ba entity trụ.

✅ **Đánh giá "hai mục còn lại bị `B-019` chặn" đã sai — và cả hai lý do đều sai:**

- `gauldoth-half-dead` — **không còn bị chặn**: `B-019` đã giải, và site chính thức NWC có **đủ sáu
  trang** campaign *Half-Dead* ở tier `T2`. Đây giờ là entity trụ **dễ làm nhất** trong ba mục còn lại.
- `tarnum` — **chưa bao giờ bị chặn**. Đã kiểm: trang `Tarnum` trên thelazy có **18.754 byte**, phủ
  đủ tám campaign *Heroes Chronicles* kèm bảng class, và nhắc Axeoth/Reckoning. Tarnum là nhân vật
  **Chronicles**, không phải nhân vật H4 — mà Chronicles thì thelazy phủ tốt. Việc xếp hắn vào diện
  "chặn bởi lỗ nguồn H4" là **lỗi phân loại**.

**Thứ tự đề xuất cho ba mục còn lại:** `gauldoth-half-dead` (nguồn `T2` đã sẵn) → `tarnum` (nguồn
`T1*` đã sẵn, nhưng phải chốt `B-010` về cấu trúc Book V) → `the-reckoning` (khó nhất, `TIMELINE-SPINE`
mục 6 ghi "chưa có nguồn").

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

**Cần gì trước:** chốt convention cho `event` — quan hệ `before`/`after`/`concurrent_with`,
cách gắn `date_certainty`, và cách tránh trùng lặp với nội dung đã có trong bài entity.

**Trạng thái:** chưa bắt đầu. Làm sau B-016 mục 1.

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

**Lời giải:** mục `heroes4/` của `heroesofmightandmagic.com` — **site chính thức của New World
Computing** — được lưu **đầy đủ** trong `web.archive.org`: khoảng **200 URL**, tier **`T2`**.

Gồm: `artifacts_{minor,major,relic,treasure,potion,tgs}.shtml`,
`heroes_{necromancers,deathknights,lords,magi,priests,sorcerers,thieves,archers,barbarians,druids,knights,campaign}.shtml`,
`creatures_*.shtml`, `buildings_*.shtml`, và **toàn bộ sáu campaign** (`halfdead`, `blade`, `daughter`,
`elwin`, `glory`, `price`).

**Đã dùng ngay:** bài `amulet-of-the-undertaker` nâng mục Heroes IV từ `T6` lên **`T2`** và **đóng
câu hỏi mở Q3**. Câu mô tả artifact trên site chính thức khớp **từng chữ** với bản Fandom — nên Fandom
đúng là bản chép, nhưng giờ không cần dùng bản chép.

**Vì sao trước đây tưởng là bế tắc:** hai giả định sai cùng lúc trong `REGISTRY.md` — rằng
`web.archive.org` **bị chặn**, và rằng `heroesofmightandmagic.com` **đã chết**. Cả hai đều đã được sửa
cùng ngày. Bản thân `B-019` là hệ quả của hai cái sai đó, không phải một lỗ nguồn thật.

⚠️ **thelazy vẫn KHÔNG phủ Heroes IV** — đã kiểm: `Heroes_of_Might_and_Magic_IV` và
`Gauldoth_Half-Dead` đều trả **0 byte**, và cả **56 trang `Translation Data/`** đều là file **Heroes
III**. Nên vẫn không có string table `T1` cho H4. Nhưng `T2` chính thức thì đủ tốt.

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

### B-022 · Khai thác nốt ~200 URL Heroes IV trên site chính thức NWC

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

**Trạng thái:** chưa fetch. **Lead giá trị nhất chưa khai thác của dự án.**

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

### B-011 · Tìm nguồn cho hệ lịch "AS"

Dự án đang dùng ký hiệu năm "AS" mà chưa biết nó viết tắt của gì và bắt nguồn từ đâu.

### B-012 · Fetch timeline trong manual Heroes III

`h3-manual-timeline` được nhắc tới trong nhiều nguồn nhưng **chưa fetch được**. Sẽ giúp
nhiều cho `TIMELINE-SPINE.md`, hiện chỉ có **hai** mốc năm tuyệt đối.

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
