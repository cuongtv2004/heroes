# Verify report: amulet-of-the-undertaker — 2026-08-03

Verifier: agent độc lập, không đọc bài gốc, không đọc `docs/sources/raw/`, không đọc các bài
cùng cụm, không đọc báo cáo verify `dead-mans-boots`.

Số claim kiểm: 19
CONFIRMED: 16 | DOWNGRADE: 1 | NOT_FOUND: 1 | CONTRADICTED: 1

Mức: **BLOCKER: 4** (C-06, C-09, C-17, C-18) · **MAJOR: 2** (F-1, F-2) · MINOR: 10 · NOTE: 11

---

## Nguồn đã fetch trong đợt này

Toàn bộ lấy bằng `curl ... ?action=raw` (wikitext thô), không qua tóm tắt.

| Nguồn | URL | Byte |
|---|---|---|
| Trang artifact | `heroes.thelazy.net/index.php?title=Amulet_of_the_Undertaker&action=raw` | 672 |
| Scenario `After the Amulet` — **đọc toàn bộ** | `...?title=After_the_Amulet&action=raw` | 12.404 |
| `Talk:Artifact/descriptions` (artraits.txt) | `...?title=Talk:Artifact/descriptions&action=raw` | 16.129 |
| `Artifact Events` | `...?title=Artifact_Events&action=raw` | 35.645 |
| HotA changelog | `...?title=Horn_of_the_Abyss_(Changelog)&action=raw` | 201.529 |
| `Taming of the Wild` | `...?title=Taming_of_the_Wild&action=raw` | 7.936 |
| `Beyond the Horizon` | `...?title=Beyond_the_Horizon&action=raw` | 57.255 |
| `Tomb Raiders` | `...?title=Tomb_Raiders&action=raw` | 117.073 |
| `Frontier` | `...?title=Frontier&action=raw` | 24.189 |
| `Apocalypse` (template) | `...?title=Apocalypse&action=raw` | 1.335 |
| `Nine-day Wonder` (template) | `...?title=Nine-day_Wonder&action=raw` | 2.348 |
| `New Beginning` (campaign) | `...?title=New_Beginning&action=raw` | 3.732 |
| `Vampire's Cowl` / `Dead Man's Boots` / `Cloak of the Undead King` | idem | 913 / 660 / 2.158 |
| `Artifact` (mục Class) · `Treasure Chest` · `Necromancy` | idem | 7.175 / 1.288 / 6.646 |
| `Template:Cram2` · `Template:CampaignHero` | idem | — |
| Backlinks (193 trang) | `api.php?action=query&list=backlinks&bltitle=Amulet of the Undertaker&bllimit=500` | — |
| Fandom `Amulet of the Undertaker` | `mightandmagic.fandom.com/api.php?action=parse&page=...&prop=wikitext` | 666 |
| Fandom `List of Heroes IV artifacts` | idem | 39.065 |
| Fandom `Prelude to Invasion` | idem | — |
| `Horn of the Abyss/Team Interview (2024)` | `...?title=Horn_of_the_Abyss/Team_Interview_(2024)&action=raw` | 51.274 |

**BH-2 (kiểm disambiguation trước claim phủ định):** đã làm. `api.php` search `Undertaker` trên
thelazy trả về **đúng một** trang (`Amulet of the Undertaker`) → không có trang trùng tên. Trên
Fandom, search `Undertaker` trả về thêm **`Amulet of Necromancy`** — artifact **khác**, không được
gộp.

**BH-1 (đọc cả block Events):** đã đọc **toàn bộ** 12.404 byte của `After the Amulet` — 13 timed
event, block `==== Events ====`, Towns, Town timed events, Heroes, Monsters, Artifacts, Resources,
`{{user commentary}}`. Trang **không có** section Epilogue.

**BH-3 (HotA dùng changelog):** đã grep toàn bộ 201.529 byte cho `Undertaker`, `Necromancy`,
`Apocalypse`, `reduced by half`. Đã xác định version header đứng trước từng dòng bằng số dòng.

---

## Chi tiết

### C-01
Claim: Amulet là thành phần **rẻ nhất và yếu nhất** của Cloak of the Undead King, và là món
**duy nhất** trong ba thành phần thuộc hạng **Treasure**.
Nhãn bài gán: (không gán nhãn, không source key)
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở:
- `heroes.thelazy.net/index.php?title=Amulet_of_the_Undertaker&action=raw`
- `...?title=Vampire's_Cowl&action=raw`
- `...?title=Dead_Man's_Boots&action=raw`
- `...?title=Cloak_of_the_Undead_King&action=raw`
- `...?title=Artifact&action=raw` (mục `== Class ==`)

Tìm thấy — cả **ba** thành phần, từ infobox `ArtifactNewSB`:

```
Amulet of the Undertaker:  class = Treasure | slot = Necklace | cost = 2000 | effect = +5%  Necromancy
Vampire's Cowl:            class = Minor    | slot = Cape     | cost = 4000 | effect = +10% Necromancy
Dead Man's Boots:          class = Major    | slot = Feet     | cost = 6000 | effect = +15% Necromancy
```

Đúng ba thành phần, từ `CombinationArtifactNewSB` của Cloak:

```
| art_1   = Amulet of the Undertaker
| art_2   = Vampire's Cowl
| art_3   = Dead Man's Boots
```

Thứ bậc hạng, trang `Artifact`:

> "Artifacts are split into 4 categories roughly rating their power and usefulness. […] The 4
> classes are Treasure, Minor, Major, and Relic. Their AI values are 2000, 5000, 10000 and 20000
> respectively."

Lý do: cả **ba** thành phần của claim đứng vững — 2000 là giá thấp nhất, +5% là hiệu ứng yếu
nhất, và Treasure là hạng duy nhất không lặp lại (Cowl = Minor, Boots = Major). Hạng Treasure là
hạng **thấp nhất** trong bốn hạng, có nguồn trực tiếp.

Mức MINOR vì **hai** lỗi hình thức, không phải lỗi nội dung:
1. Claim so sánh ba entity mà **không có nhãn và không có source key** → vi phạm
   `CANON-POLICY.md` §5.1. Cần `{T1* EXPLICIT: h3wiki-amulet-of-the-undertaker + h3wiki-vampires-cowl
   + h3wiki-dead-mans-boots}`, và thứ bậc hạng cần một key mới cho trang `Artifact`.
2. Ba từ so sánh nhất ("rẻ nhất", "yếu nhất", "duy nhất") **không ghi phạm vi game**. Xem **F-1**:
   ở Heroes IV, Amulet là **Minor** artifact và cho **+10%** Necromancy — cả hạng và con số đều
   khác. Câu phải mở đầu bằng "Trong Heroes III…".

---

### C-02
Claim: Không nguồn nào kể ai tạo ra nó.
Nhãn bài gán: (claim phủ định, không nhãn)
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: trang artifact; `Cloak of the Undead King`; `Talk:Artifact/descriptions`;
`Artifact Events`; **toàn bộ 193 backlinks** qua `api.php?action=query&list=backlinks`; Fandom
`Amulet of the Undertaker`; Fandom `List of Heroes III artifacts`; Fandom
`List of Heroes IV artifacts`; `Beyond the Horizon`; `Tomb Raiders`; `Necromancy`.

Tìm thấy — **không** nguồn nào nêu tên người tạo. Nhưng tìm được thứ **tốt hơn** một claim phủ
định: game text **chủ động từ chối** nêu tên. `Beyond_the_Horizon`, thoại Seer's Hut (2, 27, 0),
nói về đúng nhóm artifact có chứa Amulet:

> "We believe that these lands have been home to cursed artifacts since the last century. Their
> creator was... Bah, that doesn't matter. What does, is that these artifacts must be found and
> destroyed before they fall into the hands of the Necromancer's Guild."

Lý do: claim phủ định này sống sót — đây là loại claim đợt nào cũng phải soi mạnh nhất, và lần
này nó đúng. Nhưng **đừng để nó ở dạng phủ định không nhãn.** Câu trên biến "dự án không tìm
được" thành "game text cố ý bỏ trống", là một khẳng định mạnh hơn và **có nguồn**. Đề xuất viết
lại thành `{T1* EXPLICIT: hota-beyond-the-horizon — game text nêu artifact có người tạo nhưng cắt
ngang không nói tên}`, kèm ghi chú `Beyond the Horizon` là scenario **HotA (fan-made, không phải
NWC)** — cùng cách xử lý registry đã dùng cho `hota-dead-or-alive`.

Lưu ý: câu này nói về "cursed artifacts" của quest đó = Skull Helmet, Rib Cage, Amulet of the
Undertaker, Vampire's Cowl — tức phủ **cả** Amulet, nhưng là phát ngôn về **nhóm**, không riêng
Amulet. Phải viết đúng phạm vi đó.

---

### C-03
Claim: Text khi nhặt — "A dirty amulet lies next to a freshly dug grave. Upon investigation, you
discover it to be the enchanted Amulet of the Undertaker, long thought lost by mortals."
Nhãn bài gán: `T1* EXPLICIT: h3wiki-amulet-of-the-undertaker`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `...?title=Amulet_of_the_Undertaker&action=raw` (trường `event` của infobox) và — độc
lập — `...?title=Artifact_Events&action=raw`

Tìm thấy, trường `event` trên trang artifact:

