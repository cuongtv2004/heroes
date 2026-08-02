# Research dossier: Armor of the Damned — 2026-08-02

Tư liệu thô. Giữ nguyên tiếng Anh. **Không phải nguồn** — xem `sources/REGISTRY.md`.

Agent dùng `curl` với `action=raw`, không dùng WebFetch.

---

## 1. Bản thân artifact

| Trường | Giá trị |
|---|---|
| Class | Combo (`Relic` + `Combination`) |
| Slot | Torso |
| Cost | 12000 |
| Chặn slot | Helmet, Weapon, Shield |
| Stat khi ghép | **+3 Attack, +3 Defense, +2 Power, +2 Knowledge** |

### BỐN spell — xác nhận, không phải năm, không có biến thể "Mass"

Trường `effect`, nguyên văn:
> "Casts Expert Slow, Curse, Weakness, and Misfortune for 50 rounds at the start of combat."

**Xác nhận chéo ba cách độc lập:**
1. Mô tả in-game của Fandom liệt kê đúng bốn spell đó
2. Trang `Weakness` ghi Armor of the Damned là artifact **duy nhất** cast được Weakness
3. Đoạn fan-opinion cũng đếm "a total of four spells"

**Nguồn gốc hiểu nhầm "Mass":** Weakness/Slow/Curse/Misfortune ở cấp Expert **vốn đã** ảnh
hưởng toàn bộ quân địch — nhưng game text **không dùng** chữ "Mass".

### Mô tả in-game (Fandom `List_of_Heroes_III_artifacts`)

> "Worn on the torso, this armor casts Slow, Weakness, Misfortune and Curse on the enemy at
> the start of every battle. The effect lasts for **fifty turns**."

⚠️ Thứ tự khác thelazy (Slow, Weakness, Misfortune, Curse) và dùng chữ "fifty turns" thay vì
"50 rounds". Cùng bốn spell.

### Pickup text
> "You trip over the Armor of the Damned, dust it off, and stick it in your pack."

### Cơ chế chiến đấu — TẤT CẢ là văn wiki, không phải game text

Thời điểm kích hoạt:
> "The Armor of the Damned only casts its opening combat spells **once an allied creature is
> able to take its turn**; if a creature misses a turn due to low morale, the Armor of the
> Damned does not cast its spells until the next one is able to do so."

Cái gì chặn được:
> "...can be mitigated by enemy creatures' immunity, Cursed Ground, or anti-magic artifacts.
> **However, it works normally in Anti-Magic Garrisons.**"

Anti-Magic Garrison được xác nhận ở trang thứ hai (`Trivia`): "Armor of the Damned, Angelic
Alliance, and Ironfist of the Ogre spells still work in an Anti-Magic Garrison."

### ⚠️ Mâu thuẫn thật giữa hai trang — Orb of Inhibition

Trang Armor nói "anti-magic artifacts" chặn được. Nhưng trang `Orb_of_Inhibition` liệt kê
rõ dưới mục **"Does not prevent"**:

> "Artifact spell casting (i.e. **Armor of the Damned**, Angelic Alliance or Ironfist of the
> Ogre)."

Fandom đồng ý: "The spells are not prevented by the Orb of Inhibition."

→ **Orb KHÔNG chặn Armor.** Cách nói "anti-magic artifacts" của trang Armor là **lỏng lẻo,
không được lặp lại nguyên si**. Recanter's Cloak / Cape of Silence có thể là thứ được ám chỉ
nhưng agent **chưa kiểm riêng**.

### Bốn hero chuyên Weakness — kiểm từng người

| Hero | Class | Chỉ HotA? |
|---|---|---|
| Cuthbert | Cleric | Không |
| Olema | Heretic | Không |
| Mirlanda | Witch | Không |
| **Eanswythe** | Artificer (Factory) | **Có** — trang có `{{inhota}}` |

Specialty text giống nhau cả bốn:
- **HotA:** "Casts Weakness with effect increased by 4 for level 1–2 creatures, by 6 for
  level 3–4, by 8 for level 5–6, and by 10 for level 7."
- **SoD gốc:** "...increased by 3 for level 1–2, by 2 for level 3–4, and by 1 for level 5–6."

### Thay đổi HotA — KHÔNG CÓ

Agent grep toàn bộ changelog 201KB cho `armor of the damned`, `skull helmet`, `rib cage`,
`blackshard`, `yawning dead`. **Không một kết quả nào** cho cả năm artifact.

