---
id: ethric
type: character
name_vi: Ethric
name_en: Ethric
aliases:
  - Ethric the Mad
  - Ethric of Bracada
appears_in:
  - mm6
  - mm7
  - sod-rise-of-the-necromancer
  - sod-new-beginning
  - sod-unholy-alliance
  - sod-specter-of-power
status: verified
verify_pass: 2026-08-02
race: lich
sources_used:
  - h3wiki-ethric
  - h3wiki-ajit
  - h3wiki-jaegar
  - h3wiki-jabarkas
  - h3wiki-sandro
  - h3wiki-jeddite
  - sod-target
  - sod-master
  - sod-driving-for-the-boots
  - sod-poison-fit-for-a-king
  - sod-finneas-vilmar
  - mm6-ethrics-tomb
  - mm6-cartman-quest
  - mm6-shadow-dagger
  - mm7-ethrics-staff
  - fandom-ritual-endless-night
  - fandom-timeline-ancient
  - fandom-sandro-enroth
  - sod-after-the-amulet
  - sod-agents-of-vengeance
  - oe-ethric-bio
  - bullard-interview-2013
relations:
  # Quan hệ với Sandro (student_of, killed) khai ở codex/heroes/sandro.md.
  # Nghịch đảo do công cụ sinh — xem SCHEMA.md mục 3.
  - type: teacher_of
    target: jeddite
    certainty: EXPLICIT
    source: sod-target
  - type: enemy_of
    target: sandro
    certainty: EXPLICIT
    source: sod-target
  - type: practices
    target: necromancy
    certainty: EXPLICIT
    source: h3wiki-ethric
  - type: member_of_race
    target: lich
    certainty: EXPLICIT
    source: h3wiki-ethric
open_questions: 5
---

# Ethric

## Tóm lược

Được gọi là **Ethric the Mad** — theo nhiều nguồn là **lich đầu tiên của thế giới**. Ông
là thầy của cả [[sandro]] lẫn [[jeddite]], và là kẻ truy đuổi Sandro xuyên suốt
*Rise of the Necromancer*.

Nhưng điều đáng nói nhất về Ethric là điều không wiki nào ghi:

> **Trong toàn bộ Heroes III, Ethric không nói một câu nào.**

Mọi thứ người đọc biết về ông đều đến từ **miệng kẻ thù** — Sandro, cố vấn của Sandro,
hoặc những người đang chống Sandro. Nhân vật này không có tiếng nói của riêng mình.

Đây không phải chi tiết vụn. Nó có nghĩa là chân dung Ethric mà ta có **là chân dung do
một kẻ ghét ông vẽ nên.**

---

## Tiểu sử

### "Lich đầu tiên" — cần phân biệt hai claim

Đây là chỗ các nguồn hay bị gộp làm một, nhưng chúng **không cùng độ chắc**.

**Claim mạnh — "lich đầu tiên":** mô tả item MM7 khẳng định **thẳng, không rào**:

> "Much more a tool than a weapon, Ethric's Staff was fashioned by **the world's first
> Lich - Ethric the Mad**."

{T1* EXPLICIT: mm7-ethrics-staff}

**Claim yếu hơn — "lich đầu tiên VÀ necromancer đầu tiên":** phiên bản gộp này được chính
game đóng khung là **tin đồn**:

> "**According to rumor**, Ethric was the first sorcerer to discover the ritual, becoming
> the world's first lich and the first necromancer at the same time."

{T6 INFERENCE: fandom-ritual-endless-night}

Và câu tin đồn trong dungeon MM6 cũng tự rào:

> "Ethric, the first Sorcerer seeking life after death, still walks about his tomb, the
> leader of a host of undead servants. **At least, that's how the rumor goes...**"

{T1* EXPLICIT: mm6-ethrics-tomb}

⚠️ Cả hai wiki lớn đều rào claim này ("described as", "supposedly") nhưng **không nêu lý
do thật** — rằng chính game gọi nó là tin đồn.

**Xử lý của dự án:** "lich đầu tiên" là claim có nguồn khẳng định. "Necromancer đầu tiên"
thì yếu hơn một bậc.

### Từ người thành lich

