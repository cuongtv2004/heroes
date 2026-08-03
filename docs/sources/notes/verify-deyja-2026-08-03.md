# Verify report: deyja — 2026-08-03

Verifier: agent độc lập, không đọc bài gốc (`docs/codex/kingdoms/deyja.md`), không đọc
`docs/sources/raw/`, không đọc `sandro.md` / `ethric.md` / `jeddite.md` / bài artifact, không đọc
báo cáo khác trong `docs/sources/notes/`.

Phạm vi: **làm hết P1, hết P2, hết P3** — toàn bộ bảng claim.
Số claim kiểm: **68** (⚠️ bảng claim tự ghi "63 claim" nhưng có 68 dòng: P1-01→P1-25 = 25,
P2-01→P2-29 = 29, P3-01→P3-14 = 14 — **lỗi bảng claim**).

CONFIRMED: 42 | DOWNGRADE: 18 | NOT_FOUND: 0 | CONTRADICTED: 8

Mức: BLOCKER 1 · MAJOR 13 · MINOR 19 · NOTE 6

---

## ⚠️ Ba phát hiện làm thay đổi cả nền tảng nguồn của dự án

Đọc ba mục này trước khi đọc chi tiết claim — chúng ảnh hưởng tới nhiều bài, không riêng `deyja`.

### 1. `web.archive.org` KHÔNG bị chặn (2026-08-03)

Cảnh báo đứng lâu nay trong `REGISTRY.md` ("`web.archive.org` — FAILED, bị chặn hoàn toàn") và
premise của P1-05 đều **sai ở thời điểm này**. Kiểm bằng chính URL mà Fandom dẫn:

```
curl -sL "https://web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm"
→ HTTP 200, 23.144 byte
```

Hệ quả: **13 ref archive-based của Fandom Timeline đều xác minh được**, và dự án tiếp cận được
**website chính thức 3DO** — nguồn không-phải-wiki tốt nhất có thể có cho Old Universe.

### 2. Trang chính thức 3DO chốt niên đại Deyja — và **thelazy chép sai hai con số**

*The Diaries of Archibald* (nguồn chính thức 3DO, `3do.com/products/pc/mm7/story/story.htm`):

| Entry | 3DO (chính thức) | thelazy `Archibald#The Diaries of Archibald` |
|---|---|---|
| 1 | 11 June 1165 | 11 June 1165 ✅ |
| 37 | **23 October 1167** | 23 October 1166 ❌ |
| 143 | **5 August 1168** | 5 August 1167 ❌ |

Đây là ca đầu tiên dự án bắt được **thelazy sai và Fandom đúng**. Mọi mốc Deyja lấy từ trang
thelazy `Archibald` phải kiểm lại.

### 3. `Moulder` trên Fandom là một **REDIRECT tới `The Pit`**

```
curl "https://mightandmagic.fandom.com/api.php?action=query&titles=Moulder&redirects"
→ redirects: [{"from":"Moulder","to":"The Pit"}]
```

Fandom **không có** trang `Moulder`. Trường `|capital = [[Moulder]]` trong infobox trỏ về đúng
trang `The Pit`, và trang đó mở đầu bằng "**The Pit** is a region in *MM7* and **the capital of
Deyja**" + `[[Category:Capitals of Enroth]]`. "Tranh chấp thủ đô" phần lớn là **mâu thuẫn nội bộ
của Fandom / redirect cũ**, không phải hai nguồn nói khác nhau.

---

## Chi tiết

# PRIORITY 1

### P1-01
Claim: Thủ đô The Pit hay Moulder — "ba chọi một", giải bằng "The Pit = thủ đô + hoàng cung, Moulder = HQ hành chính của Guild".
Nhãn bài gán: `DISPUTED`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở:
- `https://heroes.thelazy.net/index.php?title=The_Pit&action=raw`
- `https://mightandmagic.fandom.com/api.php?action=query&titles=Moulder&redirects&format=json`
- `https://mightandmagic.fandom.com/api.php?action=parse&page=The%20Pit&prop=wikitext`
- `https://mightandmagic.fandom.com/api.php?action=parse&page=Finneas%20Vilmar&prop=wikitext`

Tìm thấy:
- Fandom API: `"redirects":[{"from":"Moulder","to":"The Pit"}]` — `Moulder` **không tồn tại** như một trang riêng.
- Fandom `The Pit`: "'''The Pit''' is a region in ''Might and Magic VII: For Blood and Honor'' and **the capital of [[Deyja]]**." + `[[Category:Capitals of Enroth]]`
- Fandom `Finneas Vilmar` **tự mâu thuẫn trong cùng một đoạn**: "the other court lords in `[[Moulder]]` began whispering into the puppet King's ear" rồi ba câu sau "Sandro … made a brief return to **the court of Castle Gloaming**".
- Nguồn `T4` mới (`fulton-names-2023`) giải thích **cơ chế** sinh ra loại mâu thuẫn này: "Town names were never part of the specification. Town names were effectively left in the hands of the Map Makers… ► Does this mean that capital names were also created by campaign map makers? ■ To your first question, 'Yes.' Capital names were also created by campaign makers."

Lý do: hai lỗi.
(a) **Khung "ba chọi một" sai**: phía "một" là một *redirect tới chính The Pit*, cộng thêm việc trang `The Pit` của Fandom cũng ghi The Pit là thủ đô. Đây là mâu thuẫn nội bộ Fandom, không phải xung đột giữa hai nguồn độc lập.
(b) **Cách giải không có nguồn**: nó dựa hoàn toàn vào P3-03 ("Moulder là HQ của Guild"), mà P3-03 bị phản bác ở cấp nguồn gốc (xem P3-03). Ngược lại, thelazy `The Pit` nói thẳng "**The Pit is the true heart of the Necromancer's Guild in Antagarich**" — tức là nguồn nói ngược đúng cái mệnh đề đang dùng để giải.
Theo `CANON-POLICY.md` mục 2, `DISPUTED` **"bắt buộc trình bày cả các phương án, không được chọn ngầm một cái"**. Đưa ra một cách giải không nguồn là chọn.
**Phải sửa:** giữ `DISPUTED`; ghi rõ `Moulder` là redirect; bỏ mệnh đề "Moulder = HQ hành chính" hoặc hạ xuống `FAN_THEORY` trong mục riêng; thêm nhận xét `T4` của Fulton về việc tên thủ đô do map maker tự đặt.

### P1-02
Claim: "Không thể là biến thể tên: Moulder là town **trên mặt đất** ở tây bắc, The Pit **dưới lòng đất**."
Nhãn bài gán: (không nhãn)
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `heroes.thelazy.net/index.php?title=Deyja_Moors&action=raw`, `…title=The_Pit&action=raw`
Tìm thấy:
- "Moulder - A town in the northwest, close to the lake that separates this land from `[[AvLee]]`. Featured in `{{mm7}}`."
- "An underground city and capital of `[[Deyja]]`. Home of the royal Castle Gloaming."

Lý do: hai nơi khác nhau — đúng. **MINOR:** "trên mặt đất" là `INFERENCE`, không `EXPLICIT` — nguồn chỉ liệt kê Moulder trong danh sách Towns của vùng bề mặt `Deyja Moors` và nói nó ở cạnh hồ, không có câu nào nói "on the surface". Ghi bước suy luận.

### P1-03
Claim: Trục xuất khỏi Bracada (truyện) vs khỏi Erathia (game text), hai lần.
Nhãn bài gán: `DISPUTED`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Deyja&action=raw` (mục `== Necromancy origin ==`), `…title=A_Gryphon%27s_Heart&action=raw`, và bản archive độc lập `web.archive.org/web/20010219115822/homm3.ga-strategy.com/necromancy.htm`
Tìm thấy:
- Truyện: "Such a practice was so blasphemous (even to the Wizards and Alchemists) that the Necromancers' cult was **exiled from the nation of Bracada** (the southern mountains I mentioned earlier)."
- `region_text` của `A Gryphon's Heart`: "**King Gryphonheart, the man who banished us from Erathia, is dead.** The Nighon and Eeofol invasion has given us the gift of death. At last we can build our armies and invade Erathia ourselves."
- Prologue cùng scenario (Unnamed male general): "**Our nation's goal was to kill the man who banished us from Erathia.**"

Lý do: cả ba trích dẫn khớp nguyên văn. `DISPUTED` là nhãn đúng. Trích dẫn truyện có **hai nhân chứng độc lập** (thelazy + bản archive của The Nether Gods 1998–2000) → độ tin cậy cao hơn bài tự đánh giá.

### P1-04
Claim: Hai sự kiện không loại trừ nhau; và game text có tier cao hơn truyện ngắn.
Nhãn bài gán: (không nhãn riêng)
Phán quyết: **CONFIRMED**
Mức: NOTE
Đã tìm ở: `CANON-POLICY.md` mục 2 + mục 3 (R1, R6); Fandom `Finneas Vilmar`
Tìm thấy: Fandom `Finneas Vilmar` độc lập đưa ra cùng cách dung hòa và gắn nó vào Nicolas: "to resume the Necromancers' scheme of revenge against Erathia for their banishment **by King Nicolas Gryphonheart, earlier in the century**."
Lý do: lập luận đứng được, và có nguồn thứ hai đồng thuận.
**NOTE 1:** kết luận dung hòa là `INFERENCE` (không nguồn nào nói "hai lần trục xuất"). Phải gắn nhãn `INFERENCE` + ghi bước suy luận, theo `CANON-POLICY.md` mục 2.
**NOTE 2:** tier của `t2-necromancy-origin` đáng xem lại. Truyện **không nằm trong game**, được post trên forum 3DO bởi nhân viên NWC → theo bảng tier, đó là mô tả của **`T4`** ("post trên forum"), không phải `T2` ("Manual, strategy guide chính thức… novelization được cấp phép"). Kết luận của bài không đổi (T1 thắng cả T2 và T4, thêm R6), nhưng nhãn nên đúng.

### P1-05
Claim: Timeline Fandom "trông chỉn chu vì nhiều `<ref>`" nhưng **phần lớn** ref trỏ tới `web.archive.org`, và archive.org **bị chặn** — không xác minh được cái nào.
Nhãn bài gán: (không nhãn)
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: `mightandmagic.fandom.com/api.php?action=parse&page=Timeline_(Ancient_universe)&prop=wikitext`; test trực tiếp `web.archive.org`
Tìm thấy (nguồn ngược):
- Đếm trên chính wikitext: **46 named ref được định nghĩa, 13 trỏ tới `web.archive.org`** — tức **28 %**, là **thiểu số**. Danh sách 13: `Catherine`, `Deyja`, `Dracon`, `Gelu`, `JadameSettled`, `Kreegan-Dungeon`, `MM7-Archie`, `MM7-Elves`, `MM7-Silence`, `Nicolas`, `Shadowspire`, `SuccessionWar`, `TimberWars`.
- `curl -sL "https://web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm"` → **HTTP 200, 23.144 byte**, nội dung đọc được đầy đủ.

Lý do: **hai mệnh đề đều sai**. Phần lớn ref là citation game trực tiếp có trích dẫn kèm, không phải archive link. Và archive.org truy cập được — bài (và `REGISTRY.md`) đã kết luận "không xác minh được cái nào" mà không kiểm lại. Đây đúng loại lỗi mà **bài học lớn nhất** của dự án cảnh báo: một claim phủ định trông giống sự cẩn trọng.
**Phải sửa:** viết lại toàn bộ Tranh chấp 3; sửa cảnh báo `web.archive.org` trong `REGISTRY.md` từ FAILED → FETCHED.

### P1-06
Claim: Mốc `1164-09-27` (đầu độc Nicolas) chính xác tới ngày nhưng **không có ref**.
Nhãn bài gán: `T6 UNVERIFIED`
Phán quyết: **CONFIRMED**
Mức: NOTE
Đã tìm ở: Fandom Timeline, dòng 362–365
Tìm thấy nguyên văn ô đó, **không có một `<ref>` nào**:
```
|'''1164 AS:'''
|… Death of Nicolas
|Sandro forges an alliance between Nighon, Vilmar and [[Xenofex]]. [[Stone City]] is invaded.<br />''September 27:'' Lord Haart poisons Nicolas Gryphonheart.<br />
```
Lý do: đúng nguyên văn. Đây là **việc CỤ THỂ số 3** ở P1 — đã tự kiểm, không tin bài.
**NOTE:** có một mảnh xác nhận gián tiếp mà bài chưa dùng: *Diaries of Archibald* Entry 1 (11 June 1165) ghi "Catherine left for Erathia **five months ago** to attend her father's funeral" → tang lễ ~tháng 1/1165, tương thích với cái chết tháng 9/1164 cộng thời gian đi biển 6–8 tuần (chính `Antagarich#Geography` nêu con số đó). Đủ để nói **năm** 1164 hợp lý; **ngày 27/09 vẫn không nguồn**. Giữ `UNVERIFIED` cho ngày.
Vị trí (`Tranh chấp 3`) chấp nhận được — không báo lỗi vị trí.

### P1-07
Claim: Mốc đáng tin nhất là 1168 (Archibald lên ngôi) và 1169 (đảo chính Kastore) — "cả hai truy được về **text MM7 trích thẳng trong bài**, không qua archive link".
Nhãn bài gán: (không nhãn)
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: Fandom Timeline dòng 387–394; `web.archive.org/web/20001017212754/…/mm7/story/story.htm`; thelazy `Archibald`
Tìm thấy (nguồn ngược):
- Dòng 1168: `|''ca 5 August:'' Lord Haart is slain. Nicolas Gryphonheart is eradicated. Archibald becomes king of Deyja.<ref name="MM7-Archie" />` — ref `MM7-Archie` là **`web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`**, tức **đúng là archive link**, và **không có trích dẫn nội dung kèm**.
- Dòng 1169: ref `ArchieDeposed` có trích MM7 — nhưng nội dung trích là "*Factionism and discord have created an intolerable situation in Deyja…*", **không nêu năm và không nêu Kastore**. Ref `RolandRescue` chỉ gọi Archibald là "deposed lord of Deyja".

Lý do: cả hai mốc **không** truy được về text trích thẳng trong bài. Mốc 1168 nằm đúng trong nhóm archive mà bài tuyên bố không xác minh được; mốc 1169 có trích dẫn nhưng trích dẫn đó **không chứa năm**. Bài đánh giá độ tin cậy nguồn **ngược**.
Bù lại — vì archive.org vào được — tôi lấy được nguồn gốc và **kết quả 1168 là đúng**: *Diaries of Archibald* Entry 143 = **5 August 1168**, ngay sau bài phát biểu chiến thắng của Catherine, "For as the lich, Gryphonheart, replaced Deathknell, **so have I replaced Gryphonheart**."
Nhưng: thelazy chép entry đó là **1167**. → mốc này phải là `DISPUTED` giữa hai bản chép, với bản 3DO chính thức thắng theo R1/R3.
**Phải sửa:** viết lại lý do tin 1168 (nguồn chính thức 3DO, không phải "trích thẳng trong bài Fandom"); ghi `DISPUTED` 1167/1168 kèm cảnh báo thelazy chép sai; hạ 1169 xuống `INFERENCE` (khung thời gian MM7), không `EXPLICIT`.

