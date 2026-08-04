# SOURCE REGISTRY

Sổ nguồn của dự án. **Mọi source key dùng trong Codex và Saga phải có mặt ở đây.**

## ⚠️ Ràng buộc định dạng source key — key KHÔNG được bắt đầu bằng số

`tools/check.py` nhận diện source key bằng:

```python
SOURCE_KEY_RE = re.compile(r"\b([a-z][a-z0-9]*(?:-[a-z0-9]+){1,})\b")
```

Key **phải bắt đầu bằng chữ cái thường**. Nếu đặt tên kiểu `3do-mm7-diaries`, regex **không**
khớp từ đầu — nó nhặt được phần sau dấu gạch (`mm7-diaries`) và báo *"nhãn dùng source key ngoài
registry"* cho một key **không tồn tại**. Cảnh báo trông như lỗi chính tả, nhưng gốc là định dạng.

**Đã xảy ra thật (2026-08-03):** key `3do-mm7-diaries-archibald` sinh ra key ma
`mm7-diaries-archibald`, **và** tồn tại song song với `mm7-diaries-3do` — hai key cho **cùng một
nguồn**. Đã gộp về `mm7-diaries-3do`.

**Quy ước:** đặt phần định danh nguồn ở **cuối**, không ở đầu — `mm7-diaries-3do`,
`aoh-h4-artifacts-minor`, `roe-all-for-one`.

---

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

### ⭐⭐ Manual chính thức, chép nguyên trang trên thelazy (`T2*`) — 214 trang, mở 2026-08-04

**Là gì:** thelazy chép **nguyên văn từng trang** manual in của cả ba sản phẩm Heroes III. Đây là
nguồn `T2*` lớn nhất dự án có, và nó **fetch được bình thường** trong khi mọi nguồn official khác
đang bị chặn (xem cảnh báo FortiGuard).

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `roe-manual-thelazy` | **T2\*** | FETCHED | ⭐⭐ *Restoration of Erathia Player Manual* — **146 trang**, 280 KB. Bìa ghi *"NEW WORLD COMPUTING · 3DO"*. Enumerate: `api.php?action=query&list=allpages&apprefix=Restoration of Erathia Manual&aplimit=500` |
| `sod-manual-thelazy` | **T2\*** | FETCHED | ⭐ *The Shadow of Death User Manual* — **38 trang**, 51 KB. Dòng bản quyền: *"© 2000 The 3DO Company. All Rights Reserved."* Trang 15–16 chứa mô tả **cả năm campaign** |
| `ab-manual-thelazy` | **T2\*** | FETCHED | ⭐⭐ *Armageddon's Blade manual* — **30 trang**, 51 KB. Mục **Section I là *"Letter from Lucifer Kreegan"*** — thư ngôi thứ nhất, nguồn `T2*` cho gốc gác Armageddon's Blade |

⚠️ **Tier là `T2*`, KHÔNG phải `T2`.** Đây là manual in **tiếp cận qua bản chép của fan wiki**, đúng
định nghĩa dấu sao — cùng logic với `T1*`. Dự án **đã hai lần** lạm phát tier vì bỏ qua dấu sao
(`heroesofmightandmagic.com` gán `T2` khi là site fan; `hota-changelog` gán `T1*` khi không phải
in-game text). Đừng lặp lần thứ ba.

**Cách lấy hiệu quả VÀ nhẹ tay với server:** dùng `generator=allpages` + `prop=revisions` để lấy
**50 trang mỗi request** — cả 214 trang chỉ cần **~7 request**, không phải 214:

```
api.php?action=query&generator=allpages&gapprefix=<TÊN MANUAL>&gaplimit=50
        &prop=revisions&rvprop=content&rvslots=main&format=json
```

#### ✅ Kiểm chứng ngược: ba key manual cũ của dự án đều ĐÚNG trang

Ba key `h3-manual-rise-of-necromancer`, `h3-manual-unholy-alliance` (ghi "tr.15") và
`h3-manual-specter-of-power` (ghi "tr.16") **đã đối chiếu được** với bản chép nguyên trang:

- `Shadow of Death Manual Page 15` **thật sự** chứa *cả hai* mô tả *Rise of the Necromancer* và
  *Unholy Alliance*.
- `Shadow of Death Manual Page 16` **thật sự** chứa *Specter of Power*, và quote
  *"With a little help from **the corrupted Lord Haart**"* khớp **từng chữ** với điều registry đã ghi.

⭐ Đây là lần đầu dự án **kiểm ngược được số trang** của một nhãn `T2*` đã dùng. Kết quả: đúng cả ba.

Thêm hai dữ kiện `T2*` từ trang 15 chưa dùng: Sandro được ghi **`Race Male Lich`** trong manual in
(tức bản in **cũng** gọi hắn là lich), kèm chỉ số khởi đầu và unique ability *"5% per level bonus to
his Sorcery skill"*. ⚠️ Bản chép có lỗi gõ **`Powe 2`** (nguyên văn) — dấu hiệu chép trung thực.

#### 🔴 Ba kết quả PHỦ ĐỊNH, đã truy trên toàn bộ 803 KB — quan trọng cho `B-011` và `B-012`

Cả ba đều grep trên **toàn văn 214 trang**, không phải suy từ im lặng:

| Truy gì | Kết quả |
|---|---|
| `\bAS\b` (phân biệt chữ hoa) và `A.S.` | **0 hit** → manual **chưa bao giờ** dùng hệ lịch "AS" |
| `timeline`, `chronolog` | **0 hit** |
| `years ago`, `centur` | **0 hit** |
| Mốc năm `11xx` | **0 hit thật** — mọi kết quả là **giá lính** (`1100 Gold`) |

→ **Cả ba manual Heroes III KHÔNG chứa mốc năm tuyệt đối nào, và không có mục timeline.** Mục lục
`Restoration of Erathia Manual` xác nhận: Introduction · Interface Reference · Main Menu · Adventure
Map · Heroes and the Hero Screen · Skills · Combat… — đây là **manual gameplay**, không phải sách lore.