Quá trình biến đổi **không được kể ở đâu cả** trong Old Universe. Nhưng có một mảnh xác
nhận độc lập rằng ông **từng là người** — mô tả item MM6:

> "Commissioned by Ethric the Mad **while still a human**, it is said these daggers have a
> link to the Land of the Dead. They are used in certain magical rituals designed to extend
> life to unnatural lengths."

{T1* EXPLICIT: mm6-shadow-dagger}

Chi tiết "extend life to unnatural lengths" gợi ý ông đã tìm cách kéo dài sự sống **trước
khi** chọn lichdom. Nhưng game không nói thêm.

### Ethric ở Bracada — danh tính công khai

Game text cho thấy Ethric — một lich — **duy trì một danh tính người sống mà công chúng
chấp nhận**. Có hai đoạn độc lập.

Đoạn nêu đích danh **Bracada** nằm trong epilogue của Gem, và nàng nói ra khi vẫn chưa
hiểu mình bị lừa:

> "I will have to **write to Ethric in Bracada** and tell Lord Fayette about this
> immediately."

{T1* EXPLICIT: sod-driving-for-the-boots}

Đây là **nguồn duy nhất nêu tên Bracada**. Nhưng danh tính học giả công khai của ông còn
được xác lập độc lập ở một chỗ khác:

> "Sandro's master, Ethric, needs an Amulet of the Undertaker to perform anti-necromancy
> research, but **Ethric is an academician**..."

{T1* EXPLICIT: sod-after-the-amulet}

Chi tiết này đáng chú ý: một druid ở AvLee có thể viết thư cho ông, và người ta biết ông
là "một học giả". Lich đầu tiên của thế giới sống giữa người sống, công khai.