### P1-08
Claim: "No war has ever been declared on Deyja — even if the Necromancers were completely destroyed, the land is uninhabitable."
Nhãn bài gán: `T2* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: thelazy `Deyja` mục `== Necromancy origin ==`; **và độc lập** `web.archive.org/web/20010219115822/homm3.ga-strategy.com/necromancy.htm`
Tìm thấy (bản archive, nguyên văn): "The elves have been unable to stop this slow spread of lifelessness, nor has any other nation even tried. **No war has ever been declared on Deyja - even if the Necromancers were completely destroyed, the land is uninhabitable.**"
Lý do: khớp từng chữ ở hai nguồn độc lập.

### P1-09
Claim: Truyện có trước RoE; Restoration Wars ứng nghiệm câu kết; phải định niên đại câu này về trước 1164.
Nhãn bài gán: (không nhãn riêng)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: bản archive nêu trên; thelazy `Lost Lore`
Tìm thấy:
- Câu kết: "In my humble opinion, **it is but a matter of time until someone does declare war upon Deyja.**"
- thelazy `Lost Lore`: "Christian Vanover, `{{homm3}}` **assistant director**, wrote a series of texts that were being posted on the official 3DO forums **as `{{roe}}` approached its release**."
- Bản archive được chụp 19/FEB/2001 từ site The Nether Gods, ghi bản quyền "1998-2000".

Lý do: mốc "trước RoE" có nguồn thẳng. Định niên đại "trước 1164" là `INFERENCE` hợp lệ — phải ghi rõ là suy luận.

### P1-10 ⭐
Claim: **Có HAI vị vua trước Finneas**; "chi tiết mà cả hai wiki lớn đều bỏ sót, chỉ lộ ra khi đọc region text". Bằng chứng 1 = region text `Finneas Vilmar`.
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `heroes.thelazy.net/index.php?title=Finneas_Vilmar&action=raw` (⚠️ tên trang đúng là `Finneas_Vilmar`; `Finneas_Vilmar_(scenario)` trả **404** trên thelazy — **lỗi tra cứu tiềm tàng**, tên đó chỉ đúng trên Fandom)
Tìm thấy, trong trường `| region_text =` — **đúng chỗ BH-1 chỉ**:
"Sandro and Finneas Vilmar are going to wipe out `[[Lord Alarice]]` before he can tell the others of **Finneas' transgressions against the old King of Deyja**. Once they have completed this trivial task, they will be able to work on removing other bothersome lords from the **Deyja court**."

Lý do: **trích dẫn khớp nguyên văn 100 %** và nó thật sự nằm trong region text — phát hiện của bài là thật, BH-1 áp dụng đúng. Hai điểm phải sửa:
(a) **Nhãn**: câu trích là `EXPLICIT`, nhưng kết luận "**hai** vị vua" là ghép hai scenario khác nhau (`Finneas Vilmar` → "the old King"; `Duke Alarice` → "the new king"). Không nguồn nào nói "hai vua". → kết luận tổng hợp phải là `T1* INFERENCE` + ghi bước suy luận; giữ `EXPLICIT` cho từng trích dẫn.
(b) **Nói quá về nguồn**: cả hai wiki **có** ghi một vua tiền nhiệm. thelazy `Finneas` mục `== Story ==`: "Sandro and Finneas impress **the current king**. In short time, however, Sandro **deposes the current king** and install Finneas on the throne." Fandom `Finneas Vilmar` infobox: `predecessors = Unnamed King of Deyja (as king)`. Cái hai wiki bỏ sót là **vị thứ hai**, không phải "cả chi tiết". Viết chính xác: *"cả hai wiki ghi một vua tiền nhiệm không tên; region text hàm ý có hai."*

### P1-11
Claim: Bằng chứng 2 — "The new king is still not settled into his throne and will be easily replaced. With any luck, he will suffer an accident in the future"; và "the new king" **không phải** Finneas.
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `heroes.thelazy.net/index.php?title=Duke_Alarice&action=raw`, trường `| region_text =`
Tìm thấy nguyên văn: "All `[[Finneas]]` or `[[Sandro]]` must do is remove the Duke of this area. **Once he is gone, they will be literally a step away from the throne. The new king is still not settled into his throne and will be easily replaced. With any luck, he will suffer an accident in the future.**"
Lý do: khớp từng chữ. Lập luận "the new king ≠ Finneas" đứng vững vì cùng câu nói Finneas/Sandro mới chỉ "a step away from the throne". Xác nhận thêm bằng epilogue (P1-12) và bằng thelazy `Finneas`: "Sandro deposes the current king and install Finneas on the throne."

### P1-12
Claim: Bằng chứng 3 (epilogue) — "The King is impressed with Finneas' stunning show of force and ability. Soon the King will understand the full view of my vision. Then it will be too late for him."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Duke_Alarice&action=raw`, mục `== Epilogue ==`
Tìm thấy nguyên văn (Sandro): "Our plan has been a great success! We are quickly on the rise. **The King is impressed with `[[Finneas]]`' stunning show of force and ability. Soon the King will understand the full view of my vision. Then it will be too late for him.**"
Lý do: khớp từng chữ. Xác nhận độc lập: Fandom `Finneas Vilmar` diễn đạt lại cùng cảnh — "impressing **the current King** with such a stunning show of force and ability" — nên vị vua đó còn sống khi chiến dịch kết thúc là chắc.

### P1-13
Claim: Cả hai vua đều không tên và điều này **có nguồn**: `predecessors = Unnamed King of Deyja`; và Fandom tự nêu lỗ hổng "(though it is not explained how in detail)".
Nhãn bài gán: `T6 EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `mightandmagic.fandom.com/api.php?action=parse&page=Finneas%20Vilmar&prop=wikitext`
Tìm thấy:
- `|predecessors = Unnamed King of Deyja (as king)`
- "Soon afterwards, Finneas and Sandro overthrew the King of Deyja **(though it is not explained how in detail)**, and Finneas became the new ruler."
Lý do: cả hai khớp nguyên văn.
**MINOR:** trích dẫn của bài bỏ hậu tố "` (as king)`". Hậu tố đó có nội dung: nó đi kèm `successors = Lich King Gryphonheart (as king)` / `Archibald Ironfist (as guildmaster)` — tức Fandom **tách hai chức vụ**, điều phản bác P2-19 (xem P2-19). Trích đủ.
Ngoài ra Fandom chỉ ghi **một** vua không tên, không phải hai — nên nguồn này chống lưng cho "vua thứ hai không tên", không cho "cả hai đều không tên".

### P1-14
Claim: Danh sách *Rulers* trên thelazy bỏ hẳn hai mục và bắt đầu từ Finneas — mâu thuẫn với chính trang scenario của thelazy.
Nhãn bài gán: (không nhãn)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Deyja&action=raw`
Tìm thấy nguyên văn mục `== Rulers ==`: chỉ bốn dòng — `King Finneas Vilmar`, `King Nicolas Gryphonheart / Lich King Gryphonheart`, `King Archibald Ironfist`, `Kastore`.
Lý do: đúng, bắt đầu từ Finneas. Và mâu thuẫn nội bộ là thật: cùng wiki, trang `Duke_Alarice` có "the new king" trong region text và trang `Finneas` có "Sandro deposes the current king".

### P1-15 ⭐
Claim: Ám sát là thủ tục kế vị; không có hội đồng necromancer nào được chứng thực; danh từ lặp lại là **court** và **lords**, không bao giờ **council**; và claim phủ định này đã được kiểm vì AvLee **có** "Council of Elders".
Nhãn bài gán: (không nhãn)
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `…title=Finneas_Vilmar&action=raw`, `…title=With_Blinders_On&action=raw`, `…title=A_Gryphon%27s_Heart&action=raw`, `…title=AvLee&action=raw`, Fandom `Falorel`
Tìm thấy:
- "court": "removing other bothersome lords from the **Deyja court**" (`Finneas Vilmar`); "always harassing you in **court**" (`With Blinders On`)
- "lords": "**our lords** watch their new king, searching for a sign of weakness" (`A Gryphon's Heart`, epilogue); "These young upstart **lords**" (`With Blinders On`)
- **"council" = 0 lần** trong toàn bộ text Deyja tôi fetch. Trang thelazy `AvLee` cũng **không** có chữ "council"/"elders" — nhưng Fandom `Falorel` **có**: "The **`[[Council of Elders]]`** later sent Gelu to avenge the deaths of Falorel…"
Lý do: claim phủ định đứng vững, và cách kiểm chéo (AvLee có council nên wiki dùng từ đó khi đúng) hoạt động — chỉ khác là nguồn nằm trên Fandom, không phải thelazy `AvLee`. Sửa source key.
**MINOR — bỏ sót có ý nghĩa:** thể chế tập thể **được chứng thực** của Deyja không phải council mà là **Necromancers' Guild / Necromantic Order**. Fandom `Necromancers' Guild`: "The Necromancers' Guild in `[[Antagarich]]` **ruled the nation of Deyja**, under the control of guildmaster and king `[[Finneas Vilmar]]`." Nói "không có thể chế tập thể, chỉ có ám sát" mà không nhắc Guild là thiếu.

### P1-16
Claim: "**Bốn cuộc kế vị được ghi lại. Bốn vụ giết.**"
Nhãn bài gán: (không nhãn)
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: `web.archive.org/…/mm7/story/story.htm`; Fandom `Deyja`; Fandom `Necromancers' Guild`; Fandom Timeline ref `RolandRescue`; thelazy `Deyja`, `Kastore`
Tìm thấy (nguồn ngược):
- Kế vị Nicolas → Archibald **không phải giết**: Nicolas bị liên quân của Catherine tiêu diệt, không bị người kế vị giết. Diaries Entry 143: "her father 'now lies in the state of natural quietude he deserves'… so have I **replaced** Gryphonheart."
- Kế vị Archibald → Kastore **không phải giết**: thelazy `Deyja`: "Kastore later staged a coup and **ousted** Archibald from Deyja's throne." Fandom `Deyja`: "Kastore staged a coup and ousted Archibald from Deyja's throne. **Archibald fled Deyja** along with the necromancers from the Science arm." Và Archibald **còn sống sau đó**, có text MM7 chứng minh: "**Archibald Ironfist, deposed lord of Deyja** and one of the most hated men in history, **offered aid** for reasons of his own."
- Kế vị "vua cũ → vua mới": **không có text nào** mô tả một vụ giết.
- Kế vị "vua mới → Finneas": Fandom nói thẳng "**it is not explained how in detail**".
Lý do: trong 4–5 cuộc kế vị được ghi lại, **đúng một** là vụ giết do người kế vị thực hiện (Finneas → Nicolas: "the lich **killed** Deathknell"; "**After killing King Vilmar**, he took command of their military and their throne"). Câu đối ngẫu "Bốn kế vị. Bốn vụ giết." nghe hay nhưng **sai dữ kiện**.
**Phải sửa:** thay bằng phát biểu đúng — ví dụ "trong các cuộc kế vị được ghi lại, chỉ một được text mô tả là giết; hai vụ khác chỉ có ý định giết được nói ra; hai vụ cuối là phế vị, người bị phế đều sống sót."

### P1-17
Claim: Krewlod — không có quan hệ nào được chứng thực; hai nước không chung biên giới.
Nhãn bài gán: `T1* INFERENCE`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=Antagarich&action=raw`, `…title=Krewlod&action=raw`
Tìm thấy:
- `Antagarich`, mục `== Political Landscape ==`: "`{{town|Necropolis|loc=Deyja}}` is landlocked, surrounded by Erathia to its South and West, and Avlee to its North and East." · "`{{town|Stronghold|loc=Krewlod}}` is on the western coast, between Erathia and Bracada."
- `Krewlod`: "It is bordered by `[[Bracada]]` to the south and east and by `[[Erathia]]` to the north and east."
Lý do: **kết luận đúng** — không nguồn nào cho Deyja và Krewlod chung biên giới, và hai mô tả biên giới độc lập đều không nhắc nhau. Nhưng **tier sai**: mục `== Political Landscape ==` là **văn biên tập viên wiki**, ngoài mọi template, cùng loại với `== Story ==` trên `h3wiki-terek` mà `REGISTRY.md` đã cảnh báo. Không phải in-game text. → phải là `T6 INFERENCE`, không `T1* INFERENCE`.

### P1-18
Claim: Deyja không xuất hiện trong MM6, lý do là địa lý (MM6 ở lục địa Enroth, không phải Antagarich); và cảnh báo không được viết claim đó trống trơn.
Nhãn bài gán: (không nhãn)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: Fandom `Deyja` infobox; `mightandmagic.fandom.com/api.php?action=query&list=allpages&apprefix=Deyja`; `heroes.thelazy.net/api.php?action=query&list=allpages&apprefix=Deyja`; thelazy `Antagarich` mục Trivia; Fandom `Necromancers' Guild`
Tìm thấy:
- Fandom `Deyja`: `|appearances = {{Icon-H3X2}}{{Icon-H3}}{{Icon-MM7}}` — **không có icon MM6**. Đây là nguồn khẳng định cho một claim phủ định, đúng cách.
- Không có trang Deyja nào gắn MM6 trên cả hai wiki (kết quả allpages ở P1-22).
- thelazy `Antagarich` Trivia: "Antagarich is located far to the southeast of `[[Enroth (continent)|Enroth]]`, `[[Jadame]]` and `[[Regna]]`… **as mentioned in `{{mm6}}`**" — MM6 nhắc Antagarich như nơi xa, không lấy bối cảnh ở đó.
- Fandom `Necromancers' Guild`: guild trên lục địa Enroth "fled to the `[[Mire of the Damned]]`, settling in `[[Castle Darkmoor]]`" — đó là MM6, và ở Enroth.
Lý do: claim phủ định có căn cứ dương (trường `appearances`) + lý do địa lý có nguồn. Cảnh báo cách viết là đúng và cần giữ.

### P1-19
Claim: Necromancers' Guild trong MM6 (Castle Darkmoor, Nimbus) chính là tổ chức di cư sang Deyja **khoảng 1166** để phục vụ Lich King.
Nhãn bài gán: `T6 INFERENCE`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `web.archive.org/web/20001017212754/…/mm7/story/story.htm`; thelazy `Nimbus`, `Archibald`; Fandom `Necromancers' Guild`
Tìm thấy (nguồn chính thức 3DO, *Diaries of Archibald*, **Entry 37 — 23 October 1167**):
"Nimbus returned to his estates bringing with him a small party of Necromancers - apparently all of any power that remained in Enroth - he was gathering to **take to Deyja in Erathia so that they might serve the lich-king, Nicolas Gryphonheart**."
Lý do: **nội dung claim đúng và mạnh hơn bài tưởng — nhưng năm sai**.
(a) **Tier**: đây là `EXPLICIT` từ nguồn chính thức 3DO (`T2`), không phải `T6 INFERENCE`. Nâng hai bậc.
(b) **Năm**: bản 3DO ghi **1167**; thelazy `Nimbus` ghi "by 1166 AS" và thelazy `Archibald` chép Entry 37 là "23 October 1166". Bài lấy con số của thelazy. → phải ghi `DISPUTED` 1166/1167, với bản 3DO thắng.
**Phải sửa:** đổi nhãn thành `T2 EXPLICIT` (nguồn 3DO mới) và đổi năm thành 1167 kèm ghi chú DISPUTED.

