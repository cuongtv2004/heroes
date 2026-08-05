---
id: gem
type: hero
name_vi: Gem
name_en: Gem
aliases:
  - Gem the Druid
  - Gem the Sorceress
# Class là ĐIỂM TRANH CHẤP THẬT: sách hướng dẫn in nói Druid, game nói Sorceress
# cho cùng một campaign. Frontmatter ghi Druid — class chuẩn ở H3 RoE/AB và H4, và
# cũng là trạng thái nàng tự chọn ở cuối tuyến truyện. Xem thân bài mục Gameplay.
class: Druid
class_certainty: DISPUTED
specialty: ""
faction: rampart
first_appearance: h1
playable_in:
  - game: h3
    campaigns: [sod-new-beginning, sod-unholy-alliance]   # New Beginning: 4 scenario, Gem chơi được cả bốn
appears_in:
  - h1
  - h2
  - roe
  - sod
  - h4
status: verified
verify_pass: verify-gem-2026-08-05
sources_used:
  - h3wiki-herobios-txt
  - h3wiki-gem
  - sod-after-the-amulet
  - sod-retrieving-the-cowl
  - sod-driving-for-the-boots
  - sod-agents-of-vengeance
  - sod-clearing-the-border
  - sod-secrets-revealed
  - sod-final-peace
  - sod-manual-p4
  - sod-manual-p14
  - roe-manual-p125
  - fulton-fanstratics-27
  - fandom-h4-hero-bios
  - fandom-gem-enroth
  - h3wiki-artraits-txt
  - fulton-names-2023
  - bullard-interview-2013
relations:
  - type: betrayed
    target: sandro
    certainty: EXPLICIT
    source: sod-driving-for-the-boots
    note: "Chiều khai là Sandro betrayed Gem; xem ghi chú dưới"
  - type: ally_of
    target: gelu
    certainty: EXPLICIT
    source: sod-agents-of-vengeance
    note: ""
open_questions: 5
---

# Gem

## Tóm lược

Nữ Sorceress người Enroth từng phụng sự **King Roland Ironfist**, sau sang Antagarich và trở
thành **Druid** của AvLee. Nàng là **entity được nhắc tới nhiều nhất** trong Codex trước khi có
bài này — 8 trên 14 bài trỏ tới nàng.

Nàng cũng là người mà [[sandro]] lừa. Và điều làm bi kịch đó sắc hơn hẳn không phải việc nàng bị
lừa, mà là **lý do nàng dễ bị lừa**: nàng nhận lời vì tin đó là nghiên cứu **chống** necromancy —
và nàng có lý do rất riêng để căm ghét necromancer.

⭐ Lý do đó **chưa từng có trong Codex**, và nó không nằm ở bio hay prologue. Nó nằm trong một
timed event ngày 1: **cả làng nàng bị đàn skeleton giết, nàng là người sống sót duy nhất.**

---

## Tiểu sử

### Xuất thân — hai mảnh, ở hai tier khác nhau

**Mảnh chính thức**, từ bảng string table hero mà thelazy đăng lại:

> "Gem was one of the greatest **Sorceresses** that Enroth had ever seen, **serving King Roland
> Ironfist during the Succession Wars**. Shortly after Roland had secured the throne of Enroth,
> **Gem left for Erathia, finding a new home in AvLee**."

{T1* EXPLICIT: h3wiki-herobios-txt — dòng 58, cột EN}

⚠️ Trên trang wiki, cùng câu này được gắn link `Enroth (nation)` và `Sorceress (class)`. **Text game
không phân biệt** "Enroth quốc gia" với "Enroth lục địa" — đó là wiki thêm vào. Bài này trích **chữ
hiển thị**.

🔴 **Về tier — một đính chính do chính bài này gây ra.** Registry từng xếp `h3wiki-herobios-txt` là
`T1` **thật** (không dấu sao), và bản đầu của bài này chép theo. **Sai.** Trang đó **không có một
câu khai xuất xứ nào**, không `<ref>`, và nằm trong `Category:Contributor resources` — khác hẳn
`h3wiki-artraits-txt`, vốn tự ghi `Information from H3Bitmap.lod > artraits.txt` và **vì thế** mới
đáng `T1`. Đã hạ xuống **`T1*`** ở đây và ở cả `archibald-ironfist`, `jeddite`.

