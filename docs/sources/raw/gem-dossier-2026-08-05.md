# Dossier research thô — `gem` (hero)

- **Entity:** `gem` · loại `hero`
- **Ngày research:** 2026-08-05
- **Trạng thái:** RAW — **chưa qua verify độc lập**. Không được trích thẳng vào thân bài.
- **Người/agent thực hiện:** research agent (không đọc bài Codex nào về Gem trước khi fetch — không có bài nào tồn tại)

> ⚠️ Đây là dossier thô theo `WORKFLOW.md` bước 2–3. Mọi trích dẫn dưới đây **nguyên văn tiếng Anh**,
> giữ nguyên cả lỗi chính tả và khoảng trắng đôi của text gốc. Nhãn tier là **đề xuất**, chờ verify.

---

## 0. TÓM TẮT ĐIỀU HÀNH — năm phát hiện quan trọng nhất

1. **Bio Heroes III của Gem là `T1` THẬT**, không phải `T1*`. Nó nằm nguyên văn trong
   `Translation Data/HeroBios.txt` (string table trích từ file game, đã là nguồn có sẵn của dự án:
   `h3wiki-herobios-txt`). Không cần hạ xuống `T1*`.

2. **Câu chuyện gốc của Gem chưa từng vào Codex, và nó nằm trong một timed event ngày 1** —
   đúng kiểu lỗi mà **BH-1** cảnh báo. Làng nàng bị skeleton tàn sát, em gái chết, nàng là
   **người sống sót duy nhất**. Đây là lý do tâm lý cho toàn bộ hành vi của nàng với Necromancer.
   Nguồn: `sod-agents-of-vengeance`, timed event **Day 1** (không phải prologue).

3. **Neo thời gian mới, rất mạnh:** *"I am in my sixty-first year as a Sorceress."*
   (`sod-driving-for-the-boots`, Day 12). Kết hợp với bio Heroes IV
   (*"over eighty years of wars and conflicts"* + nước suối thần giữ trẻ) thì đây là mắt xích
   giải thích vì sao một nhân vật có mặt từ Heroes I tới Heroes IV mà vẫn trẻ.

4. **Có MÂU THUẪN NGUỒN THẬT về class**, không phải lỗi wiki: sách hướng dẫn in
   (`sod-manual-p14`, `T2*`) ghi class của Gem trong *New Beginning* là **Druid**;
   bản thân game (`T1*`) ghi là **Sorceress (Campaign)**. Hai nguồn chính thức nói khác nhau.

5. **Liên tục H2→H3→H4 KHÔNG phải giả định của wiki** — nó được chống lưng bởi `T1` (bio game),
   `T1*` (nhiều dòng text game) và `T4` (Fulton). Chi tiết ở §1.3. Ngược lại, **liên tục H1** thì
   **chỉ có mức roster/chân dung**, không có một chữ text kể chuyện nào.

---

## 1. PRIORITY 1 — STEP A: mọi "Gem" trong Old Universe

### 1.1 Liệt kê đầy đủ — thelazy (heroes.thelazy.net)

Truy vấn:
`https://heroes.thelazy.net/api.php?action=query&list=allpages&apprefix=Gem&aplimit=500&format=json`
→ HTTP 200, 387 byte, **8 trang**. Liệt kê **toàn bộ**, kể cả trang không liên quan:

| # | Tiêu đề | Nội dung | Liên quan? |
|---|---|---|---|
| 1 | `Gem` | Bài chính, hero Rampart/Druid Heroes III | ✅ **nhân vật** |
| 2 | `Gem (Hero)` | `#REDIRECT [[Gem]]` (17 byte) | ✅ redirect |
| 3 | `Gem (Sorceress)` | Hồ sơ **riêng** cho campaign *New Beginning* | ✅ **nhân vật** |
| 4 | `Gem (Resource)` | `#REDIRECT [[Resource]]` (22 byte) | ❌ tài nguyên |
| 5 | `Gem (resource)` | `#REDIRECT [[Resource#Gems]]` (27 byte) | ❌ tài nguyên |
| 6 | `Gem Pond` | `#REDIRECT [[Mine]]` (18 byte) | ❌ công trình |
| 7 | `Gem pond` | `#REDIRECT [[Mine]]` (18 byte) | ❌ công trình |
| 8 | `Gems` | `#REDIRECT [[Resource#Gems]]` (27 byte) | ❌ tài nguyên |

**Không có trang disambiguation riêng** trên thelazy. Trang `Gem` tự gắn banner:

```
{{About|This article refers to the hero Gem. For the resource of the same name, see [[Gem (resource)]].}}
```

### 1.2 Liệt kê đầy đủ — Fandom (mightandmagic.fandom.com)

Truy vấn `list=allpages&apprefix=Gem` → **14 trang**; và `list=search&srsearch=Gem&srlimit=50`
→ `totalhits` không có trong response (schema Fandom khác), 50 kết quả trả về. Danh sách allpages **đầy đủ**:

| Tiêu đề | Nội dung | Liên quan? |
|---|---|---|
| `Gem` | **Bài về TÀI NGUYÊN**, mở đầu bằng hatnote `{{for|the Enroth character|Gem (Enroth)|the Ashan character|Gem (Ashan)}}` | ❌ (nhưng là **trang định hướng thực tế**) |
| `Gem (Enroth)` | ⭐ **Nhân vật Old Universe** — 5.340 ký tự, `refs=3` | ✅ **chính** |
| `Gem (character)` | `#REDIRECT [[Gem (Enroth)]]` (26 ký tự) | ✅ redirect |
| `Gem (Ashan)` | ⛔ **NHÂN VẬT KHÁC HẲN** — Heroes VII, New Universe | ⚠️ **bẫy** |
| `Gem Casket`, `Gem Mine`, `Gem Pond`, `Gem mine`, `Gems Mine`, `Gem of Restoration`, `Gemstone Floor 1/2/3`, `Gemstone Spire` | vật phẩm / công trình / địa điểm | ❌ |

### ⚠️ 1.2b Ba trường hợp "gần trùng" phải biết để không lặp lại lỗi Sandro (Xeen) / Haart (Cron)

1. **`Gem (Ashan)`** — nữ hero Heroes VII, class `Mystic`, sinh tại `Eridan's Crossing` trên `Ashan`.
   Bio game (nguyên văn, trong `{{text}}`):
   > *"Because of her otherworldly beauty, many believe Gem to be an Elf, when she is in fact Human.
   > This sorceress, born in the Free City of Eridan's Crossing nearly eight decades ago, became such a
   > dedicated protector of nature that the Druids of Irollan themselves welcomed her among their numbers.
   > What remains a mystery, though, is how she can still look so young."*

   ⚠️ **Cảnh báo cụ thể:** bio này **cố tình vọng lại** bio Old Universe (nữ, sorceress→druid, ~80 tuổi,
   trẻ mãi không rõ lý do). Rất dễ bị trích nhầm sang bài `gem` của Codex. **Đây là nhân vật New
   Universe, ngoài phạm vi dự án.**

2. **`Dryope`** — một hero HotA **khác** dùng **chính chân dung Gem**:
   `{{hero row|161, 19, 0|purple|Dryope|Ranger|image=Gem (HotA)}}` trong scenario `Tomb Raiders`.
   Tái dùng sprite, **không phải** Gem xuất hiện.

3. **`Dargem`** — hero HotA có chuỗi "gem" trong tên, xuất hiện ở `Chasing the Dream`,
   `The Life Guard`. Không liên quan.