### P1-20
Claim: Tên **Deyja Moors** và **Deyja Badlands** như đơn vị vùng đến từ bản đồ campaign HotA → theo R5 không phải canon Old Universe.
Nhãn bài gán: `T6 FAN_THEORY`
Phán quyết: **CONTRADICTED**
Mức: **BLOCKER**
Đã tìm ở:
- `heroes.thelazy.net/index.php?title=Horn_of_the_Abyss_(Changelog)&action=raw` (201.529 byte — **nguồn BH-3 yêu cầu**)
- `…title=Deyja_Moors&action=raw`, `…title=Deyja_Badlands&action=raw`
- Fandom `Watchtower 6`, `William Setag` (tên quest MM7)

Tìm thấy (nguồn ngược):
1. **Changelog HotA: `Deyja` = 0 lần, `Antagarich` = 0 lần, `Moors` = 0 lần, `Badlands` = 0 lần.** Nguồn chuẩn cho mọi claim HotA **không nói gì** về hai tên này.
2. **"Deyja Moors" là tên vùng trong game MM7**, xuất hiện trong **chuỗi tên quest MM7**:
   - "Go to Watchtower 6 in the **Deyja Moors**, and move the weight from the top of the tower to the bottom of the tower. Then return to William Lasker in the Erathian Sewers"
   - "Capture Alice Hargreaves from her residence in Castle Gryphonheart and return her to William's Tower in the **Deyja Moors**"
   - "Rescue Alice Hargreaves from William's Tower in the **Deyja Moors** then talk to Sir Charles Quixote"
3. thelazy `Deyja Moors` **tự phân biệt hai việc**: "A region that spans much of Deyja. **Featured in `{{mm7}}`**." … rồi **riêng một câu**: "This name is **also** used for the western part of Deyja on the `{{hota}}` campaign map." Chữ "**also**" nói rõ tên có trước HotA.
4. Chỉ **Deyja Badlands** là của HotA: "A region in southern Deyja. **The name "Deyja Badlands" for this part of the continent comes from the `{{hota}}` campaign map of `[[Antagarich]]`**."

Lý do: bài **gộp hai thứ khác nhau** và dán nhãn `FAN_THEORY` lên một tên vùng canon của MM7 (NWC). Đây là BLOCKER vì ba lẽ cộng lại: (a) sai dữ kiện; (b) hạ một tên canon xuống non-canon, tức bóp méo canon theo hướng ngược với mục đích của R5; (c) `FAN_THEORY` nằm trong mục *Địa điểm* (thân bài), vi phạm `CANON-POLICY.md` mục 5.5 vốn đòi `FAN_THEORY` phải ở mục riêng.
**Phải sửa:** `Deyja Moors` → `T1* EXPLICIT` (tên vùng MM7, dẫn qua chuỗi quest MM7 + thelazy `Deyja Moors`), đưa vào thân bài bình thường. `Deyja Badlands` → giữ ghi chú HotA nhưng nói rõ **changelog HotA không xác nhận**, nên nguồn duy nhất là câu văn biên tập viên thelazy (`T6`); nếu vẫn muốn `FAN_THEORY` thì phải chuyển sang mục riêng.

### P1-21
Claim: (a) Vokial không có trong hero list của `Duke Alarice`, chỉ là portrait cho hồ sơ Death Knight của Lord Alarice; (b) Lord Fayette là lãnh chúa AvLee; (c) Aislinn, Tamika, Nagash chỉ là đối thủ trên map, không story text.
Nhãn bài gán: (không nhãn)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Duke_Alarice&action=raw`, `…title=Finneas_Vilmar&action=raw`, `…title=Lord_Alarice&action=raw`, `…title=With_Blinders_On&action=raw`, Fandom `Alarice`, Fandom `Falorel`
Tìm thấy:
- (a) Hero list của `Duke Alarice`: `{{hero row|11, 8, 0|blue|Duke Alarice (hero)|image=Nimbus|name=Duke Alarice|Necromancer}}`, `Aislinn`, `Tamika`, `Nagash`, `Sandro`, `Finneas` — **không có Vokial**. Vokial chỉ là `image=`/`link=` trong `Finneas Vilmar`: `{{Hero row|17, 57, 0|blue|Lord Alarice|Death Knight|link=Vokial|image=Vokial}}`. Fandom `Alarice` xác nhận độc lập: "In the Finneas Vilmar scenario, Alarice has the same **icon** and specialty as `[[Vokial]]`. In the Duke Alarice scenario, he has the same icon and specialty as `[[Nimbus]]`." Thêm chứng cứ: cùng portrait Vokial còn được dùng cho `Lord Dufus` trong `With Blinders On` → đúng là portrait dùng lại, không phải nhân vật.
- (b) Fandom `Falorel`: Fayette là "one of Falorel's **peers**", Falorel là "Border Lord at the **AvLee**-Deyja border", "`{{AvLee}}`" navbox. thelazy `Lord Falorel`: "`[[AvLee]]`an `[[Border Lord]]` and **neighbor of `[[Lord Fayette]]`**". Và Fandom Timeline dòng 344 đúng là đặt cạnh nhau gây hiểu nhầm: "Duke Alarice and Lord Fayette are eradicated."
- (c) Aislinn/Tamika/Nagash chỉ xuất hiện trong `==== Heroes ====`; `Duke Alarice` **không có mục `==== Events ====`** nào, timed event duy nhất (Day 1) không nhắc ba hero này. Đã kiểm cả `==== Events ====`, `=== Timed events ===` và `region_text` theo BH-1.
Lý do: cả ba cảnh báo phân loại đều đúng và có nguồn. Đây là phần chắc nhất của bài.

### P1-22
Claim: "`Deyja (disambiguation)` chưa kiểm được trên cả hai wiki — thelazy trả về rỗng. Rỗng không đồng nghĩa với xác nhận không tồn tại."
Nhãn bài gán: (không nhãn)
Phán quyết: **CONTRADICTED**
Mức: MINOR (nhưng đây là **việc CỤ THỂ số 2** và nó đã được làm xong)
Đã tìm ở:
```
heroes.thelazy.net/api.php?action=query&list=search&srsearch=Deyja&srlimit=50
heroes.thelazy.net/api.php?action=query&list=allpages&apprefix=Deyja&aplimit=100
heroes.thelazy.net/index.php?title=Deyja_(disambiguation)&action=raw
mightandmagic.fandom.com/api.php?action=query&list=search&srsearch=Deyja&srlimit=50
mightandmagic.fandom.com/api.php?action=query&list=allpages&apprefix=Deyja&aplimit=100
```
Tìm thấy:
- thelazy `list=search` **không rỗng** — trả 4 kết quả: `Deyja`, `Deyja Badlands`, `Deyja Moors`, `Deyja minor locations`.
- thelazy `list=allpages&apprefix=Deyja` (kiểm dứt điểm): `Deyja`, `Deyja Badlands`, `Deyja Moors`, `Deyja minor locations`, `Deyjan` (= redirect `#REDIRECT[[Deyja]]`).
- thelazy `Deyja_(disambiguation)&action=raw` → **HTTP 404**.
- Fandom `allpages&apprefix=Deyja`: chỉ `Deyja`, `Deyja Moors`. Trong 50 kết quả search không có trang disambiguation nào.
**Kết luận: KHÔNG có `Deyja (disambiguation)` trên cả hai wiki, và không có thực thể "Deyja" thứ hai nào.** Không lặp lại được tiền lệ `Sandro (Xeen)`.
Lý do: bài nói "thelazy trả về rỗng" — **sai**. `list=search` hoạt động bình thường với từ khoá thường; chỉ `insource:` mới rỗng (CirrusSearch tắt), và đó là chuyện khác. Câu hỏi mở này **đóng được ngay**, không cần để tồn đọng.
**Bẫy BH-2 thật sự nằm ở chỗ khác** — và bài chưa nêu: **`Kastore` có HAI người.** thelazy `Kastore` Trivia: "A different Elven sorcerer **also named Kastore** but hailing from Enroth was featured in `{{homm1}}` and `{{homm2}}` as a Warlock." Fandom phân trang thành `Kastore (Terra)`. Mọi claim về Kastore (P2-16, P2-17, P3-12) **phải ghi rõ `Kastore (Terra)`**.

### P1-23
Claim: *Deyja* nghĩa là "chết" trong tiếng Bắc Âu cổ và tiếng Iceland.
Nhãn bài gán: **`T6 EXPLICIT`**
Phán quyết: **DOWNGRADE** (thực chất là **UPGRADE tier + sửa nội dung**)
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Gregory_Fulton/On_Names_in_Heroes_of_Might_and_Magic_III&action=raw` (98.499 byte, dòng 517–518); Fandom `Deyja` mục Trivia
Tìm thấy — **nguồn `T4`, chính Lead Designer Heroes III**:
"■ **Deyja is derived from Old Norse meaning 'to die'.** Deyja a barren wasteland, and home of the `[[undead]]`. **Deyja is the 'to die' nation, the nation of death.**"
Và Fandom (`T6`): "*Deyja* means "**to die**" in Old Norse **and Icelandic**. In fact, the English word *die* descends from *deyja*, an Old Norse loanword that displaced native words like *steorfan* and *sweltan*."
Lý do: đây là **việc CỤ THỂ số 1** ở P1 và nó cho ba kết quả:
(a) **Nâng `T6` → `T4`** cho phần "Old Norse, 'to die'" — có nguồn phát ngôn của người đặt tên.
(b) **Sửa nghĩa**: "'to die'" là **động từ**, không phải danh từ "chết". Fulton còn cho **ý định thiết kế** ("the nation of death") — thuộc mục Dev Intent/Trivia theo R6.
(c) **"tiếng Iceland" vẫn chỉ có `T6`** — Fulton không nhắc Iceland. Phải tách hai nhãn, không gộp.

**Cũng đã kiểm theo yêu cầu — `The Pit`, `Moulder`, `Necropolis`, `Necromancer` trong tài liệu Fulton:**
- **`Moulder`: 0 lần. `Gloaming`: 0 lần. `Nimbus`: 0 lần. "The Pit" (địa danh): 0 lần** (5 lần chuỗi "pit" đều là mảnh của từ khác: ca**pit**al, Ca**pit**alize, ca**pit**alized).
- **`Necropolis` (6 lần)** — không entry nào cho một town Necropolis của Deyja. Nội dung dùng được: (i) chủ đề đặt tên faction — "`[[Necropolis]]` - **Death. Decay. Undead.**"; (ii) nguồn gốc tên faction — "the `[[Necromancer]]` a `[[Necropolis]]`" nhằm giữ liên tục với HoMM2; (iii) town Necropolis duy nhất được giải thích là **Cessacioun**: "Cessation; being brought to an end. This is a Necropolis Town, a place where 'life' is brought to an end."
- **`Necromancer` (4 lần)** — dùng được nhất: "**Thant** is related to **Thanatos**; the Greek god of death. Thant is a `[[Necromancer]]`, so it fits with the theme." (liên quan `h3wiki-thant`/`h3wiki-finneas` vì Finneas dựa trên Thant.)
- **⭐ Phát hiện ngoài yêu cầu, và nó là mảnh quan trọng nhất cho P1-01:** "For the Campaigns (RoE and AB), each Map Maker was given a set of map specifications… **Town names were never part of the specification. Town names were effectively left in the hands of the Map Makers**, working under the assumption they would comply with any 'lore' requirements." → "► Does this mean that **capital names** were also created by campaign map makers? ■ To your first question, '**Yes.**' Capital names were also created by campaign makers." Cộng thêm: "**Christian Vanover** and **Dave Botan** (deceased) made all of the campaign maps" và "I created a moderately detailed outline, and the Map Makers wrote the chapters."
  Đây là `T4 EXPLICIT` cho **cơ chế** sinh ra mâu thuẫn tên thủ đô — dùng được ngay ở mục Tranh chấp 1.

### P1-24
Claim: Deyja là "một trong số ít quốc gia mà sự cằn cỗi của nó là sản phẩm do chính nó tạo ra"; "không bị chinh phục", "không được lập ra như một vương quốc".
Nhãn bài gán: (không nhãn)
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: bản archive Necromancy origin; thelazy `Deyja` mục History; thelazy `Antagarich`; Fandom `Deyja`
Tìm thấy:
- Ủng hộ phần "tự tạo ra sự cằn cỗi": "the Necromancers, trying to reach their goal of a perfect resurrection, **slowly drained all the life around them**" · "**continues to grow like a cancerous scar in the heart of the AvLee**".
- Ủng hộ phần "không được lập ra như một vương quốc": "the cult **eventually settled** in the AvLee" (định cư, không lập quốc). thelazy `Antagarich`: "the necromancers were exiled from Bracada and settled in the heart of AvLee, **forming** the undead kingdom of Deyja." Fandom Timeline: "The cult settles in southern AvLee, and **evolves into** the kingdom of Deyja."
Lý do: hai mệnh đề sau **đứng được ở mức `INFERENCE`**, không `EXPLICIT` — nguồn nói "settled/formed/evolved into", chưa nguồn nào nói "không được lập ra". **MINOR chính:** so sánh cấp bậc "**một trong số ít quốc gia** trong Old Universe" **không có nguồn nào** — không tài liệu nào so Deyja với các quốc gia khác về điểm này. Hoặc bỏ so sánh, hoặc chuyển sang mục nhận định có nhãn riêng.
**Cũng lưu ý:** Fandom Timeline đặt ngày lập Deyja là "**Unknown AS**" — tức Fandom **từ chối định năm**. Đây là chứng cứ ủng hộ P2-10 là `INFERENCE` của dự án, không phải con số có sẵn.

### P1-25
Claim: Deyja bị hủy diệt trong **Reckoning**.
Nhãn bài gán: `T6 UNVERIFIED` — **trong mục *Lịch sử*** (thân bài)
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: Fandom `Deyja` mục "Final days"; `heroes.thelazy.net/index.php?title=The_Reckoning&action=raw`
Tìm thấy:
- Fandom `Deyja`: "Like all the other nations on the world of `[[Enroth (planet)|Enroth]]`, Deyja was destroyed in the `[[Reckoning]]`." (không ref)
- thelazy `The Reckoning`: "A cataclysmic event that **rendered the planet of `[[Enroth (planet)|Enroth]]` uninhabitable**. On **February 10th, 1177 AS**, a massive explosion is created by the clash of Gelu's Armageddon's Blade and Kilgor's Sword of Frost…" kèm trích `Lost Manuscripts` (Lysander): "we knew it was going to **break apart the world**."
Lý do: **hai lỗi cần sửa.**
(a) **Vi phạm `CANON-POLICY.md` mục 5.3**: `UNVERIFIED` nằm trong *Lịch sử* = thân bài. Mục 5.3 cấm điều này (khác P1-06 và P3-13, hai claim đó ở đúng mục nên tôi không báo lỗi vị trí).
(b) **Không cần để `UNVERIFIED`**: claim này giải được ngay. Deyja ở trên hành tinh Enroth; Reckoning làm hành tinh Enroth không thể ở được (10/FEB/1177 AS). → viết lại thành `T1*/T2* INFERENCE: (nguồn về Reckoning) — Deyja ở trên Enroth, Enroth bị hủy` và đưa vào thân bài hợp lệ.

---

# PRIORITY 2

### P2-01
Claim: "Deyja is landlocked, surrounded by Erathia to its South and West, and AvLee to its North and East."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=Antagarich&action=raw`, mục `== Political Landscape ==` (dòng 42)
Tìm thấy: "`{{town|Necropolis|loc=Deyja}}` is landlocked, surrounded by Erathia to its South and West, and **Avlee** to its North and East."
Lý do: **nội dung khớp**, hai điểm phải sửa. (a) **Tier**: `== Political Landscape ==` là văn biên tập viên wiki, không phải in-game text — cùng loại đã bị bắt ở `h3wiki-terek` và `sod-hack-and-slash`. Phải là `T6`, hoặc `T1* INFERENCE` nếu dẫn về bản đồ H3/MM7 trong gallery cùng trang. (b) **Chính tả trong trích dẫn**: nguồn viết "**Avlee**", bài viết "AvLee". Trích nguyên văn thì phải giữ, hoặc dùng `[sic]`.

