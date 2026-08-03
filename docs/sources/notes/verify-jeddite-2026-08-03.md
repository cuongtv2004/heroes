# Verify report: jeddite — 2026-08-03

Verifier: agent độc lập, không đọc bài gốc
(không đọc `docs/codex/heroes/jeddite.md`, `docs/sources/raw/`, `sandro.md`, `ethric.md`,
hay báo cáo nào trong `docs/sources/notes/`)

Số claim kiểm: 45
CONFIRMED: 30 | DOWNGRADE: 9 | NOT_FOUND: 1 | CONTRADICTED: 5

BLOCKER: 3 (C-26, C-30, C-31) · MAJOR: 8 (C-08, C-18, C-27, C-28, C-29, C-33, C-38, C-40)

---

## Nguồn đã fetch trong đợt này

| URL | Dùng cho |
|---|---|
| `heroes.thelazy.net/index.php?title=Target&action=raw` (17.766 byte, đọc TOÀN BỘ) | C-01…C-16, C-20…C-22, C-38, C-41 |
| `…?title=Jeddite&action=raw` (1.718 byte) | C-17, C-29…C-33, C-35 |
| `…?title=Translation_Data/HeroBios.txt&action=raw` (dòng 186) | C-34, C-37 |
| `…?title=Ufretin&action=raw` | C-39 |
| `…?title=Dungeon&action=raw` (dòng 118) | C-33 |
| `…?title=Reference_IDs&action=raw` (dòng 937) | C-29 |
| `…?title=List_of_campaign_heroes&action=raw` (3.585 byte, 0 lần "Jeddite") | C-33 |
| `…?title=Horn_of_the_Abyss_(Changelog)&action=raw` (dòng 220, 902) | C-30, C-31 |
| `…?title=Hero_specialty&action=raw` (dòng 147, 149) | C-30 |
| `…?title=Template:Swh&action=raw` | **quyết định C-30, C-31** |
| `…?title=Heroes_from_other_games&action=raw` (dòng 227, 290, 398) | C-17, C-25 |
| `…?title=Gregory_Fulton/On_Names_in_Heroes_of_Might_and_Magic_III&action=raw` (dòng 840) | nguồn **T4** mới |
| `…?title=Xenofex&action=raw` + redirect `Zenofex` | C-36 |
| `…?title=Master&action=raw` (0 lần "Jeddite") | C-14, C-15 |
| `api.php?action=query&list=backlinks&bltitle=Jeddite&bllimit=500` (68 trang) | C-26, C-27, C-28, C-32 |
| `…?title=<scenario>&action=raw` cho 12 scenario | C-26, C-27, C-28 |
| `mightandmagic.fandom.com/api.php?action=parse&page=Jeddite` | C-24 |
| `…&page=Jeddite%20(Enroth)` | C-17, C-19, C-40 |
| `…&page=Jungle%20Fever` | **C-18, C-26, C-27** |
| `…&list=search&srsearch=Jeddite&srlimit=30` | C-24 (BH-2) |

Không vào được: `mightandmagic.fandom.com/index.php?…&action=raw` → Cloudflare challenge
(`<title>Just a moment...</title>`). `api.php` vẫn vào được — khớp ghi chú Nhóm 3 của registry.
`api.php?list=search&srsearch=insource:/Jeddite/` trên thelazy trả **rỗng** (CirrusSearch không
bật) → phải dùng `backlinks`, không có đường tắt.

---

## Chi tiết

