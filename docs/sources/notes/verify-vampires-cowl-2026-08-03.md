# Verify report: vampires-cowl — 2026-08-03

Verifier: agent độc lập, không đọc bài gốc, không đọc `docs/sources/raw/`, không đọc
các bài cùng cụm (`cloak-of-the-undead-king`, `dead-mans-boots`,
`amulet-of-the-undertaker`), không đọc báo cáo verify trước.

Số claim kiểm: 30

CONFIRMED: 12 | DOWNGRADE: 17 | NOT_FOUND: 0 | CONTRADICTED: 1

**Đủ điều kiện `status: verified`? — CHƯA.** Còn 1 BLOCKER và 11 MAJOR. Chi tiết ở
`## Kết luận`.

---

## Ghi chú phương pháp

Toàn bộ nguồn lấy bằng `curl ... ?action=raw` (wikitext thô) trên
`heroes.thelazy.net`, cộng `api.php` cho backlinks/category/revisions. Nguyên tắc phân
biệt loại nguồn dùng suốt báo cáo này:

- Text nằm **trong tham số template** (`| event =`, `| biography =`, `| description =`,
  `| victory =`, `{{TErow|...}}`, `{{SorQrow|...}}`) = bản chép **in-game text** → `T1*`.
- Text nằm **ngoài mọi template** (mục `== Story ==`, văn xuôi thân trang) = **văn biên
  tập viên wiki** → `T6`. Gán `T1*` cho loại này là sai **loại** nguồn.

Quét toàn diện thay cho việc tin danh sách của bài:

```
api.php?action=query&list=backlinks&bltitle=Vampire's Cowl&bllimit=500
```

194 kết quả. Giao với `Category:Campaign scenarios` + `Category:Single and Multiplayer
Scenarios` + `Category:Generated Maps` + `Category:Horn of the Abyss`, rồi trừ nhiễu
(các trang artifact khác link qua bảng slot Cape) → **12 trang nội dung game** nhắc tới
Cowl. Bài kể 10. Hai trang bị bỏ: `After the Amulet` và `Mormolykos` (xem C-18, C-29).

⚠️ **Sửa registry:** tiêu đề trang changelog là `Horn of the Abyss (Changelog)`.
URL kiểu `Horn_of_the_Abyss/Changelog` trả **HTTP 404**.

---

## Chi tiết

### C-01
Claim: Cowl là thành phần **thứ hai** của Cloak; là món có tuyến truyện riêng **thú vị
nhất**; nó **không nằm trên bản đồ**, mà đến kèm một tù nhân phải chuộc 40.000 vàng.
Nhãn bài gán: (không gán nhãn), không source key
Phán quyết: **DOWNGRADE**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Cloak_of_the_Undead_King&action=raw` ·
`?title=After_the_Amulet&action=raw` · `?title=New_Beginning&action=raw` ·
`?title=Taming_of_the_Wild&action=raw` · `?title=Here_There_Be_Pirates&action=raw`
Tìm thấy: trang Cloak xếp thứ tự thành phần thẳng trong template —

```
 | art_1   = Amulet of the Undertaker
 | art_2   = Vampire's Cowl
 | art_3   = Dead Man's Boots
```

Thứ tự thu thập trong truyện khớp: `After the Amulet` Day 21 — "he needs three lesser
artifacts:  an Amulet of the Undertaker, a Vampire's Cowl and a pair of Dead Man's
Boots" — rồi `Retrieving the Cowl` Day 27 (Gem đã có Amulet, còn Cowl và Boots).
Lý do: "**thứ hai**" đứng vững ở hai trục độc lập (`art_2` + thứ tự thu thập) → phần này
đủ `T1* EXPLICIT`. Ba điều phải sửa:

1. **"không nằm trên bản đồ" phải giới hạn phạm vi vào `Retrieving the Cowl`.** Nói
   chung thì **sai**: Cowl là object trên bản đồ ở `Taming of the Wild` (69, 4, 0) và
   `Here There Be Pirates` (31, 37, 0). Xem C-22, C-23.
2. **"thú vị nhất"** là nhận định biên tập, không có nguồn — phải tách khỏi câu có nhãn.
3. **Đừng lẫn "thành phần thứ hai" với "scenario thứ hai".** `New Beginning` có **bốn**
   map (`Clearing the Border` → `After the Amulet` → `Retrieving the Cowl` → `Driving
   for the Boots`); `cback` xác nhận `sod nb 2/3/4`. Cowl là thành phần **thứ hai** nhưng
   ở map **thứ ba**.

### C-02
Claim: Text khi nhặt — "You manage to find a Vampire's resting place during the day, and
are able to slay him easily. Just for good measure, you take his cowl."
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Vampire%27s_Cowl&action=raw` ·
`?title=Artifact_Events&action=raw`
Tìm thấy: trong tham số `| event =` của `ArtifactNewSB` —

```
 | event  = You manage to find a {{gl|Vampire|Vampire's}} resting place during the day, and are able to slay him easily. Just for good measure, you take his cowl.
```

Xác nhận **độc lập** trên trang `Artifact Events` (35.645 byte, mở đầu "Default
descriptions when picking an artifact."), dòng 171 —

```
{{An|Vampire's Cowl}}: You manage to find a [[Vampire]]'s resting place during the day, and are able to slay him easily. Just for good measure, you take his cowl.
```

Lý do: trích khớp từng chữ, nằm trong tham số template, và có hai trang độc lập chép
giống nhau. Nhãn `T1* EXPLICIT` đúng. **Nên dẫn thêm `h3wiki-artifact-events`** — đây là
xác nhận độc lập miễn phí, registry đã có key.

### C-03
Claim: Cowl **không phải Gem tìm ra**. Sandro đã thuê một tay sai **trước đó**, và người
đó **thất bại**.
Nhãn bài gán: (không gán nhãn riêng), không source key
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw`
Tìm thấy: prologue (thoại Gem) —

```
When I delivered the [[Amulet of the Undertaker]] to [[Sandro]], he told me he had also hired a [[Barbarian]] named [[Terek]] to locate another artifact, The [[Vampire's Cowl]].  However, [[Terek]] is long overdue and [[Sandro]] fears for his life.
```

và `| region_text =` —

```
[[Terek]], [[Sandro]]'s agent, managed to steal a [[Vampire's Cowl]].  Unfortunately, on his way across the Border Lands bandits captured him.
```

Lý do: "không phải Gem tìm ra" và "thuê trước đó" — CONFIRMED, đủ `T1* EXPLICIT` với key
`sod-retrieving-the-cowl`. Hai chỗ phải sửa:

1. **"người đó thất bại" là sai sắc thái.** Terek **thành công** ở việc lấy Cowl
   ("managed to steal a Vampire's Cowl", "has located the Vampire's Cowl for Sandro") và
   chỉ thất bại ở việc **giao hàng**. Diễn đạt an toàn: lấy được nhưng không mang về được.
2. ⚠️ **Bẫy caption wiki.** Chú thích gallery trên **ba** trang (`Vampire's Cowl`,
   `Gem (Sorceress)`, `Seeing Pool`) ghi `Gem using a [[Seeing Pool]] to scry for the
   [[Vampire's Cowl]]`. Đọc thẳng thì thành "Gem soi tìm ra Cowl" — **ngược** với C-03.
   Game text nói khác: Day 1 "**My scrying has shown he is being held** in an underground
   prison" — Gem soi ra **Terek**, không phải Cowl. Caption là văn biên tập (`T6`), không
   được dùng để chống lưng hay phản bác.

### C-04
Claim: **Terek** là một barbarian, class **Battle Mage**, người đầu tiên Sandro thuê đi
lấy Cowl.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-terek`
Phán quyết: **DOWNGRADE**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Terek&action=raw`
Tìm thấy: infobox `HeroNew` —

```
 | town       = Stronghold
 | class      = Battle Mage
 | race       = {{gl|Human}}
 | biography  = Terek spent several years as a strong-man in the {{gl|Circus of the Sun}}... the man who had beaten him recruited him for the {{gl|Krewlod}} Army.
```

Lý do: `class = Battle Mage` CONFIRMED. Nhưng **`h3wiki-terek` không chứa chữ
"barbarian" ở đâu cả** — chữ đó đến từ `sod-retrieving-the-cowl` (prologue và Day 1 đều
ghi `[[Barbarian]] named [[Terek]]`). Mis-citation nhỏ: phải dẫn hai key, không một.