### P2-02
Claim: Goblin là đa số trong số cư dân còn sống.
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=Deyja_Moors&action=raw`
Tìm thấy: "It is also populated by `[[goblin|goblins]]`, **who are a majority among Deyja's living citizens**."
Lý do: khớp nguyên văn. Nhưng toàn trang `Deyja Moors` **không có một template text in-game nào** — nó là văn biên tập viên mô tả nội dung MM7. → `T6 EXPLICIT`, không `T1* EXPLICIT`. (Xác nhận phụ độc lập: Fandom `Deyja` mục `== Allies ==` liệt kê Goblin → Hobgoblin → Goblin lord là đồng minh của Deyja trong MM7.)

### P2-03
Claim: Thủ đô là thành phố ngầm, có hoàng cung **Castle Gloaming**.
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=The_Pit&action=raw`; Fandom `The Pit` mục `== Map guide ==`
Tìm thấy:
- thelazy: "An underground city and capital of `[[Deyja]]`. **Home of the royal Castle Gloaming.**"
- Fandom `The Pit`, điểm 20 trên bản đồ MM7: "`[[Castle Gloaming]]`" — và gallery có file `Castle Gloaming entrance.png`.
Lý do: nội dung khớp và có **xác nhận độc lập** (Castle Gloaming là một điểm thật trên map MM7). Chỉ tier sai: trang `The Pit` (827 byte) là văn biên tập viên, không template in-game → `T6`. Nếu muốn `T1*` thì phải dẫn về map MM7/quest string, không dẫn về câu văn wiki.

### P2-04
Claim: "It is commonly said that the surface of Deyja is only a small part of the kingdom of death, contrary to the Pit."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `…title=The_Pit&action=raw`
Tìm thấy khớp từng chữ: "**It is commonly said that the surface of Deyja is only a small part of the kingdom of death, contrary to the Pit.**"
Lý do: trích dẫn chính xác. **MINOR:** tier `T1*` sai như P2-03 (văn wiki). Và bản thân câu tự rào bằng "It is commonly said" — nếu dùng, phải giữ nguyên phần rào đó, đừng biến thành khẳng định.

### P2-05
Claim: The Pit là trung tâm Path of Darkness, "mirroring Bracada's capitol of Celeste".
Nhãn bài gán: `T6 EXPLICIT`, key `fandom-path-of-darkness`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `…title=The_Pit&action=raw`; Fandom `Path of Darkness` (đọc toàn bộ)
Tìm thấy — trên **thelazy**, không phải Fandom: "This subterranean city is also central to the Path of Darkness, a faith practiced by people throughout the `[[Enroth (planet)|world]]`, **mirroring `[[Bracada]]`'s capitol of `[[Celeste]]`**."
Lý do: **mis-citation**. Trang Fandom `Path of Darkness` **không chứa** câu này (nó chỉ có mô tả cơ chế + bảng quest). Sửa source key thành `h3wiki-the-pit`. Xác nhận độc lập cho ý đối xứng: Fandom `The Pit`: "Characters that follow the `[[Path of Darkness]]` must go here to get their main quests, while those that follow the `[[Path of Light]]` must go to `[[Celeste]]`."

### P2-06
Claim: Nguồn gốc dựa vào truyện ngắn của **Christian Vanover** (nhân viên NWC), đăng trên diễn đàn 3DO nay đã đóng; người kể là **Marcus Finch**; bài ghi rõ nó **không thể tiếp cận ở dạng gốc**.
Nhãn bài gán: `T2* EXPLICIT`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=Lost_Lore&action=raw`; `web.archive.org/web/20010219115822/homm3.ga-strategy.com/necromancy.htm`; `…title=Gregory_Fulton/On_Names…&action=raw`
Tìm thấy:
- thelazy `Lost Lore`: "`[[Christian Vanover]]`, `{{homm3}}` **assistant director**, wrote a series of texts that were being posted on the official 3DO forums as `{{roe}}` approached its release. **They were never incorporated in the game itself**, but there are numerous references to them in hero bios and other texts… **never contradicting canon (except for one of them)**… Many of these stories were **rehosted on the now-defunct "The Nether Gods" fan site**."
- Bản archive của The Nether Gods (chụp 19/FEB/2001) — **đọc được toàn văn**, và ký cuối chỉ "**-Finch**", không có chữ "Marcus".
- Fulton (`T4`): "this was something `[[Christian Vanover|Christian]]` did **on his own** for his stories for the 3DO message board" và "`[[Christian Vanover]]` and `[[Dave Botan]]` (deceased) **made all of the campaign maps**".
Lý do: bốn chỉnh sửa.
(a) Chức vụ chính xác hơn: **assistant director của Heroes III**, không phải "nhân viên" chung.
(b) **"Không thể tiếp cận ở dạng gốc" cần sửa**: bản rehost đương thời **truy cập được** qua archive.org. Không phải bản 3DO gốc, nhưng là **nhân chứng thứ hai độc lập** — và nó khớp thelazy gần như từng chữ (khác biệt duy nhất: bản archive viết `millenium` (sic), thelazy chuẩn hoá thành `millennium`). Nên thêm source key riêng cho bản archive.
(c) "Marcus Finch" là **quy gán của wiki** (thelazy `Lost Lore` xếp bảng theo narrator), truyện chỉ ký "Finch". Là `INFERENCE`, không `EXPLICIT`.
(d) Tier `T2*` đáng xem lại — xem NOTE ở P1-04. Thêm nữa Fulton nói Vanover làm việc đó "on his own", điều làm yếu thẩm quyền canon của truyện chứ không mạnh thêm.

### P2-07
Claim: "The art of Necromancy is a spin-off, really, of Alchemy, which in itself is a spin-off of Wizardry, which is a spin-off of, of all things, Religion."
Nhãn bài gán: `T2* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: thelazy `Deyja`; bản archive The Nether Gods
Tìm thấy ở **cả hai**, khớp từng chữ: "The art of Necromancy is a spin-off, really, of Alchemy, which in itself is a spin-off of Wizardry, which is a spin-off of, of all things, Religion."
Lý do: hai nhân chứng độc lập.

### P2-08
Claim: Trích dài về trục xuất và hút cạn.
Nhãn bài gán: `T2* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: như trên
Tìm thấy: "…it quickly became apparent that in order to restore life in this fashion that **life must be taken from somewhere else**." · "the Necromancers' cult was **exiled from the nation of Bracada** (the southern mountains I mentioned earlier). Wandering the continent, the cult eventually **settled in the AvLee - a region teeming with life**. As time passed, the Necromancers… **slowly drained all the life around them**."
Lý do: khớp từng chữ ở hai nguồn.
NOTE: Fandom Timeline ghi cult định cư ở "**southern** AvLee", trong khi truyện chỉ nói "the AvLee" / "the heart of the AvLee". Chi tiết "southern" là của Fandom, đừng trích như của truyện.

### P2-09
Claim: "Today the nation of Deyja, barren home of the Necromancers for nearly a millennium, continues to grow like a cancerous scar in the heart of the AvLee."
Nhãn bài gán: `T2* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: NOTE
Đã tìm ở: như trên
Tìm thấy — bản archive: "Today the nation of Deyja, barren home of the Necromancers for nearly a **millenium**, continues to grow like a cancerous scar in the heart of the AvLee."
Lý do: khớp. **NOTE:** bản gốc viết sai chính tả `millenium` (một chữ n). thelazy sửa thành `millennium`. Nếu bài trích với hai chữ n mà gắn `EXPLICIT`, nên ghi `[sic]` hoặc nói rõ đang trích qua thelazy.

### P2-10
Claim: "gần một thiên niên kỷ" tính tới thập niên 1160 AS → Deyja hình thành khoảng thập niên 200 AS.
Nhãn bài gán: `T2* INFERENCE` (bài ghi rõ là phép suy từ neo tương đối)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: bản archive; Fandom Timeline dòng 85–87
Tìm thấy: truyện chỉ có neo tương đối "for nearly a millenium" + "Today". Fandom Timeline đặt "Foundation of Deyja" ở **"Unknown AS"** — tức nguồn `T6` lớn nhất **từ chối** định năm.
Lý do: bài xử lý **đúng** — gắn `INFERENCE` và ghi rõ là phép suy. Đây là cách làm mẫu theo `CANON-POLICY.md` mục 4 ("năm tuyệt đối là một thuộc tính có nhãn"). Không có gì phải sửa.

### P2-11
Claim: thelazy diễn đạt lại thành "nearly a millennium **before the 1160s AS**" — đó là phép tính của wiki chồng lên truyện; nên trích truyện.
Nhãn bài gán: (không nhãn)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Deyja&action=raw`, mục `== History ==`
Tìm thấy nguyên văn: "Created by the `[[Necromancer|Necromancers]]` after they were expelled from `[[Bracada]]` **nearly a millennium before the 1160s AS**."
Lý do: đúng — cụm "before the 1160s AS" **không có trong truyện**, wiki tự thêm. Kỷ luật nguồn của bài ở điểm này chính xác.

### P2-12
Claim: "He is a prime candidate for becoming a puppet; he just doesn't know it yet."
Nhãn bài gán: `T1* EXPLICIT`, key `sod-finneas-vilmar` (Day 1)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Finneas_Vilmar&action=raw`, `=== Timed events ===` Day 1
Tìm thấy: "`[[Finneas|Finneas Vilmar]]` is a young lord who desires power. With such a greedy appetite but a poor head for tactics and political manipulations, he has quickly taken to your direction. **He is a prime candidate for becoming a puppet; he just doesn't know it yet.**"
Lý do: khớp từng chữ, đúng vị trí Day 1.

### P2-13
Claim: "King Gryphonheart, the man who banished us from Erathia, is dead. …gift of death… invade Erathia ourselves."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=A_Gryphon%27s_Heart&action=raw`, trường `| region_text =`
Tìm thấy khớp từng chữ.
Lý do: trích dẫn chính xác, và nó là region text — đúng chỗ BH-1.

### P2-14
Claim: "While resurrecting King Gryphonheart from the dead, former King Vilmar met with an unfortunate accident. King Gryphonheart has taken command of the military… and the throne."
Nhãn bài gán: `T1* EXPLICIT` (epilogue)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=A_Gryphon%27s_Heart&action=raw`, mục `== Epilogue ==`
Tìm thấy khớp từng chữ, kể cả câu tiếp sau mà bài dùng ở P2-18: "However, **our lords watch their new king, searching for a sign of weakness.**"
Lý do: chính xác.

### P2-15
Claim: Catherine — "After killing King Vilmar, he took command of their military and their throne. Now they come to us. They cannot stop the monster they have created."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Safe_Passage&action=raw`, mục `== Prologue ==`
Tìm thấy khớp từng chữ.
Lý do: chính xác. Đây là xác nhận độc lập thứ ba cho cái chết của Finneas (cùng epilogue `A Gryphon's Heart` và Diaries "the lich killed Deathknell").

### P2-16
Claim: Lich King bị Catherine tiêu diệt năm 1168; sau đó Archibald lên ngôi, rồi bị Kastore đảo chính năm 1169.
Nhãn bài gán: `T6 INFERENCE`
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: `web.archive.org/web/20001017212754/…/mm7/story/story.htm`; Fandom Timeline dòng 387–394; thelazy `Archibald`, `Kastore`
Tìm thấy — nguồn chính thức 3DO, Entry 143, **5 August 1168**: "In her victory speech… **Catherine** made much ado about stability… her father 'now lies in the state of natural quietude he deserves'… For as the lich, Gryphonheart, replaced Deathknell, **so have I replaced Gryphonheart**."
Lý do: **nâng được tier rất nhiều, nhưng phải tách hai mốc.**
(a) **1168 + Archibald lên ngôi**: `T2 EXPLICIT` từ nguồn 3DO chính thức, không phải `T6 INFERENCE`. Kèm cảnh báo thelazy chép entry này thành 1167 → `DISPUTED` giữa hai bản chép.
(b) **1169 + Kastore**: **không** có nguồn `EXPLICIT`. Ref `ArchieDeposed` của Fandom trích MM7 nhưng nội dung trích là "Factionism and discord have created an intolerable situation in Deyja, so bad that one side had to leave. Archibald's ""science"" necromancers attacked Clanker's laboratory not for the alchemical treasures, but for the living space." — **không có năm, không có tên Kastore**. Fact "bị phế" thì có (`RolandRescue`: "Archibald Ironfist, **deposed lord of Deyja**"); **năm 1169 là suy luận** từ khung thời gian MM7. Giữ `INFERENCE` cho năm, ghi rõ bước suy luận.
(c) Phải ghi **`Kastore (Terra)`** — có hai Kastore (xem P1-22).

### P2-17
Claim: Bảng kế vị 6 dòng, mỗi dòng một độ chắc riêng.
Nhãn bài gán: mỗi dòng một độ chắc riêng
Phán quyết: **DOWNGRADE**
Mức: **MAJOR**
Đã tìm ở: tổng hợp toàn bộ nguồn ở P1-10 → P1-16, P2-13 → P2-16
Tìm thấy: cấu trúc 6 dòng là **đúng** và cách gán độ chắc theo từng dòng là **đúng phương pháp** (`CANON-POLICY.md` mục 4). Ba việc phải sửa:
(a) Dòng 4 (Lich King bị tiêu diệt) phải ghi rõ **bị liên quân Erathia/Bracada/AvLee + necromancer đào ngũ tiêu diệt**, không phải bị người kế vị giết. Nguồn: thelazy `Antagarich` Trivia + thelazy `Nimbus`.
(b) Dòng 5 phải ghi Archibald **bị phế nhưng còn sống** (MM7: "deposed lord of Deyja… offered aid"), không được để người đọc hiểu là chết — đây là gốc của lỗi P1-16.
(c) Dòng 6 "Kastore — vua cuối cùng được biết" cần thêm điều kiện: thelazy `Kastore` nói hắn cũng là "the ruler of `[[Deyja]]` **and `[[Terra Nova]]`** `{{wh}}`" — phần Terra Nova là HotA. Và phải viết `Kastore (Terra)`.