Thay đổi gián tiếp áp cho mọi combination artifact:
- "The option of banning combination artifacts... is added"
- "In artifact description, it is noted a component of which combination artifact it is..."
- "Fixed a bug: HotA-original combination artifacts were not included in the list of
  combination artifacts banned from assembly"

**Đáng chú ý: Cloak bị cấm mặc định ở HotA; Armor of the Damned KHÔNG bị nhắc trong lệnh
cấm đó.**

Phát biểu an toàn nhất: **changelog HotA không có entry nào cho Armor of the Damned hay các
thành phần của nó.**

### Ý kiến fan — `{{fanopinion}}`, đánh dấu rõ

> "Armor of the Damned is one of the **weakest** combination artifacts in the game in regards
> to stats alone... Conversely, its effect is easily one of the **most powerful**, casting a
> total of four spells at Expert level, at no cost, and leaving the hero free to cast another
> spell on their action (**so potentially 5 spells in a single turn**). Of the spells cast,
> only Misfortune is subpar."
>
> "Since it casts its spells only when your first unit becomes active, Armor of the Damned
> works best with a speedy unit stack... If the enemy moves before you, they may haste their
> units or slow yours, and **cripple your army before the Armor ever has a chance of
> activating**."

→ Đây là nguồn của lỗi "5 spell". Bốn của armor + một của chính hero.

---

## 2. Bốn thành phần

| Thành phần | Class | Slot | Cost | Effect |
|---|---|---|---|---|
| Skull Helmet | **Treasure** | Helmet | 3000 | +2 Knowledge |
| Rib Cage | Minor | Torso | 3000 | +2 Power |
| Blackshard of the Dead Knight | Minor | Weapon | 3000 | +3 Attack |
| Shield of the Yawning Dead | Minor | Shield | 3000 | +3 Defense |

**Pickup text:**

- **Skull Helmet:** "A brief stop at an improbable rural inn yields an exchange of money,
  tales, and **accidentally, luggage**. You find a magical helm in your new backpack."
- **Rib Cage:** "You trip over what was the rib cage of a large creature. Upon further
  examination, you discover the rib cage to be a piece of armor."
- **Blackshard:** "**The widow of a former Captain of the Guard** admires your quest and gives
  you the enchanted Sword that her husband relied on during his tour of duty."
- **Shield:** "Your troops discover an eerie shrine dedicated to the Undead. You bless the
  shrine, causing the stone shield emblem above the altar to crack. Underneath it is a real
  shield, which you decide to separate from this unholy place."

### ⭐ Phép cộng đáng chú ý

Bốn thành phần cộng lại: +3 Atk / +3 Def / +2 Pow / +2 Kno — **đúng bằng** stat của bộ hoàn
chỉnh. **Armor không cho thêm một điểm chỉ số nào so với các phần rời.** Toàn bộ giá trị của
nó nằm ở hiệu ứng spell.

Giá cũng khớp: 4 × 3000 = 12000 = giá bộ hoàn chỉnh.

*(Đây là phép tính của agent trên số đã fetch, và nó khớp với nhận xét fan rằng stat yếu.)*

---

## 3. Tuyến lừa Crag Hack

### Thứ tự scenario — sửa một giả định tự nhiên

Thứ tự **KHÔNG** giống thứ tự liệt kê trên trang artifact:

| # | Scenario | Thành phần | Độ khó | Cap level |
|---|---|---|---|---|
| 1 | Bashing Skulls | Skull Helmet | Hard | 10 |
| 2 | Black Sheep | **Blackshard** | Hard | 15 |
| 3 | A Cage in the Hand | **Rib Cage** | Expert | 20 |
| 4 | Grave Robber | Shield of the Yawning Dead | Expert | 25 |

Điều kiện thua giống nhau cả bốn: "Lose Hero Crag Hack the Barbarian."

Khung campaign (`Hack_and_Slash`): "Crag Hack... meets a young wizard named Sandro, who hires
him to find the four pieces of the Armor of the Damned **so he can destroy the cursed
thing**."

### Cảnh tuyển mộ ở Wingtail Tavern — Day 1, KHÔNG phải prologue

*(Toàn văn đã có trong dossier Sandro. Điểm mới:)*

**Giá hứa:** "five hundred thousand gold pieces **and a small land grant**".

