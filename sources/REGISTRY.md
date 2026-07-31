# SOURCE REGISTRY

Sổ nguồn của dự án. **Mọi source key dùng trong Codex và Saga phải có mặt ở đây.**

Cách đọc một entry:

- `key` — mã dùng trong nhãn, ví dụ `{T1* EXPLICIT: sod-target-prologue}`
- `tier` — cấp nguồn theo `CANON-POLICY.md` mục 2. `T1*` = in-game text tiếp cận qua
  trung gian (dự án không có file game gốc để đối chiếu)
- `access` — `FETCHED` (đã đọc trực tiếp) / `FAILED` (thử nhưng không vào được) /
  `NOT_FETCHED` (chưa thử)

---

## Lưu ý về `T1*` — bắt buộc đọc trước khi dùng

Toàn bộ text in-game trong registry này đến từ **heroes.thelazy.net**, lấy qua
`?action=raw` (wikitext thô, không qua render).

Đây **không** phải file game gốc. Nó là bản chép của một fan wiki. Do đó mọi nguồn
loại này mang tier `T1*`, không phải `T1`.

**Lý do vẫn tin ở mức cao:**

- Wiki này chép nguyên cả **lỗi chính tả trong game**, và đánh dấu bằng `{{sic}}`
  — ví dụ `{{sic|is problem with}}`, `{{sic|populous|populace}}`
- Có HTML comment `<!--Error in story text-->` ở chỗ tên Dethmar/Dethard không khớp
- Tách bạch text chính thức khỏi ý kiến fan bằng wrapper `{{user commentary}}`
  và `{{fanopinion}}`
- Tự nêu vấn đề canon (xem `h3wiki-sandro`, mục "Historical counterpart") thay vì
  khẳng định bừa

Đây là dấu hiệu của bản chép trung thực, không phải diễn giải. Nhưng vẫn cách nguồn
gốc **một bước**.

**Việc cần làm để nâng `T1*` → `T1`:** trích text trực tiếp từ file campaign
`.h3c` của Shadow of Death. Chưa làm được trong phiên này.

---

## Nhóm 1 — Text in-game Heroes III (T1*)

### Bio & tổng quan

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-sandro` | T1* | FETCHED | `heroes.thelazy.net/index.php?title=Sandro&action=raw` — bio chính thức H3, stat block đầy đủ, bảng xuất hiện theo campaign, mục "Historical counterpart" nêu vấn đề Chronicles |
| `h3wiki-shadow-of-death` | T1* | FETCHED | Trang tổng quan expansion; tóm tắt cốt truyện, danh sách campaign |

### Manual chính thức (T2, qua trung gian)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3-manual-rise-of-necromancer` | T2* | FETCHED | Manual tr.15 — mô tả campaign *Rise of the Necromancer* |
| `h3-manual-unholy-alliance` | T2* | FETCHED | Manual tr.15 — mô tả campaign *Unholy Alliance* |
| `h3-manual-specter-of-power` | T2* | FETCHED | Manual tr.16 — mô tả campaign *Specter of Power* |

### Campaign: Rise of the Necromancer (Sandro là người chơi)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `sod-target` | T1* | FETCHED | Scenario *Target* — prologue, 6 timed event (có thư Jeddite), map event (Jabarkas/con gái, Ufretin), danh sách hero |
| `sod-master` | T1* | FETCHED | Scenario *Master* — prologue, Vidomina xuất hiện, tuyến tình cảm, cảnh skeleton bàn tán, sự kiện các tộc dwarf |
| `sod-finneas-vilmar` | T1* | FETCHED | Scenario *Finneas Vilmar* — prologue, text "puppet king" Day 1, cảnh cải trang giết dwarf (event 5,28) |
| `sod-duke-alarice` | T1* | FETCHED | Scenario *Duke Alarice* — prologue, **epilogue**, danh sách hero (chứng minh Necromancer ≠ Death Knight) |