### P2-18
Claim: Ba dòng game text xác lập cơ chế ám sát.
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Duke_Alarice&action=raw` (region_text), `…title=A_Gryphon%27s_Heart&action=raw` (epilogue), `…title=With_Blinders_On&action=raw` (`| description =`)
Tìm thấy cả ba, khớp từng chữ:
1. "With any luck, **he will suffer an accident in the future**."
2. "however, **our lords watch their new king, searching for a sign of weakness**."
3. "However, **if Sandro loses even just one battle, others will sense weakness in him and destroy all he has worked for**."
Lý do: cả ba đúng, và cả ba đúng loại (`region_text` / `Epilogue` / `| description =` — tất cả là text hiện ra khi chơi). Đây là phần lập luận mạnh nhất của bài.

### P2-19
Claim: Vua Deyja **đồng thời là Guildmaster**; Finneas giữ cả hai; Archibald thắng chức guild bằng **đấu tay đôi với Nimbus**, còn ngai vàng giành riêng.
Nhãn bài gán: `T6 EXPLICIT`, key `fandom-timeline-ancient`
Phán quyết: **DOWNGRADE**
Mức: MINOR (kèm **UPGRADE tier**)
Đã tìm ở: `web.archive.org/…/mm7/story/story.htm`; Fandom `Necromancers' Guild`; Fandom `Finneas Vilmar` infobox; thelazy `Nimbus`
Tìm thấy:
- Nguồn 3DO chính thức: "**The guild leader and king of Deyja, Deathknell**, sought to take the Erathian throne…" và chữ ký cuối "Archibald Ironfist / **Guildmaster of Necromancers** / Rightful King of Enroth".
- Cùng nguồn, về Nimbus: "this little mission is now my mission. **I took it from Nimbus in the guild Challenge of Dominance.** Needless to say, I won."
- Fandom `Necromancers' Guild`: "**Archibald defeated Nimbus in a duel**, taking control of the guild." · "The Necromancers' Guild in Antagarich **ruled the nation of Deyja**, under the control of **guildmaster and king Finneas Vilmar**."
Lý do:
(a) **Tier nâng mạnh**: "vua + guildmaster" là `EXPLICIT` từ nguồn 3DO chính thức (`T2`), không phải `T6`. Tên chính xác của cuộc đấu là "**Challenge of Dominance**", không chỉ "đấu tay đôi" chung.
(b) **Phần khái quát hoá thì SAI**: hai chức vụ **không** luôn trùng. Fandom `Finneas Vilmar` infobox tách rành mạch: `successors = Lich King Gryphonheart (as king) / Archibald Ironfist (as guildmaster)`. Nguồn 3DO cũng tách: "Now Erathia and Deyja have a **new king**…**and** the guild has a **new leader**." Và Archibald ban đầu chỉ nắm guild **Enroth** (thelazy `Nimbus`: "becoming the new leader of the **Enrothian** necromancers"), mãi sau mới nắm cả guild Antagarich + ngai vàng.
→ viết lại: Finneas, Archibald và Kastore giữ cả hai chức; **dưới Lich King Gryphonheart hai chức bị tách** (vua = Gryphonheart, guild = Nimbus rồi Archibald).

### P2-20
Claim: Bảng 5 lãnh chúa (Duke Alarice, Lord Smedth, Mot, Lord Amrothal, Nimbus).
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=Lord_Alarice&action=raw`, `…title=Lord_Smedth&action=raw`, `…title=Mot&action=raw`, `…title=Nimbus&action=raw`, `…title=With_Blinders_On&action=raw`, `…title=Finneas_Vilmar&action=raw`, Fandom `Alarice`
Tìm thấy — mọi chi tiết cụ thể đều **đúng**:
- Alarice: "A lord of the court of `[[Deyja]]` who wishes to stop `[[Sandro]]` and warned `[[AvLee]]` of the threat he posed." + timed event Day 4 của `Finneas Vilmar`: "Reports have confirmed that `[[Duke Alarice]]` **warned nearby `[[AvLee]]` lords** about your powerful standing army."
- Smedth (lich, tranh chỗ cố vấn, bẫy Finneas): `With Blinders On` region_text — "always harassing you in court and **attempting to usurp your position as Finneas Vilmar's closest aid**"; prologue — "He is trying to usurp my position as `[[Finneas]]`' **top advisor**… **the conniving lich**"; epilogue — "**He tricked me into getting imprisoned for assaulting an innocent lord** so that he could rule `[[Deyja]]` by himself."
- Mot: thelazy `Mot` "A `[[Death Knight]]` who **refused to obey** King Gryphonheart's orders to attack `[[Erathia]]`."
- Amrothal: `With Blinders On` Day 1 — "`[[Lord Amrothal]]` has secured his position to the west of you, but is **only accessible through the underground tunnel system**." (khớp từng chữ)
- Nimbus: thelazy `Nimbus` — "In `[[Safe Passage]]`, Nimbus **brought proof to Catherine that it was Lord Haart who poisoned King Gryphonheart**. He and other **renegade** necromancers then joined the allied forces."
Lý do: nội dung đúng hết. Ba chỉnh nhỏ.
(a) **Tier lẫn lộn**: mô tả Alarice/Smedth/Mot/Nimbus lấy từ mục `== Story ==` = văn biên tập viên (`T6`); còn Amrothal và text Smedth lấy từ `region_text`/`Day 1`/`Epilogue` = `T1*` thật. Đừng gán một nhãn `T1* EXPLICIT` cho cả bảng.
(b) **Bảng thiếu người**: `With Blinders On` còn có **`Lord Dufus`** (Death Knight, portrait Vokial) và **`Moandor`** (Death Knight) trong hero list, và cùng timed event gọi họ là "These young upstart **lords**". Họ là lãnh chúa Deyja ngang hàng Amrothal. Bảng "5 lãnh chúa" nên là 7, hoặc phải nói rõ tiêu chí lọc.
(c) Amrothal **không có** hero row riêng — chỉ được nêu tên trong timed event. Ghi rõ điều đó.

### P2-21
Claim: Lich King về Mot — "one of my generals… does not wish to follow my orders… We do, however, need his armies, and I can not allow his disobedience to go unpunished."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Corporeal_Punishment&action=raw`, `=== Timed events ===` Intro part 1 + 2
Tìm thấy khớp từng chữ, và trọn vẹn hơn: "*Commander: It would seem as though **one of my generals, a Death Knight by the name of Mot, does not wish to follow my orders**, and believes that we should not attack Erathia. This is fine, as we do not need him for our plans.*" / "***We do, however, need his armies, and I can not allow his disobedience to go unpunished.** Your task is to find Mot and slay him… Succeed in this task and you shall replace him as my new general.*"
Lý do: chính xác. Câu cuối ("shall replace him as my new general") củng cố P1-15 — thay thế bằng cách giết là cơ chế được thể chế hoá, không chỉ ở cấp vua.

### P2-22
Claim: Giá liên minh Nighon = 100.000 vàng + 20 gỗ ban đầu + 50 gỗ mỗi tuần; giá Eeofol = Eversmoking Ring of Sulfur.
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=To_Build_a_Tunnel&action=raw`, `…title=Kreegan_Alliance&action=raw`
Tìm thấy:
- "`| victory = Accumulate Resources (100000 Gold)`" và "**have agreed to build you an underground tunnel to Erathia for the sum of 100,000 gold**"
- Timed event Day 1 `effect=-20 {{w}} Wood`; Day 7 `freq=7` `effect=-50 {{w}} Wood` + "**Each week a transport cart will arrive to pick up** a small amount of wood needed for the construction project."
- `Kreegan Alliance`: "`| description = Obtain the Eversmoking Ring of Sulfur for the Kreegans to win the scenario`" + "**To prove your sincerity they want you to turn over the Eversmoking Ring of Sulfur.**"
Lý do: cả bốn con số/vật phẩm khớp chính xác. Đọc đúng cả `effect=` — chi tiết dễ bỏ.

### P2-23
Claim: "Subterranean wood is too weak for bracing the tunnel walls and ceilings."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=To_Build_a_Tunnel&action=raw`, timed event Day 1
Tìm thấy khớp từng chữ: "However, gold is not the only material needed for your invasion plans. **Subterranean wood is too weak for bracing the tunnel walls and ceilings**, but there is plenty of strong wood in the forest for you to gather."
Lý do: chính xác.

### P2-24
Claim: "The greedy cave dwellers refuse to supply the raw materials themselves. If I did not need their support, I would lock them up in their own underground dungeons!"
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=To_Build_a_Tunnel&action=raw`, mục `== Prologue ==`
Tìm thấy: "Wood is desperately needed to keep the tunnels from collapsing, and the gold is for paying the workers. **The greedy cave dwellers refuse to supply the raw materials themselves. If I did not need their su**[pport…]"
Lý do: khớp. (Chuỗi bị cắt trong output grep của tôi ở giữa "support", nhưng đầu câu và cấu trúc khớp chính xác.)

### P2-25
Claim: "The Kreegans do not believe your sincerity. To them, Necromancers are weak wraiths feeding off the living, unable to initiate any good plan."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Kreegan_Alliance&action=raw`, trường `| region_text =`
Tìm thấy khớp từng chữ.
Lý do: chính xác, và đúng chỗ (region text).

### P2-26
Claim: "You have been sent to fetch this particular item personally because Finneas doesn't trust anyone else with the task. Kreegan support is essential to the plans of Deyja."
Nhãn bài gán: `T1* EXPLICIT` (Day 1)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Kreegan_Alliance&action=raw`, timed event Day 1
Tìm thấy khớp từng chữ.
Lý do: chính xác. Cách bài dùng nó (bằng chứng Finneas thật sự có quyền với Sandro) là đọc đúng — đây là text ở góc nhìn thứ hai nói về Sandro, không phải Sandro tự nói.

### P2-27
Claim: Lãnh chúa AvLee "didn't trust Alarice, but some of them agreed to help him against Vilmar, hoping that the undead would destroy each other".
Nhãn bài gán: `T6 INFERENCE`, key `fandom-deyja`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: Fandom `Deyja` (**đọc toàn bộ trang**); Fandom `Alarice`
Tìm thấy — trên Fandom **`Alarice`**, không phải `Deyja`: "He then offered that they should stop Vilmar together. **The lords of AvLee didn't trust Alarice, but some of them agreed to help him against Vilmar, hoping that the undead would destroy each other.**"
Lý do: trích dẫn khớp từng chữ, nhưng **mis-citation**: trang Fandom `Deyja` **không chứa** câu này. Sửa key thành `fandom-alarice` (key mới). Nhãn `INFERENCE` là đúng — không có game text nào nói động cơ "hoping the undead would destroy each other"; nó là suy đoán của biên tập viên Fandom.

### P2-28
Claim: Vampire **Falorel** giả dạng thành công một lãnh chúa AvLee cho tới khi Sandro đầu độc hắn.
Nhãn bài gán: `T6 INFERENCE`, key `fandom-deyja`
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: `heroes.thelazy.net/index.php?title=Wrath_of_Sandro&action=raw`; `…title=Lord_Falorel&action=raw`; `…title=Vayarad&action=raw`; Fandom `Falorel`; Fandom `Deyja` (toàn bộ)
Tìm thấy (nguồn ngược, **hai wiki đều nói ngược**):
- thelazy `Vayarad` → `#REDIRECT [[Lord Falorel]]`; và trang đó: "`[[AvLee]]`an `[[Border Lord]]` and neighbor of `[[Lord Fayette]]`. **The real Lord Falorel was killed and then impersonated by the vampire Vayarad** for a considerable time… **Soon after this mission he was poisoned by `[[Sandro]]`.**"
- Fandom `Falorel`: "**Lord Falorel was secretly murdered by a Vampire Lord, `[[Vayarad]]`**, who proceeded to successfully assume the guise of his victim… it transpired that **Sandro was the perpetrator, poisoning Vayarad**."
- Fandom `Falorel` infobox: `race = [[Elf (Enroth)|Elf]] ([[Renegade]])`, `occupation = Border Lord at the AvLee-Deyja border` — Falorel là **elf**, không phải vampire.

Lý do: bài **đảo tên hai nhân vật**. Falorel = nạn nhân (lãnh chúa elf thật của AvLee); Vayarad = vampire giả dạng, bị Sandro đầu độc.
**Nhưng có một nút thắt thật, và bài phải trình bày nó:** game text (bio hero trong `Wrath of Sandro`) **tự viết mơ hồ** đúng theo hướng của bài:
"He investigated the death of `[[Lord Falorel]]`, **the vampire who had successfully impersonated an AvLee lord**... until **you poisoned Falorel** for becoming too powerful."
→ Đây là `DISPUTED` thật: **game text gọi Falorel là vampire; cả hai wiki gọi Vayarad là vampire.** Cùng loại với tiền lệ `Dethmar/Dethard` mà `REGISTRY.md` đã ghi.
**Phải sửa:** đổi nhãn thành `DISPUTED`; nêu **cả hai** phương án; ít nhất phải xuất hiện tên **Vayarad**; sửa source key (`fandom-deyja` không chứa gì về việc này — đúng key là `sod-wrath-of-sandro` + `h3wiki-lord-falorel` + `fandom-falorel`, hai key sau là mới).

### P2-29
Claim: "Before the Restoration Wars, four Antagarich nations have never been united in arms. This changed when the Deyjan renegades, led by Archibald Ironfist, joined the allied forces of Erathia, Bracada and AvLee to overthrow Lich King Gryphonheart."
Nhãn bài gán: `T6 EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=Antagarich&action=raw`, mục `== Trivia ==`
Tìm thấy khớp từng chữ.
Lý do: chính xác, **và tier đúng** — bài gán `T6` cho một câu nằm trong mục Trivia (văn biên tập viên). Đây là chỗ bài gán tier chuẩn, trong khi P2-01 lấy từ cùng trang nhưng gán `T1*`. Sự bất nhất nội bộ đó chính là bằng chứng P2-01 sai tier.

---

# PRIORITY 3

