# Verify report: armor-of-the-damned — 2026-08-03

Verifier: agent độc lập, không đọc bài gốc, không đọc `docs/sources/raw/`, không đọc
`cloak-of-the-undead-king` / `sandro` / `ethric` / `jeddite`, không đọc báo cáo khác trong
`docs/sources/notes/`.

Số claim kiểm: 52
CONFIRMED: 36 | DOWNGRADE: 11 | NOT_FOUND: 3 | CONTRADICTED: 2

BLOCKER: 0 | MAJOR: 10 | MINOR: 8 | NOTE: 6

## Nguồn đã fetch trong đợt này

Tất cả qua `heroes.thelazy.net/index.php?title=<Page>&action=raw`:

`Armor of the Damned` (2.400 B) · `Weakness` (1.651 B) · `Orb of Inhibition` (848 B) ·
`Talk:Artifact/descriptions` (16.129 B) · `Bashing Skulls` (7.462 B) · `Black Sheep` (7.493 B) ·
`A Cage in the Hand` (7.571 B) · `Grave Robber` (8.717 B) · `Hack and Slash` (3.569 B) ·
`Unholy Alliance` (9.355 B) · `Wrath of Sandro` (8.474 B) · `Fall of Sandro` (19.242 B) ·
`Target` (17.766 B) · `Trivia` (15.817 B) · `Garrison` (3.343 B) · `Skull Helmet` (800 B) ·
`Rib Cage` (557 B) · `Blackshard of the Dead Knight` (549 B) · `Shield of the Yawning Dead` (642 B) ·
`Shield of the Damned` (728 B) · `Cuthbert` (1.445 B) · `Olema` (1.735 B) · `Mirlanda` (2.136 B) ·
`Eanswythe` (1.330 B) · `Recanter's Cloak` (560 B) · `Cape of Silence` (649 B) · `Terrain` (11.363 B) ·
`Horn of the Abyss (Changelog)` (201.529 B) · `Ethric` (5.525 B) · `Beyond the Horizon` (57.255 B) ·
`Gregory Fulton/On Names in Heroes of Might and Magic III` (98.499 B) ·
`Ironfist of the Ogre` (1.928 B) · `Angelic Alliance` · `The Shadow of Death` (3.974 B) ·
`Combination artifact` (8.056 B).

`Anti-Magic Garrison` và `Cursed Ground` là **redirect** (`Garrison`, `Terrain#Cursed Ground`).

---

## Chi tiết

### C-01
Claim: combination artifact **thứ hai** của Sandro; hắn lừa Crag Hack đi thu thập bằng cách nói sẽ **phá hủy** nó.
Nhãn bài gán: (không nhãn), không source key
Phán quyết: DOWNGRADE
Mức: MINOR
Đã tìm ở: `Bashing Skulls`, `Hack and Slash`, `Grave Robber`, `The Shadow of Death`, `Target`
Tìm thấy: phần "lừa bằng cách nói sẽ phá hủy" chống lưng vững — xem C-05, C-06, C-19.
Phần "**thứ hai**" thì **không** có game text nào xác lập thứ tự. `The Shadow of Death` chỉ nói song song:
"Sandro first convinces the sorceress Gem and barbarian Crag Hack to find the pieces of the two artifacts
for him". `Target` Day 1 liệt kê "You have the Cloak of the Undead King and the Armor of the Damned!" —
là liệt kê, không phải thứ tự thu được. Thứ tự duy nhất tìm được là **thứ tự liệt kê campaign** trên
`The Shadow of Death`: New Beginning → Elixir of Life → **Hack and Slash** → Birth of a Barbarian → …
Lý do: "thứ hai" tối đa là `T1* INFERENCE` (suy từ thứ tự campaign), phải ghi rõ bước suy luận và có
source key. Hiện claim nằm ở *Tóm lược* mà không nhãn, không key — vi phạm `CANON-POLICY.md` mục 5.1.

### C-02
Claim: bộ hoàn chỉnh **không cho thêm một điểm chỉ số nào**; toàn bộ giá trị nằm ở bốn spell **cấp Expert**, miễn phí, đầu trận.
Nhãn bài gán: (không nhãn)
Phán quyết: DOWNGRADE
Mức: MINOR
Đã tìm ở: `Armor of the Damned`, bốn trang thành phần, `Talk:Artifact/descriptions`, `Angelic Alliance`
Tìm thấy: phần chỉ số CONFIRMED tuyệt đối — xem C-27.
Nhưng chữ "**Expert**" **không có** trong chuỗi in-game thật. `Talk:Artifact/descriptions`
(`H3Bitmap.lod > artraits.txt`, tier `T1`) ghi cho Armor of the Damned:
"All opponents have these spells effective on them for fifty turns: Slow, Curse, Weakness, and Misfortune."
Không có chữ "Expert", không có "at the start of combat".
Đối chiếu quyết định: cùng bảng đó, Angelic Alliance **có** ghi "Casts Expert Prayer at the start of
combat." → game **biết** dùng chữ "Expert" khi cần, và với Armor thì nó **không** dùng.
Lý do: "cấp Expert" đến từ trường `effect` của template wiki và từ đoạn `fanopinion`, không từ chuỗi
in-game. Phải hạ xuống `T1* INFERENCE` hoặc dẫn nguồn khác cho mức Expert.

### C-03
Claim: **không game text nào** nêu người tạo ra hay chủ sở hữu gốc. Bài ghi: "kết luận sau khi săn chủ động".
Nhãn bài gán: (không nhãn), không source key
Phán quyết: CONFIRMED
Mức: MINOR
Đã tìm ở: bốn trang scenario Hack and Slash, `Target`, `Wrath of Sandro`, `Fall of Sandro`,
`Beyond the Horizon`, `Ethric`, `Talk:Artifact/descriptions`, `Gregory Fulton/On Names…`,
`Armor of the Damned`, bốn trang thành phần
Tìm thấy: không nguồn nào nêu người tạo hay chủ gốc. Sandro chỉ nói bốn món "taken by some very evil men".
Đáng chú ý — **có một game text đi sát câu hỏi này rồi cố ý bỏ lửng**, và bài nên dẫn nó:
`Beyond the Horizon` (HotA), Seer's Hut (2, 27, 0) đòi **Skull Helmet + Rib Cage** + Amulet + Cowl, lời priest:
"We believe that these lands have been home to cursed artifacts since the last century. Their creator
was… Bah, that doesn't matter. What does, is that these artifacts must be found and destroyed…"
Lý do: claim phủ định đứng vững sau săn độc lập. Nhưng nó **không có source key nào** — một claim phủ
định trong thân bài phải ghi rõ đã săn ở đâu. Đề nghị dẫn `hota-beyond-the-horizon` (đã có trong
registry) làm bằng chứng "game gần nhất chạm tới câu hỏi và cố tình không trả lời". Lưu ý HotA là
fan-made, không phải NWC.

### C-04
Claim: bảng "Sandro nói vs người giữ nói" cho bốn thành phần.
Nhãn bài gán: T1* EXPLICIT — `sod-bashing-skulls + sod-black-sheep + sod-a-cage-in-the-hand + sod-grave-robber`
Phán quyết: DOWNGRADE
Mức: **MAJOR**
Đã tìm ở: `Bashing Skulls`, `Black Sheep`, `A Cage in the Hand`, `Grave Robber`
Tìm thấy: **ba trong bốn dòng CONFIRMED nguyên văn.**

- Skull Helmet — Sandro: "He is a very evil man who has unearthed the first item I seek." ✅
  Barshon (map event 54, 12, 0): "It is a family heirloom handed down from generations." ✅
- Rib Cage — Sandro: "the Necromancers, knowing its importance to my research, burned the Sanctuary
  to the ground and stole the Rib Cage." ✅ Ebon Hand (timed event Day 30): "We know nothing about a
  Sanctuary, Mister Hack…" ✅
- Shield — Sandro: "They took the shield from a vampire slayer who had finally met his match when he
  challenged these Liches." ✅ Hand of Death (Day 15): "the Shield of the Yawning Dead is our relic.
  It has been a part of our graveyard for many years." ✅

**Dòng Blackshard sai người nói.** Sandro nói đúng như bài ghi: "It was stolen from the tomb of a great
hero by a Death Knight named Marzeth." Nhưng phía "thừa kế" **không phải Marzeth nói** — Marzeth
**không có một câu thoại nào** trong toàn bộ `Black Sheep`. Đó là **tin đồn của trinh sát**, timed event
Day 14, và chính game text **tự rào lại**:
"Supposedly Marzeth was a Knight of the Blade who inherited the Blackshard, but the cursed sword twisted
his soul until he became a Death Knight. This would explain why the humans are protecting him, but it
goes against Sandro's story that Marzeth stole the sword from a warrior's tomb. **At best the rumor must
be only half-true.**"
Lý do: cột "người giữ nói" gán sai chủ thể phát ngôn cho 1/4 dòng, và bỏ mất câu rào của chính game.
Phải sửa thành "tin đồn trinh sát Day 14 (game tự ghi 'at best… only half-true')". Nhãn `EXPLICIT` cho
dòng đó không đứng được.

### C-05
Claim: mô tả campaign — Crag Hack được thuê "to find the four pieces of the Armor of the Damned **so he can destroy the cursed thing**".
Nhãn bài gán: T1* EXPLICIT — `sod-bashing-skulls`
Phán quyết: NOT_FOUND (tại nguồn được dẫn)
Mức: **MAJOR**
Đã tìm ở: `Bashing Skulls` (toàn trang, gồm `description`, prologue, Timed events, Events),
sau đó `Hack and Slash`
Tìm thấy: **không có câu đó ở `Bashing Skulls`.** Trường `| description =` của `Bashing Skulls` là:
"Crag Hack must seize the first artifact Sandro requires, the Skull Helmet, from Barshon the Barbarian
to win the scenario…"
Câu bài trích nằm nguyên văn ở trang **campaign** `Hack and Slash`, trường `| description =`:
"Crag Hack, newly arrived in Erathia and looking for adventure, meets a young wizard named Sandro, who
hires him to find the four pieces of the Armor of the Damned so he can destroy the cursed thing. Great
rewards are offered for this service."
Lý do: mis-citation. Nhãn `EXPLICIT` trỏ vào chỗ không có câu đó — đúng loại lỗi mà `REGISTRY.md` đã
cảnh báo ba lần ở cụm Cloak. Cần source key mới cho trang campaign.