**Mảnh thứ hai — và đây là động cơ của cả nhân vật.** Nó nằm trong timed event ngày 1 của
`Agents of Vengeance`, khi Gem nhìn thấy một con búp bê:

> "The doll got to me. It looked just like the one my sister had right before she died. I remember
> thinking she was the luckiest girl in the world to have a doll like that. **Then the horde of
> skeletons killed everyone in my village. I was the only survivor.** I'm GLAD the Council of Elders
> choose me as one of the pair to punish Deyja."

{T1* EXPLICIT: sod-agents-of-vengeance — timed event ngày 1}

*(`choose` và chữ `GLAD` viết hoa đều **có trong bản chép**. Wiki này CÓ đánh dấu lỗi game ở chỗ khác
(`<!-- in-game mistake -->`), nên nhiều khả năng đây là nguyên văn — nhưng chưa ai đối chiếu với file
`.h3c`, nên đó là **suy luận**, không phải điều xác minh được.)*

{T1* INFERENCE: sod-agents-of-vengeance — chưa đối chiếu file game}

⭐ **Đây là lần thứ năm `BH-1` cứu một bài trong dự án.** Đoạn định nghĩa nhân vật này không có
trong bio, không có trong prologue, không có trên bất kỳ bản tóm tắt nào của hai wiki.

Hai mảnh khác cùng mạch, cũng trong timed event:

> "It's just that they remind me of a past I'd rather forget. **I haven't seen moving trees since I
> was a little girl.**"

{T1* EXPLICIT: sod-after-the-amulet — ngày 11}

> "The only bodies they can't use are the small children because their bodies are too small.
> **I buried the children**…"

{T1* EXPLICIT: sod-clearing-the-border — ngày 29 và ngày 29 (cont), hai mục timed event riêng}

### ⭐ Vì sao nàng ở Antagarich — và vì sao specialty của nàng là First Aid

Đây là chi tiết hiếm: **specialty gameplay của một hero có lý do trong truyện**, và lý do đó nối
thẳng về vụ thảm sát ở trên.

> "**Eight months ago my mentor, Amanda, told me of a device invented in Antagarich that might end
> the nightmares that have plagued me.** This invention, which she called a **First Aid Tent**, is
> capable of healing all manner of wounds. **I traveled from Enroth across the ocean to Antagarich**
> and searched until I came to the town of Clovergreen, where I was able to purchase this wonder."

{T1* EXPLICIT: sod-clearing-the-border — ngày 1}

⭐ Nàng vượt đại dương **vì những cơn ác mộng** — và thứ nàng đi tìm là một dụng cụ **chữa lành**,
không phải vũ khí. Bio chính thức chỉ nói nàng *"left for Erathia"*; **lý do** thì nằm ở đây.

### Câu tự định nghĩa của nhân vật

> "**I don't think it's wrong to hate the Hateful or not forgive the Unforgivable. What I think is
> wrong is to let that hating and unforgiving turn a person into the thing they hate or won't
> forgive. I won't make that mistake again. I won't be like them.**"

{T1* EXPLICIT: sod-retrieving-the-cowl — ngày 30}

⭐ Đặt cạnh gốc gác của nàng, câu này là **toàn bộ nhân vật trong một đoạn**: nàng có mọi lý do để
thành thứ nàng đang chống, và nàng biết điều đó.

⚠️ *(Fandom chép câu này với `hateful`/`unforgivable` viết thường; bản game viết hoa `Hateful`/
`Unforgivable`. Bài dùng bản viết hoa.)*

### Bị Sandro lừa — và vỏ bọc được thiết kế vừa khít với nàng

Vỏ bọc Sandro dùng là **nghiên cứu chống necromancy**:

> "You have agreed to help a wizard's apprentice named Sandro. **Sandro's master, Ethric, needs an
> Amulet of the Undertaker to perform anti-necromancy research**, but Ethric is an academician and
> Sandro is too inexperienced to go after the Amulet himself."