### Campaign: New Beginning (Gem bị lừa)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `sod-after-the-amulet` | T1* | FETCHED | Cảnh Sandro lừa Gem, vỏ bọc "nghiên cứu chống necromancy" |
| `sod-retrieving-the-cowl` | T1* | FETCHED | Tuyến Terek — điệp viên của Sandro bị bắt |
| `sod-driving-for-the-boots` | T1* | FETCHED | **Epilogue Gem phát hiện bị lừa** |

### Campaign: Hack and Slash (Crag Hack bị lừa)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `sod-bashing-skulls` | T1* | FETCHED | **Cảnh tuyển mộ ở Wingtail Tavern** — miêu tả ngoại hình Sandro |
| `sod-black-sheep` | T1* | FETCHED | Nhiệm vụ thứ hai của Crag Hack |
| `sod-a-cage-in-the-hand` | T1* | FETCHED | Nhiệm vụ thứ ba — Rib Cage |
| `sod-grave-robber` | T1* | FETCHED | Nhiệm vụ thứ tư — **epilogue Crag Hack bị lừa** |

### Campaign: Unholy Alliance (Sandro là phản diện)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `sod-wrath-of-sandro` | T1* | FETCHED | Prologue + region text — Sandro chủ động dụ bốn hero vào |
| `sod-invasion` | T1* | FETCHED | Prologue + region text |
| `sod-union` | T1* | FETCHED | Region text + prologue Gem — Angelic Alliance |
| `sod-fall-of-sandro` | T1* | FETCHED | Region text, prologue Gem, **epilogue Yog** — phá hủy và phân tán artifact |
| `sod-secrets-revealed` | T1* | FETCHED | Yog + Crag Hack hợp lực |
| `sod-agents-of-vengeance` | T1* | FETCHED | Gelu/Gem điều tra, **thư Ethric gửi Gem** |

### Campaign: Specter of Power (Sandro là người chơi)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `sod-poison-fit-for-a-king` | T1* | FETCHED | Prologue, **đoạn độc thoại nội tâm Day 20 "The Plan"**, thỏa thuận với Lord Haart |
| `sod-to-build-a-tunnel` | T1* | FETCHED | Thỏa thuận đào hầm với Nighon — giá 100.000 vàng |
| `sod-kreegan-alliance` | T1* | FETCHED | Liên minh Kreegan, Eversmoking Ring, Melodia, thư Dethmar |
| `sod-with-blinders-on` | T1* | FETCHED | Bẫy Lord Smedth, **epilogue trong tù — câu cuối của Sandro trong toàn arc** |

### Các scenario khác

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `roe-season-of-harvest` | T1* | FETCHED | Restoration of Erathia — Sandro bị giam, event Day 5, hero `imprisoned` tại 9,34 |
| `ab-march-of-the-undead` | T1* | FETCHED | Armageddon's Blade — Sandro là địch, level 14 |
| `hc-truth-within-nightmares` | T1* | FETCHED | Heroes Chronicles *Conquest of the Underworld* — Tarnum vs Sandro. **Xem cảnh báo DISPUTED bên dưới** |

### Artifact

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-cloak-undead-king` | T1* | FETCHED | Cơ chế, thành phần, hạn chế trong HotA 1.7.2 |
| `h3wiki-armor-of-the-damned` | T1* | FETCHED | Cơ chế, thành phần, synergy với hero |

### Nhân vật liên quan

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-ethric` | T1* | FETCHED | Ethric the Mad — lich đầu tiên, chết trong MM6, hộp sọ về tay Gabriel Cartman |
| `h3wiki-jeddite` | T1* | FETCHED | Bạn thân cũ, người giới thiệu Sandro với Ethric; bio H4 |
| `h3wiki-vidomina` | T1* | FETCHED | Học trò; Yog từng yêu; bio H3+H4 |
| `h3wiki-finneas` | T1* | FETCHED | Puppet king; hero campaign-only; portrait dựa trên Thant |
| `h3wiki-thant` | T1* | FETCHED | **Xác nhận Thant KHÔNG có vai trò cốt truyện trong H3** |
| `h3wiki-nimbus` | T1* | FETCHED | Vai trò MM7/RoE; **xác nhận không có liên hệ với Sandro** |
| `h3wiki-lord-haart` | T1* | FETCHED | **Nguồn của mâu thuẫn "theo lệnh Finneas Vilmar"** |
| `h3wiki-jabarkas` | T1* | FETCHED | Hero Stronghold; bio ghi là con Duke Boragus — **không** có nội dung về Ethric hay con gái |

