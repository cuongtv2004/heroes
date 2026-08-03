# Verify report: dead-mans-boots — 2026-08-03

Verifier: agent độc lập, không đọc bài gốc, không đọc `docs/sources/raw/`, không đọc bài codex cùng cụm
Số claim kiểm: 17
CONFIRMED: 14 | DOWNGRADE: 2 | NOT_FOUND: 0 | CONTRADICTED: 1

Mức nghiêm trọng: **BLOCKER: 1** · **MAJOR: 5** · MINOR: 4 · NOTE: 2

Phương pháp: fetch trực tiếp `?action=raw` (wikitext thô) bằng `curl`, không qua render và không qua WebFetch-summarize — vì bản summarize làm mất nguyên văn. Đã đối chiếu chéo hai fork độc lập của thelazy (`homm.fandom.com`, `homm.miraheze.org`) và hai bản dump string trích từ file game.

---

## Chi tiết

### C-01
Claim: Text khi nhặt artifact — "Discovering a pair of beautifully beaded boots made from the finest and softest leather, you thank the anonymous donor and add the boots to your inventory."
Nhãn bài gán: T1* EXPLICIT — `h3wiki-dead-mans-boots`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Dead_Man's_Boots&action=raw` · `https://heroes.thelazy.net/index.php?title=Artifact_Events&action=raw`
Tìm thấy: trong infobox — `| event  = Discovering a pair of beautifully beaded boots made from the finest and softest leather, you thank the anonymous donor and add the boots to your inventory.`
Xác nhận độc lập ở trang `Artifact Events` (35.645 byte, mở đầu bằng "Default descriptions when picking an artifact."):
> `{{An|Dead Man's Boots}}`: "Discovering a pair of beautifully beaded boots made from the finest and softest leather, you thank the anonymous donor and add the boots to your inventory."
Lý do: khớp từng chữ, có ở **hai** trang riêng biệt của cùng wiki. Trích dẫn đúng, tier đúng.

---