⚠️ **Cách nói của Sandro đúng theo kiểu luật sư:** "together, they can be assembled into a
great weapon, **a weapon that I desperately require**" — đây là **sự thật nguyên vẹn nằm
trong lời nói dối**.

### "Chúng sẽ nói dối anh" — TÌM ĐƯỢC CẢ BỐN LẦN

Đây là thủ đoạn đặc trưng của Sandro: **tiêm chủng trước cho Crag Hack chống lại sự thật.**
Mỗi lần, kẻ "nói dối" đều **đang nói thật**.

**1. Bashing Skulls (Day 1):**
> "Now, I warn you, do not listen to anything he tells you. Although, like you, he is a
> Barbarian, he has no honor and **lies like a snake**."

Trả giá — event (54, 12, 0):
> Barshon: "I know you mean to take the Skull Helmet from me... **It is a family heirloom
> handed down from generations.**"
>
> "As you tear up the scroll you remember that Sandro said Barshon **FOUND** the Helmet. You
> shrug. Barshon is a lying snake."

**2. Black Sheep (Day 1)** — Sandro dùng lại thủ đoạn để chối bỏ lời trăng trối của Barshon:
> "And do you know what Barshon told me? Said this Helmet was his, that it belonged to him
> and his family."
>
> "**See, didn't I warn you he would lie to protect a mere possession?**... I hope his death
> was a most painful one."
>
> **"Never before have you heard a Wizard talk so brutally."**

Vỏ bọc Black Sheep: "It was stolen from the tomb of a great hero by a Death Knight named
Marzeth." Bị phản bác bởi báo cáo trinh sát Day 14:
> "Supposedly Marzeth was a Knight of the Blade who **inherited** the Blackshard, but the
> cursed sword twisted his soul until he became a Death Knight... **it goes against Sandro's
> story** that Marzeth stole the sword from a warrior's tomb."

⭐ **Chi tiết rợn người tại (64, 9, 0)** — bằng chứng Sandro đang thao túng tâm trí "đồng minh":
> "As you embrace your fellow Barbarian in a bear hug, **you notice that his eyes look
> vacant**. Although he has only kind words to say about Sandro, you wonder how the puny
> wizard really managed to persuade this stout Barbarian to assist you."

**3. A Cage in the Hand (Day 1)** — vỏ bọc:
> "It was being kept safe for me in a Sanctuary, but the Necromancers... burned the Sanctuary
> to the ground and stole the Rib Cage."

Bị phản bác Day 30: "**We know nothing about a Sanctuary**, Mister Hack, but we do know this:
you are already dead. You just don't know it yet yourself."

Sandro còn khoe vàng: "Sandro takes out a sack and opens it partially, revealing gold and
gems."

**4. Grave Robber (Day 1)** — phát biểu rõ nhất về thủ đoạn:
> "And one last thing. **Like the others you have battled, the Necromancers will lie to you.
> Do not listen to them.**"

### Cung bậc nghi ngờ của Crag Hack — dựng theo ba giai đoạn

**Giai đoạn 1 — A Cage in the Hand (Day 1)**, vết nứt đầu:
> "However, doing battle for this wizard is turning out not to be as much fun as you had
> hoped. **Sandro makes you think too much.**"

**Giai đoạn 2 — Grave Robber (Day 1)**, nghi ngờ đầu tiên có hành động:
> "As you leave the tavern you think about all the lies you have encountered on Sandro's
> tasks. **Maybe you should collect your rewards BEFORE handing over the last artifact.**"

**Giai đoạn 3 — Grave Robber (Day 15)**, khoảnh khắc quyết định:
> Hand of Death: "...Be warned that the Shield of the Yawning Dead is **our relic**. It has
> been a part of our graveyard for many years."
>
> "More lies, you think as you tear up the scroll, but still doubts remain. **Is Sandro the
> one who cannot be trusted?**"

⚠️ Chú ý "**an acquaintance of ours**" trong thư — Hand of Death biết Sandro là đồng nghiệp
necromancer. Vỏ bọc đang rạn.

**Ghi chú cấu trúc:** hành động **xé cuộn giấy** lặp lại ở Bashing Skulls (54,12,0) và Grave
Robber Day 15 — cùng một cử chỉ, nhưng lần thứ hai **sự nghi ngờ sống sót qua nó**.