### C-01
Claim: Jeddite và Sandro cùng học dưới Ethric; Jeddite là "one of Ethric's best students"
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Target&action=raw`, timed event Day 2
Tìm thấy:

```
We were students together under [[Ethric]].
...
You do remember this [[Jeddite]].  Not only was he one of [[Ethric]]'s best students,
he was also your best friend.
```

Lý do: cả hai mệnh đề đều có nguyên văn. Lưu ý vị trí: đây là **map/timed event của scenario**,
không phải bio hero — dẫn nguồn `sod-target` là đúng.

---

### C-02
Claim: nguyên văn thư Jeddite Day 2
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, `{{TErow| 2 |Letter from [[Jeddite]]|…}}`
Tìm thấy:

```
"[[Sandro]],
My name is [[Jeddite]].  Perhaps you remember me, if your memories are not clouded by your
undead mind.  We were students together under [[Ethric]].  By becoming [[Necromancer]], you
have completely shamed me, for it was I who introduced you to [[Ethric]].  I should have
listened to him.  From the start, he doubted your ability to wisely endure the burden of
magical knowledge.
```

Lý do: khớp **từng chữ**, kể cả dấu hai khoảng trắng sau dấu chấm. Không sai lệch nào.

---

### C-03
Claim: lỗi ngữ pháp "By becoming Necromancer" (thiếu mạo từ) **có trong game text gốc**
Nhãn bài gán: (ghi chú trong ngoặc) · sod-target
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `Target` (grep `{{sic`)
Tìm thấy: chuỗi `By becoming [[Necromancer]], you have completely shamed me` — lỗi **có** trong
bản chép. Nhưng `grep -c "{{sic"` trên trang `Target` trả về **0**: wiki **không** đánh dấu
`{{sic}}` cho bất kỳ lỗi nào trên trang này.
Lý do: registry lấy chính việc wiki dùng `{{sic}}` làm cơ sở tin `T1*`. Ở trang này wiki
**không** dùng. Vậy "lỗi có trong bản chép" là EXPLICIT, còn "lỗi có trong **game gốc**" chỉ là
`INFERENCE` (suy từ việc bản chép không sửa lỗi — người diễn giải sẽ sửa, người chép thì không).
Phải ghi rõ bước suy luận, đừng viết như dữ kiện đã kiểm.

---

### C-04
Claim: Jeddite là người chơi xanh dương, town Dungeon, (55, 68, 0), địch **đợt hai**
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, mục `==== Heroes ====`, `==== Towns ====`, và header `{{CampaignScenario}}`
Tìm thấy:

```
| enemies        = 1: {{green}}{{orange}}{{-}}2: {{blue}}{{tan}}{{purple}}
{{Town row|55, 67, 0|blue|Dungeon}}
{{hero row|55, 68, 0|blue|Jeddite|Warlock}}
```

Lý do: cả bốn chi tiết khớp. `blue` nằm ở nhóm `2:` → đợt hai, đúng. (Town ở 55,67,0; hero ở
55,68,0 — bài ghi toạ độ hero, đúng.)

---

### C-05
Claim: "I will take the artifacts from your rotting corpse and return them to Ethric."
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, Day 2
Tìm thấy: `I will take the artifacts from your rotting corpse and return them to [[Ethric]]."`
Lý do: khớp từng chữ.

---

### C-06
Claim: Day 24 — Jeddite muốn trả artifact về Ethric, Jabarkas muốn giữ; liên minh rạn nứt vì điều này
Nhãn bài gán: T1* EXPLICIT · sod-target (Day 24)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, `{{TErow| 24 |Rumors|…}}`
Tìm thấy:

```
A spy returns with word has come about internal conflicts among your enemies.  Your old friend
[[Jeddite]] and his allies want to seize the artifacts and promptly return them to [[Ethric]].
However, two other allied [[stronghold]] towns to the North and to the Northeast want the
artifacts to remain in their possession.  According to you advisors, Lord [[Jabarkas]], the
leader of these two towns, is [[Ethric]]'s illegitimate younger brother suffers from Little
Man's Syndrome.
```

Lý do: "internal conflicts" + hai ý muốn trái ngược nêu ngay cạnh nhau → nhân quả có trong text,
không phải bài suy ra. CONFIRMED.

---

### C-07
Claim: map event (40, 46, 0) — "…we will retrieve the artifacts and give them to Jeddite."
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, `==== Events ====`, `{{Erow| 40, 46, 0 |…}}`
Tìm thấy:

```
"Yes, sir.  [[Ethric]]'s message was received this morning.  [[Sandro]] is in the area and does
hold the artifacts.  We have replied to [[Ethric]] that we will retrieve the artifacts and give
them to [[Jeddite]].  Shall we prepare to attack [[Sandro]]'s army, sir?"
```

Lý do: khớp, và đúng toạ độ. (BH-1: text này nằm trong `==== Events ====`, đúng như bài nói.)

---

### C-08
Claim: map event (49, 63, 0) là đoạn mô tả Jeddite **chi tiết nhất trong toàn Old Universe**
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `Target`, `{{Erow| 49, 63, 0 |…}}`; đối chiếu `Jeddite` (bio H3 + bio H4),
`Translation_Data/HeroBios.txt`, Fandom `Jungle Fever`
Tìm thấy — nguyên văn **đúng từng chữ**:

```
Your neighboring town is coming into view.  [[Jeddite]] has become quite a powerful lord as
well as a powerful [[warlock]].  You have learned he is a man of his word and has never backed
down from a battle.  You wonder if going into combat against a former friend will affect his
strategy.  After all, both sides have the advantage of knowing exactly what and how each other
will act in battle.
```

Lý do: **trích dẫn CONFIRMED, superlative thì không.** Không nguồn nào nói đoạn này là "chi tiết
nhất". Đây là claim độc quyền phạm vi toàn universe, và có ít nhất ba đoạn cạnh tranh:

- bio H4 (`{{H4Story|Sorcerer|…}}`): ba câu, mô tả **động cơ và tính cách** — thứ đoạn (49,63,0)
  không có
- bio H3 (`HeroBios.txt`): hai câu, dựng cả một tin đồn quanh nhân vật
- **`Jungle Fever`** (Heroes IV, Winds of War): cho hắn biệt hiệu "Jeddite **the Reckless**" và
  chi tiết hắn **nuôi rồng** — dữ kiện mà không đoạn nào khác có (xem C-18, C-26)

Bắt buộc sửa: bỏ superlative, hoặc hạ xuống `T1* INFERENCE` kèm phạm vi hẹp và ghi bước suy luận
("dài nhất trong `sod-target`" thì kiểm được; "trong toàn Old Universe" thì không).

---

### C-09
Claim: Day 2 "…find a way use this weakness against him." + lỗi thiếu *to*
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, Day 2, câu cuối
Tìm thấy: `So, he feels guilty for introducing you to [[Ethric]].  You will have to find a way use this weakness against him.`
Lý do: khớp từng chữ, lỗi có trong bản chép. (Về việc lỗi có trong game gốc: xem C-03.)

---

### C-10
Claim: Day 8, cố vấn nói nên trả lời thư "if you are to use your friendship to your advantage"
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, `{{TErow| 8 |Reply to [[Jeddite]]|…}}`
Tìm thấy: `They suggest you reply to it soon if you are to use your friendship to your advantage.`
Lý do: khớp.

---

### C-11
Claim: Day 8, thư Sandro trả lời — nguyên văn
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, Day 8
Tìm thấy:

```
If you stand in my way, I will kill every living soul under your command and convert their
[[undead]] bodies to my cause.  By the way, thank you for introducing me to the powers of
magic.  Without your help, I would never have achieved such greatness."
```

Lý do: khớp từng chữ.

---

### C-12
Claim: Sandro **cố ý bóp méo** — thư Jeddite nói "giới thiệu với Ethric", Sandro đổi thành
"giới thiệu với sức mạnh phép thuật", tức quy công tạo ra con quái vật
Nhãn bài gán: (không gán nhãn riêng)
Phán quyết: **CONFIRMED** (ở mức `INFERENCE`)
Mức: —
Đã tìm ở: `Target`, Day 2 vs Day 8
Tìm thấy: Day 2 `for it was I who introduced you to [[Ethric]]`; Day 8 `thank you for
introducing me to the powers of magic`; và câu kết Day 8: `hopefully, giving him a glimpse of the
monster he helped to create will shatter his own confidence.`
Lý do: đối chiếu hai chuỗi là dữ kiện; chữ "cố ý" được câu kết chống lưng thẳng (game nói rõ mục
đích là "shatter his own confidence"). Đây là `INFERENCE` **mạnh**, không phải suy diễn tự do.
Nếu bài viết đoạn này không có nhãn, thêm `{T1* INFERENCE: sod-target}` kèm bước suy luận.

---

### C-13
Claim: "hopefully, giving him a glimpse of the monster he helped to create will shatter his own confidence."
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, Day 8, câu cuối
Tìm thấy: `But, hopefully, giving him a glimpse of the monster he helped to create will shatter his own confidence.`
Lý do: khớp.

---

### C-14
Claim: `Target` **không có epilogue**, và **không có event nào** mô tả Jeddite bị đánh bại hay chết
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target` — liệt kê **toàn bộ** heading, đếm **toàn bộ** event; và `Master` (scenario kế
tiếp của *Rise of the Necromancer*)
Tìm thấy: heading của trang là `== Prologue ==`, `== Scenario ==`, `=== Timed events ===`,
`=== Objects ===`, `==== Events ====`, `==== Towns ====`, `==== Heroes ====`,
`==== Monsters ====`, `==== Seer's Huts ====`, `==== Artifacts ====`. **Không có
`== Epilogue ==`.** Trang chứa **8** timed event (Day 1, 2, 6, 8, 13, 18, 24, 36) và **5** map
event ((15,27,0), (17,19,0), (39,49,1), (40,46,0), (49,63,0)). Jeddite xuất hiện ở Day 2, 8, 24
và map event (40,46,0), (49,63,0) — **bài không bỏ sót event nào**. `Master` chứa **0** lần
"Jeddite".
Lý do: claim phủ định này **đứng vững** sau khi đọc hết trang, không chỉ prologue (BH-1).
⚠️ Ghi chú cho registry: entry `sod-target` ghi "6 timed event" — thực tế là **8**.

---

### C-15
Claim: **Không nguồn nào** nói Sandro giết hắn; số phận Jeddite trong `Target` là kết quả
gameplay, không phải canon
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: toàn bộ `Target`; `Master`; 68 backlink của `Jeddite` trên thelazy; Fandom
`Jeddite (Enroth)`, `Target`, và `list=search&srsearch=Jeddite&srlimit=30`
Tìm thấy: không chuỗi nào nói Jeddite chết. Ngược lại có **bằng chứng thuận**: Fandom
`Jeddite (Enroth)` ghi `|status = Alive (as of ''Heroes IV'')`, và hắn có mặt trong Heroes IV
(kể cả một scenario Winds of War — xem C-18).
Lý do: claim phủ định đứng vững, và được chống lưng bởi bằng chứng độc lập về việc hắn còn sống
sau đó. Nhưng **phải gán nhãn** — hiện claim table ghi "(không gán nhãn)". Claim phủ định không
nhãn là chỗ dễ lọt lỗi nhất; đề nghị `{T1* INFERENCE: sod-target}`.

---

### C-16
Claim: event Day 36 (mưu ám sát bằng thư không ký tên) **không được game quy cho** Jeddite
Nhãn bài gán: (ghi chú trong ngoặc) · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, `{{TErow| 36 |Attempt to assassinate|…}}`
Tìm thấy:

```
Attached was a note saying, "[[Sandro]], death to you and all who would follow you.  I will
seize those artifacts you have stolen."  The note was unsigned.
```

Lý do: game nói thẳng `The note was unsigned` và không nêu tên ai. Claim phủ định đúng, và đây là
loại claim phủ định **an toàn** vì nguồn tự khẳng định sự khuyết danh.

---

### C-17
Claim: Ở Heroes IV, Jeddite là **Sorcerer** phe **Asylum**; nguyên văn bio H4
Nhãn bài gán: T1* EXPLICIT · h3wiki-jeddite
Phán quyết: **CONFIRMED** (một phần mis-citation)
Mức: MINOR
Đã tìm ở: `Jeddite` (thelazy); `Heroes_from_other_games` dòng 227; Fandom `Jeddite (Enroth)`
Tìm thấy — trên `Jeddite`, **nằm TRONG template** `{{H4Story|…}}`, không phải văn biên tập:

```
{{H4Story|Sorcerer|Some sorcerers may enjoy causing destruction, but Jeddite worships it. He is
a dark fanatic wholly committed to the ultimate dissolution of the universe. No one knows why he
adopted such insane beliefs, but neither can anyone convince him to turn to another path.}}
```

Lý do: trích dẫn khớp từng chữ, và **kiểm được gợi ý #2 của bảng claim**: câu này nằm *trong*
template `{{H4Story}}` (in-game bio), **không** nằm trong mục `== Story ==` (văn wiki). Vậy `T1*`
là đúng loại — khác ca `Terek`.
**Nhưng "Asylum" KHÔNG có trên `h3wiki-jeddite`.** Trang chỉ ghi `Sorcerer`. Nguồn thật cho
Asylum là:
- `Heroes_from_other_games` dòng 226–227: `{{H3H4header|Asylum|Dungeon}}` … `{{H3H4row|Jeddite|Warlock}}`
- Fandom `Jeddite (Enroth)`: `|affiliation = [[Dungeon (H3)|Dungeon]] {{icon-H3}} <br> [[Asylum]] {{icon-H4}}`

Bắt buộc sửa: tách source key cho "Asylum".

---

### C-18
Claim: **Không campaign, scenario, hay manual nào** nối được từ nhân vật H3 sang kẻ cuồng tín H4;
game **cố ý** để trống khoảng giữa
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: Fandom `api.php?action=parse&page=Jungle%20Fever&prop=wikitext`
Tìm thấy — một **scenario Heroes IV** có text truyện về Jeddite:

```
|heroes     = [[Jeddite (Enroth)|Jeddite]]
|players    = 2 (1 human)
|difficulty = Expert
|win        = Be the only player to own towns and defeat [[Jeddite (Enroth)|Jeddite]]
|version    = H4X2
{{text|You once lived all alone on this jungle island until Jeddite the Reckless decided to make
his home here. For a few years that seemed to be fine, there were plenty of inhabitants for you
to turn into undead armies and plenty for him to feed to his dragons. But lately you have
noticed that there are definitely not enough island natives for the both of you. The War begins
today. He has got to go!!}}
'''Jungle Fever''' is a [[scenario]] in ''[[Heroes of Might and Magic IV: Winds of War]]''.
```

Lý do: phần "không **nối** H3 sang H4" thì vẫn đứng — `Jungle Fever` không kể lại quá khứ H3 của
hắn. Nhưng phần **"không scenario nào"** là **sai**: có một scenario Heroes IV nói về Jeddite, cho
hắn **biệt hiệu riêng** ("Jeddite the Reckless") và **chi tiết mới** (nuôi rồng, ăn thịt dân đảo),
và đặt hắn làm **địch duy nhất được nêu tên**. Đây đúng là loại lỗi `CLAUDE.md` cảnh báo: claim
phủ định trông giống sự cẩn trọng.
Cũng phải bỏ chữ "**cố ý**": không nguồn T1–T4 nào nói NWC cố ý để trống. Đó là suy đoán về ý
định tác giả, phải là `INFERENCE` hoặc bỏ.
Bắt buộc sửa: viết lại thành "không nguồn nào **giải thích** hắn đi từ warlock H3 thành kẻ cuồng
tín H4; chi tiết H4 duy nhất ngoài bio là `Jungle Fever`", kèm source key mới.

---

### C-19
Claim: hắn sống sót qua Reckoning và sang Axeoth
Nhãn bài gán: T6 INFERENCE · fandom-jeddite-enroth
Phán quyết: **DOWNGRADE** (tier quá **thấp**, không quá cao)
Mức: MINOR
Đã tìm ở: Fandom `Jeddite (Enroth)`; `Jeddite` (thelazy); Fandom `Jungle Fever`
Tìm thấy: Fandom infobox ghi `|world = [[Enroth (planet)|Enroth]]` — **không** ghi Axeoth.
Nhưng có nguồn tốt hơn T6: bio H4 in-game trên thelazy (`{{H4Story|Sorcerer|…}}`) và `Jungle
Fever` (scenario H4X2) đều là in-game text → `T1*`.
Lý do: `INFERENCE` là đúng độ chắc (không text nào nói "survived the Reckoning"). Nhưng tier nên
là `T1*` (sự có mặt trong Heroes IV là in-game), không phải `T6` — và **Fandom không phải nguồn
nói Axeoth**, nên dẫn `fandom-jeddite-enroth` cho chữ "Axeoth" là mis-citation nhẹ. Xem thêm
**C-40**: cùng dữ kiện này bị gán hai độ chắc khác nhau ở hai mục.

---

### C-20
Claim: game text dùng thì quá khứ — "he **was** also your best friend."
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, Day 2
Tìm thấy: `Not only was he one of [[Ethric]]'s best students, he was also your best friend.`
Lý do: khớp; thì quá khứ đúng như bài nói.

---

### C-21
Claim: "I have allied with the Rampart town up north, and they stand with me against you."
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Target`, Day 2; đối chiếu `==== Towns ====`
Tìm thấy: `I have allied with the [[Rampart]] town up north, and they stand with me against you.`
Kiểm chéo bản đồ: `{{Town row|32, 38, 0|tan|Rampart}}` và `{{hero row|32, 39, 0|tan|Ufretin|Ranger}}`
— Rampart ở y=38 so với Jeddite y=68 → đúng là **phía bắc**.
Lý do: trích dẫn khớp **và** dữ liệu bản đồ xác nhận độc lập.

---

### C-22
Claim: Jabarkas **không** phải đồng minh mà là đối thủ tranh artifact trong cùng liên minh;
**không có tương tác trực tiếp nào** được mô tả
Nhãn bài gán: T1* EXPLICIT · sod-target (Day 24)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: toàn bộ `Target` (8 timed event + 5 map event)
Tìm thấy: Day 24 (trích ở C-06) là **chỗ duy nhất** cả hai tên xuất hiện cùng nhau, và ở đó họ ở
hai phía đối lập về chuyện artifact. Map event (15,27,0) nói về Jabarkas nhưng **không nhắc
Jeddite**. Cấu trúc phe: `| allies = {{red}}` (chỉ Sandro) — Jabarkas là `orange` (đợt 1),
Jeddite là `blue` (đợt 2), là **hai người chơi riêng**.
Lý do: claim phủ định đứng vững sau khi đọc hết trang. Không có đoạn thoại/thư/event nào giữa hai
người.

---

### C-23
Claim: **không liên hệ trong bất kỳ nguồn nào** với Vidomina, Finneas, Gelu, Crag Hack, Gem, Yog
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONFIRMED**
Mức: NOTE
Đã tìm ở: 68 backlink của `Jeddite`; danh sách hero của cả 6 scenario ngoài `Target`; Fandom
search 30 kết quả
Tìm thấy: backlink tới `Jeddite` gồm `Sandro`, `Ethric`, `Ufretin`, `Target` — **không** có
Vidomina/Finneas/Gelu/Crag Hack/Gem/Yog. Hero cùng map với hắn ở các scenario Chronicles:
`Tarnum`, `Valita`, `Gunnar`, `Lorelei`, `Dace`, `Xarfax`, `Deemer`, `Damacon`, `Rashka` — không
ai trong sáu người.
Lý do: claim phủ định đứng vững.
**NOTE (thiếu, không phải sai):** hắn là **hero địch của Tarnum ở bốn scenario Heroes Chronicles**
(`The Dragon Mothers`, `Dragons of Deepest Blue`, `Tarnum the Overlord`, `Old Wounds`). Đó là quan
hệ "cùng map" đáng ghi nhận nhất mà bài đang không có, và nó liên quan trực tiếp tới C-26.

---

### C-24
Claim: Fandom có **hai** nhân vật cùng tên — `Jeddite (Enroth)` và `Jeddite (Ashan)` (Warlock và
Demon cultist trong *Might & Magic: Heroes VI*)
Nhãn bài gán: T6 EXPLICIT · fandom-jeddite-disambig
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `mightandmagic.fandom.com/api.php?action=parse&page=Jeddite&prop=wikitext`
Tìm thấy — nguyên văn toàn bộ trang:

```
{{Disambig}}
*[[Jeddite (Enroth)]], a [[Warlock (H3)|Warlock]] and a [[Sorcerer (H4)|Sorcerer]] from
''[[Heroes of Might and Magic III: The Restoration of Erathia|Heroes III]]'' and
''[[Heroes of Might and Magic IV|Heroes IV]]''.
*[[Jeddite (Ashan)]], a [[Warlock (H6)|Warlock]] and a Demon cultist from
''[[Might & Magic: Heroes VI|Heroes VI]]''.
```

Lý do: khớp **từng chữ**, kể cả "Demon cultist".
**BH-2 đã thực hiện:** `api.php?action=query&list=search&srsearch=Jeddite&srlimit=30` trả 30
trang; nhân vật duy nhất mang tên này là `Jeddite (Ashan)` và `Jeddite (Enroth)`. **Không có**
Jeddite nào trong Might and Magic RPG hay Heroes Chronicles (khác ca `Sandro (Xeen)`). Claim phủ
định ngầm này đứng vững.

---

### C-25
Claim: trang `Heroes from other games` xếp portrait H3 và H6 cùng hàng — đó là bảng **so sánh
portrait**, không phải claim về đồng nhất danh tính
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONFIRMED** (và mạnh hơn bài nói)
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Heroes_from_other_games&action=raw`, dòng 290 và
397–401
Tìm thấy — câu dẫn bảng nói **thẳng** điều bài chỉ suy ra:

```
The following table contains all heroes that also appeared in ''Might & Magic: Heroes VI'',
''Might & Magic: Heroes VII'', and ''Might & Magic X: Legacy''. Since ''Heroes VI'' was a
celebration of the ''Might & Magic'' franchise's 25th anniversary, a number of heroes were given
equivalents on Ashan. These characters are not the same as the ones in ''Heroes III'', since
Ashan exists in a separate continuity.
```

Và hàng của hắn: `[[Jeddite]]` / `[[File:Hero Jeddite (HotA).png]]` / `[[File:Hero Jeddite Heroes VI.png|90px]]`
Lý do: nguồn **tự khẳng định** "These characters are not the same". Bài nên **trích câu này** —
nó nâng claim từ suy luận lên EXPLICIT, và cộng hưởng với `CANON-POLICY.md` R5.

---

### C-26
Claim: danh sách xuất hiện — `Target` (SoD, *Rise of the Necromancer*); `The Dragon Mothers` +
`Dragons of Deepest Blue` (SoD, *Clash of the Dragons*); `Tarnum the Overlord` (SoD, *The Sword
of Frost*); `Old Wounds` (SoD, *Contested Underworld*); `A Friendly Visit` (AB, *Armageddon's
Blade*); `Homecoming` (HotA, *Terror of the Seas*); Heroes IV roster Asylum
Nhãn bài gán: T1* EXPLICIT · h3wiki-jeddite
Phán quyết: **CONTRADICTED**
Mức: **BLOCKER**
Đã tìm ở: `api.php?action=query&list=backlinks&bltitle=Jeddite&bllimit=500` (68 trang), rồi
`?action=raw` từng trang scenario để đọc `| source =` và `{{campaign navigational box}}`
Tìm thấy — **sáu trong tám mục bị gán sai sản phẩm hoặc sai campaign**:

| Mục | Bài ghi | Nguồn thật ghi |
|---|---|---|
| `The Dragon Mothers` | SoD, *Clash of the Dragons* | `\| source = hc` · `\| cback = chronicles 4` → **Heroes Chronicles** |
| `Dragons of Deepest Blue` | SoD, *Clash of the Dragons* | `\| source = hc` · `\| cback = chronicles 4` → **Heroes Chronicles** |
| `Tarnum the Overlord` | SoD, *The Sword of Frost* | `\| source = hc` · `\| cback = chronicles 8` → **Heroes Chronicles** |
| `Old Wounds` | SoD, *Contested Underworld* | `\| source = hc` · `\| cback = chronicles 2` → **Heroes Chronicles**, campaign *Conquest of the Underworld* |
| `A Friendly Visit` | **AB**, *Armageddon's Blade* | `\| source = hota` · `\| cback = hota ai 1` · `{{campaign navigational box\|hota=expanded\|allin=expanded}}` → **HotA**, campaign ***All In*** |
| `Homecoming` | HotA, *Terror of the Seas* | `\| source = hota` · `\| cback = hota fif 8` · `{{campaign navigational box\|hota=expanded\|forgedinfire=expanded}}` → HotA, campaign ***Forged in Fire*** |

`Clash of the Dragons`, `The Sword of Frost` và `Conquest of the Underworld` là campaign **Heroes
Chronicles**, không phải Shadow of Death. Ufretin (`h3wiki-ufretin`) tự xác nhận độc lập: "He
later fought alongside `[[Tarnum]]` in the events of `[[Clash of the Dragons]]` and against him
in `[[The Sword of Frost]]`" — Tarnum là nhân vật Chronicles.
"*Contested Underworld*" là **tên campaign không tồn tại**; tên đúng là *Conquest of the
Underworld*. "*Terror of the Seas*" tồn tại nhưng là **campaign HotA khác**
(`Template:Campaign navigational box` có cả `[[All In]]`, `[[Forged in Fire]]`,
`[[Terror of the Seas]]` là ba mục riêng).

Và **danh sách còn thiếu bốn nhóm xuất hiện**, tất cả tìm ra bằng backlinks:

1. **`Jungle Fever`** — `| version = H4X2` → **Heroes IV: Winds of War**, single scenario, Expert,
   Jeddite là **địch duy nhất được nêu tên**, có text truyện riêng (xem C-18). Trang này **không
   tồn tại trên thelazy** — chỉ có trên Fandom. Đây là **xuất hiện có cốt truyện thứ hai** của
   nhân vật, và bài đang nói `Target` là "lần duy nhất có cốt truyện".
2. **`A Cold Day in Hell`** — `| source = hota`, `{{SingleScenario}}`. Nguyên văn:
   `{{H|Jeddite|Warlock}} with 17 {{Cn|Harpy Hag}}s in prison at 63, 1.` → hắn là **tù nhân trong
   Prison**, có quân cố định. Vai trò cơ chế khác hẳn "một dòng đặt hero lên map".
3. **`Myth and Legend`** — `| source = roe`, `{{SingleScenario}}`, XL. Xem **C-28**.
4. **`Battle of the Sexes`** — `| source = sod`, `{{SingleScenario}}`; Jeddite nằm trong bảng chia
   hero Dungeon theo phe nam/nữ. Cộng thêm **8 trang template thi đấu HotA** (`H3dm1`, `Mt Jebus`,
   `Mt Andromeda`, `Mt Antares`, `Mt Diamond`, `Mt Firewalk`, `Mt TeamJebus`, `Battle of the
   Sexes`) liệt kê hắn trong `*Banned heroes:` — xem NOTE ở C-31.

Lý do BLOCKER: registry đã ghi rõ **"gán sai sản phẩm đã từng là BLOCKER"**, và đây là lần thứ
tư liên tiếp lỗi này xuất hiện. Thêm nữa `h3wiki-jeddite` **có** chứa `{{appear}}` (khác ca ba
trang artifact), nhưng template đó **chỉ liệt kê campaign scenario** — nó **không** chứa
`Jungle Fever`, `A Cold Day in Hell`, `Myth and Legend`, `Battle of the Sexes`. Vậy dẫn
`h3wiki-jeddite` cho một danh sách "xuất hiện" đầy đủ vẫn là mis-citation. Mỗi dòng phải có source
key riêng của chính trang scenario đó.

---

### C-27
Claim: **sáu scenario ngoài `Target` đều chỉ có đúng một dòng** đặt hero lên map — không thoại,
không event, không prologue nào
Nhãn bài gán: (không gán nhãn)
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `?action=raw` của cả sáu trang, grep "Jeddite"
Tìm thấy: đúng — mỗi trang có **đúng một** dòng chứa "Jeddite":

```
The Dragon Mothers      : {{hero row|68, 34, 0|red|Jeddite|Warlock}}
Dragons of Deepest Blue : {{hero row|6, 3, 0|red|Jeddite|Warlock}}
Tarnum the Overlord     : {{hero row|5, 26, 0|red|Jeddite|Warlock}}
Old Wounds              : {{hero row|102, 66, 0|purple|Jeddite|Warlock}}
A Friendly Visit        : {{hero row|52, 26, 1|orange|Jeddite|Warlock}}
Homecoming (HotA)       : {{hero row|70, 40, 1|pink|Jeddite|Warlock|image=Jeddite (HotA)}}
```

Lý do: claim **đúng với sáu scenario được nêu**, nhưng **sai ở tính đầy đủ** — chữ "ngoài
`Target`" hàm ý đã quét hết. Thực tế `Jungle Fever` có cả một đoạn text truyện, và
`A Cold Day in Hell` đặt hắn vào Prison kèm quân cố định. Phải viết lại thành "sáu scenario
campaign này…" và bổ sung hai mục kia, hoặc bỏ chữ mang nghĩa đầy đủ.

---

### C-28
Claim: **không xuất hiện trong Restoration of Erathia**
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: backlinks → `heroes.thelazy.net/index.php?title=Myth_and_Legend&action=raw`
Tìm thấy:

```
{{SingleScenario
| source         = roe
| size           = XL
{{hero row| 90, 123, 0|purple|Jeddite    |Warlock     |name=Abaris     |other=[[wikipedia:Abaris the Hyperborean|(ref)]]}}
```

Lý do: `| source = roe` → map ship kèm **Restoration of Erathia**, và hero Jeddite **có mặt trên
map**, chỉ bị **đổi tên hiển thị thành "Abaris"** (`|name=Abaris`) cho chủ đề thần thoại Hy Lạp
của map. Đây là map Single/Multiplayer độc lập, không thuộc campaign — giống ca `roe-all-for-one`
đã có trong registry.
Claim phủ định tuyệt đối là **sai**. Cách diễn đạt đúng: "Jeddite **không có vai trò cốt truyện**
trong Restoration of Erathia; slot hero của hắn được dùng lại dưới tên **Abaris** trong map độc
lập `Myth and Legend`."

---

### C-29
Claim: Town Dungeon; Class Warlock; Race Human; Specialty Resurrection; kỹ năng khởi đầu
Advanced Wisdom (**chỉ một**); spell khởi đầu Resurrection; **Hero ID 91**; Movement **1560**
Nhãn bài gán: T1* EXPLICIT · h3wiki-jeddite
Phán quyết: **DOWNGRADE** (mis-citation một trường)
Mức: **MAJOR**
Đã tìm ở: `Jeddite` (thelazy) — toàn bộ 1.718 byte; `Reference_IDs` dòng 934–938
Tìm thấy trên `Jeddite`:

```
| town       = Dungeon
| class      = Warlock
| gender     = Male
| race       = {{gl|Human}}
| specialty  = Resurrection
| skill_1    = Advanced Wisdom
| spell      = Resurrection
| s_mp       = 1560
```

**Trang không có trường nào cho Hero ID.** ID 91 nằm ở trang khác:

```
| 90 || {{H|Malekith|0=}}
| 91 || {{H|Jeddite|0=}}
```

Lý do: bảy trong tám thông số CONFIRMED. "Hero ID 91" là **EXPLICIT trỏ vào chỗ trống** trên
`h3wiki-jeddite` — đúng loại lỗi `CANON-POLICY.md` mục 2 cấm, và đúng loại lỗi đã bắt ba lần ở
các bài artifact. Cần **source key mới** cho trang `Reference IDs`.
Xác nhận thêm "**chỉ một** kỹ năng khởi đầu": có `skill_1`, **không có** `skill_2`. Kiểm chéo
`Alamar` (cùng specialty Resurrection) có `skill_1 = Basic Wisdom` **và** `skill_2 = Basic
Scholar` → khác biệt là thật, không phải trang thiếu dữ liệu.

---

### C-30
Claim: "Casts Resurrection with effect increased by **5%** (HotA: **3%**) for every N hero levels…"
Nhãn bài gán: (không gán nhãn riêng) · h3wiki-jeddite
Phán quyết: **CONTRADICTED**
Mức: **BLOCKER**
Đã tìm ở: `Template:Swh`; `Jeddite`; `Hero_specialty` dòng 147+149;
`Horn_of_the_Abyss_(Changelog)` dòng 7 + 220
Tìm thấy — **định nghĩa template quyết định vấn đề**:

```
Usage:
{{swh|content to be visible only when hota is ENABLED|content to be visible only when hota is DISABLED}}
```

Tức **tham số 1 = HotA, tham số 2 = SoD**. Trang `Jeddite` ghi
`| s_text = Casts Resurrection with effect increased by {{swh|5%|3%}} for every N hero levels…`
→ **HotA = 5%, SoD = 3%**. Bài đã **đảo ngược hai giá trị**.

Ba nguồn độc lập xác nhận chiều đúng:

**1.** `Hero_specialty` dòng 147 → SoD = 3%:

```
The normal/common spell specialty increases the efficiency of the spell (after spell power and
base spell effect is calculated) by {{swh|10%|3%}} per level, divided by target creature's level.
```

**2.** `Hero_specialty` dòng 149 → HotA Resurrection = 5%:

```
{{showwithhota|{{wh}} For [[Meteor Shower]], [[Chain Lightning]], [[Resurrection]] and
[[Animate Dead]] specialties, this effect is 5% instead (i.e. using the formula C*(1+0.05 * ''L''
/ ''n'')).}}
```

**3.** `Horn_of_the_Abyss_(Changelog)`, mục `== Version 1.8.0 (31/DEC/2025) ==` (dòng 7), dòng 220:

```
[+] Enhanced specializations that add +3% to a spell's effect for n hero levels, where n is the
target's Tier: changed to +5% for Meteor Shower, Chain Lightning, Resurrection and Raise Dead;
+10% for all other spells
```

Kiểm chéo chiều template bằng một hero khác: `Ufretin` có `{{swh|20%|5%}}` cho specialty Dwarves;
SoD dùng công thức +5%/tier chuẩn, còn changelog 1.8.0 dòng 229 ghi creature specialization thành
"+20% for other creatures" → khớp đúng chiều tham số 1 = HotA.

Lý do BLOCKER: con số sai chiều, tức bài nói HotA **yếu hơn** SoD trong khi thực tế HotA **mạnh
hơn**. Thêm nữa claim **thiếu phạm vi phiên bản** — theo changelog, +5% cho Resurrection chỉ có
**từ HotA 1.8.0 (31/DEC/2025)**; trước đó HotA dùng cùng 3% như SoD. Đúng đúng cái bẫy registry
đã ghi trong cảnh báo "Giá trị Necromancy ĐÃ ĐỔI qua các bản HotA".
Cách viết đúng: SoD = **3%**; HotA trước 1.8.0 = 3%; HotA từ **1.8.0** = **5%**. Dẫn
`hota-changelog`, không dẫn trang hero (BH-3).

---

### C-31
Claim: quân khởi đầu Troglodytes 20–30 (HotA 30–40), Harpies 6–8 (HotA 4–6), Beholders 3–4
Nhãn bài gán: (không gán nhãn riêng) · h3wiki-jeddite
Phán quyết: **CONTRADICTED**
Mức: **BLOCKER**
Đã tìm ở: `Jeddite`; `Template:Swh`
Tìm thấy:

```
| nmb_1      = {{swh|noicon=|20–30|30–40}}
| nmb_2      = {{swh|noicon=|6–8|4–6}}
| nmb_3      = 3–4
```

Lý do: cùng lỗi đảo chiều như C-30. Theo `Template:Swh` (tham số 1 = HotA, tham số 2 = SoD):

| Quân | SoD | HotA |
|---|---|---|
| Troglodyte | **30–40** | **20–30** |
| Harpy | **4–6** | **6–8** |
| Beholder | 3–4 | 3–4 |

Bài ghi ngược cả hai stack đầu. Beholder 3–4 (không có `{{swh}}`) là mục duy nhất đúng.
Kiểm chéo: `Alamar` có **y hệt** ba dòng `nmb_` này → đây là dữ liệu chuẩn của specialty
Resurrection, không phải riêng Jeddite; đảo chiều sẽ lan sang mọi bài hero sau này.
**NOTE (thiếu, đáng thêm):** changelog HotA **`== Version 1.6.0 (01/JAN/2020) ==`** dòng 902:
`[-] For all mirror templates, Jeremy is now allowed, while Alamar, Jeddite, Labetha, Grindan,
and Miriam are banned`. Xác nhận độc lập bằng `H3dm1`: `*Banned heroes:` … `**{{h|Jeddite|0=}}`.
Đây là dữ kiện gameplay HotA thật, có phạm vi phiên bản rõ, và bài đang không có.

---

### C-32
Claim: **không có level hay chỉ số cố định** — vì hắn là hero chuẩn
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONFIRMED**
Mức: NOTE
Đã tìm ở: cả 6 scenario campaign + `A Cold Day in Hell` + `Myth and Legend` + `Target`
Tìm thấy: mọi dòng đặt hắn lên map đều ở dạng `{{hero row|x, y, l|<màu>|Jeddite|Warlock}}` —
không `primary skills`, không level. Đối chiếu trong cùng trang `A Cold Day in Hell`, các hero
khác **có** chỉ số:

```
{{H|Ash|Heretic}} with one {{Cn|Efreet Sultan}}, primary skills 2/2/3/2, Bloodlust and Fireball
at 63, 14.
```

Lý do: claim đứng vững — và mạnh hơn vì có **đối chứng trong cùng một trang**.
NOTE: ở `A Cold Day in Hell` hắn **có quân cố định** (`with 17 {{Cn|Harpy Hag}}s in prison`),
không có chỉ số cố định. Nên viết "không chỉ số/level cố định", đừng viết "không gì cố định".

---

### C-33
Claim: hero chuẩn, xác minh ba cách — (1) dùng template `HeroNew` không phải `CampaignHero`;
(2) vắng mặt trong `List of campaign heroes`; (3) trang `Dungeon` khuyến nghị hắn
Nhãn bài gán: T1* EXPLICIT · h3wiki-jeddite + h3wiki-dungeon
Phán quyết: **DOWNGRADE** (cách xác minh (1) không hợp lệ)
Mức: **MAJOR**
Đã tìm ở: `Jeddite`, `Finneas`, `Template:CampaignHero`, `Template:Campaign_heroes`,
`List_of_campaign_heroes`, `Dungeon`
Tìm thấy:

- (1) **KHÔNG hợp lệ.** `Finneas` — hero **campaign-only** theo registry — mở đầu bằng
  `{{Campaign heroes}}{{HeroNew`. Tức hero campaign **cũng dùng** `HeroNew`. Dấu hiệu phân biệt
  thật là template nav đứng trước: `{{DungeonHeroesNew}}` (hero chuẩn) so với `{{Campaign heroes}}`
  (redirect tới `Template:Campaign heroes (portrait only)`). `Template:CampaignHero` **có tồn
  tại** (HTTP 200) nhưng là template **hộp hiển thị hero** dùng trong trang scenario, không phải
  marker của trang hero. Vậy "dùng `HeroNew` chứ không `CampaignHero`" **không phân biệt được gì**.
- (2) **CONFIRMED.** `List_of_campaign_heroes` tồn tại (3.585 byte), `grep -c "Jeddite"` = **0**.
- (3) **CONFIRMED**, nguyên văn khớp từng chữ, `Dungeon` dòng 118:
  `* Powerful heroes, e.g. [[Gunnar]] with Logistics specialty, and [[Jeddite]] and [[Alamar]] with [[Resurrection]] spell.`

Lý do: **kết luận đúng** (hắn là hero chuẩn), nhưng một trong ba "bằng chứng" là bằng chứng giả.
Mức MAJOR vì bài trình bày nó như một xác minh độc lập, và người đọc sau sẽ dùng lại phương pháp
sai này cho bài hero khác. Thay (1) bằng: `Jeddite` mở đầu `{{DungeonHeroesNew}}` (nav hero chuẩn
của town Dungeon), trong khi hero campaign-only mở đầu `{{Campaign heroes}}`.

---

### C-34
Claim: bio chính thức H3 — tin đồn về Zenofex
Nhãn bài gán: **T1 EXPLICIT** · h3wiki-herobios-txt
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Translation_Data/HeroBios.txt&action=raw`, **dòng 186**
Tìm thấy (cột EN):

```
Some say that Jeddite has seen the face of Zenofex, but many contend that since Jeddite is still
alive, the rumor of a meeting could not possibly be true.  Jeddite has never confirmed nor denied
the rumor.
```

Lý do: khớp **từng chữ**, kể cả hai khoảng trắng sau dấu chấm. Đây là **`T1` thật** (string table
trích từ game), không phải `T1*` — **nhãn của bài là đúng**. Cùng chuỗi cũng có trên `Jeddite`
trong `| biography =` và trên Fandom `Jeddite (Enroth)` trong `{{text|…}}` → ba lần xác nhận độc
lập.
📌 **Liên quan `B-001`:** đây là claim `T1` thật thứ ba của dự án. Đáng ghi vào registry rằng
`HeroBios.txt` phủ được **mọi** bio hero H3, không chỉ Sandro và Jeddite.

---

### C-35
Claim: bio H3 **không một chữ nào** về Ethric, Sandro, necromancy, hay sự kiện trong `Target`
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `HeroBios.txt` dòng 186; `Jeddite` trường `| biography =`
Tìm thấy: toàn bộ bio là ba mệnh đề về tin đồn Zenofex (trích ở C-34). Không có "Ethric",
"Sandro", "Necromancer", "artifact".
Lý do: claim phủ định phạm vi **hẹp và kiểm được** (một chuỗi 220 ký tự) → đứng vững hoàn toàn.
Đây là ví dụ về claim phủ định *tốt*: giới hạn ở một nguồn xác định.

---

### C-36
Claim: *Zenofex* là **Xenofex**, vua Kreegan; tin đồn này **không bao giờ được nhắc lại ở đâu**
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONFIRMED**
Mức: MINOR (một chữ)
Đã tìm ở: `heroes.thelazy.net/index.php?title=Zenofex&action=raw` và `…title=Xenofex&action=raw`;
68 backlink của `Jeddite`; Fandom search
Tìm thấy: trang `Zenofex` là `#REDIRECT [[Xenofex]]`. Trang `Xenofex` dòng 1:

```
'''Xenofex''', sometimes referred to as '''Zenofex''', is the leader of the [[Kreegan]] invasion
of [[Enroth (planet)|Enroth]].
```

Trang `Xenofex` **không** nhắc Jeddite (grep = 0), và `Xenofex` **không** nằm trong backlink của
`Jeddite`. Fandom `Jeddite (Enroth)` chỉ link `[[Xenofex|Zenofex]]` trong chính đoạn bio.
Lý do: đồng nhất Zenofex = Xenofex **CONFIRMED bằng chính wiki**. "Ngõ cụt" cũng CONFIRMED — tin
đồn không được nhắc lại ở bất kỳ trang nào.
MINOR: nguồn ghi "**leader of the Kreegan invasion** of Enroth", không ghi "**vua** Kreegan". Sửa
thành "kẻ cầm đầu cuộc xâm lăng Kreegan vào Enroth", hoặc dẫn nguồn khác cho chữ "vua".

---

### C-37
Claim: cùng file string table cho thấy bản dịch **Ba Lan và Nga đều để Jeddite là nữ**; lỗi dịch,
không phải lore
Nhãn bài gán: (ghi chú trong ngoặc) · h3wiki-herobios-txt
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Translation_Data/HeroBios.txt` dòng 186, cột PL và RU
Tìm thấy — cột **Ba Lan** (động từ quá khứ **giống nữ** `widziała`, đại từ `Ona`):

```
Niektórzy mówią, że Jeddite widziała twarz Zenofex, inni twierdzą, że nie może to być prawdą
skoro wciąż żyje. Ona sama nigdy nie zaprzecza, ale też nie potwierdza tym pogłoskom.
```

Cột **Nga** (tên đổi thành `Джедитта` dạng nữ, `видела`, `она`, `Сама же`):

```
Говорят, что однажды Джедитта видела лик Зенофекса, однако многие сходятся на том, что раз она
еще жива, слухам об этой встрече вряд ли можно верить. Сама же Джедитта всегда хранила по этому
поводу гробовое молчание.
```

Lý do: CONFIRMED **hai lần độc lập** trong cùng dòng. Bản Nga còn đi xa hơn bài nói — nó **đổi cả
tên** thành dạng nữ `Джедитта` (thêm hậu tố `-а`), không chỉ chia động từ. Chi tiết này đáng thêm.
Đối chứng: trang `Jeddite` ghi `| gender = Male`, cột Pháp không giống nữ, và Fandom ghi
`|gender = Male` → kết luận "lỗi dịch, không phải lore" đứng vững.

---

### C-38
Claim: câu dẫn thư nói "a threatening letter from **the Barbarians due west**" nhưng Jeddite là
xanh dương, Dungeon, **đông nam** (55,68,0); "Barbarian due west" mô tả đúng hơn phe Stronghold
của Jabarkas; **nhiều khả năng là lỗi copy-paste trong game gốc**
Nhãn bài gán: T1* EXPLICIT · sod-target (Day 2)
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `Target` Day 2 + `==== Heroes ====` + `==== Towns ====`; Fandom `Target`
Tìm thấy: `You have just received a threatening letter from the [[Barbarian|Barbarians]] due west.  It reads:`
Dữ liệu bản đồ (Sandro khởi đầu ở 32,61,0):

| Nhân vật | Toạ độ | Hướng so với Sandro | Town |
|---|---|---|---|
| Jeddite (blue) | 55, 68, 0 | **đông nam** | Dungeon |
| Jabarkas (orange) | 6, 30, 0 | **tây bắc** | Stronghold |
| Shiva (green) | 48, 17, 0 | đông bắc | Stronghold |

Xác nhận độc lập từ Fandom `Target` — hắn ở **phía đông**, không phải phía tây:

```
Sandro's nearest opponents are Jeddite in the east and [[Ufretin]] in the north.
```

Lý do: **nửa dữ kiện CONFIRMED** — mâu thuẫn giữa "Barbarians due west" và Jeddite là thật, và
Jabarkas (Barbarian, tây bắc) khớp hơn.
**Nửa còn lại thì không.** "Nhiều khả năng là lỗi copy-paste trong game gốc" là suy đoán về quá
trình sản xuất — không nguồn T1–T4 nào nói vậy, và không có `{{sic}}` hay
`<!--Error in story text-->` ở chỗ này (khác ca Dethmar/Dethard mà registry nêu). Nhãn phải là
`T1* INFERENCE` cho phần suy luận, kèm bước suy luận; hoặc để `DISPUTED`.
**NOTE bổ sung:** Day 24 có mâu thuẫn địa lý **cùng loại** mà bài đang không nêu — text nói "two
other allied `[[stronghold]]` towns to the **North** and to the **Northeast**", nhưng town orange
của Jabarkas ở (6,29,0) là **tây bắc**, không phải bắc/đông bắc. Hai chỗ lệch hướng trong cùng
scenario củng cố cách đọc "text được viết trước khi map chốt" — và đó là lập luận mạnh hơn
"copy-paste".

---

### C-39
Claim: trang Ufretin viết "In Target, Ufretin tried, but failed, with Ethric and Jeddite to
retrieve the Armor of the Damned and Cloak of the Undead King from Sandro." — bài gọi đây là văn
wiki giả định kết quả người chơi thắng
Nhãn bài gán: T6 FAN_THEORY · h3wiki-ufretin
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Ufretin&action=raw`, mục `== Story ==`
Tìm thấy:

```
== Story ==
In [[Target]], Ufretin tried, but failed, with [[Ethric]] and [[Jeddite]] to retrieve the
[[Armor of the Damned]] and [[Cloak of the Undead King]] from [[Sandro]].
```

Lý do: trích dẫn khớp từng chữ. **Kiểm được gợi ý #2 của bảng claim:** câu này nằm trong mục
`== Story ==`, **ngoài mọi template** — đúng khuôn `Terek` mà registry cảnh báo → là **văn biên
tập viên wiki**, tier `T6` là **đúng loại nguồn**. Đánh giá của bài ("giả định kết quả người chơi
thắng") cũng đứng: `Target` không có epilogue (C-14), nên "tried, but failed" không thể lấy từ
game text.

---

### C-40
Claim: infobox Fandom ghi "Alive (as of Heroes IV)"; bài gọi đây là suy luận từ roster, không
text nào khẳng định
Nhãn bài gán: T6 FAN_THEORY · fandom-jeddite-enroth
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: Fandom `api.php?action=parse&page=Jeddite%20(Enroth)&prop=wikitext`
Tìm thấy: `|status = Alive (as of ''Heroes IV'')` — **trích dẫn CONFIRMED từng chữ**.
Lý do: vấn đề là **độ chắc**, hai tầng:

1. `FAN_THEORY` **sai loại**. `CANON-POLICY.md` mục 2 định nghĩa `FAN_THEORY` = "**Không có nguồn
   T1–T4 chống lưng**". Nhưng có: bio H4 in-game trên `h3wiki-jeddite`
   (`{{H4Story|Sorcerer|…}}`) và scenario H4 `Jungle Fever` đều là in-game text `T1*` cho thấy
   hắn hoạt động ở thời Heroes IV. Đúng nhãn là `INFERENCE`.
2. **Mâu thuẫn nội bộ với C-19.** Cùng một mệnh đề ("còn sống tính đến Heroes IV") mang
   `T6 INFERENCE` ở mục *Tiểu sử* và `T6 FAN_THEORY` ở mục *Giả thuyết cộng đồng*. Cảnh báo của
   bảng claim là **đúng**: đây là lỗi. Theo tinh thần `CLAUDE.md` ("nếu hai bên gán độ chắc khác
   nhau thì đó là lỗi"), phải thống nhất **một** nhãn.

Bắt buộc sửa: hợp nhất C-19 và C-40 thành một claim `{T1* INFERENCE: h3wiki-jeddite — vì hắn có
mặt trong roster và bio in-game của Heroes IV, diễn ra sau Reckoning}`, và giữ ở mục *Tiểu sử*.
Mục *Giả thuyết cộng đồng* chỉ nên nói về việc **Fandom trình bày nó như dữ kiện infobox** — đó
mới là điều đáng phê.

---

### C-41
Claim: bốn lỗi gốc trong game text — "find a way use" (Day 2); "By becoming Necromancer" (Day 2);
"Am I suppose run" (thiếu *to* ×2, Day 8); "use them rise" (Day 8)
Nhãn bài gán: T1* EXPLICIT · sod-target
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `Target` — toàn bộ 8 timed event + 5 map event; `grep -c "{{sic"` = **0**
Tìm thấy: cả bốn chuỗi **có thật** trong bản chép:

```
You will have to find a way use this weakness against him.
By becoming [[Necromancer]], you have completely shamed me
Am I suppose run and hide, fearful of your vow to stop me?
where I shall use them rise to the top of the [[Deyja]] hierarchy
```

Lý do — ba vấn đề, đều nhỏ nhưng đều thật:

1. **Nhãn quá cao.** Không có `{{sic}}` nào trên trang → "lỗi có trong **game gốc**" là
   `INFERENCE`, không `EXPLICIT` (giống C-03).
2. **Mô tả sai.** "Am I suppose run" **không phải** "thiếu *to* ×2". Câu đúng là "Am I
   supposed to run": lỗi là **thiếu `-d`** ở *suppose* **và thiếu một `to`**. Hai lỗi khác loại,
   không phải hai lần cùng lỗi. (Đây có thể là lỗi bảng claim — cần đối chiếu bài.)
3. **"Bốn lỗi" không đầy đủ.** `Target` còn ít nhất bốn lỗi nữa, trong đó **hai nằm ngay trong
   event về Jeddite** (Day 24):
   - Day 18: `all the fools ... know about carry the artifacts you carry` (lặp "carry")
   - Day 24: `According to you advisors` (thiếu `r` — *your*)
   - Day 24: `is [[Ethric]]'s illegitimate younger brother suffers from Little Man's Syndrome` (thiếu *who*)
   - Day 24: `A spy returns with word has come about internal conflicts` (câu vỡ cú pháp)

   Nếu bài viết "bốn lỗi" như một thống kê, nó là claim đầy đủ **sai**. Đổi thành "trong đó có
   bốn lỗi", hoặc liệt kê hết.

---

### C-42
Claim (mục *Câu hỏi mở*): tin đồn về Zenofex là gì? Ngõ cụt hoàn toàn
Nhãn bài gán: **T1 UNVERIFIED** · h3wiki-herobios-txt
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `Xenofex`, `Zenofex` (redirect), 68 backlink của `Jeddite`, Fandom search 30 kết quả
Tìm thấy: không nguồn nào mở rộng tin đồn.
Lý do: `UNVERIFIED` **được phép** ở đây — `CANON-POLICY.md` mục 5.3 chỉ cấm trong thân bài, và cột
Mục xác nhận claim nằm ở *Câu hỏi mở*. Không báo lỗi vị trí.
Tier `T1` đúng: nguồn (`HeroBios.txt`) là T1 thật và chính nó nêu tin đồn; điều chưa kiểm được là
**nội dung** tin đồn. Cặp `T1 UNVERIFIED` nghe nghịch nhưng ở đây hợp lý: nguồn cấp cao nói có
tin đồn, dự án không truy được tin đồn nói gì.

---

### C-43
Claim (mục *Câu hỏi mở*): vì sao Ethric chọn Jeddite làm người nhận artifact thay vì tự đi lấy?
Nhãn bài gán: **T1* UNVERIFIED** · sod-target
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: toàn bộ `Target` (Ethric xuất hiện ở Day 1, Day 2, Day 18, map event (40,46,0));
`Master`; `h3wiki-ufretin`
Tìm thấy: `Target` cho thấy Ethric **loan tin** (`he has spread word of your whereabouts`) và
**gửi thư** cho các lãnh chúa (`[[Ethric]]'s message was received this morning`), nhưng **không
xuất hiện trên map** — không có `{{hero row}}` nào cho Ethric. Không đoạn nào giải thích vì sao.
Lý do: câu hỏi mở hợp lệ, ở đúng mục. `UNVERIFIED` được phép theo mục 5.3.
NOTE: dữ kiện "Ethric không có mặt trên map `Target`" là **kiểm được** và đáng nêu — nó làm câu
hỏi mở sắc hơn. Cũng lưu ý `h3wiki-ufretin` viết như thể Ethric **có** tham gia ("Ufretin tried
… **with Ethric and Jeddite**"), trong khi map data nói ngược — thêm một điểm chống lưng cho
đánh giá `T6` ở C-39.

---

### C-44
Claim (mục *Câu hỏi mở*): **không có mô tả ngoại hình**; chỉ có file portrait
Nhãn bài gán: (không gán nhãn)
Phán quyết: **CONFIRMED**
Mức: NOTE
Đã tìm ở: `Jeddite` (bio H3 + bio H4 + `== Story ==`), `HeroBios.txt` dòng 186, toàn bộ `Target`,
6 scenario campaign, `A Cold Day in Hell`, `Myth and Legend`, Fandom `Jeddite (Enroth)`,
`Jungle Fever`
Tìm thấy: không nguồn nào mô tả ngoại hình. Chỉ có file ảnh:
`[[File:Hero Jeddite (HotA).png]]`, Fandom `HeroJedditeIII.jpg` / `HeroJedditeIV.png`.
Lý do: claim phủ định đứng vững — khác ca Sandro (có cảnh Wingtail Tavern mô tả ngoại hình).
NOTE hai điểm bài nên thêm:
- `Jeddite` có `| hpicture = _(HotA)` → **HotA vẽ lại portrait**, và changelog ghi hai lần sửa
  portrait Jeddite (dòng 49 và 690). Tức có **ba** phiên bản hình, không phải một file.
- `Jungle Fever` cho **đặc điểm nhân vật** mới: biệt hiệu "Jeddite **the Reckless**" và việc hắn
  **nuôi rồng**. Không phải ngoại hình, nhưng nó làm câu "chỉ có file portrait, không có gì bằng
  chữ" thành hẹp hơn thực tế.

---

### C-45
Claim: bài tự thống kê 1 nguồn `T1`, 6 nguồn `T1*`, 2 nguồn `T6`
Nhãn bài gán: (bảng thống kê)
Phán quyết: **NOT_FOUND**
Mức: NOTE
Đã tìm ở: chính bảng claim (không được đọc bài gốc)
Tìm thấy: bảng claim chỉ để lộ **7** source key: `h3wiki-herobios-txt` (T1);
`sod-target`, `h3wiki-jeddite`, `h3wiki-dungeon`, `h3wiki-ufretin` (T1* — **4**, không phải 6);
`fandom-jeddite-enroth`, `fandom-jeddite-disambig` (T6 — 2 ✓).
Lý do: không kiểm được từ bảng claim — có thể bài dẫn thêm hai key `T1*` không xuất hiện trong
bảng (ứng viên: `Heroes from other games` ở C-25, `hota-changelog` ở C-30/C-31). **Nhưng bảng
thống kê sẽ phải viết lại bất kể sao**, vì đợt này bắt buộc thêm ít nhất 5 key mới (xem
*Kết luận*), và một key `T4` sẽ làm bài có tier chưa từng có.

---

## Phát hiện ngoài bảng claim

### ⭐ Có nguồn `T4` thật về Jeddite — Lead Designer Heroes III nói về cái tên

Tìm ra qua backlinks (trang `Gregory Fulton/On Names in Heroes of Might and Magic III`, dòng 840):

```
| {{Hn|Jeddite|0=}}
| ■ Possibly a suggestion given to me, with the obvious play on 'Jedi' from Star Wars.
```

Xuất xứ trang, ghi ở đầu: *"Interview posted on 08/AUG/2023 on Celestial Heavens, detailing
Amelrix's correspondence with `[[Gregory Fulton]]` from 2022―2023."* — thư từ dài một năm rưỡi,
khoảng 200 câu hỏi, và **chính Fulton đọc lại bản cuối** trước khi công bố. Registry đã có ba key
Fulton (`fulton-fanstratics-3/13/27`) nên nhân thân nguồn đã được xác lập.

Đây là `T4 EXPLICIT` — tier cao thứ nhì mà dự án có, và bài **đang không có nó**. Không phải
BLOCKER (bài không claim "không có developer commentary"), nhưng đúng loại nguồn mà đợt research
Sandro đã bỏ sót một lần rồi. Đề nghị thêm mục *Trivia*: nguồn gốc cái tên, ghi rõ Fulton tự rào
"Possibly" và "It's difficult to recall after 20+ years" (câu rào ông dùng ở entry `Geon` ngay bên
dưới) → `T4 INFERENCE` cho nguồn gốc, `T4 EXPLICIT` cho việc Fulton **nói vậy**.

### Registry cần sửa hai chỗ

1. Entry `sod-target` ghi "**6 timed event**" — thực tế **8** (Day 1, 2, 6, 8, 13, 18, 24, 36).
2. `h3wiki-jeddite` xuất hiện **hai lần** trong `REGISTRY.md` (dòng 191 và 195) với mô tả khác
   nhau. Gộp lại.

### Ghi chú kỹ thuật cho các đợt sau

- **`Template:Swh` phải đọc trước khi trích bất kỳ số liệu hero/creature nào từ thelazy.**
  `{{swh|A|B}}` → **A = HotA, B = SoD**. Trực giác đọc trái-sang-phải là "SoD trước" và **sai**.
  Lỗi này làm hỏng C-30 và C-31; nó sẽ làm hỏng mọi bài hero/creature sau nếu không ghi lại.
- `api.php?list=search&srsearch=insource:/…/ ` **không hoạt động** trên thelazy (trả rỗng).
  `list=backlinks` là đường duy nhất.
- Fandom: `index.php?…&action=raw` bị Cloudflare chặn (`Just a moment...`); `api.php?action=parse`
  vẫn vào được. Và **Fandom có trang mà thelazy không có** (`Jungle Fever`) → không được coi
  thelazy là bao trùm.

---

## Kết luận

**Bài KHÔNG đủ điều kiện `status: verified`.** Còn **3 BLOCKER** và **8 MAJOR**.

### Bắt buộc sửa — BLOCKER

1. **C-30 — đảo chiều `{{swh}}`, specialty.** SoD = **3%**, HotA = **5%**, và HotA chỉ đạt 5% **từ
   1.8.0 (31/DEC/2025)**; trước đó 3%. Dẫn `hota-changelog` dòng 220, không dẫn trang hero (BH-3).
2. **C-31 — đảo chiều `{{swh}}`, quân khởi đầu.** SoD: Troglodyte **30–40**, Harpy **4–6**.
   HotA: Troglodyte **20–30**, Harpy **6–8**. Beholder 3–4 cả hai.
3. **C-26 — sáu trong tám mục "Xuất hiện" gán sai sản phẩm/campaign, và thiếu bốn nhóm.**
   `The Dragon Mothers`, `Dragons of Deepest Blue`, `Tarnum the Overlord`, `Old Wounds` là
   **Heroes Chronicles** (`source = hc`), không phải SoD. `A Friendly Visit` là **HotA**, campaign
   ***All In*** — không phải AB/*Armageddon's Blade*. `Homecoming` là HotA campaign ***Forged in
   Fire*** — không phải *Terror of the Seas*. "*Contested Underworld*" là tên campaign không tồn
   tại (đúng: *Conquest of the Underworld*). Thiếu: `Jungle Fever` (H4 Winds of War),
   `A Cold Day in Hell` (HotA), `Myth and Legend` (RoE), `Battle of the Sexes` (SoD) + 7 template
   thi đấu HotA. Mỗi dòng phải có source key **của chính trang scenario đó**.

### Bắt buộc sửa — MAJOR

4. **C-08** — bỏ superlative "chi tiết nhất trong toàn Old Universe" (không nguồn; `Jungle Fever`
   và bio H4 cạnh tranh) hoặc hạ xuống `INFERENCE` với phạm vi hẹp lại.
5. **C-18** — "không scenario nào" bị `Jungle Fever` phản bác. Bỏ cả chữ "**cố ý**".
6. **C-27** — bỏ hàm ý đầy đủ; "sáu scenario **campaign**", và thêm hai mục còn lại.
7. **C-28** — "không xuất hiện trong RoE" bị `Myth and Legend` phản bác. Viết lại: không có vai
   trò cốt truyện; slot hero dùng lại dưới tên **Abaris**.
8. **C-29** — Hero ID 91 **không có** trên `h3wiki-jeddite`. Thêm key cho trang `Reference IDs`.
9. **C-33** — cách xác minh (1) không hợp lệ: `Finneas` (campaign-only) **cũng** dùng `HeroNew`.
   Thay bằng `{{DungeonHeroesNew}}` so với `{{Campaign heroes}}`.
10. **C-38** — "nhiều khả năng là lỗi copy-paste" phải là `INFERENCE`, không `EXPLICIT`.
11. **C-40 + C-19** — hợp nhất thành **một** nhãn `T1* INFERENCE`. `FAN_THEORY` sai loại vì có
    nguồn `T1*` chống lưng, và hai độ chắc cho cùng một mệnh đề là lỗi.

### Nên sửa — MINOR/NOTE

- C-03, C-41: `Target` **không có** `{{sic}}` nào → "lỗi có trong game gốc" là `INFERENCE`.
  C-41 còn mô tả sai "Am I suppose run" và chưa đủ (còn ≥4 lỗi nữa, hai nằm trong event Day 24).
- C-17: "Asylum" không có trên `h3wiki-jeddite` → tách source key.
- C-36: nguồn ghi "leader of the Kreegan invasion", không ghi "vua".
- C-37: bản Nga đổi **cả tên** thành dạng nữ (`Джедитта`), không chỉ chia động từ — đáng thêm.
- C-15, C-23, C-27, C-28, C-32, C-35, C-36: đều là claim **phủ định** hiện "(không gán nhãn)".
  `CANON-POLICY.md` mục 5.1 đòi nhãn hai trục cho **mọi** claim thân bài. Claim phủ định không
  nhãn là chỗ dự án đã trả giá nhiều nhất.
- C-23: nên thêm quan hệ "hero địch của **Tarnum** ở bốn scenario Chronicles".
- C-31: nên thêm dữ kiện HotA 1.6.0 **cấm** Jeddite ở mọi mirror template.
- C-45: bảng thống kê nguồn phải viết lại sau khi thêm key.

### Source key mới cần thêm vào `REGISTRY.md`

| key đề nghị | tier | Nội dung |
|---|---|---|
| `fulton-names-2023` | **T4** | `Gregory Fulton/On Names in Heroes of Might and Magic III` — thư từ Amelrix–Fulton 2022–2023, đăng Celestial Heavens 08/AUG/2023. Nguồn gốc tên "Jeddite" (chơi chữ *Jedi*) |
| `h3wiki-reference-ids` | T1* | Trang `Reference IDs` — bảng ID hero/object. **Nguồn duy nhất** cho Hero ID 91 |
| `h3wiki-swh-template` | — | `Template:Swh` — định nghĩa thứ tự tham số HotA/SoD. Không phải nguồn nội dung, nhưng **phải ghi lại** để không lặp lỗi C-30/C-31 |
| `h3wiki-hero-specialty` | T1* | Trang `Hero specialty` — công thức spell specialty SoD (3%) vs HotA (10%, riêng Resurrection 5%) |
| `h3wiki-heroes-other-games` | T6 | `Heroes from other games` — bảng so sánh portrait; chứa câu bác bỏ đồng nhất danh tính Ashan (dùng cho C-24, C-25) và bảng `{{H3H4header\|Asylum\|Dungeon}}` (dùng cho C-17) |
| `fandom-jungle-fever` | T6 → T1* | `Jungle Fever` — single scenario **Heroes IV: Winds of War** (`version = H4X2`); Jeddite là địch duy nhất được nêu tên; text truyện có biệt hiệu "the Reckless" và chi tiết nuôi rồng. **Chỉ có trên Fandom** |
| `hota-a-cold-day-in-hell` | T1* | Single scenario HotA — Jeddite trong Prison tại (63,1) với 17 Harpy Hag |
| `roe-myth-and-legend` | T1* | Single scenario RoE (XL) — hero Jeddite đổi tên hiển thị thành **Abaris** |
| `hc-old-wounds`, `hc-the-dragon-mothers`, `hc-dragons-of-deepest-blue`, `hc-tarnum-the-overlord` | T1* | Bốn scenario **Heroes Chronicles** (`source = hc`) — thay cho việc gán sai SoD |
| `hota-a-friendly-visit`, `hota-homecoming` | T1* | Hai scenario HotA, campaign ***All In*** và ***Forged in Fire*** |
| `h3wiki-h3dm1` | T6 | Template thi đấu — Jeddite trong `*Banned heroes:`; xác nhận độc lập changelog 1.6.0 |

### Lỗi của bảng claim (không phải lỗi bài)

- **C-41**: "Am I suppose run" được mô tả là "thiếu *to* ×2". Sai — lỗi là thiếu `-d` ở *suppose*
  **và** thiếu một `to`. Cần đối chiếu xem bài gốc có ghi vậy hay bảng claim tự diễn giải.
- **C-26**: bảng claim ghi `Old Wounds` thuộc campaign "*Contested Underworld*" — tên này không
  tồn tại ở bất kỳ sản phẩm nào. Nếu bài gốc ghi đúng "*Conquest of the Underworld*" thì đây là
  lỗi bảng claim; nếu bài cũng ghi vậy thì nằm trong BLOCKER C-26.
- **C-19/C-40**: cảnh báo cuối bảng claim về mâu thuẫn nội bộ là **đúng** — đã xác nhận, xếp MAJOR.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. Toàn bộ 3 BLOCKER và 8 MAJOR đã xử lý.

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| C-30, C-31 | Đảo chiều `{{swh}}` — cả ba con số gameplay sai | BLOCKER | **Người sửa tự fetch `Template:Swh` để xác nhận trước khi sửa.** Đúng: tham số 1 = `onlyhota`, tham số 2 = `onlysod`. Viết lại thành bảng SoD/HotA hai cột, thêm mốc 1.8.0, thêm xác nhận độc lập từ `Hero specialty` |
| C-26 | 6/8 mục sai sản phẩm, thiếu 4 mục | BLOCKER | Dựng lại bảng 12 dòng, thêm cột *Sản phẩm*, mỗi dòng một source key. Bốn scenario đổi từ SoD sang **Heroes Chronicles**; `A Friendly Visit` sang HotA/*All In*; `Homecoming` sang *Forged in Fire*. Bỏ campaign **không tồn tại** "*Contested Underworld*" |
| C-18 | "không scenario nào" bị `Jungle Fever` phản bác | MAJOR | Viết lại thành "không nguồn nào **giải thích**". Thêm text `Jungle Fever` với hai dữ kiện mới: biệt hiệu "**the Reckless**" và việc hắn **nuôi rồng**. Bỏ chữ "**cố ý**" (suy đoán về ý định tác giả) |
| C-28 | "không xuất hiện trong RoE" bị `Myth and Legend` phản bác | MAJOR | Sửa thành "không có **vai trò cốt truyện** trong RoE". Thêm dòng bảng: hero Jeddite có mặt (90,123,0) dưới tên hiển thị **Abaris** |
| C-08 | Superlative "toàn Old Universe" không nguồn | MAJOR | Rào phạm vi thành "trong các nguồn dự án đã fetch", gán `INFERENCE` |
| C-27 | "đều chỉ có đúng một dòng" hàm ý sai | MAJOR | Nêu hai ngoại lệ có ý nghĩa cơ chế: `A Cold Day in Hell` (tù nhân trong Prison + 17 Harpy Hag) và `Myth and Legend` (đổi tên) |
| C-29 | Hero ID 91 mis-citation | MAJOR | Thêm `h3wiki-reference-ids` — con số nằm ở trang đó, không ở trang `Jeddite` |
| C-33 | Cách xác minh (1) vô hiệu | MAJOR | **Bỏ** cách đó và nói rõ vì sao: hero campaign-only cũng dùng `{{HeroNew}}` (ví dụ `Finneas Vilmar`). Hai cách còn lại vẫn đứng nên kết luận không đổi |
| C-38 | "lỗi copy-paste" gán EXPLICIT | MAJOR | Tách: câu dẫn + vị trí = `EXPLICIT`; nguyên nhân = `INFERENCE` |
| C-19 + C-40 | Cùng mệnh đề, hai độ chắc; `FAN_THEORY` sai loại | MAJOR | Hợp nhất về mục *Tiểu sử* dưới `INFERENCE`. Giữ mục ở *Giả thuyết cộng đồng* nhưng đổi thành ghi nhận sự nhầm lẫn, và nêu rõ `FAN_THEORY` sai loại vì mệnh đề có nguồn `T1*` |
| C-03, C-41 | "lỗi có trong game gốc" | MINOR | Trang `Target` **không có `{{sic}}` nào** → tách thành `INFERENCE`, ghi rõ suy từ tập quán đánh dấu lỗi của wiki. Sửa mô tả lỗi "Am I suppose run". Ghi rõ danh sách **không đầy đủ** |
| C-37 | — | NOTE | Mạnh hơn bài nói: bản Nga đổi **cả tên** thành `Джедитта` |

### Nguồn `T4` mới — giá trị vượt xa bài này

Verifier tìm được `Gregory Fulton/On Names in Heroes of Might and Magic III` (98.499 byte, thư từ
2022–2023 với **Lead Designer Heroes III**, do chính ông xem lại trước khi công bố).

Người sửa đã tự fetch và grep toàn bộ để đánh giá phạm vi: tài liệu có entry cho `Jeddite`,
`Ufretin`, `Jabarkas`, `Vidomina`, `Thant`, `Deyja` — **nhưng KHÔNG có `Sandro` và `Ethric`**
(0 lần). Đã ghi thành `B-020` kèm bảng nội dung dùng được, trong đó etymology của **Deyja** dùng
ngay được cho bài `deyja` đang chờ verify.

### Hai lỗi của bảng claim, không phải của bài

Verifier chỉ ra đúng — ghi lại theo quy tắc mới ở `VERIFY-PROTOCOL.md` mục 7:

1. **C-41:** người soạn bảng mô tả "Am I suppose run" là "thiếu *to* ×2". Sai — lỗi là thiếu `-d`
   (*supposed*) và thiếu một `to`. Bài gốc ghi đúng hơn bảng claim.
2. **C-26:** người soạn ghi campaign "*Contested Underworld*". Tên đó không tồn tại — nhưng **bài
   gốc cũng ghi vậy**, nên đây vừa là lỗi bài (đã sửa) vừa được bảng claim chép lại nguyên.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-jeddite-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.