### C-02
Claim: Trong scenario `Driving for the Boots` (SoD, campaign *A New Beginning*), đôi giày nằm tại (2, 103, 0)
Nhãn bài gán: T1* EXPLICIT — `sod-driving-for-the-boots`
Phán quyết: **CONFIRMED** (toạ độ) — nhưng **tên campaign SAI**
Mức: **MINOR**
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Driving_for_the_Boots&action=raw` · `.../New_Beginning&action=raw` · `.../The_Shadow_of_Death&action=raw` · `.../Shadow_of_Death_Manual_Page_14&action=raw`
Tìm thấy: bảng `==== Artifacts ====`, ô Location: `2, 103, 0`, Type `{{An|Dead Man's Boots}}`. Và `| source = sod`, `| cback = sod nb 4`.
Nguồn ngược về tên campaign: campaign có tên **`New Beginning`**, không phải "A New Beginning" — ba nguồn độc lập cùng nói vậy:
- Trang campaign: `| scenario = New Beginning`
- Danh sách campaign trên trang `The Shadow of Death`: `* [[New Beginning]]`
- **Manual tr.14** (T2*): `New Beginning`
Lý do: toạ độ chính xác. Nhưng mạo từ "A" là do người viết thêm vào; phải bỏ. (Trùng hợp gây bẫy: chính text in-game Day 51 có câu Amanda gọi đây là the "New Beginning" — càng chứng tỏ tên đúng không có "A".)

---

### C-03
Claim: Text tại chỗ đặt giày — "In the middle of a small mountain glade sits a pair of Dead Man's Boots. The hair rises on the back of your neck. A gentle breeze carries the faint odor of decay."
Nhãn bài gán: T1* EXPLICIT — `sod-driving-for-the-boots`
Phán quyết: **CONFIRMED**
Mức: **MINOR** (trích thiếu câu cuối)
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Driving_for_the_Boots&action=raw`
Tìm thấy (nguyên văn, giữ nguyên khoảng trắng đôi của game):
> "In the middle of a small mountain glade sits a pair of [[Dead Man's Boots]].  The hair rises on the back of your neck.  A gentle breeze carries the faint odor of decay.  **Do you wish to pick up the Boots?**"
Lý do: ba câu đầu khớp từng chữ. Nhưng bài cắt mất câu thứ tư và **không đánh dấu là trích lược** — đọc như thể đó là toàn bộ đoạn text. Phải thêm `[…]` hoặc trích đủ.

---

### C-04
Claim: Lính canh gồm 7 stack, tổng 215 quân: stack 1 & 7 = 35 Power Liches; 2 & 6 = 30 Dread Knights; 3 & 5 = 30 Vampire Lords; 4 = 25 Ghost Dragons
Nhãn bài gán: T1* EXPLICIT — `sod-driving-for-the-boots`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Driving_for_the_Boots&action=raw`
Tìm thấy:
> `'''Guardians:''' 35 {{Cn|Power Lich}}es, 30 {{Cn|Dread Knight}}s, 30 {{Cn|Vampire Lord}}s, 25 {{Cn|Ghost Dragon}}s, 30 {{Cn|Vampire Lord}}s, 30 {{Cn|Dread Knight}}s,  35 {{Cn|Power Lich}}es`
Lý do: đúng 7 stack, đúng thứ tự, và **đối xứng gương** quanh stack 4 như bài mô tả. Tổng kiểm lại: 35+30+30+25+30+30+35 = **215**. Con số 215 không có sẵn trong nguồn — đó là phép cộng của người viết, nhưng phép cộng đúng và hiển nhiên; ghi `EXPLICIT` cho danh sách stack thì đúng, còn con số tổng nên ghi kèm là suy ra.

---

### C-05
Claim: Có một Quest Guard tại (3, 104, 0) đòi Sandals of the Saint mới cho qua
Nhãn bài gán: T1* EXPLICIT — `sod-driving-for-the-boots`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Driving_for_the_Boots&action=raw`
Tìm thấy: `{{SorQrow|guard=1|loc=3, 104, 0|quest=Return with:<br>{{An|Sandals of the Saint}}</br>|prop=A powerful wizard owns this tower.  He refuses to let you pass unless you bring him the Sandals of the Saint.|...}}`
Lý do: khớp hoàn toàn. **Chi tiết bổ sung đáng dùng:** Quest Guard (3,104,0) và đôi giày (2,103,0) nằm **kề nhau chéo** — nghĩa là cổng này là cửa duy nhất vào chỗ đặt giày, không phải một chướng ngại giữa đường.

---

### C-06
Claim: Sandals of the Saint lấy từ Seer's Hut tại (74, 3, 0), đổi bằng 25 Ghost Dragons; kèm hai đoạn thoại của seer
Nhãn bài gán: T1* EXPLICIT — `sod-driving-for-the-boots`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Driving_for_the_Boots&action=raw`
Tìm thấy: `{{SorQrow|seer=1|loc=74, 3, 0|quest=Return with:<br>25 {{Cn|Ghost Dragon}}s</br>|rew={{An|Sandals of the Saint}}|prop=I am a seer.  I have foreseen you will need the Sandals of the Saint.  I have a pair I am willing to give you in return for 25 Ghost Dragons.  She laughs when you grit your teeth.  "You'll be back."|prog=No 25 Ghost Dragons?  Well then, no Sandals for you.|comp=At last, the 25 Ghost Dragons!  It took you long enough.  Here, take the Sandals.  Their aura of goodness sickens me.}}`
Lý do: cả hai đoạn trích khớp từng chữ, kể cả câu chêm ngôi thứ ba "She laughs when you grit your teeth." — chi tiết này khó bịa, là dấu hiệu bản chép trung thực.
**NOTE (gợi ý, không phải lỗi):** bài chưa dùng đoạn `prog` ("No 25 Ghost Dragons?  Well then, no Sandals for you.") và chưa nêu vòng lặp thiết kế đáng chú ý: seer đòi **đúng 25 Ghost Dragons**, cũng đúng bằng stack Ghost Dragon canh giày — nhưng 25 con đó **không lấy được từ đám lính canh** (chúng bị diệt), nên người chơi buộc phải chiếm Necropolis của địch để nuôi. Đây là một chi tiết gameplay–narrative đáng đưa vào bài.

---

### C-07
Claim: Epilogue — "Sandro has tricked me! But to what purpose? Why would he run off with the Dead Man's Boots without paying me?"
Nhãn bài gán: T1* EXPLICIT — `sod-driving-for-the-boots` (epilogue)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Driving_for_the_Boots&action=raw`, mục `== Epilogue ==`
Tìm thấy:
> "[[Sandro]] has tricked me!  But to what purpose?  Why would he run off with the [[Dead Man's Boots]] without paying me?  Did he keep the money for himself?  Did he give [[Ethric]] the other artifacts?  He certainly couldn't have been an agent for [[Deyja]] - the undead troops I destroyed to get the artifacts were worth more than the artifacts themselves.  None of this makes sense!  I will have to write to [[Ethric]] in [[Bracada]] and tell [[Lord Fayette]] about this immediately."
Lý do: khớp từng chữ; đúng là trích lược đầu đoạn nên không gây hiểu sai. **NOTE:** phần bài bỏ đi có giá trị cao hơn phần đã trích — Gem tự loại giả thuyết "Sandro là người của Deyja" bằng lý lẽ kinh tế ("the undead troops I destroyed... were worth more than the artifacts themselves"). Nên dùng.

---

### C-08
Claim: Thông số gốc — slot = Feet; class = Major; giá = 6000; hiệu ứng = +15% Necromancy
Nhãn bài gán: T1* EXPLICIT — `h3wiki-dead-mans-boots`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Dead_Man's_Boots&action=raw` · `.../Necromancy&action=raw` · Fandom `List of Heroes III artifacts`
Tìm thấy: `| class = Major` · `| slot = Feet` · `| cost = 6000` · `| effect = +15% {{gl|Necromancy}}`
Xác nhận chéo, trang `Necromancy`: `* {{an|Dead Man's Boots}}: +15% Necromancy`. Và Fandom: "|Major\n| Worn on the feet, these boots increase your Necromancy skill by 15%."
Lý do: bốn thông số, ba nguồn, không lệch.

---

### C-09
Claim: Mô tả in-game — "Worn on the feet, these boots increase your Necromancy skill by 15%."
Nhãn bài gán: **T6 EXPLICIT** — `fandom-artifact-list`
Phán quyết: **CONFIRMED** — nhưng nhãn **quá THẤP**, và tổ hợp nhãn **vi phạm policy**
Mức: **MAJOR**
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Talk:Artifact/descriptions&action=raw` · `https://mightandmagic.fandom.com/api.php?action=parse&page=List_of_Heroes_III_artifacts&prop=wikitext`
Tìm thấy — nguồn tốt hơn hẳn nguồn bài đang dẫn. Trang `Talk:Artifact/descriptions` mở đầu bằng dòng tiêu đề bảng:
> `|+ style="white-space:nowrap;"|Information from H3Bitmap.lod > artraits.txt`
và dòng 117:
> `| [[Dead Man's Boots]] || Worn on the feet, these boots increase your Necromancy skill by 15%.`
Lý do — **hai lỗi độc lập:**
1. **`T6 EXPLICIT` là tổ hợp nhãn không hợp lệ.** `CANON-POLICY.md` §2 nói thẳng: "Nếu một claim chỉ có T6 chống lưng, nó tối đa là `INFERENCE` hoặc `UNVERIFIED`." Bài gán `EXPLICIT` cho một nguồn T6 → sai luật, bất kể nội dung đúng.
2. **Có nguồn `T1` thật mà bài không dùng.** `H3Bitmap.lod > artraits.txt` là **string table trích trực tiếp từ file game**, đúng loại nguồn mà `REGISTRY.md` đã xếp `h3wiki-herobios-txt` vào tier **`T1`** (không dấu sao). Fandom (không dẫn nguồn) chỉ là bản chép lại của chính chuỗi này.
**Phải sửa:** thêm source key mới vào `REGISTRY.md` — đề xuất `h3wiki-artraits-txt`, tier **`T1`**, access FETCHED, ghi chú "`Talk:Artifact/descriptions` — bảng mô tả artifact trích từ `H3Bitmap.lod > artraits.txt`" — rồi đổi nhãn C-09 thành `{T1 EXPLICIT: h3wiki-artraits-txt}`.
**Đây là tiến triển trực tiếp cho `B-001`** (nâng `T1*` → `T1`) và áp dụng được cho **toàn bộ** các bài artifact khác, không riêng bài này.

---

### C-10
Claim: SoD gốc +15%; HotA 1.3.0 → 1.7.x = +7,5%; HotA 1.8.0 khôi phục +15%
Nhãn bài gán: T1* EXPLICIT — `hota-changelog`
Phán quyết: **CONFIRMED**
Mức: — (kèm một **NOTE** về tier, xem cuối)
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Horn_of_the_Abyss_(Changelog)&action=raw` (201.529 byte) — **dùng changelog, không dùng trang artifact, theo BH-3**
Tìm thấy — hai dòng, hai phiên bản:
- `== Version 1.3.0 (01/JAN/2014) ==`, dòng 2005:
  > "[+] The number of Skeletons raised by necromancy is reduced by half, as well as bonuses to it from artifacts and a Necromancy Amplifier"
- `== Version 1.8.0 (31/DEC/2025) ==`, dòng 31:
  > "[-] 5/10/15/30% Necromancy boost values are back for the Amulet of the Undertaker, Vampire's Cowl, Dead Man's Boots, and Cloak of the Undead King (**instead of 2.5/5/7.5/15%**)"
Lý do: con số **7,5%** không phải suy ra — nó được in **nguyên văn** trong ngoặc ở dòng 1.8.0, và Dead Man's Boots được nêu tên trong cùng câu. Nên `EXPLICIT` đứng vững.
Đã kiểm cận trên/cận dưới của khoảng phiên bản: grep toàn bộ changelog cho "necromancy" trả về **không có** lần đổi giá trị artifact nào khác giữa 1.3.0 và 1.8.0; và danh sách heading xác nhận **1.7.3 (08/JUN/2025) là bản cuối trước 1.8.0**. Vậy "1.3.0 → 1.7.x" là đúng, không có khoảng trống.
**Đối chiếu ngược với trang artifact (đúng như BH-3 cảnh báo):** trang `Cloak of the Undead King` chỉ nói về lệnh cấm ghép 1.7.2, **không hề nhắc** việc giá trị Necromancy từng bị chia đôi. Ai chỉ đọc trang artifact sẽ bỏ sót toàn bộ claim này.

---

### C-11
Claim: Dead Man's Boots là thành phần mạnh nhất trong ba thành phần của Cloak of the Undead King — một mình nó bằng Amulet of the Undertaker + Vampire's Cowl
Nhãn bài gán: **(không gán nhãn trong bài)**
Phán quyết: **CONFIRMED** (nội dung) — nhưng **thiếu nhãn là lỗi**
Mức: **MAJOR**
Đã tìm ở: `.../Amulet_of_the_Undertaker&action=raw` · `.../Vampire's_Cowl&action=raw` · `.../Dead_Man's_Boots&action=raw` · `.../Necromancy&action=raw`
Tìm thấy:
- Amulet of the Undertaker: `| class = Treasure` · `| cost = 2000` · `| effect = +5% {{gl|Necromancy}}`
- Vampire's Cowl: `| class = Minor` · `| cost = 4000` · `| effect = +10% {{gl|Necromancy}}`
- Dead Man's Boots: `| class = Major` · `| cost = 6000` · `| effect = +15% {{gl|Necromancy}}`
Lý do: 5% + 10% = 15% — đúng. "Mạnh nhất" đúng theo **cả ba** thước đo độc lập: % Necromancy (15 > 10 > 5), giá (6000 > 4000 > 2000), và class (Major > Minor > Treasure). Nội dung không phản bác được.
**Nhưng:** `CANON-POLICY.md` §5.1 buộc "Mọi claim trong thân bài có nhãn hai trục + source key". Claim này nằm trong thân bài mà **không có nhãn nào** → vi phạm điều kiện hoàn thành bài.
Thêm nữa, nếu gán nhãn thì **không được gán `EXPLICIT`**: không nguồn nào nói "đôi giày bằng hai cái kia cộng lại". Đó là phép cộng của người viết → theo §2 phải là `INFERENCE`, và §2 buộc "ghi rõ suy luận theo bước nào".
**Phải sửa thành:** `{T1* INFERENCE: h3wiki-dead-mans-boots + h3wiki-amulet-of-the-undertaker + h3wiki-vampires-cowl — 5% + 10% = 15%}`
**NOTE có lợi cho bài:** quan hệ này **bất biến qua phiên bản** — trong HotA 1.3.0–1.7.x các giá trị bị chia đôi *theo tỷ lệ* (2,5 + 5 = 7,5), nên "một mình nó bằng hai cái kia" vẫn đúng. Đáng viết ra, vì nó biến một phép cộng vụn thành một nhận xét thiết kế.

---

### C-12
Claim: Danh sách scenario có đôi giày — `Driving for the Boots`; `From Day to Night` (RoE, bonus khởi đầu trên Thant); `Taming of the Wild` (nhặt tự do); `Dead or Alive` (Quest Guard); `Viking We Shall Go!` (Seer's Hut → Statesman's Medal); `Jorm's Ambush` (Seer's Hut → 13.349 vàng); `The Life Guard` (Shipwreck Survivor); `Black'n'Blue` (template, **trong danh sách artifact cho phép**); `Apocalypse` (HotA template)
Nhãn bài gán: T1* EXPLICIT — `h3wiki-dead-mans-boots`
Phán quyết: **CONTRADICTED**
Mức: **BLOCKER**
Đã tìm ở: `.../api.php?action=query&list=backlinks&bltitle=Dead Man's Boots&bllimit=500` (quét toàn bộ 200+ trang trỏ tới artifact, để không phụ thuộc vào danh sách của bài), rồi fetch raw từng scenario: `Taming_of_the_Wild`, `Dead_or_Alive`, `The_Life_Guard`, `From_Day_to_Night`, `Viking_We_Shall_Go!`, `Viking_We_Shall_Go!_(Allies)`, `Jorm's_Ambush`, `Black'n'Blue`, `Apocalypse`, `Sleepkeeper`

**Nguồn nói NGƯỢC LẠI — `Black'n'Blue`.** Bài ghi đôi giày nằm trong "danh sách artifact **cho phép**". Trang template ghi ngược hẳn:
> `*Banned artifacts:`
> `**{{An|Skull Helmet}}`
> `**{{An|Tunic of the Cyclops King}}`
> `**{{An|Dead Man's Boots}}`
> `**{{An|Angel Wings}}` …

Đôi giày bị **CẤM** trên `Black'n'Blue`, không phải được cho phép. Đây là đảo ngược ý nghĩa hoàn toàn — và nó nguy hiểm vì nằm cạnh `Apocalypse` (nơi đôi giày *thật sự* được cho phép), nên người đọc sẽ hiểu hai template cùng chiều trong khi chúng **ngược chiều**.

**Ba lỗi độc lập nữa trên cùng claim:**

1. **Source key không chống lưng nổi claim.** Toàn bộ trang `Dead Man's Boots` chỉ dài **660 byte** và đã fetch đủ ở trên: nó **không có một dòng nào** về scenario appearance. Không có bảng xuất hiện, không có tên map nào. Danh sách này thực ra nằm rải ở **chín trang scenario/template khác nhau**, không trang nào có source key trong `REGISTRY.md`. Dẫn `h3wiki-dead-mans-boots` cho danh sách này là mis-citation → vi phạm `CANON-POLICY.md` §5.2.

2. **Thiếu mục.** Backlinks lộ ra `Viking We Shall Go! (Allies)` — một trang scenario **riêng**, cũng chứa Seer's Hut đôi giày ở đúng toạ độ:
   > `{{SorQrow|seer=3|loc=<br>53, 116, 0</br>|quest=Return with:<br>{{An|Dead Man's Boots}}</br>|rew={{An|Statesman's Medal}}}}`
   Bài bỏ sót bản này.

3. **Gộp năm sản phẩm khác nhau thành một danh sách phẳng.** Đọc `| source =` từng trang cho ra:
   | Scenario | `source` |
   |---|---|
   | Driving for the Boots | **sod** |
   | From Day to Night | **roe** |
   | Taming of the Wild | **ab** (Armageddon's Blade) |
   | Viking We Shall Go! (+ Allies) | **sod** |
   | Jorm's Ambush | **hc** (Heroes Chronicles) |
   | Dead or Alive | **hota** |
   | The Life Guard | **hota** |
   | Black'n'Blue / Apocalypse | **hota** (template) |

   Bài chỉ ghi "(RoE)" cho một mục và im lặng với phần còn lại — người đọc sẽ tưởng cả danh sách là SoD. Ba mục là **HotA** (nội dung fan-made, không phải NWC) và một mục là **Heroes Chronicles**. Đây đúng là loại lỗi mà quy tắc "mọi con số gameplay phải ghi rõ phạm vi phiên bản" tồn tại để chặn.

**Phần đúng của claim** (đã kiểm từng cái, để người viết không phải làm lại):
- `From Day to Night` (roe, `cback = roe lltk 4`): `| bonus = ...{{BonusArt|Dead Man's Boots|loc=Thant}}...` → **đúng**, bonus khởi đầu trên Thant
- `Taming of the Wild` (ab) tại (67, 3, 0): message có, **không có dòng `Guardians:`** → **đúng**, nhặt tự do
- `Dead or Alive` (hota) tại (56, 30, 0): `quest=Return with:<br>{{An|Dead Man's Boots}}` → **đúng**, Quest Guard
- `Viking We Shall Go!` tại (53, 116, 0): `rew={{An|Statesman's Medal}}` → **đúng**
- `Jorm's Ambush` (hc) tại (3, 7, 1): `rew=13349 {{g}} [[Gold]]` → **đúng**, 13.349 vàng
- `The Life Guard` (hota) tại (35, 25, 1): `{{encounter row|35, 25, 1|{{map object|Shipwreck Survivor}}|{{An|Dead Man's Boots}}}}` → **đúng**
- `Apocalypse` → **đúng** (xem C-14)
- `Sleepkeeper` xuất hiện trong backlinks nhưng **là dương tính giả** — liên kết đến từ template điều hướng `{{Artifact 'see also'}}`, không phải một lần xuất hiện thật. Đã kiểm, loại.

---

### C-13
Claim: Trong `Taming of the Wild` có text riêng — "A note on the boots reads: 'Dead men tell no tales.'"
Nhãn bài gán: T1* EXPLICIT — `h3wiki-dead-mans-boots`
Phán quyết: **CONFIRMED**
Mức: **MAJOR** (source key sai) + **MINOR** (dấu câu)
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Taming_of_the_Wild&action=raw`, bảng `Artifacts`, dòng 103–105
Tìm thấy (nguyên văn):
> `A note on the boots reads:  "Dead men tell no tales".`
Lý do:
- **MAJOR:** text này nằm trên trang `Taming of the Wild`, **không** trên trang artifact (660 byte, không chứa nó). Source key `h3wiki-dead-mans-boots` không chống lưng được. Cần source key mới trong `REGISTRY.md` — đề xuất `ab-taming-of-the-wild`, tier `T1*`, ghi chú "Armageddon's Blade, campaign *Festival of Life* #2 — cả **ba** thành phần Cloak nằm kề nhau".
- **MINOR:** game đặt dấu chấm **ngoài** ngoặc kép (`tales".`), bài đặt **trong** (`tales.'`). Với một dự án lấy "chép nguyên cả lỗi chính tả trong game" làm cơ sở tin cậy `T1*`, sai dấu câu trong trích dẫn là không nhất quán với chính tiêu chuẩn đó.
**NOTE (phát hiện thêm, có giá trị):** trong `Taming of the Wild`, **cả ba** thành phần Cloak nằm sát nhau — Dead Man's Boots (67,3,0), Amulet of the Undertaker (68,4,0), Vampire's Cowl (69,4,0) — tất cả nhặt tự do, không lính canh. Nghĩa là map này cho ghép trọn Cloak of the Undead King gần như miễn phí. Đáng vào bài hơn nhiều so với chỉ nhắc câu "Dead men tell no tales".

---

### C-14
Claim: Trong template `Apocalypse` của HotA, Dead Man's Boots là một trong ba artifact **duy nhất** được cho phép
Nhãn bài gán: T1* EXPLICIT — `h3wiki-dead-mans-boots`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `.../Apocalypse&action=raw` · `.../Horn_of_the_Abyss_(Changelog)&action=raw` (grep "apocalypse", "allowed artifact", "Vampire's Cowl") · `https://h3hota.com/en/rules` (trang luật chính thức của HotA) · `.../api.php?action=query&prop=revisions&titles=Apocalypse`
Tìm thấy — trang template có đúng ba mục, và đúng là ba thành phần của Cloak:
> `*Allowed artifacts:`
> `**{{An|Amulet of the Undertaker}}`
> `**{{An|Vampire's Cowl}}`
> `**{{An|Dead Man's Boots}}`

Lý do hạ nhãn — **bốn vấn đề, ba trong số đó là BH-3 đúng nguyên văn:**

1. **Chữ "duy nhất" không có trong nguồn.** Nguồn viết "Allowed artifacts:" rồi liệt kê ba. Nó **không** viết "only three artifacts are allowed". "Duy nhất" là **suy luận** của người viết từ một đầu đề danh sách → không thể là `EXPLICIT`.

2. **Changelog KHÔNG chống lưng — vi phạm BH-3.** BH-3 buộc dùng changelog cho mọi claim HotA. Đã grep toàn bộ 201.529 byte: `Apocalypse` chỉ xuất hiện **hai lần**, và **không lần nào** là danh sách artifact cho phép:
   - `== Version 1.5.0 (01/JAN/2018) ==`: "[-] Added the Boomerang and Apocalypse templates"
   - `== Version 1.7.1 (06/APR/2024) ==`: "[-] Apocalypse template: Wanderer's Boots and Shrines of Magical Mystery banned"
   Grep "Vampire's Cowl" trong changelog chỉ trả về **một** dòng duy nhất — dòng 1.8.0 ở C-10. Danh sách ba artifact **chưa từng vào changelog**.

3. **Có bằng chứng ngược cho cách đọc "duy nhất".** Dòng 1.7.1 cấm thêm một artifact slot-Feet nữa ("Wanderer's Boots") trên Apocalypse. Nếu toàn template chỉ cho phép ba artifact thì việc cấm riêng một artifact thứ tư là **vô nghĩa** — nó đã bị cấm sẵn. Cách đọc dung hòa được: "Allowed artifacts" nghĩa là "được cho phép **thêm**, ngoài các lệnh cấm mặc định" (ba thành phần Cloak vốn liên quan lệnh cấm ghép Cloak từ 1.7.2). Dù cách đọc nào đúng thì "một trong ba artifact duy nhất" cũng **không** phải điều nguồn nói.

4. **Không có phạm vi phiên bản.** Trang `Apocalypse` được tạo 2024-01-26, sửa lần cuối **2025-05-14** — tức phản ánh khoảng HotA 1.7.2, **trước 1.8.0** (31/DEC/2025). Trang không tự ghi phiên bản nào. Đúng thứ mà `SCHEMA.md` và cảnh báo trong `REGISTRY.md` buộc phải ghi rõ.

Kiểm thêm để chắc: trang luật **chính thức** `h3hota.com/en/rules` (do chính trang template dẫn tới) có mục Apocalypse nhưng **không có danh sách artifact cho phép hay bị cấm nào cả** — nên không có nguồn cấp cao hơn để nâng claim lên.

**Phải sửa:** đổi thành `{T6 INFERENCE: <key mới cho trang template Apocalypse> — trang liệt kê ba artifact dưới đầu đề "Allowed artifacts"; chữ "duy nhất" là suy luận}`, **kèm phạm vi phiên bản** (trạng thái trang tại 2025-05-14 ≈ HotA 1.7.2–1.7.3), và **ghi rõ changelog không xác nhận**. Tier: trang đặc tả template do cộng đồng viết, **không phải in-game text** → `T1*` là sai loại; đúng nhất là `T6`.
**NOTE đáng viết:** ba artifact được cho phép chính là **ba thành phần của Cloak of the Undead King** — trên một template mà "Players and AI cannot select Necropolis as starting alignment. All neutral tows [sic] are Necropolises" và "All Necropolis heroes are banned". Đó là một lựa chọn thiết kế có ý, không phải trùng hợp.

---

### C-15
Claim: Điều khoản "artifact vô tác dụng nếu hero không có kỹ năng Necromancy" là **văn của người viết wiki**, KHÔNG phải game text; câu gốc có lỗi ngữ pháp "the Dead Man's Boots **has** no effect"
Nhãn bài gán: (nhận định về nguồn) — `h3wiki-dead-mans-boots`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `.../Dead_Man's_Boots&action=raw` · `.../Amulet_of_the_Undertaker&action=raw` · `.../Vampire's_Cowl&action=raw` · `.../Talk:Artifact/descriptions&action=raw` · `.../Artifact_Events&action=raw` · `.../Necromancy&action=raw` · `https://homm.fandom.com/api.php?...` · `https://homm.miraheze.org/w/api.php?...`
Tìm thấy — nguyên văn, và đúng là lỗi ngữ pháp:
> `If the equipped hero does not have the [[Necromancy]] secondary skill, the Dead Man's Boots **has** no effect.`

Lý do — claim này là **claim phủ định về xuất xứ**, nên tôi kiểm bằng chứng cứ dương thay vì chỉ "không thấy":

1. **Vị trí trong wikitext chứng minh nó là văn wiki.** Câu nằm **ngoài** template `{{ArtifactNewSB}}`, ở thân bài trần. Mọi game text trên wiki này đều bị bọc trong tham số template (`| event =`, `| effect =`). Câu này không.

2. **Vắng mặt khỏi cả hai bản dump string trích từ file game.** `Talk:Artifact/descriptions` (`H3Bitmap.lod > artraits.txt`) chỉ có "Worn on the feet, these boots increase your Necromancy skill by 15%." — không có điều kiện nào. `Artifact Events` chỉ có đoạn nhặt. Game **không** nói câu này ở đâu cả.

3. **Lỗi ngữ pháp truy được về nguyên nhân.** Câu y hệt xuất hiện trên trang Amulet ("the Amulet of the Undertaker has no effect") và Cowl ("the Vampire's Cowl has no effect") — ở đó `has` **đúng** vì chủ ngữ số ít. Trên trang Boots, chủ ngữ là "Boots" (số nhiều) nên `has` sai. Đây là dấu vết **copy-paste giữa ba trang** — bằng chứng gần như quyết định rằng đây là văn một biên tập viên viết, không phải chuỗi game.

4. **Ba wiki cùng lỗi, nhưng không phải ba nguồn.** `homm.fandom.com` (pageid 809) và `homm.miraheze.org` (pageid 600) trả về wikitext **giống hệt từng byte** với thelazy, kể cả lỗi `has`. Đây là fork, **không phải xác nhận độc lập** — quan trọng phải ghi vậy để không ai tưởng "ba wiki đều nói" là ba nguồn.

Bản thân **cơ chế** thì đúng (trang `Necromancy`: số skeleton hồi sinh phụ thuộc "Level of Necromancy skill"; không có skill thì không hồi sinh) — nhưng đó là mô tả cơ chế do wiki suy ra, không phải câu game nói. Đúng như claim khẳng định. Đây là claim phủ định được xử lý tốt nhất trong cả bảng.

---

### C-16
Claim: Không nguồn nào kể ai đã tạo ra artifact này
Nhãn bài gán: (claim phủ định) — không source key
Phán quyết: **CONFIRMED**
Mức: **NOTE** (claim sống, nhưng nên viết lại cho mạnh hơn)
Đã tìm ở — liệt kê đầy đủ vì đây là claim phủ định:
- `heroes.thelazy.net`: `Dead_Man's_Boots` (toàn bộ 660 byte), `Cloak_of_the_Undead_King`, `Necromancy`, `Artifact_Events`, `Talk:Artifact/descriptions`, `Driving_for_the_Boots`, `Taming_of_the_Wild`, `Dead_or_Alive`, `The_Life_Guard`, `From_Day_to_Night`, `Viking_We_Shall_Go!`, `Jorm's_Ambush`
- `.../api.php?action=query&list=backlinks&bltitle=Dead Man's Boots&bllimit=500` — quét toàn bộ 200+ trang trỏ tới artifact, không sót trang nào
- **Kiểm disambiguation theo BH-2:** `.../index.php?title=Dead_man's_boots&action=raw` → chỉ là `#REDIRECT [[Dead Man's Boots]]`, **không phải** trang disambiguation, không có thực thể trùng tên thứ hai. Tìm Fandom (`list=search`, 30 kết quả, mọi namespace) cho "Dead man boots" không ra artifact/vật phẩm trùng tên nào ở Heroes I/II/IV–VII hay MM VI–IX
- `mightandmagic.fandom.com`: `list=search` cho `"Dead Man's Boots"` → **chỉ 7 trang**, không trang nào riêng cho artifact, không trang nào có lore nguồn gốc. Trang `Cloak of the Undead King` (fetch đủ qua API) chỉ có cơ chế, không có nguồn gốc
- `homm.fandom.com`, `homm.miraheze.org` → fork byte-identical của thelazy, không thêm gì
- `heroesofmightandmagic.com/heroes3/artifactsadventure.shtml` (site NWC) → **HTTP 403**, và body là `<title>Web Filter Violation</title>` — bị **filter mạng của môi trường** chặn, không phải site chết
- WebSearch "Dead Man's Boots Heroes III artifact lore origin who created" → không kết quả nào có người tạo ra

Lý do: sau khi quét cả 200+ backlinks và hai bản dump string trích từ file game, không nguồn nào nêu người tạo. Claim đứng vững.

**NOTE — cách viết lại để claim mạnh hơn hẳn:** đừng để nó là một câu phủ định trần ("không nguồn nào kể"). **Game text tự nói ra sự vô danh đó**, và đó là chứng cứ dương:
> "you thank the **anonymous donor** and add the boots to your inventory" {T1 EXPLICIT: <artraits/Artifact Events>}

Cộng thêm mảnh duy nhất về **người giữ** (không phải người tạo), nằm trong block `=== Timed events ===` của `Driving for the Boots`, Day 4 — đúng chỗ BH-1 chỉ:
> "I tried to scry the location of the Dead Man's Boots but could not divine anything useful.  My scrying abilities are more closely tied to living things.  However, according to [[Sandro]], the Boots are in the possession of a [[Wizard]] south of here."

Viết như vậy thì claim chuyển từ "chúng tôi không tìm được" (trông giống sự cẩn trọng nhưng không kiểm được) thành "game chủ động để trống nguồn gốc, và chỉ cho biết người đang giữ" (có trích dẫn, kiểm được).

---

### C-17
Claim: Game không giải thích VÌ SAO cần Sandals of the Saint mới qua được cổng. Text **chỉ nói**: "A powerful wizard owns this tower. He refuses to let you pass unless you bring him the Sandals of the Saint."
Nhãn bài gán: **T1\* UNVERIFIED** — `sod-driving-for-the-boots`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `https://heroes.thelazy.net/index.php?title=Driving_for_the_Boots&action=raw` — đọc **toàn bộ** trang 12.995 byte: prologue, `=== Timed events ===` (14 event), `Objects`, `Town timed events`, `Heroes`, `Artifacts`, `Seer's Huts`, `Quest Guards`, epilogue
Tìm thấy — câu trích **đúng nguyên văn** (`prop` của Quest Guard (3,104,0)):
> `A powerful wizard owns this tower.  He refuses to let you pass unless you bring him the Sandals of the Saint.`

Lý do hạ nhãn — **hai vấn đề:**

1. **`UNVERIFIED` là nhãn sai, và không được phép ở thân bài.** Câu trích tôi vừa xác minh **từng chữ** — nó là `EXPLICIT`, không phải `UNVERIFIED`. Và `CANON-POLICY.md` §5.3 nói thẳng: "Không claim nào ở trạng thái `UNVERIFIED` trong thân bài". Nếu claim này đang ở thân bài, riêng nhãn đó đã đủ chặn `verified`. Nhãn đúng phải tách hai phần: câu trích = `T1* EXPLICIT`; nhận định "game không giải thích" = `T1* INFERENCE` (suy ra từ sự vắng mặt sau khi đã đọc hết trang — và phải ghi rõ bước suy luận đó theo §2).

2. **"Text CHỈ nói" là sai — đây đúng là BH-1.** Có thêm text liên quan, và nó nằm trong block `=== Timed events ===`, không ở prologue/epilogue. Day 4:
   > "I tried to scry the location of the Dead Man's Boots but could not divine anything useful.  My scrying abilities are more closely tied to living things.  However, according to [[Sandro]], the Boots are in the possession of a [[Wizard]] **south of here**."

   Đoạn này **nối** wizard giữ cổng với đôi giày: hắn không phải người gác ngẫu nhiên — hắn là **người đang giữ artifact**, và Sandro đã nói trước với Gem như vậy. Bài bỏ mất mảnh này, đúng loại sai sót mà BH-1 ghi lại ("một đợt research kết luận sai rằng cả một tuyến truyện không tồn tại vì chỉ đọc prologue").

**Phần cốt lõi của claim vẫn sống:** sau khi đọc hết 12.995 byte, thật sự **không** có đoạn nào giải thích vì sao phải là *Sandals of the Saint* — cụ thể chứ không phải vật gì khác. Nên nhận định chính đứng vững; chỉ có nhãn và cơ sở chứng cứ phải sửa.
**NOTE:** mảnh gần nhất với một lời giải thích là câu của seer — "Here, take the Sandals.  **Their aura of goodness sickens me.**" — xác lập Sandals là vật thuộc phe Thiện. Không giải thích được yêu cầu của wizard, nhưng là chi tiết duy nhất trong map gán *tính chất* cho Sandals, và đáng nhắc ở mục Câu hỏi mở thay vì để trống.

---

## Kết luận

**Bài KHÔNG đủ điều kiện `status: verified`.** Còn **1 BLOCKER** và **5 MAJOR**. Điều kiện là không còn BLOCKER và không còn MAJOR.

Điểm tích cực trước: **phần in-game text của bài rất chắc.** Bảy claim trích text SoD (C-01 → C-07) khớp **từng chữ** với wikitext thô, kể cả khoảng trắng đôi và các câu chêm khó bịa. Người viết đã đọc nguồn thật, không dựng lại từ trí nhớ. C-15 là ví dụ mẫu về cách xử lý một claim phủ định: nó không chỉ nói "không phải game text" mà chỉ ra được lỗi ngữ pháp làm dấu vết. Vấn đề của bài **không** nằm ở text SoD — nó nằm ở **phần HotA/template và ở kỷ luật gán source key**.

### Bắt buộc sửa — BLOCKER

1. **C-12 — `Black'n'Blue` bị đảo ngược ý nghĩa.** Đôi giày nằm trong `*Banned artifacts:` của template đó, **không** phải danh sách cho phép. Phải sửa thành "bị cấm". Sai này nặng vì nó nằm ngay cạnh `Apocalypse` (nơi đôi giày được cho phép) nên người đọc sẽ hiểu hai template cùng chiều trong khi chúng ngược chiều.
   Cùng claim, sửa luôn: (a) đổi source key — trang artifact 660 byte **không chứa** danh sách scenario nào, phải dẫn về chín trang scenario/template thật; (b) thêm `Viking We Shall Go! (Allies)`; (c) ghi rõ sản phẩm từng mục — **ba mục là HotA** (fan-made, không phải NWC) và **một mục là Heroes Chronicles**, hiện đang bị gộp phẳng vào danh sách trông như toàn SoD.

### Bắt buộc sửa — MAJOR

2. **C-09 — nâng tier, không hạ.** `T6 EXPLICIT` là **tổ hợp nhãn không hợp lệ** theo `CANON-POLICY.md` §2 (T6 tối đa `INFERENCE`). Và không cần dùng T6: `Talk:Artifact/descriptions` trên thelazy là bảng trích từ **`H3Bitmap.lod > artraits.txt`**, cùng loại với `h3wiki-herobios-txt` mà REGISTRY đã xếp **`T1`** thật. Thêm key mới (đề xuất `h3wiki-artraits-txt`, tier `T1`) rồi đổi nhãn thành `{T1 EXPLICIT: h3wiki-artraits-txt}`. **Đây là tiến triển trực tiếp cho `B-001` và dùng lại được cho mọi bài artifact khác** — giá trị vượt xa bài này.

3. **C-11 — claim trong thân bài không có nhãn**, vi phạm `CANON-POLICY.md` §5.1. Và khi gán thì **không được `EXPLICIT`**: không nguồn nào nói "đôi giày bằng hai cái kia cộng lại", đó là phép cộng của người viết. Đổi thành `{T1* INFERENCE: h3wiki-dead-mans-boots + h3wiki-amulet-of-the-undertaker + h3wiki-vampires-cowl — 5% + 10% = 15%}`.

4. **C-13 — mis-citation.** Text "Dead men tell no tales" nằm trên trang `Taming of the Wild`, không trên trang artifact. Cần source key mới (đề xuất `ab-taming-of-the-wild`, `T1*`). Sửa cả dấu câu: game để dấu chấm **ngoài** ngoặc (`tales".`).

5. **C-14 — "duy nhất" là suy luận, và changelog không chống lưng (vi phạm BH-3).** Nguồn viết "Allowed artifacts:" rồi liệt kê ba; nó không viết "only". Grep toàn bộ 201.529 byte changelog: `Apocalypse` xuất hiện **hai lần**, không lần nào là danh sách artifact. Trang luật chính thức `h3hota.com/en/rules` cũng **không có** danh sách artifact cho Apocalypse. Ngược lại, dòng **1.7.1** ("Apocalypse template: Wanderer's Boots and Shrines of Magical Mystery banned") là **bằng chứng ngược** cho cách đọc "chỉ ba artifact được phép". Hạ xuống `T6 INFERENCE`, **kèm phạm vi phiên bản** (trang sửa lần cuối 2025-05-14 ≈ HotA 1.7.2–1.7.3, **trước 1.8.0**), và ghi rõ changelog không xác nhận.

6. **C-17 — nhãn `UNVERIFIED` không được phép ở thân bài** (`CANON-POLICY.md` §5.3), và bản thân nhãn sai: câu trích đã xác minh từng chữ → `EXPLICIT`. Tách hai phần (câu trích = `EXPLICIT`; "game không giải thích" = `INFERENCE`, ghi rõ bước suy luận). Và bỏ chữ "**chỉ** nói" — **đây là BH-1 tái diễn**: block `=== Timed events ===` Day 4 có thêm text nối wizard giữ cổng với đôi giày ("according to Sandro, the Boots are in the possession of a Wizard south of here"), bài đã bỏ sót.

### Nên sửa — MINOR

7. **C-02** — tên campaign là **`New Beginning`**, không phải "A New Beginning". Ba nguồn cùng nói: trang campaign, danh sách trên trang `The Shadow of Death`, và **manual tr.14**.
8. **C-03** — trích thiếu câu "Do you wish to pick up the Boots?" mà không đánh dấu lược. Thêm `[…]` hoặc trích đủ.
9. **C-13** — dấu câu (đã nêu ở trên).

### Gợi ý làm bài mạnh hơn — NOTE

- **C-16 nên đổi từ phủ định trần sang có trích dẫn.** Game **tự** nói ra sự vô danh: "you thank the **anonymous donor**". Đó là chứng cứ dương cho việc nguồn gốc bị để trống *có chủ ý*, mạnh hơn hẳn "không nguồn nào kể". Kèm mảnh duy nhất về người **giữ** (Day 4, không phải người tạo).
- **C-11 có một điểm đáng viết mà bài chưa dùng:** quan hệ "một mình nó bằng hai cái kia" **bất biến qua phiên bản** — HotA 1.3.0–1.7.x chia đôi theo tỷ lệ (2,5 + 5 = 7,5), nên quan hệ vẫn đúng. Biến một phép cộng vụn thành nhận xét thiết kế.
- **C-13/C-12:** trong `Taming of the Wild`, **cả ba** thành phần Cloak nằm kề nhau — (67,3,0), (68,4,0), (69,4,0) — tất cả nhặt tự do, không lính canh. Map này cho ghép trọn Cloak of the Undead King gần như miễn phí. Đáng vào bài hơn câu "Dead men tell no tales".
- **C-14:** ba artifact được `Apocalypse` cho phép **chính là ba thành phần Cloak**, trên một template cấm Necropolis làm tộc khởi đầu, cấm toàn bộ hero Necropolis, và đặt mọi town trung lập thành Necropolis. Lựa chọn thiết kế có ý.
- **C-06:** seer đòi đúng 25 Ghost Dragons, bằng đúng stack Ghost Dragon canh giày — nhưng 25 con đó không lấy được từ đám lính canh, nên người chơi buộc phải chiếm Necropolis địch. Vòng lặp gameplay–narrative đáng nêu.
- **C-07:** phần epilogue bị bỏ có giá trị hơn phần đã trích — Gem tự loại giả thuyết "Sandro là người của Deyja" bằng lý lẽ kinh tế.

### Hai điểm cần sửa trong `REGISTRY.md` (ngoài phạm vi bài, nhưng phát hiện trong đợt này)

- **`hota-changelog` đang mang tier `T1*`, tức "in-game text qua trung gian" — sai loại.** Changelog là **văn bản phát hành của nhóm phát triển một expansion fan-made**, không phải text hiện ra khi chơi. Theo `CANON-POLICY.md` §2 nó gần `T4` (phát ngôn developer) hoặc `T6` (cộng đồng) hơn nhiều. Nội dung C-10 vẫn đúng và trích được nguyên văn, nên tôi không hạ verdict của C-10 vì việc này — nhưng key này đang được dùng cho "mọi claim về HotA" nên sai tier ở đây sẽ lan ra các bài sau. Nên xử lý riêng.
- **`heroesofmightandmagic.com` không phải "connection refused".** Registry ghi FAILED (connection refused) và suy ra "site chính thức của NWC, có thể đã chết". Thực tế trả **HTTP 403** với body `<title>Web Filter Violation</title>` — bị **filter mạng của môi trường** chặn, site có thể vẫn sống. Đây lại là một kết luận phủ định ("site đã chết") không đúng; nên sửa ghi chú để lần sau thử qua đường khác thay vì bỏ.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Ghi lại theo `VERIFY-PROTOCOL.md` mục 5. Cả sáu phát hiện BLOCKER/MAJOR đều được xử lý bằng
**sửa bài** hoặc **đưa nguồn mới**, không có mục nào bị phản hồi bằng trí nhớ.

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| C-12 | `Black'n'Blue` bị đảo ngược nghĩa | BLOCKER | Sửa thành **BỊ CẤM**. Bảng xuất hiện viết lại: thêm cột *Sản phẩm*, thêm `Viking We Shall Go! (Allies)`, mỗi dòng một source key riêng. Thêm cảnh báo hai template đi ngược chiều |
| C-09 | `T6 EXPLICIT` là tổ hợp nhãn không hợp lệ | MAJOR | **Nâng tier**, không hạ. Thêm `h3wiki-artraits-txt` (`T1` thật) vào REGISTRY, đổi nhãn. Bỏ `fandom-artifact-list` khỏi `sources_used` |
| C-11 | Claim thân bài không có nhãn | MAJOR | Gán `{T1* INFERENCE: ... — 5% + 10% = 15%}`, ghi rõ bước suy luận. Thêm nhận xét quan hệ bất biến qua phiên bản |
| C-13 | Mis-citation "Dead men tell no tales" | MAJOR | Thêm `ab-taming-of-the-wild` vào REGISTRY, đổi source key. Sửa dấu chấm ra ngoài ngoặc kép |
| C-14 | "duy nhất" là suy luận; changelog không chống lưng | MAJOR | Hạ xuống `T6 INFERENCE`. Thêm cả ba lý lẽ phản bác cách đọc "duy nhất", kèm phạm vi phiên bản (2025-05-14 ≈ 1.7.2–1.7.3) |
| C-17 | `UNVERIFIED` trong thân bài | MAJOR | Tách hai nhãn: câu trích = `EXPLICIT`, nhận định vắng mặt = `INFERENCE`. Bỏ chữ "chỉ nói". Thêm timed event Day 4 (BH-1) |
| C-03 | Trích thiếu câu, không đánh dấu lược | MINOR | Trích đủ câu "Do you wish to pick up the Boots?" |
| C-16 | Claim phủ định trần | NOTE | Viết lại theo hướng chứng cứ dương ("anonymous donor"), kèm mảnh Day 4 về **người giữ** |
| C-15 | — | CONFIRMED | Củng cố thêm: nêu đủ ba bằng chứng, và ghi rõ ba wiki là **fork**, không phải ba nguồn |

### Đính chính một phát hiện của verifier — C-02

**C-02 (MINOR, tên campaign "A New Beginning") không phải lỗi của bài.**

Verifier đúng rằng tên campaign là `New Beginning`, không có mạo từ "A". Nhưng chuỗi "A New
Beginning" **không tồn tại trong bài** — nó do người soạn bảng claim thêm vào khi diễn giải, và
verifier chỉ thấy bảng claim chứ không thấy bài. Kiểm lại toàn bộ `docs/codex/`: mọi chỗ đều ghi
`New Beginning` đúng, và `REGISTRY.md` cũng vậy.

⭐ **Đáng ghi lại vì nó là hạn chế cấu trúc của chính luồng verify**, không phải sơ suất một lần:
verifier bị cấm đọc bài gốc, nên nó **không phân biệt được** lỗi của bài với lỗi của bảng claim.
Mọi diễn giải người soạn bảng thêm vào đều trở thành claim mà verifier tưởng là của bài.

**Quy tắc rút ra cho các đợt sau:** bảng claim phải **trích nguyên văn** từ bài, không được diễn
giải hay thêm ngữ cảnh. Nếu cần thêm ngữ cảnh để claim đọc được, phải đánh dấu rõ phần nào là
ngữ cảnh của người soạn.

### Hai việc ngoài phạm vi bài — đã chuyển tiếp

- **`heroesofmightandmagic.com` không phải "site đã chết"** → đã sửa ghi chú trong `REGISTRY.md`
  Nhóm 3 thành `403 web filter`. Đây lại là một **kết luận phủ định sai**, đúng loại lỗi mà
  `CLAUDE.md` xếp là nguy hiểm nhất.
- **`hota-changelog` đang mang tier `T1*` — sai loại nguồn.** Changelog là văn bản phát hành của
  nhóm phát triển một expansion fan-made, không phải in-game text. Ảnh hưởng nhiều bài nên
  **không** sửa trong đợt này; đã ghi thành `B-018` trong `BACKLOG.md`.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-dead-mans-boots-2026-08-03`.

Không còn BLOCKER, không còn MAJOR. `check.py` 0 lỗi.