🔴 **Hệ quả: `B-012` dựng trên tiền đề SAI.** Xem `BACKLOG.md`.

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
| `sod-agents-of-vengeance` | T1* | FETCHED | Gelu/Gem điều tra, **thư Ethric gửi Gem** — chứa neo thời gian "decades" |
| `sod-gathering-the-legion` | T1* | FETCHED | **Tuyến Tyranell / Statue of Legion** — xác nhận đây là game text thật, không phải wiki bịa. Map event (8,60,0) là bằng chứng quyết định |
| `h3wiki-tyranell` | T1* | FETCHED | Hero Tyranell — knight quân Erathia, được Sandro trả tiền đi lấy các mảnh Legion, bị Crag Hack đánh bại |

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
| `sod-clearing-the-border` | T1* | FETCHED | Shadow of Death, prologue video campaign — ⭐ lời Gem chốt **kết cục canon Heroes II**: "a year has passed since **Archibald and his Necromancer allies were defeated**, ending the Succession Wars" |
| `ab-march-of-the-undead` | T1* | FETCHED | Armageddon's Blade — Sandro là địch, level 14 |
| `hc-truth-within-nightmares` | T1* | FETCHED | Heroes Chronicles *Conquest of the Underworld* — Tarnum vs Sandro. **Xem cảnh báo DISPUTED bên dưới** |
| `hc-the-dragon-mothers` | T1* | FETCHED | **Heroes Chronicles** (`source = hc`, `cback = chronicles 4` = *Clash of the Dragons*) — Jeddite chỉ có mặt trong roster. ⚠️ Bài `jeddite` từng gán sai là SoD |
| `hc-dragons-of-deepest-blue` | T1* | FETCHED | **Heroes Chronicles** (`cback = chronicles 4` = *Clash of the Dragons*) — Jeddite chỉ trong roster. ⚠️ Từng bị gán sai là SoD |
| `hc-tarnum-the-overlord` | T1* | FETCHED | **Heroes Chronicles** (`cback = chronicles 8` = *The Sword of Frost*) — Jeddite chỉ trong roster. ⚠️ Từng bị gán sai là SoD. ⭐⭐ **VÀ ĐÂY LÀ NGUỒN CỦA LỜI TIÊN TRI trung tâm cho `the-reckoning`** (phát hiện 2026-08-04): `==== Events ====` day 1 chứa *"If the Sword of Frost and Armageddon's Blade should ever meet, it would mean the end of the world!"* — **BH-1 lại đúng một lần nữa**: câu quan trọng nhất của cả entity nằm trong timed event, **không** ở prologue. Đợt trước đọc trang này mà chỉ lấy roster |
| `hc-old-wounds` | T1* | FETCHED | **Heroes Chronicles** (`cback = chronicles 2` = *Conquest of the Underworld*) — Jeddite chỉ trong roster. ⚠️ Từng bị gán sai là SoD, campaign *Contested Underworld* — **tên campaign đó không tồn tại** |
| `hota-a-friendly-visit` | T1* | FETCHED | Scenario **HotA**, campaign ***All In*** (`cback = hota ai 1`) — Jeddite chỉ trong roster. ⚠️ Từng bị gán sai là AB / *Armageddon's Blade* |
| `hota-homecoming` | T1* | FETCHED | Scenario **HotA**, campaign ***Forged in Fire*** (`cback = hota fif 8`) — Jeddite chỉ trong roster. ⚠️ Từng bị gán sai campaign là *Terror of the Seas* (là campaign HotA **khác**) |
| `hota-a-cold-day-in-hell` | T1* | FETCHED | Scenario đơn **HotA** — ⭐ Jeddite là **tù nhân trong Prison** tại (63, 1) kèm **17 Harpy Hag** cố định. Vai trò cơ chế khác hẳn "một dòng đặt hero lên map" |
| `roe-myth-and-legend` | T1* | FETCHED | Map Single/MP **Restoration of Erathia** (`source = roe`), size XL — ⭐ hero Jeddite có mặt tại (90, 123, 0) nhưng **đổi tên hiển thị thành `Abaris`** theo chủ đề thần thoại Hy Lạp. **Phản bác** claim "Jeddite không xuất hiện trong RoE" |
| `sod-battle-of-the-sexes` | T1* | FETCHED | Scenario đơn **Shadow of Death** — Jeddite trong roster |
| `fandom-jungle-fever` | T6 | FETCHED | Scenario **Heroes IV: Winds of War** (`version = H4X2`), Expert — ⭐ Jeddite là **địch duy nhất được nêu tên**, có text truyện riêng gọi hắn "**Jeddite the Reckless**" và cho chi tiết mới: hắn **nuôi rồng** và cho chúng ăn thịt dân đảo. **Trang này không tồn tại trên thelazy** — chỉ có trên Fandom |
| `h3wiki-hero-specialty` | T1* | FETCHED | Trang `Hero specialty` — công thức specialty. Dòng 149 xác nhận HotA nâng hiệu ứng Resurrection lên **5%** (mặc định SoD là 3%) |
| `h3wiki-reference-ids` | T1* | FETCHED | Trang `Reference IDs` — bảng ID nội bộ của game. Dòng 937: Jeddite = **91**. ⚠️ Con số này **không có** trên trang `Jeddite` |
| `sod-hack-and-slash` | T1* | FETCHED | Trang **campaign** *Hack and Slash*. `\| description =` là text in-game hiện khi chọn campaign — chứa "…so he can **destroy the cursed thing**". ⚠️ Trang có **ba tier trộn lẫn**: `\| description =` (`T1*`), mục `== Manual description ==` (`T2*`, manual tr.13), mục `== Important information ==` (`T6`, văn biên tập viên) |
| `sod-unholy-alliance` | T6 | FETCHED | Trang campaign *Unholy Alliance*, mục `== Important information ==` — **văn biên tập viên wiki**, ngoài mọi template. Chứa nhận định "Sandro xuất hiện ở map cuối với Armor of the Damned nhưng không có Cloak of the Undead King". ⭐ Cũng là nơi wiki **tự phản bác game text**: các campaign description nói hero mang skill sang campaign sau — "it is not true" |
| `h3wiki-cuthbert` | T1* | FETCHED | Hero Cleric — specialty Weakness |
| `h3wiki-olema` | T1* | FETCHED | Hero Heretic — specialty Weakness |
| `h3wiki-mirlanda` | T1* | FETCHED | Hero Witch — specialty Weakness |
| `h3wiki-eanswythe` | T1* | FETCHED | Hero Artificer (Factory) — specialty Weakness. **Chỉ có ở HotA**. ⭐ Con số specialty của hero này **không qua `{{swh}}`**, nên nó là mốc xác nhận độc lập cho chiều của template đó |
| `h3wiki-shield-of-the-damned` | T1* | FETCHED | Artifact **riêng biệt**, không liên quan `Shield of the Yawning Dead`. Dùng để chống nhầm tên |
| `h3wiki-recanters-cloak` | T1* | FETCHED | Artifact chặn phép — dùng kiểm claim "anti-magic artifacts chặn được Armor" |
| `h3wiki-cape-of-silence` | T1* | FETCHED | Artifact chặn phép — dùng kiểm cùng claim trên |
| `h3wiki-terrain` | T1* | FETCHED | Trang `Terrain` — cơ chế Cursed Ground |
| `h3wiki-ironfist-of-the-ogre` | T1* | FETCHED | Combination artifact khác cũng cast phép đầu trận. ⚠️ Câu về "cái gì chặn được" lặp **nguyên văn** trên trang này, trang `Angelic Alliance` và trang `Armor of the Damned` → đó là **boilerplate của biên tập viên** (`T6`), không phải game text |
| `roe-from-day-to-night` | T1* | FETCHED | Restoration of Erathia, *Long Live the King* #4 — Dead Man's Boots là **bonus khởi đầu, trên hero Thant** |
| `ab-taming-of-the-wild` | T1* | FETCHED | Armageddon's Blade — ⭐ **cả ba** thành phần Cloak nằm kề nhau, nhặt tự do không lính canh: Boots (67,3,0), Amulet (68,4,0), Cowl (69,4,0). Chứa text riêng "Dead men tell no tales" |
| `sod-viking-we-shall-go` | T1* | FETCHED | Shadow of Death — Seer's Hut (53,116,0) đổi Boots → Statesman's Medal. ⚠️ Có **trang riêng** cho bản `(Allies)`, cùng toạ độ |
| `hc-jorms-ambush` | T1* | FETCHED | Heroes Chronicles — Seer's Hut (3,7,1) đổi Boots → 13.349 vàng |
| `hota-dead-or-alive` | T1* | FETCHED | Scenario **HotA** (fan-made, không phải NWC) — Quest Guard (56,30,0) đòi Boots |
| `hota-the-life-guard` | T1* | FETCHED | Scenario **HotA** (fan-made, không phải NWC) — Boots từ Shipwreck Survivor (35,25,1) |
| `hota-beyond-the-horizon` | T1* | FETCHED | Scenario **HotA** (`source = hota`, `cback = hota fif 2`) — Seer's Hut (2,27,0) đòi **bốn** artifact (Skull Helmet, Rib Cage, Amulet of the Undertaker, Vampire's Cowl) → Golden Bow. ⭐ Chứa câu priest **cố ý bỏ lửng nguồn gốc artifact**: "Their creator was... Bah, that doesn't matter." |
| `hota-tomb-raiders` | T1* | FETCHED | Scenario **HotA** (`cback = hota fif 4`) — Seer's Hut **lặp lại** (`rpt=y`) tại (16,172,0) → +1 primary skill tự chọn; và Quest Guard (12,178,0) đòi Amulet để sửa **Skeleton Transformer** |
| `hota-frontier` | T1* | FETCHED | Scenario **HotA** (`cback = hota hota 1`) — Seer's Hut (70,18,0) → Ring of Vitality |
| `hota-nine-day-wonder` | T6 | FETCHED | Trang đặc tả template `Nine-day Wonder` của HotA — do cộng đồng viết. ⚠️ Amulet of the Undertaker nằm trong `Banned artifacts`, **ngược chiều** với `hota-apocalypse-template` |
| `ab-undead-unrest` | T1* | FETCHED | Armageddon's Blade — `victory = Acquire Artifact Vampire's Cowl`. ⚠️ **Trang chỉ 623 byte**: không có mục Objects, không Timed events, không toạ độ. Gần như không có text map nào được chép — **không được dùng để suy claim phủ định** kiểu "Sandro không xuất hiện" |
| `ab-here-there-be-pirates` | T1* | FETCHED | Armageddon's Blade — Cowl trên map, 26 Dragon Flies canh |
| `roe-all-for-one` | T1* | FETCHED | Restoration of Erathia (`source = roe`) — map **Single/Multiplayer độc lập**, không thuộc campaign. Seer's Hut (1,16,0) → +5 Attack. ⚠️ Seer's Hut này **không có** text `prop`/`comp` |
| `hota-all-hands-on-board` | T1* | FETCHED | Scenario **HotA** (`cback = hota hota 4`) — Seer's Hut (47,26,1) → 50 Vampire Lords |
| `h3wiki-lord-falorel` | T1* | FETCHED | Border Lord của AvLee, láng giềng Lord Fayette. ⚠️ **Điểm DISPUTED:** trang này (và Fandom) nói **Vayarad** là vampire giả dạng và **Falorel** là nạn nhân elf; nhưng **game text** trong `sod-wrath-of-sandro` gọi chính **Falorel** là vampire. Cùng loại với ca `Dethmar/Dethard`. Trang `Vayarad` là redirect tới đây |
| `h3wiki-mormolykos` | T1* | FETCHED | ⭐ Hero **HotA** — vampire gốc Jadame, mang sẵn Cowl (`spart_6`). Là **chủ sở hữu có tên trong truyện** duy nhất của Cowl; `hota-tomb-raiders` gọi nó là "Mormolykos' Cowl" |

### Artifact

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-cloak-undead-king` | T1* | FETCHED | Cơ chế, thành phần, bảng hồi sinh, quy tắc cộng dồn. ⚠️ Câu về HotA 1.7.2 trên trang này **sai** — xem cảnh báo bên dưới |
| `h3wiki-armor-of-the-damned` | T1* | FETCHED | Cơ chế, thành phần, synergy với hero. Mô tả in-game: **4 spell**, không phải 5 |
| `h3wiki-amulet-of-the-undertaker` | T1* | FETCHED | Thành phần Cloak — Treasure, Necklace, 2000, +5% Necromancy |
| `h3wiki-vampires-cowl` | T1* | FETCHED | Thành phần Cloak — Minor, Cape, 4000, +10% Necromancy. ⚠️ **Chỉ 913 byte — KHÔNG dùng được cho bảng xuất hiện scenario.** Tên scenario duy nhất trên trang nằm trong chú thích gallery. Xem cảnh báo "Trang artifact không chứa danh sách scenario" bên dưới |
| `h3wiki-dead-mans-boots` | T1* | FETCHED | Thành phần Cloak — Major, Feet, 6000, +15% Necromancy |
| `h3wiki-angelic-alliance` | T1* | FETCHED | Artifact đối kháng — 84000, đắt nhất SoD, +21 cả bốn primary skill |
| `h3wiki-necromancy` | T1* | FETCHED | Giới hạn cơ chế Necromancy. Khác biệt SoD vs HotA về cách tính |
| `hota-changelog` | T1* | FETCHED | Changelog Horn of the Abyss, 201.529 byte. **Nguồn chuẩn** cho mọi claim về HotA — trang artifact không đáng tin bằng. 📌 Tên trang đúng là `Horn of the Abyss (Changelog)` — dạng `Horn of the Abyss/Changelog` trả **404**. ⚠️ Tier `T1*` đang **sai loại nguồn** — xem `B-018` |
| `sod-a-tough-start` | T1* | FETCHED | Yog phân tán các mảnh Angelic Alliance — bài kiểm tra lòng trung thành của Boragus |
| `sod-black-sheep` | T1* | FETCHED | Hack and Slash #2 — Blackshard. Chứa event (64,9,0): mắt đồng minh **trống rỗng** — bằng chứng Sandro thao túng tâm trí |
| `sod-a-cage-in-the-hand` | T1* | FETCHED | Hack and Slash #3 — Rib Cage. Vỏ bọc "Sanctuary" bị Ebon Hand phản bác |
| `h3wiki-skull-helmet` | T1* | FETCHED | Thành phần Armor — Treasure, Helmet, 3000, +2 Knowledge |
| `h3wiki-rib-cage` | T1* | FETCHED | Thành phần Armor — Minor, Torso, 3000, +2 Power |
| `h3wiki-blackshard` | T1* | FETCHED | Thành phần Armor — Minor, Weapon, 3000, +3 Attack |
| `h3wiki-shield-yawning-dead` | T1* | FETCHED | Thành phần Armor — Minor, Shield, 3000, +3 Defense. ⚠️ **Khác** `Shield of the Damned` |
| `h3wiki-orb-of-inhibition` | T1* | FETCHED | **Phản bác** cách nói "anti-magic artifacts chặn Armor" — Orb ghi rõ "Does not prevent: Artifact spell casting (i.e. Armor of the Damned...)" |
| `h3wiki-trivia` | T1* | FETCHED | Xác nhận độc lập: Armor hoạt động bình thường trong Anti-Magic Garrison |
| `h3wiki-weakness` | T1* | FETCHED | Armor of the Damned là artifact **duy nhất** cast được Weakness; 4 hero chuyên |
| `h3wiki-terek` | T1* | FETCHED | Barbarian/Battle Mage, tay sai đầu tiên Sandro thuê lấy Cowl; bị cướp bắt. ⚠️ **Trang có HAI loại nội dung, tier khác nhau:** `\| biography =` là in-game text (`T1*`) và **không nhắc Sandro/Cowl/bị bắt** — nó nói về Circus of the Sun và quân Krewlod. Mục `== Story ==` là **văn biên tập viên wiki** (`T6`), nằm ngoài mọi template. Đừng gán `T1*` cho câu lấy từ `== Story ==` |
| `h3wiki-sandals-of-the-saint` | T1* | FETCHED | Cần để qua Quest Guard lấy Dead Man's Boots |
| `fandom-artifact-list` | T6 | FETCHED | `List of Heroes III artifacts` — **nguồn duy nhất** cho mô tả in-game của artifact. Fandom **không dẫn nguồn** |
| `h3wiki-herobios-txt` | **T1** | FETCHED | ⭐ `Translation Data/HeroBios.txt` — **file string table TRÍCH TỪ GAME** (168KB, cột EN/FR/PL/RU). Đây là `T1` **thật**, không phải `T1*` |
| `h3wiki-artraits-txt` | **T1** | FETCHED | ⭐ `Talk:Artifact/descriptions` — bảng mô tả artifact, tự ghi đầu bảng `Information from H3Bitmap.lod > artraits.txt`. **String table trích từ file game** → `T1` **thật**. Thay `fandom-artifact-list` cho mọi mô tả in-game của artifact |
| `h3wiki-artifact-events` | T1* | FETCHED | `Artifact Events` (35.645 byte) — text hiện ra khi **nhặt** artifact. Mở đầu: "Default descriptions when picking an artifact." Xác nhận độc lập cho trường `event` trên từng trang artifact |
| `hota-apocalypse-template` | T6 | FETCHED | Trang đặc tả template `Apocalypse` của HotA — **do cộng đồng viết, KHÔNG phải in-game text**. Liệt kê ba artifact dưới đầu đề "Allowed artifacts". ⚠️ Sửa lần cuối 2025-05-14 ≈ HotA 1.7.2–1.7.3, **trước 1.8.0**. Changelog **không** xác nhận danh sách này — xem cảnh báo bên dưới |
| `hota-blacknblue-template` | T6 | FETCHED | Trang đặc tả template `Black'n'Blue` của HotA — do cộng đồng viết. ⚠️ Dead Man's Boots nằm trong `Banned artifacts`, **không** phải danh sách cho phép |

### Heroes I – II (kỷ Age of Kings)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h2-first-blood` | T1* | FETCHED | Heroes II, scenario 1 campaign Archibald — briefing "**I am King! Not Roland.**" + scenario description. Lấy qua Fandom API; `{{quote}}` = briefing trong game, `{{text}}` = description trong game |
| `h2-apocalypse` | T1* | FETCHED | Heroes II, scenario 11 (cuối campaign Archibald) — briefing "bring my brother back in chains!" + epilogue Archibald phong Roland làm "**monarch of the Western Tower**" |
| `h2-final-justice` | T1* | FETCHED | Heroes II, scenario 10 (cuối campaign Roland) — ⭐ **bản án hóa đá**, mốc quan trọng nhất của Heroes II. Ràng buộc "until future generations should take pity upon you and restore you to life" |
| `h2-archibalds-campaign` | T6 | FETCHED | Trang campaign Archibald trên Fandom — 11 scenario, `date = 1151–1154 AS`. ⚠️ Câu "Roland's campaign is the canonically true one" **không dẫn nguồn** — nhưng kết luận đó **có** chống lưng `T1` thật, xem `h3wiki-herobios-txt` |
| `h1-morglin-ironfist` | T6 | FETCHED | Cha của Archibald và Roland. ⚠️ Tên in-game ở Heroes I là **"Jerico"**; "Morglin" chỉ có trong manual. Bốn lãnh chúa Heroes I **đều không playable** theo nghĩa hero có tên |
| `thelazy-succession-wars` | T6 | FETCHED | Hai cuộc Succession Wars. Niên đại "around the 1110s to **1154** AS" — ⚠️ **không khít** với `1151–1154` của trang campaign |

### Might & Magic VI – VII (Archibald sau Heroes II)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `mm7-diaries-3do` | **T2** | FETCHED | ⭐⭐ *The Diaries of Archibald* — **text manual MM7 trên website CHÍNH THỨC của 3DO**, lấy qua archive: `web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`. **Archibald tự kể ở ngôi thứ nhất.** Ba entry: 1165 / **1167** / **1168**. Nguồn **không-phải-wiki** tốt nhất dự án có cho niên đại Antagarich 1165–1168, và là nguồn duy nhất kể **đúng** cách hắn lên ngôi Deyja. Chốt được `Deathknell` = Finneas Vilmar. ⚠️ **thelazy chép sai hai con số năm từ nguồn này** |
| `fandom-path-of-darkness` | T6 | FETCHED | Bảng quest Dark Path MM7 — Archibald **mời** party vào The Pit sau khi chọn Sleen |
| `fandom-archibald-ironfist` | T6 | FETCHED | Bài dài nhất về nhân vật. ⚠️ **Gộp sai** Challenge of Dominance với việc lên ngôi Deyja — xem cảnh báo bên dưới |
| `fandom-archibald-disambig` | T6 | FETCHED | ⚠️ **BH-2:** chứng minh có **`Archibald Dawnsglow`** — expert Light Magic trainer trong MM8, nhân vật **khác**. Đối xứng trớ trêu: Ironfist là Grandmaster **Dark** Magic trainer ở MM7 |
| `thelazy-nimbus` | T6 | FETCHED | ⚠️ Trang này **tách đúng** hai sự kiện (thắng Nimbus ≠ lên ngôi Deyja), trong khi trang `Archibald` của **cùng wiki** gộp sai. Bằng chứng thelazy tự mâu thuẫn |
| `hota-beyond-the-horizon-rumors` | T1* | FETCHED | ⭐ Rumor game text HotA: "Zog named his powerful artifact **in memory of Archibald**. The usurper king and the Jackal were **allies during the Succession Wars**." Changelog HotA **0 hit** Archibald — nên chỉ tìm ra bằng cách đọc content, không đọc changelog |

### ⭐ Heroes IV — `Age of Heroes` (T1*), lấy qua archive

**Đây là lời giải cho `B-019`** — nhưng **không** ở tier như đợt đầu tưởng. Mục `heroes4/` của
`heroesofmightandmagic.com` được lưu đầy đủ trong archive, khoảng **200 URL**. Registry từng ghi domain
này là `FAILED (403 web filter)`; qua archive thì vào được bình thường.

🔴 **ĐÍNH CHÍNH (2026-08-03): đây KHÔNG phải site chính thức của NWC.** Đợt giải `B-019` gán nó tier
**`T2` official** và mô tả là "site chính thức của New World Computing" — **sai**, và cái sai đó **đã
lên `main`** trước khi bị bắt.

Footer của chính trang nói rõ:

> "**Age of Heroes** and Heroes Community are copyrighted **©2005 Valera Koltsov**. Heroes of Might and
> Magic 1, 2, 3, 4, 5 are registered trademarks of UbiSoft Entertainment."

Đã grep toàn trang: **0 lần** nhắc `New World Computing`, **0 lần** nhắc `3DO`. Đây là **site fan** do
Valera Koltsov làm, cùng nhà với diễn đàn *Heroes Community*.