### C-06
Claim: giá 500.000 vàng + một mảnh đất phong; trích Day 1 Wingtail Tavern.
Nhãn bài gán: T1* EXPLICIT — `sod-bashing-skulls`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Bashing Skulls`, Timed events Day 1
Tìm thấy: "Not only will I give you five hundred thousand gold pieces and a small land grant when you
bring me these four items, but once they are assembled I will be able to destroy The Armor of the
Damned, a magic artifact of unspeakable power and evil. NOW are you interested?"
Lý do: khớp từng chữ, đúng ngày, đúng địa điểm (`Wingtail Tavern`).

### C-07
Claim: lời dối "đúng theo kiểu luật sư" — "Together, they can be assembled into a great weapon, a weapon that I desperately require".
Nhãn bài gán: (không nhãn riêng) — `sod-bashing-skulls`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Bashing Skulls`, Timed events Day 1
Tìm thấy: "Individually, the items are worthless, mere tokens. But together, they can be assembled into
a great weapon, a weapon that I desperately require."
Lý do: khớp; bài lược chữ "But" ở đầu, không đổi nghĩa.

### C-08
Claim: thủ đoạn "chúng sẽ nói dối anh" xuất hiện ở **cả bốn** scenario, và **mỗi lần** kẻ bị gọi là nói dối đều đang nói thật.
Nhãn bài gán: T1* EXPLICIT — cả bốn key
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: cả bốn trang scenario, grep độc lập cho `will lie`, `would lie`, `lies like`, `do not listen`, `lying`
Tìm thấy: thủ đoạn có ở **ba** scenario, **không** có ở `A Cage in the Hand`.

- `Bashing Skulls`: "Now, I warn you, do not listen to anything he tells you… he has no honor and lies
  like a snake." ✅
- `Black Sheep`: "See, didn't I warn you he would lie to protect a mere possession?" ✅
- `A Cage in the Hand`: **0 kết quả.** Toàn bộ lời Sandro Day 1 chỉ có
  "They will do everything in their power to stop you from obtaining it." — cản đường, **không** phải
  cáo buộc nói dối. Grep `will lie|would lie|lies like|do not listen|lying` trên trang này: không match.
- `Grave Robber`: "Like the others you have battled, the Necromancers will lie to you. Do not listen to
  them." ✅

Vế thứ hai ("mỗi lần đều đang nói thật") cũng không đạt `EXPLICIT`: không game text nào xác nhận
Barshon nói thật, và với Marzeth thì game **tự phủ định** — "At best the rumor must be only half-true."
Lý do: claim "cả bốn" bị chính nguồn thứ ba phản bác; `sod-a-cage-in-the-hand` là key trỏ vào chỗ trống.
Sửa thành "ba trong bốn scenario" và hạ vế hai xuống `INFERENCE`.

### C-09
Claim: lần 1 — "lies like a snake" + Crag Hack xé cuộn giấy, "Barshon is a lying snake".
Nhãn bài gán: T1* EXPLICIT — `sod-bashing-skulls`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Bashing Skulls`, Timed events Day 1 + Events (54, 12, 0)
Tìm thấy: "do not listen to anything he tells you. Although, like you, he is a Barbarian, he has no
honor and lies like a snake." / "As you tear up the scroll you remember that Sandro said Barshon FOUND
the Helmet. You shrug. Barshon is a lying snake. Time to cut out his forked tongue!"
Lý do: khớp nguyên văn. Đúng như BH-1: câu thứ hai nằm trong block `==== Events ====`, không phải prologue.

### C-10
Claim: lần 2 — "See, didn't I warn you…" và "Never before have you heard a Wizard talk so brutally."
Nhãn bài gán: T1* EXPLICIT — `sod-black-sheep`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Black Sheep`, Timed events Day 1
Tìm thấy: "See, didn't I warn you he would lie to protect a mere possession? And he dared to call
himself a Barbarian! The coward had no honor. I hope his death was a most painful one." /
"Never before have you heard a Wizard talk so brutally."
Lý do: khớp từng chữ.

### C-11
Claim: map event (64, 9, 0) — mắt đồng minh trống rỗng, bằng chứng Sandro thao túng tâm trí.
Nhãn bài gán: T1* EXPLICIT — `sod-black-sheep`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Black Sheep`, `==== Events ====`, toạ độ (64, 9, 0)
Tìm thấy: "The Stronghold leader and his clan ride forward to greet you. As you embrace your fellow
Barbarian in a bear hug, you notice that his eyes look vacant. Although he has only kind words to say
about Sandro, you wonder how the puny wizard really managed to persuade this stout Barbarian to assist you."
Lý do: khớp nguyên văn, đúng toạ độ, đúng loại block.

### C-12
Claim: lần 3 — "We know nothing about a Sanctuary, Mister Hack, but we do know this: you are already dead…"
Nhãn bài gán: T1* EXPLICIT — `sod-a-cage-in-the-hand`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `A Cage in the Hand`, Timed events **Day 30** ("Reply")
Tìm thấy: "We know nothing about a Sanctuary, Mister Hack, but we do know this: you are already dead.
You just don't know it yet yourself."
Lý do: khớp nguyên văn. Ghi chú: đây là **timed event Day 30**, trả lời cho tin nhắn Crag Hack gửi
Day 21 — nếu bài ghi là map event thì sai chỗ.

### C-13
Claim: lần 4 — "Like the others you have battled, the Necromancers will lie to you. Do not listen to them."
Nhãn bài gán: T1* EXPLICIT — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber`, Timed events Day 1
Tìm thấy: "And one last thing. Like the others you have battled, the Necromancers will lie to you.
Do not listen to them."
Lý do: khớp từng chữ.

### C-14
Claim: GĐ1 nghi ngờ — "Sandro makes you think too much." (Day 1)
Nhãn bài gán: T1* EXPLICIT — `sod-a-cage-in-the-hand`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `A Cage in the Hand`, Timed events Day 1
Tìm thấy: "However, doing battle for this wizard is turning out not to be as much fun as you had hoped.
Sandro makes you think too much."
Lý do: khớp nguyên văn, đúng ngày.

### C-15
Claim: GĐ2 — "Maybe you should collect your rewards BEFORE handing over the last artifact." (Day 1)
Nhãn bài gán: T1* EXPLICIT — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber`, Timed events Day 1
Tìm thấy: "As you leave the tavern you think about all the lies you have encountered on Sandro's tasks.
Maybe you should collect your rewards BEFORE handing over the last artifact."
Lý do: khớp nguyên văn kể cả chữ in hoa `BEFORE`.

### C-16
Claim: GĐ3 — "Is Sandro the one who cannot be trusted?" (Day 15)
Nhãn bài gán: T1* EXPLICIT — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber`, Timed events Day 15
Tìm thấy: "More lies, you think as you tear up the scroll, but still doubts remain. Is Sandro the one
who cannot be trusted?"
Lý do: khớp nguyên văn, đúng ngày.

### C-17
Claim: hành động **xé cuộn giấy** lặp lại **đúng hai lần**, ở `sod-bashing-skulls` và `sod-grave-robber`.
Nhãn bài gán: (không nhãn), không source key
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: grep `tear up the scroll` trên cả bốn trang scenario
Tìm thấy: `Bashing Skulls` 1 lần (event 54, 12, 0), `Grave Robber` 1 lần (Day 15),
`Black Sheep` 0, `A Cage in the Hand` 0. Tổng đúng **2**.
Lý do: đếm độc lập khớp. Lưu ý `A Cage in the Hand` có hành động **tương tự nhưng khác chữ** —
"You crumble up the paper" (Day 30) — nên nếu bài định nói về mô-típ chứ không về chuỗi chữ thì con số
"đúng hai lần" cần nói rõ là đếm theo cụm "tear up the scroll".

### C-18
Claim: Hand of Death gọi Sandro là "an acquaintance of ours".
Nhãn bài gán: (không nhãn riêng) — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber`, Timed events Day 15
Tìm thấy: "We know you have been sent by an acquaintance of ours and what it is you seek."
Lý do: khớp nguyên văn.

### C-19
Claim: epilogue — "I've been tricked! The thieving Wizard took off with the artifacts…"
Nhãn bài gán: T1* EXPLICIT — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber`, `== Epilogue ==`
Tìm thấy: "I've been tricked! The thieving Wizard took off with the artifacts and didn't give me my gold!
When I find Sandro I'm going to rip his arms off and shove them down his lying throat! Argggggggggggggh!"
Lý do: khớp từng chữ kể cả số lượng chữ `g`.