**Bảng "Different characters with the same name"** trên `Heroes from other games` liệt kê
Solmyr, Kastore, Maximus, Crag Hack, Yog, Nymus, Ignatius — **Gem KHÔNG có trong đó**.
Nghĩa là thelazy coi Gem H1–H4 là **một** nhân vật liên tục.

### 1.3 Câu hỏi đồng nhất: H2, H3, H4 có phải MỘT người không?

**Kết luận: CÓ — và điều này có nguồn, không phải suy đoán của wiki.** Năm mắt xích độc lập:

| # | Bằng chứng | Nguồn | Tier |
|---|---|---|---|
| 1 | Bio game H3 tự nối nàng vào kỷ nguyên Heroes I–II: *"serving King Roland Ironfist during the Succession Wars"* | `h3wiki-herobios-txt` | **`T1` thật** |
| 2 | Prologue: *"a year has passed since Archibald and his Necromancer allies were defeated, ending the Succession Wars"* | `sod-clearing-the-border` | `T1*` |
| 3 | Day 1: *"When Delino learned I had been a general in the Enroth's Succession Wars"* | `sod-clearing-the-border` | `T1*` |
| 4 | Nàng **nhận ra Yog từ Enroth**: *"Hmm, I met him once in Enroth."* | `sod-agents-of-vengeance` Day 25 | `T1*` |
| 5 | Fulton ghi lại yêu cầu thiết kế họp khởi động H3: *"Keep specific heroes from HoMM2, like ... Gem the Druid ..."* | `fulton-fanstratics-27` | **`T4`** |

**H3 → H4:** bio Heroes IV nói *"over eighty years of wars and conflicts"* và
*"With the destruction of the old world"* — tự nối vào The Reckoning và vào một đời người dài
xuyên các game trước. Đây là **text game H4** (bọc trong `{{H4Story}}` / `{{text}}`, đúng chuẩn
`fandom-h4-hero-bios` và `h3wiki-h4-hero-bios` mà dự án đã dùng).

⚠️ **NHƯNG — H1 thì KHÁC.** Xem §4.3: liên tục Heroes I **chỉ có** ở mức roster + chân dung.
**Không có một dòng text kể chuyện nào** trong Heroes I nói về Gem (H1 không có hero biography).
Đừng viết "Gem xuất hiện từ Heroes I" như một claim tự sự — nó là claim **gameplay/roster**.

### 1.4 Bio Heroes IV — nguyên văn

Giống hệt nhau trên **hai** trung gian độc lập (thelazy `{{H4Story|Druid|...}}`, Fandom `{{text}}`),
khớp từng chữ:

> *"Even though Gem was at the center of over eighty years of wars and conflicts, she remained young
> and beautiful thanks to the waters of a special fountain. With the destruction of the old world, she
> no longer has access to those magical waters and is beginning to age normally again - something she
> desperately wants to avoid."*

⚠️ **STEP D:** trên Fandom câu này viết `[[Reckoning|destruction of the old world]]`.
**Chữ "Reckoning" KHÔNG hiển thị trong game** — nó là đích wikilink do người sửa wiki thêm.
Text game chỉ có *"the destruction of the old world"*. Đây đúng cái bẫy mà `fandom-h4-hero-bios`
đã ghi trong REGISTRY.

⚠️ Gem **không xuất hiện trong campaign Heroes IV nào.** Kiểm bằng
`list=backlinks&bltitle=Gem (Enroth)&bllimit=200` (200 backlink): chỉ có `Druid (H4)`, `Preserve`,
`Template:PreserveHeroH4` thuộc về H4 — **không** có trang campaign/scenario H4 nào. Nàng là hero
Preserve thuê được tiêu chuẩn, có bio, **không** có tuyến truyện H4.

---

## 2. PRIORITY 2 — Vai trò trong Shadow of Death, theo text game

### 2.0 Bảng phân biệt: PLAYABLE vs CHỈ ĐƯỢC NHẮC

Dựng từ trường `{{appear}}` của hai trang thelazy + đối chiếu `hero row` từng scenario.

| Campaign | Scenario | Vai trò | Ghi chú |
|---|---|---|---|
| *New Beginning* | `Clearing the Border` | 🎮 **PLAYABLE** (green) | class hiển thị **Sorceress (Campaign)** |
| *New Beginning* | `After the Amulet` | 🎮 **PLAYABLE** | cùng Clancy |
| *New Beginning* | `Retrieving the Cowl` | 🎮 **PLAYABLE** | cùng Clancy |
| *New Beginning* | `Driving for the Boots` | 🎮 **PLAYABLE** | cùng Clancy |
| *Unholy Alliance* | `Search for a Killer` | 💬 chỉ nhắc | người chơi là Gelu |
| *Unholy Alliance* | `Final Peace` | 🎮 **PLAYABLE** (green) | class **Druid** |
| *Unholy Alliance* | `Secrets Revealed` | 💬 chỉ nhắc | người chơi là Crag Hack |
| *Unholy Alliance* | `Agents of Vengeance` | 🎮 **PLAYABLE** (green) | cùng Gelu, class **Druid** |
| *Unholy Alliance* | `Wrath of Sandro` | 💬 chỉ nhắc | người chơi là Sandro |
| *Unholy Alliance* | `Invasion` | ⚔️ **ĐỊCH** (green, AI) | người chơi là **Sandro** (red) |
| *Unholy Alliance* | `To Strive, To Seek` | 🎮 **PLAYABLE** | cùng Gelu |
| *Unholy Alliance* | `Union` | 🎮 **PLAYABLE** (blue) | bốn hero |
| *Unholy Alliance* | `Fall of Sandro` | 🎮 **PLAYABLE** (blue) | bốn hero |
| *Specter of Power* | `Poison Fit for a King` | 💬 chỉ nhắc | POV Sandro |
| *Specter of Power* | `To Build a Tunnel` | ⚔️ **ĐỊCH** (pink) | chỉ là `hero row`, không có text truyện |

⚠️ **Sửa một hiểu nhầm dễ mắc:** `Invasion` — trang `Gem` ghi `{{enemy}}`, và điều đó **đúng**.
Đã kiểm header scenario: `| allies = {{red}}`, `| enemies = {{blue}}{{green}}`,
`| carry = {{Hn|Sandro}}` → người chơi **là Sandro**, Gem (green) là AI đối địch.
Nàng **không đổi phe**; chỉ là góc nhìn đổi.

### 2.1 `New Beginning` — Sandro tuyển mộ Gem như thế nào

**Region text** (`sod-after-the-amulet`) — vỏ bọc, nguyên văn:
> *"You have agreed to help a wizard's apprentice named Sandro.  Sandro's master, Ethric, needs an
> Amulet of the Undertaker to perform anti-necromancy research, but Ethric is an academician and
> Sandro is too inexperienced to go after the Amulet himself."*

**Prologue** — cách Gem hiểu về Sandro lúc đầu:
> *"I have met a Wizard named Sandro who is conducting research to combat necromancy.  He is creating
> a magical amulet, which will ward off the undead and wants to pay me a large sum of gold to find the
> pieces he needs to construct it.  He seems to think me quite the mercenary."*

⚠️ Chú ý mâu thuẫn nội tại **trong chính game**: prologue gọi Sandro là *"a Wizard"*, region text và
timed event Day 1 gọi hắn là *"a wizard's apprentice"*. Cả hai đều là text game.

