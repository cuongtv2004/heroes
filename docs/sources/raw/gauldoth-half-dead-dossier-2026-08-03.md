# Dossier research thô — `gauldoth-half-dead` (Gauldoth Half-Dead)

- **Ngày:** 2026-08-03
- **Loại:** dossier thô, KHÔNG xuất bản (nằm trong `sources/raw/`)
- **Phạm vi đã làm:** PRIORITY 1 ✅ · PRIORITY 2 ✅ (một phần — stat block chỉ có 1 nguồn) · PRIORITY 3 ✅ · PRIORITY 4 ✅
- **Entity:** nhân vật chính campaign *Half-Dead* (Death/Necropolis) của Heroes IV, kỷ nguyên **Axeoth**

## Cách fetch (môi trường)

Bash tool ở đây là **Git Bash trên Windows**, `python3` **không tồn tại** ở đó. Phải chạy
xuyên qua WSL:

```
wsl.exe -d Ubuntu -e bash -lc '<lệnh>'
```

Ghi chú access đã kiểm trong phiên này:

- `web.archive.org` **VÀO ĐƯỢC** với `curl -sL` + timestamp đầy đủ. Xác nhận lại ghi chú mới.
- CDX API vào được; để lọc theo đuôi file dùng
  `...&matchType=prefix&filter=original:.*\.shtml.*&limit=400`.
- `heroes.thelazy.net` **CẦN User-Agent** — không có UA thì trả 0 byte im lặng. Xác nhận lại.
- Fandom `api.php?action=parse&...&prop=wikitext` OK.
- `python3` có trong WSL; chuyển RTF → text bằng script tự viết `/tmp/rtf2txt.py`.

---

## ⚠️ SỬA GHI CHÚ ACCESS — `heroesofmightandmagic.com` KHÔNG phải site chính thức

Prompt research ghi domain này là *"Site CHÍNH THỨC của New World Computing … tier T2"*.
**Điều đó SAI.** Footer của chính các trang đã fetch ghi nguyên văn:

> "Age of Heroes and Heroes Community are copyrighted ©2005 Valera Koltsov."
> "Age of Heroes is copyrighted ©1999-2006. Unauthorised reproduction is prohibited."
> — footer `campaign_halfdead.shtml`, `campaigns.shtml`, `heroes_necromancers.shtml`

Breadcrumb đầu trang cũng ghi `Age of Heroes: Heroes of Might and Magic 4:`. Và
`heroes_necromancers.shtml` cảm ơn *"Lich (Guardian's Grove Admin, Heroes Community
Moderator) for heroes data and images"* — tức **dữ liệu do fan biên soạn**.

→ Đây là **fansite Age of Heroes (AoH)**, không phải nhà phát hành. Đề nghị tier **T3**
(fansite biên soạn, chép lại text in-game nhưng có lỗi chép — chứng minh ở §1.8), **không
phải T2**. Nếu registry đã ghi T2 cho domain này thì phải sửa.

**Bằng chứng cụ thể AoH chép sai:** `campaigns.shtml` ghi
`"including must of his humanity"` — trong khi transcript CH và Fandom đều ghi
`"including most of his humanity"`. AoH có lỗi chính tả do chép tay.

---

## ⭐⭐ PHÁT HIỆN LỚN NHẤT — transcript ĐẦY ĐỦ text in-game của campaign

Fandom trích dẫn mọi claim cốt truyện H4 về một nguồn duy nhất:
`http://www.celestialheavens.com/viewpage.php?id=763`. Truy được qua Wayback:

- Trang index: `https://web.archive.org/web/20130117072816/http://www.celestialheavens.com/viewpage.php?id=763`
  → **FETCHED**, 31.476 byte. Tiêu đề **"Heroes IV Text Collection"**, by Kalah.
  Văn nguyên văn trên trang:

  > "Here is a collection of all the storyline texts from Heroes IV's six main campaigns,
  > collected by **Corlagon** and and Zamfir, and put into .RTF format for your viewing
  > pleasure."

  (chữ "and and" là nguyên văn trên trang, không phải lỗi của tôi)

- File Death campaign: `https://web.archive.org/web/20130117072816/http://www.celestialheavens.com/homm4/texts/H4-DeathTexts.rtf`
  → **FETCHED**, **89.002 byte RTF** (81.666 ký tự sau khi convert), **1.233 dòng**.
  `file` xác nhận: `Rich Text Format data, version 1, ANSI, code page 1252`.

Đây là **toàn bộ text kể chuyện của campaign Half-Dead**: 5 scenario description, 5 đoạn
monologue mở màn, **54 block sự kiện** (`==Tên block==`), gồm cả **5 block `Quest:`** có
đủ ba trạng thái `Proposal` / `Progress` / `Completion` — tức là **region text và timed
event**, đúng thứ BH-1 nói phải đọc. Không chỉ prologue/epilogue.

**Đề nghị tier `T1*`** — cùng loại với các nguồn thelazy trong registry: text in-game
verbatim, tiếp cận qua trung gian fan, không phải file game gốc. Bằng chứng độ trung
thực: transcript giữ cả lỗi/dị bản mà bản AoH đã sửa hoặc làm sai (xem §1.8), và giữ
nguyên xưng hô ngôi thứ nhất/thứ hai theo đúng cách game phân biệt (§1.7).

**Danh sách 54 block sự kiện** (theo thứ tự trong file, số dòng trong bản convert):

```
Scenario 1: Gauldoth(15) · Full Circle(55) · The Past(77) · Bandit Ambush(89) ·
            Halas(111) · Vengeance(117) · Survival(123) · Vitross Captured(131)
Scenario 2: Fire!(179) · The Kreegans(191) · The Crusader(225) · Politics(235) ·
            Refusal(257) · Taking Action(285) · Philosophy(289) · To Survive(301) ·
            Quest: Bone Dragons(337) · Quest: The Angel's Blade(350) ·
            Quest: The Nexus Point(366) · The Fiery Realm(382) · Kalibarr(386)
Scenario 3: Nekorrum(414) · Kreegan Rebellion(426) · Quest: First Point of Power(464) ·
            Enric's Demise(480) · Alana(526) · Quest: Second and Third Points of
            Power(568) · Creation and Destruction(582) · Pleasant Company(634) ·
            Quest: Fourth Point of Power(662) · Suraze(704) ·
            Quest: Fifth Point of Power(708)
Scenario 4: Masters(770) · Malvich(794) · Messenger(828) · Hadrin(846) ·
            The Life Shield(876) · Malvich Enraged(880) · Quest: Shrine of
            Korbert(892) · Children(950) · Life and Death(978) ·
            The Deadwood Staff(984)
Scenario 5: Death(1014) · The Plane of Death(1028) · The Unholy Breath(1068) ·
            Real World(1076) · Directions(1104) · Rija(1108) · Hadrin's Welcome(1112) ·
            Hadrin's Stand(1126) · Drastic Measures(1132) · Quest: Suraze(1150) ·
            Hadrin's Fate(1188) · Hadrin Stands Again(1196) ·
            Kalibarr Defeated(1208) · Epilogue(1214)
```

---

# PRIORITY 1 — campaign *The Half-Dead*

Hai nguồn độc lập cho cùng nội dung: AoH (6 trang, có metadata scenario) và CH transcript
(text đầy đủ, không có metadata). **Đối chiếu chéo hai bên đã làm.**

URL AoH đã fetch (đủ **cả sáu** trang, mỗi trang là một snapshot khác nhau):

| trang | timestamp Wayback | byte |
|---|---|---|
| `campaign_halfdead.shtml` | `20060118021947` | 12.892 |
| `campaign_halfdead2.shtml` | `20071102140229` | 17.956 |
| `campaign_halfdead3.shtml` | `20070808181955` | 18.033 |
| `campaign_halfdead4.shtml` | `20070808032934` | 18.110 |
| `campaign_halfdead5.shtml` | `20061209093603` | 18.208 |
| `campaign_halfdead6.shtml` | `20070811121343` | 17.406 |

Mẫu URL: `https://web.archive.org/web/<ts>/http://www.heroesofmightandmagic.com/heroes4/<file>`

⚠️ **Trang thứ 6 KHÔNG phải scenario 6.** Nó tên `Conclusion`. Campaign có **5 map**,
trang 6 là kết. Nav trên trang xác nhận: `1. Eater of Children / 2. The Fiery Realm /
3. The Points of Power / 4. Life and Death / 5. The Unholy Breath / 6. Conclusion`.
`campaigns.shtml` cũng ghi `Number of Maps: 5`.

## 1.1 Scenario 1 — Eater of Children

**Metadata (AoH, `campaign_halfdead.shtml`, nguyên văn):**

> **Map Difficulty:** Advanced.
> **Map Size:** Small, with underground.
> **Victory Condition:** Capture Vitross.
> **Loss Condition:** Lose Gauldoth Half-Dead.
> **Carryover:** Gauldoth and all of his spells, skills, and experience will transfer to
> the next map. All of your heroes have a maximum level of 12.

**Monologue mở màn — GAME TEXT, ngôi thứ nhất** (HTML AoH đặt trong `<i>`; transcript CH
đặt dưới nhãn `Gauldoth Half-Dead:` trong ngoặc kép → **hai nguồn khớp từng chữ**):

> "Can you go years without talking to another human being? What about untold months
> snatching your meals from the forest floor and sleeping in muddy pits? Sanity is a
> spider clinging to a fluttering thread of web unaware of the fingers reaching for it,
> catching it, plopping it in my mouth..."

**Scenario description — GAME TEXT** (AoH để ngoài `<i>`; transcript CH đặt ngay sau
`Scenario 1: Eater of Children` → khớp từng chữ):