{T1* EXPLICIT: sod-after-the-amulet — region text}

Cách Gem hiểu về hắn lúc đầu:

> "I have met a Wizard named Sandro who is **conducting research to combat necromancy**. […] **He
> seems to think me quite the mercenary.**"

{T1* EXPLICIT: sod-after-the-amulet — prologue}

⚠️ **Game tự lệch một chi tiết:** prologue gọi Sandro là *"a Wizard"*, còn region text và timed
event ngày 1 gọi hắn là *"a wizard's apprentice"*. Cả hai đều là text game.

{T1* DISPUTED: sod-after-the-amulet — hai đoạn cùng scenario gọi khác nhau}

### Nàng muốn góp tiền cho chính kẻ đang lừa mình

Đây là đoạn làm nhân vật này đau:

> "I wrote back to Sandro that Ethric's project was a worthwhile one […] I decided to look up Ethric
> upon the completion of my quests and **persuade him to let me donate money towards his research.
> I admire his values.**"

{T1* EXPLICIT: sod-after-the-amulet — ngày 21}

Và nàng **có** nhận tiền — nhưng lý do thì hoàn toàn khác điều Sandro tưởng:

> "People are strange about gold. If you don't let them give it to you, they don't know what to do
> and get upset. […] I could tell Sandro wouldn't have known how to deal with me if I hadn't taken my
> payment; **he was so certain he could buy my loyalty. The funny thing is I would have helped his
> anti-necromancy research for free.**"

{T1* EXPLICIT: sod-after-the-amulet — ngày 49}

⭐ Sandro tưởng mình **mua** được lòng trung thành. Nàng đã cho không nếu hắn hỏi thẳng.

### Lời cảnh báo bị bỏ qua — của Amanda, trong một giấc mơ

> "…She just looked at me with her wise, calm eyes and advised me to **be careful, very careful about
> what I was doing**, and it wouldn't be like the last time."

{T1* EXPLICIT: sod-retrieving-the-cowl — ngày 27}

*(Cụm cuối đọc như lỗi ngữ pháp của bản game; giữ nguyên văn.)*

### Phát hiện bị lừa — nhưng vẫn tin Ethric là người tốt

Epilogue của scenario cuối:

> "**Sandro has tricked me!** But to what purpose? Why would he run off with the Dead Man's Boots
> without paying me? […] None of this makes sense! **I will have to write to Ethric in Bracada** and
> tell Lord Fayette about this immediately."

{T1* EXPLICIT: sod-driving-for-the-boots — epilogue}

⭐ **Bi kịch kép:** nàng biết mình bị lừa, nhưng vẫn tin **Ethric** là một học giả có thật và tử tế —
và định viết thư cho ông ta. [[ethric]] là một lich cổ, và là **thầy** của Sandro.

Sự thật đến sau, qua một lá thư — cũng trong timed event:

> "I received a message from Ethric today. Ethric said **it had been decades Sandro was his
> apprentice**. He said **Sandro ran away and become a Necromancer!** […] Ethric said Sandro might be
> trying to construct a powerful artifact from all the artifacts I gathered for him. **I was so
> furious, I screamed.** None of my troops came near me for an hour."

{T1* EXPLICIT: sod-agents-of-vengeance — ngày 9}

*(`it had been decades Sandro was his apprentice` và `ran away and become a Necromancer` — hai lỗi ngữ
pháp có trong bản chép; cùng giới hạn như trên, chưa đối chiếu file game.)*

⭐ Đây cũng là **neo thời gian** mà `TIMELINE-SPINE.md` đang dùng cho khoảng cách "Sandro học việc →
Restoration Wars".

### Từ Sorceress thành Druid — một tuyến truyện trọn vẹn, giấu trong timed events

Cả tuyến này nằm trong timed events, không có ở prologue hay epilogue.