**Day 21 — Sandro nâng cấp vỏ bọc** (`sod-after-the-amulet`):
> *"I received a very interesting letter from Sandro today.  Apparently he convinced his master I could
> be entrusted with the full story.  It seems that Ethric is doing more than just research.  He believes
> he has found a way to construct a necromancy suppressing artifact, but to do this he needs three lesser
> artifacts:  an Amulet of the Undertaker, a Vampire's Cowl and a pair of Dead Man's Boots.  Sandro offered
> me more gold to find the other two artifacts once I locate the Amulet."*

**Day 21 (cont) — Gem muốn GÓP TIỀN:**
> *"I wrote back to Sandro that Ethric's project was a worthwhile one and promised to search for the two
> artifacts after finding the Amulet of the Undertaker.  After sending off the letter, I decided to look
> up Ethric upon the completion of my quests and persuade him to let me donate money towards his research.
> I admire his values."*

**Day 49 — nàng CÓ nhận tiền, và lý do** (⭐ chốt lại điểm dự án đã ghi trong `sandro`):
> *"People are strange about gold.  If you don't let them give it to you, they don't know what to do and
> get upset.  I've gotten to the point where I just take it when they offer it to me - if they can afford
> it.  It's just easier that way.  I could tell Sandro wouldn't have known how to deal with me if I hadn't
> taken my payment; he was so certain he could buy my loyalty.  The funny thing is I would have helped his
> anti-necromancy research for free."*

**Lời cảnh báo bị bỏ qua** (`sod-retrieving-the-cowl`, Day 27):
> *"...She just looked at me with her wise, calm eyes and advised me to be careful, very careful about what
> I was doing, and it wouldn't be like the last time."*

⚠️ **STEP D + độ chính xác:** cụm cuối là ***"and it wouldn't be like the last time"*** — nguyên văn như
vậy trong wikitext (đọc như lỗi ngữ pháp của bản game, có thể gốc là *"so it wouldn't be…"*). Dự án hiện
diễn giải ý này ở `cloak-of-the-undead-king.md` — nên **đối chiếu lại nguyên văn** khi viết bài.

### 2.2 Epilogue — Gem phát hiện bị lừa (`sod-driving-for-the-boots`), nguyên văn ĐẦY ĐỦ

> *"Sandro has tricked me!  But to what purpose?  Why would he run off with the Dead Man's Boots without
> paying me?  Did he keep the money for himself?  Did he give Ethric the other artifacts?  He certainly
> couldn't have been an agent for Deyja - the undead troops I destroyed to get the artifacts were worth
> more than the artifacts themselves.  None of this makes sense!  I will have to write to Ethric in
> Bracada and tell Lord Fayette about this immediately."*

⭐ Điểm bi kịch: nàng biết **bị lừa**, nhưng vẫn tin **Ethric là người thật và tử tế**. Nàng định viết
thư cho Ethric — trong khi Ethric là một lich cổ. Khớp với `ethric.md` của dự án.

### 2.3 `Agents of Vengeance` — thư của Ethric, nguyên văn ĐẦY ĐỦ

Day 9, `{{Hn|Gem|0=}}` (⚠️ **timed event**, không phải prologue):
> *"I received a message from Ethric today.  Ethric said it had been decades Sandro was his apprentice.
> He said Sandro ran away and become a Necromancer!  There were more ill tidings.  Ethric said Sandro
> might be trying to construct a powerful artifact from all the artifacts I gathered for him.  I was so
> furious, I screamed.  None of my troops came near me for an hour.  I must pass these tidings on to
> Gelu and the Council of Elders."*

⚠️ Hai lỗi ngữ pháp **có trong bản game**, giữ nguyên: *"it had been decades Sandro was his apprentice"*
và *"ran away and become a Necromancer"*. Neo thời gian **"decades"** mà dự án đã dùng nằm ở đây.

### 2.4 ⭐⭐ GỐC GÁC GEM — Day 1, `Agents of Vengeance` (PHÁT HIỆN MỚI)

`{{Hn|Gem|0=}}`, nguyên văn:
> *"The doll got to me.  It looked just like the one my sister had right before she died.  I remember
> thinking she was the luckiest girl in the world to have a doll like that.  Then the horde of skeletons
> killed everyone in my village.  I was the only survivor.  I'm GLAD the Council of Elders choose me as
> one of the pair to punish Deyja."*

(`choose` — nguyên văn, lẽ ra là `chose`. Chữ `GLAD` viết hoa nguyên văn.)

**Vì sao đây là phát hiện quan trọng nhất của đợt research:** nó là **động cơ gốc** của Gem, và nó
**không có trong bio, không có trong prologue, không có trên bất kỳ bản tóm tắt nào**. Nó chỉ tồn tại
trong một timed event ngày 1. Đúng kiểu **BH-1**.

Ghép với hai mảnh khác thành một mạch nhất quán:
- `sod-after-the-amulet` Day 11: *"It's just that they remind me of a past I'd rather forget.
  I haven't seen moving trees since I was a little girl."*
- `sod-clearing-the-border` Day 29: *"...The only bodies they can't use are the small children because
  their bodies are too small.  I buried the children..."*

### 2.5 Liên minh bốn người — text game

**`Secrets Revealed`** Day 39 (POV Crag Hack) — mối nối đầu tiên:
> *"It seems you and Crag Hack are not the only ones fighting these necromancers.  A Ranger and a Druid,
> Gelu and Gem, are also fending off the forces of undead, but they are working within the borders of AvLee."*

**`Agents of Vengeance`** Day 25 (POV Gem) — ⭐ mối nối Enroth:
> *"To my surprise, an hour later some of my Elven scouts escorted in some Orc spies with a message for me.
> It was from a blue Barbarian hero named Yog.  Hmm, I met him once in Enroth.  He's with another Barbarian
> named Crag Hack.  I've heard of Crag too. ... What?!  Crag collected artifacts for Sandro, which DID
> combine into a powerful artifact!  Ethric was right!"*

Day 25 (cont) — nàng là người **chọn điểm hẹn**:
> *"...but afterwards I'll ask Yog and Crag to meet Gelu and myself at a place called Blagden."*

**`To Strive, To Seek`** Day 25 — ⭐ Gem là người **phát hiện ra mưu Sandro**, bằng scrying:
> *"Scrying in her bowl, Gem often learned for certain the nature of things around her.  She once told Gelu
> the way she learned of Sandro's ploy, that he was using Vilmar as a puppet to control Deyja from the
> shadows. ... He did not count on the cunning of the one called Crag Hack or the clever mind of Gem."*

⚠️ **STEP D:** trong wikitext là `[[Vilmar]]`, hiển thị **"Vilmar"** — game **không** nói "Finneas Vilmar"
ở dòng này.

**`To Strive, To Seek`** Day 33 — nét tính cách hiếm:
> *"Gelu, steely eyed as ever, renewed her steadfast approach to victory.  Gem, meanwhile, took a more
> spiritual course, choosing to perform several small rites of passing for the departed, an offering to the
> powers above to aid the fallen in their travels beyond."*

(⚠️ `renewed **her** steadfast approach` khi nói về Gelu — lỗi đại từ **có trong bản game**.)

**`Union`** prologue, `{{h|Gem}}` — Gem là người dẫn chuyện:
> *"We have collected the pieces of the Angelic Alliance, but Sandro learned of our efforts and blocked our
> path.  The bulk of his army now separates us from each other.  We must break through the Necromancer's army
> and converge upon one point.  Once we join the pieces of the Angelic Alliance, we can defeat Sandro.  If we
> fail, he will dominate all of Antagarich."*