---

## Nhóm 2 — Wiki cộng đồng, không có dẫn nguồn (T6)

⚠️ **Theo `CANON-POLICY.md`: nguồn T6 không bao giờ đủ để một claim đạt `CANON`.**
Chỉ dùng để dẫn đường tới T1–T4.

| key | tier | access | Nội dung & cảnh báo |
|-----|------|--------|---------------------|
| `fandom-sandro-enroth` | T6 | FETCHED | Might and Magic Wiki, lấy qua `api.php?action=parse&prop=wikitext`. Tiểu sử dài nhất, số XP/level H3, vai trò MM8, quote Gauldoth. **CẢNH BÁO: toàn bài KHÔNG có một inline citation nào.** Chỉ có 2 HTML comment xác định bio H3 và H4 là chính thức |
| `fandom-warlock-h1` | T6 | FETCHED | Xác nhận Sandro trong roster Warlock của Heroes I |
| `fandom-necromancer-h2` | T6 | FETCHED | Xác nhận Sandro là Necromancer **chuẩn** (không phải campaign-only) ở Heroes II |
| `kmcgames-sandro` | T6 | FETCHED | `kmcgames.wikidot.com/sandro`. **Chất lượng thấp.** Là văn fan tự viết, không phải tài liệu tham khảo. Có lỗi rõ ("Colony" thay vì Enroth), thêm bình phẩm kiểu TV Tropes. Dùng hết sức thận trọng |
| `ch-walkthrough-302` | T6 | FETCHED | Celestial Heavens walkthrough *Wrath of Sandro* — chiến thuật, không có transcript |
| `ch-walkthrough-303` | T6 | FETCHED | Celestial Heavens walkthrough *Invasion* |
| `ch-walkthrough-307` | T6 | FETCHED | Celestial Heavens walkthrough *Fall of Sandro*. Số liệu hữu ích: Sandro trận cuối có 13 Attack / 14 Defense / 17 Power / 7 Knowledge, bị chặn sau Quest Gate cần Boots of Levitation |

---

## Nhóm 3 — Nguồn thử nhưng KHÔNG vào được

Ghi lại để lần sau thử tiếp. **Không được dùng làm nguồn.**

| Nguồn | Trạng thái | Ghi chú |
|-------|-----------|---------|
| `mightandmagic.fandom.com/wiki/*` | FAILED (402/403) | Chỉ vào được qua `api.php` |
| `homm.miraheze.org/wiki/Sandro` | FAILED (403) | |
| `strategywiki.org/.../Rise_of_the_Necromancer` | FAILED (403) | |
| `heroesofmightandmagic.com/heroes3sod/campaigns.shtml` | FAILED (connection refused) | **Site chính thức của NWC, có thể đã chết.** Đây là nguồn không-phải-wiki tốt nhất có thể có |
| `web.archive.org` | FAILED (bị chặn hoàn toàn) | Nên không lấy được bản lưu của site chính thức |
| `en.namu.wiki/.../Sandro` | NOT_FETCHED | Chỉ thấy trong kết quả tìm kiếm |
| File campaign `.h3c` gốc | NOT_FETCHED | **Đây là việc cần làm để nâng T1\* thành T1** |

---

## Nhóm 4 — Nguồn KHÔNG tồn tại

| Loại | Kết luận |
|------|----------|
| **Developer commentary về Sandro** | **KHÔNG TÌM ĐƯỢC GÌ.** Không có phỏng vấn nào của NWC về Sandro hay cốt truyện SoD. Ba đường còn lại đều tắc: archive.org bị chặn, site chính thức đã chết, báo game 1999–2000 không tìm được. **Codex tuyệt đối không được khẳng định "ý định của developer" về Sandro** |