> "Alone in this new world for years, Gauldoth has lived like an animal in the wilderness.
> When some farmers catch him and try to burn him at the stake, Gauldoth barely escapes
> into the forest. Soon, rage and fear give birth to a new sense of purpose. Gauldoth
> raises a small army of his own and embarks on a quest for knowledge as well as revenge."

## 1.2 Scenario 2 — The Fiery Realm

> **Map Difficulty:** Advanced.
> **Map Size:** Medium, with underground.
> **Victory Condition:** Rescue Kalibarr.
> **Loss Condition:** Lose Gauldoth Half-Dead.
> **Carryover:** … All of your heroes have a maximum level of 18.

Monologue (GAME TEXT):

> "In the scope of the Universe, we are but a single breath. To say we're insignificant is
> to give us too much credit. But when the Universe chooses you to be part of its plan,
> you'd better hold on and take what you can get because your ride will surely be over
> before you know it!"

⚠️ **Dị bản:** AoH ghi `"to be part of its plan"`; transcript CH ghi
`"to be a part of its plan"` (thêm chữ **a**). Fandom `Qlisten` chép theo bản AoH
(`to be part of`). Ba nguồn, hai dị bản. Không có file game gốc để phân xử → nếu trích
câu này trong bài, ghi rõ dị bản hoặc trích ngắn hơn.

Scenario description (GAME TEXT, hai nguồn khớp):

> "A startling vision from another realm informs Gauldoth that his Master, Kalibarr, didn't
> perish during the Reckoning. Now, he must battle crusaders and demons to find a way to
> reach this otherworld and rescue the one who saved his life long ago."

## 1.3 Scenario 3 — The Points of Power

> **Map Difficulty:** Advanced.
> **Map Size:** Medium, no underground.
> **Victory Condition:** Flag 5 points of power.
> **Loss Condition:** Lose Gauldoth Half-Dead.
> **Carryover:** … maximum level of 24.

Monologue (GAME TEXT) — ⚠️ **dị bản, quan trọng vì Fandom dựa vào đây:**

- AoH: `"…then why is lifeblood of creation - water - the most destructive force on the planet?"`
- CH transcript: `"…then why is **the** lifeblood of creation - water - the most destructive force on the planet?"`

Bản CH đúng ngữ pháp hơn; bản AoH thiếu `the`. Đoạn đầu khớp cả hai:

> "Why can't everyone see the inherent goodness in destruction? Or the evil in creation?
> A forest cannot live without the nutrients provided by the destructive force of a forest
> fire."

Scenario description (GAME TEXT):

> "In an attempt to restore his master's power, Gauldoth sets out to do the impossible -
> activate all five Points of Power. But this isn't the best time to be away from home with
> the Kingdom of Nekross in the middle of a demon rebellion."

## 1.4 Scenario 4 — Life and Death

> **Map Difficulty:** Advanced.
> **Map Size:** Medium, with underground.
> **Victory Condition:** Defeat Malvich.
> **Loss Condition:** Lose Gauldoth Half-Dead.
> **Carryover:** … maximum level of 30.

Monologue (GAME TEXT, hai nguồn khớp):

> "So, what is the point if I am but an insignificant pawn of the Universe?
>
> Knowledge! To know the Universe is to transcend it. Destruction, creation, good, and
> evil; the grand scheme of things they are just the masks we use to understand that which
> we cannot grasp. Well, here is my hand. Show me your secrets. I am not afraid!"

(Câu "the grand scheme of things they are just the masks" thiếu chữ *in* — **cả hai nguồn
đều ghi y như vậy**, nên đây khả năng cao là lỗi trong game, không phải lỗi chép. Nếu
trích, dùng `{{sic}}`-style ghi chú.)

Scenario description (GAME TEXT):

> "A powerful vampire and former supporter of Nekross named Malvich has riled the anger of
> Kalibarr. So, Gauldoth has been sent on a mission not only to kill the offender, but also
> to retrieve the bloodsucker's most prized possession, the unique and supremely unholy
> Deadwood Staff."

## 1.5 Scenario 5 — The Unholy Breath

> **Map Difficulty:** Expert.
> **Map Size:** Small, with underground.
> **Victory Condition:** Defeat Kalibarr and take Nekorrum.
> **Loss Condition:** Lose Gauldoth Half-Dead and Defeat the map before Month 4.