| Ngày | Nội dung |
|---|---|
| 12 | ⭐ *"**I am in my sixty-first year as a Sorceress.** Over time you learn to protect yourself and your troops from ill magic."* |
| 20 | Một druid già mời nàng: *"being a Sorceress didn't necessarily prevent me from also being a Druid"* |
| 31 | *"While there are differences in specifics, **the core philosophies are virtually identical**."* |
| 34 | Nàng do dự: *"I would feel so **disloyal** to her and my sister Sorceresses."* |
| 45 | Cơ chế: *"each Druid wrote their own oaths… submit my oaths to the **Druid High Council**"* |
| 48 | *"**A part of me will always be a Sorceress, but I have evolved into a Druid**, finally finding a new life for myself in Antagarich."* |
| 51 | *"my sister Sorcerers had approved my petition… she thought this would be the **'New Beginning'** she had hoped I would find"* |

{T1* EXPLICIT: sod-driving-for-the-boots — các timed event}

### ⚠️ Trình tự chính xác — và một đính chính về chính bài này

**Bản đầu của bài viết rằng việc chuyển thành Druid hoàn tất *trong* scenario cuối, và cáo buộc cả
hai wiki ghi sai trình tự. Cả hai điều đó đều SAI, và luồng kiểm định bắt được.**

Phải tách **ba** mốc, vì chúng không xảy ra cùng lúc:

| Mốc | Khi nào | Nguồn |
|---|---|---|
| **Quyết định** + soạn lời thề | ngày 37 → 45, **trong** scenario cuối | `sod-driving-for-the-boots` |
| **Tự nhận mình đã đổi** — *"I have evolved into a Druid"* | ngày 48 | như trên |
| **Tuyên thệ chính thức** | ❗ **HOÃN tới SAU khi xong nhiệm vụ** | như trên, ngày 52 |

Câu quyết định nằm ở ngày 52 — và nó nói ngược hẳn điều bài này viết ban đầu:

> "I also told him **I would like to finish this last quest for the Boots as a Sorcerer.** After
> that, **if the Druid High Council has approved my vows, I would swear them on the next full moon.**
> […] Soon I would be an AvLee hero and a Druid soon. **But first I had to get the Boots to Sandro.**"

{T1* EXPLICIT: sod-driving-for-the-boots — ngày 52}

*(`a Druid soon… soon` — lỗi lặp có trong bản game.)*

→ Nàng **cố ý hoàn thành nhiệm vụ với tư cách Sorceress**, và Druid High Council **chưa** phê duyệt
tính tới ngày 52.

🔴 **Và vì thế lời cáo buộc nhắm vào thelazy là oan.** Câu *"Once her quest for Sandro was complete,
she changed her allegiance to AvLee and became a Druid"* **khớp với text game**. Điều tương tự đúng
cho phần AvLee: Lord Fayette mời nàng làm General *"**as soon as my promise to Sandro was
fulfilled**"*.

{T1* EXPLICIT: sod-retrieving-the-cowl — ngày 50}

⚠️ **Ghi lại vì đây là loại lỗi tệ hơn lỗi thường:** bài không chỉ sai dữ kiện, mà còn **buộc tội một
nguồn là sai trong khi nguồn đó đúng**. Với một dự án lấy việc kiểm nguồn làm cốt lõi, đó là lỗi
phải nêu tên chứ không sửa lặng lẽ.

⭐ Còn điều **vẫn đứng**: tên campaign *New Beginning* nói về **chuyển hóa của Gem**, không phải về
âm mưu của Sandro. Game text dùng đúng cụm đó ở ngày 51.

{T1* INFERENCE: sod-driving-for-the-boots — ngày 51 dùng đúng cụm "New Beginning", nhưng không nguồn nào nói thẳng rằng tên campaign đặt theo đó}

### Liên minh bốn người

Mối nối đầu tiên, từ phía Crag Hack:

> "It seems you and Crag Hack are not the only ones fighting these necromancers. **A Ranger and a
> Druid, Gelu and Gem**, are also fending off the forces of undead, but they are working within the
> borders of AvLee."

{T1* EXPLICIT: sod-secrets-revealed — ngày 39}

Và từ phía Gem — đoạn này còn xác nhận nàng **quen Yog từ thời Enroth**:

> "It was from a blue Barbarian hero named Yog. **Hmm, I met him once in Enroth.** […] What?! **Crag
> collected artifacts for Sandro**, which DID combine into a powerful artifact! **Ethric was right!**"

{T1* EXPLICIT: sod-agents-of-vengeance — ngày 25}

---

## Quan hệ

**[[sandro]] — kẻ lừa nàng.** Quan hệ khai một chiều từ phía nàng là `betrayed`, nhưng **chiều đúng
về nghĩa là Sandro phản bội Gem**; bài [[sandro]] đã khai `betrayed → gem` từ trước, nên ở đây chỉ
là chiều đọc ngược của cùng một sự việc.

{T1* EXPLICIT: sod-driving-for-the-boots}

**[[gelu]] — đồng đội ở AvLee.** Hai người được Council of Elders cử thành **một cặp** để trừng phạt
Deyja: *"the Council of Elders choose me as **one of the pair** to punish Deyja"*.

{T1* EXPLICIT: sod-agents-of-vengeance}

**[[ethric]] — người nàng kính trọng mà chưa từng gặp.** Nàng tin ông là học giả chống necromancy, và
định góp tiền cho ông. Ông là lich, và là thầy Sandro.

{T1* EXPLICIT: sod-after-the-amulet + sod-agents-of-vengeance}

**[[yog]] và [[crag-hack]]** — quen Yog từ Enroth; hợp lực ở giai đoạn cuối.

{T1* EXPLICIT: sod-agents-of-vengeance}

---

## Xuất hiện trong game

⚠️ Bảng này phân biệt **chơi được** với **chỉ được nhắc** — hai thứ khác nhau, và các bản tóm tắt
hay gộp.

| Sản phẩm | Vai trò | Chơi được? |
|---|---|---|
| **Heroes I** | Có trong roster | ✅ (hero thuê được) |
| **Heroes II** | Có trong roster | ✅ |
| **Heroes III** RoE / AB | Hero Rampart tiêu chuẩn | ✅ |
| **Heroes III** SoD — *New Beginning* | **Nhân vật chính**, **4 scenario** (chơi được cả bốn) | ✅ |
| **Heroes III** SoD — *Unholy Alliance* | Một trong bốn hero chống Sandro | ✅ |
| **Heroes IV** | Hero Preserve thuê được, **có bio riêng** | ✅ |

{T1* EXPLICIT: sod-after-the-amulet + fandom-h4-hero-bios + roe-manual-p125}

⚠️ **Nàng KHÔNG xuất hiện trong campaign Heroes IV nào.** Kiểm bằng cách quét 200 backlink của trang
`Gem (Enroth)`: chỉ có `Druid (H4)`, `Preserve`, và template roster — **không** trang campaign nào.

{T1* EXPLICIT: fandom-gem-enroth — kết quả quét backlink, không phải suy từ im lặng}

### Heroes IV — nàng sống qua The Reckoning

> "Even though Gem was at the center of **over eighty years** of wars and conflicts, she remained
> young and beautiful **thanks to the waters of a special fountain**. With **the destruction of the
> old world**, she no longer has access to those magical waters and is **beginning to age normally
> again** — something she desperately wants to avoid."

{T1* EXPLICIT: fandom-h4-hero-bios}

⚠️ **Text game nói *"the destruction of the old world"*, KHÔNG nói "the Reckoning".** Chữ đó chỉ là
đích wikilink do người sửa wiki thêm — cùng cái bẫy đã ghi ở [[the-reckoning]].

⭐ Bio này giải quyết được vấn đề tuổi thọ: *"over eighty years"* cộng **một đài phun nước giữ trẻ**
là **cơ chế trong truyện** cho việc cùng một người có mặt từ Heroes I tới Heroes IV.

---

## Gameplay

### ⚠️ Class là điểm tranh chấp THẬT — hai nguồn chính thức nói khác nhau