### Epilogue phản bội — Grave Robber
> "I've been tricked! The thieving Wizard took off with the artifacts and didn't give me my
> gold! When I find Sandro I'm going to rip his arms off and shove them down his lying
> throat! Argggggggggggggh!"

---

## 4. ⭐⭐ LỖI LIÊN TỤC TRONG GAME — chứng minh chắc chắn

Prologue `Grave_Robber`, nguyên văn:
> "Now that I gave him **the Death Knight's Sword**, Sandro wants me to fight some more
> Necromancers for a shield..."

**Bằng chứng không thể chối cãi: CÙNG MỘT TRANG tự mâu thuẫn.** Day 1 timed event của chính
Grave Robber mở đầu:
> "**You have the Rib Cage!** Excellent work, Mister Hack" Sandro says back in the Wingtail
> Tavern."

→ Trong cùng một scenario, prologue nói món vừa giao là *Death Knight's Sword*, còn Day 1
event nói là *Rib Cage*.

**Rib Cage mới đúng.** Blackshard ("Death Knight's Sword") đã giao **một scenario trước**, ở
đầu `A Cage in the Hand`: "I got Sandro his cursed sword, and now he wants me to fight more
moldy Necromancers to get some kind of armor made out of bones."

**Chuỗi prologue để đối chiếu:**

| Scenario | Prologue nói vừa giao gì |
|---|---|
| Bashing Skulls | (chưa giao gì — mới nhận việc) |
| Black Sheep | "I went back to the Tavern to give Sandro this ugly **Helmet**" |
| A Cage in the Hand | "I got Sandro his cursed **sword**" |
| **Grave Robber** | "**the Death Knight's Sword**" ← **SAI, phải là Rib Cage** |

**Chẩn đoán của agent (đánh dấu là suy luận):** prologue Grave Robber có vẻ là bản sao của
thứ lẽ ra thuộc về A Cage in the Hand — tức prologue bị **lệch một scenario**.

⚠️ **Wiki âm thầm che lỗi này** bằng cách pipe link: `[[Blackshard of the Dead
Knight|Death Knight's Sword]]`. Biên tập viên link tới Blackshard — đúng với chữ, nhưng
**sai với cốt truyện**. Wiki không đánh dấu đây là lỗi ở đâu cả.

### Hai lỗi text khác trong cùng scenario

**Lỗi 2:** mô tả Grave Robber nói Crag Hack "will carry his experience, skills and spells on
to his next campaign". Wiki tự ghi chú: "**Note: Although the description states that Crag
Hack carries over to the next campaign, that is not accurate.**" Bảng campaign cũng ghi
`carry=(none)`.

**Lỗi 3:** mô tả gọi là "the **Yawning Shield of the Dead**" trong khi tên thật và điều kiện
thắng là "**Shield of the Yawning Dead**".

→ Ba lỗi text trong cùng một scenario.

---

## 5. Chủ sở hữu và kết cục

### KHÔNG game text nào nêu người tạo ra hay chủ sở hữu gốc

Agent săn chủ động, không giả định. **Kết quả: không có.** Cũng không có chủ cũ nào khác được
nêu tên.

### Claim "từng thuộc về Ethric" — tìm được nguồn gốc, và nó KHÔNG đứng vững

Trang `Ethric`, mục Trivia:
> "Armor of the Damned and Cloak of the Undead King once belonged to Ethric, **since**
> Jeddite's stated goal in Target is to return them to him... It is also **possible, though
> not confirmed**, that the two artifacts... were originally created by Ethric."

Wiki tự rào bằng "since" (đánh dấu là suy luận) và "possible, though not confirmed".

**Agent fetch `Target` và kiểm suy luận đó. Nó không đứng vững.** Day 1:
> "Ethric has spread word of your whereabouts to **those who lost these two precious
> artifacts** and to others who have their own reasons for despising Necromancers."

"Those who lost these two precious artifacts" = những bên Sandro đã cướp (Crag Hack, Gem, và
các chủ gốc như Barshon, Knights of the Blade, Ebon Hand, Hand of Death). **Ethric là kẻ
loan tin, không phải người đòi lại.**

Thêm nữa, region text: "Some of the lords want these artifacts for their own use; others want
to destroy them" — và Day 24 cho thấy Jabarkas muốn giữ. **Mâu thuẫn với cách đọc một-chủ-sở-hữu.**

"Return them to Ethric" hợp lý nhất là **Jeddite giao lại cho thầy để cất giữ/tiêu hủy** —
đúng như cách người ta đưa vật nguy hiểm cho pháp sư cao tay hơn. Nó không xác lập sở hữu quá khứ.