⚠️ Dòng Loss Condition trên AoH viết **lủng củng** ("Lose … and Defeat the map before
Month 4") — nghĩa thật là *thất bại nếu không thắng trước Tháng 4*. **Không trích nguyên
văn dòng này như thể là text in-game.** Con số "Month 4" khớp với game text: nameless one
ra lệnh Kalibarr chờ 3 tháng (§3.5). ⚠️ Trang 5 **không có dòng Carryover** — đây là map
cuối nên hợp lý, nhưng ghi rõ là *không có*, không phải *chưa đọc*.

Monologue (GAME TEXT):

> "A worm knows one thing with complete faith. Eat to live. Whether it's moldy dirt or
> rotten flesh, that worm digs and eats, eats and digs to fulfill its one truth. Eat to
> live.
>
> But I hold one now in my Undead fingers. It squirms, fighting to free itself. What is it
> thinking? When I pop it in my mouth and chew its pink flesh, does it realize that you
> should NEVER place all your faith in one ideal?"

Scenario description (GAME TEXT) — ⚠️ dị bản chữ hoa:

- AoH: `"In three months time, the **Stars** will be in alignment…"`
- CH: `"In three months time, the **stars** will be in alignment…"`

> "Gauldoth is forced to betray his beloved master, Kalibarr, when he learns that the lich
> actually serves a malicious god of death determined to destroy every living being on this
> new world. In three months time, the stars will be in alignment and Kalibarr will be able
> to forge the Unholy Breath, an artifact with the power to destroy all living flesh. For
> the sake of the entire world, and for his own survival, Gauldoth must stop him."

## 1.6 Conclusion (trang 6 AoH = block `==Epilogue==` + monologue kết trong transcript)

Monologue kết (GAME TEXT, hai nguồn khớp):

> "I have struggled to understand a Universe that allows the destruction of an entire
> planet. Which will win this endless conflict - destruction or creation? The only thing I
> know for certain is never to place your faith entirely on one side. Play the middle if
> you want to survive.
>
> Everyone else is a fanatic.
>
> I am Gauldoth Half-Dead. Your savior."

Epilogue (chỉ có trong transcript CH, **AoH KHÔNG có** — bằng chứng transcript đầy đủ hơn):

> "I, Gauldoth, was greeted like a hero when my army rode through Nekorrum's black gates.
>
> "Half-Dead! Half-Dead!" they screamed.
>
> The human inhabitants of the city called me 'Protector' and 'Father Gauldoth' because I
> brought their children home. […] I ordered the child pens to be destroyed, and then I
> started repairs on the siege-damaged city. There was a lot of work to be done, but this
> was my city. I know now I never should have given it to Kalibarr.
>
> I am Gauldoth Half-Dead, King of Nekross! And I plan to stay this way."

## 1.7 Tổng quan campaign (AoH `campaigns.shtml`, ts `20060118021016`)

> "Gauldoth lost everything when the world was destroyed, including must of his humanity.
> After a powerful spell goes wrong, it leaves Gauldoth in a state of constant contradiction.
> Half of his body is living, while the other half is Undead. As necessity forces Gauldoth
> to carve out a small portion of this new world for himself, his destiny becomes
> intertwined with that of a malevolent being from another realm determined to bring an end
> to all life in the Universe.
>
> Number of Maps: 5
> Map Difficulties: Advanced x4, Expert.
> Map Sizes: S+U, M+U, M, M+U, S+U."

(`must` là lỗi AoH — CH và Fandom đều ghi `most`.)

**Thang độ khó H4 suy ra từ cùng trang này:** Novice / Intermediate / Advanced / Expert
(các campaign khác dùng `Novice x2, Intermediate x3` v.v.). Không có mức "Hard" — xem
mâu thuẫn ở §5.

## 1.8 Ba dấu hiệu cho thấy transcript CH đáng tin hơn AoH

1. AoH có lỗi `must` ↔ CH có `most`.
2. AoH thiếu chữ `a` / `the` ở hai monologue; CH có.
3. AoH **không có** epilogue và **không có** 54 block sự kiện; CH có đủ.
4. CH giữ nguyên **sự phân biệt ngôi**: block ngôi thứ nhất (Gauldoth kể — journal in-game)
   vs. block ngôi thứ hai `"You spot a naked corpse…"` (region/quest text mô tả người
   chơi). Ví dụ `==Kalibarr==` và cả 5 block `Quest:` đều ngôi thứ hai. Đây là dấu hiệu
   chép trung thực theo đúng cách game phân loại text.

---

# PRIORITY 2 — Gauldoth là ai, thông số hero

## 2.1 Class / alignment

**GAME TEXT gián tiếp + AoH:** Gauldoth nằm dưới đề mục `Campaign Necromancers` trong
`heroes_campaign.shtml` (ts `20060118010939`, 31.882 byte, **FETCHED-VÀ-ĐỌC**). Campaign
của hắn là **Death/Necropolis campaign**.

**Fandom `Necromancer (H4)` (T5, FETCHED):**

> "The '''Necromancer''' is the basic magic class of the Necropolis faction in ''Heroes of
> Might and Magic IV''. It starts with Basic Death Magic and Basic Occultism. Its might
> counterpart is the Death Knight."

**AoH `heroes_necromancers.shtml` (ts `20060118010443`, 24.958 byte, FETCHED) — số liệu
gameplay, phạm vi phiên bản KHÔNG được nêu trên trang (xem GAPS):**

> "Necromancers start with Basic Death Magic and Basic Occultism.
> Necromancer hero cost in Necropolis is 1500 Gold.
> Necromancer hero cost in Tavern, Academy and Asylum is 2000 Gold.
> Necromancers cannot be hired in Haven, Stronghold and Preserve."

⚠️ **Lỗi trên AoH:** heading trang ghi `Death/Necropolis **Might** Heroes - Necromancers`.
Necromancer là **magic** class (might class của Death là Death Knight). Đây là lỗi
copy-paste của fansite. Đừng chép heading đó.

⚠️ **KHÔNG có "specialty".** Heroes IV **không dùng cơ chế hero specialty** như H3 — không
nguồn nào tìm được gán specialty cho Gauldoth. Nếu bài viết nêu specialty thì đó là bịa.

## 2.2 Chỉ số / stat block — CHỈ CÓ MỘT NGUỒN

Nguồn duy nhất tìm được: Fandom `Gauldoth`, template `HeroSkills` (T5, **không dẫn nguồn**):

```
|caption = Gauldoth's stats in Eater of Children
|level = 2
skills:  Basic Death Magic · Basic Occultism · Basic Nature Magic
spells:  Curse · Summon sprite
```

- Chỉ cho **scenario 1** (Eater of Children), **bản H4 gốc** (Fandom `|version = H4`).
- Không có Attack/Defense/Spell Power/Knowledge, không có movement, không có stat cho 4
  scenario sau.
- **Corroboration một phần từ GAME TEXT:** `Basic Nature Magic` khớp với text in-game —
  Gauldoth tự nói *"Through my studies of Nature Magic, I have learned to see these lines
  of magic"* (`==The Crusader==`) và *"Is it really a contradiction for a necromancer to
  embrace Nature? I don't think so."* (`==Survival==`). Spell `Slow` cũng khớp: block
  `==Gauldoth==` kể hắn cast spell *"send an unearthly chill into the muscles of everyone
  present, slowing their movement"* — nhưng Fandom **không** liệt Slow trong spell khởi đầu.
  ⚠️ Đây là **mâu thuẫn nhỏ**: game text cho thấy spell hắn dùng khi thoát giàn thiêu là
  Slow, nhưng đó là **cutscene trước khi map bắt đầu**, nên có thể không phải spell khởi đầu.
  Đừng gộp hai chuyện.
- ⚠️ `Summon sprite` là spell **Nature Magic**, phù hợp với Basic Nature Magic. Nhưng lưu ý
  block `==Halas==` nói Halas gửi thư *bằng* một Sprite → có thể là nguồn cảm hứng thiết kế,
  **không suy diễn**.

**Level cap theo scenario (AoH, T3, bản H4 gốc):** 12 → 18 → 24 → 30 → (không ghi).

**Yêu cầu level trong game (GAME TEXT, `==Quest: The Angel's Blade==`):**

> "The one known as Gauldoth Half-Dead can have it, but only after he reaches 18th level,"
> the demon says.

## 2.3 ⭐ Cơ chế "Half-Dead" — GAME TEXT giải thích đầy đủ

Đây là điểm định danh nhân vật, và **có text tường minh**, không cần suy đoán.

**Nguồn gốc (block `==The Past==`, GAME TEXT, ngôi thứ nhất):**

> "I owed Kalibarr my life, but in the end, I failed to return the favor. During the first
> hours of the Reckoning, I returned to the Necromantic Order's secret library to find it on
> fire. Kalibarr lived within. I tried to find him, but the fire was too great.
>
> Naked and with burns that would soon claim my life, I opened a scroll that was far beyond
> my power. I was dying. I could feel my scorched lungs slowing, unable to take another
> breath. So, I read the words on the ancient parchment. It was my last chance.
>
> I lived, of course. At least, part of me was still alive. The rest was undead. I had a
> foot in both worlds now - living and dead - but I didn't feel part of either."

**Nửa nào là nửa nào — GAME TEXT xác nhận PHẢI = chết, TRÁI = sống.** Bảy chỗ độc lập:

| block | nguyên văn |
|---|---|
| `==Gauldoth==` | "Then a pitchfork pierced my **right** shoulder." |
| `==Gauldoth==` | "I felt the skin of my **dead right hand** come loose" |
| `==Bandit Ambush==` | "I reached up with my **dead right arm** and grabbed his wrist." |
| `==Bandit Ambush==` | "closed my **right hand** around his neck… **My undead flesh is far stronger that it appears**" (chữ `that` thay `than` — nguyên văn cả nguồn) |
| `==To Survive==` | "I tattooed Mardor's name on the **living skin of my left arm**." |
| `Quest: Fifth Point` | "I brushed Alana's warm cheek with the soft, **living fingers of my left hand**" |
| `==Hadrin==` | "The zombie's **left arm** was missing… It was no coincidence that **my living arm was my left**. It was a threat." |
| `Quest: Fourth Point` | "You are right handed. You have always touched the crystal with your **dead right hand**." |

→ Claim "nửa phải undead, nửa trái người sống" là **EXPLICIT game text**, không phải suy
diễn từ infobox Fandom.

**Hệ quả cơ chế (GAME TEXT):**

- Nửa sống vẫn cần ăn: `==Gauldoth==` — *"The part of me that still requires sustenance
  hungers for what normal people eat - a juicy piece of beef or perhaps some salmon grilled
  over a wood fire. The rest of me - the undead half - hungers for nothing. That half is
  empty."*
- **Chưa từng ăn thịt/uống máu người:** *"To this day, I still have not tasted human flesh,
  or blood either."* — phủ định biệt danh "Eater of Children".
- Nửa undead khỏe bất thường (bóp vỡ cổ tên cướp).
- **Nửa sống là điểm yếu:** `==The Unholy Breath==` — *"if I don't find the portal back to
  Nekorrum soon, I think the living half of my body will finally succumb to this realm's
  life-draining effects."* Và Alana phải chữa hắn sau khi ice demon làm nửa sống mất máu.
- Nửa sống là **lý do hắn phải chặn Kalibarr:** *"Obviously, it will kill every living
  thing on the planet - **including me**!"*
- Sợ lửa: *"Fire! I had reason to fear it. A fire was responsible for my half-dead
  condition."*
- Chưa từng được phụ nữ chạm: `Quest: Fifth Point` — *"I had never felt the touch of a
  woman's lips before"*.

## 2.4 Bio chính thức (AoH `heroes_campaign.shtml`) — phân biệt hai loại văn trên cùng trang

Trang này có **hai loại văn khác nhau**, phải tách:

**(a) `Biography:` — văn sạch, giọng nhà phát hành, khả năng cao là bio in-game/manual
(nhưng CHƯA xác minh được là in-game):**

> "**Gauldoth Half-Dead - Male Human / Undead**
> Biography: Gauldoth's earliest memory is the bite of a vampire. During the Reckoning, a
> fire consumed most of his body, and due to an errant spell he was made into a
> contradiction both in body and spirit. He is half-living and half-undead, endlessly
> seeking to understand what kind of universe would create a being such as him.
> History: New"

→ Fandom chép **đúng nguyên văn đoạn này** trong template `{{text|…}}` (= scenario/bio
description in-game theo quy ước Fandom). Hai nguồn độc lập khớp từng chữ → **đề nghị coi
là in-game bio, T1\* nếu editor đồng ý**; nếu không thì T3.

`History: New` = nhân vật mới, không xuất hiện ở game trước. (So sánh: Sandro có
`History: Since Strategic Quest (Homm1)…`)

**(b) `Part in:` — văn fansite, ĐẦY LỖI, KHÔNG được dùng làm nguồn:**

> "Part in: Half-Dead (Original Homm4 Death Campaign). He is the main characters and takes
> part in all maps… An accident turned **Galdoth** into half undead entity… Quite a
> **phylosophic** individual… whom he gave this new kingdom as a present… This campaign is
> the most interesting and thoughtful campaign there was in Heroes."

Lỗi chính tả tên riêng (`Galdoth`), lỗi ngữ pháp, và câu cuối là **ý kiến fan**. Đây là
**văn wiki/fansite**, tier T3 cao nhất, và phần đánh giá là opinion.

---

# PRIORITY 3 — Axeoth, Reckoning, quan hệ

## 3.1 Reckoning — Gauldoth liên quan thế nào

**GAME TEXT** (`==The Past==`, `==Gauldoth==`, `==Full Circle==`):

- Gauldoth **ở Enroth khi Reckoning xảy ra**, trong "Necromantic Order's secret library".
- Hắn **thoát qua portal sang Axeoth** — text không nói portal trực tiếp, nhưng nói:
  *"The Reckoning destroyed nations, armies and even ancient societies like the Necromantic
  Order, but I survived."* và *"Alone in this new world for years"*.
  ⚠️ **Chi tiết "đi qua portal cùng những người tị nạn khác" là văn Fandom, KHÔNG có trong
  transcript.** Xem §5.
- Reckoning giết Kilgor — GAME TEXT, `==Creation and Destruction==`:
  > "Take the Reckoning - the greatest example of a destructive force that I can think of.
  > I can argue that it probably did as much good as evil. For one, the Reckoning claimed
  > the life of that Barbarian scum, Kilgor."
  → **liên kết trực tiếp sang Kilgor (H3 Armageddon's Blade).**
- Sandro được nêu tên — GAME TEXT, `==Philosophy==`:
  > "When others like the powerful necromancer, **Sandro**, sought to control the world, the
  > force of destruction supported them temporarily. Then, for lack of a better description,
  > it changed its mind."
  → **liên kết trực tiếp sang entity `sandro` đã verified trong Codex.** Đây là chỗ nối
  Enroth ↔ Axeoth mạnh nhất tìm được.

**Ngày Reckoning (T5, thelazy `The_Reckoning`, FETCHED 13.958 byte):**

> "On February 10th, 1177 AS, a massive explosion is created by the clash of Gelu's
> Armageddon's Blade and Kilgor's Sword of Frost…"

Wiki tự dẫn nguồn là `Lost Manuscripts#11-08-1178`. **Chưa fetch `Lost Manuscripts`** →
ngày này là **T5 chưa xác minh tận nguồn**.

**Lịch:** cả thelazy và Fandom **tiếp tục dùng `AS`** cho Axeoth (Fandom: `birth = ~ 1100s
AS`, `years = ca 1180s AS`). **Không tìm được nguồn nào nói Axeoth dùng lịch khác.** Nhưng
campaign Half-Dead **không có một mốc tuyệt đối nào** — mọi mốc là tương đối (xem TIMELINE).

## 3.2 Kalibarr — quan hệ chủ/tớ, và cái chết

**Bio (AoH `heroes_campaign.shtml`, mục `Campaign Necromancers`):**

> "**Kalibarr - Male Lich**
> Biography: Kalibarr is the lich necromancer who rescued Gauldoth from the crypts, making
> him his protege. As awesomely powerful as he is, Kalibarr's name is relatively unknown
> even among other necromancers.
> History: New"

**GAME TEXT — Kalibarr cứu Gauldoth khỏi vampire Loscan (`==The Past==`):**

> "My Master, Kalibarr, told me once that he had seen a power within me that couldn't be
> wasted, but Loscan, the vampire who kept me for his own, wouldn't release me even when
> Kalibarr offered him ten young children as a replacement. Since Loscan was a member of the
> Necromantic Order, Kalibarr's hands were tied. He couldn't force Loscan to turn me over,
> so he arranged for a holy crusader to learn the location of the vampire's crypt. That was
> the end of Loscan."

**GAME TEXT — Gauldoth từng là sát thủ cho Kalibarr (`==Vengeance==`):**

> "all my Master's actions were part of his plan to one day seize control of the Necromantic
> Order. I know from personal experience that he also had a strong sense of vengeance.
> Whenever someone crossed him, he usually had me slip poison in their wine or a dagger
> between their ribs."

**GAME TEXT — Gauldoth TỰ NGUYỆN nhường ngôi (`==Nekorrum==`):**

> ""It's all yours," I told my Master when we completed the tour. […] Master Kalibarr was
> silent for some time. He leaned on me for support, still too weak to exert himself for any
> length of time, and said, "It's a start.""

**GAME TEXT — Kalibarr bóp cổ Gauldoth (`==Malvich==`):**

> ""Malvich means nothing to me, Gauldoth, because **Nekross means nothing to me**! Bring me
> the Deadwood Staff or I will find someone else to serve me!""

**GAME TEXT — cảm xúc sau khi giết (`==Kalibarr Defeated==`):**

> "I try to muster the anger that is rightfully mine, but I cannot think badly about my
> former master. Kalibarr was my savior, a teacher and master to me for so many years he
> seemed more like family. Now, he is gone. Destroyed. And I am alone.
>
> I like to think that he really died during the Reckoning - not by my hand. It's easier
> that way."

## 3.3 "Nikolai" — KHÔNG có nhân vật tên Nikolai trong campaign

Prompt yêu cầu kiểm `Nikolai`. **Kết quả: grep transcript 89 KB → 0 hit cho `Nikolai`,
`Nicolai`, `Nicolas`.** Không nhân vật nào tên đó xuất hiện trong campaign Half-Dead.

Tên gần nhất là trong **infobox Fandom** (T5): `Nicolas Gryphonheart (father)` và
`Nicolai Ironfist (nephew)`. Cả hai đến từ chuỗi suy luận huyết thống ở §4.1 — **không
phải từ game**. Xem mâu thuẫn §5.

## 3.4 Danh sách nhân vật campaign nêu tên (tất cả từ GAME TEXT transcript)

| tên | vai | ghi chú nguồn |
|---|---|---|
| **Kalibarr** | lich, thầy rồi phản diện chính | AoH có bio riêng |
| **Loscan** | vampire giam Gauldoth thời bé | chỉ nêu trong `==The Past==` |
| **Sir Mardor** | chỉ huy Vitross → bị thiêu → **ghost làm phó tướng** | AoH không có bio |
| **Captain Enric** | thuộc cấp Mardor → phản Mardor → vampire → bị Gauldoth xử tử | GAME TEXT `==Enric's Demise==` |
| **Halas** | druid canh rừng, gửi thư đe dọa | `==Halas==` |
| **Alana** | priestess Life Magic; **chết khi kích hoạt Point of Power thứ 5** | `==Alana==`, `Quest: Fifth Point` |
| **Suraze** | demon lãnh đạo phản loạn → sau liên minh, đòi làm "Duke Suraze" | AoH có bio (dưới `Campaign Death Knights`) |
| **Malvich** | vampire giữ Deadwood Staff, đồng minh cũ | `==Malvich==` |
| **Hadrin** | dân thường tình nguyện chết → zombie một tay → bodyguard/captain | `==Hadrin==` |
| **Rahjuu** | Kreegan canh xác Kalibarr ở Fiery Realm | **CHỈ có ở Fandom**, transcript block `==Kalibarr==` KHÔNG nêu tên → xem §5 |
| **Korbert** | "Benevolent Sir Korbert", bị Gauldoth hồi sinh để giết đám monk | `Quest: Shrine of Korbert` |
| **Queen Emilia Nighthaven** | vua Great Arcan; Gauldoth **gửi bản đồ cảnh báo** | `==Politics==`, `==To Survive==` |
| **"the nameless one"** | thực thể ở Plane of Death, chủ của Kalibarr | §3.5 |
| **Kilgor** | nêu tên như người chết trong Reckoning | `==Creation and Destruction==` |
| **Sandro** | nêu tên như tiền lệ necromancer thất bại | `==Philosophy==` |

**AoH bio Suraze (mục `Campaign Death Knights`):**

> "Suraze is an ancient and charismatic demon who has seen the destruction of two worlds and
> has come to realize that he has nothing to show for it. No longer motivated by causing
> havoc, Suraze now wants wealth and power (and perhaps the occasional war)."

## 3.5 Vị thần chết — GAME TEXT KHÔNG ĐẶT TÊN

⚠️ Quan trọng: Fandom có trang tên `God of Death`. Nhưng **trong game text, thực thể này
luôn được gọi là "the nameless one" / "the dark one" / "Master"**. Grep transcript:
`nameless` = 5 hit, `god of death` = **1 hit duy nhất**, và hit đó nằm trong **scenario
description** (*"a malicious god of death"*, chữ thường, danh từ chung), không phải tên
riêng.

GAME TEXT (`==The Plane of Death==`):

> ""Wait for the Convergence, for the planets to align," said the nameless one. […] "Only
> then do you forge this to the Deadwood Staff." […]
> "I have visited the remains of your former world, Kalibarr. I have seen the rubble of
> ancient cities, the bones of those who couldn't make it through those annoying portals!
> So much gone. It was beautiful! But it's a pity so many escaped my reach." […]
> "Now, go, Kalibarr! Return to your world, and in three months when the Convergence comes,
> release the Unholy Breath. Then they will learn there is no escape! When their living
> flesh melts into a putrid ooze, then they will know oblivion!""

→ Nếu Codex viết "God of Death" như **tên riêng**, đó là quy ước wiki, không phải game.

## 3.6 Có xuất hiện ngoài campaign của hắn không? — SĂN CHỦ ĐỘNG, ba kết quả

**(a) Expansion The Gathering Storm / Winds of War → KHÔNG.** Đã fetch và grep 4 trang AoH:

| trang | ts | byte | `grep -ci gauldoth` |
|---|---|---|---|
| `heroes4/tgs_campaigns.shtml` | `20060118011028` | 16.282 | **0** |
| `heroes4/tgs_heroes.shtml` | `20060118011603` | 16.408 | **0** |
| `heroes4/wow_campaigns.shtml` | `20060118012311` | 15.442 | **0** |
| `heroes4/wow_heroes.shtml` | `20060118002209` | 16.903 | **0** |

TGS có cast hoàn toàn khác (Dogwoggle, Alita, Hexis…). **Có nguồn T4 độc lập chống lưng
claim phủ định này** — xem §4.2.

**(b) ⭐ CÓ xuất hiện: Heroes IV Card and Tile Game.** Đây là phát hiện mới, prompt không
yêu cầu. AoH `heroes4card/heroesnecromancers.shtml` (ts `20070812172340`, 25.937 byte,
FETCHED) có card `3_Necromancer_Gauldoth.jpg` trong danh sách 28 card
`Necromancers - Magic Heroes of Death Alignment`. Kalibarr và Sandro cũng có card. Footer:

> "Card and tile images have been exclusively provided to Age of Heroes by **DGA Games** and
> may not be copied or reproduced."

→ Gauldoth là **magic hero card của Death alignment** trong board/card game do DGA Games
làm. ⚠️ **Chỉ có tên file ảnh + vị trí trong bảng**; **KHÔNG đọc được text/stat trên card**
(là ảnh JPG, và bản archive chỉ có thumbnail 104×141). Không claim gì về nội dung card.

**(c) Out-of-canon:** Fandom liệt `Heroes of Might and Magic V: Legends of the Ancients`
dưới mục `===Out-of-canon===`. Đó là **mod fan**, không phải sản phẩm chính thức. Chưa
fetch để xác minh.

## 3.7 Disambiguation — ĐÃ KIỂM (theo BH-2)

Ba hướng kiểm, tất cả đều cho kết quả **chỉ có MỘT Gauldoth**:

1. Fandom `list=allpages&apprefix=Gauldoth` → đúng **2** kết quả:
   `Gauldoth` và `Gauldoth Half-Dead`. Trang thứ hai là **redirect**: nội dung wikitext là
   `#REDIRECT [[Gauldoth]]` (91 byte). **Không có trang disambiguation.**
2. Fandom full-text search `Gauldoth`, 40 kết quả đầu → tất cả đều là entity H4 liên quan
   (scenario, Nekross, Kalibarr, Alana…) + danh sách hero Necromancer H4. **Không có
   `Gauldoth (…)` thứ hai** kiểu `Sandro (Xeen)`.
3. thelazy: `apprefix=Gauldoth` → `[]` (rỗng). `list=search&srsearch=Gauldoth` →
   `totalhits: 0`. **thelazy không phủ Gauldoth chút nào** — khớp ghi chú access rằng
   thelazy không phủ Heroes IV.

⚠️ Lưu ý ngược lại: **tên bài chính trên Fandom là `Gauldoth`, không phải
`Gauldoth Half-Dead`** (ngược với entity-id của dự án). Infobox ghi tên đầy đủ là
`King Gauldoth Half-Dead`.

---

# PRIORITY 4 — phát ngôn developer (T4)

## 4.1 ⭐⭐ Terry B. Ray — người VIẾT Heroes IV. Phỏng vấn chính thức Ubisoft.

**Đây là phát hiện T4 lớn nhất, và nó ĐẢO NGƯỢC giả định trong prompt.** Prompt hướng tôi
tìm Jennifer Bullard vì "bà là designer/story writer cho Heroes IV". Bullard **có** liên
quan (§4.3), nhưng **người viết chính của Heroes IV là Terry B. Ray**, và ông đã trả lời
phỏng vấn **dài, chính thức, trên site Ubisoft**, nói **rất nhiều** về Gauldoth.

- URL sống: `https://mmh7.ubi.com/en/blog/post/view/lost-tales-q-a-with-terry-ray`
  → **FAILED**: redirect sang trang bán game Ubisoft Store (104.618 byte, không có nội dung
  phỏng vấn). Nội dung gốc đã bị xóa.
- URL dùng được: `https://web.archive.org/web/20151020063103/http://mmh7.ubi.com/en/blog/post/view/lost-tales-q-a-with-terry-ray`
  → **FETCHED**, 49.049 byte. Ngày đăng ghi trên trang: **09/11/2015**, 105 comment.
  Đăng bởi Ubisoft (site chính thức MMH7). Cuối bài: *"(Special thanks to David Mullich and
  George Almond.)"*

**Xác lập vai trò (nguyên văn intro của Ubisoft):**

> "Set on the world of Axeoth, these two free bonus campaigns, Unity and Every Dog Has His
> Day, were written by **Heroes IV's master bard: Terry B. Ray**. We have asked Terry to tell
> us more about these two lost stories, and his work on Might & Magic in general."

**Ray tự thuật công việc trên H4 (nguyên văn):**

> "For me, the project began with creating the campaign story ideas. Sometimes, people had
> to wait for me to create characters or aspects of the stories before they could do their
> job. […] I made maps, edited the stories, worked on the manual, and wrote other content.
>
> All told, I was hired to work on Heroes IV, but also wrote the Heroes III Chronicles
> series."

> "my bosses gave me just a few rules such as a campaign for every town type. Then I would
> create the central character for each story […] I don't plot everything out. I let the
> characters and their choices in given situations write the story."

**⭐ Về Gauldoth — đoạn quan trọng nhất, nguyên văn:**

> "But hands down and far ahead in this race for my love like a cheetah running against
> sloths is **Gauldoth Half-Dead**. I set out to make Gauldoth **the opposite of every
> necromancer from every fantasy story** and he became so much more during the writing
> process. […]
>
> He's still very real to me, and to this day I do annual searches about him just to see
> what people have been saying. Despite his horrible life, **he's a philosopher and probably
> wiser than anyone around him. He is not ruled by a quest for power like most necromancers,
> but he sees the purpose and usefulness of power. He is neither good nor evil.** He sees
> chaos and order, creation and destruction all as one thing dependent on each other.
> **I wanted him to be a metaphor for all Mankind.** Because of that, I think he is the one
> and only hope for peace in the troubled realms of the Might & Magic universe."

> "For years, I have been telling my friends I would love to write a Gauldoth book, or maybe
> a series of books. […] Gauldoth will forever be my child. May he live and unlive forever."

> "I can say that **Gauldoth would not have been the bad guy**, and Lysander would not have
> been all good. […] That's one of the reasons I think the Gauldoth campaign is so popular.
> **In my eyes, he is a hero.**"

**⭐⭐ Huyết thống — CÂU HỎI và CÂU TRẢ LỜI KHÔNG KHỚP NHAU. Đọc kỹ.**

Câu hỏi của người phỏng vấn (Ubisoft) — **đây là văn người phỏng vấn, KHÔNG phải Ray:**

> "Your script notes reveal some secrets about some of Heroes IV's characters. For instance,
> the fact that **Lysander, Waerjak and Gauldoth were actually brothers, the illegitimate
> sons of King Nicholas Gryphonheart with a woman named Iduna**. What was your "master plan"
> with the storyline?"

Ray trả lời (nguyên văn, **đoạn quyết định được in đậm**):

> "Ah, you caught me! Knew I should have burned those notes. […]
>
> When I looked on the future of the story line, I wanted to select three characters that
> would be pivotal in future games. I wanted these characters to share the same blood.
> **Not like they were all from the same mother, but all from the same bloodline.** That is
> where Lysander, Waerjak, and Gauldoth came in. **In my defense, this idea was never
> completely developed. I was toying with other options too**, but these three characters
> were at the top of the list."

→ **Ray KHÔNG xác nhận "cùng một mẹ tên Iduna".** Ông xác nhận *cùng huyết thống*, và **phủ
định** *cùng mẹ*. Ông cũng nói rõ ý này **chưa bao giờ được phát triển hoàn chỉnh** và ông
còn đang cân nhắc phương án khác. Xem mâu thuẫn §5.1 — đây là mâu thuẫn nghiêm trọng nhất
tìm được trong phiên này.

Ray cũng nói thêm: *"What may not be in the notes is the fact that **Tawni Balfour**, the
Pirate Queen, was probably going to be the major villain."*

## 4.2 ⭐ Ray phủ nhận liên quan tới expansion — chống lưng claim phủ định §3.6(a)

Câu hỏi (văn người phỏng vấn Ubisoft):

> "The expansion packs for Heroes IV, the Gathering Storm and Winds of War, were very
> different in tone from the base game and featured new lands and new characters, **with no
> connection to the stories of Emilia, Gauldoth and co.** Were you involved in their
> conception and writing?"

Ray:

> "No, I wasn't involved in those titles. That was after me. When Heroes IV shipped, **most
> of the company was let go.** That's when I left the industry."

→ Hai nguồn độc lập (grep 4 trang AoH = 0 hit; + T4 này) cho cùng kết luận. Claim phủ định
"Gauldoth không xuất hiện trong TGS/WoW" **đã săn chủ động**, không suy từ im lặng. Nhưng
lưu ý: câu "no connection" là **tiền đề của người phỏng vấn**, Ray chỉ trả lời phần "tôi có
tham gia không". Ghi nhãn cho chính xác.

## 4.3 Jennifer Bullard — có, và có nói về Gauldoth

Prompt hỏi đúng chỗ, nhưng bà là **designer/story writer** chứ không phải người tạo
Gauldoth.

**thelazy `Jennifer_Bullard`** (FETCHED, 654 byte, T5):

> "Jennifer Bullard is a member of the original New World Computing team which created the
> Might & Magic franchise. She is most known for her work as a designer and storyline writer
> for [H3], [H4], and [Heroes Chronicles]. Sometimes goes by the nickname "Maranthea".
> Jennifer also preserved several […] stories about The Reckoning which bridge the gap
> between [H3] and [H4]."

**Phỏng vấn Acid Cave** — thelazy `Jennifer_Bullard/Acid_Cave_Interview` (FETCHED, 13.712
byte). Trang tự khai:

> "= Acid Cave Interview [https://www.acidcave.net/jennifer_bullard_interview.html] =
> This interview was conducted in **2013** by **Alchemik** for Acid Cave."

⚠️ **Tôi fetch bản chép trên thelazy, KHÔNG fetch `acidcave.net` trực tiếp.** Nếu bài viết
trích, nên xác minh lại ở acidcave.net (registry ghi là FETCHED được). Tier: T4 (phát ngôn
developer) **qua trung gian T5**.

**Bốn Q&A liên quan trực tiếp Gauldoth (nguyên văn):**

> "Q: What caused the opening of the portals during the Reckoning? Were they opened by a
> Guardian?
> A: The Guardian opened the portals. We wanted to wash a lot of the history away from the
> old world and needed a mechanism to do so."

> "Q: Was the Guardian (who opened the portals) Corak […] Melian […] or someone
> (something?) else?
> A: **It was Corak - it is always Corak.**"

> "Q: **Where was Kalibarr when Gauldoth came looking for him?** Is it the planet after the
> Reckoning or a different planet conquered by Kreegans? If it's the planet conquered by
> Kreegans, how Kalibarr got there?
> A: **Kalibarr was held on the planet after the Reckoning, he was kidnapped and brought
> there by Demons.**"

⚠️ **Câu trả lời này có vẻ MÂU THUẪN với game text** — xem §5.4.

> "Q: There is the Paradise to which souls go after death, but what is it **the Plane of
> Death visited by Gauldoth** spying Kalibarr? Is it the opposition of paradise like hell
> and heaven in our world?
> A: For the most part. In a video game you want to use concepts the player is familiar
> with, but directly referencing religion can have problems. We want to appeal to a broad
> audience, so using Heaven and Hell can discourage some players. Which is why we use things
> like Paradise or the Plane of Death."

Thêm, hữu ích cho lore Axeoth:

> "Q: How far the design of Axeoth had been developed?
> A: We actually had a fairly fleshed out world. Knowing we would do 2-3 expansions our
> initial work gave space to expand, but also hinted at existing places. However, the layoffs
> happened so soon after the launch I am not sure how much was utilized in the subsequent
> expansions."

## 4.4 Gregory Fulton `On Names…` — KẾT QUẢ ÂM, đã kiểm

- URL: `https://heroes.thelazy.net/index.php?title=Gregory_Fulton/On_Names_in_Heroes_of_Might_and_Magic_III&action=raw`
- **FETCHED**, **98.499 byte** (khớp con số ~98 KB trong prompt).
- `grep -c -i "gauldoth"` → **0**.
- `grep -i "axeoth\|heroes iv\|heroes 4"` → **0**.

→ Đúng như prompt dự đoán: Fulton không làm Heroes IV, tài liệu này không có entry
`Gauldoth`. **Kết quả âm đã xác minh bằng fetch, không phải suy đoán.**

## 4.5 thelazy `Terry_Ray` (FETCHED, 267 byte, T5) — hai trivia

> "Main writer of Heroes Chronicles […] and [H4].
> == Trivia ==
> * The small Bracaduunian town of Terray's Hamlet is named after him.
> * Tarnum was originally the name of his ''Dungeons & Dragons'' character."

Trivia thứ hai **được Ray xác nhận trong phỏng vấn Ubisoft**: *"Tarnum from the Heroes
Chronicles series is a close second. He is my Crag Hack, my very first D&D character that I
brought to life in many tales."* → Hai nguồn khớp.

---

# SOURCE LIST

⚠️ Không key nào bắt đầu bằng số. Tier là **đề nghị**, editor quyết định theo
`CANON-POLICY.md`.

## Nhóm A — text in-game qua trung gian (đề nghị T1*)

| key đề nghị | tier | access | nội dung |
|---|---|---|---|
| `h4-transcript-halfdead-ch` | T1* | **FETCHED** | ⭐⭐ `H4-DeathTexts.rtf` 89.002 byte trên Celestial Heavens (Wayback `20130117072816`) — **toàn bộ** text kể của campaign Half-Dead: 5 scenario desc, 5 monologue, 54 block sự kiện gồm 5 quest có Proposal/Progress/Completion. Do Corlagon & Zamfir chép |
| `h4-transcripts-index-ch` | T3 | FETCHED | Trang index "Heroes IV Text Collection" by Kalah trên CH — khai rõ ai chép, dẫn tới 6 file RTF của 6 campaign |
| `h4-bio-gauldoth-campaign` | T1*? | FETCHED | Đoạn `Biography:` của Gauldoth trên AoH `heroes_campaign.shtml`, **khớp từng chữ** với `{{text}}` của Fandom → khả năng cao là bio in-game. Cần editor quyết tier |

## Nhóm B — fansite Age of Heroes (đề nghị T3, KHÔNG phải T2)

| key đề nghị | tier | access | nội dung |
|---|---|---|---|
| `aoh-h4-campaign-halfdead` | T3 | **FETCHED** | Cả 6 trang `campaign_halfdead[2-6].shtml` — nguồn **duy nhất** cho Map Difficulty / Map Size / Victory / Loss / Carryover từng scenario |
| `aoh-h4-campaigns-overview` | T3 | FETCHED | `campaigns.shtml` — tóm tắt 6 campaign H4, `Number of Maps: 5`, `Map Difficulties: Advanced x4, Expert` |
| `aoh-h4-heroes-campaign` | T3 | FETCHED | `heroes_campaign.shtml` 31.882 byte — bio Gauldoth, Kalibarr, Suraze + mục `Part in:` là văn fan có lỗi |
| `aoh-h4-heroes-necromancers` | T3 | FETCHED | `heroes_necromancers.shtml` — class Necromancer: khởi đầu Basic Death Magic + Basic Occultism, giá thuê 1500/2000 gold. **Không có Gauldoth** (hắn là campaign hero) |
| `aoh-h4-card-necromancers` | T3 | FETCHED | `heroes4card/heroesnecromancers.shtml` — chứng minh **có card Gauldoth** trong Heroes IV Card and Tile Game (DGA Games) |
| `aoh-h4-tgs-campaigns` | T3 | FETCHED | `tgs_campaigns.shtml` + `tgs_heroes.shtml` — 0 hit `gauldoth`. Bằng chứng phủ định |
| `aoh-h4-wow-campaigns` | T3 | FETCHED | `wow_campaigns.shtml` + `wow_heroes.shtml` — 0 hit `gauldoth`. Bằng chứng phủ định |
| `aoh-h4-heroes-deathknights` | T3 | FETCHED | `heroes_deathknights.shtml` 30.273 byte — 0 hit `gauldoth`, xác nhận hắn không phải Death Knight |

## Nhóm C — phát ngôn developer (T4)

| key đề nghị | tier | access | nội dung |
|---|---|---|---|
| `terry-ray-interview-ubisoft` | T4 | **FETCHED** (qua Wayback) | ⭐⭐ Phỏng vấn chính thức Ubisoft 09/11/2015 với **Terry B. Ray, người viết Heroes IV**. Gauldoth là nhân vật ông yêu nhất; ý đồ thiết kế; **phủ định "cùng một mẹ"**; xác nhận không tham gia TGS/WoW. URL sống đã chết (redirect sang store) |
| `bullard-interview-acidcave` | T4 | FETCHED **qua thelazy** | Phỏng vấn Jennifer Bullard 2013 do Alchemik thực hiện cho Acid Cave. Có 4 Q&A về Gauldoth/Kalibarr/Plane of Death/Corak. **Chưa đối chiếu với acidcave.net gốc** |
| `h3wiki-fulton-names` | T4 | FETCHED | `Gregory Fulton/On Names…` 98.499 byte — **0 hit `Gauldoth`**. Kết quả âm đã xác minh |

## Nhóm D — fan wiki (T5)

| key đề nghị | tier | access | nội dung |
|---|---|---|---|
| `mmwiki-gauldoth` | T5 | FETCHED | Fandom `Gauldoth` 16.935 byte — bài dài nhất về nhân vật; **stat block duy nhất** (level 2, 3 skill, 2 spell, Eater of Children); infobox huyết thống; trivia không dẫn nguồn |
| `mmwiki-eater-of-children` | T5 | FETCHED | Scenario 1 — infobox có 4 faction, walkthrough, strategy. Ghi difficulty = "Hard" (mâu thuẫn AoH) |
| `mmwiki-halfdead-campaign` | T5 | FETCHED | Trang campaign, `{{quote}}` = tóm tắt campaign in-game |
| `mmwiki-nekross` | T5 | FETCHED | Vương quốc Nekross — lịch sử, `founder`/`ruler` = Gauldoth |
| `mmwiki-nekorrum` | T5 | FETCHED | Thủ đô — dân số, hầm xác, "dark piper" |
| `mmwiki-necromancer-h4` | T5 | FETCHED | Class Necromancer H4 + bảng ưu tiên skill (Necromancy 5, Death Magic/Demonology/Occultism 4, …) |
| `mmwiki-iduna` | T5 | FETCHED | Trang cho nhân vật **không xuất hiện trong game nào** — chỉ dựa vào script notes của Ray. Nguồn của mâu thuẫn §5.1 |
| `h3wiki-the-reckoning` | T5 | FETCHED | thelazy 13.958 byte — ngày Reckoning 10/02/1177 AS, lời kể của Lysander, Dogwoggle |
| `h3wiki-jennifer-bullard` | T5 | FETCHED | Vai trò Bullard, nickname "Maranthea" |
| `h3wiki-terry-ray` | T5 | FETCHED | 267 byte — vai trò Ray + 2 trivia |

## FAILED / NOT_FETCHED

| nguồn | trạng thái | ghi chú |
|---|---|---|
| `mmh7.ubi.com` URL sống | **FAILED** | Redirect sang Ubisoft Store, nội dung phỏng vấn đã bị xóa. Phải dùng Wayback `20151020063103` |
| `celestialheavens.com` URL sống | **FAILED** | `curl` trực tiếp treo > 120 s (domain không phục vụ nữa). CDX chỉ có **1** snapshot cho `viewpage.php?id=763` — `20130117072816`. Dùng đúng snapshot đó |
| `acidcave.net/jennifer_bullard_interview.html` | **NOT_FETCHED** | Chỉ đọc bản chép trên thelazy |
| thelazy `Gauldoth_Half-Dead`, `Heroes_of_Might_and_Magic_IV` | **FAILED (0 byte)** | Xác nhận: thelazy **không phủ Heroes IV**. Đã có UA đầy đủ |
| `Lost Manuscripts` (thelazy) | **NOT_FETCHED** | Nguồn gốc của ngày Reckoning 1177 AS |
| Ảnh card Gauldoth (DGA Games) | **NOT_FETCHED** | Chỉ có thumbnail 104×141; không đọc được text/stat trên card |
| 4 file RTF campaign khác trên CH | **NOT_FETCHED** | `H4-LifeTexts.rtf` (Lysander), `H4-MightTexts.rtf` (Waerjak), `H4-OrderTexts.rtf` (Emilia), `H4-ChaosTexts.rtf` (Tawni), `H4-NatureTexts.rtf`. **Sẵn có, cùng snapshot** — mở đường cho 5 entity Axeoth nữa |
| `Heroes IV manual` | **NOT_FETCHED** | Ray nói ông "worked on the manual". Manual H4 có thể là nguồn T2 thật (khác AoH) |

---

# GAPS — tìm mà không thấy, kèm chỗ đã tìm

1. **Stat block đầy đủ.** Không tìm được Attack / Defense / Spell Power / Knowledge của
   Gauldoth ở bất kỳ scenario nào. Đã tìm: AoH `heroes_necromancers.shtml` (chỉ có class,
   không có campaign hero), `heroes_campaign.shtml` (chỉ bio, **không có stat**),
   `heroes_deathknights.shtml`, Fandom `Gauldoth` (chỉ level 2 + 3 skill + 2 spell cho
   scenario 1), thelazy (không phủ H4). **Nguồn duy nhất là Fandom và nó không dẫn nguồn.**

2. **Advanced class.** H4 cho hero lên advanced class khi đủ 2 skill. Không nguồn nào nói
   Gauldoth lên class gì. Đã tìm: `heroclasses.shtml` có trong CDX nhưng **chưa fetch**.

3. **Phạm vi phiên bản của con số gameplay.** AoH không ghi trang mô tả bản nào (H4 gốc?
   patch nào? TGS/WoW có đổi?). Level cap 12/18/24/30 và giá 1500/2000 gold **phải ghi là
   "bản H4 gốc, chưa xác minh với patch/expansion"**. Không tìm được changelog H4 nào trong
   phiên này.

4. **Ngày tuyệt đối trong campaign.** Campaign Half-Dead **không có một mốc lịch nào**. Mọi
   con số "1100s AS" / "1180s AS" chỉ có ở infobox Fandom, **không dẫn nguồn**.

5. **Manual chính thức H4.** Chưa tìm. Ray nói ông có làm manual → manual là nguồn T2 thật,
   khác hoàn toàn với AoH. Đây là hướng nâng tier tốt nhất cho entity này.

6. **Text/stat trên card DGA Games.** Xác nhận card tồn tại nhưng không đọc được nội dung.

7. **Ai là "the nameless one".** Game không đặt tên. Bullard chỉ nói nó tương ứng khái niệm
   "hell". Không tìm được nguồn nào đặt tên chính thức.

8. **"Script notes" của Terry Ray.** Người phỏng vấn Ubisoft nói đã xem được. Tôi
   **không tìm được** bản công bố nào của chính script notes đó — chỉ có câu hỏi mô tả lại.
   Đã tìm: link "Presentation of the Lost Tales available here" ở cuối bài (chưa theo).

9. **Rahjuu.** Fandom nói Kreegan canh xác Kalibarr tên Rahjuu; transcript block
   `==Kalibarr==` **không nêu tên nào**. Có thể tên này đến từ tên hero trên map (không có
   trong text kể). Chưa xác minh.

---

# SUSPECTED WIKI-ONLY CLAIMS

Claim chỉ có văn wiki chống lưng. **Không đưa vào thân bài mà không thêm nguồn.**

| claim | ở đâu | tại sao đáng ngờ |
|---|---|---|
| Gauldoth sinh `~1100s AS`; trị vì `ca 1180s AS` | infobox Fandom `Gauldoth` | **Không dẫn nguồn.** Campaign không có mốc lịch nào |
| Gauldoth thoát Reckoning "by passing through one of the portals to Axeoth, alongside countless fellow refugees" | thân bài Fandom, dẫn về `H4HDM1` | Transcript block `==The Past==` **không** nói tới portal hay đoàn tị nạn. Là suy diễn từ lore Reckoning chung |
| Nekross nằm ở **Iranese**; Gauldoth "roamed Iranese" | Fandom `Nekross`, `Gauldoth` | `grep -c Iranese` trên transcript = **0**. Iranese là tên vương quốc **của Lysander** theo lời kể Lysander |
| "Sometime after the **founding of Great Arcan**" | Fandom `Gauldoth` | Transcript chỉ nói Vitross "had a small garrison to support the expansion of Great Arcan's eastern borders". Thứ tự thời gian là suy diễn |
| Nekorrum có "a living population of 3000 people" | Fandom `Nekorrum` | Game text nói **~3000 xác** và "the living population… could be killed to give us **over six thousand** undead defenders" → dân sống suy ra ≥3000, là **INFERENCE**, không explicit |
| Gauldoth "is unique among his predecessors in actively seeking positive relations with fellow rulers" | mở bài Fandom | Nhận định biên tập. **Nhưng** có T4 chống lưng gần tương đương (Ray: "the opposite of every necromancer from every fantasy story") → dùng nguồn Ray, đừng dùng wiki |
| "Arantir, a Necromancer in the Ubisoft continuity, fills a somewhat similar role" | Trivia Fandom | Mở đầu bằng "It is considered that…" — **văn fan, không dẫn nguồn** |
| "Gauldoth shares his musical theme with … Necropolis town" | Trivia Fandom | Không dẫn nguồn. Kiểm được nếu có file game |
| "Gauldoth is the only protagonist who directly interacts with another during the campaigns"; "the only storyline internally implied to have occured after the events of another" | Trivia Fandom | Claim **so sánh toàn cục** không dẫn nguồn. Muốn dùng phải đọc cả 5 transcript campaign còn lại — **chúng đang có sẵn**, cùng snapshot CH |
| Iduna là **mẹ** của Lysander, Waerjak, Gauldoth | Fandom `Iduna` + infobox `Gauldoth` | ⚠️ **Ray phủ định trong chính nguồn Fandom dẫn.** Xem §5.1 |
| `Catherine Gryphonheart (half-sister)`, `Nicolai Ironfist (nephew)`, `Beatrice Gryphonheart (half-sister)` | infobox `Gauldoth` | **Không có `<ref>`** — khác với 4 quan hệ kia. Đây là suy diễn tầng hai từ một tiền đề đã sai |
| Kalibarr "arranged for a **Crusader (H3)** to destroy him" (link tới creature H3) | Fandom `Gauldoth` | Game text chỉ nói "a holy crusader" (chữ thường). Link sang creature H3 là quy ước wiki |
| "God of Death" như **tên riêng** | Fandom | Game text luôn gọi "the nameless one" |
| "leading them out of Nekorrum 'like some kind of dark piper from a fairy tale'" | Fandom `Nekorrum` | ✅ **Claim này ĐÚNG** — có trong transcript, block sau `==Children==`. Ghi ở đây để đánh dấu **đã kiểm và đạt**, không phải để loại |

---

# TIMELINE

**Lịch:** không nguồn nào nói Axeoth dùng lịch khác Enroth; cả thelazy và Fandom tiếp tục
dùng `AS`. **Nhưng campaign Half-Dead không có một mốc tuyệt đối nào** — toàn bộ mốc dưới
đây là **TƯƠNG ĐỐI**, trừ hai dòng đầu.

## Mốc tuyệt đối (từ nguồn ngoài campaign)

| mốc | nguồn | độ chắc |
|---|---|---|
| **10 tháng 2, 1177 AS** — Reckoning: Armageddon's Blade × Sword of Frost | thelazy `The_Reckoning` (T5), tự dẫn về `Lost Manuscripts` chưa fetch | T5, **UNVERIFIED tận nguồn** |
| Gauldoth sinh `~1100s AS`; trị vì `ca 1180s AS` | infobox Fandom, **không dẫn nguồn** | **UNVERIFIED** |

## Mốc tương đối — từ GAME TEXT (transcript), theo thứ tự truyện

| # | mốc | nguyên văn / căn cứ |
|---|---|---|
| 1 | Ký ức sớm nhất: bị vampire **Loscan** giam trong crypt, hút máu từ nhỏ | `"My first childhood memory is of a crypt… the Vampire who kept me alive to feed on my young blood."` |
| 2 | Kalibarr trả giá 10 đứa trẻ để đổi Gauldoth → Loscan từ chối → Kalibarr thuê crusader diệt Loscan → nhận Gauldoth làm học trò | `==The Past==` |
| 3 | Nhiều năm làm học trò + sát thủ cho Kalibarr | `==Vengeance==` |
| 4 | **"During the first hours of the Reckoning"** — thư viện mật của Necromantic Order cháy; Gauldoth đọc scroll quá tầm → thành half-dead | `==The Past==`. **Đây là mốc neo duy nhất gắn với sự kiện có ngày** |
| 5 | Sang Axeoth. **"Alone in this new world for years"** — sống như con vật | scenario 1 desc + `==Gauldoth==` |
| 6 | Bị dân Vitross bắt, gọi 'Ghoul' và 'Eater of Children', suýt thiêu; cast spell làm chậm rồi chạy | `==Gauldoth==` |
| 7 | **"A few nights later"** — tới graveyard, dựng quân đội undead đầu tiên | `==Full Circle==` |
| 8 | Diệt druid **Halas**, thiêu Vitross, biến Mardor thành ghost phó tướng. Gauldoth nói với Mardor rằng đó là **"months ago"** so với lần hắn bị thiêu | `==Vitross Captured==` |
| 9 | **"Over the past few months"** — lập biên giới Kingdom of **Nekross**; Enric làm garrison. Gauldoth **tự gọi mình là King of Nekross** ở `==Taking Action==` | `==The Kreegans==` |
| 10 | Vision lửa → biết Kalibarr còn sống | `==Fire!==` |
| 11 | Lấy **Angel's Blade** (cần **level 18**), đập vỡ ở nexus point → mở cổng sang **Fiery Realm** | 3 block `Quest:` scenario 2 |
| 12 | Gửi bản đồ tấn công cho Queen **Emilia Nighthaven** thay vì đánh Great Arcan | `==To Survive==` |
| 13 | Cứu Kalibarr từ altar ở Fiery Realm; đưa về Nekorrum; **nhường ngôi** | `==Kalibarr==`, `==Nekorrum==` |
| 14 | **"That was four months ago"** → Kreegan Rebellion phá nửa Nekorrum | `==Nekorrum==` → `==Kreegan Rebellion==` |
| 15 | Xử tử Enric; cứu **Alana**; kích hoạt 4 Point of Power | `==Enric's Demise==`…`Quest: Fourth Point` |
| 16 | **Alana chết** khi kích hoạt Point thứ 5 — Gauldoth **biết trước là có thể chết** và vẫn để bà làm | `Quest: Fifth Point` |
| 17 | Dẹp phản loạn của **Suraze** | `==Suraze==` |
| 18 | **"In the two months since I crushed the last of the rebellious demons"** — Kalibarr xa cách, cơ thể mục dần; Gauldoth theo dõi và nghe Kalibarr gọi ai đó là "Master" | `==Masters==` |
| 19 | Giết **Malvich**, lấy **Deadwood Staff** (Malvich giữ nó **"close to seven hundred years"**); nhận **Hadrin** làm bodyguard; lấy **Life Shield** ở Shrine of Korbert | `==Malvich==`…`==The Deadwood Staff==` |
| 20 | Kalibarr gom **toàn bộ trẻ em sống** ở Nekorrum; **100 đứa đầu** bị mang qua portal | `==Children==` |
| 21 | Gauldoth theo Kalibarr sang **Plane of Death**; nghe "the nameless one" ra lệnh: chờ **Convergence** (hành tinh thẳng hàng), **trong 3 tháng**, rèn skull vào Deadwood Staff → **Unholy Breath** | `==The Plane of Death==` |
| 22 | Thả trẻ em, chạy về Rija; **Hadrin's Stand** thất thủ do bị mua; Hadrin bị giam ở Plane of Death rồi được cứu | `==Hadrin's Stand==`, `==Hadrin's Fate==` |
| 23 | Liên minh **Suraze** (giá: đất + 4 town + danh hiệu "Duke") | `Quest: Suraze` |
| 24 | **Giết Kalibarr** trước Convergence. Loss condition map 5: phải thắng **trước Month 4** | `==Kalibarr Defeated==` + AoH |
| 25 | Epilogue: được đón như anh hùng; được gọi **'Protector'** và **'Father Gauldoth'**; phá chuồng giam trẻ; tự nhận **"King of Nekross"** | `==Epilogue==` |

**Tổng thời lượng nội bộ:** không cộng được thành số chính xác. Cận dưới an toàn: từ mốc 5
("years") tới mốc 25 là **nhiều năm**, trong đó riêng đoạn 13→24 là **≥ 9 tháng** (4 tháng +
2 tháng + 3 tháng).

---

# §5 — MÂU THUẪN GIỮA CÁC NGUỒN (phần dự án quan tâm nhất)

## 5.1 ⚠️⚠️ NGHIÊM TRỌNG NHẤT — "Iduna là mẹ của cả ba"

- **Fandom `Iduna`** khẳng định: *"Terry Ray's script notes for Heroes of Might and Magic IV
  revealed that **she was the mother of** Lysander, Waerjak, and Gauldoth"* — và dẫn `<ref>`
  về đúng bài phỏng vấn Ubisoft.
- **Fandom infobox `Gauldoth`** ghi `Iduna (mother)`, `Nicolas Gryphonheart (father)`,
  `Lysander (brother)`, `Waerjak (brother)` — cả bốn dẫn cùng một `<ref name=Family>`.
- **Trong chính nguồn đó, Terry Ray nói:** *"I wanted these characters to share the same
  blood. **Not like they were all from the same mother, but all from the same bloodline.**"*

→ Fandom **lấy tiền đề từ câu hỏi của người phỏng vấn** rồi trình bày như thể Ray xác nhận,
trong khi Ray **phủ định đúng chi tiết đó** ngay câu sau. Cộng thêm Ray nói *"this idea was
never completely developed. I was toying with other options too."*

**Khuyến nghị nhãn:** claim "Gauldoth là con của Nicolas Gryphonheart và Iduna, anh em với
Lysander và Waerjak" phải là **`DISPUTED`**, tier **T4**, kèm ghi rõ: (a) đây là **ý tưởng
chưa phát triển trong script notes chưa công bố**, không phải nội dung game; (b) phần "cùng
một mẹ" bị **chính tác giả phủ định**. Ba quan hệ suy tầng hai (`Catherine` half-sister,
`Nicolai Ironfist` nephew, `Beatrice` half-sister) **không có ref nào cả** →
`UNVERIFIED`, không vào thân bài.