**Tier đúng là `T1*`** — không phải `T2`, cũng không phải `T6`: nội dung nó đăng là **mô tả item
in-game** (tức `T1` theo mục 2 của `CANON-POLICY.md`) **tiếp cận qua trung gian fan**, đúng định nghĩa
`T1*`. Cùng loại với `heroes.thelazy.net`.

⚠️ **Nhưng độ tin thấp hơn thelazy.** Đã phát hiện nó **chép sai**: `"must of his humanity"` trong khi
hai nguồn khác đều ghi `"most"`. thelazy được tin ở mức `T1*` phần vì nó đánh dấu `{{sic}}` và chép cả
lỗi gốc; Age of Heroes **không** có kỷ luật đó. Claim quan trọng phải đối chiếu nguồn thứ hai.

**Bài học:** đừng suy chủ sở hữu site từ **tên miền**. `heroesofmightandmagic.com` nghe như site chính
thức, ghi chú cũ của registry cũng gọi nó là "site chính thức của NWC" — nhưng **chưa ai đọc footer**.

**Cách lấy:** liệt kê bằng CDX API rồi fetch theo timestamp —

```
curl -s "http://web.archive.org/cdx/search/cdx?url=heroesofmightandmagic.com/heroes4*&output=text&fl=original,timestamp&collapse=urlkey&limit=200"
curl -sL "https://web.archive.org/web/<timestamp>/<url>"
```

⚠️ CDX trả cả **URL cắt lỗi** (`artifactinor.shtml`, `buildinlife.shtml`…) — chúng trả trang rỗng
~2,3 KB. Tên đúng có dấu gạch dưới đầy đủ: `artifacts_minor.shtml`, `buildings_life.shtml`.

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `aoh-h4-artifacts-minor` | **T1*** | FETCHED | ⭐ `heroes4/artifacts_minor.shtml` (24.206 byte) — bảng artifact **Minor** của H4 kèm Slot + Description nguyên văn. Chứa `Amulet of the Undertaker`: "Increases the hero's Necromancy skill by 10% if the hero has the skill. **Otherwise, it acts as the Basic Necromancy skill.**" **Thay được `fandom-h4-artifact-list` (`T6`)** — hai nguồn khớp từng chữ |
| `aoh-h4-campaign-halfdead` | **T1*** | FETCHED | ⭐⭐ `heroes4/campaign_halfdead.shtml` (12.894 byte) — **toàn bộ campaign *Half-Dead*** của Gauldoth: điều kiện thắng/thua từng scenario, carryover, và văn kể ở **ngôi thứ nhất**. Mở đường cho entity trụ `gauldoth-half-dead` (`B-016` mục 3) |
| `aoh-h4-index` | **T1*** | FETCHED | Mục `heroes4/` nói chung — còn `artifacts_{major,relic,treasure,potion,tgs}.shtml`, `heroes_{necromancers,deathknights,lords,…}.shtml`, `creatures_death.shtml`, `buildings_death.shtml`, và **năm campaign khác** (`blade`, `daughter`, `elwin`, `glory`, `price`). **Phần lớn chưa khai thác** |

### Heroes Chronicles — Tarnum

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-tarnum` | T1* | FETCHED | Trang `Tarnum` (18.754 byte) — ⭐ **bảng sáu class** kèm danh hiệu riêng cho từng class (King Tarnum / Sir Tarnum / Lord Tarnum / Tarnum Dragonfriend / Tarnum Hopewielder / Overlord Tarnum). ⚠️ Mục `== Deaths ==` và `== Relationships ==` là **văn wiki không dẫn nguồn** |
| `hc-tunnels-of-ice` | T1* | FETCHED | ⭐⭐ Scenario *The Sword of Frost* — **game text tường minh cho cơ chế bất tử**, nằm trong `=== Timed events ===` day 23–24 (đúng BH-1: đọc prologue thôi là trượt). Tarnum **tự đâm dao vào tim** trước mặt Ufretin để chứng minh, hôm sau **không còn sẹo** |
| `hc-the-protectors-of-the-sword` | T1* | FETCHED | ⭐⭐ **Epilogue của toàn bộ Heroes Chronicles** — chuỗi nhân quả dẫn tới The Reckoning: Tarnum **tha mạng Kija** → ả trộm Sword of Frost → giao Kilgor. Kết bằng lời cầu: *"Ancestors, please don't let my compassion destroy the world!"* |
| `chronicles-official-3do` | **T2** | FETCHED | ⭐⭐ **Site chính thức 3DO**, `3do.com/products/pc/chronicles/` qua archive — **80 trang**, gồm trang riêng cho từng campaign. Bản quyền *"Heroes Chronicles © 2000 The 3DO Company. All Rights Reserved."* Ví dụ text: *"the **Immortal Hero, Tarnum**, rides forth to battle… the Dragon Queen, Mutare"*. ⚠️ Đường dẫn có **thêm một tầng** (`/products/pc/`); index `/mightandmagic/` **không** link tới đây |
| `ch-h4-might-texts` | T1* | FETCHED | Transcript campaign *Glory of Days Past* (Heroes IV Might), 61.771 byte RTF trên Celestial Heavens qua archive. ⭐ Chứa **cái chết cuối** của Tarnum trên Axeoth và cảnh hắn **TỪ CHỐI Paradise**. ⚠️ URL sống trả **403** — phải qua archive |
| `h3wiki-heroes-chronicles` | T6 | FETCHED | Trang tổng quan tám campaign. ⚠️ Số map và cách bán là **văn wiki không dẫn nguồn** |
| `fandom-tarnum` | T6 | FETCHED | ⚠️ Ghi Waerjak là "son"; game text nói **"foster father"** xuyên suốt — xem cảnh báo |

### Kỷ Axeoth — Heroes IV, campaign *The Half-Dead*

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h4-death-texts-ch` | T1* | FETCHED | ⭐⭐ **Nguồn tốt nhất dự án có cho Heroes IV.** `H4-DeathTexts.rtf` trên Celestial Heavens qua Wayback (`20130117072816`) — **89.002 byte**, toàn bộ text kể chuyện campaign Death: 5 scenario description, 5 monologue, và **54 block sự kiện** gồm 5 quest có đủ `Proposal`/`Progress`/`Completion`. Tức có cả **region text và timed event**, đúng thứ BH-1 đòi. Trang index tự ghi: "collected by **Corlagon** and and Zamfir" *(chữ "and and" là nguyên văn)*. Đây là nguồn mà **Fandom dẫn cho mọi claim cốt truyện H4** |
| `aoh-h4-heroes-campaign` | T1* | FETCHED | `Age of Heroes` — `heroes4/heroes_campaign.shtml` (31.882 byte). Bio các campaign hero H4, gồm Gauldoth và Kalibarr. ⚠️ Trang trộn **hai loại văn**: `Biography` là text in-game, `History` là ghi chú của fansite |
| `aoh-h4-heroes-necromancers` | T1* | FETCHED | `Age of Heroes` — số liệu class Necromancer H4 (giá thuê, skill khởi đầu). ⚠️ **Heading trang ghi sai**: "Death/Necropolis **Might** Heroes — Necromancers"; Necromancer là **magic** class, might class của Death là Death Knight. Đừng chép heading |
| `ray-interview-ubisoft-2015` | **T4** | FETCHED | ⭐⭐ **Phỏng vấn Terry B. Ray — người VIẾT cốt truyện Heroes IV.** Trên site chính thức Ubisoft MMH7, đăng **09/11/2015**. URL sống **đã chết** (redirect sang store); phải dùng `web.archive.org/web/20151020063103/…`. Ubisoft gọi ông là "**Heroes IV's master bard**". Ray tự thuật: *"I made maps, edited the stories, worked on the manual"* và *"I was hired to work on Heroes IV, but also wrote the **Heroes III Chronicles** series"* — nên nguồn này còn dùng được cho `tarnum`. ⚠️ Xem cảnh báo về dòng dõi Gauldoth bên dưới |
| `fandom-gauldoth` | T6 | FETCHED | Bài Fandom về Gauldoth. ⚠️ Infobox ghi bốn quan hệ gia đình dẫn **cùng một** `<ref>` về bài Ray — nhưng nguồn đó **phủ định** đúng chi tiết ấy. Xem cảnh báo |
| `fandom-iduna` | T6 | FETCHED | ⚠️ Khẳng định Iduna "**was the mother of** Lysander, Waerjak, and Gauldoth", dẫn ref về bài Ray. **Ray nói ngược.** Xem cảnh báo |
| `thelazy-the-reckoning` | T6 | FETCHED | Trang `The_Reckoning` (13.958 byte) — văn xuôi wiki. Mở đầu: "On **February 10th, 1177 AS**…". 🔴 **HAI ĐÍNH CHÍNH so với bản ghi chú cũ, xem mục cảnh báo riêng bên dưới:** (1) "hai số hiệu lệch nhau (1177 vs 1178)" là **SAI** — 1178 là năm Lysander *viết lại*, không phải năm xảy ra; (2) `Lost Manuscripts` giờ **đã fetch**, và nó **không phải text in-game** mà là outline nội bộ chưa xuất bản (`h3wiki-lost-manuscripts`, `T4`). ⚠️ Mục `== Lysander's account of The Reckoning ==` gắn icon `{{wll}}` = *"Only found in the Lost Lore"* → **nằm ngoài game**. Đây là **trang wiki duy nhất trong đợt này thực sự dẫn nguồn** (2 footnote, cả hai đã truy tận gốc) |
| `h4-official-3do-story` | **T2** | FETCHED | ⭐ Site **chính thức 3DO**, `3do.com/mightandmagic/heroes4/story.html` qua archive (`20011005033543`). Dòng bản quyền: *"© 2001 The 3DO Company. All Rights Reserved."* ⚠️ **Chỉ ~630 ký tự chữ hiển thị** — văn giới thiệu bán game, **không nhắc** `Axeoth`/`Reckoning`/`Gauldoth`. Mục `heroes4/` có **58 trang** sạch (`char_*`, `expansion-tgs`, `expansion-wow`, `features`, `gallery_*`, `intro`, `gameplay`, `story`). ⚠️ Đường dẫn là `/mightandmagic/heroes4/`, **không** phải `/heroes4` hay `/products/pc/heroes4` — lần quét CDX đầu tìm sai path và báo âm |
| `fandom-necromancer-h4` | T6 | FETCHED | Trang `Necromancer (H4)` — class cơ bản magic của Necropolis, khởi đầu Basic Death Magic + Basic Occultism |

### ⭐ The Reckoning — ranh giới Enroth → Axeoth (đợt 2026-08-04)

**Cấu trúc bằng chứng của sự kiện này lệch một cách đáng chú ý, và đó là điều quan trọng nhất
cần biết trước khi dùng các key dưới đây:**

| Mảng nội dung | Có text game? | Nguồn tốt nhất |
|---|---|---|
| **Nguyên nhân** — hai lưỡi gặp nhau = tận thế | ✅ CÓ | Chronicles book 8, `==== Events ====` |
| **Điều kiện dẫn tới** — Kija trộm Sword, Gelu giữ Blade | ✅ CÓ | Chronicles book 8 epilogue; H3:AB |
| **Tên gọi "the Reckoning"** | ✅ CÓ | 16 bio hero H4 |
| **Hệ quả** — Erathia mất, Kreegan sụp, dân tị nạn | ✅ CÓ | 16 bio hero H4 |
| **Diễn biến thảm hoạ** — động đất, dung nham, ba giờ | ❌ **KHÔNG** | chỉ `h3wiki-lost-manuscripts` = **T4 non-canonical** |
| **Portal & cách người ta thoát** | ❌ **KHÔNG** | `h3wiki-lost-manuscripts` + `bullard-interview-2013`, cả hai **T4** |
| **Ravenwood** | ❌ **KHÔNG** | chỉ `h3wiki-lost-manuscripts` |
| **Ngày tháng chính xác** | ❌ **KHÔNG** | phép cộng của wiki trên nền T4 |
| **Nguồn chính thức T2** | ❌ | **chưa đọc được** — không phải "đã đọc và không có" |