Đáng ghi thêm: game text gọi hắn **Barbarian** trong khi class thật là **Battle Mage**
(class phép của Stronghold, không phải class might). Đây là **lệch trong chính tư liệu
in-game**, không phải lỗi wiki — nên nói rõ chứ đừng làm phẳng thành "barbarian class
Battle Mage" như thể hai thứ cùng nghĩa. Bio in-game chỉ chống lưng "người Krewlod",
không chống lưng class Barbarian.

### C-05
Claim: Trích "In Retrieving the Cowl, Terek was **the first hero Sandro hired** to
retrieve the Vampire's Cowl. He was captured and imprisoned by bandits until Gem arrived
and ransomed him and the cowl."
Nhãn bài gán: `T1* EXPLICIT: h3wiki-terek`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Terek&action=raw`
Tìm thấy: câu tồn tại **nguyên văn**, nhưng nó nằm ở mục `== Story ==`, **ngoài mọi
template** —

```
== Story ==
In [[Retrieving the Cowl]], Terek was the first hero [[Sandro]] hired to retrieve the [[Vampire's Cowl]]. He was captured and imprisoned by bandits until [[Gem]] arrived and ransomed him and the cowl.
```

Lý do: **nghi vấn của bảng claim là đúng.** Đây là văn biên tập viên wiki tóm tắt
scenario, **không phải chuỗi text nào hiện ra trong game**. In-game text của trang này
nằm ở `| biography =` — và bio đó nói về Circus of the Sun và quân Krewlod, **không nhắc
Sandro, không nhắc Cowl, không nhắc bị bắt**. Vậy `T1*` sai **loại** nguồn, không chỉ
sai cấp. Nhãn đúng: `T6`, và theo `CANON-POLICY.md` mục 2 thì `T6` tối đa là
`INFERENCE`/`UNVERIFIED`.

**Không cần dùng câu này.** Cùng một nội dung có nguồn `T1*` thật, mạnh hơn:

- "thuê đầu tiên / trước Gem" → prologue + `| region_text =` của
  `sod-retrieving-the-cowl` (xem C-03).
- "bị cướp bắt và giam" → Day 1 + `{{hero row|54, 43, 1|{{imprisoned}}|Terek|Battle Mage}}`.
- "Gem chuộc" → Quest Guard `{{SorQrow|...}}` (xem C-08).

Chỉ mảnh "**ransomed him and the cowl**" là không có nguồn `T1*` — và đó chính là mảnh
C-19/C-30 xoay quanh.

### C-06
Claim: Trích Day 1 về Terek bị Bandits ở Contested Lands bắt và thuyết phục chúng đòi
tiền chuộc.
Nhãn bài gán: `T1* EXPLICIT: sod-retrieving-the-cowl (Day 1)`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw`
Tìm thấy: `=== Timed events ===`, `{{TErow| 1 |Intro|...}}` —

```
{{TErow| 1 |Intro|A [[Barbarian]] named [[Terek]] has located the [[Vampire's Cowl]] for [[Sandro]].  Unfortunately, Bandits in the [[Contested Lands]] captured [[Terek]] on his way back from [[Deyja]]. [[Terek]] convinced the bandits that his friends would pay handsomely for his return with his possessions intact.<p>My scrying has shown he is being held in an underground prison near the [[Deyja]]n border.}}
```

Lý do: khớp từng chữ. Nhãn đúng. Hai ghi chú:

1. **Bài cắt mất câu quan trọng nhất cho C-07:** "My scrying has shown he is being held
   in an underground prison near the Deyjan border." Đây là chỗ duy nhất game text nói
   "underground prison near the Deyjan border" — nên trích kèm.
2. **Lệch địa danh trong chính game text:** Day 1 ghi bandits ở **Contested Lands**;
   `| region_text =` ghi **Border Lands** ("on his way across the Border Lands"). Cả hai
   đều in-game. Nếu bài chỉ nêu một, nên nói rõ nguồn nào nói gì.

### C-07
Claim: Terek bị giam tại **(54, 43, 1)** — dưới lòng đất, gần biên giới Deyja.
Nhãn bài gán: `T1* EXPLICIT: sod-retrieving-the-cowl`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw`
Tìm thấy: bảng `==== Heroes ====` —

```
{{hero row|54, 43, 1|{{imprisoned}}|Terek|Battle Mage}}
```

Lý do: toạ độ khớp; `z = 1` = tầng ngầm, khớp "underground prison"; trạng thái
`{{imprisoned}}` khớp "imprisoned". "Gần biên giới Deyja" có game text riêng (Day 1,
prologue). Bảng `== Appearances ==` trên trang Terek cũng độc lập ghi
`{{prison}}: [[Retrieving the Cowl]]`. Nhãn đúng.

### C-08
Claim: Tiền chuộc **40.000 vàng**, qua một Quest Guard tại (54, 44, 1), kèm trích nguyên văn.
Nhãn bài gán: `T1* EXPLICIT: sod-retrieving-the-cowl`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw`
Tìm thấy: `==== Quest Guards ====` —

```
{{SorQrow|guard=1|loc=54, 44, 1|quest=Return with:<br>40000 {{g}} [[Gold]]</br>|prop=A group of bandits man this tower.  They say, "If you want [[Terek]] and his equipment, you have to pay his ransom of 40,000 gold."|prog=No 40,000 gold, no [[Terek]].|comp=[[Terek]] is in the prison north of here.  His ransom is 40,000 Gold.  Do you wish to pay the ransom?}}
```

Lý do: toạ độ, số tiền và trích dẫn khớp từng chữ. Nhãn đúng. Chi tiết đáng dùng mà bài
chưa dùng: Quest Guard ở (54, 44, 1) nằm **ngay dưới** nhà tù (54, 43, 1) — câu `comp`
nói thẳng "Terek is in the prison **north of here**", tự khớp với toạ độ.

### C-09
Claim: Câu khi chưa đủ tiền — "No 40,000 gold, no Terek."
Nhãn bài gán: (không gán nhãn riêng), key `sod-retrieving-the-cowl`
Phán quyết: **CONFIRMED**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw`
Tìm thấy: tham số `prog=` của `{{SorQrow|...}}` ở trên — `prog=No 40,000 gold, no [[Terek]].`
Lý do: nguyên văn khớp. `prog` = text hiện khi chưa hoàn thành quest → in-game text thật,
xứng `T1* EXPLICIT`. **MINOR vì thiếu nhãn:** đây là một trích dẫn in-game trong thân
bài, `CANON-POLICY.md` mục 5.1 buộc có nhãn hai trục + source key.

### C-10
Claim: Điều kiện thắng là mang Cowl về **Leafhall** — town **Rampart trung lập** tại
(9, 11, 0). **Mất Cowl cũng là thua.**
Nhãn bài gán: `T1* EXPLICIT: sod-retrieving-the-cowl`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw` ·
`?title=New_Beginning&action=raw`
Tìm thấy: ba chỗ độc lập —

```
| victory        = Transport Artifact {{gl|Vampire's Cowl}} to {{gl|Leafhall}}.
| description    = Bring the Vampire's Cowl to the town of Leafhall to win the scenario.  However, if Gem or Clancy are defeated in combat or you lose the Cowl, the scenario is lost.
{{Town row|9, 11, 0||Rampart|[[Leafhall]]|nofort=y}}
```

Lý do: cả ba phần khớp. `{{Town row}}` không có tham số màu chủ → **trung lập**; thêm
`nofort=y` (không có fort) — chi tiết bài có thể dùng. Cùng `| description =` xuất hiện
nguyên văn lần hai trên trang campaign `New Beginning` → xác nhận độc lập.

NOTE: "mất Cowl là thua" có nguồn ở `| description =` (text hiện trên màn hình chọn
campaign), **không** ở `| loss =` — trường đó chỉ ghi `Lose Hero {{gl|Gem}} or
{{gl|Clancy}}.`. Nếu bài dẫn "điều kiện thua", nên nói rõ là theo mô tả scenario.

### C-11
Claim: Gem mơ thấy Amanda; trích Day 27 về lời khuyên "be careful, very careful".
Nhãn bài gán: `T1* EXPLICIT: sod-retrieving-the-cowl (Day 27)`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw`
Tìm thấy: `{{TErow| 27 |Dream from Manda|...}}` —

```
I had another dream about [[Amanda]] last night.  I think the dreams are real, and she's communicating with me by magic.<p>She asked me how I was faring.  I told her I had recovered the Amulet for [[Sandro]] and agreed to help his master, [[Ethric]], find a [[Vampire's Cowl]] and a pair of [[Dead Man's Boots]].  Shaking with fury, I also told her about the 'harvesting,' and how I was trying to help the villagers in this area.  She just looked at me with her wise, calm eyes and advised me to be careful, very careful about what I was doing, and it wouldn't be like the last time.
```

Lý do: khớp từng chữ. Nhãn đúng. Chi tiết đắt mà bài bỏ, nằm ngay câu trước đoạn trích:
Gem tin nàng đang giúp **Ethric**, không phải Sandro ("agreed to help his master,
Ethric") — đây là bằng chứng trực tiếp cho vỏ bọc, và nó khớp `After the Amulet` Day 21
(xem C-18). Tiêu đề event là "Dream from **Manda**" (tên gọi thân mật), thân text là
"Amanda" — nếu bài viết tên, dùng Amanda.

### C-12
Claim: Gem vẫn đi tiếp, vì "needed to finish gathering the items Ethric wanted first."
Nhãn bài gán: `T1* EXPLICIT: sod-retrieving-the-cowl (Day 42)`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw`
Tìm thấy: `{{TErow| 42 |Letter to Lord|...}}` —

```
I finally wrote him today that I would be happy to join his forces but needed to finish gathering the items [[Ethric]] wanted first.
```

Lý do: khớp từng chữ, nhãn đúng.

NOTE: trích Day 42 mà không trích **Day 50** làm tuyến Lord Fayette bỏ lửng. Day 50 đóng
nó lại: "It formally invited me to join his forces as a General **as soon as my promise to
Sandro was fulfilled**." Chú ý đảo chủ thể — Day 42 Gem nói "items **Ethric** wanted",
Day 50 nói "promise to **Sandro**". Nếu bài dùng Day 42 để chứng minh Gem tin vỏ bọc
Ethric, Day 50 là mảnh còn lại của cùng lập luận.

### C-13
Claim: slot = Cape; class = **Minor**; giá = 4.000; hiệu ứng = **+10% Necromancy**.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Vampire%27s_Cowl&action=raw` ·
`?title=Necromancy&action=raw`
Tìm thấy: template `ArtifactNewSB` —

```
 | class   = Minor
 | slot    = Cape
 | cost    = 4000
 | effect = +10% {{gl|Necromancy}}
```

Xác nhận độc lập trên trang `Necromancy`, mục "Related factors":
`* {{an|Vampire's Cowl}}: +10% Necromancy`
Lý do: cả bốn thông số khớp, nằm trong tham số template, và có trang thứ hai xác nhận
con số hiệu ứng. Nhãn đúng. Đây là claim duy nhất trong bài mà key
`h3wiki-vampires-cowl` **thực sự** chống lưng được (so với C-19→C-28).

### C-14
Claim: Mô tả in-game — "Worn about the shoulders, this cowl increases your Necromancy
skill by 10%."
Nhãn bài gán: **`T6 EXPLICIT: fandom-artifact-list`**
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Talk:Artifact/descriptions&action=raw` ·
`mightandmagic.fandom.com/api.php?action=parse&page=List of Heroes III artifacts&prop=wikitext`
Tìm thấy: **nguồn `T1` thật có dòng này.** `Talk:Artifact/descriptions` (16.129 byte) tự
ghi ở đầu bảng —

```
|+ style="white-space:nowrap;"|Information from H3Bitmap.lod > artraits.txt
```

— và dòng 115 —

```
| [[Vampire's Cowl]] || Worn about the shoulders, this cowl increases your Necromancy skill by 10%.
```

Fandom (`fandom-artifact-list`) chép **cùng một câu**, không dẫn nguồn.
Lý do: hai lỗi độc lập.

1. **`T6 EXPLICIT` là tổ hợp nhãn không hợp lệ.** `CANON-POLICY.md` mục 2: "Nếu một claim
   chỉ có T6 chống lưng, nó tối đa là `INFERENCE` hoặc `UNVERIFIED`."
2. **Không cần T6.** Dự án đã có `h3wiki-artraits-txt` tier **`T1`** thật (string table
   trích từ `H3Bitmap.lod > artraits.txt`) và bảng đó **có** dòng cho Vampire's Cowl.

Sửa: `{T1 EXPLICIT: h3wiki-artraits-txt}`. Bỏ `fandom-artifact-list` khỏi claim này.
Đây là cách vá **nâng** tier chứ không hạ — sau khi sửa, `EXPLICIT` hợp lệ.

Bằng chứng phụ có ích: bảng cùng cho cả cụm, xác nhận chuỗi 5/10/15% —
`Amulet of the Undertaker` "increases your Necromancy skill by 5%",
`Dead Man's Boots` "increase your Necromancy skill by 15%".

### C-15
Claim: Cowl chiếm **cùng slot Cape** với bộ hoàn chỉnh — nên khi ghép xong, nó **bị thay
thế chứ không cộng dồn**.
Nhãn bài gán: (không gán nhãn riêng), key `h3wiki-cloak-undead-king`
Phán quyết: **DOWNGRADE**
Mức: **MINOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Cloak_of_the_Undead_King&action=raw`
Tìm thấy: template `CombinationArtifactNewSB` —

```
 | slot    = Cape
 | blocked = Necklace<p>Feet
```

và văn xuôi thân trang —

```
the power of the artifact '''can''' be increased by the from the Necromancy Amplifier, Soul Prison, and the Necromancy specialty (but not the Cloak's components' effects)
```

Lý do: **kết luận đúng, lập luận sai đường.** Chỗ duy nhất nói thẳng chuyện không cộng
dồn là mệnh đề "(but not the Cloak's components' effects)" — và mệnh đề đó nằm **ngoài
template**, tức là văn wiki (`T6`), không phải game text.

Lập luận theo slot thì **không đủ và không chính xác**: Cloak chiếm slot **Cape** nhưng
`blocked = Necklace, Feet` — nghĩa là nó khoá luôn slot của **cả hai** thành phần kia.
Nói "cùng slot Cape nên bị thay thế" chỉ giải thích được một trong ba, và bỏ mất cơ chế
thật (ghép là **tiêu thụ** cả ba thành phần). Sửa: ghi kết luận là `INFERENCE` với bước
suy luận nêu rõ `slot` + `blocked`, hoặc dẫn thẳng câu văn wiki và gán `T6`.

### C-16
Claim: Điều khoản "vô tác dụng nếu hero không có Necromancy" là **văn wiki, không phải
game text**.
Nhãn bài gán: (không gán nhãn), không source key
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Vampire%27s_Cowl&action=raw` ·
`?title=Talk:Artifact/descriptions&action=raw` · `?title=Necromancy&action=raw`
Tìm thấy: câu đó nằm **ngoài** template `ArtifactNewSB`, ngay sau khi template đóng —

```
If the equipped hero does not have the [[Necromancy]] secondary skill, the Vampire's Cowl has no effect.
```

Lý do: **claim đúng, và kiểm được cả hai chiều.**
Chiều thuận: câu nằm ngoài mọi tham số template → văn biên tập viên (`T6`).
Chiều nghịch: mô tả in-game thật (`h3wiki-artraits-txt`) chỉ nói "increases your
Necromancy skill by 10%", **không** có điều kiện nào về việc phải có skill. Trang
`Necromancy` cũng không nêu quy tắc này — nó chỉ nói bonus là cộng dồn ("+% means that
effect from items are cumulative and are added instead of being multiplied").

⚠️ Kèm cảnh báo cho người viết: xác nhận "đây là văn wiki" **không** đồng nghĩa xác nhận
"điều đó đúng trong game". Dự án chưa có nguồn nào chứng minh hay phản bác quy tắc này.
Nếu bài nêu nó như cơ chế, phải là `T6` + `INFERENCE`, hoặc đưa xuống *Câu hỏi mở*.

### C-17
Claim: SoD gốc **+10%**; HotA 1.3.0 → 1.7.x = **+5%**; HotA 1.8.0 khôi phục **+10%**.
Nhãn bài gán: `T1* EXPLICIT: hota-changelog`
Phán quyết: **CONFIRMED**
Mức: **NOTE**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Horn_of_the_Abyss_(Changelog)&action=raw`
(201.529 byte)
Tìm thấy: changelog **nêu tên Vampire's Cowl thẳng ra**. Dòng 31, dưới tiêu đề
`== Version 1.8.0 (31/DEC/2025) ==` (dòng 7) —

```
[-] 5/10/15/30% Necromancy boost values are back for the Amulet of the Undertaker, Vampire's Cowl, Dead Man's Boots, and Cloak of the Undead King (instead of 2.5/5/7.5/15%)
```

Dòng 2005, nằm giữa `== Version 1.3.0 (01/JAN/2014) ==` (dòng 1966) và
`== Version 1.2fix ==` (dòng 2139) —

```
[+] The number of Skeletons raised by necromancy is reduced by half, as well as bonuses to it from artifacts and a Necromancy Amplifier
```

Lý do: **claim mạnh nhất trong bài, và đúng theo BH-3.** Đây là ca duy nhất changelog nêu
đích danh Cowl, nên không phải suy từ cụm. Chuỗi `5/10/15/30%` khớp đúng vị trí
Amulet/Cowl/Boots/Cloak → Cowl là con `10`, và bản halved là con `5` trong
`2.5/5/7.5/15%`. Ba mốc phiên bản trong claim đều truy được về tiêu đề phiên bản có ngày.
`grep -i cowl` toàn bộ 201.529 byte chỉ ra **đúng một** dòng — không có thay đổi nào khác
về Cowl bị bỏ sót.

NOTE (không phải lỗi của bài, là vấn đề registry): `hota-changelog` đang mang tier `T1*`
= "in-game text qua trung gian". Changelog là **ghi chú phát hành của developer**, không
phải chuỗi text nào hiện ra trong game — xét theo `CANON-POLICY.md` mục 2 thì nó gần `T2`
(tài liệu chính thức) hoặc `T4` (phát ngôn developer) hơn. Ngoài ra HotA là mod
**fan-made, không phải NWC**, nên mọi con số HotA là thay đổi của mod, không phải thay
đổi canon Old Universe. Nên xử ở cấp registry cho toàn bộ bài artifact, không sửa lẻ ở
bài này.

### C-18
Claim: Cowl là thành phần xuất hiện **nhiều nhất** trong ba thành phần.
Nhãn bài gán: (không gán nhãn), không source key
Phán quyết: **DOWNGRADE**
Mức: **MINOR**
Đã tìm ở: `api.php?action=query&list=backlinks` cho cả **ba** artifact (`Vampire's
Cowl` 194 · `Dead Man's Boots` 192 · `Amulet of the Undertaker` 193 backlink), giao với
`Category:Campaign scenarios` + `Category:Single and Multiplayer Scenarios` +
`Category:Generated Maps` + `Category:Horn of the Abyss`, trừ nhiễu artifact.
Tìm thấy: đếm được như sau.

| | Map/scenario | Trang hero mang sẵn artifact | Tổng trang nội dung game |
|---|---|---|---|
| Vampire's Cowl | **9** | 1 (`Mormolykos`) | **10** |
| Dead Man's Boots | 8 | 0 | 8 |
| Amulet of the Undertaker | 5 | **5** | **10** |

9 map của Cowl: `Retrieving the Cowl` (SoD), `Season of Harvest` (RoE), `All for One`
(RoE), `Undead Unrest` (AB), `Taming of the Wild` (AB), `Here There Be Pirates` (AB),
`Beyond the Horizon` (HotA), `Tomb Raiders` (HotA), `All Hands on Board!` (HotA).
5 hero mang Amulet, kiểm từng trang bằng `spart_`: `Aiedia`, `Erybarus`, `Ioke`, `Nahia`,
`Thammus` (đều `{{Ang|Amulet of the Undertaker}}`).

Lý do: **claim đúng theo một cách đếm, và hoà theo cách đếm khác.** Tính theo số
map/scenario thì Cowl thắng rõ (9 > 8 > 5). Tính theo tổng trang nội dung game thì Cowl
**hoà** với Amulet (10–10). Không nguồn nào phát biểu câu này — nó là phép đếm của người
viết. Sửa: gán `INFERENCE` và **ghi rõ đơn vị đếm** ("xuất hiện trên nhiều
scenario nhất"), đừng để superlative trần không nhãn.

Kèm hai chỗ bài bỏ sót (xem thêm C-29): `After the Amulet` (Cowl được nêu tên ở Day 21 và
Day 23, dù không phải object) và `Mormolykos` (hero **mang** Cowl).

### C-19
Claim: `Retrieving the Cowl` — Cowl **đi kèm Terek khi chuộc**.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Vampire%27s_Cowl&action=raw` ·
`?title=Retrieving_the_Cowl&action=raw` · `?title=Terek&action=raw`
Tìm thấy: hai lỗi.

1. **Mis-citation.** Trang `Vampire's Cowl` dài **913 byte**. Tên scenario duy nhất trên
   đó nằm trong chú thích gallery (`[[Retrieving the Cowl]]{{-ws}} prologue`). Trang
   **không** nói gì về Terek hay chuộc tiền. (Cùng kiểu lỗi ở C-20→C-28.)
2. **`EXPLICIT` không có cơ sở.** Game text không mô tả Cowl đổi tay. Bằng chứng: bảng
   `==== Heroes ====` liệt kê Terek **không kèm artifact nào** —
   `{{hero row|54, 43, 1|{{imprisoned}}|Terek|Battle Mage}}` — trong khi wiki này **có**
   ghi artifact của hero khi biết, ví dụ trang `Mormolykos` ghi thẳng
   `spart_6 = {{Ang|Vampire's Cowl}}`. Trang `Terek` cũng không có tham số `spart_` nào.

Chống lưng gần nhất là suy luận từ hai mảnh: `prop` của Quest Guard nói "If you want
Terek **and his equipment**, you have to pay his ransom", và điều kiện thắng đòi mang
Cowl tới Leafhall — nên Cowl phải đến từ Terek. Đó là `INFERENCE`, không phải `EXPLICIT`.
Sửa: `{T1* INFERENCE: sod-retrieving-the-cowl — Quest Guard hứa trả "Terek and his
equipment"; Cowl không có mặt trong bảng Artifacts của map; điều kiện thắng đòi Cowl}`.

### C-20
Claim: `Season of Harvest` (RoE) — Cowl là **bonus khởi đầu**.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Season_of_Harvest&action=raw` ·
`?title=Long_Live_the_King&action=raw`
Tìm thấy: nội dung **đúng**, source key **sai**.

```
| source         = roe
| cback          = roe lltk 2
| bonus          = {{BonusArt|Vampire's Cowl}}{{BonusB|Necropolis|Necromancy Amplifier}}{{BonusB|Necropolis|Unearthed Graves}}
```

Cùng dòng `bonus` xuất hiện lần hai trên trang campaign `Long Live the King` → xác nhận
độc lập. `source = roe` xác nhận đúng sản phẩm **Restoration of Erathia**.
Lý do: `h3wiki-vampires-cowl` (913 byte) không chứa tên scenario này. Sửa key →
`roe-season-of-harvest` (registry đã có). Thêm sắc thái: Cowl là **một trong ba** lựa
chọn bonus (cùng Necromancy Amplifier và Unearthed Graves), không phải bonus mặc định —
"bonus khởi đầu" trần dễ đọc thành "luôn có".

### C-21
Claim: `Undead Unrest` (AB) — Cowl **là điều kiện thắng**; "undead... are rallying around
the 'Vampire's Cowl'".
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Undead_Unrest&action=raw` (623 byte)
Tìm thấy: nội dung **đúng nguyên văn**, source key **sai**.

```
| description    = Many undead from Castle Nightmare have broken loose and are rallying around the "Vampire's Cowl". Find the Cowl to end the unrest among the undead.
| source         = ab
| victory        = Acquire Artifact {{gl|Vampire's Cowl}}.
| victory_c      = get_art
```

Lý do: `source = ab` xác nhận **Armageddon's Blade**; `victory` xác nhận điều kiện thắng;
trích dẫn khớp. Chỉ sai key. Cần key mới `ab-undead-unrest`.
⚠️ Ghi kèm vào registry: trang này là **stub 623 byte** — không có mục Objects, không có
Timed events, không có toạ độ. Xem C-29 về hệ quả.

### C-22
Claim: `Taming of the Wild` — nhặt tự do, text "It looks like a careless vampire left this
lying about."
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Taming_of_the_Wild&action=raw`
Tìm thấy: nội dung **đúng nguyên văn**, source key **sai**. Bảng `==== Artifacts ====`,
`source = ab` —

```
| 69, 4, 0 | {{An|Vampire's Cowl}} | It looks like a careless [[vampire]] left this lying about.
```

Ba thành phần Cloak nằm kề nhau, **không** cột Guardians nào → nhặt tự do:
Boots (67, 3, 0) "A note on the boots reads:  \"Dead men tell no tales\"", Amulet
(68, 4, 0), Cowl (69, 4, 0).
Lý do: chỉ sai key. Sửa → `ab-taming-of-the-wild` (registry đã có, đã ghi đúng toạ độ).
Đây cũng là **phản bác** cho cách đọc rộng của C-01 ("không nằm trên bản đồ").

### C-23
Claim: `Here There Be Pirates` (AB) — trên map, **26 Dragon Flies** canh.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Here_There_Be_Pirates&action=raw`
Tìm thấy: nội dung **đúng chính xác**, source key **sai**. `source = ab`,
`cback = ab fw 3` —

```
| 31, 37, 0 | {{An|Vampire's Cowl}} | <center>'''Guardians:''' 26 {{Cn|Dragon Fly|name=Dragon Flies}}</center>
```

Lý do: con số 26 và loại lính canh khớp; sản phẩm AB xác nhận qua `source`. Chỉ sai key.
Cần key mới `ab-here-there-be-pirates`. Bài nên bổ sung toạ độ (31, 37, 0) — đang thiếu.

### C-24
Claim: `Beyond the Horizon` — một trong **bốn** artifact Seer's Hut đòi.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Beyond_the_Horizon&action=raw`
Tìm thấy: nội dung **đúng**, source key **sai**. `source = hota`, `cback = hota fif 2`,
Seer's Hut (2, 27, 0) —

```
{{SorQrow|seer=1|loc=2, 27, 0|quest=Return with:<br>{{An|Skull Helmet}}<br>{{An|Rib Cage}}<br>{{An|Amulet of the Undertaker}}<br>{{An|Vampire's Cowl}}</br>|rew={{An|Golden Bow}}|...}}
```

Lý do: đếm được đúng **bốn** artifact (Skull Helmet, Rib Cage, Amulet of the Undertaker,
Vampire's Cowl) → `Golden Bow`. Chỉ sai key; sửa → `hota-beyond-the-horizon` (registry đã
có). **Phải ghi rõ đây là HotA (fan-made, không phải NWC).**

### C-25
Claim: `Tomb Raiders` (HotA) — Seer's Hut → **20 Engineers**.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Tomb_Raiders&action=raw` (117.073 byte)
Tìm thấy: nội dung **đúng**, source key **sai**. `source = hota`, `cback = hota fif 4`,
Seer's Hut `seer=2` tại **(153, 136, 0)** → `rew=20 {{Cnlite|Engineer|name=Engineers}}`.
Sửa key → `hota-tomb-raiders` (registry đã có). Bài nên bổ sung toạ độ.

⭐ **PHÁT HIỆN MỚI, chưa có trong bảng claim — HotA đặt tên chủ sở hữu cho Cowl.** Text
đầy đủ của Seer's Hut này —

```
|prop=...they cannot leave the camp unguarded because the vampire [[Mormolykos]] has recently been seen by the village, with several miners falling victim to him.<p>If you could track the vampire down and destroy him, the engineers would join you on your quest.|comp=When the engineers see [[Mormolykos]]’ Cowl, they immediately express their willingness to go with you.
```

Và trang `Mormolykos` (`{{inhota}}`, `CampaignHero`) —

```
 | race       = {{gl|Vampire}}
 | class      = Necromancer
 | spart_6      = {{Ang|Vampire's Cowl}}
== Story ==
A vampire from [[Jadame]] who preys on miners.
```

Nghĩa là trong HotA, chiếc Cowl **được mang bởi một vampire có tên**, và quest là đi giết
hắn lấy Cowl — HotA hiện thực hoá đúng cái text nhặt artifact của SoD ("You manage to
find a Vampire's resting place... you take his cowl", C-02). Đây là mảnh lore đáng giá
nhất mà bài đang bỏ, và nó **phản bác** cách đọc "lore của Cowl chỉ gắn với Sandro" (xem
C-29). Cần key mới `h3wiki-mormolykos`.

### C-26
Claim: `All for One` — Seer's Hut → **+5 Attack**.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=All_for_One&action=raw`
Tìm thấy: nội dung **đúng**, source key **sai**.

```
| source         = roe
{{SorQrow|seer=3|loc=1, 16, 0|quest=Return with:<br>{{An|Vampire's Cowl}} |rew=+5 {{Ps|Attack}}}}
```

Lý do: thưởng +5 Attack khớp; Seer's Hut ở (1, 16, 0). Chỉ sai key; cần key mới
`roe-all-for-one`. **Bài phải ghi sản phẩm: `source = roe` — Restoration of Erathia**, và
đây là map Single/Multiplayer độc lập (`Category:Single and Multiplayer Scenarios`),
không thuộc campaign nào. Bảng claim không ghi sản phẩm cho C-26; gán sai sản phẩm từng
là BLOCKER ở đợt trước nên phải nói rõ. Lưu ý Seer's Hut này **không có** text
`prop`/`comp` — không trích được câu thoại nào.

### C-27
Claim: `All Hands on Board!` — Seer's Hut → **50 Vampire Lords**.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=All_Hands_on_Board%21&action=raw`
Tìm thấy: nội dung **đúng**, source key **sai**. `source = hota`, `cback = hota hota 4` —

```
{{SorQrow|seer=3|loc=47, 26, 1|quest=Return with:<br>{{An|Vampire's Cowl}}</br>|rew=50 {{Cn|Vampire Lord}}s|prop=Long ago, powerful wizards were able to create magical artifacts, but time has caused us to forget how to make new items.  I would like to learn these techniques myself, but I need one of these artifacts first to see how it was done.  If you could bring me, the Vampire's Cowl, you would be well rewarded.|comp=Ah, exactly what I needed!  Here is the reward I promised.  You still wish to trade the Vampire's Cowl, yes?}}
```

Lý do: 50 Vampire Lords khớp; Seer's Hut (47, 26, 1). Chỉ sai key; cần key mới
`hota-all-hands-on-board`. **Bài phải ghi rõ đây là HotA (fan-made, không phải NWC)** —
bảng claim gắn nhãn HotA cho C-25 và C-28 nhưng **không** cho C-27, dễ làm người đọc xếp
map này vào SoD/AB.

### C-28
Claim: `Apocalypse` (HotA template) — một trong ba artifact **duy nhất** được cho phép.
Nhãn bài gán: `T1* EXPLICIT: h3wiki-vampires-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Apocalypse&action=raw` (1.335 byte) ·
`?title=Horn_of_the_Abyss_(Changelog)&action=raw` ·
`api.php?action=query&prop=revisions&titles=Apocalypse`
Tìm thấy: **xác nhận độc lập phát hiện #3 của bảng claim.** Trang ghi —

```
*Allowed artifacts:
**{{An|Amulet of the Undertaker}}
**{{An|Vampire's Cowl}}
**{{An|Dead Man's Boots}}
```

**Không có chữ "only" / "duy nhất" ở đâu.**
Ba lỗi phải sửa:

1. **"duy nhất" là cách đọc thêm vào, không có trong nguồn.** Bằng chứng ngược nằm trong
   changelog dòng 549, dưới `== Version 1.7.1 (06/APR/2024) ==` —
   `[-] Apocalypse template: Wanderer's Boots and Shrines of Magical Mystery banned`.
   Nếu template chỉ cho phép ba artifact thì cấm riêng một artifact thứ tư là vô nghĩa.
   `grep Apocalypse` toàn bộ 201.529 byte changelog chỉ ra **hai** dòng (1.5.0 "Added the
   Boomerang and Apocalypse templates" — dòng 1154; và dòng 549 trên) — **không lần nào**
   là danh sách artifact.
2. **Loại nguồn sai.** Trang đặc tả template do cộng đồng viết (`{{Template map}}`,
   `[[Category:Generated Maps]]`) — **không phải in-game text**. Tier đúng: `T6`, và `T6`
   tối đa `INFERENCE`/`UNVERIFIED`. Gán `T1*` sai **loại**. Ngoài ra key
   `h3wiki-vampires-cowl` cũng sai — phải là `hota-apocalypse-template`.
3. **Thiếu phạm vi phiên bản.** `prop=revisions` cho ngày sửa cuối
   **2025-05-14T20:37:29Z** ≈ HotA 1.7.2–1.7.3, **trước 1.8.0 (31/DEC/2025)**. Trang tự
   nó không ghi phiên bản nào.

⚠️ **Kiểm cái bẫy ngược chiều — với Cowl thì bẫy KHÔNG nổ.** Đã kiểm ba đường độc lập:
`Black'n'Blue` (`*Banned artifacts:` = Skull Helmet, Tunic of the Cyclops King, **Dead
Man's Boots**, Angel Wings, Spellbinder's Hat, Statesman's Medal); `Nine-day Wonder`
(`*Banned artifacts:` = Angel Wings, Wayfarer's Boots, **Amulet of the Undertaker**,
Garniture of Interference, Surcoat of Counterpoise, Boots of Polarity); và toàn bộ 194
backlink của `Vampire's Cowl` — trang template **duy nhất** trỏ tới Cowl là `Apocalypse`.
`grep -i cowl` trên `List of map templates` cũng trắng.

**Kết luận:** Vampire's Cowl là thành phần **duy nhất trong ba** không bị cấm ở bất kỳ
template nào. Đây là điều đáng nói ra như một dữ kiện tích cực (`INFERENCE`, nêu rõ
phương pháp đếm là quét backlinks) — nhưng **đừng** viết thành "được cho phép ở mọi
template", vì backlinks chỉ bắt được mention **có link**.

### C-29
Claim: `Undead Unrest` là scenario **duy nhất** mà Cowl là **mục tiêu chính**, và lore của
nó **độc lập với Sandro** — undead tụ tập quanh chiếc mũ trùm như quanh **một vật thiêng**.
Nhãn bài gán: (không gán nhãn), không source key
Phán quyết: **CONTRADICTED**
Mức: **BLOCKER**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Undead_Unrest&action=raw` ·
`?title=Retrieving_the_Cowl&action=raw` · `?title=Tomb_Raiders&action=raw` ·
`?title=Mormolykos&action=raw` · `api.php?action=query&prop=revisions&titles=Undead Unrest`
Tìm thấy: **nguồn ngược nằm ngay trong scenario chính của bài.** `Retrieving the Cowl` —

```
| victory        = Transport Artifact {{gl|Vampire's Cowl}} to {{gl|Leafhall}}.
| description    = Bring the Vampire's Cowl to the town of Leafhall to win the scenario.  However, if Gem or Clancy are defeated in combat or you lose the Cowl, the scenario is lost.
```

so với `Undead Unrest` —

```
| victory        = Acquire Artifact {{gl|Vampire's Cowl}}.
```

Lý do: **"duy nhất" bị phản bác.** Ở **cả hai** scenario, Cowl là điều kiện thắng, tức là
mục tiêu chính. Khác biệt duy nhất là **loại** điều kiện: `Acquire Artifact` (get_art) so
với `Transport Artifact`. Bài không thể gọi `Undead Unrest` là scenario duy nhất mà Cowl
là mục tiêu chính khi bài **cũng** dẫn `Retrieving the Cowl` với điều kiện thắng là mang
Cowl về Leafhall (C-10). Đây là mâu thuẫn **nội bộ giữa C-10 và C-29** — `check.py` dạng
"mâu thuẫn giữa hai bài" bắt đúng loại này.

Diễn đạt sửa được: "scenario duy nhất mà việc **chiếm được** Cowl tự nó là điều kiện
thắng" (`Acquire Artifact`), so với `Retrieving the Cowl` đòi **vận chuyển** nó tới đích.

Hai lỗi kèm theo, cùng mức MAJOR nếu tách riêng:

- **"lore độc lập với Sandro" dựa trên một stub.** `Undead Unrest` chỉ **623 byte**
  (`prop=revisions`: size 623, sửa cuối 2025-05-14). Trang **không có** mục Objects,
  không có Timed events, không có toạ độ — nghĩa là gần như **không có** nội dung text
  của map nào được chép. Sandro vắng mặt trên một trang chưa được chép đầy đủ **không
  phải bằng chứng** Sandro vắng mặt trong map. Đây đúng loại claim phủ định "trông giống
  sự cẩn trọng" mà BH của dự án cảnh báo. Tối đa `INFERENCE`, và phải nói rõ là suy từ
  một trang stub.
- **"như quanh một vật thiêng" là chữ của người viết, không có trong nguồn.** Game text
  chỉ nói "rallying around". Bỏ hoặc tách khỏi câu có nhãn.

Bổ sung quan trọng cho ý "lore độc lập với Sandro": ý đó **đúng nhưng bài chọn sai ví
dụ**. Tuyến lore Cowl không-Sandro **có** bằng chứng thật, và nằm ở HotA: vampire
`Mormolykos` từ `Jadame` mang chính chiếc Cowl (`spart_6`), và Seer's Hut ở `Tomb Raiders`
gọi nó là "**Mormolykos' Cowl**". Xem C-25.

### C-30
Claim: Bảng Artifacts của `Retrieving the Cowl` **không có** Cowl như một object trên map.
Nó đi kèm Terek, nhưng **không có text nào** mô tả việc nó đổi tay.
Nhãn bài gán: **`T1* UNVERIFIED`**, key `sod-retrieving-the-cowl`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Retrieving_the_Cowl&action=raw` ·
`?title=Terek&action=raw`
Tìm thấy: đã đọc **toàn bộ** bảng `==== Artifacts ====` — **12** dòng, tất cả là artifact
ngẫu nhiên, **không dòng nào** là Vampire's Cowl:

(3,17,1) Random Minor · (9,29,1) Random Treasure · (18,16,1) Random Minor ·
(22,7,1) Random Major · (22,61,1) Random Major · (23,54,1) Random Treasure ·
(25,17,1) Random Treasure · (29,63,1) Random Minor · (49,52,1) Random Relic ·
(65,23,1) Random Treasure · (65,31,1) Random Minor · (66,28,1) Random Major.

Lý do: **claim đúng, nhưng nhãn vừa không hợp lệ vừa sai cấp — theo chiều bất ngờ.**

1. **Nửa đầu là `EXPLICIT`, không phải `UNVERIFIED`.** "Bảng Artifacts không có Cowh" là
   dữ kiện **đọc trực tiếp được** từ nguồn — bảng nằm đó, 12 dòng, đếm được. Gán
   `UNVERIFIED` cho một điều đã kiểm xong là hạ cấp sai.
2. **`UNVERIFIED` không được phép trong thân bài.** `CANON-POLICY.md` mục 5.3: "Không
   claim nào ở trạng thái `UNVERIFIED` trong thân bài (chuyển xuống mục *Câu hỏi mở* nếu
   chưa giải quyết được)." Điều này một mình đã chặn `status: verified`.
3. **Nửa sau là `INFERENCE`, và có một điểm cận-phản-bác phải nêu.** Game text gần nhất
   với "đổi tay" là `prop` của Quest Guard: "If you want Terek **and his equipment**, you
   have to pay his ransom" — không nêu tên Cowl, nhưng hàm ý trang bị của Terek về theo
   hắn. Nói "không có text nào" mà không nhắc câu này là để hở. Củng cố thêm cho nửa sau:
   bảng Heroes ghi Terek **không kèm artifact**, và trang `Terek` không có `spart_` nào —
   trong khi wiki này **có** ghi `spart_6 = {{Ang|Vampire's Cowl}}` cho `Mormolykos`, nên
   sự vắng mặt ở đây là vắng mặt **có ý nghĩa**.

Sửa: tách thành hai câu — `{T1* EXPLICIT: sod-retrieving-the-cowl}` cho dữ kiện bảng
Artifacts, và `{T1* INFERENCE: sod-retrieving-the-cowl — chỉ có "Terek and his equipment"
ở Quest Guard; không dòng nào nêu tên Cowl; Terek không được ghi mang artifact}` cho
nhận định phủ định. Không dùng `UNVERIFIED` ở cả hai.

---

## Kiểm BH-1 — timed event bị bỏ

Đã đọc **toàn bộ** `=== Timed events ===` của `Retrieving the Cowl`: **12** event ở các
Day **1, 1(cont), 3, 11, 11(cont), 19, 27, 30, 38, 42, 50**, cộng 10 town timed event.
Bài trích Day 1, 27, 42 → **bỏ 8 event**. Ba cái đáng kể:

- **Day 11 "Another Harvested Village" (hai phần)** — đáng kể nhất, và đáng kể **đúng cho
  một bài về artifact Necromancy**: "another small hamlet that had been \"harvested\" by a
  [[Necromancer]] about a month ago.  I buried what was left of the children's bodies.
  There weren't any adults; they had all been raised as skeletons, I'm sure." Đây là chỗ
  game text cho thấy **hậu quả** của chính cơ chế mà Cowl khuếch đại, trong cùng scenario
  Gem đi lấy Cowl. Day 27 mà bài đã trích cũng trỏ ngược về đây ("I also told her about
  the 'harvesting,'") — trích Day 27 mà không có Day 11 làm mất đối tượng của câu đó.
- **Day 30 "Sorting it out"** — "I don't think it's wrong to hate the Hateful... What I
  think is wrong is to let that hating and unforgiving turn a person into the thing they
  hate... I won't be like them." Cùng tuyến đạo đức với lời cảnh báo của Amanda ở Day 27.
- **Day 50 "Letter from Lord"** — đóng tuyến Day 42 mà bài đang để lửng (xem C-12).

Mức: **MINOR** (thiếu sót nội dung, không phải claim sai). Day 3, 19, 38 là thứ yếu, nhưng
Day 19 có chi tiết "a Vampire Scout spotted us" — thuận đề tài nếu bài cần.

## Kiểm BH-2 — trang disambiguation / redirect

Làm **trước** khi chấp nhận bất kỳ claim phủ định nào về phạm vi xuất hiện:

| Kiểm | Kết quả |
|---|---|
| `Vampire's cowl` (chữ c thường) | `#REDIRECT [[Vampire's Cowl]]` — cùng một trang |
| `Vampire's Cowl (disambiguation)` | HTTP **404** — không tồn tại |
| `Vampire` | `#REDIRECT [[Vampire and Vampire Lord]]` — creature, không phải artifact |
| `List of Heroes IV artifacts` (Fandom) | `grep -i vampire` → **trắng**. Không có Vampire's Cowl trong H4 |
| `List of Might and Magic VIII items` (Fandom) | chỉ khớp cụm "chain cowl" trong mô tả một áo giáp ring mail — **không** phải artifact cùng tên |
| Fandom search "Vampire's Cowl" | 9 trang, toàn bộ là H3/SoD/HotA — không có mục nào ở dòng MM RPG |

**Kết luận:** Vampire's Cowl chỉ tồn tại trong Heroes III (RoE / AB / SoD) và HotA. Không
có trùng tên ở H4 hay MM RPG, không có trang disambiguation. Claim phủ định dạng "chỉ có
ở Heroes III" **an toàn** — khác với ca `Sandro (Xeen)`.

## Kiểm BH-3 — HotA phải dùng changelog

Đã đối chiếu changelog (`Horn of the Abyss (Changelog)`, 201.529 byte) cho cả ba claim
HotA được yêu cầu:

- **C-17** — changelog **nêu đích danh Vampire's Cowl**, dòng 31 (1.8.0) và dòng 2005
  (1.3.0). Claim đứng vững. Đây là ca changelog **chống lưng** bài.
- **C-25** — `Tomb Raiders` là scenario (`source = hota`), không phải cơ chế; changelog
  không phải nguồn thích hợp. Đã xác minh trực tiếp bằng `{{SorQrow|...}}`.
- **C-28** — changelog **phản bác** cách đọc "duy nhất" (dòng 549, 1.7.1). Đây là ca
  changelog **bác** trang artifact/template. Xem C-28.

Ngoài ra `grep -i cowl` toàn changelog chỉ ra **một** dòng duy nhất → không có thay đổi
HotA nào khác về Cowl bị bỏ sót.

---

## Source key cần thêm / sửa trong REGISTRY

**Cần thêm (5):**

| key đề nghị | tier | Nội dung |
|---|---|---|
| `ab-undead-unrest` | T1* | Armageddon's Blade, map Single/Multiplayer (`source = ab`). `victory = Acquire Artifact Vampire's Cowl`; mô tả "rallying around the \"Vampire's Cowl\"". ⚠️ **Stub 623 byte** — không có Objects, không có Timed events. Không dùng làm cơ sở cho claim phủ định |
| `ab-here-there-be-pirates` | T1* | Armageddon's Blade (`source = ab`, `cback = ab fw 3`) — Cowl trên map tại (31, 37, 0), lính canh **26 Dragon Flies** |
| `roe-all-for-one` | T1* | **Restoration of Erathia** (`source = roe`), map Single/Multiplayer độc lập — Seer's Hut (1, 16, 0) đổi Cowl → **+5 Attack**. Không có text `prop`/`comp` |
| `hota-all-hands-on-board` | T1* | Scenario **HotA** (fan-made, `source = hota`, `cback = hota hota 4`) — Seer's Hut (47, 26, 1) đổi Cowl → **50 Vampire Lords**. Có thoại đầy đủ về nghề làm artifact đã mai một |
| `h3wiki-mormolykos` | T1* | ⭐ Hero **HotA** (`{{inhota}}`, `CampaignHero`): vampire từ **Jadame**, class Necromancer, mang `spart_6 = Vampire's Cowl`, địch trong `Tomb Raiders`. **Nguồn duy nhất đặt tên chủ sở hữu in-fiction cho Cowl** — HotA gọi nó "Mormolykos' Cowl" |

**Cần sửa/bổ sung ghi chú (4):**

| key | Sửa gì |
|---|---|
| `hota-changelog` | **Tiêu đề trang đúng là `Horn of the Abyss (Changelog)`.** URL kiểu `Horn_of_the_Abyss/Changelog` trả **404**. Kèm ghi chú: đây là **ghi chú phát hành của developer**, không phải in-game text — tier `T1*` hiện tại đáng xem lại ở cấp registry (gần `T2`/`T4` hơn) |
| `h3wiki-vampires-cowl` | Thêm cảnh báo: trang chỉ **913 byte**, chứa `class/slot/cost/event/effect` và **không một tên scenario nào** (ngoài caption gallery). **Không được dùng cho bảng xuất hiện.** Cùng kiểu với Boots/Amulet ở hai đợt trước |
| `sod-after-the-amulet` | Thêm nội dung đã xác minh: Day 21 chứa **vỏ bọc đầy đủ** — "he has found a way to construct a **necromancy suppressing artifact**, but to do this he needs three lesser artifacts: an Amulet of the Undertaker, a Vampire's Cowl and a pair of Dead Man's Boots" — và Day 23 nhắc lại. Đây là nguồn `T1*` cho **thứ tự ba thành phần** (C-01) |
| `sod-retrieving-the-cowl` | Thêm: **12** timed event (Day 1–50), không chỉ 3; Leafhall (9, 11, 0) Rampart trung lập `nofort=y`; bảng Artifacts **12 dòng toàn artifact ngẫu nhiên, không có Cowl**; Terek (54, 43, 1) `{{imprisoned}}` **không kèm artifact**; lệch địa danh Contested Lands (Day 1) vs Border Lands (`region_text`) |

**Đáng thêm nếu bài dùng (2):** `h3wiki-new-beginning` (T1*) — campaign 4 map, xác nhận
Cowl ở map **thứ ba**, `cback = sod nb 2/3/4`; `roe-long-live-the-king` (T1*) — xác nhận
độc lập `Season of Harvest` là map 2 của RoE với Cowl trong danh sách bonus.

**Lead chưa khai thác:** tồn tại trang `Horn of the Abyss/Team Interview (2024)` trên
thelazy.net. Có thể là nguồn **T4** cho ý định thiết kế phía HotA (ví dụ vì sao đưa
Mormolykos vào). Chưa fetch trong đợt này — ghi vào `BACKLOG.md`, và nhớ BH của dự án về
việc kết luận "không có developer commentary".

---

## Kết luận

**Bài `vampires-cowl` CHƯA đủ điều kiện `status: verified`.** Còn **1 BLOCKER** và
**11 MAJOR**.

Điểm mạnh cần ghi nhận: phần **text in-game** của bài rất chắc. 12 claim CONFIRMED gồm
toàn bộ trích dẫn nguyên văn (C-02, C-06, C-08, C-09, C-11, C-12) — tất cả khớp **từng
chữ** với wikitext thô, kể cả dấu câu. Thông số gốc (C-13) và tuyến phiên bản HotA (C-17)
cũng đứng vững, và C-17 là ca hiếm mà changelog nêu đích danh artifact. Không có claim nào
`NOT_FOUND` — nghĩa là bài không bịa nguồn.

Toàn bộ vấn đề tập trung ở **hai chỗ**, và cả hai đều là lỗi hệ thống, không phải lỗi lẻ:

**Bắt buộc sửa — BLOCKER (1):**

1. **C-29** — "`Undead Unrest` là scenario duy nhất mà Cowl là mục tiêu chính" bị **chính
   bài phản bác**: `Retrieving the Cowl` có `victory = Transport Artifact Vampire's Cowl
   to Leafhall` (mà bài đã dẫn ở C-10). Phải đổi thành "duy nhất mà **chiếm được** Cowl
   tự nó là điều kiện thắng (`Acquire Artifact`)". Kèm hai lỗi cùng claim: "lore độc lập
   với Sandro" suy từ một **stub 623 byte** → tối đa `INFERENCE`; "như quanh một vật
   thiêng" là chữ thêm vào, nguồn chỉ nói "rallying around".

**Bắt buộc sửa — MAJOR (11):**

2. **C-19 → C-28 (10 claim) — mis-citation hàng loạt.** Bài dẫn `h3wiki-vampires-cowl`
   cho **toàn bộ** bảng xuất hiện, nhưng trang đó dài **913 byte** và không chứa một tên
   scenario nào. Tin tốt: **nội dung của cả 10 claim đều đúng** — tôi đã xác minh từng
   cái trên trang scenario tương ứng. Nên đây là việc thay key, không phải viết lại.
   Kèm ba việc trong đó: C-19 phải hạ `EXPLICIT` → `INFERENCE` (game text không mô tả
   Cowl đổi tay); C-28 phải bỏ chữ "duy nhất", đổi tier `T1*` → `T6` và ghi phạm vi
   phiên bản (sửa cuối 2025-05-14, trước 1.8.0); C-26/C-27 phải ghi đúng sản phẩm
   (`All for One` = **RoE**; `All Hands on Board!` = **HotA fan-made**).
3. **C-05 — sai loại nguồn.** Câu "In Retrieving the Cowl, Terek was the first hero
   Sandro hired..." nằm ở mục `== Story ==`, **ngoài mọi template** → văn wiki (`T6`),
   không phải in-game text. Nghi vấn của bảng claim đúng. Không cần dùng câu này: cùng
   nội dung có nguồn `T1*` mạnh hơn ở prologue, `region_text` và Day 1.
4. **C-14 — nhãn không hợp lệ.** `T6 EXPLICIT` vi phạm `CANON-POLICY.md` mục 2. Sửa bằng
   cách **nâng** tier: `h3wiki-artraits-txt` (`T1` thật) **có** dòng cho Vampire's Cowl —
   "Worn about the shoulders, this cowl increases your Necromancy skill by 10%." Bỏ
   `fandom-artifact-list`.
5. **C-30 — `UNVERIFIED` trong thân bài**, vi phạm `CANON-POLICY.md` mục 5.3. Tách thành
   `EXPLICIT` (bảng Artifacts 12 dòng, không có Cowl — đọc trực tiếp được) và `INFERENCE`
   (nhận định phủ định về việc đổi tay, phải nhắc "Terek and his equipment").

**Nên sửa — MINOR (5):** C-01 (giới hạn phạm vi "không nằm trên bản đồ" vào
`Retrieving the Cowl`; ở `Taming of the Wild` và `Here There Be Pirates` nó **là** object
trên map; bỏ "thú vị nhất"; đừng lẫn thành phần thứ hai với scenario thứ hai — Cowl ở map
thứ **ba**) · C-03 (Terek **thành công** lấy Cowl, chỉ thất bại ở việc giao) · C-04
(`h3wiki-terek` không chứa chữ "barbarian"; và game text gọi hắn Barbarian trong khi class
thật là Battle Mage) · C-09 (thiếu nhãn hai trục) · C-15 (lập luận slot chưa đúng: Cloak
`blocked = Necklace, Feet`, khoá cả slot hai thành phần kia) · C-18 (superlative không
nhãn; đúng theo số map 9–8–5 nhưng **hoà** với Amulet 10–10 nếu tính cả trang hero) ·
thiếu **8 timed event**, đáng kể nhất là Day 11 "Another Harvested Village" (BH-1).

**Hai thứ bài nên thêm vì đợt kiểm tìm được:**

- ⭐ **Tuyến Mormolykos (HotA)** — chiếc Cowl có **chủ sở hữu in-fiction có tên**: vampire
  `Mormolykos` từ Jadame, và `Tomb Raiders` gọi nó "Mormolykos' Cowl". HotA hiện thực hoá
  đúng text nhặt artifact của SoD (C-02). Đây là mảnh lore đáng giá nhất bài đang bỏ, và
  nó là ví dụ **thật** cho ý "lore Cowl không chỉ gắn với Sandro" mà C-29 đang chống lưng
  bằng ví dụ sai.
- **Cowl là thành phần duy nhất trong ba không bị cấm ở template nào.** Đã kiểm ba đường
  (`Black'n'Blue` cấm Boots, `Nine-day Wonder` cấm Amulet, và toàn bộ 194 backlink của
  Cowl chỉ ra một trang template duy nhất là `Apocalypse` — ở danh sách **cho phép**).
  Ghi `INFERENCE` kèm phương pháp đếm.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. BLOCKER và toàn bộ MAJOR đều xử lý bằng **sửa bài** hoặc **đưa
nguồn mới**.

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| C-29 | "scenario duy nhất mà Cowl là mục tiêu chính" **tự mâu thuẫn với C-10 trong cùng bài** | BLOCKER | Sửa thành "scenario duy nhất mà **chiếm được** Cowl tự nó là điều kiện thắng" (`Acquire Artifact`), phân biệt rõ với `Transport Artifact` của `Retrieving the Cowl`. Bỏ "như quanh một vật thiêng" (chữ người viết thêm) |
| C-29b | "lore độc lập với Sandro" dựa trên trang **623 byte** | BLOCKER (kèm) | Hạ xuống `INFERENCE` và nói rõ chỉ suy được "trang nguồn không nhắc Sandro", không suy được "map không có Sandro". **Thay bằng chứng cứ dương:** `Mormolykos` — chủ sở hữu có tên trong truyện, và `Tomb Raiders` gọi thẳng "Mormolykos' Cowl" |
| C-19→C-28 | Mis-citation hàng loạt (10 claim dẫn trang 913 byte) | MAJOR | Tách thành 10 key riêng; thêm 5 key mới vào REGISTRY. Ghi cột *Sản phẩm* cho từng dòng — **C-26 là RoE, C-27 là HotA**, trước đó không ghi |
| C-19 | "đi kèm Terek" gán EXPLICIT | MAJOR | Hạ `INFERENCE`. Bằng chứng quyết định: bảng Heroes liệt kê Terek **không kèm artifact**, trong khi wiki **có** ghi `spart_` khi biết (trang `Mormolykos`) |
| C-05 | Câu wiki tóm tắt bị gán `T1*` | MAJOR | Hạ `T6 INFERENCE`, nêu rõ nó nằm ngoài mọi template. Thay bằng nguồn game text thật cho cùng nội dung. Kiểm chứng ngược: `\| biography =` của Terek **không nhắc** Sandro/Cowl/bị bắt |
| C-14 | `T6 EXPLICIT` không hợp lệ | MAJOR | Đổi `{T1 EXPLICIT: h3wiki-artraits-txt}` — **nâng** tier |
| C-30 | `UNVERIFIED` trong thân bài, và **hạ cấp sai chiều** | MAJOR | Tách: "bảng Artifacts không có Cowl" là `EXPLICIT` (đếm được: 12 dòng, tất cả ngẫu nhiên); "không có text mô tả đổi tay" là `INFERENCE` |
| C-18 | "xuất hiện nhiều nhất" không nhãn | MINOR | Gán `INFERENCE` và **ghi rõ đơn vị đếm**. Nêu luôn rằng đổi đơn vị thì Cowl **hoà** với Amulet 10–10 |
| C-01 | Không nhãn | MINOR | Gán `EXPLICIT` cho phần kiểm được, thêm Mormolykos |

### Phát hiện được nâng thành cảnh báo cấp registry

Lỗi mis-citation bảng xuất hiện đã xảy ra ở **cả ba** bài thành phần Cloak, mỗi bài do một verifier
độc lập bắt được. Ba lần thì không còn là sự cố — nên đã thêm mục cảnh báo
**"Trang artifact trên thelazy KHÔNG chứa danh sách scenario"** vào `REGISTRY.md`, kèm bảng kích
thước ba trang (660 / 672 / 913 byte) và cách làm đúng (quét `list=backlinks`, dẫn key riêng từng
dòng, đọc `| source =` để ghi sản phẩm).

Cũng ghi cảnh báo vào hai key đã có:

- `h3wiki-terek` — trang có **hai loại nội dung, tier khác nhau**: `| biography =` là `T1*`, mục
  `== Story ==` là `T6`.
- `h3wiki-vampires-cowl` — 913 byte, **không dùng được** cho bảng xuất hiện.
- `hota-changelog` — ghi rõ tên trang đúng là `Horn of the Abyss (Changelog)`; dạng `/Changelog`
  trả **404**.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-vampires-cowl-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.