Ghi chú thêm: câu hỏi của Ubisoft viết **"Nicholas"**, Fandom viết **"Nicolas"**. Sai lệch
chính tả tên vua giữa hai nguồn.

## 5.2 Độ khó scenario 1: "Advanced" vs "Hard"

- AoH `campaign_halfdead.shtml`: `Map Difficulty: **Advanced**`.
- Fandom `Eater of Children` infobox: `difficulty = **Hard**`.

Thang H4 (suy từ AoH `campaigns.shtml`, các campaign khác) là
Novice/Intermediate/Advanced/Expert — **không có "Hard"**. → Fandom đã tự chuẩn hóa sang
thang khác. **Dùng "Advanced"**, và nếu bài viết dẫn Fandom cho độ khó thì đó là lỗi.

## 5.3 Victory condition scenario 1: mức chi tiết khác nhau

- AoH: `Victory Condition: Capture Vitross.`
- Fandom: `win = Capture the **Academy town** of Vitross`

Không mâu thuẫn về bản chất, nhưng Fandom **thêm thông tin** (Vitross là town Academy)
không có ở AoH. Nếu trích, phân biệt: "Capture Vitross" là điều kiện; "Academy town" là
thông tin bổ sung của wiki.

## 5.4 ⚠️ Kalibarr bị giam Ở ĐÂU — Bullard (T4) vs game text (T1*)