*(Cách hiểu này khớp với việc Sandro cũng dùng ảo ảnh để che thân xác lich khi giao tiếp
với Gem và Crag Hack. Nhưng game không nói Ethric dùng cùng thủ đoạn — xem
[Điểm tranh chấp](#tranh-chap-danh-tinh).)*

### Thầy của Sandro và Jeddite

Ethric dạy cả hai. Jeddite là người **giới thiệu** Sandro với ông:

> "We were students together under Ethric. By becoming Necromancer, you have completely
> shamed me, for it was I who introduced you to Ethric. I should have listened to him.
> **From the start, he doubted your ability to wisely endure the burden of magical
> knowledge.**"

{T1* EXPLICIT: sod-target — thư Jeddite, Day 2}

Câu cuối đáng chú ý: Ethric **nghi ngờ Sandro ngay từ đầu**. Ông không bị học trò lừa —
ông đã cảnh giác từ trước, và đã đúng.

### Ông dạy Sandro cái gì? — hai nguồn nói ngược nhau

Xem [Điểm tranh chấp](#tranh-chap-day-gi) — đây là mâu thuẫn thật
giữa hai nguồn in-game.

### Cuộc truy đuổi

Khi biết Sandro thành necromancer, Ethric **nổi giận**:

> "Ethric, your old master, **became furious** when he received word you became a
> Necromancer."

{T1* EXPLICIT: sod-target — Day 1}

Sandro mô tả động cơ của thầy theo cách riêng — và đầy khinh bỉ:

> "He hasn't been too happy about me becoming a Necromancer and **wants to remove the
> blight from his career**."

{T1* EXPLICIT: sod-target — prologue}

Phương pháp của Ethric không phải đánh trực diện. Ông **tung tin**:

> "Ethric is a sly old Warlock. He has spread word of Sandro and the artifacts he carries to
> the lords of this region. Some of the lords want these artifacts for their own use; others
> want to destroy them."

{T1* EXPLICIT: sod-target — region text}

Ông cũng cảnh báo Gem — người đang bị Sandro lợi dụng — về việc Sandro đang ghép artifact.
{T1* EXPLICIT: sod-agents-of-vengeance}

Nhưng liên minh ông dựng lên **không đồng lòng**, và chính Sandro nhận ra điều đó:

> "You... wonder what Ethric was thinking when he enlisted these people in his cause."

{T1* EXPLICIT: sod-target — Day 18}

Một nửa muốn trả artifact cho Ethric; nửa kia muốn giữ. Sandro khai thác đúng khe hở này.

### Kết cục — hoặc hai kết cục

Xem [Điểm tranh chấp](#tranh-chap-hai-cai-chet).

Sau khi bị Sandro đánh bại trong *Master*, **campaign đơn giản là không nhắc tới ông nữa.**
{T1* EXPLICIT: sod-finneas-vilmar — scenario kế tiếp, Ethric hoàn toàn vắng mặt}

Trong MM6, nhóm nhân vật chính giết một Ethric ở **Tomb of Ethric the Mad** phía tây
Free Haven, khoảng đầu năm 1165 AS. Hộp sọ của ông được mang về cho **Gabriel Cartman**,
một nhà luyện kim ở Free Haven — người hy vọng nghiên cứu nó sẽ tìm ra cách **đảo ngược**
quá trình biến thành lich. {T1* EXPLICIT: mm6-cartman-quest}

Chi tiết đó có sức nặng riêng: hộp sọ của **lich đầu tiên** trở thành vật thí nghiệm cho
người muốn **chấm dứt** thứ ông tạo ra.

---

## Quan hệ

**[[sandro]]** — học trò, rồi kẻ thù, rồi kẻ đánh bại ông. Trục quan hệ định hình cả hai
nhân vật. Ethric nghi ngờ Sandro từ đầu {T1* EXPLICIT: sod-target}, nổi giận khi hắn thành
necromancer, và dành phần cuối đời truy đuổi hắn.

**[[jeddite]]** — học trò, và là người giới thiệu Sandro với ông. Trong *Target*, Jeddite
chiến đấu để **giành artifact về cho Ethric**. {T1* EXPLICIT: sod-target}

**[[jabarkas]]** — theo một dòng game text thì là **em trai ngoài giá thú** của Ethric.
Nhưng claim này có vấn đề nghiêm trọng — xem
[Điểm tranh chấp](#tranh-chap-jabarkas).

**[[gem]]** — Ethric cảnh báo nàng về Sandro. Trớ trêu: Sandro đã dùng **chính tên Ethric**
làm vỏ bọc để lừa nàng thu thập artifact.
{T1* EXPLICIT: sod-after-the-amulet} Xem [[cloak-of-the-undead-king]].

**[[gabriel-cartman]]** — nhà luyện kim ở Free Haven, người nhận hộp sọ Ethric để nghiên
cứu cách đảo ngược lichdom. {T1* EXPLICIT: mm6-cartman-quest}

---

## Vì sao không phải hero chơi được

Ethric là `character`, không phải `hero`, theo tiêu chí ở `SCHEMA.md`: **không điều khiển
được ở bất kỳ game nào thuộc Old Universe.**

Trong Heroes III ông chỉ xuất hiện **một lần**, làm hero **địch** trong scenario *Master*.
{T1* EXPLICIT: sod-master} Trong MM6 ông là **quái boss**. Trong MM7 ông chỉ được nhắc qua
mô tả một item.

*(Ông có là hero chơi được trong Heroes: Olden Era — nhưng đó là sản phẩm ngoài Old
Universe, xem mục dưới.)*

---

## Xuất hiện trong game

**Đã kiểm trang disambiguation trên cả hai wiki** — không có trang nào, và full-text search
xác nhận **chỉ có đúng một nhân vật tên Ethric** trong toàn bộ Might and Magic. Không có
bản Ashan, không có người trùng tên. {T6 EXPLICIT: fandom-ritual-endless-night}

*(Đây là kiểm chứng chủ động, không phải giả định — theo bài học từ ca `Sandro (Xeen)`.)*

| Game | Vai trò |
|---|---|
| **MM6** | Quái boss độc nhất, tại Tomb of Ethric the Mad |
| **MM7** | **Chỉ được nhắc** — qua mô tả item Ethric's Staff |
| **H3: Shadow of Death** | Hero **địch** trong *Master*; được nhắc ở 7 scenario khác |
| *Olden Era* | Hero chơi được — **ngoài Old Universe**, xem dưới |

### Chi tiết Heroes III

| Campaign | Scenario | Vai trò |
|---|---|---|
| *Rise of the Necromancer* | Target | Được nhắc (prologue, Day 1/2/18/24, event 40,46,0) |
| *Rise of the Necromancer* | **Master** | **Hero địch** — orange, town Dungeon |
| *New Beginning* | After the Amulet, Retrieving the Cowl, Driving for the Boots | Được nhắc |
| *Unholy Alliance* | Agents of Vengeance, Wrath of Sandro | Được nhắc |
| *Specter of Power* | Poison Fit for a King | Được nhắc |

{T1* EXPLICIT: h3wiki-ethric}

### Heroes: Olden Era — ngoài Old Universe

⚠️ Theo `CANON-POLICY.md` R5, *Heroes of Might and Magic: Olden Era* là sản phẩm hiện đại
và **không có quyền gì với canon Old Universe**. Ghi lại đây **chỉ để tham chiếu**, vì nó
là tiểu sử duy nhất kể nguồn gốc Ethric:

> "Once a brilliant but reclusive wizard of Bracada, Ethric delved too deeply into death
> magic - secrets no mortal was meant to wield. In his attempt to conceal his findings, he
> became the target of betrayal that nearly cost him his life. Ethric embraced undeath to
> survive and became a lich. Yet he still clings to the pretence of life, walking among
> mortals with cryptic purpose."

{T5 EXPLICIT: oe-ethric-bio — **ngoài Old Universe**, sản phẩm chưa phát hành, có thể đổi}

Đoạn này khớp đáng ngạc nhiên với dòng "Ethric in Bracada" của Gem. Nhưng **không được
dùng nó để lấp lỗ hổng Old Universe** — nó là cách một nhóm phát triển khác, nhiều năm sau,
diễn giải nhân vật.

---

## Gameplay

### Heroes III

| Thuộc tính | Giá trị |
|---|---|
| Town | Dungeon |
| Class | **Warlock** |
| Race | **Lich** |
| Specialty | **Mysticism** (+5%/level) |
| Level | 6 |
| Chỉ số | 4 Attack / 3 Defense / 2 Power / 2 Knowledge |
| Spell khởi đầu | Blind |
| Movement | 1560 |

{T1* EXPLICIT: h3wiki-ethric}

**Tám kỹ năng ở mức Expert** — bất thường với một hero địch cấp 6: Wisdom, Eagle Eye,
Scholar, Tactics, Learning, Offense, Intelligence, Sorcery.

Quân khởi đầu: Troglodyte 30–40 (100%), Harpy 4–6 (88%), Beholder 3–4 (25%).

### Portrait — hai tầng, đáng ghi

Ethric **mượn portrait của hero Ajit**. {T1* EXPLICIT: h3wiki-ethric — trường
`picture = Ajit`; và `sod-master` hero row ghi `image=Ajit`}

Nhưng **Ajit không phải template nền**. Hero Ethric thực chất dựa trên **Jaegar**:

- Ajit specialty = **Beholders** {T1* EXPLICIT: h3wiki-ajit}
- Jaegar specialty = **Mysticism**, "Receives a 5% per level bonus to Mysticism skill" —
  **khớp chuỗi chính xác** với Ethric, và Jaegar cũng khởi đầu với Basic Mysticism
  {T1* EXPLICIT: h3wiki-jaegar}

→ **Portrait của Ajit, chỉ số của Jaegar.** Đây là kiểu tái sử dụng tài nguyên phổ biến
trong campaign Heroes III, và là lý do người chơi hay nhầm Ethric với Ajit.

### Might and Magic VI

Lich cấp 40, 280 HP, AC 25, gây 5D8+20 sát thương năng lượng tầm xa, cho 2000 XP khi bị
giết. Kháng 20 với lửa/điện/lạnh/độc/vật lý, kháng 10 với phép.
{T6 EXPLICIT: mm6-cartman-quest}

Trong game ông hiển thị bằng sprite **Power lich**.
{T6 EXPLICIT: mm6-cartman-quest — walkthrough: "Kill Ethric (he will look like a Power
lich)"}

---

## Điểm tranh chấp canon

### 1. Ethric dạy Sandro Necromancy hay Warlock? { #tranh-chap-day-gi }

**Hai nguồn in-game nói ngược nhau.**

**Bio chính thức của Sandro** (từ `HEROBIOS.TXT`, file dữ liệu in-game):

> "Sandro first studied **Necromancy** under the tutelage of the wizard, and later the lich,
> Ethric."

{T1* EXPLICIT: h3wiki-sandro}

**Campaign text nói ngược hoàn toàn:**

- Ethric "**became furious** when he received word you became a Necromancer"
  {T1* EXPLICIT: sod-target — Day 1}
- Sandro: ông "hasn't been too happy about me becoming a Necromancer"
  {T1* EXPLICIT: sod-target}
- Jeddite: Ethric "**doubted your ability** to wisely endure the burden of magical
  knowledge" ngay từ đầu {T1* EXPLICIT: sod-target}
- Trong *Master*, Ethric xuất hiện với class **Warlock** {T1* EXPLICIT: sod-master}

**Cách wiki xử lý — và một điểm bất nhất đáng nêu.**

Wiki khẳng định Ethric "trained him to be a warlock and objected to him becoming a
necromancer" — tổng hợp này **hợp với campaign nhưng mâu thuẫn thẳng với bio chính thức**,
và wiki trình bày mà không ghi nhận xung đột.

Nhưng ở mục trivia, wiki lại **dùng chính bio đó làm bằng chứng** cho một giả thuyết khác
(rằng Ethric của H3 chính là Ethric the Mad của MM6): "The fact that Sandro's bio remains
unchanged all throughout Shadow of Death... stating that he was a pupil of the lich Ethric,
corroborates the above hints." {T6 INFERENCE: h3wiki-ethric}

→ Wiki coi bio là **có thẩm quyền khi nó ủng hộ**, nhưng **gạt đi khi nó mâu thuẫn**. Đây
là phương pháp bất nhất, và đáng ghi lại.

**Xử lý của dự án:** `DISPUTED`. Campaign text nhiều và nhất quán hơn; nhưng cả hai đều là
in-game text nên `CANON-POLICY.md` R1 (in-game thắng manual) **không áp dụng được**.

Cách dung hòa khả dĩ: Ethric có nhiều class qua nhiều thời kỳ (wiki liệt kê **năm** tham
chiếu khác nhau: Wizard, Warlock, Lich). Bio có thể đang nén một quãng dài thành một câu.

### 2. Ethric chết hai lần — mâu thuẫn không có lời giải { #tranh-chap-hai-cai-chet }

Đây là tranh chấp lớn nhất về nhân vật này, và **hai wiki giải quyết theo hai hướng ngược
nhau.**

**Cái chết A — trong *Master* (Heroes III):** Sandro đánh bại ông.

Nhưng đây là **phát hiện phủ định quan trọng**: việc Ethric bị đánh bại **chỉ tồn tại
dưới dạng điều kiện thắng.** Không có đoạn kể nào mô tả cái chết — không epilogue, không
xác, không gì.

> "Defeat Ethric and all of his allies to win the scenario."

{T1* EXPLICIT: sod-master}

Và scenario **kế tiếp** không nhắc ông một lần nào. Campaign đơn giản là bỏ rơi nhân vật.
{T1* EXPLICIT: sod-finneas-vilmar}

**Cái chết B — trong MM6:** nhóm nhân vật chính giết ông tại Tomb of Ethric the Mad,
khoảng đầu 1165 AS, và lấy hộp sọ. {T1* EXPLICIT: mm6-cartman-quest}

**Vấn đề niên đại:** MM6 xảy ra **trước** *Rise of the Necromancer*. Nên nhóm MM6 giết
Ethric trước, rồi Sandro đánh bại ông sau.

**Ba cách xử lý, không cái nào có nguồn:**

| Nguồn | Cách xử lý |
|---|---|
| **Bullard (T4)** | Xác nhận **hai Ethric là một người** — nhưng **không nói gì** về hai cái chết. Giải quyết *danh tính*, không giải quyết *niên đại* {T4 EXPLICIT: bullard-interview-2013} |
| **Fandom** | Lấp bằng một câu không dẫn nguồn: "**Somehow surviving** his encounter in Enroth, Ethric returned to Antagarich in his human guise..." Chữ "Somehow" gánh toàn bộ lập luận {T6 FAN_THEORY: fandom-sandro-enroth} |
| **thelazy** | **Đảo ngược thứ tự.** Đặt sự kiện SoD trước, rồi "**Afterwards**, he became active on Enroth... slain by MM6 protagonists" → MM6 thành cái chết cuối {T6 FAN_THEORY: h3wiki-ethric} |

**Một chi tiết nghiêng cán cân:** timeline của **chính Fandom** đặt Shadow of Death vào
khoảng 1155–1164 AS và MM6 vào **1165 AS** — tức là **ủng hộ thứ tự của thelazy, chống lại
văn xuôi của chính Fandom.** {T6 INFERENCE: fandom-timeline-ancient}

**Xử lý của dự án:** `DISPUTED`, và **không chọn bên**. Hai wiki mâu thuẫn nhau, cả hai
không dẫn nguồn, và nguồn developer duy nhất không đề cập vấn đề. Nhưng nếu buộc phải
nghiêng, thứ tự của thelazy (MM6 là cái chết sau) được timeline chống lưng tốt hơn.

Cần nói thêm: claim của Fandom rằng Sandro "**eradicate** Ethric" và infobox
`status = Eradicated` là **suy ra từ điều kiện thắng**, không từ text kể nào.
{T6 FAN_THEORY: fandom-sandro-enroth}

### 3. Ethric duy trì danh tính người sống bằng cách nào? { #tranh-chap-danh-tinh }

Wiki đề xuất: "It can be surmised that Ethric has had an **alter-ego of a mortal Bracadan
wizard and warlock** for a considerable time, the general public apparently being unaware
that he is actually Ethric the Mad... In a similar fashion, Sandro is shown to be using an
illusion to disguise him being a lich."

{T6 INFERENCE: h3wiki-ethric}

**Chú ý wiki tự rào:** "It can be surmised", "apparently", "very likely". Đây là **suy luận
của biên tập viên wiki**, không phải lore có nguồn — và cả trang **không có một footnote
nào**.

Điều **có** nguồn: Gem định viết thư cho "Ethric in Bracada" như một người bình thường.
{T1* EXPLICIT: sod-driving-for-the-boots} Còn cơ chế cụ thể thì không.

### 4. Jabarkas có phải em trai Ethric? { #tranh-chap-jabarkas }

Game text (`sod-target` Day 24) nói Jabarkas là "Ethric's illegitimate younger brother".
Nhưng claim này có **bốn** vấn đề:

**Vấn đề 1 — là tin nghe lại *trong* game text.** Câu mở đầu bằng "**According to you
advisors**" (nguyên văn, kể cả lỗi "you" thay vì "your"). Cố vấn của Sandro nói, không
phải người kể chuyện. {T1* EXPLICIT: sod-target}

*(Câu này còn sai ngữ pháp trong chính game: "is Ethric's illegitimate younger brother
suffers from Little Man's Syndrome" — thiếu "and who". Dự án giữ nguyên khi trích.)*

**Vấn đề 2 — xung đột với bio in-game khác.** Bio chính thức của Jabarkas ghi ông là
"**eldest son of Duke Boragus**", race **Ogre**, xứ Krewlod — và **không nhắc Ethric một
chữ nào**. {T1* EXPLICIT: h3wiki-jabarkas} Khó dung hòa với việc là em trai một wizard
người Bracada đã sống hàng thế kỷ.

**Vấn đề 3 — chính wiki cũng đánh giá là bịa.** "It is not made clear whether Jabarkas is
Ethric's actual brother, or if this is part of the cover story. **The latter is very
likely**." {T6 INFERENCE: h3wiki-ethric}

**Vấn đề 4 — game text tự phản bác động cơ.** Đây là mảnh mạnh nhất, và nó nằm trong một
map event dễ bỏ sót:

> "Sir, Lord Jabarkas knows you are in the area and is planning to kill you. **He has not
> forgotten you kidnapping his daughter and violating her.**"
>
> "**Did he make mention of the artifacts?**" you ask.
>
> "**No, sir.**"

{T1* EXPLICIT: sod-target — map event (15, 27, 0)}

Động cơ thật của Jabarkas là **thù riêng vì con gái** — không phải ghen tị với anh trai về
artifact. Chính game text tách hai động cơ ra, và Sandro hỏi thẳng câu xác nhận.

**Xử lý:** `DISPUTED`, nghiêng mạnh về **đây là vỏ bọc hoặc tin đồn sai**.

Cũng lưu ý: wiki ghi "**half**-brother", nhưng game chỉ nói "**brother**". Từ "half" là
wiki tự thêm. {T6 FAN_THEORY: h3wiki-ethric}

### 5. "Đội quân lich tấn công Sandro trong *Master*" — đọc sai

Wiki nêu ở mục trivia: "A force of liches attacks Sandro in Master, further hinting at
Ethric's true nature." {T6 FAN_THEORY: h3wiki-ethric}

**Game text không nói vậy.** Event (24, 10, 0):

> "An operating sawmill stands before you. Lots of Power Liches guard it. You never thought
> you'd fight against your own kind."

{T1* EXPLICIT: sod-master}

Chúng canh một **xưởng cưa**. Đây là quái trung lập canh tài nguyên — kiểu bố trí bình
thường trên bản đồ Heroes III, không phải quân của Ethric.

---

## Giả thuyết cộng đồng

### Ethric tạo ra hai combination artifact?

Wiki nêu, và tự đánh dấu là chưa xác nhận: "It is also possible, **though not confirmed**,
that the two artifacts, reassembled by Sandro, were originally created by Ethric."
{T6 FAN_THEORY: h3wiki-ethric}

Xem thêm [[cloak-of-the-undead-king]] — claim liên quan rằng hai artifact "từng thuộc về
Ethric" **bị game text phản bác**.

### "Somehow surviving" — cách Fandom nối hai cái chết

Xem *Điểm tranh chấp* mục 2. Đây là văn nối, không phải lore.
{T6 FAN_THEORY: fandom-sandro-enroth}

---

## Trivia & Dev Notes

### Phát ngôn của developer

Jennifer Bullard, Lead Designer và người viết cốt truyện *Shadow of Death*, được hỏi thẳng:

> **Hỏi:** "Ethric the Mad from Might and Magic VI - The Mandate of Heaven. Was he the same
> master of Sandro from Heroes of Might and Magic III - Shadow of Death storyline?"
>
> **Đáp:** "**Yes**, we always tried to tie the different products together so people who
> played everything could see a theme."

{T4 EXPLICIT: bullard-interview-2013}

⚠️ **Cần đọc đúng phạm vi của câu này.** Nó xác nhận **danh tính**, nhưng được đóng khung
như một **triết lý thiết kế chung**, không phải phán quyết chi tiết về continuity. Nó
**không** đề cập: hai cái chết, tuổi tác, Jabarkas, hay ông thuộc class nào.

Đây là **toàn bộ** phần nói về Ethric trong phỏng vấn — hai dòng. Tìm "Ethric", "lich",
"necroman" trong toàn văn không ra kết quả nào khác.

> **Các wiki dựa vào câu này nặng hơn hai mệnh đề của nó cho phép.**

### Ethric không có tiếng nói

Điều đáng chú ý nhất về nhân vật này, và không wiki nào ghi: **trong toàn bộ Heroes III,
Ethric không nói một câu nào.**

Ông chỉ được mô tả, được trích gián tiếp, hoặc được kể lại. Thư Jeddite diễn giải ý ông;
thuộc cấp của Ufretin nói đã nhận "Ethric's message" nhưng không trích nội dung.

Mọi mô tả về Ethric đều lọc qua ba lớp: **Sandro** (kẻ kể thù địch), **cố vấn của Sandro**,
hoặc **kẻ địch của Sandro**.

### Đoạn mô tả Ethric đầy đủ nhất — và nó là một cơn ác mộng

Nghịch lý: chân dung sống động nhất của Ethric trong Heroes III nằm trong **giấc mơ của kẻ
đã giết ông**.

> The nightmare began as usual. Ethric was chasing you, waving his sword like the lunatic he
> was... There is no doubt in your mind this **Warlock** would rip your head from your
> shoulders and use it to play kickball. **He was mad**, insane with jealousy and unable to
> control the power he already had.

{T1* EXPLICIT: sod-poison-fit-for-a-king — Day 69 "Nightmare"}

**Ba điều đáng ghi:**

1. "**He was mad**" — thì quá khứ, và đây là chỗ Heroes III tiến gần nhất tới việc gọi ông
   là "the Mad". Là cầu nối in-game mạnh nhất tới Ethric the Mad của MM6.
2. Cảnh này diễn ra **sau** *Master* — Ethric vẫn ám ảnh Sandro sau khi đã bị đánh bại. Và
   cơn ác mộng **lặp lại**: nó còn xuất hiện ở Day 71, "you know **his sword** is about to
   slice through you as though you were melted butter." {T1* EXPLICIT:
   sod-poison-fit-for-a-king — Day 71}
3. Nhưng Ethric ở đây vung **kiếm** — không hợp với một wizard/warlock. Và đây là **giấc mơ
   chủ quan** của một kẻ thù. Không nên đọc như mô tả khách quan.

---

## Câu hỏi mở

**Q1. Ethric thành lich khi nào và bằng cách nào?**
Không nguồn Old Universe nào kể. Chỉ có mô tả item MM6 xác nhận ông **từng là người**.
Tiểu sử Olden Era có kể, nhưng đó là **ngoài Old Universe**.

**Q2. Ethric bao nhiêu tuổi?**
Không nguồn nào có. "Hàng thế kỷ" là suy luận của wiki dựa trên việc ông là necromancer đầu
tiên. {T6 UNVERIFIED: h3wiki-ethric — **không dẫn nguồn**}

**Q3. Hai cái chết hòa giải thế nào?**
Không có lời giải canon. Xem *Điểm tranh chấp* mục 2.

**Q4. Mô tả item `Ethric's Skull` trong MM6 nói gì?**
Chưa lấy được — trang chỉ là redirect tới danh sách item.
{T1* UNVERIFIED: mm6-cartman-quest — **chưa xác minh**}

**Q5. Bốn scenario "được nhắc" có gì trong block Events?**
`After the Amulet`, `Retrieving the Cowl`, `Agents of Vengeance`, `Wrath of Sandro` chưa
được đọc đầy đủ trong đợt này — phần nhắc Ethric lấy từ danh sách của wiki.
{T1* UNVERIFIED: h3wiki-ethric — **chưa xác minh trực tiếp**}

### Hạn chế nền tảng

Toàn bộ text in-game mang tier **`T1*`** — bản chép fan wiki, không phải file game gốc.
Ngoài ra, bản gốc phỏng vấn Bullard trên acidcave.net **chưa fetch** — chỉ đọc bản chép
của thelazy.

---

## Nguồn

| Loại | Số lượng | Ghi chú |
|---|---|---|
| `T1*` — text in-game qua trung gian | 14 | heroes.thelazy.net + trang MM6/MM7 |
| **`T4`** — developer statement | 1 | Phỏng vấn Bullard — chỉ **hai dòng** về Ethric |
| `T5` — ngoài Old Universe | 1 | `oe-ethric-bio` — chỉ tham chiếu, không phải canon |
| `T6` — wiki cộng đồng | 3 | Chủ yếu dùng để **cảnh báo** về claim không nguồn |

Nguồn quan trọng nhất cho bài này: `sod-target` (map event 15,27,0 phá vỡ claim Jabarkas),
`mm7-ethrics-staff` (claim "lich đầu tiên" duy nhất không rào), và
`fandom-ritual-endless-night` (nêu rõ claim gộp là tin đồn).

---

## Liên kết

**Nhân vật:** [[sandro]] · [[jeddite]] · [[jabarkas]] · [[gem]] · [[vidomina]] ·
[[gabriel-cartman]]

**Vật phẩm:** [[cloak-of-the-undead-king]] · [[armor-of-the-damned]] · [[ethrics-staff]] ·
[[shadow-dagger]]

**Địa điểm:** [[bracada]] · [[tomb-of-ethric-the-mad]] · [[free-haven]] · [[deyja]]

**Phép thuật:** [[necromancy]] · [[ritual-of-endless-night]]

**Campaign:** [[sod-rise-of-the-necromancer]] · [[mm6]]

**Người sáng tạo:** [[jennifer-bullard]]