### P3-01
Claim: **Hall of the Pit** — dungeon lối vào; mô tả MM7 gồm "shadowy claws and twisted demonic figures… a woman singing in the distance".
Nhãn bài gán: `T6 EXPLICIT`, key `fandom-deyja`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `…title=Deyja_Moors&action=raw`; `…title=The_Pit&action=raw`; Fandom `Deyja` (toàn bộ)
Tìm thấy — trên **thelazy `Deyja Moors`**: "Hall of the Pit: **The dungeon that serves as the Pit's entrance.** Visitors are greeted by a frightening spectacle of **shadowy claws and twisted demonic figures** that beckons them inside the Hall, and can faintly hear **a woman singing in the distance**. Located in northern Deyja, near the shore of the Deyja-AvLee lake and far to the east of Moulder. Guarded by gargoyles, harpies and the undead."
Xác nhận độc lập: thelazy `The Pit` — "The entrance to the Pit, called the `[[Hall of the Pit]]`, is located in northern Deyja."
Lý do: trích dẫn khớp từng chữ, nhưng **mis-citation**: trang Fandom `Deyja` **không chứa** đoạn này. Key đúng là `h3wiki-deyja-moors`. Tier `T6` thì đúng.

### P3-02
Claim: **Watchtower VI** — "the only one that survived the Restoration Wars".
Nhãn bài gán: `T6 EXPLICIT`, key `fandom-deyja`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `…title=Deyja_Moors&action=raw`; Fandom `Watchtower 6`; Fandom `Deyja` (toàn bộ)
Tìm thấy — trên **thelazy `Deyja Moors`**: "Watchtower VI: Part of a series of watchtowers that once guarded the Deyjan border, and **the only one that survived the `[[Restoration Wars]]`**. Located in the mountains on the southern edge of Deyja. Manned by goblins, necromancers, liches and earth elementals. **Sabotaged by the lords of `[[Harmondale]]` on a mission from `[[Bill Lasker]]` to undermine Deyja's defenses.**"
Lý do: **mis-citation** như P3-01 — Fandom `Deyja` không có; và trang Fandom `Watchtower 6` **cũng không** có mệnh đề "the only one that survived" (nó chỉ ghi vị trí "south-western wastelands of Deyja region"). Câu này **chỉ tồn tại trên thelazy** → key phải là `h3wiki-deyja-moors`.
NOTE: hai wiki lệch nhau về vị trí ("mountains on the southern edge" vs "south-western wastelands") — nếu bài ghi vị trí thì phải chọn nguồn hoặc ghi `DISPUTED`.

### P3-03
Claim: **Moulder** — town trên mặt đất ở tây bắc; **trụ sở hành chính của Necromancers' Guild** cho tới khoảng 1170.
Nhãn bài gán: `T6 EXPLICIT`, key `fandom-timeline-ancient`
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: Fandom Timeline dòng 397–399 và ref `Shadowspire`; **và nguồn gốc mà ref đó trỏ tới**: `web.archive.org/web/20000901045811/www.3do.com/products/pc/mm_destroyer/monsters/skeleton.html`
Tìm thấy:
- Fandom Timeline: "Shadowspire replaces **Moulder** as the Necromantic Order's headquarters.`<ref name="Shadowspire">`[web.archive…mm_destroyer/monsters/skeleton.html *Might and Magic VIII* lore ("Skeleton")]`</ref>`"
- **Nguồn gốc (website chính thức 3DO, MM8), toàn văn đoạn liên quan:** "Many sorcerers are drawn to the easy power offered by the dark arts of necromancy. **Since the Necromancers Guild relocated its headquarters to the Shadowspire region of Jadame**, Skeletons and other undead creatures animated by these foul magicians have become all too common there and elsewhere."

Lý do: **nguồn được Fandom dẫn KHÔNG nhắc Moulder một lần nào.** Nó chỉ nói guild dời HQ **tới** Shadowspire. Chữ "Moulder" là **Fandom tự thêm**, không có chống lưng — và archive.org vào được nên điều này kiểm được ngay, không phải phỏng đoán.
Hệ quả nghiêm trọng: đây là **trụ đỡ duy nhất** cho cách giải Tranh chấp 1 ở P1-01. Trụ này sụp. Càng nặng hơn vì thelazy nói **ngược**: "**The Pit is the true heart of the Necromancer's Guild in Antagarich.**"
**Phải sửa:** bỏ "Moulder là trụ sở Guild" khỏi thân bài (hoặc hạ xuống `FAN_THEORY` trong mục riêng, ghi rõ nguồn gốc không chống lưng); giữ lại phần có nguồn thật: Moulder là một town ở tây bắc Deyja, xuất hiện trong MM7 (`h3wiki-deyja-moors`), và Guild dời HQ sang Shadowspire (nguồn 3DO chính thức, key mới).

### P3-04
Claim: **Caverns of the Dead** — gần đất của Mot.
Nhãn bài gán: `T1* EXPLICIT`, key `roe-corporeal-punishment`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=Corporeal_Punishment&action=raw` (toàn bộ: `region_text`, Prologue, Timed events, Rumors, Objects); `…title=Deyja_minor_locations&action=raw`
Tìm thấy:
- Game text duy nhất, trong mục `=== Rumors ===`: "The whirlpool is the gateway to the `[[Caverns of the Dead]]`, but the `[[Collar of Conjuring]]` is the Key."
- Mệnh đề "gần đất của Mot" chỉ có trên thelazy `Deyja minor locations`: "Caverns of the Dead - **Located near the lands of the rogue `[[Death Knight]]`, `[[Mot]]`**."
Lý do: game text **không nói** Caverns ở gần đất Mot — nó chỉ nói cách vào. Mệnh đề vị trí là suy luận của biên tập viên wiki từ việc Caverns nằm trên map của scenario Mot. → `T1* EXPLICIT` sai; phải là `T1* INFERENCE` (nếu tự suy từ việc nó ở trên map đó, ghi bước suy luận) hoặc `T6 EXPLICIT` (nếu trích wiki). Thêm key `h3wiki-deyja-minor-locations`.

### P3-05
Claim: **Blagden** — tây bắc Deyja, nơi Gem và Gelu gặp Yog và Crag Hack. ⚠️ **Fandom viết "Bragden"** — chính tả tranh chấp.
Nhãn bài gán: `T1* EXPLICIT`, key `sod-finneas-vilmar`
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: `…title=Finneas_Vilmar&action=raw` (toàn bộ); `api.php?action=query&list=backlinks&bltitle=Blagden` và `…bltitle=Bragden`; `…title=Secrets_Revealed&action=raw`; `…title=Agents_of_Vengeance&action=raw`; `…title=The_Shadow_of_Death&action=raw`; `…title=Blagden&action=raw`; `…title=Bragden&action=raw`
Tìm thấy (nguồn ngược):
1. **Chữ "Blagden" KHÔNG xuất hiện trong `sod-finneas-vilmar`.** Tôi đọc hết trang (9.499 byte): prologue, 3 timed event, 5 event, towns, heroes, seer's huts, ocean bottle. Không có. → `T1* EXPLICIT` trỏ vào chỗ trống, đúng loại lỗi `REGISTRY.md` đã ghi ba lần với trang artifact.
2. `backlinks` cho biết nguồn game text thật:
   - `Agents_of_Vengeance`: "…but afterwards I'll ask `[[Yog]]` and `[[Crag]]` to meet `[[Gelu]]` and myself at a place called **`[[Blagden]]`**." + map event "To `[[Blagden]]`" tại (35, 71, 0)
   - `Secrets_Revealed`: "A messenger arrived shortly ago informing me that `[[Gem]]` and `[[Gelu]]` want to meet in **`[[Blagden|Bragden]]`**`<!--Error in the story text-->`, which is in the **Northwestern area of `[[Deyja]]`**."
3. **Chính tả lệch nằm TRONG GAME, không phải "Fandom viết khác".** thelazy đánh dấu thẳng bằng HTML comment `<!--Error in the story text-->` — cùng cơ chế `{{sic}}` mà `REGISTRY.md` coi là dấu hiệu bản chép trung thực. Và thelazy có **cả hai** trang `Blagden` và `Bragden`, cả hai `#REDIRECT [[Deyja minor locations]]`; chính trang thelazy `The Shadow of Death` cũng dùng "**Bragden**": "They arrange to meet at the plains of `[[Bragden]]`."
Lý do: source key sai, và **mô tả bản chất tranh chấp sai** — biến một lỗi text nội tại của H3 thành "Fandom viết khác".
**Phải sửa:** key → `sod-agents-of-vengeance` (Blagden) + `sod-secrets-revealed` (Bragden, kèm ghi chú lỗi text); nói rõ hai cách viết cùng xuất hiện trong game text SoD và cả trên thelazy. Cả hai key này **đã có trong `REGISTRY.md`** — bài có sẵn nguồn đúng mà dùng nguồn sai.

### P3-06
Claim: "The Lich itself is not evil - it is merely the attempt of a mage to keep himself alive after his death by trading his life for his own resurrection… but must continue to feed on life to survive."
Nhãn bài gán: `T2* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: thelazy `Deyja`; bản archive The Nether Gods
Tìm thấy ở cả hai, khớp từng chữ: "**The Lich itself is not evil** - it is merely the attempt of a mage to keep himself alive after his death by ***trading*** his life for his own resurrection. Far more sentient than the animated Zombies or Skeletons, the Lich retains the abilities of its previous form, but **must continue to feed on life to survive**."
Lý do: hai nhân chứng độc lập. Lưu ý bản gốc **nhấn mạnh** chữ *trading* (thelazy bằng `'''bold'''`, bản archive bằng `*trading*`) — bài giữ được sắc thái đó là đúng.

### P3-07
Claim: Mục tiêu của necromancy là hồi sinh hoàn hảo; lichdom là mức xấp xỉ gần nhất, được khung là một **cuộc trao đổi**, không phải điều ác.
Nhãn bài gán: (không nhãn riêng)
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: như P3-06
Tìm thấy: "the Necromancers sought **the complete and total resurrection of the dead**" · "the Necromancers, **trying to reach their goal of a perfect resurrection**" · "**The closest the Necromancers have come to a resurrection is the creation of the Lich.**"
Lý do: cả ba mệnh đề có nguồn nguyên văn. Cách đọc "trao đổi, không phải điều ác" là đúng ý văn bản và có chữ *trading* + "not evil" chống lưng.

### P3-08
Claim: Trong MM7, Path of Darkness là alignment đầy đủ: chọn phe này khiến nhóm thành "close allies to the Necromancers of Deyja and permanently hostile to the Wizards of Bracada".
Nhãn bài gán: (không nhãn riêng), key `fandom-path-of-darkness`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `mightandmagic.fandom.com/api.php?action=parse&page=Path%20of%20Darkness&prop=wikitext`
Tìm thấy khớp từng chữ: "After choosing `[[Sleen|Devon Sleen]]` over `[[Fairweather|Brandis Fairweather]]` to replace `[[Grey|Judge Grey]]`, the party become **close allies to the Necromancers of `[[Deyja]]` and permanently hostile to the Wizards of `[[Bracada]]`**."
Lý do: trích dẫn chính xác **và source key đúng** — đây là claim duy nhất trong nhóm P3 dẫn `fandom-path-of-darkness` mà nội dung thật sự nằm ở đó. Bảng quest trên cùng trang cũng chống lưng cho "alignment đầy đủ": 7 quest promotion + 7 main quest đều đặt ở `Deyja`/`The Pit`.

### P3-09
Claim: "For the necromancers, this is a season of harvest. This is a season for war."
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: —
Đã tìm ở: `…title=A_Gryphon%27s_Heart&action=raw`, mục `== Prologue ==`
Tìm thấy khớp từng chữ: "`[[Erathia]]` is strewn with the dead. **For the `[[necromancer]]`s, this is a season of harvest. This is a season for war.**"
Lý do: chính xác.

### P3-10
Claim: `Season of Harvest` đặt chỉ tiêu 2500 skeleton trong ba tháng, thu hoạch từ **dân thường Erathia** dọc biên giới, cố ý "without attracting much notice".
Nhãn bài gán: `T1* EXPLICIT`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `…title=Season_of_Harvest&action=raw`; `…title=Long_Live_the_King&action=raw`
Tìm thấy:
- "`| description = To win, you must have a total of **2500 Skeletons** in all your armies **within 3 months**.`" · "`| victory = Accumulate Creatures (2500 Skeletons)`"
- Prologue: "found a perfect area along Erathia's border from which we can **harvest enough creatures** for our armies **without attracting much notice from the Erathian Military**"
- Timed events: "we must attack **within three months**… you must provide us with **at least 2500 skeletons**" · "you have but **two weeks** until we launch our attack"
Lý do: con số, thời hạn và câu "without attracting much notice" đều khớp chính xác.
**MINOR:** game text nói "harvest enough **creatures**" và "harvest the **creatures** along the Erathian border" — **không** nói "dân thường/civilians". Trong H3 đó là các stack monster trung lập. "Dân thường Erathia" là đọc thêm; hoặc sửa thành "creatures", hoặc gắn `INFERENCE` với bước suy luận.

### P3-11
Claim: **William Setag** là một **paladin** — "a paladin on the Path of Darkness… considered by some to be the most black-hearted villain alive"; tên hắn là "Gates" viết ngược.
Nhãn bài gán: `T6 EXPLICIT`, key `fandom-deyja`
Phán quyết: **CONFIRMED**
Mức: MINOR
Đã tìm ở: `…title=Deyja_Moors&action=raw`; Fandom `William Setag`; Fandom `Deyja` (toàn bộ)
Tìm thấy — trên **thelazy `Deyja Moors`**: "William Setag's Tower: Home of William Setag, **a paladin on the Path of Darkness**. Highly respected in Deyja, Setag is **considered by some to be the most black-hearted villain alive**, a title he proudly wears. He is also one of the kingdom's best agents, often scheming against `[[Bracada]]`." + Trivia: "**William Setag is named after Bill Gates, his last name being "Gates" spelled backwards.**"
Xác nhận độc lập (Fandom `William Setag`): "He is considered to be "**the most black hearted villain alive**", and can promote `[[Crusader (MM7)|Crusaders]]` in the party to `[[Villain (MM7)|Villains]]`." + Trivia: "His last name is '**Gates**' reversed, making a developer inside joke about Bill (William) Gates."
Lý do: nội dung đúng, có hai nguồn. **MINOR — mis-citation**: cả hai đoạn trích nằm trên thelazy `Deyja Moors` và Fandom `William Setag`, **không** trên Fandom `Deyja`. Sửa key.
NOTE hay: từ "paladin" được cơ chế MM7 chống lưng độc lập — Setag promote **Crusader → Villain**, tức hắn nằm trên nhánh Paladin (Paladin → Crusader → Hero/Villain).

### P3-12
Claim: Bảng 6 dòng xuất hiện (RoE / SoD / AB / MM7 / MM8 / Heroes IV).
Nhãn bài gán: `T1* EXPLICIT`, key `h3wiki-deyja` + `fandom-deyja`
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: `…title=Long_Live_the_King&action=raw`; `…title=Deyja&action=raw`; `…title=Deyja_Moors&action=raw`; Fandom `Deyja`; Fandom `Path of Darkness`; `web.archive.org/…/mm_destroyer/monsters/skeleton.html`; `…title=The_Reckoning&action=raw`
Tìm thấy — kiểm từng dòng:
- **RoE**: ✅ `Long Live the King` là "`{{gl|Necropolis}}` campaign", **đúng 4 map**: `A Gryphon's Heart`, `Season of Harvest`, `Corporeal Punishment`, `From Day to Night`. Phản diện trong `Song for the Father` ✅ (`Safe Passage` là scenario #1 của `sftf`, `cback = roe sftf 1`).
- **SoD**: ✅ `Rise of the Necromancer` (`cback = sod rotn 1..4`), `Specter of Power` (`cback = sod sop 4`), `Unholy Alliance`.
- **AB**: ✅ (`ab-march-of-the-undead` đã có trong registry).
- **MM7**: ✅ và mạnh hơn bài ghi — The Pit và Deyja Moors khám phá được, Path of Darkness là alignment (14 quest), Archibald + Kastore cư trú (Fandom `The Pit` map guide điểm 20–24 liệt kê Castle Gloaming, Maximus, Dark Shade, Tolberti, Kastore).
- **MM8**: ⚠️ **thiếu nguồn cho "Deyja được nhắc"**. Nguồn 3DO chính thức chỉ nói guild dời HQ **tới Shadowspire ở Jadame** — **không nhắc Deyja**. Fandom `Necromancers' Guild` có "due to the guild's diminished status on Enroth **and Antagarich**" — vẫn không phải chữ "Deyja". Fandom `Deyja` chỉ nói Sandro/Thant "moved to Jadame".
- **Heroes IV**: ⚠️ như P1-25 — không nguồn nào nói riêng "Deyja bị hủy"; nguồn nói **cả hành tinh Enroth** bị hủy (10/FEB/1177 AS). Là `INFERENCE`.
Lý do: 4/6 dòng chắc; hai dòng cuối phải hạ xuống `INFERENCE` hoặc bổ sung nguồn. Ngoài ra bảng phải ghi **`Kastore (Terra)`** (P1-22).