- **GAME TEXT** (`==The Kreegans==`): *"some [Kreegans] retreated to the safety of **another
  realm**. That's where I would find my Master!"*
  Và `==The Fiery Realm==`: *"**You have come to another world** - a world that has seen the
  domination of the Kreegans."*
  Và toàn bộ scenario 2 xoay quanh việc **phải mở cổng liên giới** bằng cách đập vỡ Angel's
  Blade ở nexus point — vô nghĩa nếu Kalibarr ở ngay trên Axeoth.
- **Bullard (T4, 2013):** *"Kalibarr was held **on the planet after the Reckoning**, he was
  kidnapped and brought there by Demons."*

Hai cách đọc câu Bullard: (a) "the planet after the Reckoning" = Axeoth → **mâu thuẫn thẳng
với game text**; (b) bà đang trả lời lệch, hoặc "the planet" chỉ hành tinh mà Kreegan chiếm.
Câu hỏi gốc đưa ra đúng hai lựa chọn đó và bà chọn cái thứ nhất.

**Khuyến nghị:** ưu tiên **game text** (T1* EXPLICIT: "another world"). Nếu nêu phát ngôn
Bullard thì gắn nhãn **`DISPUTED`** và trình bày như **mâu thuẫn hồi tưởng của developer sau
11 năm** — chính bà mở đầu phỏng vấn bằng *"It has been many years since I worked on those
games, so my memory may not be perfect."*