**`Fall of Sandro`** prologue, `{{h|Gem}}` — ⭐ nguồn của cụm *"time of reckoning"* mà `the-reckoning.md` đã dùng:
> *"We face the Necromancer in his lair.  The time of reckoning has come, but our vengeance must be carried
> out swiftly.  Sandro has sent for reinforcements from others within Deyja.  Slow moving as undead are, they
> will still be here in four months.  If we have not defeated Sandro by then, he will surely rule all of
> Antagarich.  I shudder at the thought.  Failure is simply not an option."*

⚠️ **Epilogue của `Fall of Sandro` là của YOG, không phải Gem.** Người viết bài dễ gán nhầm:
> *"After realizing how corrupting these artifacts are, we decided to split them up into less powerful
> components and disperse them throughout Antagarich.  As for us, we decided to separate as well, to distance
> our thoughts from a disaster history may never record."*

**Góc nhìn Sandro về Gem** (`sod-wrath-of-sandro`, Day 12) — ⭐ chưa có trong Codex:
> *"Another old 'friend' of yours is now opposing you.  Gem, the lady Druid, has taken up arms and was
> responsible for the slaughtering of lord Fayette and his undead army.  Such a waste that turned out to be!
> She was able to defeat the entire army you had given him and slay a perfectly good Death Knight.  It was
> such a pity, he seemed like a nice fellow.  It doesn't matter.  She assembled the pieces for the Cloak of
> the Undead King.  Of course, she did send a letter to Ethric, tipping him off of your whereabouts.
> She'll make a lovely lich."*

**`Poison Fit for a King`** Day 20 (POV Sandro) — bản đầy đủ của câu dự án đã trích trong `sandro`:
> *"Your rage towards Crag Hack, Gem, Yog and that snippet Gelu is not easy to control.  Who would have thought
> two Barbarians would suddenly develop a conscience?  Not to mention a boy ranger and **a foreign druid**
> actually gathering together the resources to build an army large enough to defeat yours!"*

(⭐ *"a foreign druid"* — Sandro vẫn coi nàng là người ngoại quốc.)

### 2.6 `Final Peace` — tuyến Lord Fayette

**Region text:**
> *"Gem's employer, the AvLee border lord Fayette, has been killed by the Necromancers while on a secret
> mission.  Never able to leave an enemy defeated, the Necromancers have further humiliated Fayette by raising
> him as a Death Knight.  Gem can't accept this insult.  Lord Fayette's undead body must be destroyed to grant
> him final peace."*

**Prologue,** `{{h|Gem}}`:
> *"When I went to tell Lord Fayette about Sandro tricking me, I learned he left on a mission into Deyja while
> I was searching for the boots and had not yet returned.  So I scryed for Lord Fayette and discovered his
> mission had gone horribly wrong.  He had been killed by the Necromancers and... and... resurrected as a Death
> Knight!  Curse all Necromancers!  There is one last service I can do for my lord.  I will grant his soul final
> peace by destroying the undead body chaining it to this world.  I owe him that much."*

**`Search for a Killer`** Day 22 (POV Gelu) — Gem chủ động liên lạc trước:
> *"A letter arrived today from a Druid named Gem.  She wants to meet with you when you are finished with your
> business in Lord Falorel's land and look further into the recent events with the Necromancers."*

---

## 3. PRIORITY 3 — Nàng là ai: class, gốc gác, phe

### 3.1 Bio in-game Heroes III — `T1` THẬT ⭐

**STEP E:** đây là **trường `biography` của infobox**, KHÔNG phải mục `== Story ==`. Hai thứ khác tier hoàn toàn.

Nguyên văn từ `Translation Data/HeroBios.txt` dòng 58, cột EN (**giữ nguyên khoảng trắng đôi sau "Wars."**):
> *"Gem was one of the greatest Sorceresses that Enroth had ever seen, serving King Roland Ironfist during the
> Succession Wars.  Shortly after Roland had secured the throne of Enroth, Gem left for Erathia, finding a new
> home in AvLee."*

⭐ **Đây là `T1` thật** — string table trích từ file game, không qua diễn giải của fan.
Dự án đã dùng chính nguồn này trong `archibald-ironfist.md` để chốt "Roland thắng".

⚠️ **STEP D:** trên trang `Gem` của thelazy, cùng câu này viết `{{gl|Enroth (nation)|Enroth}}` và
`{{gl|Sorceress (class)|sorceresses}}`. Hiển thị vẫn là *"Enroth"* / *"Sorceresses"*. Text game
**không** phân biệt "Enroth (nation)" với "Enroth (continent)" — đó là wiki thêm vào.

### 3.2 Bio riêng của bản campaign (`Gem (Sorceress)`), `T1*`
> *"After her Deyjan raiders campaign, Gem agrees to help a wizard's anti-necromancy research by getting an
> Amulet of the Undertaker."*

### 3.3 ⚠️ MÂU THUẪN NGUỒN THẬT về class — cần xử lý trong bài

| Sản phẩm / bối cảnh | Class | Nguồn | Tier |
|---|---|---|---|
| Heroes I | Sorceress | roster/chân dung | `T6` (xem §4.3) |
| Heroes II | Sorceress | roster/chân dung | `T6` (xem §4.3) |
| Heroes III RoE / AB | **Druid** (Rampart) | `roe-manual-p125`, bio game | `T2*` + `T1` |
| Heroes III SoD, campaign *New Beginning* | **Sorceress (Campaign)** | game | `T1*` |
| Heroes III SoD, campaign *New Beginning* | **Druid** | **sách hướng dẫn in** `sod-manual-p14` | **`T2*`** |
| Heroes III SoD, campaign *Unholy Alliance* | **Druid** | game (`hero row ... |Gem|Druid`) | `T1*` |
| Heroes IV | Druid (Preserve) | Fandom `Gem (Enroth)` | `T1*` |

⚠️⚠️ **Dòng 4 và 5 mâu thuẫn nhau, và CẢ HAI đều là nguồn chính thức.** Sách in nói Druid; game nói
Sorceress. Đây **không** phải lỗi wiki — tôi đã đọc nguyên văn cả hai. Bài viết phải nêu cả hai,
gắn `DISPUTED`, **không được chọn một bên rồi im lặng**.

Ghi chú của game về chính điểm này (thelazy, mục `== Campaign vs. Standard hero ==`, **prose không dẫn nguồn**):
> *"her class is listed as Sorceress though she is still technically a Druid"*
→ **`T6`** — đây là **hòa giải của người sửa wiki**, không phải text game. Đừng trình bày như sự thật.

### 3.4 Chuyển đổi Sorceress → Druid: có nguyên cả một tuyến truyện (`sod-driving-for-the-boots`)

Toàn bộ nằm trong **timed events**, không có trong prologue/epilogue:

- **Day 12** ⭐ neo tuổi: *"I am in my sixty-first year as a Sorceress.  Over time you learn to protect
  yourself and your troops from ill magic."*
- **Day 20** — lời mời: *"Over breakfast he asked me to think about becoming a Druid. I was stunned for a
  moment, but then I shook my head and told him I was a Sorceress.  The old druid calmly took another bite
  and told me, from what he knew, being a Sorceress didn't necessarily prevent me from also being a Druid."*
- **Day 31** — *"While there are differences in specifics, the core philosophies are virtually identical."*
- **Day 34** — Amanda: *"Gem, if our two philosophies are as similar as you say, it may be a good idea to
  join them."* Gem: *"I would feel so disloyal to her and my sister Sorceresses."*
- **Day 45** — cơ chế lời thề: *"He explained that each Druid wrote their own oaths, and by lunch we had
  worked out a set of oaths I was happy with. ... submit my oaths to the Druid High Council."*