### C-20
Claim: trang campaign *Unholy Alliance* ghi Sandro trở lại làm địch với Armor of the Damned nhưng **KHÔNG** có Cloak of the Undead King.
Nhãn bài gán: T1* EXPLICIT — `sod-wrath-of-sandro`
Phán quyết: NOT_FOUND (tại nguồn được dẫn)
Mức: **MAJOR**
Đã tìm ở: `Wrath of Sandro` (toàn trang), rồi `Unholy Alliance`, `Fall of Sandro`
Tìm thấy: câu đó **không có** ở `Wrath of Sandro`. Nó nằm ở trang campaign `Unholy Alliance`, mục
`==Important information==`, là **văn biên tập viên wiki** (ngoài mọi template):
"After you have played for Sandro, he appears in final scenarios as your enemy with Armor of the Damned,
but without Cloak of the Undead King."
Ngược lại, `Wrath of Sandro` **có** một game text thật liên quan trực tiếp, và nó là neo `T1*` tốt hơn
nhiều cho việc Sandro sở hữu Armor — timed event Day 4:
"With the Armor of the Damned and the Cloak of the Undead King in your possession, you will easily
overtake them and force these invaders out of your lands."
Lý do: hai lỗi cùng lúc — (a) mis-citation: bảng claim mô tả đúng là "trang campaign" nhưng key lại là
scenario; (b) sai **loại** tier: văn `==Important information==` là `T6`, không phải `T1*`. Nội dung
claim đúng, nhưng phải tách: sự kiện cơ chế "map cuối không có Cloak" → `T6`; sự kiện sở hữu →
`T1* EXPLICIT: sod-wrath-of-sandro` Day 4 (và `sod-target` Day 1: "At last! You have the Cloak of the
Undead King and the Armor of the Damned!").

### C-21
Claim: epilogue Yog — "we decided to split them up into less powerful components and disperse them throughout Antagarich."
Nhãn bài gán: T1* EXPLICIT — `sod-fall-of-sandro`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Fall of Sandro`, `== Epilogue ==`
Tìm thấy: "After realizing how corrupting these artifacts are, we decided to split them up into less
powerful components and disperse them throughout Antagarich. As for us, we decided to separate as well,
to distance our thoughts from a disaster history may never record."
Lý do: khớp nguyên văn.

### C-22
Claim: "These artifacts" là số nhiều và **không nêu tên**; epilogue **không bao giờ** gọi tên artifact nào; chúng bị **tháo rời và phân tán, không bị phá hủy**.
Nhãn bài gán: (không nhãn riêng) — `sod-fall-of-sandro`
Phán quyết: DOWNGRADE
Mức: MINOR
Đã tìm ở: `Fall of Sandro` (toàn trang: `region_text`, prologue, Timed events, Epilogue)
Tìm thấy: hai vế đầu CONFIRMED — epilogue thật sự chỉ nói "these artifacts", không tên nào, và
grep `Armor of the Damned|Cloak of the Undead` trên toàn trang `Fall of Sandro`: **0 kết quả**.
Nhưng vế "**không bị phá hủy**" bị chính trang đó làm phức tạp. `| region_text =`:
"Sandro must be conquered to ensure that he will never rise to power and threaten Antagarich again.
**The only certain way is to destroy the artifact that gave him his power and disperse the pieces
throughout the world.**"
Lý do: cùng một scenario dùng cả chữ "destroy" (số ít, region text) và "split them up… disperse"
(số nhiều, epilogue). Câu khẳng định phẳng "không bị phá hủy" bỏ mất nửa còn lại. Cách viết đúng:
epilogue mô tả **tháo rời + phân tán**; region text gọi cùng việc đó là "destroy the artifact… and
disperse the pieces" — tức game dùng "destroy" theo nghĩa **giải thể**, và bài nên nói rõ điều đó thay
vì phủ định trơn.

### C-23
Claim: Slot Torso; Class Combination (Relic); giá 12.000; chặn Helmet/Weapon/Shield; +3 Attack, +3 Defense, +2 Power, +2 Knowledge.
Nhãn bài gán: T1* EXPLICIT — `h3wiki-armor-of-the-damned`
Phán quyết: CONFIRMED
Mức: NOTE
Đã tìm ở: `Armor of the Damned`, template `CombinationArtifactNewSB`
Tìm thấy (wikitext thô):

```
 | class   = Combo
 | slot    = Torso
 | cost    = 12000
 | ceffect = +3 {{Psg|Attack}}<p>+3 {{Psg|Defense}}<p>+2 {{Psg|Power}}<p>+2 {{Psg|Knowledge}}
 | blocked = Helmet<p>Weapon<p>Shield
```

và cuối trang: `[[Category:Relic artifacts]]` · `[[Category:Combination artifacts]]`.
Lý do: mọi con số khớp. NOTE nhỏ: trường `class` ghi đúng chữ là **`Combo`**; chữ "Relic" đến từ
**category**, không từ trường class. Nếu bài viết "Class: Combination (Relic)" thì nên nói rõ hai nguồn
khác nhau của hai chữ đó.

### C-24
Claim: "Hiệu ứng in-game nguyên văn": "Casts Expert Slow, Curse, Weakness, and Misfortune for 50 rounds at the start of combat." — bốn spell, không phải năm, không có biến thể "Mass".
Nhãn bài gán: (không nhãn riêng) — `h3wiki-armor-of-the-damned`
Phán quyết: DOWNGRADE
Mức: **MAJOR**
Đã tìm ở: `Armor of the Damned` (trường `| effect =`), `Talk:Artifact/descriptions`
Tìm thấy: câu bài trích **đúng nguyên văn trường `| effect =`** của template wiki. Nhưng nó **không phải
text in-game**. Chuỗi in-game thật (`Talk:Artifact/descriptions`, tự ghi
`Information from H3Bitmap.lod > artraits.txt`, tier `T1`) là:
"All opponents have these spells effective on them for fifty turns: Slow, Curse, Weakness, and Misfortune."
Bằng chứng trường `effect` là văn wiki chuẩn hoá, không phải in-game: đối chiếu cùng hai nguồn cho các
artifact khác —

| Artifact | `\| effect =` trên wiki | `artraits.txt` (T1) |
|---|---|---|
| Orb of Inhibition | "Prevents either hero from casting any spells during combat." | "This powerful orb prevents all spell casting in combat." |
| Recanter's Cloak | "Prevents either hero from casting level 3, 4, or 5 spells during combat." | "While wearing this cloak, neither you nor your opponent will be able to cast level 3 or higher spells during combat." |
| Skull Helmet | "+2 Knowledge" | "Worn on the head, this item increases your Knowledge skill by +2." |

Lý do: vế nội dung ("bốn spell, không năm, không Mass") **đứng vững** — cả hai nguồn đều nói bốn spell.
Nhưng gọi câu đó là "hiệu ứng **in-game nguyên văn**" là sai loại nguồn, và nó lệch với `T1` ở hai chỗ đo
được: "50 rounds" vs "fifty turns", và có/không có chữ "Expert". Phải đổi câu trích sang chuỗi `T1` và
giữ câu wiki (nếu muốn) như diễn giải cơ chế, dẫn `h3wiki-armor-of-the-damned` với đúng tính chất.

### C-25
Claim: "Mô tả in-game": "Worn on the torso, this armor casts Slow, Weakness, Misfortune and Curse on the enemy at the start of every battle. The effect lasts for fifty turns."
Nhãn bài gán: **T6 EXPLICIT** — `fandom-artifact-list`
Phán quyết: **CONTRADICTED**
Mức: **MAJOR**
Đã tìm ở: `Talk:Artifact/descriptions` dòng 269 (bảng `H3Bitmap.lod > artraits.txt`)
Tìm thấy nguồn ngược, nguyên văn:
"All opponents have these spells effective on them for fifty turns: Slow, Curse, Weakness, and Misfortune."
Lý do: đây là **string table trích từ file game** (tier `T1` thật, key `h3wiki-artraits-txt` đã có trong
`REGISTRY.md`), và nó **không** phải câu Fandom. Câu Fandom là **diễn giải**, không phải mô tả in-game:
khác thứ tự spell (Slow/Curse/Weakness/Misfortune vs Slow/Weakness/Misfortune/Curse), thêm "Worn on the
torso", thêm "at the start of every battle", đổi "All opponents" thành "on the enemy". Chỉ "fifty turns"
là trùng.
Ngoài ra `T6 EXPLICIT` là **tổ hợp nhãn không hợp lệ** theo `CANON-POLICY.md` mục 2 (T6 tối đa
`INFERENCE`/`UNVERIFIED`).
**Đây là mục nên sửa đầu tiên**, và hướng sửa là **nâng tier**: thay bằng chuỗi `T1` ở trên, key
`h3wiki-artraits-txt`, nhãn `{T1 EXPLICIT: h3wiki-artraits-txt}`. Bỏ `fandom-artifact-list` khỏi bài.
Việc này cũng đóng luôn *Câu hỏi mở* Q5 mà bài tự nêu.

### C-26
Claim: text khi nhặt — "You trip over the Armor of the Damned, dust it off, and stick it in your pack."
Nhãn bài gán: (không nhãn), không source key
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Armor of the Damned`, trường `| event =`
Tìm thấy: "You trip over the Armor of the Damned, dust it off, and stick it in your pack."
Lý do: khớp từng chữ. (Trường `event` **là** in-game text — `REGISTRY.md` đã xác nhận độc lập qua
`h3wiki-artifact-events`, "Default descriptions when picking an artifact.")

### C-27
Claim: cộng chỉ số bốn thành phần = +3/+3/+2/+2, **bằng đúng** bộ hoàn chỉnh; giá 4 × 3.000 = 12.000.
Nhãn bài gán: T1* INFERENCE — bốn key thành phần
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Skull Helmet`, `Rib Cage`, `Blackshard of the Dead Knight`, `Shield of the Yawning Dead`, `Armor of the Damned`
Tìm thấy: +2 Knowledge (Helmet) + 2 Power (Rib Cage) + 3 Attack (Blackshard) + 3 Defense (Shield)
= +3 Attack / +3 Defense / +2 Power / +2 Knowledge, khớp **chính xác** `ceffect` của bộ. Giá:
3000 × 4 = 12000 = `cost` của bộ.
Lý do: phép cộng trên số liệu đã fetch độc lập; `INFERENCE` là nhãn đúng và bước suy luận đã ghi rõ.

### C-28
Claim: bảng bốn thành phần — class/slot/giá/hiệu ứng.
Nhãn bài gán: T1* EXPLICIT — bốn key thành phần
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: bốn trang thành phần, template `ArtifactNewSB`
Tìm thấy: Skull Helmet `class = Treasure`, `slot = Helmet`, `cost = 3000`, `+2 Knowledge` ·
Rib Cage `Minor`/`Torso`/`3000`/`+2 Power` · Blackshard `Minor`/`Weapon`/`3000`/`+3 Attack` ·
Shield of the Yawning Dead `Minor`/`Shield`/`3000`/`+3 Defense`.
Lý do: cả 16 ô khớp.

### C-29
Claim: text khi nhặt của từng món (Skull Helmet / Blackshard / Shield).
Nhãn bài gán: (không nhãn), không source key
Phán quyết: CONFIRMED
Mức: MINOR
Đã tìm ở: ba trang thành phần, trường `| event =`
Tìm thấy: Blackshard khớp **trọn câu**: "The widow of a former Captain of the Guard admires your quest
and gives you the enchanted Sword that her husband relied on during his tour of duty." ✅
Hai câu còn lại bị **cắt giữa đoạn không có dấu lược**:
- Skull Helmet, nguyên văn đầy đủ: "A brief stop at an improbable rural inn yields an exchange of money,
  tales, and accidentally, luggage. **You find a magical helm in your new backpack.**"
- Shield, nguyên văn đầy đủ: "Your troops discover an eerie shrine dedicated to the Undead. You bless
  the shrine, causing the stone shield emblem above the altar to crack. **Underneath it is a real
  shield, which you decide to separate from this unholy place.**"
Lý do: nội dung đúng, nhưng trích dẫn "nguyên văn" mà bỏ câu cuối và đóng bằng dấu chấm thường thì người
đọc tưởng đã hết. Thêm `…` hoặc trích đủ. Cũng nên bổ sung `event` của Rib Cage cho đủ bốn:
"You trip over what was the rib cage of a large creature. Upon further examination, you discover the rib
cage to be a piece of armor."

### C-30
Claim: `Shield of the Yawning Dead` **khác hoàn toàn** `Shield of the Damned` — artifact riêng biệt, không liên quan.
Nhãn bài gán: (không nhãn), không source key
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Shield of the Damned` (fetch trực tiếp, 728 byte), `Shield of the Yawning Dead`
Tìm thấy: `Shield of the Damned` — `class = Major`, `slot = Shield`, `cost = 6000`, `+6 Defense`, và
"Component of [[Armageddon's Blade]] in [[Maker of Sorrows]]." · Related artifacts: Armageddon's Blade,
Breastplate of Brimstone, Sword of Hellfire, Sphere of Permanence. Không có liên hệ nào tới Armor of
the Damned hay bốn thành phần của nó.
Lý do: theo BH-2, claim phủ định đã được kiểm bằng cách fetch **chính trang kia**, không suy từ im lặng.
Hai artifact khác class, khác giá, khác hiệu ứng, thuộc hai bộ combo khác nhau. Nên thêm source key
riêng cho trang `Shield of the Damned` (hiện claim không có key nào).

### C-31
Claim: "The Armor of the Damned only casts its opening combat spells once an allied creature is able to take its turn; if a creature misses a turn due to low morale…"
Nhãn bài gán: T1* INFERENCE — `h3wiki-armor-of-the-damned`
Phán quyết: DOWNGRADE
Mức: **MAJOR**
Đã tìm ở: `Armor of the Damned` (thân trang), `Ironfist of the Ogre`, `Angelic Alliance`, `Talk:Artifact/descriptions`
Tìm thấy: câu này CONFIRMED nguyên văn — nhưng nó nằm **ngoài mọi template**, là **văn biên tập viên
wiki, không một footnote nào**. Không có trong `artraits.txt`, không có trên `Trivia`, không có trên
hai trang artifact-cast khác.
Lý do: sai **loại** tier. Theo tiền lệ đã ghi trong `REGISTRY.md` (`h3wiki-terek`: "Đừng gán `T1*` cho
câu lấy từ `== Story ==`"), văn ngoài template là `T6`. Một claim `T6` tối đa `INFERENCE`/`UNVERIFIED` —
nhãn `INFERENCE` thì đúng trục B, nhưng trục A phải là `T6`, và `CANON-POLICY.md` mục 2 buộc `INFERENCE`
phải **ghi rõ bước suy luận**; ở đây không có bước nào, chỉ là chép lại lời wiki.
Ghi nhận điểm cộng: bài đã tự đưa cơ chế này xuống *Câu hỏi mở* (C-52), nên chỉ cần sửa tier + cách diễn
đạt ("theo văn wiki không dẫn nguồn"), không cần bỏ.

### C-32
Claim: cái gì chặn được — immunity của quân địch, **Cursed Ground**, và "anti-magic artifacts".
Nhãn bài gán: (không nhãn riêng) — `h3wiki-armor-of-the-damned`
Phán quyết: DOWNGRADE
Mức: **MAJOR**
Đã tìm ở: `Armor of the Damned`, `Ironfist of the Ogre`, `Angelic Alliance`, `Orb of Inhibition`, `Terrain`
Tìm thấy: câu CONFIRMED nguyên văn trên trang Armor —
"The Armor of the Damned's ability to cast Slow, Curse, Weakness, and Misfortune, can be mitigated by
enemy creatures' immunity, Cursed Ground, or anti-magic artifacts. However, it works normally in
Anti-Magic Garrisons."
Nhưng **đúng câu đó, gần như từng chữ, được lặp lại trên hai trang artifact khác**:
- `Ironfist of the Ogre`: "…can be mitigated by enemy creatures' immunity, Cursed Ground, or anti-magic
  artifacts. However, it works normally in Anti-Magic Garrisons."
- `Angelic Alliance`: "…can be mitigated by allied creatures' immunity, Cursed Ground, or anti-magic
  artifacts. However, it works normally in Anti-Magic Garrisons."

Lý do: sự lặp lại y nguyên trên ba trang (một trong đó là artifact **HotA**) chứng minh dứt điểm đây là
**boilerplate của biên tập viên**, không phải text sản phẩm → `T6`, không phải `T1*`. Nặng hơn: nội dung
của nó **sai ở ít nhất một trường hợp** đã được chính wiki phản bác (xem C-41), và vế Cursed Ground
không được `Terrain` chống lưng (xem C-51). Vậy claim này không được trình bày như dữ kiện gameplay mà
phải trình bày như "trang wiki nói X, nhưng trang Orb of Inhibition nói ngược".

### C-33
Claim: hoạt động bình thường trong Anti-Magic Garrison, xác nhận độc lập ở trang thứ hai.
Nhãn bài gán: T1* EXPLICIT — `h3wiki-trivia`
Phán quyết: DOWNGRADE
Mức: MINOR
Đã tìm ở: `Trivia` (15.817 byte, khớp `revisions.size` qua API), dòng 56, mục
`== Verified Statements ==` → `=== Artifacts ===`; kiểm chéo `list=backlinks&bltitle=Anti-Magic Garrison`
Tìm thấy (wikitext thô):

```
* {{An|Armor of the Damned}}, {{An|Angelic Alliance}}, and {{An|Ironfist of the Ogre}}{{-wh}} spells still work in an [[Anti-Magic Garrison]].
```

Lý do: nội dung CONFIRMED nguyên văn, và đúng là **trang thứ hai** (backlinks xác nhận `Trivia` liên kết
tới `Anti-Magic Garrison`). Chỉ tier sai: `Trivia` là trang **tổng hợp của cộng đồng** — chính trang tự
chia `Verified Statements` / `Unverified Claims` / `False Claims`, tức là quan sát của người chơi, không
phải text sản phẩm → `T6`. Việc wiki tự xếp vào "Verified" đáng ghi, nhưng không nâng được tier.

### C-34
Claim: **bốn hero** tăng hiệu quả Weakness — Cuthbert, Olema, Mirlanda, Eanswythe (chỉ có ở HotA).
Nhãn bài gán: T1* EXPLICIT — `h3wiki-weakness`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Armor of the Damned`, `Weakness`, và **từng trang hero**: `Cuthbert`, `Olema`, `Mirlanda`, `Eanswythe`
Tìm thấy: trang Armor (wikitext thô):

```
{{Hn|Cuthbert|0=}}, {{Hn|Olema|0=}}, {{Hn|Mirlanda|0=}}{{showwithhota|, and {{Hn|Eanswythe|0=}}{{-wh}}}}'s specialties will improve the effect of {{Sn|Weakness}} cast by the Armor of the Damned.
```

Trang `Weakness`, mục "Heroes specialising in Weakness": Cuthbert (Cleric), Olema (Heretic),
Mirlanda (Witch), và Eanswythe (Artificer) trong `<ul class="onlyhota">`.
Eanswythe chỉ có ở HotA — trang hero mở đầu bằng `{{inhota}}`, `| town = Factory`, `| class = Artificer`.
Lý do: con số **4** đúng, không thiếu ai (đối chiếu hai danh sách độc lập: "starting with Weakness" và
"specialising in Weakness" — trùng nhau hoàn toàn), và tính HotA-only của Eanswythe được xác nhận bằng
hai dấu độc lập (`{{inhota}}` trên trang hero, `onlyhota` trên trang spell). Cả class Artificer lẫn town
Factory đều khớp.

### C-35
Claim: specialty cả bốn giống nhau — HotA: +4/+6/+8/+10 theo bậc quân; SoD gốc: +3/+2/+1.
Nhãn bài gán: (không nhãn riêng) — `h3wiki-weakness`
Phán quyết: NOT_FOUND (tại nguồn được dẫn) — **nhưng chiều đọc `{{swh}}` là ĐÚNG**
Mức: **MAJOR**
Đã tìm ở: `Weakness` (toàn trang), rồi `Cuthbert`, `Olema`, `Mirlanda`, `Eanswythe`
Tìm thấy: trang `Weakness` **không chứa một con số specialty nào** — nó chỉ liệt kê tên hero. Các con số
nằm ở trường `| s_text =` của **từng trang hero**. Nguyên văn (giống hệt nhau ở cả Cuthbert, Olema,
Mirlanda):

```
| s_text = {{swh|Casts Weakness with effect increased by 4 for level 1–2 creatures, by 6 for level 3–4 creatures, by 8 for level 5–6 creatures, and by 10 for level 7 creatures.|Casts Weakness with effect increased by 3 for level 1–2 creatures, by 2 for level 3–4 creatures, and by 1 for level 5–6 creatures.}}
```

**Kiểm bẫy `{{swh}}` — bài đọc ĐÚNG chiều.** Tham số 1 = HotA (4/6/8/10), tham số 2 = SoD (3/2/1),
khớp chính xác điều bài viết. Xác nhận độc lập, không dựa vào `Template:Swh`: **Eanswythe là hero
chỉ-có-ở-HotA**, và trường `s_text` của nàng **không dùng `{{swh}}` chút nào** — nó ghi trơn:
"Casts Weakness with effect increased by 4 for level 1–2 creatures, by 6 for level 3–4 creatures, by 8
for level 5–6 creatures, and by 10 for level 7 creatures."
Một hero chỉ tồn tại trong HotA mang đúng dãy 4/6/8/10 → dãy đó **là** giá trị HotA. Chiều đọc của bài
được chứng minh bằng nguồn thứ hai, không phải bằng suy diễn.
Lý do MAJOR: mis-citation. `h3wiki-weakness` trỏ vào chỗ không có con số nào. Phải thay bằng bốn key
trang hero. (Nội dung không cần sửa.)

### C-36
Claim: Armor of the Damned là **artifact duy nhất trong game** cast được Weakness.
Nhãn bài gán: T1* EXPLICIT — `h3wiki-weakness`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Weakness` (mục "Artifacts capable of casting Weakness"), kiểm chéo `Ironfist of the Ogre`, `Angelic Alliance`, `Talk:Artifact/descriptions`
Tìm thấy: trang `Weakness` liệt kê **đúng một** mục:

```
'''Artifacts capable of casting Weakness:'''
* {{An|Armor of the Damned}} {{-ws}}
```

Kiểm chéo hai artifact cast-spell còn lại: `Ironfist of the Ogre` cast Haste / Bloodlust / Fire Shield /
Counterstrike; `Angelic Alliance` cast Prayer ("Casts Expert Prayer at the start of combat" trong
`artraits.txt`). Không cái nào cast Weakness.
Lý do: claim độc quyền được kiểm bằng cách liệt kê **toàn bộ** tập ứng viên (ba artifact cast spell trong
H3 + HotA) chứ không chỉ đọc một danh sách. Không tìm được phản ví dụ.

### C-37
Claim: **không có thay đổi nào riêng cho artifact này** qua các bản; grep toàn changelog HotA cho cả năm cái tên — **không một kết quả nào**.
Nhãn bài gán: T1* EXPLICIT — `hota-changelog`
Phán quyết: DOWNGRADE
Mức: **MAJOR**
Đã tìm ở: `Horn of the Abyss (Changelog)`, fetch lại độc lập — **201.529 byte**, khớp con số registry
Tìm thấy: grep độc lập, case-insensitive, từng tên một:
`Armor of the Damned` → **0** · `Skull Helmet` → **0** · `Rib Cage` → **0** · `Blackshard` → **0** ·
`Yawning` → **0**. Đối chứng cùng lần grep: `Cloak of the Undead King` → **3**. Vậy grep hoạt động,
con số 0 là thật.
Lý do DOWNGRADE — hai điểm:
1. **`EXPLICIT` từ im lặng là nhãn không hợp lệ.** Không có câu nào trong changelog nói "Armor of the
   Damned không đổi". Đây là suy luận từ vắng mặt → `T1* INFERENCE`, và phải ghi rõ bước suy luận.
   Đúng loại lỗi mà `CLAUDE.md` gọi là "trông giống sự cẩn trọng".
2. **Claim thiếu, không chỉ sai nhãn.** Changelog **có** những thay đổi chung cho combination artifact,
   áp lên Armor of the Damned dù không gọi tên:
   - "The option of banning combination artifacts, which influences the possibility to assemble and
     disassemble them, is added" (xuất hiện hai lần, một bản cho map và một cho template)
   - "Fixed a bug: HotA-original combination artifacts were not included in the list of combination
     artifacts banned from assembly"
   - "In artifact description, it is noted a component of which combination artifact it is, and whether
     this combination artifact is allowed for assembly on the current map" — thay đổi này **đổi text
     hiển thị của bốn thành phần** trong HotA.

   Chữ "riêng cho artifact này" cứu được vế đầu, nhưng bài nên nói thêm rằng có thay đổi **chung** chạm
   tới nó, thay vì để người đọc hiểu là hoàn toàn không bị ảnh hưởng.

### C-38
Claim: Cloak of the Undead King bị cấm ghép mặc định trong HotA, Armor of the Damned **không nằm trong** lệnh cấm đó.
Nhãn bài gán: (không nhãn riêng) — `hota-changelog`
Phán quyết: DOWNGRADE
Mức: MINOR
Đã tìm ở: `Horn of the Abyss (Changelog)`, grep `Cloak of the Undead King` (3 kết quả) và `combination artifact` (4 kết quả)
Tìm thấy nguyên văn: "The Cloak of the Undead King is not allowed to be assembled by default. It remains
allowed on the Anarchy and Clash of Dragons templates, as well as in a number of single player scenarios"
Hai kết quả còn lại: bản sau thêm template "Default Random Map (Legacy)" — "allowed Cloak of the Undead
King…"; và một dòng về giá trị Necromancy.
Lý do: vế "Cloak bị cấm" là `EXPLICIT` ✅. Vế "Armor **không** nằm trong lệnh cấm" là **suy từ việc câu
đó chỉ gọi tên Cloak** cộng với 0 kết quả grep cho Armor → `INFERENCE`, không `EXPLICIT`. Mức nhẹ vì câu
nguồn nêu tên đích danh chỉ một artifact, nên suy luận rất ngắn — nhưng vẫn là suy luận.

### C-39
Claim: nguồn của lỗi "5 spell" nằm trong đoạn `fanopinion` trên chính trang artifact.
Nhãn bài gán: T6 FAN_THEORY — `h3wiki-armor-of-the-damned`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Armor of the Damned`, khối `{{fanopinion|…}}`
Tìm thấy: "…casting a total of four spells at Expert level, at no cost, and leaving the hero free to
cast another spell on their action (so potentially 5 spells in a single turn)."
Lý do: khớp nguyên văn, và **đúng là nằm trong wrapper `fanopinion`**, đóng bằng
`}}<!-- end of fan opinion -->`. Nhãn `T6 FAN_THEORY` là tổ hợp hợp lệ, và theo `CANON-POLICY.md` mục 5.5
nó phải ở mục riêng — bài đặt ở *Điểm tranh chấp canon*, đúng chỗ.

### C-40
Claim: grep toàn trang — **0 kết quả** cho cả "Mass" lẫn "Disrupting".
Nhãn bài gán: (không nhãn), không source key
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Armor of the Damned`, toàn bộ 2.400 byte gồm cả `fanopinion` và gallery
Tìm thấy: `grep -c "Mass"` → **0** · `grep -c "Disrupting"` → **0**
Lý do: grep lại độc lập (không tin con số của bài), trên bản fetch riêng. Khớp.