## 5.5 Ba dị bản chữ giữa AoH và transcript CH

| chỗ | AoH | CH transcript | Fandom |
|---|---|---|---|
| tóm tắt campaign | `including **must** of his humanity` | `including **most** of his humanity` | `most` |
| monologue sc.2 | `to be part of its plan` | `to be **a** part of its plan` | `to be part of` |
| monologue sc.3 | `why is lifeblood of creation` | `why is **the** lifeblood of creation` | (Fandom không trích) |
| desc sc.5 | `the **S**tars will be in alignment` | `the **s**tars will be in alignment` | — |

→ Không có nguồn nào phân xử được (không có file game). **Với text in-game, ưu tiên CH
transcript**, vì AoH có lỗi rõ ràng (`must`) trong khi CH thì không, và CH giữ cả những dị
biệt trông "sai" nhưng nhất quán (`the grand scheme of things they are just the masks`,
`far stronger that it appears`) → dấu hiệu chép nguyên, không sửa.

## 5.6 Vai của Jennifer Bullard vs Terry Ray

Prompt (và có thể registry) coi Bullard là "designer/story writer cho Heroes IV". Đúng —
thelazy khẳng định vậy. Nhưng **phỏng vấn chính thức Ubisoft gọi Terry B. Ray là "Heroes
IV's master bard"** và chính Ray nói *"anything that had text attached to it was run through
me"* và *"I would create the central character for each story"*. → Với **Gauldoth cụ thể**,
**Ray là nguồn tác giả**, Bullard là nguồn thứ cấp về thiết kế thế giới. Không mâu thuẫn,
nhưng **ưu tiên nguồn phải đảo lại** so với giả định trong prompt.

## 5.7 Ba lỗi/mâu thuẫn nội tại của fansite AoH (ghi để không chép lại)

1. `heroes_necromancers.shtml` heading: `Death/Necropolis **Might** Heroes - Necromancers`
   — sai, Necromancer là magic class (trang `heroes_deathknights.shtml` mới là might).
2. `heroes_campaign.shtml` mục `Part in:` viết tên nhân vật là **`Galdoth`** (thiếu `u`)
   **bốn lần**, và chứa lỗi `resqued`, `phylosophic`, `imprissoned`.
3. `campaign_halfdead5.shtml` dòng Loss Condition ghép hai điều kiện thành một câu vô nghĩa
   ngữ pháp.

**Kết luận về tiering:** AoH **tốt** cho metadata scenario (không nguồn nào khác có) nhưng
**kém** cho text in-game. CH transcript **tốt** cho text in-game nhưng **không có** metadata.
Hai nguồn **bổ sung nhau**, không thay thế nhau.