| Bối cảnh | Class | Nguồn | Tier |
|---|---|---|---|
| Heroes III RoE / AB | **Druid** (Rampart) | `roe-manual-p125` + bio game | `T2*` + `T1` |
| SoD — *New Beginning* | **Sorceress (Campaign)** | game | `T1*` |
| SoD — *New Beginning* | **Druid** | **sách hướng dẫn in** | **`T2*`** |
| SoD — *Unholy Alliance* | **Druid** | game | `T1*` |
| Heroes IV | **Druid** (Preserve) | bio game | `T1*` |

{T2* DISPUTED: sod-manual-p14 + sod-after-the-amulet}

🔴 **Hai dòng giữa mâu thuẫn nhau, và CẢ HAI đều là nguồn chính thức** — sách in nói `Druid`, game
nói `Sorceress (Campaign)`, cho **cùng một campaign**. Đây **không** phải lỗi wiki.

⭐ **Và phạm vi của mâu thuẫn hẹp hơn "sách in vs game" rất nhiều** — đây là điều bản đầu của bài
nói chưa đủ chính xác. Nhãn `Sorceress` **chỉ tồn tại trong campaign *New Beginning***. Ở nơi khác,
**chính engine game** gán nàng là Druid — `Agents of Vengeance` ghi `hero row … |Gem|Druid` — và
**text game** cũng vậy: *"A Ranger and a Druid, Gelu and Gem"*.

{T1* EXPLICIT: sod-agents-of-vengeance + sod-secrets-revealed}

→ Nên phát biểu đúng là: **một bản ghi hero của MỘT campaign lệch với tất cả phần còn lại, kể cả
phần còn lại của chính game đó.**

⭐ Fandom bổ sung chi tiết chốt vấn đề: Gem là **hero duy nhất trong game có tên class riêng**
(`Sorceress (Campaign)` không phải class chuẩn của bất kỳ town nào).

{T6 EXPLICIT: fandom-gem-enroth}

Theo `CANON-POLICY.md` **R1** (*cùng game, in-game thắng manual*): trong *New Beginning* nàng là
**Sorceress**. Nhưng bài không chọn ngầm — cả hai được ghi.

⚠️ Wiki tự hòa giải bằng câu *"her class is listed as Sorceress though she is still technically a
Druid"* — đó là **suy diễn của người sửa wiki**, không dẫn nguồn, và không được dùng.

{T6 UNVERIFIED: h3wiki-gem — văn xuôi wiki không dẫn nguồn}

⭐ **Và điều mỉa mai là game có câu trả lời hay hơn cả hai wiki:** tuyến truyện ở *Driving for the
Boots* cho thấy nàng **đang trong quá trình chuyển đổi** ngay trong campaign đó — nên "vừa Sorceress
vừa Druid" **là trạng thái thật của nhân vật**, không phải lỗi dữ liệu.

{T1* INFERENCE: sod-driving-for-the-boots — suy từ việc tuyến chuyển đổi diễn ra trong chính campaign đang tranh chấp}

---

## Điểm tranh chấp canon

### 1. Class Sorceress vs Druid

Xem *Gameplay*. `DISPUTED`, hai nguồn chính thức.

### 2. Tính liên tục Heroes I → IV: có nguồn tới đâu?

**Có nguồn cho H2 → H3 → H4:** bio nói thẳng nàng phụng sự Roland *"during the Succession Wars"*
(tức Heroes II) rồi sang Erathia.

⭐⭐ **Và có phát ngôn developer gọi ĐÍCH DANH nàng** — bản đầu của bài cắt câu trích ngay trước chỗ
quan trọng nhất. Nguyên văn đầy đủ, từ danh sách yêu cầu **bắt buộc** chốt ở buổi họp khởi động
Heroes III:

> "Keep specific heroes from HoMM2, like Sandro the Necromancer, Halon the Wizard, Lord Haart,
> Crag Hack the Barbarian, **Gem the Druid**, Yog the Barbarian, and Alamar the Warlock."

{T4 EXPLICIT: fulton-fanstratics-27}

→ Đây **không** phải bằng chứng chung chung về "nhân vật kế thừa". Đây là **Lead Designer Heroes III
ghi lại rằng việc giữ Gem là một yêu cầu thành văn** — tức phát ngôn first-party, gọi thẳng tên nhân
vật này.