### P3-13
Claim: Q4 — "**Deathknell** có phải tên khác của Finneas?" Được cho là xuất hiện trong *The Diaries of Archibald* (manual MM7), **chưa xác minh từ nguồn gốc**.
Nhãn bài gán: `T6 UNVERIFIED` (trong mục *Câu hỏi mở* — vị trí này **hợp lệ** theo mục 5.3, tôi không báo lỗi vị trí)
Phán quyết: **CONFIRMED** — và câu hỏi mở này **đóng được**
Mức: **MAJOR**
Đã tìm ở: `web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm` (**website chính thức 3DO**); `heroes.thelazy.net/index.php?title=Archibald&action=raw` (mục `=== The Diaries of Archibald ===`, tự ghi "*The following is from the `{{mm7}}` manual.*"); Fandom `Finneas Vilmar`
Tìm thấy — nguồn chính thức 3DO, Entry 37, nguyên văn:
"The Erathian guild has made a bold and perhaps foolhardy play for power. **The guild leader and king of Deyja, Deathknell**, sought to take the Erathian throne by assassinating Gryphonheart and then reanimating him as a lich, bound to his service. Well, he got as far as the reanimation, but the binding did not take. **Instead, the lich killed Deathknell.** Now Erathia and Deyja have a new king…and the guild has a new leader."
Và Entry 143: "For as the lich, Gryphonheart, **replaced Deathknell**, so have I replaced Gryphonheart."
Xác nhận độc lập: Fandom `Finneas Vilmar` mở đầu — "As the King of `[[Deyja]]` during the `[[Restoration Wars]]`, '''Finneas Vilmar''' — **also known as '''Deathknell'''** — plays the role of an antagonist…"; thelazy `Finneas`: "In `[[Archibald#The Diaries of Archibald|The Diaries of Archibald]]` from the `{{mm7}}` manual, Finneas is referred to as '''Deathknell'''."
Lý do: **định danh chắc chắn.** "The guild leader and king of Deyja" bị "the lich" giết ngay sau nghi thức hồi sinh = đúng và chỉ có thể là Finneas Vilmar, khớp từng chi tiết với `roe-a-gryphons-heart` ("former King Vilmar met with an unfortunate accident") và `roe-safe-passage` ("After killing King Vilmar").
Đây là **MAJOR** vì đúng loại sai lầm nặng nhất trong lịch sử dự án: để một câu hỏi ở `UNVERIFIED` trong khi câu trả lời nằm ngay trên nguồn chính thức truy cập được. Nhãn phải thành `T2 EXPLICIT` (nguồn 3DO) và claim phải **chuyển từ *Câu hỏi mở* lên thân bài**.

### P3-14
Claim: Bài tự thống kê 15 nguồn `T1*`, 1 nguồn `T2*`, 5 nguồn `T6`.
Nhãn bài gán: (bảng thống kê)
Phán quyết: **DOWNGRADE**
Mức: MINOR
Đã tìm ở: toàn bộ báo cáo này
Lý do: bảng thống kê **sẽ sai sau khi sửa**. Tổng kết thay đổi tier bắt buộc:
- **Thêm `T4`**: `fulton-names-2023` (từ nguyên Deyja + cơ chế đặt tên thủ đô) — dự án đã có key này trong registry nhưng bài chưa dùng.
- **Thêm 3 nguồn chính thức 3DO** (mới, xem mục source key bên dưới) — cao hơn `T6` mà bài đang dựa vào cho Diaries, Necromancy origin và Shadowspire.
- **Hạ 6 claim từ `T1*` xuống `T6`** (P2-01, P2-02, P2-03, P2-04, P1-17, một phần P2-20): văn biên tập viên thelazy bị gán là in-game text.
- **Nâng 4 claim từ `T6` lên `T2`** (P1-19, P2-16a, P2-19, P3-13).
Đếm lại sau khi sửa.

---

## Kết luận

### Chưa đủ điều kiện `status: verified`

Còn **1 BLOCKER** và **13 MAJOR**. Điều kiện là không còn BLOCKER **và** không còn MAJOR.

Nói cho công bằng: đây là bài chất lượng cao nhất tôi kiểm. **42/68 claim CONFIRMED, và toàn bộ khối
trích dẫn game text (P2-12 → P2-26, P3-09, P3-10, P1-10 → P1-12, P1-21) khớp nguyên văn 100 %** — kể
cả những chỗ khó như trường `effect=` của timed event và việc phân biệt `region_text` với prologue.
Bài áp dụng BH-1 đúng và phát hiện region text về hai vị vua là thật. Vấn đề không nằm ở việc đọc
game text, mà nằm ở **hai chỗ**: (a) đánh giá độ tin cậy của nguồn `T6`/archive, và (b) kỷ luật
source key — nhiều claim trỏ vào trang không chứa nội dung đó.

### BLOCKER — phải sửa

1. **P1-20** — `Deyja Moors` bị dán nhãn `T6 FAN_THEORY` "không phải canon Old Universe", trong khi
   đó là **tên vùng trong game MM7** (xuất hiện trong ba chuỗi tên quest MM7), và changelog HotA —
   nguồn mà BH-3 bắt buộc dùng — **không nhắc `Deyja`, `Antagarich`, `Moors`, `Badlands` một lần
   nào**. Chỉ `Deyja Badlands` mới là của HotA. Kèm vi phạm mục 5.5 (`FAN_THEORY` nằm trong thân bài).

### MAJOR — phải sửa

2. **P1-01** — cách giải Tranh chấp 1 không có nguồn, và khung "ba chọi một" sai: Fandom `Moulder` là
   **redirect tới `The Pit`**, và trang `The Pit` của Fandom cũng ghi The Pit là thủ đô.
3. **P1-05** — `web.archive.org` **không bị chặn** (HTTP 200), và chỉ **13/46** ref của Fandom Timeline
   là archive link, không phải "phần lớn". Cả Tranh chấp 3 phải viết lại.
4. **P1-07** — mốc 1168/1169 **không** truy được về "text MM7 trích thẳng trong bài": chúng dựa vào
   ref archive `MM7-Archie`. Bài đánh giá độ tin cậy nguồn ngược.
5. **P1-16** — "Bốn cuộc kế vị. Bốn vụ giết." sai: chỉ **một** cuộc kế vị được text mô tả là giết;
   Nicolas bị liên quân tiêu diệt, Archibald bị **phế mà vẫn sống** ("deposed lord of Deyja… offered aid").
6. **P1-19** — năm phải là **1167** (nguồn 3DO), không 1166 (thelazy chép sai); và nhãn nâng từ
   `T6 INFERENCE` lên `T2 EXPLICIT`.
7. **P1-23** — có nguồn `T4` của Lead Designer cho từ nguyên; "chết" phải là "**to die**"; "tiếng
   Iceland" vẫn chỉ `T6`.
8. **P1-25** — `UNVERIFIED` nằm trong mục *Lịch sử* = vi phạm mục 5.3; và claim giải được ngay qua
   `The Reckoning` (Enroth bị hủy 10/FEB/1177 AS).
9. **P2-16** — tách hai mốc: 1168 nâng lên `T2 EXPLICIT`; 1169 + Kastore giữ `INFERENCE` (ref
   `ArchieDeposed` không chứa năm cũng không chứa tên Kastore).
10. **P2-17** — bảng kế vị phải sửa dòng 4, 5, 6 theo P1-16; phải viết `Kastore (Terra)`.
11. **P2-28** — **đảo tên nhân vật**: vampire giả dạng là **Vayarad**, Falorel là nạn nhân elf. Nhưng
    game text tự viết mơ hồ ("Lord Falorel, the vampire") → phải thành `DISPUTED` và nêu cả hai tên.
12. **P3-03** — "Moulder là trụ sở Guild": nguồn gốc mà Fandom dẫn (website 3DO MM8) **không nhắc
    Moulder**, chỉ nói dời HQ tới Shadowspire. Đây là trụ đỡ duy nhất của P1-01 và nó không có thật.
13. **P3-05** — `T1* EXPLICIT` trỏ vào trang **không chứa** chữ "Blagden"; và lệch chính tả nằm
    **trong game text SoD** (`Secrets Revealed` viết "Bragden", thelazy đánh dấu
    `<!--Error in the story text-->`), không phải "Fandom viết khác".
14. **P3-13** — *Deathknell = Finneas* xác minh được từ website chính thức 3DO. Phải rời *Câu hỏi mở*,
    lên thân bài với nhãn `T2 EXPLICIT`.

### MINOR đáng làm cùng lúc

- **Mis-citation hàng loạt sang `fandom-deyja`**: P3-01, P3-02, P3-11 (và P2-27, P2-28) dẫn
  `fandom-deyja` cho nội dung **không có** trên trang đó. Tôi đọc toàn bộ trang Fandom `Deyja`
  (5.955 byte) — nó không có Hall of the Pit, Watchtower VI, William Setag, Falorel, Bragden. Đúng
  loại lỗi `REGISTRY.md` đã ghi ba lần với trang artifact: nhãn `EXPLICIT` trỏ vào chỗ trống.
- **Mis-tier hàng loạt `T1*` → `T6`**: P2-01, P2-02, P2-03, P2-04, P1-17, phần `== Story ==` của P2-20.
  Cách tự kiểm: nếu câu nằm ngoài mọi template `{{...}}` và ngoài `region_text`/`| description =`/
  Prologue/Epilogue/Timed events/Events, thì đó là văn biên tập viên. Bằng chứng bài **biết** quy tắc
  này: P2-29 lấy từ cùng trang `Antagarich` và được gán `T6` đúng.
- P1-02, P1-24, P3-10: hạ `EXPLICIT` → `INFERENCE` (Moulder "trên mặt đất"; "không được lập ra";
  "dân thường" thay vì "creatures").
- P1-22: đóng câu hỏi mở — **không có trang disambiguation trên cả hai wiki** (đã kiểm bằng
  `list=allpages&apprefix=Deyja`). Nhưng thay vào đó phải thêm cảnh báo **có HAI Kastore**.
- P2-20: bảng lãnh chúa thiếu **Lord Dufus** và **Moandor**; Amrothal không có hero row.
- P1-15: nêu **Necromancers' Guild / Necromantic Order** là thể chế tập thể được chứng thực.
- P2-06: Vanover là **assistant director của Heroes III**; truyện **tiếp cận được** qua archive.

### Source key mới cần thêm vào `REGISTRY.md`

| key đề xuất | tier | access | Nội dung |
|---|---|---|---|
| `3do-mm7-diaries-archibald` | **T2** | FETCHED | ⭐⭐ **Website chính thức 3DO**, *The Diaries of Archibald*, qua `web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`. Ba entry đầy đủ: **11 June 1165 / 23 October 1167 / 5 August 1168**. Chốt: Deathknell = Finneas; "the guild leader and king of Deyja"; Challenge of Dominance; Archibald thay Gryphonheart. ⚠️ **thelazy `Archibald` chép SAI năm Entry 37 (1166) và Entry 143 (1167)** |
| `3do-mm8-skeleton-lore` | **T2** | FETCHED | Website chính thức 3DO, MM8 *Skeletons*, `web.archive.org/web/20000901045811/www.3do.com/products/pc/mm_destroyer/monsters/skeleton.html`. ⚠️ **Phản bác** claim của Fandom rằng Shadowspire thay **Moulder** — nguồn chỉ nói "relocated its headquarters to the Shadowspire region of Jadame", **không nhắc Moulder** |
| `nethergods-necromancy-origin` | T2*/T4 | FETCHED | Bản rehost đương thời của truyện *Necromancy Origin* trên site The Nether Gods (bản quyền 1998–2000), chụp 19/FEB/2001: `web.archive.org/web/20010219115822/homm3.ga-strategy.com/necromancy.htm`. **Nhân chứng thứ hai độc lập** cho `t2-necromancy-origin`; khớp thelazy gần từng chữ (bản gốc sai chính tả `millenium`, ký chỉ "-Finch") |
| `h3wiki-deyja-minor-locations` | T6 | FETCHED | `Deyja minor locations` — Blagden, Caverns of the Dead. Là **văn biên tập viên**, `T6`. Cả `Blagden` và `Bragden` redirect về đây |
| `h3wiki-deyja-badlands` | T6 | FETCHED | `Deyja Badlands` — vùng nam Deyja; tự ghi tên đến từ bản đồ campaign HotA. ⚠️ **Changelog HotA không xác nhận** |
| `h3wiki-lord-falorel` | T6 | FETCHED | `Lord Falorel` (thelazy; `Vayarad` redirect về đây) — Falorel = lãnh chúa elf AvLee bị giết, **Vayarad** = vampire giả dạng. ⚠️ **Ngược với bio hero trong `sod-wrath-of-sandro`** |
| `fandom-falorel` | T6 | FETCHED | Fandom `Falorel` — cùng kết luận với trên; cũng là nơi chứng thực "**Council of Elders**" của AvLee (dùng cho P1-15) |
| `fandom-alarice` | T6 | FETCHED | Fandom `Alarice` — nguồn thật của câu "The lords of AvLee didn't trust Alarice…"; và ghi rõ Alarice dùng icon Vokial ở scenario này, icon Nimbus ở scenario kia |
| `fandom-necromancers-guild` | T6 | FETCHED | Fandom `Necromancers' Guild` — "ruled the nation of Deyja, under the control of guildmaster and king Finneas Vilmar"; Castle Darkmoor (MM6); "defeated Nimbus in a duel"; Kastore "drove him out" |
| `fandom-william-setag` | T6 | FETCHED | Fandom `William Setag` — xác nhận độc lập "most black hearted villain alive" + trò chơi chữ Bill Gates; promote Crusader → Villain |
| `h3wiki-lost-lore` | T6 | FETCHED | thelazy `Lost Lore` — bảng phân loại toàn bộ truyện Vanover/Bullard. Vanover = **assistant director** H3; các truyện "**never incorporated in the game itself**"; "never contradicting canon (except for one of them)" |
| `sod-secrets-revealed` | T1* | FETCHED | (đã có trong registry) — chứa "**Bragden**" + `<!--Error in the story text-->` + "Northwestern area of Deyja" |
| `h3wiki-the-reckoning` | T1*/T6 | FETCHED | thelazy `The Reckoning` — "rendered the planet of Enroth uninhabitable", **10 February 1177 AS**. Dùng để nâng P1-25 khỏi `UNVERIFIED` |