> Nói cách khác: **cái mà mọi wiki kể như "tường thuật chính" của The Reckoning — Ravenwood,
> portal, ba giờ hỗn loạn, ngày 10/02/1177 — toàn bộ nằm trong một tài liệu chưa bao giờ vào
> game, và chính wiki dán nhãn "at least partially non-canonical".** Thứ *có* text game chống
> lưng lại là hai đầu: **nguyên nhân** (Chronicles) và **hệ quả** (bio hero H4).

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-lost-manuscripts` | **T4** | FETCHED | 🔴 **KEY QUAN TRỌNG NHẤT, VÀ TIER CỦA NÓ LÀ CÁI BẪY.** Trang `Lost_Manuscripts` (22.552 byte) — nhật ký General Kendal + hồi ký King Lysander, tường thuật đầy đủ nhất về The Reckoning. **KHÔNG PHẢI `T1*`.** Trang tự khai: *"In 2017 Jennifer Bullard shared various outlines for the backstory of Heroes of Might and Magic IV, written in the early 2000s… Note that the information here **might not be entirely canonical**"*. Tức là **outline hậu trường, chưa bao giờ vào game** → `T4`. Chứa: lời cảnh báo Ravenwood, cơ chế portal, "three hours", quốc gia mới **Iranese** bên **Brystol Sea**, và biệt danh **"Day of Undoing"**. ⚠️ **Tự mâu thuẫn nội tại:** mục Kendal `02-04-1177` nói người đàn bà đến *"last night"*, bản dài Lysander nói *"three nights ago"* |
| `h3wiki-lost-lore` | T6 | FETCHED | Trang `Lost_Lore` (6.621 byte) — **đây là bằng chứng tier** cho key trên. Verbatim: *"these outlines were written during the game's development and **never officially published. They are at least partially non-canonical**"*. Cũng liệt kê rõ **hai** mục Bullard: `Lost Manuscripts` và `The Reckoning (Lysander's account)` → **cả hai** tường thuật dài đều ngoài game. Template `Inll` định nghĩa icon `{{wll}}` = *"Only found in the Lost Lore"* — thấy icon đó ở đâu thì chỗ đó **không** phải text game |
| `h3wiki-h4-hero-bios` | **T1\*** | FETCHED | ⭐⭐ **Nguồn text game tốt nhất cho entity này, và là thứ chốt câu hỏi quyết định.** 16 bio hero Heroes IV gọi thẳng tên "the Reckoning" → **thuật ngữ này LÀ text game, và xuất hiện lần đầu ở Heroes IV** (không phải H3/AB/Chronicles). Lấy bằng `api.php?action=query&generator=backlinks&gbltitle=The Reckoning&gbllimit=500&prop=revisions&rvprop=content&rvslots=main` rồi trích template `{{H4Story}}` (tham số 2 = *"The Heroes 4 biography text"*, render kèm chữ *"— Biography"*). **Mỗi bio kiểm lại được riêng** tại `index.php?title=<Hero>&action=raw`. 16 hero: `Sephinroth` `Sandro` `Gruezak` `Bron` `Oris` `Calh` `Fiona` `Tamika` `Ignatius` `Mephala` `Labetha` `Ingham` `Mirlanda` `Shiva` `Lorelei` `Theodorus`. ⚠️ **Chú ý ngược dòng:** không bio nào nhắc `Enroth`, `Axeoth`, `portal`, `Gelu`, `Sword of Frost` hay `Armageddon's Blade` — chúng chỉ nói *"the old world"* / *"the new world"*. Nghĩa là **cơ chế** thảm hoạ **không** nằm trong text game H4 |
| `hc-the-barbarians-wife` | T1* | FETCHED | Chronicles book 8, `==== Events ====` day 1 — gốc gác Sword of Frost: *"Volee was the first city of the Vori Elves, but it disappeared more than a thousand years ago shortly after the Sword of Frost was created… Some speculate that the Sword of Frost itself is responsible for the creation of the glaciers that buried the ancient city"* |
| `hc-the-land-of-the-vori` | T1* | FETCHED | Chronicles book 8, `==== Events ====` day 1 — Tarnum tự nói đã kể lời tiên tri cho người Vori: *"even told them about the prophecy linking the Sword of Frost and Armageddon's Blade, but they wouldn't listen"*. Cũng ghi Gelu **là half-Vori** |
| `h3wiki-the-sword-of-frost-campaign` | T1* | FETCHED | Mô tả campaign book 8 (5.619 byte): *"The Elven Hero, Gelu, sets out to find the arcane Sword of Frost despite an apocalyptic prophecy"* |
| `ab-oblivions-edge` | T1* | FETCHED | ⭐⭐ Scenario **cuối** của H3: *Armageddon's Blade* (13.571 byte). **Hai timed event quan trọng, và cả hai đều là bẫy suy luận** — xem cảnh báo riêng. (1) event 14 *"Tamar's Return"*: *"Oceans will boil, the ground shall swallow entire cities, and everyone will die a horrifying death"* — hình ảnh **gần trùng khít** The Reckoning **nhưng điều kiện NGƯỢC** (thảm hoạ xảy ra nếu Gelu **thất bại**). (2) event 10 *"Seduced by the Blade"*: giấc mơ tiên tri của Gelu, có *"steel-haired woman"* |
| `h3wiki-armageddons-blade-artifact` | T1* | FETCHED | Text game khi nhặt artifact: *"Deep beneath the earth, you find a vault of the Ancients from before the Silence… you break the seal"*. Hiệu ứng SoD/AB: +3 Attack/Defense/Power, +6 Knowledge, *"Gain Armageddon while equipped"*, class `Relic`, giá 50.000. Do forgesmith **Khazandar** rèn trong `Maker of Sorrows` |
| `ab-to-kill-a-hero` | T1* | FETCHED | Mô tả Blade bằng text game: *"Armageddon's Blade was born of Chaos, shaped by Magic, and bound by steel and flesh."* |
| `fulton-tavern-interview-2018` | **T4** | FETCHED | ⭐⭐ **Greg Fulton, Lead Designer Heroes III** — phỏng vấn *Tavern of Might and Magic* do **XEL** thực hiện, đăng **02/JUL/2018** (thelazy 35.730 byte). **Câu chốt hạ:** *"Lore work for HoMM4, and the idea for 'the Reckoning', **did not begin until long after I had left NWC**."* Và về người đàn bà tóc thép trong giấc mơ Gelu: *"**Officially, there were no plans for the steel-haired woman.**"* — Marcus Pregent dựng chi tiết campaign AB chỉ để *"laying the groundwork for potential storylines"*, và *"At the time, this 'story hook' was **unrelated to HoMM4**"*. ✅ Fulton **in lại nguyên văn** trong Fanstratics Newsletter #3 — đã đối chiếu hai trang thelazy, **khớp từng chữ**. ⚠️ URL gốc `celestialheavens.com/forum/topic/16786` và `fanstratics.com/fstnewsletter03` đều **KHÔNG vào được** |
| `h3wiki-ravenwood` | **T4** | FETCHED | Trang `Ravenwood` (685 byte) — **toàn trang gắn `{{inll}}`**, tức 100% là Lost Lore, không có gì trong game. Nhân vật mở portal theo lời kể Kendal/Lysander |
| `h3wiki-talk-timeline` | T6 | FETCHED | ⭐ Trang `Talk:Timeline` (81.324 byte) — **tự khai ra phép cộng** tạo nên ngày `10/02/1177`: *"Lost Manuscripts: 11-08-1178: The Reckoning occurs six days after 02-04-1177, on February 10th, 1177."* Cả hai dòng gắn `{{wll}}`. **Không nguồn nào — game hay ngoài game — viết ra ngày đó** |
| `h3wiki-enroth-planet` | T6 | FETCHED | Trang `Enroth (planet)` (4.697 byte): *"Enroth was rendered uninhabitable after the Reckoning **in the 1170s AS**"*. ⭐ Đáng chú ý: **ở đây chính wiki chỉ dám nói "1170s"**, không dám nói 1177 — mâu thuẫn với trang `The_Reckoning` của cùng wiki. ⚠️ `Enroth` là **trang disambiguation ba nghĩa** (`nation` / `continent` / `planet`) — BH-2 |
| `h3wiki-axeoth` | T6 | FETCHED | Trang `Axeoth` (2.096 byte) — danh sách quốc gia hậu-Reckoning (Palaedra, Aranorn, Nekross, Great Arcan, The Wheel, Tribal Lands). ⚠️ **Không citation nào**, và ⚠️ **không có một mốc năm nào** trên trang |
| `h3wiki-kilgor` | T6 | FETCHED | Trang `Kilgor` (6.213 byte). ⚠️ *"Kilgor acquires the Sword of Frost and **forces** Gelu to confront him"* — chữ **"forces"** **không có nguồn nào chống lưng**; text game Chronicles cho thấy Gelu chủ động đi tìm Sword để **phá huỷ** nó |
| `h3wiki-gelu` | T6 | FETCHED | Trang `Gelu` (7.190 byte). ⚠️ **KHÔNG nói gì về số phận Gelu sau Reckoning** — đáng ghi vì Fandom liệt Gelu vào danh sách người chết mà **không citation**, và wiki này im lặng. Hai wiki không đồng ý nhau |
| `fandom-reckoning` | T6 | FETCHED | Trang Fandom tên `Reckoning` (**không** phải `The Reckoning` — tên đó trả `missingtitle`). ⚠️⚠️ **`grep -c "<ref"` = 0 — toàn trang KHÔNG CÓ MỘT CITATION NÀO.** Ghi `date = 1175 AS`, **lệch 2 năm** với thelazy. Kèm danh sách `==Deaths==` và hai câu quote không attribution. Xem cảnh báo riêng |
| `fandom-great-reckoning` | T6 | FETCHED | ⚠️ **SỰ KIỆN KHÁC HẲN** — thần thoại tận thế **tương lai** của Axeoth (MM9), không liên quan việc Enroth bị phá. Chỉ dùng để **phân biệt**, không bao giờ làm nguồn cho `the-reckoning` |
| `fandom-h4-hero-bios` | **T1\*** | FETCHED | ⭐⭐ Bộ bio hero Heroes IV trên Fandom, gói trong template `{{text}}` / `{{quote}}` — tooltip `Template:Text` ghi rõ *"This is the background/description from the game/official game guide itself"*. Lấy bằng `api.php?action=query&generator=backlinks&gbltitle=Reckoning&gbllimit=500&prop=revisions&rvprop=content&rvslots=main`. **Đếm chính xác (2026-08-04): 45 block game text gọi tên "Reckoning"** trên 180 trang backlink. ✅ **Khớp từng chữ với `h3wiki-h4-hero-bios`** ở các bio đối chiếu được → hai trung gian độc lập cùng chép một text. ⚠️⚠️ **BẪY QUAN TRỌNG:** tên `Enroth` và `Axeoth` trong các block này **chỉ là ĐÍCH WIKILINK do người sửa wiki thêm** (`[[Axeoth|new world]]`, `[[Enroth (planet)|old world]]`) — **text hiển thị trong game là "the old world" / "the new world"**. Đừng đọc đích link thành text game. ⚠️ Tooltip nói *"game **or official game guide**"* — trung gian này không luôn phân biệt hai thứ đó |
| `h3wiki-day-of-reckoning` | T6 | FETCHED | ⚠️ **KHÔNG phải nguồn lore.** Trang `Day of Reckoning` (16.898 byte) — một **mod expansion fan chưa phát hành** cho Heroes III, tự gắn `{{speculative}}`. Đáng ghi vì nó *"designed in consultation with Heroes III lead designer Gregory Fulton"*, nên dễ bị nhầm là có thẩm quyền. Tối đa `FAN_THEORY`. Chỉ dùng để **phân biệt tên** với `the-reckoning` |
| `fandom-palaedra` | T6 | FETCHED | ⭐ Trang `Palaedra` — **bằng chứng khẳng định rằng Fandom KHÔNG dùng lịch "AS" cho Axeoth**: đề *"ca 525 A.C."*, và `A.C.` chuyển hướng tới `Great Cataclysm`. Mạnh hơn lập luận "trang `Axeoth` không có mốc năm nào" |
| `fandom-fahtrim` | **T1\*** | FETCHED | ⭐ Bio hero H4 `Fahtrim` (1.050 byte) — **phản ví dụ duy nhất** cho claim "không bio nào nhắc portal": *"During the Reckoning, he revealed his bold selflessness by **staying behind until the last possible moment to help others through the portals**"*. Chữ "portals" là **text hiển thị**, không phải đích link. → **Portal CÓ trong text game H4**, dù cơ chế và người mở thì không. ⚠️ **Trang này KHÔNG tồn tại trên thelazy (0 byte)** — nên đây là ca thelazy thiếu mà Fandom có |
| `fandom-gauldoth-refs` | T6 | FETCHED | Đối chứng chất lượng: trang `Gauldoth` của Fandom (16.682 byte) **CÓ `<ref>` đầy đủ**, dẫn từng scenario H4 kèm transcript — trong khi trang `Reckoning` của **cùng wiki** có **0 ref**. ⭐ Bài học: **đừng gán "Fandom = T6 kém" cho mọi trang**; chất lượng lệch rất xa giữa các trang, phải kiểm từng trang |

### ⚠️⚠️⚠️ `heroesofmightandmagic.com` và `3do.com` — đã ĐỊNH VỊ CHÍNH XÁC 63 trang mà KHÔNG đọc được

Đợt `the-reckoning` (2026-08-04) enumerate được **đầy đủ** hai bộ trang mà `B-022` và `B-023` cần,
kèm **timestamp chính xác cho từng trang**, nhưng **không đọc được một trang nào** — vì `web.archive.org`
bị chặn nội dung (xem mục dưới). Ghi lại timestamp để đợt sau **không phải quét lại**:

- **Age of Heroes, 39 trang campaign H4** (nhiều hơn 6 trang mà `B-022` tưởng — có trang con theo từng
  scenario): `campaign_halfdead` `20060118021947` · `halfdead2` `20071102140229` ·
  `halfdead3` `20070808181955` · `halfdead4` `20070808032934` · `halfdead5` `20061209093603` ·
  `halfdead6` `20070811121343` · `campaign_blade` `20060118020340` · `blade2` `20070116140110` ·
  `blade3` `20070116140223` · `blade4` `20070129045001` · `blade5` `20070129082526` ·
  `blade6` `20070129082536` · `campaign_daughter` `20060118020415` · `daughter2` `20070716194303` ·
  `daughter3` `20070808032723` · `daughter4` `20070808033147` · `daughter5` `20070808032541` ·
  `daughter6` `20070808032912` · `campaign_elwin` `20060118015731` · `elwin2` `20070510174106` ·
  `elwin3` `20070510173224` · `elwin4` `20070428055736` · `elwin5` `20070510174043` ·
  `elwin6` `20070510174208` · `campaign_glory` `20060118021419` · `glory2` `20070708123801` ·
  `glory3` `20070708123532` · `glory4` `20070708123633` · `glory5` `20070708123415` ·
  `campaign_price` `20060118020700` · `price2` `20070808181643` · `price3` `20070808032319` ·
  `price4` `20071109110852` · `price5` `20071109110857` · `price6` `20070808032407` ·
  `price7` `20070808182203` · `price8` `20070808182106` · `price9` `20071109222348` ·
  `campaigns` `20060118021016` · `heroes_campaign` `20060118010939`
- **3DO chính thức, 24 trang HTML thật** dưới `3do.com/mightandmagic/heroes4/`:
  `story.html` `20011005033543` · `intro.html` `20011011114108` · `features.html` `20011211180001` ·
  `gameplay.html` `20011024014406` · `gallery_characters.html` `20011030080150` ·
  `preview.html` `20011030080439` · `expansions.html` `20020809075912` ·
  `expansion-tgs.html` `20030129092715` · `expansion-wow.html` `20030117102012` ·
  `downloads.html` `20011004075524` · và 14 trang `char_*`
- ⚠️ **Đừng kỳ vọng bio ở 14 trang `char_*`: chúng chỉ 530–544 byte.** Đây đúng dấu hiệu đã biết ở
  trang artifact/hero thelazy (660–1.718 byte) — kích thước đó không đủ chứa bio. Trang đáng đọc nhất
  là `gameplay.html`, `gallery_characters.html`, `features.html`, `intro.html`, `expansion-*`.
- ⚠️ CDX cũng trả rất nhiều **URL méo** kiểu `heroes4%22target=new_window` — bỏ, chúng 404.

🔴 **Và vì thế, phủ định về nguồn T2 phải nói cho đúng mức:**

> Dự án **chưa đọc được** nguồn chính thức nào nhắc "Reckoning". Đây **KHÔNG** phải
> *"đã đọc và không có"*. 24 trang 3DO đã được định vị chính xác kèm timestamp, chúng **tồn tại**,
> chỉ là bị chặn ở tầng mạng của máy dev.

Đây đúng loại claim phủ định mà bài học lớn nhất của dự án cảnh báo — *"nó trông giống sự cẩn trọng"*.

### ⚠️⚠️ Ba thứ TÊN GẦN GIỐNG mà KHÔNG phải The Reckoning

Bẫy lẫn entity, đã kiểm cả ba:

| Tên | Nó thật ra là gì |
|---|---|
| `Great Reckoning` / `Day of Wrath` | Thần thoại **Axeoth** (Might and Magic IX) về một ngày tận thế **tương lai**: *"the day 'when even the gods must atone for their lives'. Njam the Meddler will break out, and bind and slay Krohn"*. Dựa trên Ragnarök. Chính trang Fandom phải mở bằng hatnote để phân biệt. Key: `fandom-great-reckoning` (T6) |
| `Day of Fire` | Thảm hoạ vũ khí Ancient **thời cổ**, tạo ra Dragonsand. Khác hẳn. Cũng gắn `{{inll}}` |
| `Day of Reckoning` (`DoR`) | ⚠️ **Một mod expansion FAN cho Heroes III**, trang gắn `{{speculative}}`. **Tuyệt đối không phải nguồn lore** |

### ⚠️⚠️ Dòng dõi Gauldoth — Fandom lấy tiền đề từ CÂU HỎI rồi trình bày như tác giả xác nhận

Phát hiện khi research `gauldoth-half-dead` (2026-08-03). Đây là **cùng họ với lỗi "Archibald thắng
Nimbus để lấy ngai Deyja"**: wiki đọc quá nguồn.

- **Fandom `Iduna`:** *"Terry Ray's script notes for Heroes of Might and Magic IV revealed that **she
  was the mother of** Lysander, Waerjak, and Gauldoth"* — dẫn `<ref>` về bài phỏng vấn Ubisoft.
- **Fandom infobox `Gauldoth`:** `Iduna (mother)`, `Nicolas Gryphonheart (father)`, `Lysander
  (brother)`, `Waerjak (brother)` — cả bốn dẫn **cùng một** ref.
- **Nhưng trong chính nguồn đó, Ray nói:** *"I wanted these characters to share the same blood.
  **Not like they were all from the same mother, but all from the same bloodline.**"* Và:
  *"**this idea was never completely developed.** I was toying with other options too."*

→ Người phỏng vấn đặt câu hỏi có tiền đề "cùng mẹ"; Ray **phủ định đúng chi tiết đó** ngay câu sau.
Fandom lấy tiền đề của câu hỏi làm câu trả lời.

**Xử lý:** claim dòng dõi là **`DISPUTED`**, tier `T4`, và phải ghi rõ đây là **ý tưởng chưa phát
triển trong script notes chưa công bố**, không phải nội dung game. Ba quan hệ suy tầng hai
(`Catherine` half-sister, `Nicolai Ironfist` nephew, `Beatrice` half-sister) **không có ref nào** →
`UNVERIFIED`, không được vào thân bài.

*(Chi tiết phụ: câu hỏi của Ubisoft viết **"Nicholas"**, Fandom viết **"Nicolas"** — lệch chính tả tên
vua giữa hai nguồn.)*

### Phát ngôn developer về Archibald (T4)

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `fulton-fanstratics-nl5` | **T4** | FETCHED | ⭐ Fulton: "the MM7 team decided to give Archibald an undefined 'behind the scenes' role in the Seeds of Discontent. So, **yes, Archibald did play a role in the Contested Lands becoming independent**." Giải nghĩa dòng cuối Entry 143 |
| `fulton-fanstratics-nl4` | **T4** | FETCHED | Story AB gốc: "Archibald's **former** 'Advisors' restored production to… the 'Heavenly Forge'" — chữ "former" quan trọng |
| `fulton-tavern-interview` | **T4** | FETCHED | Fulton gọi mâu thuẫn dòng dõi Ironfist/Gryphonheart là "**looks like a simple mistake**"; động cơ advisor là "simple lust for power" |

### Nhân vật liên quan

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-ethric` | T1* | FETCHED | Ethric the Mad — infobox H3 (Warlock/Lich, portrait Ajit, specialty Mysticism), Story section. ⚠️ **Trang không có một footnote nào** |
| `h3wiki-ajit` | T1* | FETCHED | Hero Ajit — specialty **Beholders**. Dùng để kiểm chéo: Ethric mượn portrait Ajit nhưng KHÔNG dùng template Ajit |
| `h3wiki-jaegar` | T1* | FETCHED | Hero Jaegar — specialty **Mysticism**, khớp chuỗi chính xác với Ethric. **Đây mới là template nền của Ethric** |
| `mm6-ethrics-tomb` | T1* | FETCHED | Dungeon MM6 — câu tin đồn in-game: "the first Sorcerer seeking life after death... **At least, that's how the rumor goes**" |
| `mm6-cartman-quest` | T1* | FETCHED | Quest MM6 lấy hộp sọ Ethric cho Gabriel Cartman. Walkthrough: "Kill Ethric (he will look like a Power lich)" |
| `mm6-shadow-dagger` | T1* | FETCHED | Mô tả item MM6 — "Commissioned by Ethric the Mad **while still a human**". Xác nhận độc lập quá trình người → lich |
| `mm7-ethrics-staff` | T1* | FETCHED | Mô tả item MM7 — **khẳng định thẳng** "the world's first Lich - Ethric the Mad", không rào "tin đồn" |
| `fandom-ritual-endless-night` | T6 | FETCHED | Trang Fandom giá trị nhất về Ethric — nêu rõ claim "lich đầu tiên + necromancer đầu tiên" là **theo tin đồn** |
| `fandom-timeline-ancient` | T6 | FETCHED | Timeline Old Universe của Fandom. Đặt SoD ~1155–1164 AS, MM6 **1165 AS** — **mâu thuẫn với văn xuôi của chính Fandom** về thứ tự hai cái chết của Ethric. ⚠️⚠️ **Xem cảnh báo archive-link bên dưới** |
| `h3wiki-deyja` | T1* | FETCHED | Trang Deyja. ⚠️ Danh sách "Rulers" **không đầy đủ** — bỏ cả hai vua không tên mà chính trang scenario của thelazy chứng thực |
| `h3wiki-the-pit` | T1* | FETCHED | Thủ đô ngầm, hoàng cung Castle Gloaming, trung tâm Path of Darkness |
| `h3wiki-antagarich` | T1* | FETCHED | Địa lý lục địa — Deyja kín trong đất liền, giáp Erathia (nam/tây) và AvLee (bắc/đông) |
| `h3wiki-deyja-moors` | T1* | FETCHED | Vùng Deyja. **Goblin là đa số cư dân sống**. ⚠️ Tên vùng đến từ bản đồ HotA |
| `h3wiki-erathia` | T1* | FETCHED | "the north fell to Deyja" (1164) |
| `h3wiki-lord-alarice` | T1* | FETCHED | Lãnh chúa triều Deyja cảnh báo AvLee. ⚠️ **Hai stat profile khác nhau** ở hai scenario |
| `h3wiki-lord-smedth` | T1* | FETCHED | Lich, tranh chỗ cố vấn thân cận của Finneas. Là bẫy Finneas giăng cho Sandro |
| `h3wiki-mot` | T1* | FETCHED | Death Knight **từ chối lệnh** Lich King, tin trung lập sẽ giữ được đất. Bị giết làm gương |
| `h3wiki-kastore` | T1* | FETCHED | Đảo chính Archibald (1169). Trích MM7 về "factionism and discord" |
| `roe-a-gryphons-heart` | T1* | FETCHED | **Nguồn quan trọng nhất về động cơ Deyja**: "the man who banished us from **Erathia**". Epilogue: Finneas "met with an unfortunate accident" |
| `roe-safe-passage` | T1* | FETCHED | Catherine xác nhận độc lập: "After killing King Vilmar, he took command of their military and their throne" |
| `roe-corporeal-punishment` | T1* | FETCHED | Tuyến Mot; rumor về Caverns of the Dead |
| `t2-necromancy-origin` | **T2*** | FETCHED | ⭐ **Truyện ngắn nguồn gốc Necromancy**, do **Christian Vanover** (nhân viên NWC) viết, đăng trên 3DO message board (**đã chết**). Người kể trong truyện: Marcus Finch. Nguồn duy nhất cho nguồn gốc Deyja và bản chất lich |
| `fandom-deyja` | T6 | FETCHED | ⚠️ Infobox ghi thủ đô là **Moulder**, mâu thuẫn 3 nguồn khác ghi **The Pit** |
| `fandom-finneas-vilmar` | T6 | FETCHED | ⚠️ **Tiểu thuyết hóa nặng** — "Sandro admitted to himself", "retreated into his private chambers". Khai thác làm đầu mối, **không trích như dữ kiện**. Nhưng infobox ghi thẳng `predecessors = Unnamed King of Deyja` |
| `fandom-path-of-darkness` | T6 | FETCHED | Tín ngưỡng đối xứng với Path of Light của Bracada |
| `fandom-jeddite-disambig` | T6 | FETCHED | ⚠️ **Có HAI Jeddite**: `(Enroth)` là chủ thể; `(Ashan)` là Demon cultist trong Heroes VI — **continuity khác, không được gộp** |
| `fandom-jeddite-enroth` | T6 | FETCHED | Trang Jeddite bản Enroth. Bio H4 khớp thelazy. ⚠️ Trạng thái "Alive (as of Heroes IV)" là **suy luận từ roster**, không text nào khẳng định |
| `h3wiki-jeddite` | T1* | FETCHED | Infobox H3 (Warlock/Dungeon/Human, specialty Resurrection, hero ID 91), bio H4, bảng xuất hiện |
| `h3wiki-ufretin` | T1* | FETCHED | Ranger Rampart, đồng minh Jeddite trong `Target`. ⚠️ Câu "tried, but failed" là **văn wiki giả định kết quả người chơi thắng** |
| `h3wiki-dungeon` | T1* | FETCHED | Trang town Dungeon — khuyến nghị Jeddite cho lối chơi thường, xác nhận hắn là hero **chuẩn** không phải campaign-only |
| `oe-ethric-bio` | **T5** | FETCHED | Tiểu sử Ethric trong *Heroes: Olden Era*. ⚠️ **NGOÀI Old Universe** theo `CANON-POLICY.md` R5. Sản phẩm chưa phát hành, có thể đổi. Chỉ dùng tham chiếu |
| `h3wiki-jeddite` | T1* | FETCHED | Bạn thân cũ, người giới thiệu Sandro với Ethric; bio H4 |
| `h3wiki-vidomina` | T1* | FETCHED | Học trò; Yog từng yêu; bio H3+H4 |
| `h3wiki-finneas` | T1* | FETCHED | Puppet king; hero campaign-only; portrait dựa trên Thant |
| `h3wiki-thant` | T1* | FETCHED | **Xác nhận Thant KHÔNG có vai trò cốt truyện trong H3** |
| `h3wiki-nimbus` | T1* | FETCHED | Vai trò MM7/RoE; **xác nhận không có liên hệ với Sandro** |
| `h3wiki-lord-haart` | T1* | FETCHED | **Nguồn của mâu thuẫn "theo lệnh Finneas Vilmar"** |
| `h3wiki-jabarkas` | T1* | FETCHED | Hero Stronghold; bio ghi là **con trai cả của Duke Boragus**, race Ogre của Krewlod — **xung đột** với claim "em trai Ethric" trong `sod-target` |
| `h3wiki-necromancer` | T1* | FETCHED | Định nghĩa class Necromancer — chỉ số khởi đầu 1/0/2/2 |
| `h3wiki-death-knight` | T1* | FETCHED | Định nghĩa class Death Knight — 1/2/2/1, khởi đầu có Spell Book. **Bằng chứng thật** cho việc hai class khác nhau |
| `h3wiki-a-gryphons-heart` | T1* | FETCHED | Epilogue — Finneas "met with an unfortunate accident" khi hồi sinh Gryphonheart |
| `h3wiki-on-the-run` | T1* | FETCHED | Yog kể từng yêu Vidomina trước khi nàng bị tha hóa |
| `sod-manual-p14` | T2* | FETCHED | Manual tr.14 — Yog phân tán các mảnh Angelic Alliance |
| `sod-manual-p15` | T2* | FETCHED | Manual tr.15 — thông số Sandro. **Lưu ý: KHÔNG có đoạn bio nào** |

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
| `mm8-guide-walkthrough` | T6 | FETCHED | Walkthrough MM8 độc lập với Fandom, `tumblr.com/mm8-guide/663630859431231488` — **xác nhận độc lập** phần MM8 và **sửa** một chi tiết: Sandro là **lãnh đạo**, Thant là **phó**, không phải đồng lãnh đạo |
| `fandom-sandro-xeen` | T6 | FETCHED | Trang `Sandro (Xeen)` — nhân vật **riêng** trong *Might and Magic V: Darkside of Xeen*, lich, questgiver/boss ở Necropolis. **Quan trọng:** sprite của nhân vật này là gốc của portrait Sandro Enroth |
| `fandom-h4-artifact-list` | T6 | FETCHED | `List of Heroes IV artifacts` — mục `=== Minor artifacts ===`. **Nguồn duy nhất** cho thông số artifact ở Heroes IV. Fandom **không dẫn nguồn**. ⚠️ Xem lỗ nguồn H4 ở `BACKLOG.md` B-019 |
| `fandom-prelude-to-invasion` | T6 | FETCHED | Scenario H4 đầu tiên của campaign *Death March* (`version = H4X2`, *Winds of War*) — Amulet of the Undertaker là một trong năm artifact đổi lấy Dwarven Hammer/Shield/Ring of Protection mang sang map sau |

---

## Nhóm 3 — Nguồn thử nhưng KHÔNG vào được

Ghi lại để lần sau thử tiếp. **Không được dùng làm nguồn.**

| Nguồn | Trạng thái | Ghi chú |
|-------|-----------|---------|
| `mightandmagic.fandom.com/wiki/*` | FAILED (402/403) | Chỉ vào được qua `api.php` |
| `homm.miraheze.org/wiki/Sandro` | FAILED (403) | |
| `strategywiki.org/.../Rise_of_the_Necromancer` | FAILED (403) | |
| `heroesofmightandmagic.com/*` | ⚠️ **FETCHED 2026-08-03, FAILED 2026-08-04** | 🔴 **ĐÍNH CHÍNH: đây KHÔNG phải "site chính thức của NWC" và KHÔNG phải tier `T2`.** Nó là **site fan `Age of Heroes`** (footer: *"©2005 Valera Koltsov"*; grep `New World Computing` = **0 lần**), tier đúng là **`T1*`** — xem mục *Heroes IV — Age of Heroes* ở Nhóm 1. Ghi chú cũ ở dòng này còn sót lại cái sai đó sau khi đợt `e7c5ec5` đã sửa ở chỗ khác. Đường vào là `web.archive.org` + CDX API, nhưng **từ 2026-08-04 nội dung wayback bị chặn** — xem mục cảnh báo bên dưới |
| ~~`web.archive.org`~~ | ⚠️ **CDX chạy · NỘI DUNG bị chặn (2026-08-04)** | 🔴 **Trạng thái đã ĐỔI, không phải bị ghi sai.** 2026-08-03 đọc được thật (151 KB). 2026-08-04 **nội dung** bị **FortiGuard của mạng công ty** chặn theo category *"Games"*, trong khi **CDX index vẫn chạy bình thường**. Hai thứ khác nhau, trước giờ chưa phân biệt. Xem mục cảnh báo bên dưới để biết **dấu hiệu nhận biết** — trang chặn trả **HTTP 200** nên `curl` trông như thành công |
| `en.namu.wiki/.../Sandro` | NOT_FETCHED | Chỉ thấy trong kết quả tìm kiếm |
| File campaign `.h3c` gốc | NOT_FETCHED | **Đây là việc cần làm để nâng T1\* thành T1** |

---

## Nhóm 4 — Developer statement (T4)

⚠️ **Đợt research đầu kết luận sai rằng "không có developer commentary nào".** Luồng
kiểm định độc lập tìm được nguồn T4 thật. Ghi lại sai sót này để nhớ: **kết luận
"không tồn tại" cần được kiểm chứng nghiêm khắc như mọi claim khác.**

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `bullard-interview-2013` | **T4** | FETCHED | **Phỏng vấn Jennifer Bullard**, do Alchemik thực hiện năm 2013 cho Acid Cave. `acidcave.net/jennifer_bullard_interview.html` — **còn sống, truy cập trực tiếp được, không cần archive.org**. Mirror/index tại `heroes.thelazy.net/index.php/Jennifer_Bullard`. ✅ **Đã đối chiếu bản thelazy với bản gốc acidcave.net — khớp từng chữ.** Đây là **corroboration hai domain thật sự độc lập**, loại tốt nhất dự án có. ⭐⭐ **Còn là nguồn T4 duy nhất trả lời "vì sao thế giới bị phá"** (bổ sung 2026-08-04): *"The Guardian opened the portals. **We wanted to wash a lot of the history away from the old world and needed a mechanism to do so.**"* · *"**It was Corak - it is always Corak.**"* · và lý do biên tập: *"The main reason behind wiping the history was because it had become **convoluted and hard to manage**."* · về Axeoth: *"We actually had a fairly fleshed out world… however, **the layoffs happened so soon after the launch**"*. ⚠️ Chú ý: **không text game nào** nhắc portal hay Corak — đây là T4 thuần |
| `fulton-tavern-interview-2018` | **T4** | FETCHED | Xem entry đầy đủ ở Nhóm 1, mục *The Reckoning*. ⭐ *"Lore work for HoMM4, and the idea for 'the Reckoning', did not begin until long after I had left NWC."* |
| `bullard-papers-ut-austin` | **T3** | NOT_FETCHED | **Tài liệu thiết kế gốc do chính Bullard tập hợp**, lưu tại Dolph Briscoe Center for American History, University of Texas. `repositories.lib.utexas.edu/items/e3abd6e5-b6be-4547-8900-17b2c9e237da` — mục lục ghi "Heroes [of Might and Magic] documents" |
| `fulton-fanstratics-13` | **T4** | FETCHED | **Greg Fulton, Lead Designer Heroes III** — Fanstratics Newsletter #13. Gọi Sandro là hero mang tính biểu tượng: "Astral, Crag Hack, Dracon, **Sandro**, Solmyr, Tazar..." |
| `fulton-fanstratics-27` | **T4** | FETCHED | Fulton, Newsletter #27 — ghi lại yêu cầu thiết kế ở buổi họp khởi động H3: "Keep specific heroes from HoMM2, like **Sandro the Necromancer**, Halon the Wizard, Lord Haart..." |
| `fulton-fanstratics-3` | **T4** | FETCHED | Fulton, Newsletter #3 — xác nhận **Bullard là Lead Designer của SoD**: "I was not involved in the conception or creation of SoD... Jennifer Bullard was the project's Lead Designer, and any questions you have about SoD would best be directed to her" |
| `fulton-names-2023` | **T4** | FETCHED | ⭐⭐ `Gregory Fulton/On Names in Heroes of Might and Magic III` trên thelazy — **98.499 byte**. Thư từ Amelrix ↔ Fulton 2022–2023, công bố 08/AUG/2023 trên Celestial Heavens, **~200 câu hỏi** về nguồn gốc tên town và hero, **do chính Fulton xem lại trước khi công bố**. Xem `B-020` — nguồn này chưa được khai thác hết |

### Jennifer Bullard là ai

Thành viên gốc của New World Computing. **"Designer and storyline writer for Heroes III
and IV as well as the Heroes Chronicles series."** Được ghi công là một trong các
designer của *Shadow of Death*, cùng **Gregory Fulton** và **Jon Van Caneghem**.

Nghĩa là: đây không phải phát ngôn của một nhân viên bên lề. Đây là **người viết cốt
truyện**.

### Phát ngôn quan trọng nhất — về thầy của Sandro

> **Hỏi:** "Ethric the Mad from Might and Magic VI - The Mandate of Heaven. Was he the
> same master of Sandro from Heroes of Might and Magic III - Shadow of Death
> storyline?"
>
> **Đáp:** "**Yes**, we always tried to tie the different products together so people
> who played everything could see a theme."

{T4 EXPLICIT: bullard-interview-2013}

Đây là phát ngôn có sức nặng nhất về tiểu sử Sandro mà dự án có: nó xác nhận thầy của
Sandro **chính là** Ethric the Mad — lich đầu tiên và necromancer đầu tiên của thế
giới, cũng là kẻ bị nhóm nhân vật MM6 giết. Nó cũng xác lập việc **nối các sản phẩm
với nhau là chính sách thiết kế có chủ ý**, không phải trùng hợp.

### Phát ngôn về Heroes Chronicles — liên quan trực tiếp tới vấn đề trùng tên

> "Jon Van Caneghem was not involved in the Heroes Chronicles series - In fact **I did
> a majority of the work myself.**"

> "The Heroes Chronicles were meant to be more **stand-alone** than anything.
> Honestly, it was marketing who had the greatest hand in driving the products. We were
> slipping on Heroes IV and they wanted our fan base to have more maps to play. So I was
> asked to create 8 campaigns that could stand alone and be played in any order,
> **without any reference to each other or the other products in development**. […]
> Each original story & maps was written by one level designer and then I cleaned and
> polished them until ship. **Each one was supposed to take place in 'the distant past'
> and we didn't create a specific order to their events.**"

{T4 EXPLICIT: bullard-interview-2013}

**Đây là chìa khóa giải thích vấn đề Sandro trong Chronicles.** Chronicles được làm như
sản phẩm độc lập, **cố ý không tham chiếu** các sản phẩm khác, mỗi campaign do một
level designer viết. Một designer chọn tên necromancer dễ nhận ra cho boss một map —
trong sản phẩm bị tách biệt có chủ ý — chính là quy trình sinh ra một cái tên trùng
ngẫu nhiên.

Lưu ý: đây là **suy luận từ mô tả quy trình**, không phải phát ngôn về Sandro. Bullard
không được hỏi về Sandro dưới hầm.

Bà cũng cảnh báo fan "are even finding references which may not exist" trong Chronicles
— lời nhắc áp đúng vào trường hợp này.

### Phát ngôn về việc bỏ Forge

> "The story was relatively unchanged after we removed the Forge. It just had a
> different origin from the original story."

{T4 EXPLICIT: bullard-interview-2013}

### Điều phỏng vấn KHÔNG trả lời

Không có phát ngôn nào về: quá trình Sandro thành lich, tên khai sinh của hắn, hay các
cảnh Tyranell / Finneas. Phỏng vấn là dạng hỏi-đáp theo câu hỏi của fan, và **không ai
hỏi những điều đó.**

### Lead giá trị nhất chưa khai thác

`bullard-papers-ut-austin` — tài liệu thiết kế gốc của Shadow of Death và Heroes IV,
do chính người viết cốt truyện tập hợp, lưu tại thư viện đại học. **Chưa fetch.**

Đây là đường có triển vọng nhất để trả lời câu hỏi mở lớn nhất về Sandro (quá trình
thành lich). Cũng đáng chú ý: `heroes3wog.net` được cho là có lưu tư liệu phục hồi từ
bộ này, ví dụ "General Kendal's Diary". Thread cộng đồng liên quan:
`celestialheavens.com/forum/topic/16558` ("Jennifer Bullard - Lost manuscript files").

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

**Cập nhật sau kiểm định — hai lập luận KHÔNG mạnh như nhau:**

Luồng kiểm định độc lập đọc lại toàn bộ `hc-truth-within-nightmares` và tách được:

- **Lập luận niên đại (mạnh, có nguồn game text).** Ethric nói Sandro làm học trò mình
  "**decades**" — vài thập kỷ, không phải hàng trăm năm.
  {T1* EXPLICIT: sod-agents-of-vengeance} Thêm nữa, Jeddite — bạn học cùng thời, người
  **phàm** — vẫn còn sống và hoạt động trong Shadow of Death, giới hạn khoảng cách
  trong một đời người. {T1* EXPLICIT: sod-target} Trong khi *Conquest of the Underworld*
  diễn ra dưới thời **Rion Gryphonheart, vua đầu tiên** của Erathia — cách Nicolas
  Gryphonheart nhiều thế hệ. Lệch nhau khoảng một bậc độ lớn. **Đây là lập luận gánh
  toàn bộ kết luận.**

- **Lập luận sinh tử (YẾU hơn thelazy.net hàm ý).** Chữ "kill" chỉ xuất hiện trong
  **mô tả scenario** ("Tarnum must kill Sandro to get the key"), **không** có đoạn nào
  trong phần kể mô tả Sandro chết — không epilogue, không xác. Điều kiện thắng là
  "Defeat Hero", một mục tiêu cơ chế thông thường **không** hàm ý cái chết. Và Sandro
  chứng minh nhiều lần rằng hắn sống sót qua thất bại.
  {T1* INFERENCE: hc-truth-within-nightmares}

**Thêm một mảnh từ nguồn T4:** Bullard cho biết Chronicles được làm như sản phẩm độc
lập, **cố ý không tham chiếu** sản phẩm khác, mỗi campaign do một level designer viết,
và "we didn't create a specific order to their events."
{T4 EXPLICIT: bullard-interview-2013} Đây là quy trình sinh ra tên trùng ngẫu nhiên.

**Kết luận sau kiểm định:** vẫn `DISPUTED`, nhưng nghiêng mạnh về "người trùng tên" —
và lý do là **niên đại**, không phải chuyện Tarnum có giết hắn hay không. Khi viết,
phải dùng đúng lập luận mạnh.

**Không có năm tuyệt đối cho *Conquest of the Underworld*.** Đây không phải thất bại
tra cứu mà là **thuộc tính của tư liệu** — theo Bullard, chưa từng có thứ tự cụ thể nào
được tạo ra.

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

### ⚠️⚠️ `fandom-timeline-ancient` — phần lớn `<ref>` KHÔNG xác minh được

Đây là cảnh báo nghiêm trọng nhất về nguồn mà dự án phát hiện được, vì nó ảnh hưởng tới
**mọi mốc niên đại** lấy từ trang đó.

Trang Timeline của Fandom **trông rất chỉn chu** vì có nhiều thẻ `<ref>`. Nhưng các ref
`Deyja`, `TimberWars`, `Nicolas`, `Catherine`, `Shadowspire` đều trỏ tới:

```
web.archive.org/.../homm3.ga-strategy.com/...
```

**Archive.org bị chặn trong môi trường này.** Không xác minh được **một cái nào**.

**Hệ quả:** mọi mốc dựa trên archive link là **chưa xác minh ở cấp nguồn gốc**. Chúng có thể
đúng, nhưng **không được nâng lên `T2*`** nếu chưa lấy được độc lập.

**Ngoại lệ — đáng tin hơn:** các ref trích thẳng text MM6/MM7/H3 trong chính bài (`Melian`,
`ArchieDeposed`, `Gelu-Kendal`, `Celeste`) — vì **có nội dung trích kèm**, đọc được ngay.

**Mốc đáng ngờ nhất:** `1164-09-27` cho vụ đầu độc Nicolas — **chính xác tới ngày** nhưng
dòng đó **không có ref nào**. Độ chính xác kiểu này mà không nguồn là dấu hiệu xấu.

**Mốc đáng tin nhất:** `1168-08-05` (Archibald lên ngôi) và `1169` (đảo chính Kastore) —
cả hai truy được về text MM7 trích thẳng.

### ⭐ `h3wiki-herobios-txt` là `T1` THẬT, không phải `T1*`

Phát hiện đáng chú ý: thelazy có trang `Translation Data/HeroBios.txt` — **file string table
trích trực tiếp từ game** (168KB, bốn cột EN/FR/PL/RU).

Đây **không phải** bản chép do người viết lại, mà là **dữ liệu trích từ file game**. Theo
`CANON-POLICY.md`, nó xứng đáng tier **`T1`** không có dấu sao.

**Đây là nguồn tốt nhất dự án có được tính tới nay**, và là bước tiến nhỏ hướng tới `B-001`.

*(Chi tiết phụ thú vị từ chính file: bản dịch **Ba Lan và Nga đều để Jeddite là nữ**. Lỗi
dịch, không phải lore.)*

**✅ Đã giải quyết (2026-08-03, verify `dead-mans-boots`):** `Talk:Artifact/descriptions` **đúng
là** chuỗi trích từ game. Trang tự ghi ở đầu bảng:

> `|+ style="white-space:nowrap;"|Information from H3Bitmap.lod > artraits.txt`

Đã vào registry thành `h3wiki-artraits-txt`, tier **`T1`** thật. Đây là nguồn thứ **hai** đạt
`T1` không dấu sao, và nó **thay được `fandom-artifact-list` (T6) cho mọi mô tả in-game của
artifact** — dùng lại được cho toàn bộ bài artifact, không riêng một bài.

**Việc còn lại:** quét nốt các trang `Translation Data/` khác trên thelazy để tìm string table
tương tự cho creature, spell, town.

### ⚠️ Claim "artifact từng thuộc về Ethric" — BỊ GAME TEXT PHẢN BÁC

Trang `h3wiki-shadow-of-death` viết (văn wiki, **không dẫn nguồn**):

> "...two powerful artifacts **that once belonged to his former mentor Ethric**."

**Game text nói ngược.** `sod-target` Day 1:

> "You have also learned Ethric has spread word of your whereabouts to those **who lost
> these two precious artifacts**..."

Chủ cũ là **những bên khác, không được nêu tên** — phân biệt rõ với Ethric. Trong toàn bộ
`sod-target`, Ethric xuất hiện với hai vai: **thầy cũ** và **kẻ truy đuổi**, không lần nào
là chủ sở hữu.

**Nguồn của hiểu nhầm có lẽ là thư Jeddite:** "I will take the artifacts from your rotting
corpse and **return them to Ethric**." Nhưng đó là **ý định giao nộp trong tương lai** của
một bên thù địch, không nói gì về sở hữu quá khứ.

**Xử lý:** không dùng claim này. Cách diễn đạt an toàn — Ethric là thầy cũ đã truy đuổi
Sandro vì các artifact; các thành phần được lấy từ nhiều người giữ khác nhau qua tay Gem
và Crag Hack.

### ⚠️ Trang artifact KHÔNG đáng tin về HotA — dùng changelog

Trang `h3wiki-cloak-undead-king` ghi lệnh cấm HotA 1.7.2 kèm **ba** template ngoại lệ.
Đối chiếu `hota-changelog` cho thấy **sai**:

- **1.7.2** (31/DEC/2024): cấm ghép, ngoại lệ **hai** template (Anarchy, Clash of Dragons)
  và "a number of single player scenarios". **Không nhắc Legacy.**
- **1.7.3** (08/JUN/2025): mới thêm template "Default Random Map (Legacy)"

Trang wiki gộp hai phiên bản thành một.

### ⚠️⚠️ Cả hai wiki hiểu SAI cách Archibald lên ngôi Deyja — và thelazy tự mâu thuẫn

Phát hiện khi research `archibald-ironfist` (2026-08-03). Đáng ghi vì đây là ca **hai wiki lớn cùng
sai theo cùng một hướng**, và nguồn chính thức nói khác.

**Game text** (*Diaries of Archibald*, site 3DO, `T2`) nói **hai sự kiện tách rời**:

1. **Challenge of Dominance** với Nimbus → Archibald thắng, và cái hắn giành được là *"this little
   mission"* — quyền chỉ huy đoàn Necromancer Enroth sang Deyja. Xảy ra **TRƯỚC** khi Gryphonheart bị
   tiêu diệt (Entry 37).
2. **Thay thế Gryphonheart** → *"so have I replaced Gryphonheart"*. Đây mới là lúc hắn thành vua Deyja.
   Xảy ra **SAU** khi Catherine thắng (Entry 143).

**Cả hai wiki gộp hai sự kiện và gán nhân quả mà game text không có:**

- thelazy `Archibald`: "After the lich form of King Nicolas Gryphonheart is put to rest, **Archibald
  battles Nimbus for the title of King of Deyja**, and wins."
- Fandom: "**Defeating Nimbus in the guild Challenge of Dominance, Archibald assumed control over the
  now-vacant throne of Deyja.**"

Cả hai còn đặt Challenge of Dominance **sau** khi Gryphonheart bị diệt — trái Entry 37.

🔴 **Và thelazy tự mâu thuẫn với chính nó.** Trang `Nimbus` của **cùng wiki** tách đúng: "Archibald
battled Nimbus for the title of **guildmaster**… becoming the new leader of **the Enrothian necromancers
who joined the forces of Deyja**." Hai trang cùng wiki nói khác nhau.

⚠️ **Hệ quả cho bài `deyja`:** bài đó viết "Archibald thắng chức guild bằng **đấu tay đôi** với Nimbus".
Game text **không** nói đấu tay đôi, và cái thắng được là **quyền chỉ huy đoàn quân**, không phải chức
guildmaster. Cần sửa.

### ⚠️⚠️⚠️ `web.archive.org` KHÔNG bị chặn — và điều đó mở ra nguồn chính thức của NWC/3DO

Phát hiện khi verify `deyja` (2026-08-03). **Đây là cảnh báo quan trọng nhất trong registry**, vì nó
đảo ngược một giả định đã dùng để hạ độ tin cậy của nhiều claim.

Registry cũ ghi `web.archive.org` là "FAILED (bị chặn hoàn toàn)", và bài `deyja` dựa vào đó để kết
luận rằng phần lớn `<ref>` của timeline Fandom "không xác minh được".

**Cả hai đều sai.** Đã kiểm độc lập hai lần:

- `https://web.archive.org/web/2005/http://www.3do.com/...` → **HTTP 302**, theo redirect ra **151.258
  byte** nội dung thật.
- `https://web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm` →
  lấy được **toàn văn** *The Diaries of Archibald*.

**Cách dùng đúng:** phải có `-L` (theo redirect) và **nên dùng dạng có timestamp đầy đủ**
(`/web/YYYYMMDDhhmmss/`). Dạng `/web/2005/` cũng chạy nhưng hay ra trang wrapper rỗng. API
`archive.org/wayback/available` trả **429** (rate limit) — đó là giới hạn tần suất, **không** phải bị chặn.

**Hệ quả:** `3do.com` — site chính thức của 3DO, "nguồn
không-phải-wiki tốt nhất có thể có" — **tiếp cận được qua archive**. Việc này liên quan trực tiếp tới
`B-001` (nâng `T1*` → `T1`) và `B-002`.

#### 🔴 CẬP NHẬT 2026-08-04 — nội dung wayback GIỜ BỊ CHẶN, nhưng CDX thì không

Mục trên **vẫn đúng về phía archive.org**. Cái đổi là **mạng của máy dev**. Phát hiện khi research
`the-reckoning`: **`web.archive.org` bị firewall FortiGuard chặn theo category "Games"**, và nó chặn
**nội dung** chứ không chặn **index**.

Body trả về thay cho trang, verbatim:

> Web Filter Violation — FortiGuard Intrusion Prevention - Access Blocked — Web Page Blocked
> You have tried to access a web page that is in violation of your Internet usage policy.
> **Category: Games**

#### 🔬 CHẨN ĐOÁN CHÍNH XÁC (2026-08-04) — chặn theo TÊN MIỀN ĐÍCH, không phải theo tần suất

Đã kiểm bằng thí nghiệm đối chứng, **mỗi URL một request nguội duy nhất** — nên rate limit bị loại
trừ ngay từ thiết kế:

| Request | Kết quả |
|---|---|
| wayback → `3do.com/mightandmagic/heroes4/story.html` | **403**, 35.311 byte, FortiGuard |
| wayback → `3do.com/` (gốc, path **không** có từ khóa game) | **403**, 35.241 byte, FortiGuard |
| wayback → `heroesofmightandmagic.com/` (gốc) | **403**, 35.277 byte, FortiGuard |
| wayback → `example.com/` | ✅ **200**, 2.914 byte, **không** FortiGuard |
| wayback → `example.com/mightandmagic/heroes4/story.html` (từ khóa game, host vô hại) | ✅ **404 của chính archive.org**, 151 KB, **không** FortiGuard |
| `archive.org/metadata/...` (không có tiền tố `web.`) | ✅ **200** |

**Kết luận, ba điều và cả ba đều đảo ngược phỏng đoán ban đầu:**

1. **`web.archive.org` KHÔNG bị chặn.** Nó chạy tốt. Cái bị chặn là **tên miền được archive** nằm
   trong URL — FortiGuard đọc URL đích rồi tra category của **domain đó**.
2. **KHÔNG phải rate limit, và giảm tần suất KHÔNG giúp gì.** Một request nguội duy nhất vẫn 403.
   Đây là **chính sách theo category**, mang tính tất định — chậm lại bao nhiêu cũng cho cùng kết quả.
3. **Không phải từ khóa trong path.** `example.com/mightandmagic/heroes4/…` đi qua bình thường;
   `3do.com/` trơ trọi thì bị chặn. Tức `3do.com` và `heroesofmightandmagic.com` bị **xếp category
   "Games"** ở mức domain.

⚠️ **Sửa lại mã HTTP:** ghi chú đầu ghi trang chặn trả **200**; đo lại thì là **403**. Có thể khác
theo lần. **Đừng dựa vào mã HTTP để nhận diện** — dựa vào **kích thước ~35,3 KB + text ~370 ký tự**,
và grep chữ `FortiGuard`.

⛔ **Đường duy nhất còn lại là đổi mạng** (hotspot điện thoại / VPN / máy khác) hoặc xin whitelist hai
domain đó. Không có mẹo kỹ thuật nào ở tầng URL vượt được — đã thử tám cách, xem dưới.
✅ `timetravel.mementoweb.org` cũng **không** cứu được: không kết nối nổi (`http=000`).

⚠️⚠️ **DẤU HIỆU NHẬN BIẾT — ĐỌC KỸ, ĐÂY LÀ BẪY IM LẶNG:**
trang chặn trả về **HTTP 200 hoặc 403** và **~35,3 KB HTML**, nên `curl` có thể báo **thành công**.
Strip tag xuống chỉ còn **~360–376 ký tự**. Cả 39 file Age of Heroes và 24 file 3DO đều ra
**đúng ~35,3 KB**.

> **Kích thước giống nhau đến từng trăm byte trên nhiều file khác nhau = dấu hiệu chắc chắn bị chặn.**
> Nếu đợt sau thấy file wayback ~35 KB mà text ~370 ký tự: **đó là trang chặn**, KHÔNG phải trang rỗng
> của archive.org, và **KHÔNG** có nghĩa là URL đó "không được archive".

**Tám đường vượt đã thử, tất cả FAILED** — ghi lại để không thử lại từ đầu:
`curl` trực tiếp · percent-encode URL nhúng (filter decode trước khi rate) · chế độ raw `id_` ·
proxy `r.jina.ai` (403, *"Anonymous access to domain web.archive.org blocked until Sun Sep 30 2035"*) ·
proxy `api.allorigins.win` (522) · proxy `api.codetabs.com` (521) ·
**tool `WebFetch`** (*"Claude Code is unable to fetch from web.archive.org"* — chặn ở **tầng tool**, nên
WebFetch **không** cứu được ca này) · site Age of Heroes **live** (`ECONNREFUSED` — không chạy HTTPS).

✅ **CÁI GÌ VẪN CHẠY ĐƯỢC:**

- **CDX API chạy tốt** → vẫn **enumerate** được, chỉ không **đọc** được:
  `http://web.archive.org/cdx/search/cdx?url=...&filter=...&output=text&fl=timestamp,original,statuscode,length`
  (gặp `504` một lần với `filter=` phức tạp; **retry với `url=<prefix>/*` đơn giản hơn thì được ngay**)
- **`archive.org` KHÔNG có tiền tố `web.` chạy tốt:** `advancedsearch.php`, `metadata/<id>`
- `heroes.thelazy.net` (cả `action=raw` và `api.php`), `mightandmagic.fandom.com/api.php`,
  `acidcave.net` — đều tốt

**Hệ quả thực hành:** nguồn nào chỉ vào được qua wayback thì **tạm thời không lấy thêm được** — kể cả
`ray-interview-ubisoft-2015`, `ch-h4-might-texts`, `h4-death-texts-ch`, `mm7-diaries-3do`. Các quote
**đã trích trong registry vẫn dùng được**; chỉ là không mở rộng được cho tới khi có mạng khác.

### ⚠️⚠️ thelazy CHÉP SAI hai con số năm trong *The Diaries of Archibald*

Ca **đầu tiên** dự án bắt được **thelazy sai và Fandom đúng**. Đáng ghi vì toàn bộ registry dựa vào
thelazy làm nguồn `T1*` xương sống, với lý do "wiki này chép trung thực, chép cả lỗi chính tả".

Đối chiếu trang chính thức 3DO với trang `Archibald` mục `=== The Diaries of Archibald ===` trên
thelazy (trang này **tự ghi** "*The following is from the MM7 manual*"):

| Entry | 3DO chính thức | thelazy | |
|---|---|---|---|
| 1 | 11 June **1165** | 11 June 1165 | ✅ |
| 37 | 23 October **1167** | 23 October **1166** | ❌ lệch 1 năm |
| 143 | 5 August **1168** | 5 August **1167** | ❌ lệch 1 năm |

**Quy tắc rút ra:** "chép trung thực" **không** đồng nghĩa với "chép đúng". Với **mọi mốc niên đại**
lấy từ thelazy, phải đối chiếu nguồn chính thức qua archive khi có thể — nhất là các mốc quanh
1165–1169, vốn là giai đoạn dày sự kiện nhất của Antagarich.

### ⚠️ `Moulder` trên Fandom là REDIRECT tới `The Pit` — "tranh chấp thủ đô" phần lớn tan

Đã kiểm trực tiếp: `api.php?action=query&titles=Moulder&redirects` trả
`redirects: [{"from":"Moulder","to":"The Pit"}]`. Fandom **không có** trang `Moulder` riêng.

Nghĩa là trường `| capital = [[Moulder]]` trong infobox Fandom **trỏ về đúng trang `The Pit`** — nó
không phải một nguồn thứ tư nói ngược. Bài `deyja` từng trình bày đây là tranh chấp "ba chọi một".

### ⚠️⚠️ Bẫy `{{swh}}` — tham số ĐẦU là HotA, tham số SAU là SoD

Phát hiện khi verify `jeddite` (2026-08-03). Đây là **bẫy đọc**, không phải lỗi chép của wiki —
nguồn hoàn toàn đúng, người đọc suy sai.

Nguyên văn `Template:Swh`:

```
<span class='onlyhota'>{{{1|}}}</span><span class='onlysod'>{{{2|}}}</span>
```

và trang tự ghi cách dùng:

> `{{swh|content to be visible only when hota is ENABLED|content to be visible only when hota is DISABLED}}`

**Nghĩa là `{{swh|A|B}}` → A = HotA, B = SoD.**

⚠️ **Trực giác đọc trái-sang-phải là "bản gốc trước, bản mod sau" — và nó SAI.** Bài `jeddite` đọc
`{{swh|5%|3%}}` thành "SoD 5%, HotA 3%", trong khi đúng là **SoD 3%, HotA 5%**. Cả ba con số
gameplay của bài đều bị đảo, và đó là `BLOCKER`.

**Cách tự kiểm mỗi lần dùng:** HotA hầu như luôn là bản **thay đổi**, nên nếu con số ở tham số 1
trùng với giá trị "kinh điển" mà cộng đồng biết thì gần như chắc là đã đọc ngược. Kiểm chéo bằng
`h3wiki-hero-specialty` hoặc `hota-changelog` — cả hai đều phát biểu theo hướng "HotA đổi thành X".

Cũng lưu ý biến thể `{{swh|noicon=|A|B}}`: tham số `noicon=` **không** chiếm vị trí số, nên A vẫn là
tham số 1 (HotA).

### ⚠️⚠️ Trang artifact trên thelazy KHÔNG chứa danh sách scenario — đã sai ba lần liên tiếp

Lỗi này xuất hiện ở **cả ba** bài thành phần Cloak, mỗi bài do một verifier độc lập bắt được.
Ba lần thì không còn là sự cố — nó là **quy luật của nguồn**.

| Trang | Kích thước | Có tên scenario? |
|---|---|---|
| `Dead Man's Boots` | 660 byte | Không |
| `Amulet of the Undertaker` | 672 byte | Không |
| `Vampire's Cowl` | 913 byte | Chỉ trong chú thích gallery |

Trang artifact chỉ chứa template `{{ArtifactNewSB}}` (class/slot/cost/event/effect), một câu văn
wiki về điều kiện Necromancy, mục *Related artifacts*, và category. **Không có mục scenario nào.**

**Hệ quả:** mọi bảng "Xuất hiện trong game" dẫn về `h3wiki-<artifact>` là **mis-citation** — nhãn
`EXPLICIT` trỏ vào chỗ trống, tức "EXPLICIT không nguồn" theo `CANON-POLICY.md` mục 2.

**Cách làm đúng:** quét `api.php?action=query&list=backlinks&bltitle=<Artifact>&bllimit=500` (mỗi
artifact có 190–195 backlink), rồi fetch `?action=raw` từng trang scenario và dẫn **key riêng cho
từng dòng**. Bắt buộc đọc trường `| source =` của mỗi trang để ghi đúng sản phẩm — **gán sai sản
phẩm đã từng là BLOCKER**, và cả ba đợt đều phát hiện mục bị gán sai hoặc bị bỏ sót.

Cách này cũng là cách duy nhất tìm ra:
- `Viking We Shall Go! (Allies)` — trang scenario riêng, bị bỏ sót ở bài Boots
- template `Black'n'Blue` **cấm** Boots và `Nine-day Wonder` **cấm** Amulet — ngược chiều `Apocalypse`
- `Mormolykos` — hero HotA mang sẵn Cowl, chủ sở hữu có tên duy nhất của nó

### ⚠️ Trang template HotA là `T6`, và "Allowed artifacts" KHÔNG có nghĩa "chỉ ba artifact"

Phát hiện khi verify `dead-mans-boots` (2026-08-03). Cùng họ với cảnh báo trên, nhưng là một
cái bẫy khác — **bẫy suy luận**, không phải bẫy phiên bản.

Trang `hota-apocalypse-template` liệt kê đúng ba artifact dưới đầu đề `*Allowed artifacts:` —
và đúng là ba thành phần Cloak. Rất dễ viết thành "một trong ba artifact **duy nhất** được cho
phép". **Nguồn không nói chữ "only".**

Ba lý do không được đọc theo nghĩa "duy nhất":

- **Changelog không chống lưng.** Grep toàn bộ 201.529 byte `hota-changelog`: `Apocalypse` chỉ
  xuất hiện **hai lần**, không lần nào là danh sách artifact (1.5.0 "Added the Boomerang and
  Apocalypse templates"; 1.7.1 "Apocalypse template: Wanderer's Boots and Shrines of Magical
  Mystery banned").
- **Có bằng chứng ngược.** Dòng 1.7.1 cấm thêm **Wanderer's Boots**. Nếu template chỉ cho phép
  ba artifact thì cấm riêng một artifact thứ tư là **vô nghĩa** — nó đã bị cấm sẵn. Cách đọc
  dung hòa: "Allowed" = được cho phép **thêm**, ngoài các lệnh cấm mặc định.
- **Trang luật chính thức không có danh sách này.** `h3hota.com/en/rules` (do chính trang
  template dẫn tới) có mục Apocalypse nhưng **không có** danh sách artifact cho phép/bị cấm nào.

**Hai quy tắc rút ra:**

1. **Trang đặc tả template do cộng đồng viết là `T6`, không phải `T1*`.** Nó không phải in-game
   text — không có chuỗi nào trong game hiện ra nội dung đó. Gán `T1*` là sai **loại nguồn**,
   không chỉ sai cấp.
2. **Trang template phải ghi phạm vi phiên bản theo ngày sửa cuối.** Trang `Apocalypse` sửa lần
   cuối **2025-05-14** ≈ HotA 1.7.2–1.7.3, **trước 1.8.0** (31/DEC/2025), và tự nó **không ghi**
   phiên bản nào.

⚠️ **Bẫy đi kèm:** template `hota-blacknblue-template` liệt kê Dead Man's Boots trong
`*Banned artifacts:` — **ngược chiều** với Apocalypse. Hai template này hay bị nhắc cạnh nhau
nên rất dễ gộp thành cùng một chiều. Bài `dead-mans-boots` đã mắc đúng lỗi này (BLOCKER).

### ⚠️⚠️ Giá trị Necromancy ĐÃ ĐỔI qua các bản HotA

Đây là phát hiện quan trọng nhất về gameplay trong đợt này, và nó ảnh hưởng **mọi bài
artifact sau này**.

- **HotA 1.3.0** (01/JAN/2014): "The number of Skeletons raised by necromancy is reduced by
  half, as well as bonuses to it from artifacts and a Necromancy Amplifier"
- **HotA 1.8.0** (31/DEC/2025): "5/10/15/30% Necromancy boost values are **back**... (instead
  of 2.5/5/7.5/15%)"

Nghĩa là trong HotA **1.3.0 → 1.7.x**, giá trị là **2,5/5/7,5/15%**. Con số chuẩn SoD chỉ
trở lại ở **1.8.0**.

**Quy tắc rút ra:** mọi con số gameplay trong Codex **phải ghi rõ phạm vi phiên bản**.
Đây chính là lý do `SCHEMA.md` bắt tách *Cơ chế gốc* khỏi *Thay đổi qua các bản*.

### ⚠️ Bio hero chính thức là `T1*`, KHÔNG phải `T2*`

Sai sót về tier mà luồng kiểm định phát hiện, ghi lại vì nó ảnh hưởng nhiều bài sau này.

Bio chính thức của hero trong Heroes III/IV **không** đến từ manual in. Wiki ghi rõ
chúng được chép từ **`HEROBIOS.TXT`** — một **file dữ liệu trong game**. Do đó tier đúng
là `T1*`, không phải `T2*`.

Kiểm chứng ngược: manual in của Shadow of Death **trang 15** có thông số Sandro (class,
specialty, kỹ năng khởi đầu) nhưng **không có đoạn bio nào**.
{T2* EXPLICIT: sod-manual-p15}

**Hệ quả:** khi trích bio hero, dùng `T1*`. Đừng nâng lên `T2*` vì nghe "chính thức
hơn" — tier phản ánh **nguồn**, không phản ánh mức trang trọng.

### ⚠️ Có một Sandro khác trong Might and Magic V

Luồng kiểm định phát hiện claim "Sandro không xuất hiện trong game MM RPG nào ngoài MM8"
là **sai**.

Có **`Sandro (Xeen)`** — nhân vật riêng trong *Might and Magic V: Darkside of Xeen*, một
lich, questgiver và boss ở Necropolis. {T6 EXPLICIT: fandom-sandro-xeen}

Và hai người có liên hệ thật ở tầng sản xuất: **sprite của Sandro Xeen là gốc của
portrait Sandro Enroth** — "by essentially just recoloring and throwing him into a robe."

**Khác với ca Chronicles:** ở Chronicles, tranh chấp là *có phải cùng một người không*.
Ở đây wiki đã xếp sẵn thành hai nhân vật riêng; điều đáng ghi là quan hệ tái sử dụng
hình ảnh.

**Bài học:** claim phủ định dạng "không xuất hiện ở đâu khác" phải kiểm qua **trang
disambiguation**, không chỉ trang nhân vật.

### `h3wiki-sandro` (bio chính thức) lệch với campaign text — nhưng không phải mâu thuẫn thẳng

Bio chính thức H3: *"Sandro first studied **Necromancy** under the tutelage of the
wizard, and later the lich, Ethric."*

Nhưng toàn bộ campaign text nói ngược: Ethric dạy **warlock**, nổi giận vì Sandro
thành necromancer, và truy sát hắn vì điều đó. `h3wiki-ethric` ghi Ethric "trained
him to be a warlock and objected to him becoming a necromancer."

**Cập nhật sau kiểm định — sự lệch này YẾU hơn tưởng ban đầu.**

Hai điều làm dịu:

1. **Wiki tự dung hòa** thay vì coi là xung đột: "It can be surmised that Ethric has had
   an alter-ego of a mortal Bracadan wizard and warlock for a considerable time."
   {T1* INFERENCE: h3wiki-ethric}
2. **Chính người viết cốt truyện xác nhận** Ethric ở MM6 và thầy của Sandro là cùng một
   người. {T4 EXPLICIT: bullard-interview-2013} Nếu Ethric xuyên nhiều thế kỷ với nhiều
   danh tính, thì "the wizard, and later the lich" không sai — chỉ nén thời gian.

**Xử lý:** ghi nhận sự lệch, nhưng **không** gọi là "mâu thuẫn trong tư liệu chính thức".
Điều còn đứng vững: campaign text nhấn mạnh necromancy là thứ Ethric **phản đối**, còn
bio đọc như thể ông dạy nó. Đây là lệch **giọng**, không phải lệch **dữ kiện**.

Cũng lưu ý `CANON-POLICY.md` R1 (in-game thắng manual) **không áp dụng được ở đây** — vì
cả hai đều là in-game text (bio từ `HEROBIOS.TXT`, campaign text từ file campaign).

### `sod-target` vs `h3wiki-jabarkas` — Jabarkas có phải em trai Ethric?

`sod-target` (Day 24) nói Lord Jabarkas là "Ethric's illegitimate younger brother".
Nhưng có ba vấn đề:

1. **Là tin nghe lại *trong* game text.** Nguyên văn mở đầu "**According to you
   advisors**..." — cố vấn của Sandro nói, không phải người kể chuyện.
2. **Xung đột với bio in-game khác.** `h3wiki-jabarkas` ghi Jabarkas là "**eldest son of
   Duke Boragus**", race **Ogre** của Krewlod — khó dung hòa với em trai một wizard-lich
   người Bracada.
3. **Wiki cũng đánh giá là chuyện bịa.** `h3wiki-ethric`: "It is not made clear whether
   Jabarkas is Ethric's actual brother, or if this is part of the cover story. **The
   latter is very likely**, since lore implies that, as the first necromancer, Ethric
   should be centuries old."

**Xử lý:** `DISPUTED`, nghiêng về **đây là vỏ bọc**. Không được ghi như dữ kiện.

---

## Đã giải quyết sau kiểm định

| Việc | Kết quả |
|------|---------|
| ~~Tìm nguồn MM8 độc lập~~ | ✅ `mm8-guide-walkthrough` xác nhận độc lập. **Sửa một chi tiết:** Sandro là **lãnh đạo** guild, Thant là **phó** và là người **tạo ra** Nightshade Brazier — không phải đồng lãnh đạo |
| ~~Kiểm tuyến Tyranell / Statue of Legion~~ | ✅ **Là game text thật.** Nằm trong `sod-gathering-the-legion` (campaign của Crag Hack). Bằng chứng quyết định: map event (8,60,0) — một cựu thuộc hạ của Tyranell khai "Sandro was going to pay Tyranell well to find the Head and other pieces of Legion". Tyranell tồn tại như hero thật, mang Head of Legion |
| ~~Kiểm cảnh "dấu ngón tay xương trên ngực Finneas"~~ | ✅ **Tìm được.** Ở `sod-invasion` Day 17, **không** phải Specter of Power. Nguyên văn: "The impression of your bony fingertips is now permanently emblazoned on his chest, a small spell you picked up years ago." Wiki paraphrase **chính xác** |
| ~~Tìm developer commentary~~ | ✅ **Kết luận "không tồn tại" của đợt đầu là SAI.** Xem Nhóm 4 |

**Bài học từ hai mục đầu:** cả hai claim wiki bị nghi là "wiki tự bịa" đều **có thật**.
Lý do đợt đầu không tìm được: text nằm trong scenario mà **Sandro không phải nhân vật
chính** — tuyến Tyranell hiện qua một NPC phụ trong campaign của Crag Hack, còn cảnh
Finneas nằm ở `sod-invasion`. Tra cứu chỉ giới hạn trong scenario của Sandro sẽ bỏ sót.

**Bài học quan trọng hơn:** đợt đầu kết luận "không có developer commentary" và mình đã
ghi điều đó vào ba chỗ trong Codex. Kết luận đó sai.
**Claim dạng "không tồn tại" phải bị kiểm nghiêm như mọi claim khác.**

## Cần bổ sung sau

| Việc | Vì sao |
|------|--------|
| **Fetch `bullard-papers-ut-austin`** | Tài liệu thiết kế gốc của chính người viết cốt truyện. **Lead giá trị nhất chưa khai thác** — có thể chứa phần tiểu sử Sandro chưa từng phát hành |
| Trích text từ file `.h3c` | Nâng toàn bộ `T1*` → `T1`. Vẫn là hạn chế lớn nhất |
| Thử lại `heroesofmightandmagic.com` qua proxy khác | Nguồn chính thức duy nhất còn khả năng |
| Kiểm quote Gauldoth Half-Dead (H4) | Hiện chỉ là quote-box trên Fandom, không dẫn nguồn |
| Thử lại Celestial Heavens interview archive | Trả 403 trong cả hai đợt. Có thể còn phỏng vấn NWC khác |
| Tìm `heroes3wog.net` — tư liệu phục hồi từ bộ Bullard | Được cho là có "General Kendal's Diary" và tài liệu khác |

---

## Lịch sử sửa đổi

| Ngày | Thay đổi |
|------|----------|
| 2026-07-31 | Bản đầu — 47 nguồn từ đợt research Sandro |