⚠️ Đáng chú ý: Fulton gọi nàng là **"Gem the Druid"** khi nói về **Heroes II** — trong khi ở H1/H2
nàng là **Sorceress**. Đây là dữ kiện cho mục tranh chấp class bên dưới, không phải lỗi.

⚠️ **Nhưng Heroes I thì chỉ có roster và chân dung.** Heroes I và Heroes II **không có bio hero**,
nên **không claim tự sự nào** về việc nàng *làm gì* ở hai game đó là dựng được.

{T6 UNVERIFIED: h3wiki-gem — H1/H2 không có text tiểu sử để đối chiếu}

---

## Giả thuyết cộng đồng

### Sprite Heroes II có phải cùng chân dung không?

Hai ghi chú của người sửa wiki gợi ý chân dung Gem ở Heroes II là nguồn của chân dung về sau. Không
nguồn nào xác nhận.

{T6 FAN_THEORY: h3wiki-gem}

⚠️ Và có một bẫy thật ở đây: hero **`Dryope`** của HotA **dùng lại chân dung của Gem** (cùng khoá
ảnh). Ai đối chiếu ảnh mà không đọc tên sẽ nhầm hai người.

{T6 EXPLICIT: h3wiki-gem}

### ⚠️ Một chỗ trang `Gem` của thelazy nói SAI, và game text phân xử được

Trang `Gem` viết nàng *"befriended Clancy and **recruited him**"*; trang `Clancy` của **cùng wiki**
viết ngược — *"**He offered to help** Gem"*.

Game text đứng về phía trang `Clancy`:

> "I told Clancy of my agreement… and **he surprised me by offering to help me with the quest.**"

{T1* EXPLICIT: sod-after-the-amulet — ngày 1}

→ Nên đây không phải "hai trang wiki bất đồng" mà là **trang `Gem` mâu thuẫn với game**.

---

## Trivia & Dev Notes

### Ba cái tên gần giống — kiểm trước khi trích

| Tên | Là gì |
|---|---|
| **`Gem (Ashan)`** | Hero **Heroes VII**, universe Ashan. ⚠️ Bio của nàng **trùng ba điểm** với bio Old Universe — sorceress chuyển thành druid, *"nearly eight decades"*, và *"how she can still look so young"* — nên **rất dễ trích nhầm**. *(Việc trùng này có **chủ ý** hay không thì không nguồn nào nói — đó là suy đoán.)* Theo `CANON-POLICY.md` R5, Ashan **không có quyền gì** với Old Universe. ⚠️ Class trong game của nàng là **Mystic**, không phải Druid |
| **`Dryope`** | Hero HotA **dùng lại chân dung Gem** |
| **`Dargem`** | Nhân vật khác hẳn, chỉ trùng chuỗi ký tự |

{T6 EXPLICIT: h3wiki-gem + fandom-gem-enroth}

### ⚠️ "Fulton không nói gì về Gem" — một phủ định SAI mà bài suýt viết ra

Tài liệu `Gregory Fulton/On Names in Heroes of Might and Magic III` (98.499 byte) **không có mục nào
về tên Gem** — đã enumerate đủ **92** tên hero trong đó và không có nàng.

**Nhưng viết "Fulton không bình luận gì về Gem" thì SAI HẲN** — xem *Điểm tranh chấp canon* mục 2:
ông ghi thẳng **"Gem the Druid"** trong danh sách yêu cầu bắt buộc của Heroes III.

🔴 **Vì sao vắng mặt — và đây là điều làm phủ định kia thành bẫy:** tài liệu đó liệt kê những cái tên
**Fulton tự đặt cho Heroes III**. Tên Gem có từ **Heroes I/II**, nên nàng không thuộc phạm vi tài
liệu. Sandro, Crag Hack, Yog, Gelu, Clancy cũng vắng mặt vì **cùng lý do**.

{T4 EXPLICIT: fulton-fanstratics-27 + fulton-names-2023}

⚠️ Đây đúng là **`BH-3` suýt tái diễn**: kết luận "không có developer commentary" trong khi commentary
**có thật và gọi đích danh**, chỉ nằm ở tài liệu khác. Sai lầm nặng nhất trong lịch sử dự án đúng là
kiểu này.