```
 | event  = A dirty amulet lies next to a freshly dug grave. Upon investigation, you discover it to be the enchanted Amulet of the Undertaker, long thought lost by mortals.
```

Và trên trang `Artifact Events` (tự mô tả đầu trang: "Default descriptions when picking an
artifact."), dòng 107:

```
{{An|Amulet of the Undertaker}}: A dirty amulet lies next to a freshly dug grave. Upon investigation, you discover it to be the enchanted [[Amulet of the Undertaker]], long thought lost by mortals.
```

Lý do: khớp **từng chữ**, kể cả dấu chấm. Nhãn `T1* EXPLICIT` đúng cấp và đúng độ chắc.
NOTE: nên thêm `h3wiki-artifact-events` làm nguồn xác nhận **độc lập** (registry đã có key này) —
hai trang khác nhau trên cùng wiki chép ra cùng một chuỗi là bằng chứng mạnh hơn một trang.

---

### C-04
Claim: Đây là món **đầu tiên** Sandro sai Gem đi lấy. Text: "You have agreed to help a wizard's
apprentice named Sandro. Sandro's master, Ethric, needs an Amulet of the Undertaker to perform
anti-necromancy research, but Ethric is an academician and Sandro is too inexperienced to go after
the Amulet himself."
Nhãn bài gán: `T1* EXPLICIT: sod-after-the-amulet`
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `...?title=After_the_Amulet&action=raw` (trường `region_text`) và
`...?title=New_Beginning&action=raw`

Tìm thấy, `region_text`:

```
| region_text    = You have agreed to help a wizard's apprentice named [[Sandro]].  Sandro's master, [[Ethric]], needs an [[Amulet of the Undertaker]] to perform anti-necromancy research, but Ethric is an academician and Sandro is too inexperienced to go after the Amulet himself.
```

Trích khớp nguyên văn (lưu ý bản gốc dùng **hai** dấu cách sau dấu chấm — đặc trưng của chuỗi
game, không phải văn wiki).

Về chữ "**đầu tiên**": text trích **không** chứa từ đó. Nhưng có hai nguồn chống lưng:
- Campaign `New Beginning` gồm 4 map, theo đúng thứ tự: `Clearing the Border` → **`After the
  Amulet`** → `Retrieving the Cowl` → `Driving for the Boots`. Map 1 không liên quan artifact →
  Amulet là artifact đầu tiên.
- `After the Amulet`, timed event **Day 21**, thư Sandro: "Sandro offered me more gold to find the
  other two artifacts **once I locate the Amulet**."

Lý do: nội dung đúng, nhãn đúng cấp. Mức MINOR vì bộ phận "đầu tiên" là **claim thứ tự** không
nằm trong đoạn trích đang được dẫn — phải bổ sung key cho trang campaign `New Beginning` (chưa có
trong registry) hoặc dẫn thẳng thư Day 21.

---

### C-05
Claim: Amulet nằm tại (39, 8, 0). Text: "Buried under the gems and gold of the Ghost Dragons'
hoard you find the Amulet of the Undertaker."
Nhãn bài gán: `T1* EXPLICIT: sod-after-the-amulet`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `...?title=After_the_Amulet&action=raw`, section `==== Artifacts ====`

Tìm thấy:

```
| style="text-align:center;" | 39, 8, 0
| ... | {{An|Amulet of the Undertaker}}
| ... | Buried under the gems and gold of the [[Ghost Dragon|Ghost Dragons]]' hoard you find the [[Amulet of the Undertaker]].
```

Lý do: toạ độ và nguyên văn khớp chính xác.

---

### C-06
Claim: Ô chứa Amulet **không có lính canh nào**. Việc canh giữ do một stack Ghost Dragon **liền
kề** tại (38, 8, 0) đảm nhiệm — và **số lượng không được nêu**.
Nhãn bài gán: `T1* EXPLICIT: sod-after-the-amulet`
Phán quyết: **NOT_FOUND**
Mức: **BLOCKER**
Đã tìm ở:
- `...?title=After_the_Amulet&action=raw` — toàn bộ trang
- `...?title=Taming_of_the_Wild&action=raw` — section `==== Artifacts ====` (đối chiếu format)
- `...?title=Beyond_the_Horizon&action=raw` — section `==== Artifacts ====` (đối chiếu format)
- `...?title=Template:Cram2&action=raw` — kiểm template có tham số số lượng hay không

Tìm thấy — **ba bộ phận của claim có ba số phận khác nhau:**

**(a) Stack Ghost Dragon tại (38, 8, 0): CONFIRMED.** Section `==== Monsters ====`:

```
| style="text-align:center;" | 38, 8, 0
| ... | {{Cram2|Ghost Dragon}}
| ... | Despite the pleasant surroundings, the unmistakable odor of death permeates the area.  You see a group of [[Ghost Dragon|Ghost Dragons]] ahead.
```

**(b) "Số lượng không được nêu": CONFIRMED.** `Template:Cram2` **không có tham số số lượng nào** —
`<includeonly>[[File:{{{1}}}...gif|...]]{{-}}{{{0|[[{{{2|{{{1}}}}}}|{{{name|{{{1}}}}}}]]}}}</includeonly>`,
tự mô tả là "Template for monsters' appearance on the Adventure Map." Bảng Monsters cũng chỉ có
ba cột `Location / Type / Message`. Trang **về mặt cấu trúc không thể** ghi số lượng.

**(c) "Ô chứa Amulet không có lính canh nào": KHÔNG CÓ NGUỒN.** Bảng `==== Artifacts ====` trên
thelazy có **đúng ba cột** `Location / Type / Message` và **không có trường guardian nào**. Đã
đối chiếu ba scenario khác nhau (`After the Amulet`, `Taming of the Wild`, `Beyond the Horizon`) —
format y hệt. Nghĩa là bảng này **không thể** ghi lính canh **dù có hay không có**. So sánh: bảng
`==== Events ====` của cùng trang **có** ghi, ngay trong cột Message: `'''Guardians:''' 20 …`.

Lý do — đây đúng là loại lỗi mà bảng claim cảnh báo, và nó là **BLOCKER**:

1. `T1* EXPLICIT` đòi trích được câu chống lưng (`CANON-POLICY.md` §2, trục B). **Không có câu
   nào** nói ô (39, 8, 0) không có lính canh. Suy ra từ **im lặng của một format vốn luôn im lặng
   về việc đó** là suy luận không hợp lệ — nó sẽ cho ra kết luận "không lính canh" cho **mọi**
   artifact trên **mọi** scenario page của thelazy.
2. Bộ phận "việc canh giữ do stack liền kề đảm nhiệm" là **diễn giải chức năng từ vị trí liền
   kề**, không phải điều nguồn nói. Tối đa là `INFERENCE`, và phải ghi rõ bước suy luận.
3. Đúng như bảng claim dự đoán: claim phủ định + claim độc quyền là chỗ hỏng. "Không có lính canh
   nào" **trông giống sự cẩn trọng** (nó thừa nhận một sự thiếu) nhưng thực chất là một khẳng định
   về map file mà dự án **không có** để đối chiếu.

**Phải sửa:** giữ (a) và (b) ở `T1* EXPLICIT`; chuyển (c) thành `INFERENCE` với bước suy luận ghi
rõ, hoặc — tốt hơn — bỏ hẳn câu "không có lính canh nào" và viết theo hướng khẳng định: *artifact
nằm tại (39, 8, 0), sát ngay stack Ghost Dragon tại (38, 8, 0); trang nguồn không ghi lính canh
riêng cho ô artifact và không ghi số lượng Ghost Dragon*. Câu đó nói đúng những gì nguồn nói và
không hơn.

---

### C-07
Claim: Có một **event phục kích** tại (32, 5, 0) với 20 Bone Dragon + 20 Ghost Dragon + 20 Bone
Dragon. Stack 60 con đó **không phải** lính canh artifact.
Nhãn bài gán: `T1* EXPLICIT: sod-after-the-amulet`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `...?title=After_the_Amulet&action=raw`, section `=== Objects === / ==== Events ====`

Tìm thấy, nguyên văn dòng duy nhất trong block Events:

```
{{Erow| {{green}} 32, 5, 0 | Suddenly, the smell of death is overwhelming.  "Ambush!" screams one of your troops, pointing at the sky.<p><center>'''Guardians:''' 20 {{Cn|Bone Dragon|name=Bone Dragons}}, 20 {{Cn|Ghost Dragon|name=Ghost Dragons}}, 20 {{Cn|Bone Dragon|name=Bone Dragons}}<p>'''Contents:''' {{Morale|+2}}</center></p>}}
```

Lý do: toạ độ, ba stack và thứ tự lạ (Bone Dragon xuất hiện **hai lần**, ở stack 1 và stack 3) đều
khớp chính xác — dấu hiệu bài đã chép từ nguồn chứ không viết lại từ trí nhớ. Từ "phục kích" có
nguồn: `"Ambush!" screams one of your troops`.

Claim phân biệt "**không phải** lính canh artifact" đứng vững ở mức explicit: đây là entry trong
block `==== Events ====` tại **(32, 5, 0)**, còn artifact ở **(39, 8, 0)** trong block
`==== Artifacts ====` — hai object khác nhau, hai ô khác nhau, hai bảng khác nhau. Đây là claim
phân biệt **đúng**, và nó có ích: 60 con dragon dễ bị nhầm thành lính canh artifact.

NOTE: nên ghi thêm `Contents: Morale +2` — đó là phần thưởng của event, và nó chứng minh thêm rằng
event này là một object độc lập có nội dung riêng, không phải guard.

---

### C-08
Claim: Thông số gốc — slot = Necklace; class = **Treasure**; giá = 2.000; hiệu ứng = **+5%
Necromancy**.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-amulet-of-the-undertaker`
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `...?title=Amulet_of_the_Undertaker&action=raw`

Tìm thấy, toàn bộ infobox:

```
{{ArtifactNewSB
 | class  = Treasure
 | slot   = Necklace
 | cost   = 2000
 | event  = A dirty amulet lies next to a freshly dug grave. ...
 | effect = +5% {{gl|Necromancy}}
}}
```

Xác nhận độc lập cho +5% từ trang `Necromancy`, mục "Related factors":
`* {{an|Amulet of the Undertaker}}: +5% Necromancy`.

Lý do: bốn thông số khớp chính xác. Mức MINOR vì chữ "**gốc**" cần định nghĩa rõ **gốc của bản
nào**: theo C-11 con số này là 2,5% trong HotA 1.3.0–1.7.x, và theo **F-1** là +10% ở Heroes IV.
`SCHEMA.md` bắt tách *Cơ chế gốc* khỏi *Thay đổi qua các bản* chính vì việc này — mục "Cơ chế
gốc" phải nói rõ "Shadow of Death / RoE / AB".

---

### C-09
Claim: Mô tả in-game — "Worn about the neck, this amulet increases your Necromancy skill by 5%."
Nhãn bài gán: **`T6 EXPLICIT: fandom-artifact-list`**
Phán quyết: **DOWNGRADE** (nhãn sai loại — và đồng thời cấp nguồn bị đặt **quá thấp**)
Mức: **BLOCKER**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Talk:Artifact/descriptions&action=raw` và
`mightandmagic.fandom.com/api.php?action=parse&page=Amulet of the Undertaker&prop=wikitext`

Tìm thấy — `Talk:Artifact/descriptions` tự khai nguồn ở caption đầu bảng:

```
|+ style="white-space:nowrap;"|Information from H3Bitmap.lod > artraits.txt{{---}}
```

và dòng 113 của bảng đó:

```
| [[Amulet of the Undertaker]] || Worn about the neck, this amulet increases your Necromancy skill by 5%.
```

Fandom (`fandom-artifact-list`) chép **y hệt từng chữ**: "Worn about the neck, this amulet
increases your Necromancy skill by 5%."

Lý do — **hai lỗi độc lập, cả hai đều là BLOCKER:**

1. **`T6 EXPLICIT` là tổ hợp nhãn không hợp lệ.** `CANON-POLICY.md` §2 nói thẳng: "Nếu một claim
   chỉ có T6 chống lưng, nó tối đa là `INFERENCE` hoặc `UNVERIFIED`." Không có ngoại lệ nào cho
   trường hợp trích nguyên văn. Xác nhận: phát hiện #1 của đợt `dead-mans-boots` **áp dụng đúng**
   cho bài này.
2. **Có nguồn `T1` thật và bài không dùng.** `h3wiki-artraits-txt` đã có trong registry với tier
   `T1` (không dấu sao) vì nó là **string table trích từ file game**, không phải bản chép do người
   viết lại. Bảng đó **có** dòng cho Amulet of the Undertaker — tôi đã trích ở trên. Nghĩa là claim
   này không cần T6 chút nào.

**Phải sửa thành:** `{T1 EXPLICIT: h3wiki-artraits-txt}`. Có thể giữ `fandom-artifact-list` như
nguồn xác nhận trùng khớp, nhưng nó không được là nguồn chính. Đây là claim **duy nhất** trong
bảng mà việc sửa nhãn làm bài **mạnh lên**: nó nâng một dòng từ T6 lên `T1` thật, đúng hướng
`B-001`.

---

### C-10
Claim: Vì là hạng Treasure (hạng thấp nhất), Amulet có thể xuất hiện từ Treasure Chest. Trích:
"If you are lucky enough, you can win this scenario by opening Treasure Chests. That's because
Amulet of the Undertaker is a treasure."
Nhãn bài gán: `T6 FAN_THEORY: sod-after-the-amulet` (bài ghi rõ: nằm trong `{{user commentary}}`)
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `...?title=After_the_Amulet&action=raw` (cuối trang) và `...?title=Treasure_Chest&action=raw`

Tìm thấy, nguyên văn khối cuối trang scenario:

```
{{user commentary|
If you are lucky enough, you can win this scenario by opening [[File:Treasure_Chest.gif]] [[Treasure Chest|Treasure Chests]]. That's because {{An|Amulet of the Undertaker}} is a [[treasure]].
}}{{end of user commentary}}
```

Lý do: trích khớp, và mô tả của bài về vị trí văn bản (**trong** `{{user commentary}}`) là **đúng**
— bài đã cẩn thận đúng chỗ cần cẩn thận.

Mức MINOR vì `FAN_THEORY` **đặt quá thấp** cho phần cơ chế. `FAN_THEORY` theo `CANON-POLICY.md` §2
nghĩa là "Không có nguồn T1–T4 chống lưng". Nhưng cơ chế ở đây **có** nguồn, và tôi trích được.
Trang `Treasure Chest`:

> "It gives either gold for the kingdom, experience or an artifact for the hero. […] If the chest
> contains an artifact, the player receives no choice but **a random treasure class artifact** is
> put in the hero's backpack."

kèm bảng xác suất: `5% || [[Artifact]]`. Cộng với C-08 (Amulet **là** hạng Treasure) và điều kiện
thắng của scenario (`victory = Acquire Artifact Amulet of the Undertaker`), chuỗi suy luận hoàn
toàn truy được về nguồn.

**Nên tách hai thứ đang bị gộp:**
- *Cơ chế* — Treasure Chest có 5% cho ra một artifact hạng Treasure ngẫu nhiên, và Amulet thuộc
  hạng đó → `{T1* INFERENCE: h3wiki-treasure-chest + h3wiki-amulet-of-the-undertaker}`. Cái này
  được vào thân bài.
- *Lời khuyên chiến thuật* — "you can win this scenario by opening Treasure Chests" → vẫn là
  `{T6 FAN_THEORY: sod-after-the-amulet}`, vẫn ở mục riêng theo §5.5, vì không nguồn nào xác nhận
  scenario này thực sự sinh Treasure Chest (trang scenario **không** liệt kê object đó).

---

### C-11
Claim: SoD gốc **+5%**; HotA 1.3.0 → 1.7.x = **+2,5%**; HotA 1.8.0 trở đi khôi phục **+5%**.
Nhãn bài gán: `T1* EXPLICIT: hota-changelog`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Horn_of_the_Abyss_(Changelog)&action=raw` —
201.529 byte, grep toàn file

Tìm thấy — dòng 2005, dưới header `== Version 1.3.0 (01/JAN/2014) ==` (dòng 1966):

> "[+] The number of Skeletons raised by necromancy is reduced by half, as well as bonuses to it
> from artifacts and a Necromancy Amplifier"

và dòng 31, dưới header `== Version 1.8.0 (31/DEC/2025) ==` (dòng 7):

> "[-] 5/10/15/30% Necromancy boost values are back for the **Amulet of the Undertaker**, Vampire's
> Cowl, Dead Man's Boots, and Cloak of the Undead King (instead of 2.5/5/7.5/15%)"

Lý do: cả ba mốc đứng vững, và tôi đã đóng lỗ hổng còn lại — grep `Necromancy` (không phân biệt
hoa thường) trên **toàn bộ** 201.529 byte cho ra **10 dòng**, và ngoài hai dòng trên **không dòng
nào** đổi giá trị bonus của artifact. Tám dòng còn lại là: sửa bug Fangarm quick-battle (1.7.x),
sửa AI đếm Necromancy Amplifier, AI raise creature nâng cấp, crash khi map chỉ có 4 skill, đổi
cách tính theo tổng quân bị giết, bug AI-vs-AI raise 1 skeleton, University không dạy necromancy,
và bug Witch Hut. Không cái nào chạm vào con số của Amulet.

Nghĩa là cửa sổ **1.3.0 → 1.7.x = 2,5%** không bị dòng nào cắt ngang. Xác nhận: cảnh báo
"Giá trị Necromancy ĐÃ ĐỔI qua các bản HotA" trong registry **áp dụng đúng** cho artifact này, với
con số riêng của nó (5% → 2,5% → 5%).

---

### C-12
Claim: Dòng changelog 1.3.0 chỉ nói "reduced by half" — **không nêu tên artifact này và không nêu
con số**. Giá trị 2,5% chỉ được **chứng thực hồi cố** qua dòng 1.8.0.
Nhãn bài gán: `T1* INFERENCE: hota-changelog`
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: cùng nguồn C-11, dòng 2005 và dòng 31

Tìm thấy: dòng 1.3.0 nguyên văn là "…as well as bonuses to it from **artifacts** and a Necromancy
Amplifier" — nói "artifacts" ở dạng chung, **không** tên riêng nào, **không** con số nào. Đúng.

Lý do: claim đúng và nhãn `INFERENCE` đúng — bước suy luận (5% chia đôi = 2,5%, hiệu lực từ 1.3.0)
là suy luận thật, không phải trích dẫn.

Mức MINOR vì một chi tiết diễn đạt **dễ gây hiểu sai theo chiều tự hạ thấp**: câu "chứng thực hồi
cố" có thể đọc thành "con số 2,5% chỉ là suy ra". Không phải. Dòng 1.8.0 **nêu thẳng tên** "Amulet
of the Undertaker" **và nêu thẳng** "(instead of 2.5/5/7.5/15%)". Nên bản thân **con số 2,5% cho
đúng artifact này là `EXPLICIT`**; chỉ **mốc bắt đầu là 1.3.0** mới là `INFERENCE`. Đề xuất tách
làm hai claim thay vì gộp:
- giá trị pre-1.8.0 của Amulet = 2,5% → `{T1* EXPLICIT: hota-changelog}`
- mốc bắt đầu = 1.3.0 → `{T1* INFERENCE: hota-changelog — dòng 1.3.0 chia đôi bonus artifact nói
  chung; không dòng nào giữa 1.3.0 và 1.8.0 đổi lại}`

---

### C-13
Claim: Trong `Taming of the Wild`: nhặt tự do, text riêng "A strange man dressed in black throws an
amulet to you, bows and then vanishes."
Nhãn bài gán: `T1* EXPLICIT: h3wiki-amulet-of-the-undertaker`
Phán quyết: **CONFIRMED** (nội dung) — nhưng source key sai, xem **F-2**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Taming_of_the_Wild&action=raw`, section
`==== Artifacts ====`

Tìm thấy:

```
| style="text-align:center;" | 68, 4, 0
| ... | {{An|Amulet of the Undertaker}}
| ... | A strange man dressed in black throws an amulet to you, bows and then vanishes.
```

Ba thành phần Cloak nằm kề nhau đúng như registry đã ghi: Boots (67, 3, 0) — "A note on the boots
reads: 'Dead men tell no tales'.", Amulet (68, 4, 0), Cowl (69, 4, 0) — "It looks like a careless
vampire left this lying about."

Lý do: nguyên văn khớp chính xác. "Nhặt tự do" đúng ở mức nguồn cho phép nói (bảng Artifacts không
ghi lính canh) — nhưng lưu ý **cùng cái bẫy của C-06**: format bảng vốn không ghi lính canh, nên
"tự do" ở đây cũng là suy luận, không phải trích. Vì đây là mô tả phụ chứ không phải claim trung
tâm, tôi để MINOR chứ không BLOCKER — nhưng phải xử lý nhất quán với C-06.

Mức MINOR chủ yếu vì source key: nội dung này **không nằm** trên trang artifact (xem F-2). Key
đúng là `ab-taming-of-the-wild`, **đã có trong registry** và entry của nó thậm chí đã ghi sẵn toạ
độ (68, 4, 0).

---

### C-14
Claim: Trong `Beyond the Horizon`: một trong **bốn** artifact Seer's Hut đòi → phần thưởng Golden
Bow.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-amulet-of-the-undertaker`
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Beyond_the_Horizon&action=raw`, section
`==== Seer's Huts ====`, Seer's Hut tại (2, 27, 0)

Tìm thấy — con số **bốn** đúng, và đây là danh sách đầy đủ:

```
{{SorQrow|seer=1|loc=2, 27, 0|quest=Return with:<br>{{An|Skull Helmet}}<br>{{An|Rib Cage}}<br>{{An|Amulet of the Undertaker}}<br>{{An|Vampire's Cowl}}</br>|rew={{An|Golden Bow}}| ...
```

Text hoàn thành quest, nguyên văn:

> "The priest takes a long look at each of the artifacts, and finally speaks: 'You have been of
> invaluable help to our Temple. I will hand the artifacts over to my brethren immediately. We will
> make sure that they not harm anyone else. As for the reward... Take this Golden Bow.'"

Lý do: đếm được **đúng bốn** `{{An|…}}` trong trường `quest`: Skull Helmet, Rib Cage, Amulet of the
Undertaker, Vampire's Cowl. Phần thưởng Golden Bow khớp. Bảng claim yêu cầu kiểm con số 4 — kiểm
rồi, đúng.

Chi tiết đáng chú ý: **bốn artifact này thuộc hai** combination artifact khác nhau — Amulet + Cowl
là thành phần Cloak of the Undead King, còn Skull Helmet + Rib Cage là thành phần **Armor of the
Damned**. Bài nên nói rõ, vì "bốn artifact Seer's Hut đòi" dễ bị đọc thành bốn thành phần của cùng
một combo.

Mức MINOR vì hai điều:
1. Source key sai (F-2). Cần key mới, ví dụ `hota-beyond-the-horizon`.
2. **Bài không ghi đây là scenario HotA.** Trang mở đầu bằng `{{inhota}}` và có `source = hota`,
   thuộc campaign `Forged in Fire`. Registry đã có tiền lệ bắt ghi rõ điều này
   (`hota-dead-or-alive`: "Scenario **HotA** (fan-made, không phải NWC)"). C-15 được ghi "(HotA)"
   nhưng C-14 và C-16 thì không — không nhất quán.

---

### C-15
Claim: Trong `Tomb Raiders` (HotA): Seer's Hut **lặp lại** → +1 primary skill; và Quest Guard cần
nó để sửa Skeleton Transformer.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-amulet-of-the-undertaker`
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Tomb_Raiders&action=raw` (117.073 byte)

Tìm thấy — Seer's Hut tại (16, 172, 0), tham số `rpt=y` (repeatable):

```
{{SorQrow|seer=1|loc=16, 172, 0|rpt=y|quest=Return with:<br>{{An|Amulet of the Undertaker}}|rew=+1 {{Ps|Attack}} or +1 {{Ps|Defense}} or<br>+1 {{Ps|Power}} or +1 {{Ps|Knowledge}}|prop=Long ago, powerful wizards were able to create magical artifacts, but time has caused us to forget how to make new items.  I would like to learn these techniques myself, but I need one of these artifacts first to see how it was done.  If you could bring me, the Amulet of the Undertaker, you would be well rewarded.|comp=Ah, exactly what I needed!  Here is the reward I promised.  You still wish to trade the Amulet of the Undertaker, yes?}}
```

Và Quest Guard tại (12, 178, 0), tham số `guard=1`:

> "A black-cloaked vampire watchman stands at the entrance to the Transformer, eyeing your army with
> suspicion. 'You're looking for a new way to replenish your army, aren't you?', smirks the vampire.
> 'Forget it! The Transformer was broken by giant worms, and now it doesn't work. We might be able
> to get it chugging again, though, if you could find a strong enough artifact.'"

Text hoàn thành: "'All right!', the vampire rubs his skinny hands. 'This amulet will help us restore
the Transformer, so it can work again!'"

Lý do: cả hai bộ phận đúng, xác nhận bằng nguyên văn. `rpt=y` là bằng chứng cơ chế cho "lặp lại".
Lưu ý phụ có ích: changelog 1.8.0 có dòng "[-] The AI no longer desires to obtain unlimited
identical artifacts from reusable Seer Hut quests" — chính là loại quest này, và là bằng chứng độc
lập rằng Seer's Hut lặp lại tồn tại như một cơ chế thật.

Mức MINOR vì hai điều diễn đạt:
1. Source key sai (F-2) — cần key mới `hota-tomb-raiders`.
2. "**+1 primary skill**" nói thiếu: nguồn ghi "+1 Attack **or** +1 Defense **or** +1 Power **or**
   +1 Knowledge" — người chơi **chọn một trong bốn**, không phải nhận một primary skill do map định
   sẵn. Kết hợp với `rpt=y` thì đây là nguồn tăng chỉ số **không giới hạn** — chi tiết đáng nói, và
   nói đúng thì mới thấy vì sao 1.8.0 phải vá AI.

---

### C-16
Claim: Trong `Frontier`: Seer's Hut → phần thưởng Ring of Vitality.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-amulet-of-the-undertaker`
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Frontier&action=raw`

Tìm thấy — Seer's Hut tại (70, 18, 0):

```
{{SorQrow|seer=w|loc=70, 18, 0|quest=Return with:<br>{{An|Amulet of the Undertaker}}</br>|rew={{An|Ring of Vitality}}|prop=A serpent devoured my keychain and scurried away westward. Chase him and bring back the thing. I will return the favor.|comp=Ah, exactly what I needed!  Here is the reward I promised.  You still wish to trade the Amulet of the Undertaker, yes?}}
```

Lý do: đúng, nguyên văn khớp. Mức MINOR vì:
1. Source key sai (F-2) — cần key mới `hota-frontier`.
2. **Bài không ghi đây là HotA.** Trang mở đầu `{{inhota}}`, `source = hota`, campaign
   `Horn of the Abyss`, hero Jeremy. Cùng vấn đề nhất quán như C-14.
3. `seer=w` = Seer's Hut **trên nước** — chi tiết nhỏ nhưng có nghĩa với một campaign hàng hải.

Chi tiết thú vị đáng ghi vào Trivia: text hoàn thành ở Frontier và ở Tomb Raiders **giống nhau
từng chữ** ("Ah, exactly what I needed! Here is the reward I promised. You still wish to trade the
Amulet of the Undertaker, yes?") — đó là chuỗi mặc định của Seer's Hut, không phải text viết riêng.
Nếu bài trích câu đó như "text riêng của scenario" thì sẽ là lỗi; tôi không đọc bài nên chỉ cảnh
báo.

---

### C-17
Claim: Trong template `Apocalypse` (HotA): Amulet là một trong ba artifact **duy nhất** được cho
phép.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-amulet-of-the-undertaker`
Phán quyết: **CONTRADICTED**
Mức: **BLOCKER**
Đã tìm ở:
- `heroes.thelazy.net/index.php?title=Apocalypse&action=raw` (1.335 byte, đọc toàn bộ)
- `...?title=Horn_of_the_Abyss_(Changelog)&action=raw` — grep `Apocalypse` toàn bộ 201.529 byte
- `...?title=Nine-day_Wonder&action=raw`

Tìm thấy — nguyên văn trang `Apocalypse`, **không có chữ "only"**:

```
*Allowed artifacts:
**{{An|Amulet of the Undertaker}}
**{{An|Vampire's Cowl}}
**{{An|Dead Man's Boots}}
*Banned objects:
**[[Dragon Utopia]]
**[[Skeleton Transformer]]
```

**Nguồn nói ngược (bắt buộc trích):** grep `Apocalypse` trên toàn changelog cho **đúng hai** dòng,
không dòng nào là danh sách artifact:

> dòng 1154, `== Version 1.5.0 (01/JAN/2018) ==`: "[-] Added the Boomerang and Apocalypse templates"
>
> dòng 549, `== Version 1.7.1 (06/APR/2024) ==`: "[-] Apocalypse template: **Wanderer's Boots** and
> Shrines of Magical Mystery banned"

**Và một nguồn ngược mới, riêng cho artifact này** — template `Nine-day Wonder`:

```
*Banned artifacts:
**{{An|Angel Wings}}
**{{An|Wayfarer's Boots}}
**{{An|Amulet of the Undertaker}}
**{{An|Garniture of Interference}}
...
```

Lý do — **bốn** lập luận, mỗi cái độc lập đủ để bác cách đọc "duy nhất":

1. **Nguồn không có chữ "only".** `*Allowed artifacts:` + ba dòng. Suy ra "duy nhất" là **thêm vào**
   nguồn. Xác nhận: phát hiện #3 của đợt `dead-mans-boots` **áp dụng nguyên vẹn** cho bài này —
   cùng trang, cùng ba artifact.
2. **Có bằng chứng ngược trực tiếp.** Dòng 1.7.1 cấm riêng **Wanderer's Boots** khỏi Apocalypse.
   Nếu template chỉ cho phép ba artifact thì việc cấm artifact thứ tư là **vô nghĩa** — nó đã bị
   cấm sẵn. Cách đọc dung hòa duy nhất: "Allowed" = được cho phép **thêm**, bên trên các lệnh cấm
   mặc định.
3. **Sai loại nguồn, không chỉ sai cấp.** Trang đặc tả template do cộng đồng viết là **`T6`**.
   Registry đã ghi `hota-apocalypse-template` = `T6`. Không có chuỗi nào **trong game** hiện ra nội
   dung đó, nên gán `T1*` là sai **loại**. Và source key thì lại trỏ về trang artifact (F-2), nơi
   không có một chữ nào về template.
4. **Thiếu phạm vi phiên bản.** Trang `Apocalypse` sửa lần cuối **2025-05-14** ≈ HotA 1.7.2–1.7.3,
   **trước 1.8.0** (31/DEC/2025), và **tự nó không ghi** phiên bản nào.

**Và cái bẫy mà bảng claim đã cảnh báo đúng:** Amulet of the Undertaker **cũng có mặt trong
`*Banned artifacts:` của template `Nine-day Wonder`** — ngược chiều hoàn toàn với Apocalypse. Xem
**F-3**. Viết "Amulet là một trong ba artifact duy nhất được cho phép" mà bỏ qua việc nó bị **cấm**
ở template khác là bức tranh sai lệch về vai trò của nó trong HotA competitive.

**Phải sửa thành** (đại ý): *trong template `Apocalypse` của HotA, Amulet of the Undertaker nằm
trong danh sách "Allowed artifacts" cùng Vampire's Cowl và Dead Man's Boots — hiểu là được cho phép
thêm ngoài các lệnh cấm mặc định, không phải "ba artifact duy nhất"; ngược lại, ở template
`Nine-day Wonder` nó nằm trong danh sách "Banned artifacts".* Nhãn `{T6 INFERENCE: hota-apocalypse-template
+ hota-nine-day-wonder}`, kèm ghi chú trang sửa lần cuối 2025-05-14, trước 1.8.0.

---

### C-18
Claim: Số lượng Ghost Dragon canh Amulet trong `After the Amulet`: trang wiki **không nêu**.
Nhãn bài gán: **`T1* UNVERIFIED: sod-after-the-amulet`**
Phán quyết: **CONFIRMED** (về mặt nội dung — trang wiki thật sự không nêu)
Mức: **BLOCKER** (vì nhãn `UNVERIFIED`, không vì nội dung)
Đã tìm ở: `...?title=After_the_Amulet&action=raw`; `...?title=Template:Cram2&action=raw`;
`CANON-POLICY.md` §5.3

Tìm thấy: bảng `==== Monsters ====` chỉ có ba cột `Location / Type / Message`; ô Type là
`{{Cram2|Ghost Dragon}}`; `Template:Cram2` **không có tham số số lượng** (chỉ có `1` = tên creature,
`2` = link, `name`, `0`). Message cũng chỉ nói "a group of Ghost Dragons". Không con số nào ở đâu.

Lý do — nội dung claim đúng, nhưng **hai** vấn đề:

1. **`UNVERIFIED` không được phép trong thân bài.** `CANON-POLICY.md` §5.3: "Không claim nào ở
   trạng thái `UNVERIFIED` trong thân bài (chuyển xuống mục *Câu hỏi mở* nếu chưa giải quyết
   được)." Xác nhận: phát hiện #4 của đợt `dead-mans-boots` **áp dụng đúng** cho bài này. Phải
   chuyển claim này xuống mục **Câu hỏi mở**.
2. **Cách phát biểu tự gài bẫy.** "Số lượng Ghost Dragon **canh Amulet**" đã giả định sẵn rằng đám
   dragon đó canh Amulet — chính là điều C-06 **không** chứng minh được. Nếu để nguyên, bài
   `UNVERIFIED` một con số nhưng lại **ngầm khẳng định** quan hệ canh giữ. Đó là cách một claim
   chưa kiểm được lẻn vào thân bài qua cửa sau.

**Phải sửa:** ở mục *Câu hỏi mở*, viết ví dụ *"Trang nguồn không ghi số lượng stack Ghost Dragon
tại (38, 8, 0) — `Template:Cram2` không có tham số số lượng. Chỉ giải được bằng cách mở file map
gốc (liên quan B-001)."* Câu đó không cần nhãn độ chắc, và không giả định quan hệ canh giữ.

---

### C-19
Claim: Điều khoản "vô tác dụng nếu hero không có Necromancy" lưu hành trên wiki **là văn wiki,
không phải game text**.
Nhãn bài gán: (dẫn sang bài khác, không nhãn riêng)
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: trang artifact (thelazy); `Talk:Artifact/descriptions`; `Artifact Events`;
`...?title=Necromancy&action=raw`; `...?title=Cloak_of_the_Undead_King&action=raw`; Fandom
`List of Heroes IV artifacts`

Tìm thấy — câu đó nằm **ngoài** infobox, trong phần văn xuôi của trang artifact:

```
If the equipped hero does not have the [[Necromancy]] secondary skill, the Amulet of the Undertaker has no effect.
```

và là **boilerplate lặp y hệt** trên cả ba trang thành phần (chỉ đổi tên artifact) — dấu hiệu rõ
của văn wiki, không phải chuỗi game:

```
If the equipped hero does not have the [[Necromancy]] secondary skill, the Vampire's Cowl has no effect.
If the equipped hero does not have the [[Necromancy]] secondary skill, the Dead Man's Boots has no effect.
```

Đối chiếu **nguồn `T1` thật** (`H3Bitmap.lod > artraits.txt`): mô tả in-game của Amulet là **đúng
một câu**, "Worn about the neck, this amulet increases your Necromancy skill by 5%." — **không có**
điều khoản nào. Trang `Necromancy` cũng **không** nêu điều khoản đó; ví dụ tính cộng dồn của nó
("Expert Necromancy (15%) + Amulet of the Undertaker (+5%) + …") không đặt điều kiện nào.

Lý do: claim đúng, và cách bài xử lý (dẫn sang bài khác thay vì lặp lại) là hợp lý.

**Bổ sung có giá trị — có lẽ đây là nguồn của hiểu nhầm.** Ở **Heroes IV**, điều khoản đó **là**
game text thật. Fandom `List of Heroes IV artifacts`, hàng Amulet of the Undertaker, mục
*Minor artifacts*:

> "Increases the hero's Necromancy skill by 10% **if the hero has the skill. Otherwise, it acts as
> the Basic Necromancy skill.**"

Nghĩa là H4 **có** điều khoản điều kiện trong chính mô tả, nhưng hệ quả **ngược lại** với văn wiki
H3: ở H4 hero không có skill thì amulet **vẫn hoạt động** (như Basic Necromancy), chứ không phải
"vô tác dụng". Đây là chi tiết đáng đưa vào bài: nó giải thích điều khoản từ đâu ra **và** cho
thấy văn wiki H3 không chỉ thiếu nguồn mà còn có thể là kết quả trộn hai game. Xem **F-1**.

---

## Phát hiện ngoài bảng claim

### F-1 — Bài (theo bảng claim) **bỏ hẳn** phiên bản Heroes IV của artifact — MAJOR

Đã tìm ở: `mightandmagic.fandom.com/api.php?action=parse&page=Amulet of the Undertaker&prop=wikitext`;
`...&page=List of Heroes IV artifacts`; `...&page=Prelude to Invasion`

Trang Fandom về artifact mở đầu bằng:

> "The **Amulet of the Undertaker** is an artifact from *Heroes of Might and Magic III* and
> ***Heroes of Might and Magic IV***."

`List of Heroes IV artifacts` (xác nhận độc lập, trang khác), mục **`=== Minor artifacts ===`**:

> Name: Amulet of the Undertaker · Description: "Increases the hero's Necromancy skill by 10% if the
> hero has the skill. Otherwise, it acts as the Basic Necromancy skill." · Slot: **Neck**

Và nó có **vai trò scenario** ở H4, không chỉ là một dòng dữ liệu. `Prelude to Invasion` —
`ScenarioInfobox` ghi `campaign = Death March (H4)`, `version = H4X2`, và bài xác định "is the first
scenario in the Death March campaign in **Winds of War**":

> "In return for an Amulet of Fear, a Wand of Animating Dead, a Hideous Mask, an **Amulet of the
> Undertaker**, and a Wand of Curses, he will give Von Tarkin a Dwarven Hammer, Dwarven Shield, and
> Ring of Protection that carry over to the next map."

Vì sao là MAJOR, không phải NOTE:

- `CANON-POLICY.md` §1 xác định phạm vi Old Universe là **Heroes I–IV** + Chronicles + MM I–VIII.
  Heroes IV **trong** phạm vi.
- Đây không phải chuyện bổ sung cho đủ. Nó làm **sai** các claim đang có: C-01 nói "yếu nhất" và
  "duy nhất hạng Treasure", C-08 nói "thông số gốc… Treasure… +5%" — **không câu nào ghi phạm vi
  game**. Ở H4 cùng artifact đó là **Minor**, **+10%**, và **không vô tác dụng** khi hero thiếu
  skill. Người đọc gặp ba câu so sánh nhất không rào phạm vi sẽ hiểu sai.
- Đây đúng là lỗi mà BH-3 đã dạy, chỉ đổi trục: registry đã chốt "mọi con số gameplay **phải ghi rõ
  phạm vi phiên bản**" sau vụ HotA. Phạm vi **game** cũng vậy, và hậu quả nặng hơn vì lệch xa hơn.

**Phải làm:** thêm mục Heroes IV (hoặc ít nhất một câu phạm vi ở đầu mục Cơ chế), với nhãn **`T6`**
cho tới khi tìm được nguồn tốt hơn — hiện chỉ có Fandom, và Fandom **không dẫn nguồn**. Cần hai key
mới: `fandom-h4-artifact-list`, `fandom-prelude-to-invasion`. thelazy gần như chỉ phủ H3 nên không
giúp được ở đây; đây là một lỗ nguồn thật của dự án, nên ghi vào BACKLOG.

### F-2 — Source key `h3wiki-amulet-of-the-undertaker` **không thể** chống lưng C-13 → C-17 — MAJOR

Trang artifact trên thelazy dài **672 byte**. Tôi dán **toàn bộ** ở đây để khỏi phải tranh luận:

```
{{ArtifactNewSB
 | class  = Treasure
 | slot   = Necklace
 | cost   = 2000
 | event  = A dirty amulet lies next to a freshly dug grave. Upon investigation, you discover it to be the enchanted Amulet of the Undertaker, long thought lost by mortals.
 | effect = +5% {{gl|Necromancy}}
}}

If the equipped hero does not have the [[Necromancy]] secondary skill, the Amulet of the Undertaker has no effect.

Component of [[Cloak of the Undead King]]{{-ws}}.

== Related artifacts ==
* {{An|Cloak of the Undead King}}
* {{An|Vampire's Cowl}}
* {{An|Dead Man's Boots}}

{{Artifact 'see also'}}

[[Category:Treasure artifacts]]
[[Category:Parts of combination artifacts]]
__NOTOC__
```

**Không có section scenario. Không có một tên scenario nào. Không có `Taming of the Wild`,
`Beyond the Horizon`, `Tomb Raiders`, `Frontier`, `Apocalypse`.** Năm claim C-13 → C-17 dẫn về
trang này đều dẫn về chỗ trống. Cách duy nhất tôi tìm được các scenario đó là quét
`api.php?action=query&list=backlinks` — 193 trang trỏ tới artifact.

Key đúng cho từng claim:

| Claim | Key phải dùng | Trạng thái registry |
|---|---|---|
| C-13 | `ab-taming-of-the-wild` | **đã có** |
| C-14 | `hota-beyond-the-horizon` | cần thêm |
| C-15 | `hota-tomb-raiders` | cần thêm |
| C-16 | `hota-frontier` | cần thêm |
| C-17 | `hota-apocalypse-template` (+ `hota-nine-day-wonder`) | đã có / cần thêm |

⚠️ **Điều kiện của phát hiện này:** tôi không được đọc bài gốc, nên tôi chỉ thấy cột "Source key
bài dẫn" của **bảng claim**. Nếu bài thật sự đã dẫn `ab-taming-of-the-wild` và các key scenario
riêng, thì F-2 là **lỗi bảng claim**, không phải lỗi bài, và mức MAJOR này rơi xuống NOTE. Người
sửa kiểm việc này trong một phút; tôi ghi ở mức MAJOR vì nếu đúng như bảng claim mô tả thì năm
claim đang có nhãn `EXPLICIT` trỏ vào nguồn rỗng — theo định nghĩa, "EXPLICIT không nguồn".

### F-3 — Template `Nine-day Wonder` **cấm** Amulet — MINOR (thiếu, và nó ngược chiều C-17)

Đã tìm ở: `heroes.thelazy.net/index.php?title=Nine-day_Wonder&action=raw` (2.348 byte, đọc toàn bộ)

```
*Banned artifacts:
**{{An|Angel Wings}}
**{{An|Wayfarer's Boots}}
**{{An|Amulet of the Undertaker}}
**{{An|Garniture of Interference}}
**{{An|Surcoat of Counterpoise}}
**{{An|Boots of Polarity}}
**{{An|Bird of Perception}}
**{{An|Stoic Watchman}}
**{{An|Emblem of Cognizance}}
**{{An|Head of Legion}}
**{{An|Arms of Legion}}
**{{An|Torso of Legion}}
**{{An|Loins of Legion}}
**{{An|Legs of Legion}}
```

Cảnh báo của bảng claim ("nếu Amulet cũng có mặt trong một template nào đó, **phải kiểm nó nằm ở
danh sách cho phép hay bị cấm**") là **đúng chỗ**: Amulet nằm ở **cả hai** chiều — `Allowed` ở
`Apocalypse`, `Banned` ở `Nine-day Wonder`. Bài chỉ có chiều "allowed" là bức tranh một nửa, và nửa
bị thiếu chính là nửa làm cách đọc "duy nhất được cho phép" sụp hẳn.

Cần key mới `hota-nine-day-wonder`, tier **`T6`** (trang đặc tả template do cộng đồng viết), kèm
ngày sửa cuối để chốt phạm vi phiên bản.

### F-4 — Sáu hero campaign HotA khởi đầu **mang** Amulet — NOTE (thiếu)

Từ 193 backlinks, sáu trang hero có Amulet trong trường `spart_*` của `Template:CampaignHero`:

| Hero | Town | Class | Trường |
|---|---|---|---|
| Boyd | Factory | Death Knight | `spart_11` |
| Aiedia | Tower | Alchemist | `spart_3` |
| Erybarus | Castle | Knight | `spart_3` |
| Ioke | Necropolis | Necromancer | `spart_4` |
| Nahia | Necropolis | Necromancer | `spart_3` |
| Thammus | Necropolis | Death Knight | `spart_3` |

`spart_*` = **spells & artifacts khởi đầu**: `Template:CampaignHero` có HTML comment nhãn cột ở
dòng 67 — `<!---…Spells & Artifacts…--->` — và các trường dùng `{{Sng|…}}` cho spell, `{{Ang|…}}`
cho artifact. Boyd là hero campaign độc quyền của scenario HotA `Dead or Alive` (registry đã có
`hota-dead-or-alive`), thuộc `prison` của người chơi.

Đáng ghi vì bài (theo bảng claim) chỉ có Amulet ở vai **mục tiêu đi tìm** hoặc **vật đổi quest**.
Sáu hero này là vai thứ ba: **trang bị sẵn trên hero**. Với Ioke / Nahia / Thammus (Necropolis) thì
nó còn có nghĩa cơ chế thật, vì họ có Necromancy.

### F-5 — Kiểm disambiguation (BH-2): sạch, nhưng có một tên dễ nhầm — NOTE

- thelazy: `api.php?action=query&list=search&srsearch=Undertaker` → **đúng một** kết quả,
  `Amulet of the Undertaker`. Không có trang `(Xeen)`, `(Ashan)`, hay biến thể nào.
- Fandom: search `Undertaker` trả về thêm **`Amulet of Necromancy`** — artifact **khác**. Nếu bài
  có câu phủ định kiểu "không có amulet nào khác liên quan necromancy", câu đó sai.
- `Treasure` trên thelazy là `#REDIRECT [[Artifact#Class]]` — nên nếu bài dẫn "hạng Treasure" thì
  anchor thật là mục `Class` của trang `Artifact`, không phải một trang riêng.

### F-6 — Tồn tại `Horn of the Abyss/Team Interview (2024)` — NOTE

`heroes.thelazy.net/index.php?title=Horn_of_the_Abyss/Team_Interview_(2024)&action=raw`, **51.274
byte**, dạng hỏi-đáp với HotA Crew.

Tôi đã grep `undertaker`, `cloak`, `necromancy`: **không** phát ngôn nào về artifact này (hai hit
duy nhất là câu hỏi về rework cân bằng nói chung và câu trả lời về Orb of Inhibition /
Recanter's Cloak). Nên **nó không chống lưng claim nào của bài** — tôi ghi lại chính vì thế.

Lý do ghi: dự án đã một lần kết luận "không có developer commentary nào" trong khi phỏng vấn Lead
Designer nằm ngay trên wiki đang dùng. Đợt này tôi **đã kiểm** và **đã trích kết quả rỗng**, thay
vì im lặng. Nếu bài sau cần phát ngôn của đội HotA về cân bằng necromancy, đây là trang phải mở
đầu tiên. Đề xuất vào registry là lead chưa khai thác.

### F-7 — Key mới cần thêm vào `REGISTRY.md` — NOTE

| key đề xuất | tier | Nội dung |
|---|---|---|
| `hota-beyond-the-horizon` | T1* | Scenario HotA (fan-made) — Seer's Hut (2,27,0) đòi 4 artifact → Golden Bow. Chứa câu game text **cố ý bỏ trống người tạo** artifact |
| `hota-tomb-raiders` | T1* | Scenario HotA — Seer's Hut lặp lại (16,172,0) → chọn 1 trong 4 primary skill; Quest Guard (12,178,0) sửa Skeleton Transformer |
| `hota-frontier` | T1* | Scenario HotA — Seer's Hut trên nước (70,18,0) → Ring of Vitality |
| `hota-nine-day-wonder` | **T6** | Trang đặc tả template HotA — Amulet nằm trong `Banned artifacts`. ⚠️ **Ngược chiều** `hota-apocalypse-template` |
| `h3wiki-treasure-chest` | T1* | Treasure Chest: 5% ra artifact, "a random treasure class artifact" |
| `h3wiki-artifact-class` | T1* | `Artifact` mục Class — bốn hạng Treasure/Minor/Major/Relic, AI value 2000/5000/10000/20000 |
| `h3wiki-new-beginning` | T1* | Trang campaign — thứ tự 4 map, chứng minh Amulet là artifact đầu tiên |
| `fandom-h4-artifact-list` | T6 | `List of Heroes IV artifacts` — Amulet là **Minor**, slot Neck, **+10%** Necromancy |
| `fandom-prelude-to-invasion` | T6 | Scenario H4 *Winds of War*, campaign *Death March* — Amulet là 1 trong 5 artifact đổi lấy Dwarven Hammer/Shield/Ring of Protection |
| `hota-team-interview-2024` | T4-tương đương | Hỏi-đáp HotA Crew, 51.274 byte. **Không** nói về artifact này (đã kiểm) |

---

## Bốn phát hiện đợt trước — có áp dụng cho artifact này không

| # | Phát hiện | Áp dụng? | Chỗ áp dụng |
|---|---|---|---|
| 1 | `T6 EXPLICIT` là tổ hợp nhãn không hợp lệ | ✅ **Có** | C-09 — BLOCKER |
| 2 | `Talk:Artifact/descriptions` là `T1` thật (`H3Bitmap.lod > artraits.txt`) | ✅ **Có, đã xác nhận có dòng riêng cho Amulet** | C-09 — trích được nguyên văn ở trên |
| 3 | "Một trong ba artifact *duy nhất*" ở `Apocalypse` là cách đọc SAI | ✅ **Có, nguyên vẹn** | C-17 — BLOCKER, **cộng thêm** nguồn ngược mới (F-3) |
| 4 | `UNVERIFIED` không được ở thân bài | ✅ **Có** | C-18 — BLOCKER |

Cả bốn áp dụng đúng, không cái nào cần điều chỉnh. Phát hiện #2 mạnh thêm: bảng artraits.txt
**có** dòng cho Amulet, nên C-09 nâng được lên `T1` thật thay vì chỉ hạ nhãn.

Cảnh báo kèm theo của bảng claim (template ngược chiều) **đã bắt được cá thật**: xem F-3.

---

## Kết luận

**Bài KHÔNG đủ điều kiện `status: verified`.** Điều kiện là không còn BLOCKER và không còn MAJOR;
hiện còn **4 BLOCKER** và **2 MAJOR**.

Điểm mạnh của bài, nói cho công bằng trước: **13 trong 19 claim trích khớp nguyên văn tới từng dấu
câu**, kể cả những chỗ dễ chép sai (thứ tự "Bone/Ghost/Bone" ở C-07, hai dấu cách trong chuỗi game
ở C-04, con số 4 artifact ở C-14, tham số `rpt=y` ở C-15). Người viết đã đọc nguồn thật, không viết
từ trí nhớ. Hai claim phủ định lớn nhất (C-02 "không ai tạo ra nó", C-19 "là văn wiki") **đều đứng
vững** — đây là loại claim dự án hay sai, và lần này không sai.

### Bắt buộc sửa — BLOCKER

1. **C-09** — `T6 EXPLICIT` là tổ hợp không hợp lệ (`CANON-POLICY.md` §2). Sửa thành
   **`{T1 EXPLICIT: h3wiki-artraits-txt}`**, trích: "Worn about the neck, this amulet increases your
   Necromancy skill by 5%." Đây là sửa **có lợi** — nâng một dòng từ T6 lên `T1` không dấu sao.
2. **C-17** — bỏ chữ "**duy nhất**". Nguồn không có "only"; changelog 1.7.1 cấm thêm Wanderer's
   Boots là bằng chứng ngược; và Amulet **bị cấm** ở template `Nine-day Wonder` (F-3). Đổi tier
   `T1*` → **`T6`** (sai **loại** nguồn, không chỉ sai cấp), ghi phạm vi phiên bản (trang sửa cuối
   2025-05-14, trước 1.8.0), và nêu cả chiều ngược.
3. **C-06** — bỏ hoặc hạ nhãn câu "**không có lính canh nào**". Bảng `Artifacts` của thelazy có ba
   cột và **không có trường guardian**, đã đối chiếu ba scenario — im lặng của nó không chứng minh
   được gì. `EXPLICIT` ở đây là EXPLICIT không nguồn. Giữ (38, 8, 0) và "số lượng không được nêu"
   ở `EXPLICIT`; phần còn lại xuống `INFERENCE` có ghi bước, hoặc viết lại theo hướng khẳng định.
4. **C-18** — chuyển khỏi thân bài xuống **Câu hỏi mở** (`CANON-POLICY.md` §5.3). Đồng thời bỏ chữ
   "**canh Amulet**" khỏi cách phát biểu, vì nó ngầm khẳng định đúng cái quan hệ mà C-06 không
   chứng minh được.

### Bắt buộc sửa — MAJOR

5. **F-1** — thêm phạm vi game. Amulet of the Undertaker **cũng tồn tại ở Heroes IV** (Minor, slot
   Neck, **+10%** Necromancy, "Otherwise, it acts as the Basic Necromancy skill"), và có vai trò
   quest trong `Prelude to Invasion` (*Winds of War*, campaign *Death March*). Heroes IV nằm **trong**
   phạm vi Old Universe theo §1. Tối thiểu: rào phạm vi cho C-01 và C-08 bằng "Trong Heroes III…".
   Tốt hơn: thêm mục Heroes IV, nhãn `T6` (chỉ có Fandom, không dẫn nguồn) và ghi lỗ nguồn này vào
   BACKLOG.
6. **F-2** — sửa source key cho C-13 → C-17. Trang artifact dài 672 byte và **không chứa một tên
   scenario nào**; năm claim này hiện dẫn về chỗ trống. Dùng `ab-taming-of-the-wild` (đã có) +
   bốn key mới. *Nếu bài thật sự đã dẫn đúng key scenario thì đây là lỗi bảng claim và mục này rơi
   xuống NOTE — kiểm trước khi sửa.*

### Nên sửa — MINOR (không chặn `verified`)

- **C-01** — thêm nhãn + source key (đang trống hoàn toàn, vi phạm §5.1).
- **C-04** — bổ sung nguồn cho chữ "đầu tiên" (trang campaign `New Beginning`, hoặc thư Day 21).
- **C-08** — ghi rõ "gốc" là bản nào (SoD/RoE/AB), vì HotA 1.3.0–1.7.x là 2,5% và H4 là +10%.
- **C-10** — tách *cơ chế* (truy được về nguồn → `INFERENCE`, vào thân bài) khỏi *lời khuyên chiến
  thuật* (giữ `FAN_THEORY`, giữ ở mục riêng).
- **C-12** — con số 2,5% cho **đúng artifact này** là `EXPLICIT` (dòng 1.8.0 nêu tên và nêu số);
  chỉ mốc **bắt đầu 1.3.0** mới là `INFERENCE`. Tách hai claim.
- **C-14, C-16** — ghi rõ `Beyond the Horizon` và `Frontier` là scenario **HotA (fan-made, không
  phải NWC)**, nhất quán với cách C-15 đã làm.
- **C-15** — sửa "+1 primary skill" thành "**chọn một trong** +1 Attack / Defense / Power /
  Knowledge", và nói rõ hệ quả của `rpt=y`.
- **C-16** — không trích "Ah, exactly what I needed!…" như text riêng của scenario: câu đó giống
  từng chữ với `Tomb Raiders`, tức là chuỗi **mặc định** của Seer's Hut.
- **F-3** — thêm `Nine-day Wonder` (Amulet trong `Banned artifacts`).

### Nên thêm — NOTE

- **F-4** — sáu hero campaign HotA khởi đầu mang Amulet (Boyd, Aiedia, Erybarus, Ioke, Nahia,
  Thammus). Vai thứ ba của artifact, hiện chưa có trong bài.
- **F-5** — `Amulet of Necromancy` là artifact khác, đừng gộp.
- **F-6** — `Horn of the Abyss/Team Interview (2024)` tồn tại, đã kiểm, **không** nói về artifact
  này. Ghi lại để lần sau không phải kiểm lại và không kết luận "không tồn tại" mà chưa mở.
- **F-7** — mười key mới cho `REGISTRY.md`.
- **C-03** — thêm `h3wiki-artifact-events` làm xác nhận độc lập cho text khi nhặt.
- **C-07** — ghi thêm `Contents: Morale +2` của event (32, 5, 0).
- **C-14** — nói rõ bốn artifact đó thuộc **hai** combination artifact khác nhau (Cloak of the
  Undead King và Armor of the Damned), tránh bị đọc thành bốn thành phần cùng một combo.

### Một nhận xét về hình mẫu lỗi

Bốn BLOCKER của bài rơi vào **đúng hai** khuôn, và cả hai đã có tiền lệ trong registry:

- **Suy luận từ im lặng của nguồn** (C-06, C-18): bảng wiki không nói gì về lính canh và số lượng,
  và bài đọc sự im lặng đó thành dữ kiện. Đây là biến thể của bài học lớn nhất trong `CLAUDE.md` —
  claim phủ định trông giống sự cẩn trọng. Cách chữa không phải "cẩn trọng hơn" mà là **viết theo
  hướng khẳng định**: nói nguồn *có* gì, đừng nói nguồn *không có* gì.
- **Thêm chữ vào nguồn** (C-17: "duy nhất"; C-09: gọi T6 là EXPLICIT): nguồn ghi `*Allowed
  artifacts:` và bài đọc thành "chỉ ba artifact được phép". Cùng một trang, cùng ba artifact, đã
  bắt được ở đợt `dead-mans-boots` **cùng ngày** — nghĩa là lỗi này lặp lại qua các bài trong cùng
  cụm, không phải sự cố lẻ. Đề xuất: khi viết bài thành phần Cloak thứ ba, kiểm mục này **trước**
  khi viết, không phải sau.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. Cả 4 BLOCKER và 2 MAJOR đều xử lý bằng **sửa bài** hoặc **đưa
nguồn mới**.

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| C-09 | `T6 EXPLICIT` không hợp lệ | BLOCKER | Đổi sang `{T1 EXPLICIT: h3wiki-artraits-txt}` — **nâng** tier, không hạ |
| C-17 | "duy nhất" bị phản bác | BLOCKER | Bỏ chữ "duy nhất", hạ `T6`, thêm phạm vi phiên bản, thêm dòng `Nine-day Wonder` **BỊ CẤM** để nêu cả chiều ngược |
| C-06 | "không có lính canh" = EXPLICIT không nguồn | BLOCKER | Viết lại toàn mục. Nêu rõ bảng `Artifacts` **không có trường guardian** nên im lặng không chứng minh được gì. Quan hệ canh giữ hạ xuống `INFERENCE` có ghi bước |
| C-18 | `UNVERIFIED` trong thân bài | BLOCKER | Chuyển xuống *Câu hỏi mở* thành Q1, và **bỏ chữ "canh Amulet"** khỏi cách phát biểu |
| F-1 | Bỏ hẳn Heroes IV | MAJOR | Thêm mục *Cơ chế trong Heroes IV* kèm bảng đối chiếu H3/H4. Rào phạm vi cho Tóm lược và đổi tiêu đề thành *Cơ chế trong Heroes III*. Ghi lỗ nguồn thành `B-019` |
| F-2 | Source key trỏ vào trang rỗng | MAJOR | **Đã kiểm: đây là lỗi bài thật**, không phải lỗi bảng claim — bài dẫn `h3wiki-amulet-of-the-undertaker` cho cả bảng xuất hiện. Tách thành 6 key riêng, thêm 4 key mới vào REGISTRY |
| C-01 | Không có nhãn nào | MINOR | Gán `INFERENCE` kèm ba thước đo đối chiếu |
| C-02 | Claim phủ định | NOTE | Củng cố: nêu phạm vi đã quét (193 backlinks + Team Interview 2024), và thêm chứng cứ dương từ `Beyond the Horizon` |

### Xác minh độc lập của người sửa

Trước khi thêm 4 key scenario, tôi tự fetch lại `?action=raw` cho `Beyond_the_Horizon`,
`Tomb_Raiders`, `Frontier`, `Nine-day_Wonder`, `Apocalypse` để **xác nhận trường `source`** —
vì gán sai sản phẩm từng là BLOCKER ở đợt `dead-mans-boots`. Kết quả khớp verifier hoàn toàn:
cả ba scenario đều `source = hota` (`cback` lần lượt `hota fif 2`, `hota fif 4`, `hota hota 1`),
và hai template xác nhận đúng chiều cấm/cho phép.

### Phát hiện của verifier được dùng làm nội dung, không chỉ để sửa lỗi

Ba mục sau **làm bài tốt hơn** chứ không chỉ vá lỗi, nên đã đưa vào thân bài:

- Câu priest ở `Beyond the Horizon` **cố ý bỏ lửng** nguồn gốc artifact ("Their creator was...
  Bah, that doesn't matter.") — biến một claim phủ định thành chứng cứ dương.
- `Template:Cram2` **không có tham số số lượng** — giải thích được *vì sao* nguồn im lặng, thay vì
  chỉ ghi nhận là im lặng.
- Heroes IV cho Amulet hoạt động như **Basic Necromancy** khi hero không có skill — trái ngược H3,
  và là chi tiết thiết kế đáng chú ý chứ không phải một dòng thông số.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-amulet-of-the-undertaker-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.

---

## ⚠️ ĐÍNH CHÍNH (2026-08-03, sau khi verify `jeddite`)

**Phát hiện "nhãn `UNVERIFIED` không được phép — vi phạm `CANON-POLICY.md` mục 5.3" là SAI.**

Nguyên văn mục 5.3:

> "Không claim nào ở trạng thái `UNVERIFIED` trong thân bài
> (**chuyển xuống mục *Câu hỏi mở* nếu chưa giải quyết được**)."

Nhãn `UNVERIFIED` bị phát hiện trong bài **đã nằm trong mục *Câu hỏi mở*** — tức là nó đã ở đúng
chỗ mà mục 5.3 quy định. Đưa một claim chưa kiểm được xuống *Câu hỏi mở* **là cách xử lý đúng**,
không phải vi phạm. Bài không hề vi phạm mục 5.3 ở điểm này.

**Những phần khác của cùng phát hiện vẫn đúng và vẫn cần sửa** — chúng độc lập với mục 5.3:

- Nhãn bị gán **sai cấp**: dữ kiện đếm được / trích được nguyên văn thì phải là `EXPLICIT`, không
  phải `UNVERIFIED`. Gán `UNVERIFIED` cho điều đã kiểm xong là hạ cấp sai chiều.
- **Cách phát biểu tự gài bẫy**: câu hỏi ngầm khẳng định một quan hệ chưa chứng minh được.
- **Trộn hai loại claim vào một nhãn**: câu trích (`EXPLICIT`) và nhận định về sự vắng mặt
  (`INFERENCE`) phải tách.

Nên các sửa đã áp dụng vẫn giữ nguyên — chỉ **lý do** ghi trong báo cáo là sai ở một điểm.

### Vì sao lỗi này lan ra ba báo cáo

Người soạn bảng claim đưa "UNVERIFIED không được phép trong thân bài" vào mục *"Những phát hiện ĐÃ
XÁC LẬP ở đợt trước"* của bảng claim cho hai bài sau. Verifier được yêu cầu **không đọc bài gốc**,
nên không thấy nhãn đó nằm trong *Câu hỏi mở*, và cũng không có lý do nghi ngờ một điều đã được
tuyên là "đã xác lập".

**Đây là lỗi của người điều phối, không phải của verifier.** Xem `VERIFY-PROTOCOL.md` mục 7.