---

## Cảnh báo DISPUTED gắn với source key

Ghi ở đây để người viết không vô tình dùng nguồn sai.

### `hc-truth-within-nightmares` — có thể KHÔNG phải Sandro của chúng ta

`h3wiki-sandro` mục "Historical counterpart" tự nêu:

> "Although represented by Sandro in-game, he is probably only a namesake, since
> according to Ethric and Jeddite, their Sandro became a necromancer decades before
> the Restoration Wars, and those events happened centuries prior. Also, the
> scenario description strongly hints that Tarnum killed the Underworld Sandro."

Hai vấn đề độc lập: **niên đại** (Chronicles xảy ra trước hàng trăm năm) và
**sinh tử** (Tarnum có vẻ đã giết hắn, nhưng Sandro còn sống sau đó).

`fandom-sandro-enroth` liệt kê Conquest of the Underworld trong danh sách xuất hiện
**không kèm cảnh báo nào** → hai wiki lớn bất đồng thật sự.

**Xử lý:** claim này bắt buộc `DISPUTED`. Không được ghi Sandro xuất hiện trong
Chronicles như dữ kiện.

### `h3wiki-lord-haart` vs `sod-poison-fit-for-a-king` — ai ra lệnh đầu độc?

- `h3wiki-lord-haart`: Haart đầu độc nhà vua **"theo lệnh Finneas Vilmar"**
- `sod-poison-fit-for-a-king` (prologue, chính Sandro nói): đây là kế của **Sandro**,
  Haart là công cụ
- `h3-manual-specter-of-power`: ghi công cho kế hoạch của Sandro, "the corrupted
  Lord Haart"
- `fandom-sandro-enroth` dung hòa bằng cách gọi Haart là "điệp viên hai mang của Vilmar"

**Xử lý:** `DISPUTED`. Cách diễn đạt an toàn: Sandro cung cấp thuốc độc và dàn kế;
Haart ra tay; **lòng trung thành cuối cùng của Haart (Sandro hay Finneas) thì các
nguồn nói khác nhau**.

### `h3wiki-sandro` (bio chính thức) tự mâu thuẫn với campaign text

Bio chính thức H3: *"Sandro first studied **Necromancy** under the tutelage of the
wizard, and later the lich, Ethric."*

Nhưng toàn bộ campaign text nói ngược: Ethric dạy **warlock**, nổi giận vì Sandro
thành necromancer, và truy sát hắn vì điều đó. `h3wiki-ethric` ghi Ethric "trained
him to be a warlock and objected to him becoming a necromancer."

**Xử lý:** đây là mâu thuẫn **trong chính tư liệu chính thức**. Theo
`CANON-POLICY.md` R1 (cùng game, in-game thắng manual/bio), campaign text thắng.
Nhưng phải nêu rõ mâu thuẫn, không được im lặng chọn bên.

---

## Cần bổ sung sau

| Việc | Vì sao |
|------|--------|
| Trích text từ file `.h3c` | Nâng toàn bộ `T1*` → `T1`. Là hạn chế lớn nhất hiện tại |
| Thử lại `heroesofmightandmagic.com` qua proxy khác | Nguồn chính thức duy nhất còn khả năng |
| Tìm nguồn MM8 độc lập | Toàn bộ phần MM8 hiện chỉ có `fandom-sandro-enroth` (T6, không dẫn nguồn) |
| Kiểm quote Gauldoth Half-Dead (H4) | Hiện chỉ là quote-box trên Fandom, không dẫn nguồn |
| Kiểm tuyến Tyranell / Statue of Legion | `h3wiki-sandro` khẳng định nhưng chưa tìm được scenario text chống lưng |
| Kiểm cảnh "dấu ngón tay xương trên ngực Finneas" | `h3wiki-finneas` kể nhưng không rõ từ scenario nào |

---

## Lịch sử sửa đổi

| Ngày | Thay đổi |
|------|----------|
| 2026-07-31 | Bản đầu — 47 nguồn từ đợt research Sandro |