*(Quét toàn bộ **45** Fanstratics newsletter: chữ "Gem" xuất hiện **đúng một lần**, và đó là dòng yêu
cầu thiết kế trên.)*

Phỏng vấn Bullard thì thật sự không nhắc Gem — grep toàn văn, 0 hit.

{T4 UNVERIFIED: bullard-interview-2013 — đã grep toàn văn, không tìm thấy}

---

## Câu hỏi mở

**Q1. "Sixty-first year as a Sorceress" tính từ mốc nào?**
Không nguồn nào nói nàng bắt đầu làm Sorceress năm bao nhiêu tuổi, nên con số 61 **không** quy ra
được tuổi.
{T1* UNVERIFIED: sod-driving-for-the-boots — không xác minh được điểm bắt đầu}

**Q2. Đài phun nước giữ trẻ ở đâu, và ai cho nàng dùng?**
Bio Heroes IV nhắc *"a special fountain"* nhưng **không định vị**, và không nguồn nào khác nhắc tới.
{T1* UNVERIFIED: fandom-h4-hero-bios — nguồn không nói thêm}

**Q3. Nàng có gặp Ethric bao giờ không?**
Nàng nhận **thư** của Ethric và định tới thăm, nhưng không text nào cho thấy hai người gặp nhau.
{T1* UNVERIFIED: sod-agents-of-vengeance — không có text về cuộc gặp}

**Q4. Làng nàng ở đâu, và bị tấn công khi nào?**
Text chỉ nói *"my village"* và *"when I was a little girl"*. Không địa danh, không mốc.
{T1* UNVERIFIED: sod-agents-of-vengeance — không dẫn nguồn địa danh}

**Q5. Vai trò của nàng ở Heroes I và Heroes II là gì?**
Chỉ có roster và chân dung; hai game đó **không có bio hero**.
{T6 UNVERIFIED: h3wiki-gem — không có text tiểu sử ở H1/H2}

---

## Nguồn

| Loại | Số lượng | Ghi chú |
|---|---|---|
| **`T1`** — file game thật | **1** | ⭐⭐ `h3wiki-herobios-txt` — bio trích từ string table, **không dấu sao** |
| `T1*` — text game qua trung gian | **9** | ⭐⭐ `sod-agents-of-vengeance` (gốc gác) · `sod-driving-for-the-boots` (tuyến chuyển Druid) · `sod-after-the-amulet` (vụ lừa) |
| **`T2*`** — sách in qua trung gian | **3** | ⚠️ `sod-manual-p14` là **một phía** của tranh chấp class |
| `T4` — phát ngôn developer | 1 | `fulton-fanstratics-27` — xác nhận nhân vật kế thừa có chủ ý |
| `T6` — wiki cộng đồng | 2 | ⚠️ Dùng chủ yếu để **loại trừ** |

**Nguồn giá trị nhất: `sod-agents-of-vengeance`.** Nó chứa **cả** gốc gác nhân vật **và** neo thời
gian "decades" mà `TIMELINE-SPINE.md` đang dùng — và **cả hai đều nằm trong timed event**, không có
trong prologue.

⭐ **Đặc điểm đáng chú ý của bộ nguồn này:** phần **hay nhất** về nhân vật đều **không nằm ở nơi
người ta tìm**. Bio chính thức cho biết nàng từng phụng sự Roland; nhưng thứ giải thích **vì sao nàng
làm mọi việc nàng làm** thì nằm rải trong các timed event của bốn scenario.

---

## Liên kết

**Nhân vật:** [[sandro]] · [[ethric]] · [[gelu]] · [[yog]] · [[crag-hack]] · [[vidomina]]

**Quốc gia:** [[avlee]] · [[erathia]] · [[deyja]] · [[bracada]]

**Vật phẩm:** [[amulet-of-the-undertaker]] · [[vampires-cowl]] · [[dead-mans-boots]] ·
[[cloak-of-the-undead-king]]

**Sự kiện:** [[the-reckoning]]