### Điều game text CÓ nói về xuất xứ

Chỉ có **lai lịch gần đây của từng thành phần** — và Sandro nói dối về **từng cái một**:

| Thành phần | Sandro nói | Người giữ nói |
|---|---|---|
| Skull Helmet | Barshon "unearthed" nó | **Gia bảo truyền đời** |
| Blackshard | Marzeth trộm từ mộ anh hùng | Marzeth **thừa kế** nó |
| Rib Cage | Necromancer đốt Sanctuary và trộm | "**We know nothing about a Sanctuary**" |
| Shield | (ngụ ý là bị chiếm) | "**our relic**, đã ở nghĩa địa chúng tôi nhiều năm" |

⭐ **Mỗi lần, lời của người giữ mới là lời đáng tin, còn lời Sandro là lời dối.** Nhưng không
lời nào mô tả việc **tạo ra** Armor — chỉ là quyền giữ gần đây.

### Kết cục — `Fall_of_Sandro` epilogue (Yog)

> "After realizing how corrupting these artifacts are, we decided to split them up into less
> powerful components and disperse them throughout Antagarich."

Xác nhận: **"these artifacts" số nhiều và không nêu tên**, bao gồm cả hai. Epilogue **không
bao giờ nêu tên** artifact nào.

⭐ **Bị tháo rời và phân tán — KHÔNG bị phá hủy.** Đây là cái kết mỉa mai của campaign: các
thành phần trở về đúng trạng thái ban đầu, và **lời nói dối của Sandro với Crag Hack (rằng
Armor sẽ bị phá hủy) được kẻ thù của hắn thực hiện, dưới dạng biến thể, thay vì hắn.**

Game text xác nhận Sandro thật sự dùng nó — `Wrath_of_Sandro` Day 4:
> "With the Armor of the Damned and the Cloak of the Undead King in your possession, you will
> easily overtake them and force these invaders out of your lands."

---

## Lỗ hổng

1. **Không lấy được số phiên bản HotA** — changelog không có entry nào cho năm artifact này.
   Phát biểu an toàn: changelog **không có** entry nào.
2. **Recanter's Cloak / Cape of Silence chưa kiểm.** Đã bác bỏ Orb of Inhibition, nhưng chưa
   fetch hai cái kia. Không được lặp lại cách nói "anti-magic artifacts" mà chưa kiểm.
3. **Cursed Ground chưa xác minh độc lập.**
4. **Mô tả in-game lấy từ bảng của Fandom**, không từ file game. Nhất quán giữa hai wiki
   nhưng vẫn là bản chép.
5. **`Talk:Artifact/descriptions` xuất hiện trong backlink, CHƯA FETCH** — có thể chứa chuỗi
   trích từ file game. **Đây là bước tiếp theo giá trị nhất** nếu muốn mô tả cấp file game.
6. Video cutscene Skull Helmet chưa chép lời.
7. `Armor_of_the_Damned_(disambiguation)` **không tồn tại** (0 byte). ⚠️ `Shield_of_the_Damned`
   là artifact **riêng biệt, không liên quan** — đừng nhầm với `Shield_of_the_Yawning_Dead`.

## Claim chỉ có wiki chống lưng

1. **"Từng thuộc về Ethric"** — suy luận Trivia, wiki tự rào, và `Target` Day 1 phản bác.
   **Coi như đã bị bác bỏ.**
2. **"Có thể do Ethric tạo ra"** — wiki tự ghi "possible, though not confirmed"
3. **Cơ chế thời điểm kích hoạt** — văn wiki chi tiết, không dẫn nguồn. Gần như chắc chắn
   đúng (quan sát người chơi) nhưng **không phải game text**
4. **"Works normally in Anti-Magic Garrisons"** — được xác nhận ở trang thứ hai, nên vững hơn
   phần lớn. Vẫn không dẫn nguồn in-game
5. **"Anti-magic artifacts" chặn được** — bị trang Orb of Inhibition phản bác một phần
6. Toàn bộ `{{fanopinion}}` / `{{user commentary}}` — phải giữ nhãn ý kiến fan
7. **Link pipe `[[Blackshard of the Dead Knight|Death Knight's Sword]]`** — diễn giải của
   biên tập viên **che lỗi thay vì ghi nhận nó**