### C-41
Claim: trang Orb of Inhibition liệt kê dưới "Does not prevent": "Artifact spell casting (i.e. Armor of the Damned, Angelic Alliance or Ironfist of the Ogre)."
Nhãn bài gán: T1* EXPLICIT — `h3wiki-orb-of-inhibition`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Orb of Inhibition`
Tìm thấy (wikitext thô):

```
'''Does not prevent:'''
* Artifact spell casting (i.e. {{An|Armor of the Damned}}, {{An|Angelic Alliance}} or {{An|Ironfist of the Ogre}}{{-wh}}).
* {{Cn|Faerie Dragon}} spell casting.
```

Lý do: khớp nguyên văn. Kết luận của bài — cách nói "anti-magic artifacts" trên trang Armor sai với ít
nhất một trường hợp — đứng vững, và mạnh hơn bài nghĩ: Orb of Inhibition là artifact anti-magic **triệt
để nhất** trong game (`artraits.txt`: "This powerful orb prevents all spell casting in combat."), vậy
phản ví dụ này là phản ví dụ ở trường hợp cực đoan nhất. Lưu ý tier: hai mục này nằm ngoài template
(`'''Does not prevent:'''`), nên chặt chẽ thì là `T6` — nhưng nó là **phản bác một claim `T6` khác**, nên
sức nặng logic không đổi.

### C-42
Claim: trang Ethric mục Trivia suy Armor + Cloak từng thuộc Ethric, "since Jeddite's stated goal in Target is to return them to him"; và "possible, though not confirmed" rằng Ethric tạo ra chúng.
Nhãn bài gán: T6 FAN_THEORY — `h3wiki-ethric`
Phán quyết: CONFIRMED
Mức: NOTE
Đã tìm ở: `Ethric` mục `== Trivia ==` (dòng 91)
Tìm thấy nguyên văn, **cả câu**: "Armor of the Damned and Cloak of the Undead King once belonged to
Ethric, since Jeddite's stated goal in Target is to return them to him. **This is an apparent hint at
this Ethric actually being Ethric the Mad, as later directly confirmed by Jennifer Bullard.** It is also
possible, though not confirmed, that the two artifacts, reassembled by Sandro, were originally created
by Ethric."
Lý do: khớp; `T6 FAN_THEORY` là nhãn đúng (trang Ethric không có một footnote nào).
NOTE cho bài: (a) đoạn bài lược bỏ câu giữa, mà câu giữa quan trọng — nó cho thấy wiki dùng **cùng một
suy luận** để đạt **hai** kết luận, trong đó kết luận về Ethric the Mad thì `bullard-interview-2013`
chống lưng còn kết luận về sở hữu thì không; (b) cùng một suy luận này còn xuất hiện ở **trang thứ hai**:
`The Shadow of Death` mục Plot ghi "two powerful artifacts that once belonged to his former mentor
Ethric". Bài nên nêu cả hai vị trí, vì `REGISTRY.md` đã đánh dấu câu ở trang SoD là bị game text phản bác.

### C-43
Claim: phản bác — `sod-target` Day 1: Ethric là **kẻ loan tin**, không phải người đòi lại; và region text về các lãnh chúa.
Nhãn bài gán: T1* EXPLICIT — `sod-target`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Target`, Timed events Day 1 và `| region_text =`
Tìm thấy: Day 1 — "You have also learned Ethric has spread word of your whereabouts to those who lost
these two precious artifacts and to others who have their own reasons for despising Necromancers."
`region_text` — "Ethric is a sly old Warlock. He has spread word of Sandro and the artifacts he carries
to the lords of this region. Some of the lords want these artifacts for their own use; others want to
destroy them."
Lý do: khớp nguyên văn cả hai. Thêm một xác nhận thứ ba mà bài có thể dùng — prologue (chính Sandro nói):
"He spread word of my location to those who would stop me." Ba lần trên cùng một trang, Ethric giữ đúng
một vai: **người loan tin**. Không lần nào là chủ sở hữu hay người đòi lại. Phản bác vững.

