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
| `ab-march-of-the-undead` | T1* | FETCHED | Armageddon's Blade — Sandro là địch, level 14 |
| `hc-truth-within-nightmares` | T1* | FETCHED | Heroes Chronicles *Conquest of the Underworld* — Tarnum vs Sandro. **Xem cảnh báo DISPUTED bên dưới** |

### Artifact

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `h3wiki-cloak-undead-king` | T1* | FETCHED | Cơ chế, thành phần, bảng hồi sinh, quy tắc cộng dồn. ⚠️ Câu về HotA 1.7.2 trên trang này **sai** — xem cảnh báo bên dưới |
| `h3wiki-armor-of-the-damned` | T1* | FETCHED | Cơ chế, thành phần, synergy với hero. Mô tả in-game: **4 spell**, không phải 5 |
| `h3wiki-amulet-of-the-undertaker` | T1* | FETCHED | Thành phần Cloak — Treasure, Necklace, 2000, +5% Necromancy |
| `h3wiki-vampires-cowl` | T1* | FETCHED | Thành phần Cloak — Minor, Cape, 4000, +10% Necromancy |
| `h3wiki-dead-mans-boots` | T1* | FETCHED | Thành phần Cloak — Major, Feet, 6000, +15% Necromancy |
| `h3wiki-angelic-alliance` | T1* | FETCHED | Artifact đối kháng — 84000, đắt nhất SoD, +21 cả bốn primary skill |
| `h3wiki-necromancy` | T1* | FETCHED | Giới hạn cơ chế Necromancy. Khác biệt SoD vs HotA về cách tính |
| `hota-changelog` | T1* | FETCHED | Changelog Horn of the Abyss, 201.529 byte. **Nguồn chuẩn** cho mọi claim về HotA — trang artifact không đáng tin bằng |
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
| `h3wiki-terek` | T1* | FETCHED | Barbarian/Battle Mage, tay sai đầu tiên Sandro thuê lấy Cowl; bị cướp bắt |
| `h3wiki-sandals-of-the-saint` | T1* | FETCHED | Cần để qua Quest Guard lấy Dead Man's Boots |
| `fandom-artifact-list` | T6 | FETCHED | `List of Heroes III artifacts` — **nguồn duy nhất** cho mô tả in-game của artifact. Fandom **không dẫn nguồn** |
| `h3wiki-herobios-txt` | **T1** | FETCHED | ⭐ `Translation Data/HeroBios.txt` — **file string table TRÍCH TỪ GAME** (168KB, cột EN/FR/PL/RU). Đây là `T1` **thật**, không phải `T1*` |

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

## Nhóm 4 — Developer statement (T4)

⚠️ **Đợt research đầu kết luận sai rằng "không có developer commentary nào".** Luồng
kiểm định độc lập tìm được nguồn T4 thật. Ghi lại sai sót này để nhớ: **kết luận
"không tồn tại" cần được kiểm chứng nghiêm khắc như mọi claim khác.**

| key | tier | access | Nội dung |
|-----|------|--------|----------|
| `bullard-interview-2013` | **T4** | FETCHED | **Phỏng vấn Jennifer Bullard**, do Alchemik thực hiện năm 2013 cho Acid Cave. `acidcave.net/jennifer_bullard_interview.html` — **còn sống, truy cập trực tiếp được, không cần archive.org**. Mirror/index tại `heroes.thelazy.net/index.php/Jennifer_Bullard` |
| `bullard-papers-ut-austin` | **T3** | NOT_FETCHED | **Tài liệu thiết kế gốc do chính Bullard tập hợp**, lưu tại Dolph Briscoe Center for American History, University of Texas. `repositories.lib.utexas.edu/items/e3abd6e5-b6be-4547-8900-17b2c9e237da` — mục lục ghi "Heroes [of Might and Magic] documents" |
| `fulton-fanstratics-13` | **T4** | FETCHED | **Greg Fulton, Lead Designer Heroes III** — Fanstratics Newsletter #13. Gọi Sandro là hero mang tính biểu tượng: "Astral, Crag Hack, Dracon, **Sandro**, Solmyr, Tazar..." |
| `fulton-fanstratics-27` | **T4** | FETCHED | Fulton, Newsletter #27 — ghi lại yêu cầu thiết kế ở buổi họp khởi động H3: "Keep specific heroes from HoMM2, like **Sandro the Necromancer**, Halon the Wizard, Lord Haart..." |
| `fulton-fanstratics-3` | **T4** | FETCHED | Fulton, Newsletter #3 — xác nhận **Bullard là Lead Designer của SoD**: "I was not involved in the conception or creation of SoD... Jennifer Bullard was the project's Lead Designer, and any questions you have about SoD would best be directed to her" |

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

**Việc cần làm:** kiểm xem thelazy còn trang `Translation Data/` nào khác —
`Talk:Artifact/descriptions` cũng được nêu là có thể chứa chuỗi trích từ game.

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