### Sửa `REGISTRY.md` — hai cảnh báo đang sai

1. **`web.archive.org` — FAILED (bị chặn hoàn toàn)** → phải thành **FETCHED**. Kiểm 2026-08-03, ba
   URL độc lập đều HTTP 200. Hệ quả lan rộng: dòng "Nên không lấy được bản lưu của site chính thức"
   không còn đúng, và mục "⚠️⚠️ `fandom-timeline-ancient` — phần lớn `<ref>` KHÔNG xác minh được"
   phải viết lại (13/46 là archive, và cả 13 đều xác minh được).
2. Thêm cảnh báo mới: **thelazy `Archibald#The Diaries of Archibald` chép sai hai con số năm** so với
   website chính thức 3DO. Đây là ca đầu tiên dự án bắt được thelazy sai và Fandom đúng — nó làm yếu
   giả định nền "thelazy là bản chép trung thực", nên đáng ghi cạnh mục `T1*`.

### Chỗ bảng claim mô tả sai (lỗi bảng claim, không phải lỗi bài)

1. **"Bảng có 63 claim"** — thực tế **68 dòng** (P1: 25, P2: 29, P3: 14).
2. **P1-22, "thelazy trả về rỗng"** — không đúng: `list=search&srsearch=Deyja` trả 4 kết quả bình
   thường. Chỉ `insource:` mới rỗng, và mẹo kỹ thuật ở cuối bảng đã nói đúng điều đó — hai chỗ trong
   cùng một file tự chỏi nhau.
3. **P1-20 mô tả "Deyja Moors và Deyja Badlands… đến từ bản đồ campaign HotA"** — gộp hai thứ khác
   nhau; nguồn thelazy tách rành mạch bằng chữ "**also**".
4. **P1-05 mô tả "archive.org bị chặn"** và **"Mẹo kỹ thuật: `web.archive.org` bị chặn hoàn toàn
   trong môi trường này"** — cả hai sai ở thời điểm kiểm.
5. **P2-05 gán `fandom-path-of-darkness`**, **P3-01/P3-02/P3-11 gán `fandom-deyja`** — bảng chép lại
   source key sai của bài; tôi báo là lỗi bài (mis-citation), nhưng bảng cũng không bắt được.
6. **Tên trang thelazy trong ngoặc**: `sod-finneas-vilmar` ứng với `Finneas_Vilmar`, **không** phải
   `Finneas_Vilmar_(scenario)` (dạng đó trả **404** trên thelazy; nó chỉ đúng trên Fandom). Cùng loại
   bẫy với `Horn of the Abyss (Changelog)` mà mẹo kỹ thuật đã ghi.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. BLOCKER và toàn bộ MAJOR đã xử lý.

### Ba phát hiện cấp dự án — người sửa TỰ DỰNG LẠI trước khi tin

Ba phát hiện này đảo ngược các giả định đã dùng trong cả registry, nên không thể áp theo lời verifier.
Kết quả kiểm độc lập:

| Phát hiện | Kết quả tự kiểm | Kết luận |
|---|---|---|
| `web.archive.org` **không** bị chặn | Fetch được **151.258 byte** nội dung thật; HTTP **302** cần `-L`; API `wayback/available` trả **429** (rate limit) | ✅ **XÁC NHẬN** |
| Nguồn chính thức 3DO tiếp cận được, chốt `Deathknell` | Fetch `web/20001017212754/…/mm7/story/story.htm` → `Deathknell` xuất hiện **3 lần**, trích được nguyên văn Entry 37 | ✅ **XÁC NHẬN** |
| thelazy chép **sai hai con số năm** | 3DO: Entry 1 = 1165, Entry 37 = **1167**, Entry 143 = **1168**. thelazy: 1165 ✅, **1166** ❌, **1167** ❌ | ✅ **XÁC NHẬN** |
| Fandom `Moulder` là **redirect** tới `The Pit` | `api.php?…&titles=Moulder&redirects` → `redirects: [{"from":"Moulder","to":"The Pit"}]` | ✅ **XÁC NHẬN** |

⚠️ **Một lần thử thất bại, ghi lại để lần sau khỏi lặp:** URL dạng `web/2005/http://...` trả về **trang
wrapper 1.941 byte không có nội dung**. Phải dùng **timestamp đầy đủ** (`web/YYYYMMDDhhmmss/`). Nếu chỉ
thử dạng ngắn rồi kết luận "không lấy được", sẽ tái lập đúng cái sai mà đợt này vừa sửa.

### Bảng xử lý

| # | Phát hiện | Mức | Cách xử lý |
|---|---|---|---|
| P1-20 | `Deyja Moors` bị dán `FAN_THEORY` "không canon" | **BLOCKER** | Tách bảng hai dòng: **Moors = canon MM7** (có trong chuỗi tên quest MM7), **Badlands = HotA**. Nêu rõ lỗi này đi **ngược mục đích của R5** — R5 để giữ nội dung fan ra ngoài, không phải đẩy canon NWC ra ngoài. Dẫn changelog HotA: `Deyja`/`Moors`/`Badlands` đều **0 lần** |
| P1-16 | "Bốn kế vị, bốn vụ giết" | MAJOR | Lập bảng năm cuộc kế vị với cơ chế thật: **đúng một** vụ giết được text mô tả; hai vụ chỉ có **ý định**; hai vụ cuối là **phế vị và người bị phế sống sót**. Thêm text chứng minh Archibald còn sống |
| P2-28 | Đảo tên Falorel / Vayarad | MAJOR | Đổi thành `DISPUTED` và lập bảng hai phương án: **game text gọi Falorel là vampire; cả hai wiki gọi Vayarad là vampire, Falorel là nạn nhân elf**. Thêm key `h3wiki-lord-falorel`. Cùng loại tiền lệ `Dethmar/Dethard` |
| P1-23 | Từ nguyên chỉ có `T6` | MAJOR | Nâng **`T6` → `T4`** bằng phát ngôn Fulton. Sửa nghĩa thành **"to die"** (động từ). Ghi rõ phần "tiếng Iceland" chỉ Fandom nói |
| P3-13 | `Deathknell` bị để ở *Câu hỏi mở* | MAJOR | **Đóng câu hỏi.** Thêm mục thân bài với hai trích dẫn `T2` từ site 3DO, và giải thích vì sao định danh là chắc chắn |
| P1-01 | Cách giải tranh chấp thủ đô không nguồn | MAJOR | Viết lại: tranh chấp **phần lớn tan** vì `Moulder` là redirect → **bốn nguồn, không nguồn nào chọi**. Nhưng nêu rõ trụ đỡ "Moulder là HQ Guild" **chỉ có một dòng `T6`** — 3DO và Fulton đều **0 lần** nhắc Moulder. Thêm `Q3b` |
| P1-05, P1-07 | "archive.org bị chặn", đánh giá nguồn ngược | MAJOR | Viết lại cả mục. Nêu rõ đây là **claim phủ định về chính công cụ nghiên cứu**, và nó **tự làm dự án nghèo đi**. Sửa cả đánh giá 1168/1169 (chúng **dựa vào** ref archive, không phải "không qua archive") |
| P1-19, P3-03 | Năm 1166 | MAJOR | Sửa thành **1167** theo nguồn 3DO, kèm ghi chú thelazy chép sai |
| P1-25 | `UNVERIFIED` trong **thân bài** | MAJOR | Lần này **đúng là** vi phạm mục 5.3 (khác ba bài trước, nơi nhãn đã ở *Câu hỏi mở*). Chuyển claim Reckoning xuống Q3 |
| P1-22 | Chưa kiểm disambiguation | MINOR | Đã kiểm: **không wiki nào có** trang disambiguation cho Deyja, và thelazy **không** trả rỗng. Ghi lại bẫy BH-2 thật: **có HAI `Kastore`** |

### Sửa `REGISTRY.md` — bốn cảnh báo cấp dự án

1. `web.archive.org`: **FAILED → FETCHED**, kèm hướng dẫn dùng `-L` và timestamp đầy đủ.
2. Cảnh báo mới: **thelazy chép sai hai con số năm** trong *Diaries of Archibald* — ca **đầu tiên**
   thelazy sai và Fandom đúng. Quy tắc rút ra: *"chép trung thực" không đồng nghĩa với "chép đúng"*.
3. Cảnh báo mới: `Moulder` trên Fandom là **redirect** tới `The Pit`.
4. Key mới: `3do-mm7-diaries-archibald` (**T2**, site chính thức 3DO), `h3wiki-lord-falorel`.

### Một phát hiện của verifier KHÔNG được áp

Verifier đề nghị thêm `3do-mm8-skeleton-lore` (T2) và `nethergods-necromancy-origin`. **Chưa áp** vì
người sửa **không tự fetch lại được** hai nguồn đó trong phiên này, và tiêu chuẩn của dự án là không
đưa key vào registry khi chưa tự xác minh. Đã để lại cho đợt sau.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-deyja-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.

---

## 🔴 SỰ CỐ: verifier của báo cáo này BỊA MỘT TRÍCH DẪN (phát hiện 2026-08-03, sau khi commit)

Ghi ở đây thay vì xóa, vì đây là **sự cố của quy trình**, không phải một lỗi biên tập.

### Câu bịa

Ở mục P1-16, báo cáo này đưa ra câu trích sau làm **bằng chứng quyết định** cho việc Archibald sống
sót sau khi bị phế:

> *"Archibald Ironfist, deposed lord of Deyja and one of the most hated men in history, offered aid
> for reasons of his own."*

**Câu này không tồn tại ở bất kỳ nguồn nào.** Đã kiểm lại độc lập:

| Cách kiểm | Kết quả |
|---|---|
| Fandom search `"most hated men"` | **rỗng** |
| Fandom search `"deposed lord of Deyja"` | **rỗng** |
| grep trang `Deyja` (thelazy) cho `most hated` | **0** |
| grep trang `Archibald`, `Kastore` (thelazy) | **0** |
| grep toàn văn wikitext trang `Deyja` (Fandom, 5.934 byte) cho `most hated` / `deposed lord` / `offered aid` | **0 / 0 / 0** |

### Vì sao nó lọt qua người điều phối

**Kết luận mà nó chống lưng thì ĐÚNG.** Archibald thật sự bị phế mà không bị giết — và có nguồn thật
nói vậy, chỉ là bằng chữ khác: thelazy *"Kastore later staged a coup and **ousted** Archibald"*, Fandom
*"**Archibald fled Deyja** along with the necromancers from the Science arm"*.

Một trích dẫn bịa **đi kèm một kết luận đúng** là trường hợp khó bắt nhất: không có gì trong kết luận
gợi ra sự bất thường, và người điều phối đang có lý do để tin nó.

Nó được phát hiện **tình cờ** — đợt research `archibald-ironfist` ngay sau đó đi tìm câu này để dùng
cho bài riêng của Archibald, tìm ở sáu chỗ, và không thấy.

### Đã sửa

Bài `deyja` thay bằng hai câu trích **thật** (`ousted` / `fled Deyja`), và ghi lại sự cố ngay tại chỗ.

### Quy tắc mới — V4

Đã thêm vào `VERIFY-PROTOCOL.md` mục 7: **người điều phối phải tự fetch lại mọi trích dẫn mà verifier
dùng làm bằng chứng quyết định** — không chỉ những trích dẫn nó phản bác. Cụ thể khi câu trích (a) chốt
một `BLOCKER`/`MAJOR`, (b) là nguồn **duy nhất** cho một claim, hoặc (c) được verifier giới thiệu như
**nguồn mới** mà bài chưa có.

Lý do sâu hơn: mục 1 của `VERIFY-PROTOCOL.md` viết rằng "mô hình ngôn ngữ có xu hướng tạo ra chi tiết
nghe hợp lý mà không có nguồn". Điều bản đầu chưa lường: **verifier cũng là mô hình ngôn ngữ**, nên V3
("phải trích được nguyên văn") **không tự bảo vệ được chính nó**.

### Audit hồi tố — áp V4 cho cả sáu bài của đợt này

Sau khi phát hiện, đã fetch lại **mọi trích dẫn quyết định** mà người điều phối đã nhận từ verifier
trong cả đợt 6 bài:

| Trích dẫn / bằng chứng | Bài | Kết quả |
|---|---|---|
| `artraits.txt` — "Worn on the feet…15%" | dead-mans-boots | ✅ có, đúng 1 lần |
| `artraits.txt` — "Worn about the neck…5%" | amulet | ✅ có, đúng 1 lần |
| `artraits.txt` — "Worn about the shoulders…10%" | vampires-cowl | ✅ có, đúng 1 lần |
| `artraits.txt` — "All opponents have these spells…fifty turns" | armor | ✅ có, đúng 1 lần |
| Caption `Information from H3Bitmap.lod > artraits.txt` | (cả bốn) | ✅ có |
| `Template:Swh` — tham số 1 = `onlyhota` | jeddite | ✅ xác nhận |
| Fulton — "obvious play on 'Jedi' from Star Wars" | jeddite | ✅ xác nhận |
| `Jungle Fever` — "Jeddite the Reckless" | jeddite | ✅ xác nhận |
| `Mormolykos` — `spart_6 = Vampire's Cowl` | vampires-cowl | ✅ xác nhận (dòng 29) |
| `Tomb Raiders` — "Mormolykos' Cowl" | vampires-cowl | ✅ xác nhận |
| 3DO — "the lich killed Deathknell" | deyja | ✅ xác nhận |
| 3DO vs thelazy — lệch năm Entry 37/143 | deyja | ✅ xác nhận |
| Fandom `Moulder` là redirect | deyja | ✅ xác nhận |
| **"deposed lord of Deyja… most hated men"** | **deyja** | 🔴 **BỊA** |

**Tỉ lệ: 1 câu bịa trên ~13 trích dẫn quyết định được audit.** Toàn bộ phần còn lại sạch — nghĩa là
luồng verify vẫn đáng dùng, nhưng **không được nhận trích dẫn của nó mà không kiểm**.