### C-44
Claim: **Lỗi 1** — prologue `Grave Robber` nói vừa giao "the Death Knight's Sword", nhưng Day 1 event của chính scenario đó mở đầu "You have the Rib Cage!"
Nhãn bài gán: T1* EXPLICIT — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber`, `== Prologue ==` và Timed events Day 1; kiểm `{{sic}}` / `<!--Error` trên cả bốn trang scenario
Tìm thấy: prologue — "Now that I gave him the Death Knight's Sword, Sandro wants me to fight some more
Necromancers for a shield." · Day 1 — "You have the Rib Cage! Excellent work, Mister Hack".
Grep `{{sic` trên cả bốn trang scenario: **0 kết quả**. Grep `<!--Error`: 0.
Lý do: mâu thuẫn nội bộ CONFIRMED trong cùng một trang, cùng một scenario. Và wiki **không** đánh dấu
`{{sic}}` cho nó, khớp với điều bài khẳng định ở C-46.

### C-45
Claim: Blackshard đã giao **một scenario trước**, ở đầu `A Cage in the Hand`.
Nhãn bài gán: T1* EXPLICIT — `sod-a-cage-in-the-hand`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `A Cage in the Hand`, `== Prologue ==`
Tìm thấy: "I got Sandro his cursed sword, and now he wants me to fight more moldy Necromancers to get
some kind of armor made out of bones. Hah! It'll be their bones I smash!"
Xác nhận chéo: `A Cage in the Hand` Day 1 — Sandro nói "That stinking Death Knight Marzeth is now a
dead Knight" và chuyển sang "the third item I require is the Rib Cage of Power". Vậy Blackshard giao ở
đầu scenario 3, Rib Cage giao ở đầu scenario 4 — đúng như bài lập luận.
Lý do: khớp nguyên văn; chuỗi giao hàng khép kín được xác nhận bằng hai trang liền nhau.

### C-46
Claim: wiki **âm thầm che lỗi này** bằng pipe link `[[Blackshard of the Dead Knight|Death Knight's Sword]]`, và wiki **không đánh dấu là lỗi ở đâu cả**.
Nhãn bài gán: (không nhãn), không source key
Phán quyết: DOWNGRADE
Mức: MINOR
Đã tìm ở: `Grave Robber` (wikitext thô), `A Cage in the Hand`, grep `{{sic` và `<!--Error` trên cả bốn trang
Tìm thấy: pipe link tồn tại đúng như bài ghi (wikitext thô):

```
Now that I gave him the [[Blackshard of the Dead Knight|Death Knight's Sword]], [[Sandro]] wants me to fight some more [[Necromancer|Necromancers]] for a [[Shield of the Yawning Dead|shield]].
```

Không có `{{sic}}` nào trên bốn trang scenario ✅.
Lý do DOWNGRADE — hai chỗ cần chỉnh:
1. "**âm thầm che lỗi**" là **diễn giải**, không phải dữ kiện. Pipe link chỉ đổi **chữ hiển thị**; lỗi
   cốt truyện (nói vừa giao *sword* trong khi vừa giao *Rib Cage*) nằm trong văn xuôi và hiện ra bất kể
   pipe link. Thực tế pipe link còn làm **rõ** món được nhắc là Blackshard — tức nó phơi lỗi ra chứ
   không che. Cùng trang cũng dùng pipe link y hệt cho `[[Shield of the Yawning Dead|shield]]` ở chỗ
   **không có lỗi** nào — đây là quy ước trình bày chung, không phải hành vi che.
2. "**không đánh dấu là lỗi ở đâu cả**" phải thu hẹp phạm vi: **chính trang đó có** một chú thích của
   biên tập viên đánh dấu một lỗi **khác** trong cùng đoạn mô tả — "''Note: Although the description
   states that Crag Hack carries over to the next campaign, that is not accurate.''" (xem C-47). Nên
   viết: wiki đánh dấu lỗi carry-over nhưng **không** đánh dấu lỗi sword/Rib Cage.

### C-47
Claim: **Lỗi 2** — mô tả scenario nói Crag Hack "will carry his experience, skills and spells on to his next campaign", và wiki phải ghi chú "that is not accurate."
Nhãn bài gán: (không nhãn) — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber` (`| description =` và dòng ghi chú ngay sau template), `Unholy Alliance`
Tìm thấy: `| description = … Crag Hack is limited to level 25 but will carry his experience, skills and
spells on to his next campaign.` · ngay sau đó: "''Note: Although the description states that Crag Hack
carries over to the next campaign, that is not accurate. Click here for more details.''"
Xác nhận chéo tại `Unholy Alliance` mục `==Important information==`: "Although previous Shadow of Death
campaign descriptions state that Crag Hack, Gelu, Gem, and Yog advance to the next campaign… with their
primary skills, secondary skills and spells, it is not true. Heroes appear on level 25 in their first
scenarios, but with no magic (Gem with one spell), and… with a *random* set of eight secondary skills…"
Lý do: khớp nguyên văn; và tìm được nguồn thứ hai giải thích cụ thể lỗi đó — bài có thể dẫn thêm.
Cũng thêm một điểm khách quan: trường `| carry =` của `Grave Robber` **để trống** (trong bảng campaign
ghi `carry=(none)`), khác cả ba scenario trước đều `carry = Crag Hack` → dữ liệu map tự phản bác mô tả.

### C-48
Claim: **Lỗi 3** — mô tả gọi artifact là "the Yawning Shield of the Dead", trong khi tên thật và điều kiện thắng là "Shield of the Yawning Dead".
Nhãn bài gán: (không nhãn) — `sod-grave-robber`
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: `Grave Robber`, `| description =` và `| victory =`
Tìm thấy: `| description = Seize the Yawning Shield of the Dead from the "Hand of Death" Necromancer
cult to win the campaign.` · `| victory = Acquire Artifact {{gl|Shield of the Yawning Dead}}.`
Lý do: hai trường của **cùng một template, cùng một trang** dùng hai tên khác nhau. Tên trang artifact
thật là `Shield of the Yawning Dead` (fetch được, 642 byte). Lỗi CONFIRMED, và cũng không có `{{sic}}`.

### C-49
Claim: thứ tự thu thập 1→4 kèm độ khó; thứ tự này **không** khớp thứ tự liệt kê thành phần trên trang artifact.
Nhãn bài gán: T1* EXPLICIT — bốn key
Phán quyết: CONFIRMED
Mức: —
Đã tìm ở: bốn trang scenario (`| victory =`, `| difficulty =`, `| cback =`), `Hack and Slash`, `Armor of the Damned`
Tìm thấy: `Bashing Skulls` → Skull Helmet, `difficulty = Hard`, `cback = sod has 1` ·
`Black Sheep` → Blackshard of the Dead Knight, `Hard`, `sod has 2` ·
`A Cage in the Hand` → Rib Cage, `Expert`, `sod has 3` ·
`Grave Robber` → Shield of the Yawning Dead, `Expert`, `sod has 4`.
Trang artifact liệt kê: `art_1 = Skull Helmet` · `art_2 = Rib Cage` · `art_3 = Blackshard of the Dead
Knight` · `art_4 = Shield of the Yawning Dead`.
Lý do: cả bốn dòng khớp, độ khó khớp, và thứ tự `cback` (`sod has 1..4`) xác nhận thứ tự campaign một
cách độc lập với suy luận. Lệch thật: vị trí 2 và 3 đảo nhau giữa hai danh sách.

### C-50
Claim (Câu hỏi mở): Recanter's Cloak và Cape of Silence có chặn được không? Chưa kiểm.
Nhãn bài gán: **T1\* UNVERIFIED** — `h3wiki-armor-of-the-damned`
Phán quyết: CONFIRMED (vị trí hợp lệ)
Mức: NOTE — **đã giải được phần lớn trong đợt này**
Đã tìm ở: `Recanter's Cloak`, `Cape of Silence`, `Orb of Inhibition`, `Talk:Artifact/descriptions`
Tìm thấy: `Recanter's Cloak` — `| effect = Prevents either hero from casting level 3, 4, or 5 spells
during combat.` (`artraits.txt`: "While wearing this cloak, neither you nor your opponent will be able
to cast level 3 or higher spells during combat.")
`Cape of Silence` (HotA) — `| effect = Prevents either hero from casting level 1 or 2 spells during combat.`
Lý do: `UNVERIFIED` trong *Câu hỏi mở* là hợp lệ theo `CANON-POLICY.md` mục 5.3 — **không báo lỗi vị trí**.
Nhưng câu hỏi giờ trả lời được ở mức `INFERENCE`: cả hai artifact đều được mô tả là chặn **hero**
("either hero"), không phải chặn artifact; và `Orb of Inhibition` — thứ chặn **toàn bộ** hero casting —
lại ghi thẳng rằng nó **không** chặn artifact casting của Armor of the Damned (C-41). Một artifact chặn
hẹp hơn thì không thể chặn nhiều hơn artifact chặn rộng hơn. Vậy suy được: **không chặn**.
Đề nghị: hạ từ `UNVERIFIED` xuống `{T1* INFERENCE: h3wiki-recanters-cloak + h3wiki-cape-of-silence +
h3wiki-orb-of-inhibition — cả hai chỉ chặn hero casting, và Orb chặn rộng hơn vẫn không chặn artifact}`.
Đây là **thu hẹp** một câu hỏi mở, một việc `CANON-POLICY.md` mục 2 gọi là cần xử lý, không để tồn đọng.

### C-51
Claim (Câu hỏi mở): Cursed Ground thật sự chặn được không? Chỉ có trang Armor khẳng định.
Nhãn bài gán: **T1\* UNVERIFIED** — `h3wiki-armor-of-the-damned`
Phán quyết: CONFIRMED (vị trí hợp lệ)
Mức: NOTE — có **phản chỉ dấu** mới
Đã tìm ở: `Cursed Ground` (là redirect → `Terrain#Cursed Ground`), `Terrain`, `Trivia`, `Orb of Inhibition`
Tìm thấy: `Terrain`, hàng Cursed Ground, nguyên văn: "Prevents hero from casting of spells above level 1,
includes both adventure and combat spells. Also does not allow creatures to cast any spells. Disables all
native terrain bonuses. Negates all positive morale effects. Negates all positive luck effects."
Lý do: `UNVERIFIED` ở *Câu hỏi mở* là hợp lệ, không báo lỗi vị trí. Nhưng ghi nhận cho lần sau: trang
`Terrain` **liệt kê đủ hiệu ứng của Cursed Ground và không nhắc artifact casting** — chỉ hero (trên cấp 1)
và creature. Đây là **cùng một cấu trúc** với trường hợp Orb of Inhibition, nơi "không nhắc" hoá ra là
"không chặn". Thêm nữa Slow/Curse là cấp 1 nên cả giới hạn "above level 1" cũng không áp được cho hai
spell đó. Vậy câu khẳng định trên trang Armor không được nguồn thứ hai chống lưng và có phần nghiêng về
**sai**. Đây cũng là chi tiết củng cố C-32.

### C-52
Claim (Câu hỏi mở): cơ chế "chỉ kích hoạt khi quân đồng minh được đi" có đúng không? Văn wiki chi tiết nhưng không dẫn nguồn.
Nhãn bài gán: **T1\* UNVERIFIED** — `h3wiki-armor-of-the-damned`
Phán quyết: CONFIRMED (vị trí hợp lệ)
Mức: NOTE
Đã tìm ở: `Armor of the Damned`, `Ironfist of the Ogre`, `Angelic Alliance`, `Trivia` (cả ba mục
Verified / Unverified / False Claims), `Talk:Artifact/descriptions`
Tìm thấy: câu về morale/lượt đi **chỉ tồn tại trên trang Armor of the Damned**. Hai trang artifact
cast-spell còn lại **không có** câu tương ứng — dù chúng chia sẻ nguyên văn câu boilerplate thứ hai
(xem C-32). `Trivia` không nhắc gì tới cơ chế này ở bất cứ mục nào.
Lý do: `UNVERIFIED` ở *Câu hỏi mở* là hợp lệ và **đúng đắn** — đây chính là mức nên dùng. Ghi thêm để
lần sau khỏi tìm lại: đã quét bốn trang, không có xác nhận độc lập nào. Chỉ giải được bằng test in-game
hoặc reverse-engineering, không giải được bằng wiki.

---

## Phát hiện phụ (không thuộc claim nào)

**1. `Wrath of Sandro` chứa game text `T1*` mà bài chưa dùng.** Timed event Day 4:
"With the Armor of the Damned and the Cloak of the Undead King in your possession, you will easily
overtake them and force these invaders out of your lands." Và Day 12 nhắc Gem "assembled the pieces for
the Cloak of the Undead King… she did send a letter to Ethric, tipping him off of your whereabouts."
Đây là neo `T1*` cho việc Sandro **đồng thời** sở hữu cả hai artifact ở đầu *Unholy Alliance*, tốt hơn
hẳn văn wiki mà C-20 đang dẫn.

**2. Nguồn `T4` `fulton-names-2023`: đã kiểm, KHÔNG có gì.** Fetch trọn 98.499 byte
`Gregory Fulton/On Names in Heroes of Might and Magic III`. Grep: `Armor of the Damned` 0 · `Blackshard`
0 · `Skull Helmet` 0 · `Rib Cage` 0 · `Yawning` 0 · `Damned` 0. `Crag Hack` và `Yog` mỗi tên **1** lần,
và cả hai chỉ nằm trong danh sách hero **HoMM1** mà Fulton dẫn ra làm ví dụ cho việc đặt tên tuỳ hứng
("Do any of these names strike you as resulting from some form of research, or… improvisation? To my eyes
and ears… improvisation."), **không** phải bình luận về nhân vật. Kết luận: không có nguồn `T4` mới cho
bài này. Ghi lại để `B-020` không phải quét lại phần này.

**3. Cơ hội nâng tier `T1` — đã tìm được, thuộc `B-001`.** `Talk:Artifact/descriptions` (đã có key
`h3wiki-artraits-txt`, tier `T1` thật) chứa dòng cho **cả năm** artifact của bài:

| Artifact | Chuỗi in-game (`H3Bitmap.lod > artraits.txt`) |
|---|---|
| Armor of the Damned | "All opponents have these spells effective on them for fifty turns: Slow, Curse, Weakness, and Misfortune." |
| Skull Helmet | "Worn on the head, this item increases your Knowledge skill by +2." |
| Rib Cage | "Worn on the torso, this item increases your Power skill by +2." |
| Blackshard of the Dead Knight | "This right handed weapon increases your Attack skill by +3." |
| Shield of the Yawning Dead | "This left handed item increases your Defense skill by +3." |

Năm claim hiện mang `T1*` hoặc `T6` (C-23, C-24, C-25, C-28) **nâng được lên `T1` không dấu sao** bằng
nguồn này. Đây là tiến bộ cụ thể cho `B-001`.

---

## Kết luận

**CHƯA đủ điều kiện `status: verified`.** Không còn `BLOCKER`, nhưng còn **10 `MAJOR`**, và tiêu chí là
"không còn BLOCKER **và** không còn MAJOR".

Điểm mạnh của bài: 36/52 claim CONFIRMED nguyên văn, tỉ lệ rất cao cho một bài dày text scenario. Đặc
biệt, **bẫy `{{swh}}` đã được vượt qua đúng chiều** (C-35) — dãy HotA 4/6/8/10 và SoD 3/2/1 là chính xác,
và tôi xác nhận lại bằng nguồn thứ hai độc lập (hero Eanswythe chỉ-có-ở-HotA mang dãy 4/6/8/10 **không
qua `{{swh}}`**). Bài cũng đã kiểm đúng trang disambiguation cho C-30 theo BH-2, và đọc đúng block
`==== Events ====` cho C-09/C-11 theo BH-1.

### Bắt buộc sửa (MAJOR) — theo thứ tự ưu tiên

1. **C-25** — thay câu Fandom bằng chuỗi `T1` thật từ `h3wiki-artraits-txt`:
   "All opponents have these spells effective on them for fifty turns: Slow, Curse, Weakness, and
   Misfortune." Bỏ `fandom-artifact-list`. `T6 EXPLICIT` là tổ hợp nhãn không hợp lệ. Sửa cái này đóng
   luôn *Câu hỏi mở* Q5 và nâng tier.
2. **C-24** — thôi gọi trường `| effect =` của wiki là "hiệu ứng in-game nguyên văn". Nó là văn wiki
   chuẩn hoá (đã chứng minh bằng ba đối chiếu). Vế "bốn spell, không năm" vẫn giữ.
3. **C-08** — sửa "cả bốn scenario" thành **ba** scenario. `A Cage in the Hand` **không có** thủ đoạn
   "chúng sẽ nói dối anh" (grep 0 kết quả). Hạ vế "mỗi lần đều nói thật" xuống `INFERENCE`.
4. **C-04** — dòng Blackshard: "người giữ nói" là **sai chủ thể**. Đó là tin đồn trinh sát Day 14, và
   game tự rào "At best the rumor must be only half-true." Marzeth không có thoại nào.
5. **C-05** — mis-citation: câu trích ở trang campaign `Hack and Slash`, không ở `Bashing Skulls`.
6. **C-20** — mis-citation + sai loại tier: câu ở `Unholy Alliance` §Important information (văn wiki,
   `T6`), không ở `Wrath of Sandro`. Dùng `Wrath of Sandro` Day 4 làm neo `T1*` cho việc sở hữu.
7. **C-35** — mis-citation: con số specialty nằm ở bốn trang hero, `Weakness` không có con số nào.
   Nội dung đúng, chỉ thiếu key.
8. **C-31** — `T1*` sai loại: văn ngoài template là `T6`; và `INFERENCE` phải ghi bước suy luận.
9. **C-32** — `T1*` sai loại, chứng minh bằng việc **cùng câu đó lặp nguyên văn** trên
   `Ironfist of the Ogre` và `Angelic Alliance` → boilerplate biên tập viên. Phải trình bày như
   "wiki nói X nhưng trang Orb nói ngược".
10. **C-37** — `EXPLICIT` từ im lặng → `INFERENCE`. Và bổ sung: changelog **có** thay đổi chung cho
    combination artifact chạm tới Armor (tuỳ chọn cấm ghép; bug fix danh sách cấm; text mô tả thành phần
    được thêm thông tin combo).

### Nên sửa (MINOR)

C-01 (thêm nhãn + key cho "thứ hai", tối đa `INFERENCE`) · C-02 (chữ "Expert" không có trong chuỗi
`T1`) · C-03 (thêm source key; dẫn `hota-beyond-the-horizon` làm bằng chứng săn chủ động) ·
C-22 ("không bị phá hủy" bỏ mất `region_text` "destroy the artifact… and disperse the pieces") ·
C-29 (hai trích dẫn bị cắt giữa đoạn không có dấu lược; thiếu `event` của Rib Cage) ·
C-33 (`Trivia` là `T6`) · C-38 (vế "Armor không nằm trong lệnh cấm" là `INFERENCE`) ·
C-46 ("âm thầm che lỗi" là diễn giải; và chính trang đó **có** đánh dấu một lỗi khác).

### Source key mới cần thêm vào `REGISTRY.md`

| key đề nghị | tier | nội dung |
|---|---|---|
| `sod-hack-and-slash` | T1* | Trang campaign `Hack and Slash` — `description` (nguồn của C-05) + Manual description tr.13 + mục Quest/Objective |
| `sod-unholy-alliance` | **T6** | Trang campaign `Unholy Alliance` §`Important information` — **văn biên tập viên**, nguồn của C-20 và của lời phủ nhận carry-over (C-47) |
| `h3wiki-cuthbert` | T1* | `s_text` trong `{{swh}}` — specialty Weakness, HotA 4/6/8/10 vs SoD 3/2/1 |
| `h3wiki-olema` | T1* | như trên (Heretic, Inferno) |
| `h3wiki-mirlanda` | T1* | như trên (Witch, Fortress) |
| `h3wiki-eanswythe` | T1* | ⭐ hero **chỉ có ở HotA** (`{{inhota}}`, Factory/Artificer); `s_text` **không dùng `{{swh}}`** → **xác nhận độc lập chiều đọc `{{swh}}`** |
| `h3wiki-shield-of-the-damned` | T1* | Major/Shield/6000/+6 Defense, thành phần Armageddon's Blade trong `Maker of Sorrows` — nguồn phủ định cho C-30 |
| `h3wiki-recanters-cloak` | T1* | chặn hero cast cấp 3–5; dùng cho C-50 |
| `h3wiki-cape-of-silence` | T1* | HotA, chặn hero cast cấp 1–2; dùng cho C-50 |
| `h3wiki-terrain` | T1* | `Terrain#Cursed Ground` — liệt kê đủ hiệu ứng, **không** nhắc artifact casting; dùng cho C-51/C-32 |
| `h3wiki-ironfist-of-the-ogre` | T1* | artifact HotA cast 4 spell — **bằng chứng boilerplate** cho C-32, và phản ví dụ kiểm C-36 |

Cần dùng lại (đã có trong registry, bài chưa dẫn): **`h3wiki-artraits-txt`** (`T1` thật — C-23/24/25/28),
**`hota-beyond-the-horizon`** (C-03), **`h3wiki-angelic-alliance`** (C-32, C-36).

### Lỗi của **bảng claim** (không phải lỗi bài)

- **C-33** ghi "xác nhận độc lập ở **trang thứ hai**" nhưng không nói tên trang. Đó là trang `Trivia`,
  dòng 56, mục `== Verified Statements ==` → `=== Artifacts ===`. Khi tôi grep lần đầu bằng
  `grep -o` với context dài trên wikitext nhiều template thì **không ra kết quả** và tôi gần như kết luận
  NOT_FOUND. Chỉ `grep -n` trơn mới ra. Ghi lại làm mẹo kỹ thuật: **đừng dùng `grep -o ".\{80\}…"`
  trên wikitext**, dùng `grep -n` rồi `cut`.
- **C-12** gọi là "Lần 3" mà không nói vị trí; nó là **timed event Day 30**, trả lời tin nhắn Day 21.
  Nếu bài ghi là map event thì sai loại block.
- **C-04** mô tả cột thứ hai là "người giữ nói" cho cả bốn dòng. Với Blackshard thì không có "người giữ
  nói" nào — đây là mô tả sai của bảng claim, và nó dẫn tới lỗi thật trong bài (xem C-04).
- **C-05** và **C-20**: phần mô tả của bảng claim **nói đúng** ("Mô tả campaign", "Trang campaign
  *Unholy Alliance*") nhưng cột Source key lại ghi trang scenario. Bảng claim tự tố giác mis-citation —
  nếu ai đó đọc kỹ hai cột cạnh nhau thì đã thấy.
- **Mẹo kỹ thuật trong đề bài đúng**: `Horn of the Abyss (Changelog)` là tên trang hợp lệ (201.529 byte,
  khớp registry). Bổ sung: `Anti-Magic Garrison` và `Cursed Ground` là **redirect**
  (→ `Garrison`, → `Terrain#Cursed Ground`); `Shadow of Death` redirect → `The Shadow of Death`.
  Ngoài ra `list=search` của wiki này trả 0 kết quả cho truy vấn có dấu ngoặc kép và cho `insource:`,
  nên phải dùng `list=backlinks` + fetch `action=raw` rồi grep tại chỗ.

---

## Phụ lục — xử lý sau kiểm định (người viết, 2026-08-03)

Theo `VERIFY-PROTOCOL.md` mục 5. Không có BLOCKER; toàn bộ 10 MAJOR đã xử lý.

| # | Phát hiện | Cách xử lý |
|---|---|---|
| C-25 | Câu Fandom **không phải** mô tả in-game | Thay bằng chuỗi `T1` thật từ `artraits.txt`: "All opponents have these spells effective on them for fifty turns: Slow, Curse, Weakness, and Misfortune." Thêm **bảng đối chiếu** cho thấy câu Fandom khác cả thứ tự spell lẫn chủ thể. **Bỏ `fandom-artifact-list` khỏi bài** |
| C-24 | Trường `\| effect =` không phải in-game text | Nói rõ đó là cách biên tập viên tóm tắt; giữ vế "bốn spell" vì nó khớp `artraits.txt` |
| C-08 | Thủ đoạn chỉ có ở **3/4** scenario | Sửa tiêu đề "bốn lần" → "ba lần". Trích lời Sandro ở `A Cage in the Hand` để cho thấy nó chỉ cảnh báo cản đường, không cáo buộc nói dối. Vế "mỗi lần đều nói thật" hạ xuống `INFERENCE` |
| C-04 | Dòng Blackshard sai chủ thể phát ngôn | Thêm cột **"Ai nói"** cho cả bốn dòng. Nêu rõ Marzeth **không có thoại nào**; phiên bản "thừa kế" là **tin đồn trinh sát Day 14**, và trích cả câu game tự rào: "At best the rumor must be only half-true" |
| C-05 | Source key trỏ sai trang | Đổi sang `sod-hack-and-slash` (trang campaign) |
| C-20 | Trộn hai tier vào một claim | Tách: sự kiện **sở hữu** → `T1* EXPLICIT` từ game text Day 4 mà verifier tìm được; nhận định **"map cuối không có Cloak"** → `T6` (mục *Important information*, văn biên tập viên) |
| C-31, C-32 | `T1*` sai **loại** nguồn | Hạ `T6`. Nêu bằng chứng quyết định: câu về "cái gì chặn được" lặp **nguyên văn** trên `Ironfist of the Ogre` và `Angelic Alliance` → boilerplate |
| C-35 | Con số specialty không ở trang được dẫn | Dẫn bốn trang hero. Đổi thành **bảng SoD/HotA**, và ghi lại cách xác minh chiều `{{swh}}` |
| C-37 | `EXPLICIT` từ sự im lặng | Hạ `INFERENCE`, và sửa "không có thay đổi nào" → "không có thay đổi nào **nêu tên riêng**", vì changelog **có** thay đổi chung cho combination artifact chạm tới Armor |
| Q5 | Bài tự nêu việc chưa làm | ✅ **Đóng** — trang `Talk:Artifact/descriptions` đã fetch, đúng là string table trích từ file game |

### Người sửa tự xác minh hai điểm trước khi áp

1. **Tier của `sod-hack-and-slash`.** Verifier đề nghị `T6`. Người sửa tự fetch và thấy câu đó nằm
   **trong** `{{Campaign | description = }}`, tức template parameter. Chứng cứ quyết định: mục
   `== Important information ==` của trang *Unholy Alliance* nói các **campaign description** phát biểu
   điều "**it is not true**" — tức wiki coi chúng là **văn bản do game phát ra** rồi phản bác. Vậy tier
   đúng là **`T1*`**, không phải `T6`. Đã ghi vào registry kèm cảnh báo trang này **trộn ba tier**
   (`description` = `T1*`, `Manual description` = `T2*`, `Important information` = `T6`).
2. **Chiều `{{swh}}` ở C-35.** Bảng claim đã cảnh báo đây có thể là bẫy vì cùng ngày một bài khác bị
   `BLOCKER` do đọc ngược. Verifier kết luận **bài này đọc ĐÚNG** — và mốc xác nhận rất gọn:
   **Eanswythe** là hero chỉ-có-HotA nên con số của hero đó không cần `{{swh}}`, và nó là dãy 4/6/8/10.
   Cảnh báo trong bảng claim **không** tạo dương tính giả.

### Ghi nhận điểm mạnh của bài

Bài này là bài **duy nhất trong năm bài đã kiểm không có BLOCKER**. Nó đã tự làm sẵn phần lớn công
việc phản biện: tự tìm ra **nguồn của lỗi "5 spell"** (nằm trong `{{fanopinion}}` trên chính trang
đó), tự **phản bác** claim "artifact từng thuộc về Ethric" bằng game text, và tự **ghi nhận** ba lỗi
text của scenario thay vì che chúng như wiki đã làm.

### Bốn lỗi của bảng claim, không phải của bài

Ghi lại theo quy tắc ở `VERIFY-PROTOCOL.md` mục 7:

1. **C-04** — người soạn đặt tiêu đề cột là "người giữ nói" cho cả bốn dòng, trong khi dòng Blackshard
   không có người giữ nào phát ngôn. Bài gốc cũng có lỗi này, nên nó vừa là lỗi bài vừa bị bảng claim
   chép lại.
2. **C-05** và **C-20** — người soạn **mô tả đúng** ("mô tả campaign", "trang campaign *Unholy
   Alliance*") nhưng cột *Source key* lại ghi key scenario. Mâu thuẫn nội bộ trong chính bảng claim.
3. **C-12** — người soạn ghi là "map event", thực tế là **timed event Day 30**.

### Trạng thái

`status: draft` → **`status: verified`**. `verify_pass: verify-armor-of-the-damned-2026-08-03`.

Không còn BLOCKER, không còn MAJOR.