- **Day 48** — *"A part of me will always be a Sorceress, but I have evolved into a Druid, finally finding a
  new life for myself in Antagarich."*
- **Day 51** — *"my sister Sorcerers had approved my petition to join the Druids.  She hugged me and told me
  she thought this would be the 'New Beginning' she had hoped I would find in Antagarich."*
- **Day 52** — *"Soon I would be an AvLee hero and a Druid soon.  But first I had to get the Boots to Sandro."*
  (⚠️ *"soon ... soon"* — lỗi lặp **có trong bản game**.)

⚠️ **Điểm quan trọng về trình tự:** việc chuyển sang Druid **diễn ra TRONG scenario cuối**, tức là
**TRƯỚC KHI** hoàn tất nhiệm vụ và **TRƯỚC KHI** biết mình bị lừa. Prose trên thelazy nói
*"Once her quest for Sandro was complete, she changed her allegiance to AvLee and became a Druid"* —
**sai trình tự** (xem §6).

### 3.5 Gốc gác và phe — có nguồn

| Claim | Nguyên văn | Nguồn | Tier |
|---|---|---|---|
| Từ Enroth sang Antagarich | *"I traveled from Enroth across the ocean to Antagarich"* | `sod-clearing-the-border` D1 | `T1*` |
| Từng là **tướng** trong Succession Wars | *"I had been a general in the Enroth's Succession Wars"* | `sod-clearing-the-border` D1 | `T1*` |
| Lý do sang: mua **First Aid Tent** | *"a device invented in Antagarich that might end the nightmares... which she called a First Aid Tent"* | `sod-clearing-the-border` D1 | `T1*` |
| Chỉ huy đầu tiên: **Mayor Delino**, Clovergreen | *"I agreed to command Delino's militia"* | `sod-clearing-the-border` D1 | `T1*` |
| Clovergreen thuộc **Contested Lands**, đất Erathia | *"Clovergreen lies in the Contested Lands between Erathia, AvLee and Deyja. Currently these lands are Erathian territory"* | `sod-clearing-the-border` D1 | `T1*` |
| Sau đó theo **AvLee**, dưới Lord Fayette | *"It formally invited me to join his forces as a General as soon as my promise to Sandro was fulfilled."* | `sod-retrieving-the-cowl` D50 | `T1*` |
| Cuối cùng chịu lệnh **Council of Elders** của AvLee | *"the AvLee Council of Elders commanded Gem and myself"* | `sod-agents-of-vengeance` prologue | `T1*` |
| Thầy: **Amanda**, một Sorceress Enroth | *"I hope my former teacher, Amanda, is right."* | `sod-clearing-the-border` prologue | `T1*` |

**Tóm tắt tuyến phe:** Enroth (Roland) → Clovergreen Militia (Erathia, Mayor Delino) → Lord Fayette
(AvLee) → Council of Elders (AvLee). **Không phải** "Erathia hay AvLee" — mà là **cả hai, theo thứ tự**.

### 3.6 Chỉ số và specialty — sách hướng dẫn in (`T2*`)

**`sod-manual-p14`** (trang 14, mục *New Beginning*) — nguyên văn, giữ nguyên bố cục xuống dòng của bản chép:
```
Heroes: Druid
Gem
Race            Female Human
Secondary Skills  Basic Wisdom, Basic First Aid
Attack   0     Power       1
Defense  2     Knowledge   2
Unique Ability  Gem receives a 5% per level bonus to her First Aid skill.
```

**`roe-manual-p125`** (trang 125, mục **Druids**) — **giống hệt** khối trên, đặt giữa `Elleshar` và `Malcom`.
→ Hai sách hướng dẫn in độc lập cho cùng một bộ số. Chỉ số **không đổi** giữa RoE và SoD.

**Đối chiếu chéo với file game:** `Translation Data/HeroSpec.txt` chứa đúng chuỗi
*"Receives a 5% per level bonus to First Aid skill."* (dạng ngôi thứ ba, không có tên) — khớp.
⚠️ File này đánh chỉ số theo **thứ tự hero**, không theo tên, nên **không** gán chắc dòng nào là của Gem;
chỉ dùng để xác nhận chuỗi specialty tồn tại trong file game.

**Từ infobox thelazy** (`T1*`): town Rampart · gender Female · race Human · spell khởi đầu **Summon Boat**
(bản campaign: **Lightning Bolt**) · quân khởi đầu Centaur / First Aid Tent / Wood Elf · `s_mp = 1700`.
Trong **Horn of the Abyss**, spell khởi đầu đổi từ Summon Boat sang **Bless** trên bản đồ không có nước.

---

## 4. PRIORITY 4 — Heroes II (và Heroes I)

### 4.1 Bằng chứng `T4` — nàng là nhân vật kế thừa CÓ CHỦ Ý

`fulton-fanstratics-27` (Greg Fulton, Lead Designer Heroes III, ghi lại yêu cầu ở buổi họp khởi động H3):
> *"Keep specific heroes from HoMM2, like Sandro the Necromancer, Halon the Wizard, Lord Haart, Crag Hack
> the Barbarian, **Gem the Druid**, Yog the Barbarian, and Alamar the Warlock."*

⚠️ **Lưu ý tinh tế:** Fulton gọi nàng *"Gem the Druid"*, nhưng trong Heroes II nàng là **Sorceress**.
Fulton viết hồi tưởng và gán **class Heroes III** cho danh sách Heroes II. **Đừng** dùng câu này để
chứng minh nàng là Druid ở H2 — nó chứng minh **ý đồ kế thừa nhân vật**, không phải class H2.

Bổ sung từ `fulton-names-2023`, mục *On the Authorship of Names*:
> *"I created most of the Hero names, but not all of them.  Some were carried over from HoMM2."*
> *"Christian created all the hero bios..."* (tức bio H3 của Gem do **Christian Vanover** viết)

### 4.2 Roster Heroes I / Heroes II — có mặt, xác nhận hai wiki

- **thelazy `Heroes from other games`**, bảng *Assorted NWC Games*, dòng `Gem`:
  cột Heroes I → `Hero Gem (Heroes I).png` (chú thích **Sorceress**);
  cột Heroes II → `Hero Gem (Heroes II).png` (chú thích **Sorceress**);
  cột Heroes III → `Hero Gem (Sorceress).png` (**Sorceress**) + `Hero Gem (HotA).png` (**Druid**).
- **Fandom** `Category:Heroes I Sorceresses` (9 thành viên) → chứa `Gem (Enroth)`.
- **Fandom** `Category:Heroes II Sorceresses` (11 thành viên) → chứa `Gem (Enroth)`.
- **Fandom** `Sorceress (H2)`, gallery: `HeroGemII.jpg|[[Gem (Enroth)|Gem]]`.
- **thelazy** bảng H3→H4, nhóm `Preserve | Rampart | Conflux`: `{{H3H4row|Gem|Druid}}`.

**Trivia thelazy** (⚠️ **không dẫn nguồn** — `T6`, nhưng kiểm chứng được bằng roster):
> *"Gem, Luna, Crag Hack, and Sandro are the only heroes to appear in all four NWC Heroes of Might and
> Magic games."*

### 4.3 ⚠️ GIỚI HẠN PHẢI TÔN TRỌNG — không có TEXT KỂ CHUYỆN nào ở H1/H2

Heroes I và Heroes II **không có hero biography**. Toàn bộ bằng chứng H1/H2 là **roster + chân dung**.
Nghĩa là:

- ✅ Được viết: *"Gem có mặt trong roster Sorceress của Heroes I và Heroes II"* — `T1*`/`T6`.
- ✅ Được viết: *"Heroes III xác nhận nàng phục vụ Roland trong Succession Wars"* — `T1`, và đây là
  **hồi cố từ H3**, không phải text H2.
- ⛔ **KHÔNG** được viết: bất kỳ điều gì Gem *làm* trong cốt truyện Heroes II. **Không nguồn nào nói.**

### 4.4 Hai ghi chú của người sửa wiki gợi ý sprite Heroes II — CHỈ LÀ SUY ĐOÁN

Trên `sod-clearing-the-border`, dưới bảng timed events, **chữ nghiêng, không dẫn nguồn**:
> *"There is no check for any player to which this event applies. It was apparently intended that Gem would
> not only have a unique hero class in this campaign, but also her own sprite for battles, based on the
> Sorceress hero sprite from Heroes II, hence the black hair. This never materialized, and the event was left
> disabled."*
> *"The creatures in this dream match the creature lineup from the Sorceress town in Heroes II."*

⚠️ **`T6` — suy đoán ("apparently intended").** Phần *"event bị vô hiệu hoá"* là quan sát kỹ thuật kiểm
chứng được; phần *"intended ... based on the H2 sprite"* thì **không**. Tách hai thứ khi viết.

Text game thật sự đằng sau nó (`sod-clearing-the-border`, **Day 21**, event bị vô hiệu hoá):
> *"'My Lady Gem,' he asked 'Why is it your hair turns black before and during a battle?' ... 'Where I come
> from, most of the Sorcerers are raven haired.' ... 'It's just to confuse our enemies.  So it's harder for
> observers to tell which Sorcerer is actually on the field.    Of course, there aren't any other Sorcerers
> that I know of in Antagarich.'"*

⚠️⚠️ **BẪY LỚN:** event này **KHÔNG BAO GIỜ CHẠY trong game** (theo chính ghi chú trên: *"the event was
left disabled"*, và điều kiện là *"Deleted Unless Gem gets her horse"* với *"no check for any player"*).
Vậy mà **Fandom trích nó như sự thật** (mục Trivia, có `<ref>`). Nếu bài Codex dùng đoạn này,
**bắt buộc** ghi rõ nó là nội dung **không tiếp cận được khi chơi**.

---

## 5. PRIORITY 5 — Phát ngôn developer (`T4`)

### 5.1 `fulton-names-2023` — KHÔNG có gì về tên "Gem" (âm tính, đã enumerate)

- Trang: `Gregory Fulton/On Names in Heroes of Might and Magic III`, **98.499 byte, FETCHED**.
- `grep -c -w "Gem"` → **0**. (Mọi hit của chuỗi con "gem" đều nằm trong *arran**gem**ent*,
  *jud**gem**ent*, *mana**gem**ent*, *acknowled**gem**ent*.)
- Mục `=== Rampart ===` được **đọc toàn bộ**: liệt kê đúng 10 hero —
  `Mephala`, `Ufretin`, `Jenova`, `Thorgrim`, `Coronius`, `Uland`, `Elleshar`, `Melodia`, `Alagar`, `Aeris`.
  **Gem không có mặt.**

✅ **Claim âm tính này AN TOÀN** vì đã fetch trọn trang và grep cục bộ (**STEP B**), không dùng full-text search.

**Và có lý do hợp lý cho sự vắng mặt:** Fulton chỉ giải thích tên **do ông đặt**. Gem là tên **kế thừa
từ HoMM2** (§4.1) — nên đương nhiên không nằm trong danh sách sáng tác của ông. Sự vắng mặt này **củng cố**
tư cách nhân vật kế thừa chứ không phải khoảng trống đáng lo.

### 5.2 `Jennifer Bullard/Acid Cave Interview` — KHÔNG có gì về Gem (âm tính)

- 13.712 byte, FETCHED. `grep -i "gem"` → **1 hit duy nhất**, nằm trong chữ *"development"*. Không nhắc Gem.
- ⚠️ Đáng tiếc: Bullard **là Lead Designer của Shadow of Death** (theo `fulton-fanstratics-3`), tức là
  người có thẩm quyền nhất về Gem — nhưng bài phỏng vấn theo câu hỏi của fan và **không ai hỏi về nàng**.

### 5.3 ⚠️ Nhắc lại BH cay đắng nhất — ĐỪNG kết luận "không có developer commentary"

Có `T4` **thật** về Gem: `fulton-fanstratics-27` (§4.1). Nó **không** nằm trong `fulton-names-2023`.
Ai chỉ grep một trang rồi kết luận "không có" sẽ lặp lại đúng sai lầm nặng nhất của dự án.

---

## 6. PRIORITY 6 — SUSPECTED WIKI-ONLY CLAIMS (⛔ không được vào thân bài như sự thật)

### 6.1 thelazy — trang `Gem`, mục `== Story ==`

**STEP E, quan trọng:** `grep -c '<ref'` trên trang `Gem` = **0** và trên `Gem (Sorceress)` = **0**.
Trường `biography` của infobox là text game (`T1`); **toàn bộ mục `== Story ==` là prose không dẫn nguồn**.

| # | Claim của wiki | Đối chiếu text game | Phán quyết |
|---|---|---|---|
| 1 | *"She befriended Clancy and **recruited him** to help her in this quest."* | Game: *"he **surprised me by offering** to help me with the quest"* (`sod-after-the-amulet` D1) | ⛔ **BỊ PHẢN BÁC.** Clancy tự đề nghị. Chính trang `Clancy` của thelazy cũng viết *"He **offered** to help Gem"* — **wiki tự mâu thuẫn** |
| 2 | *"Gem served as a Sorceress for **sixty-one years** before becoming a Druid."* | Game: *"I am **in my sixty-first year** as a Sorceress"* (D12) | ⚠️ **Diễn giải lệch.** "Đang trong năm thứ 61" ≠ "đã phục vụ 61 năm rồi mới thành Druid". Dùng nguyên văn |
| 3 | *"**Once her quest for Sandro was complete**, she changed her allegiance to AvLee and became a Druid."* | Toàn bộ tuyến chuyển đổi diễn ra Day 20–52 **TRONG** scenario cuối, trước khi giao Boots | ⛔ **SAI TRÌNH TỰ** (xem §3.4) |
| 4 | *"In Erathia, she enlisted under the command of Mayor Delino."* | Khớp `sod-clearing-the-border` D1 | ✅ có nguồn |
| 5 | *"Through Clancy, she got to know Lord Fayette and the Druids."* | Fayette: khớp (D38 Cowl). Old Druid: *"he had heard much about me from both Mayor Delino and Clancy"* | ✅ có nguồn, hơi giản lược |
| 6 | *"her class is listed as Sorceress **though she is still technically a Druid**"* | Không text game nào nói vậy | ⛔ **hòa giải của editor** — `T6` |
| 7 | *"Gem, Luna, Crag Hack, and Sandro are the only heroes to appear in all four NWC games."* | Kiểm được bằng roster nhưng không dẫn nguồn | ⚠️ `T6`, kiểm chứng được |
| 8 | *"It was **apparently intended** that Gem would ... have her own sprite ... based on the Sorceress hero sprite from Heroes II"* | Suy đoán tự khai | ⛔ `T6` (xem §4.4) |

### 6.2 Fandom — `Gem (Enroth)`

`refs=3`, nhưng cả 3 `<ref>` đều chỉ trỏ tới scenario Heroes III; **phần đặc tả tính cách không có ref nào**.

| # | Claim không dẫn nguồn | Phán quyết |
|---|---|---|
| 1 | *"intelligent, conscious, and skillful in magic and scrying, but also sensitive and emotional"* | ⛔ đặc tả của editor |
| 2 | *"She has a flair for strategy as well as for **philosophical debates**, but tends to be **naive** when participating in causes for the greater good."* | ⛔ diễn giải của editor. "Naive" là **phán xét**, không phải text game |
| 3 | *"She is considered **one of the finest** Sorceresses and Druids"* | ⚠️ chỉ đúng một nửa: bio game nói *"one of the greatest **Sorceresses**"* — **không** nói về Druid |
| 4 | infobox `status = Alive (as of Heroes IV)` | ⚠️ suy ra từ việc có bio H4; **không nguồn nào nói nàng còn sống** |
| 5 | infobox `world = Enroth (planet)`, `affiliation = Forest {{icon-H1}}` | ⛔ gán của editor cho H1 |
| 6 | infobox `introduced = Heroes of Might and Magic: A Strategic Quest` | ⚠️ mức roster, không có text tự sự (§4.3) |
| 7 | *"She is the only hero in the game to have a unique class name."* | ⚠️ `T6`, kiểm chứng được, chưa kiểm |
| 8 | *"She **scorns necromancy for the pain it brings to living creatures**"* | ⚠️ diễn giải hợp lý và **có** text chống lưng (D29 Clearing the Border), nhưng câu chữ là của editor |

### 6.3 ⚠️ Fandom chép SAI một câu trích — đã bắt được

Fandom, mục Quotes, ghi:
> *"I don't think it's wrong to hate the **hateful** or not forgive the **unforgivable**."*

Text game (`sod-retrieving-the-cowl`, Day 30) viết hoa:
> *"I don't think it's wrong to hate the **Hateful** or not forgive the **Unforgivable**."*

Fandom cũng gán nguồn là *"New Beginning campaign"* chung chung, **không nêu scenario**. Đây đúng
cảnh báo đã có trong REGISTRY: **trung gian chép trung thực nhưng không luôn chép đúng**. Dùng bản thelazy.

---

## 7. SOURCE LIST

`FETCHED` = đã tải và đọc nguyên văn trong đợt này.
Cột "mới?" cho biết key đã có trong `REGISTRY.md` hay cần thêm.

### 7.1 Nguồn tier `T1` — file game thật

| key đề xuất | URL chính xác | tier | trạng thái | bytes | mới? |
|---|---|---|---|---|---|
| `h3wiki-herobios-txt` | `https://heroes.thelazy.net/index.php?title=Translation Data/HeroBios.txt&action=raw` | **`T1`** | FETCHED | 168.918 | ✅ đã có |
| `h3wiki-herospec-txt` | `https://heroes.thelazy.net/index.php?title=Translation Data/HeroSpec.txt&action=raw` | **`T1`** | FETCHED | 105.850 | 🆕 **MỚI** — ⚠️ đánh chỉ số theo thứ tự hero, **không** theo tên |

### 7.2 Nguồn tier `T2*` — sách hướng dẫn in, thelazy chép theo trang

| key đề xuất | URL chính xác | tier | trạng thái | bytes | mới? |
|---|---|---|---|---|---|
| `sod-manual-p14` | `https://heroes.thelazy.net/index.php?title=Shadow of Death Manual Page 14&action=raw` | `T2*` | FETCHED | 1.564 | ✅ đã có |
| `sod-manual-p4` | `https://heroes.thelazy.net/index.php?title=Shadow of Death Manual Page 4&action=raw` | `T2*` | FETCHED | 1.229 | 🆕 **MỚI** — mở đầu thư Yog |
| `sod-manual-p5` | `https://heroes.thelazy.net/index.php?title=Shadow of Death Manual Page 5&action=raw` | `T2*` | FETCHED | 1.156 | ✅ đã có |
| `roe-manual-p125` | `https://heroes.thelazy.net/index.php?title=Restoration of Erathia Manual Page 125&action=raw` | `T2*` | FETCHED | 2.350 | 🆕 **MỚI** — khối chỉ số Druids |

### 7.3 Nguồn tier `T1*` — text game qua thelazy (scenario)

Tất cả đều `FETCHED` trong đợt này qua
`https://heroes.thelazy.net/api.php?action=query&titles=...&prop=revisions&rvprop=content&rvslots=main&format=json&formatversion=2`

| key | trang | ký tự | mới? |
|---|---|---|---|
| `sod-clearing-the-border` | `Clearing the Border` | 9.710 | ✅ đã có |
| `sod-after-the-amulet` | `After the Amulet` | 12.404 | ✅ đã có |
| `sod-retrieving-the-cowl` | `Retrieving the Cowl` | 14.699 | ✅ đã có |
| `sod-driving-for-the-boots` | `Driving for the Boots` | 12.995 | ✅ đã có |
| `sod-search-for-a-killer` | `Search for a Killer` | 8.076 | ✅ đã có |
| **`sod-final-peace`** | `Final Peace` | 7.695 | 🆕 **MỚI** |
| `sod-secrets-revealed` | `Secrets Revealed` | 12.469 | ✅ đã có |
| `sod-agents-of-vengeance` | `Agents of Vengeance` | 10.064 | ✅ đã có |
| `sod-wrath-of-sandro` | `Wrath of Sandro` | 8.474 | ✅ đã có |
| `sod-invasion` | `Invasion` | 17.544 | ✅ đã có |
| `sod-to-strive-to-seek` | `To Strive, To Seek` | 9.177 | ✅ đã có |
| `sod-union` | `Union` | 20.094 | ✅ đã có |
| `sod-fall-of-sandro` | `Fall of Sandro` | 19.240 | ✅ đã có |
| `sod-poison-fit-for-a-king` | `Poison Fit for a King` | 10.737 | ✅ đã có |
| `sod-to-build-a-tunnel` | `To Build a Tunnel` | 5.085 | ✅ đã có |
| `sod-unholy-alliance` | `Unholy Alliance` | 9.355 | ✅ đã có |
| **`sod-new-beginning-campaign`** | `New Beginning` | 3.732 | 🆕 **MỚI** (trang campaign, khác các scenario) |

### 7.4 Trang wiki hỗn hợp tier — ⚠️ **STEP E: phải gắn tier THEO TỪNG MỤC**

| key đề xuất | URL | tier theo mục | trạng thái | bytes | mới? |
|---|---|---|---|---|---|
| `h3wiki-gem` | `https://heroes.thelazy.net/index.php?title=Gem&action=raw` | infobox `biography` → **`T1`** · `== Story ==` prose → **`T6`** · `== Trivia ==` → `T1*` (dẫn scenario) · `{{appear}}` → `T1*` | FETCHED | 6.066 | 🆕 **MỚI** · `grep -c '<ref'` = **0** |
| `h3wiki-gem-sorceress` | `https://heroes.thelazy.net/index.php?title=Gem (Sorceress)&action=raw` | infobox `biography` → `T1*` · prose → `T6` | FETCHED | 2.095 | 🆕 **MỚI** · `refs` = **0** |
| `fandom-gem-enroth` | `https://mightandmagic.fandom.com/api.php?action=parse&page=Gem (Enroth)&prop=wikitext&format=json&formatversion=2` | khối `{{text}}` → `T1*` · prose mở đầu → **`T6`** · infobox → `T6` | FETCHED | 5.340 ký tự | 🆕 **MỚI** · `refs` = 3 |
| `h3wiki-heroes-from-other-games` | `https://heroes.thelazy.net/index.php?title=Heroes from other games&action=raw` | bảng roster → `T1*` · Trivia → `T6` | FETCHED | 17.578 | 🆕 **MỚI** |
| `h3wiki-clancy` | `https://heroes.thelazy.net/index.php?title=Clancy&action=raw` | prose → `T6` | FETCHED | 2.912 | 🆕 **MỚI** |
| `h3wiki-amanda` | `https://heroes.thelazy.net/index.php?title=Amanda&action=raw` | prose → `T6` | FETCHED | 146 | 🆕 **MỚI** — stub |

### 7.5 Nguồn `T4` — phát ngôn developer

| key | nội dung | trạng thái | mới? |
|---|---|---|---|
| `fulton-fanstratics-27` | *"Keep specific heroes from HoMM2, like ... Gem the Druid ..."* | đã có trong REGISTRY | ✅ đã có |
| `fulton-names-2023` | `https://heroes.thelazy.net/index.php?title=Gregory Fulton/On Names in Heroes of Might and Magic III&action=raw` — 98.499 byte, FETCHED, **0 hit cho "Gem"** | FETCHED | ✅ đã có |
| `bullard-interview-2013` | `https://heroes.thelazy.net/index.php?title=Jennifer Bullard/Acid Cave Interview&action=raw` — 13.712 byte, FETCHED, **0 hit cho "Gem"** | FETCHED | ✅ đã có |

### 7.6 Nguồn định hướng / loại trừ

| key đề xuất | URL | tier | trạng thái | mới? |
|---|---|---|---|---|
| `fandom-gem-ashan` | `https://mightandmagic.fandom.com/api.php?action=parse&page=Gem (Ashan)&prop=wikitext&format=json&formatversion=2` | `T1*` (New Universe) | FETCHED, 1.269 ký tự | 🆕 **MỚI** — ⛔ chỉ dùng để **loại trừ** |
| `fandom-gem-resource` | `...&page=Gem&...` | — | FETCHED, 2.071 ký tự | 🆕 hatnote định hướng |

---

## 8. GAPS — không tìm được, đã thử gì, trả về gì

| # | Thứ cần | Đã thử | Kết quả | Đánh giá |
|---|---|---|---|---|
| 1 | Text kể chuyện về Gem trong **Heroes I / Heroes II** | `Category:Heroes I Sorceresses`, `Category:Heroes II Sorceresses`, `Sorceress (H2)`, `Heroes from other games` | Chỉ có roster + chân dung. **H1/H2 không có hệ thống hero biography** | ⚠️ Nhiều khả năng **không tồn tại**, không phải lỗi tìm kiếm |
| 2 | Ngày/năm cụ thể cho đời Gem | thelazy `Timeline` | **434 byte — chỉ là một FILE ẢNH** (`Timeline.png`), không có text đọc được | ❌ Không dùng được bằng công cụ text. Trang tự dẫn sang `Talk:Timeline` (= `h3wiki-talk-timeline`, dự án đã có) |
| 3 | Xuất hiện của Gem trong **campaign Heroes IV** | `list=backlinks&bltitle=Gem (Enroth)&bllimit=200` (200 backlink) | Chỉ `Druid (H4)`, `Preserve`, `Template:PreserveHeroH4`. **Không** campaign/scenario H4 nào | ✅ Âm tính **đã enumerate** — nàng không có tuyến truyện H4 |
| 4 | "Special fountain" trong bio H4 là gì | Chưa truy | — | 🔜 Chưa làm. Đáng đào: là mắt xích duy nhất giải thích tuổi thọ |
| 5 | Bio Heroes IV ở dạng file game (`T1` thật) | Chưa tìm được bản tương đương `HeroBios.txt` cho H4 | `Translation Data/*` trên thelazy **chỉ có H3** (đã liệt kê đủ 57 trang) | ⚠️ Bio H4 đành ở `T1*` |
| 6 | Phát ngôn của **Jennifer Bullard** riêng về Gem | `Jennifer Bullard/Acid Cave Interview` | 0 hit | ⚠️ Bullard là Lead Designer SoD — **không ai hỏi về Gem**. Xem `bullard-papers-ut-austin` (401) |
| 7 | Chỉ số/roster Gem trong Heroes I & II | Chưa truy sách hướng dẫn H1/H2 | — | 🔜 Chưa làm |

**Không có URL nào bị FortiGuard chặn trong đợt này.** Không dùng `web.archive.org`;
không đụng `celestialheavens.com`. Mọi fetch đều HTTP 200.

---

## 9. NOTE KIỂM SOÁT CHẤT LƯỢNG — sáu bước bắt buộc đã làm gì

| Bước | Đã làm | Kết quả |
|---|---|---|
| **A — disambiguation trước** | Enumerate `apprefix=Gem` trên **cả hai** wiki **trước mọi fetch khác** | 8 trang thelazy + 14 trang Fandom, **liệt kê đủ ở §1.1/§1.2**. Bắt được `Gem (Ashan)`, `Dryope` (dùng chung chân dung), `Dargem` |
| **B — không search cho claim âm tính** | 3 claim âm tính, cả 3 đều dựng bằng **enumerate + grep cục bộ**: (a) Fulton — fetch trọn 98.499 byte; (b) campaign H4 — 200 backlink; (c) **toàn bộ 172 campaign scenario** qua `categorymembers` rồi bulk-fetch **172/172** và grep `\bGem\b` | Không dùng full-text search ở bất kỳ đâu |
| **C — đọc trọn trang** | Đọc đủ `==== Events ====`, `=== Timed events ===` của mọi scenario chính | ⭐ **Ba phát hiện lớn nhất đều nằm trong timed event, không trong prologue**: gốc gác (AoV D1), tuổi 61 (DftB D12), lý do mắt xanh (FP D6) |
| **D — wikilink ≠ text game** | Đánh dấu từng chỗ | `{{gl|Druid\|Sorceress}}` → hiện **"Sorceress"** · `[[Enroth (nation)\|Enroth]]` → hiện **"Enroth"** · `[[Reckoning\|destruction of the old world]]` → **"Reckoning" KHÔNG hiện trong game** · `[[Vilmar]]` → **"Vilmar"**, không phải "Finneas Vilmar" |
| **E — tier thay đổi trong cùng trang** | `grep -c '<ref'` trên mọi trang trích làm sự thật | `Gem` = **0** · `Gem (Sorceress)` = **0** · `Gem (Enroth)` = **3**. Bảng tier-theo-mục ở §7.4 |
| **F — không suy từ metadata CDX** | Không dùng archive.org | Không áp dụng. Không trang nào bị suy đoán nội dung — trang nào không đọc được thì ghi thẳng ở §8 |

### ⚠️ Ba cảnh báo chuyển tiếp cho người viết bài

1. **Mâu thuẫn class (§3.3) là mâu thuẫn NGUỒN THẬT, không phải lỗi wiki.** Sách in `T2*` nói Druid,
   game `T1*` nói Sorceress, cho **cùng một campaign**. Phải gắn `DISPUTED` và nêu cả hai.
2. **Event "tóc đen" (§4.4) KHÔNG BAO GIỜ chạy trong game** — nhưng Fandom trích nó như sự thật,
   và trang `Gem` của thelazy đưa nó lên mục Trivia. Nếu dùng, **bắt buộc** ghi rõ tình trạng vô hiệu hoá.
3. **Ba claim của thelazy đã bị text game phản bác hoặc làm lệch** (§6.1 mục 1, 2, 3). Riêng
   *"recruited Clancy"* thì **chính trang `Clancy` của thelazy nói ngược lại** — wiki tự mâu thuẫn.
