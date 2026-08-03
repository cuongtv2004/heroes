# Dossier research thô — `archibald-ironfist` (Archibald Ironfist)

- **Ngày:** 2026-08-03
- **Loại:** dossier thô, KHÔNG xuất bản (nằm trong `sources/raw/`)
- **Phạm vi đã làm:** PRIORITY 1 ✅ · PRIORITY 2 ✅ · PRIORITY 3 ✅ · PRIORITY 4 ✅ (một phần — xem `GAPS`)
- **Cách fetch:** `curl` trực tiếp (Git Bash trên Windows). Cụ thể:
  - `curl -sL "https://web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm"` → **VÀO ĐƯỢC**, 23.142 byte, đọc toàn bộ 288 dòng text.
  - `curl -s -A "Mozilla/5.0 Research" "https://heroes.thelazy.net/index.php?title=PAGE&action=raw"` → cần **User-Agent**; không có UA thì trả **rỗng** (lần gọi đầu tiên cho `Archibald` trả 0 byte, thêm UA thì ra 8.937 byte). ⚠️ **Ghi chú access mới cần thêm mục này.**
  - `curl -s "https://mightandmagic.fandom.com/api.php?action=parse&page=PAGE&prop=wikitext&format=json&formatversion=2"` → OK.
  - Fandom **có** CirrusSearch (`insource:` chạy được) — khác thelazy.
- **Môi trường:** không có `python3` trong Bash tool (Git Bash trên Windows). Phải giải JSON bằng `sed`.

---

## PRIORITY 1 — nguồn chính thức và bio in-game

### 1.1 ⭐ `The Diaries of Archibald` — site chính thức 3DO (FETCH-VÀ-ĐỌC TOÀN BỘ)

URL: `https://web.archive.org/web/20001017212754/http://www.3do.com/products/pc/mm7/story/story.htm`
(bên trong trang, `__wm.wombat` khai snapshot gốc là `http://www.3do.com:80/products/pc/mm7/story/story.htm` @ `20000817185733`)

Trang chứa **4 văn bản**: `The Diaries of Archibald`, `The Story`, `The Black Rose` (Bard Tanni), `The Silence` (Bard Tanni). Diaries có **đúng 3 entry**. Đây là **text manual MM7**, Archibald tự kể ở ngôi thứ nhất — **T2** (nguồn chính thức nhà phát hành, không phải file game trích trực tiếp).

**Đã đọc hết trang** — sau `The Silence` không còn mục nào nhắc Archibald (grep `archibald|ironfist|deyja|necroman` trên phần còn lại: 0 hit).

#### Entry 1 — **11 June 1165** (nguyên văn, trích các đoạn quyết định)

> "Free at last! Never again will I take for granted what it means to bend limb and breathe air. But what air do I breathe? What land do I flee across? It is my Enroth, surely, but so much has changed in **the ten years I have been my brother's coat rack—made an insensate stone statue by his pet wizard, Tanir**. If it wasn't for those fool "adventurers" I'd still be there now. Tanir! I promise you I will repay the insult one day. And repay it with usurious interest."

> "I am a hunted man, but have found refuge in **the remote estate of my colleague in the necromatic arts, Nimbus**. His apprentices tell me that their master has sailed for Erathia. […] all I can derive is that the **Necromancer's Guild has some bold plan for Erathia**. Perhaps I should join them?"

> "Both my hated brother, **Roland Ironfist**, and his loathsome queen **Catherine** are absent. Roland is, by all accounts, **taken by strange demons**. Catherine **left for Erathia five months ago to attend her father's funeral** and has not been heard from since. Their brat, **Nicolai**, sits on the throne with the loutish **Wilbur Humphrey** standing as Regent."

> "But first, I must rebuild. **With no nation**, it is as if I am once again at the beginning of things."

> (về học trò của Nimbus) "What endless pride they take in their zombified rats and mice! Bah, the useless things fall apart inside of hours. Pathetic."

#### Entry 37 — **23 October 1167** ⚠️ *(3DO)* / **23 October 1166** *(thelazy)* — xem §1.5

> "Nimbus returned to his estates bringing with him a small party of Necromancers — **apparently all of any power that remained in Enroth** — he was gathering to take to Deyja in Erathia so that they might serve the lich-king, Nicolas Gryphonheart. Yes, that Gryphonheart! Catherine's father."

> "The Erathian guild has made a bold and perhaps foolhardy play for power. **The guild leader and king of Deyja, Deathknell, sought to take the Erathian throne by assassinating Gryphonheart and then reanimating him as a lich, bound to his service. Well, he got as far as the reanimation, but the binding did not take. Instead, the lich killed Deathknell.** Now Erathia and Deyja have a new king…and the guild has a new leader."

> "Now Gryphonheart has called the Necromancer Guild to his aid, and I and the Necromancers of Enroth are heeding the call. He fights his daughter, Catherine. That is a cause I can hearken to, indeed! **Incidentally, this little mission is now my mission. I took it from Nimbus in the guild Challenge of Dominance. Needless to say, I won.**"

> "It is hard to believe that this is the same guild of **Henden'lal** or **Neberneith**! Those luminaries would never have let things become as they have were they still around."

#### Entry 143 — **5 August 1168** ⚠️ *(3DO)* / **5 August 1167** *(thelazy)*

> "In her victory speech, as it was reported to me — I was, to be sure, nowhere near — Catherine made much ado about stability. True, the "dark and vile forces who had wronged her father so," were defeated, AND her father "now lies in the state of natural quietude he deserves," AND "the people of Erathia can lay down their swords safe in the knowledge that peace reigns instead of terror.""

> "**For as the lich, Gryphonheart, replaced Deathknell, so have I replaced Gryphonheart.** Catherine faces a more devious opponent in me. What my predecessors used like a bludgeon, I will use as a tailor's needle. The Necromancer Guild, under my leadership, will enter a golden age of advance. Even now, our new laboratory of research is producing new knowledge."

> "But all plots must begin somewhere or remain formless. **Perhaps my seed of discontent will root in those fertile "disputed lands?"** Time will tell, and the telling will be against my brother and his wife! So swear I here!"

**Chữ ký (nguyên văn, 3 dòng):**

> Archibald Ironfist
> **Guildmaster of Necromancers**
> **Rightful King of Enroth**

### 1.2 🔴 PHÁT HIỆN LỚN NHẤT — hai wiki đều **hiểu sai** cách Archibald lên ngôi

Game text (Entry 37 + 143) nói **HAI sự kiện tách rời**:

1. **Challenge of Dominance** với Nimbus → Archibald thắng, và cái hắn giành được là **"this little mission"** (quyền chỉ huy đoàn Necromancer Enroth sang Deyja). Xảy ra **trước khi** Gryphonheart bị tiêu diệt.
2. **Thay thế Gryphonheart** → "so have I replaced Gryphonheart". Đây mới là lúc hắn thành guild leader + vua Deyja. Xảy ra **sau** khi Catherine thắng (Entry 143).

Nhưng:

- `thelazy` trang `Archibald` (văn wiki, NGOÀI template): "After the lich form of King Nicolas Gryphonheart is put to rest, **Archibald battles Nimbus for the title of King of Deyja**, and wins."
- Fandom `Archibald Ironfist` (văn wiki): "**Defeating Nimbus in the guild Challenge of Dominance, Archibald assumed control over the now-vacant throne of Deyja.**"

→ Cả hai **gộp** hai sự kiện thành một và **gán nhân quả** mà game text không có. Cả hai cũng đặt Challenge of Dominance **sau** khi Gryphonheart bị tiêu diệt, trái với Entry 37.

**Còn tệ hơn:** `thelazy` **tự mâu thuẫn với chính nó**. Trang `Nimbus` (văn wiki) viết: "Archibald battled Nimbus for the title of **guildmaster** and won, becoming the new leader of **the Enrothian necromancers who joined the forces of Deyja**. […] Following the victory, **Archibald became the new ruler of Deyja**." — tức trang `Nimbus` tách đúng hai sự kiện, còn trang `Archibald` gộp lại. **Hai trang cùng wiki nói khác nhau.**

Ghi chú cho người viết bài: dossier `deyja-dossier-2026-08-02.md` dòng 125 đã ghi "Archibald thắng chức guild bằng **đấu tay đôi** với Nimbus" — cần **sửa lại**: game text không nói đấu tay đôi, và cái thắng được là quyền chỉ huy đoàn quân, không phải chức guildmaster.

### 1.3 ✅ "Deathknell" — GIẢI QUYẾT câu hỏi treo của `deyja-dossier`

`deyja-dossier-2026-08-02.md` dòng 89–90 và 461 để treo: *"trong The Diaries of Archibald (manual MM7), Finneas được gọi là **Deathknell**. Cần xác minh nguồn gốc."*

**Đã xác minh trên nguồn chính thức 3DO** (không chỉ trên wiki): Entry 37 gọi đích danh **"the guild leader and king of Deyja, Deathknell"**, và mô tả đúng chuỗi hành động của Finneas Vilmar (ám sát Gryphonheart → hồi sinh thành lich → binding thất bại → bị chính lich giết).

- Hai tên chỉ **cùng một vai** — nhưng đây là **INFERENCE**, không phải EXPLICIT. Không nguồn nào nói "Deathknell = Finneas Vilmar".
- Cả `thelazy` và Fandom đều đơn phương dịch "Deathknell" thành "Finneas Vilmar" trong văn wiki, **không ghi chú** rằng manual dùng tên khác. Đây là claim wiki không dẫn nguồn.

### 1.4 Bio in-game (`Translation Data`) — **T1 thật**, kết quả ÂM

Đã grep `archibald` trên **7 string table** trích trực tiếp từ game HoMM3:

| File | byte | hit `archibald` |
|---|---|---|
| `HeroBios.txt` | 168.918 | **0** |
| `CampText.txt` | 12.238 | **0** |
| `CAMPDIAG.TXT` | 59.146 | **0** |
| `CAMPHIGH.TXT` | 3.359 | **0** |
| `GENRLTXT.TXT` | 154.975 | **0** |
| `HeroSpec.txt` | 105.850 | **0** |
| `regions.txt` | 29.323 | **0** |
| `advevent.txt` | 117.313 | **0** |

→ **Archibald KHÔNG có bio hero trong HoMM3** (hắn không phải hero HoMM3). Kết luận này là claim **phủ định đã săn chủ động**, không suy từ im lặng.

**NHƯNG** `HeroBios.txt` cho **hai bio T1 nhắc Archibald/Roland** — đây là chống lưng canon mạnh nhất tìm được:

`HeroBios.txt` dòng 180 (bio **Alamar**, hero Dungeon HoMM3) — **T1 EXPLICIT**:

> "**Alamar served Archibald Ironfist during the succession wars, and was barely able to escape Enroth following Archibald's defeat.** He has since taken up residence in Nighon where he secretly serves the Dungeon Overlords."

`HeroBios.txt` dòng 58 (bio **Gem**) — **T1 EXPLICIT**:

> "Gem was one of the greatest Sorceresses that Enroth had ever seen, **serving King Roland Ironfist during the Succession Wars. Shortly after Roland had secured the throne of Enroth**, Gem left for Erathia, finding a new home in AvLee."

`HeroBios.txt` dòng 12 (bio **Lord Haart**) — **T1**, nhắc Roland: "…his service to the crown of Erathia has been as spotless as it was to **Roland Ironfist before the Succession Wars**."

→ **Hai bio T1 độc lập xác nhận Archibald THUA và Roland giữ ngai Enroth.** Đây là chốt canon cho câu hỏi "ai thắng theo canon" ở PRIORITY 2 — mạnh hơn nhiều so với câu văn wiki "Roland's campaign is the canonically true one".

### 1.5 🔴 MÂU THUẪN NGUỒN — ngày của Entry 37 và Entry 143 lệch **đúng 1 năm**

| Entry | Site chính thức **3DO** (T2) | `thelazy` (T2*, chép lại manual) |
|---|---|---|
| Entry 1 | 11 June **1165** | 11 June **1165** ✅ khớp |
| Entry 37 | 23 October **1167** | 23 October **1166** ❌ |
| Entry 143 | 5 August **1168** | 5 August **1167** ❌ |

Đã verify bằng `grep -oE "(1[0-9] June|23 October|5 August) 11[0-9][0-9]"` trên HTML thô của 3DO và `grep -E "^(11 June|23 October|5 August)"` trên wikitext thô của thelazy. **Không phải lỗi đọc của tôi.**

**Đây KHÔNG phải lỗi chép đơn lẻ** — `thelazy` xây cả timeline trên mốc 1166: trang `Nimbus` (văn wiki) viết "Nimbus gathered remnants of the Necromancer's Guild in Enroth **by 1166 AS**". Tức thelazy nhất quán nội bộ với con số của nó.

**Trọng số:** `deyja-dossier-2026-08-02.md` dòng 178–180 đã dùng **1167-10-23** và **1168-08-05** (lấy từ Fandom, Fandom ref *Diaries*). Vậy **3DO + Fandom = 1167/1168**, còn **thelazy = 1166/1167**. Nguồn chính thức của nhà phát hành thắng → **1167/1168 là con số nên dùng**, và ghi thelazy là DISPUTED.

⚠️ **Chưa giải quyết:** vì sao cả hai vẫn khớp ở Entry 1 (1165)? Nếu là lỗi chép một chỗ thì thường sai cả ba hoặc sai ngẫu nhiên. Có thể **manual in ra tồn tại hai bản** (bản in giấy vs. bản web 3DO). **Cần xem scan manual MM7 thật để chốt.**

### 1.6 Vai trò vua Deyja — hai mốc

**Mốc lên ngôi** — game text T2, Entry 143: "so have I replaced Gryphonheart", chữ ký "Guildmaster of Necromancers".

**Mốc bị Kastore đảo chính** — **KHÔNG tìm được game text**. Chỉ có văn wiki:

- `thelazy` trang `Tularea` (văn wiki): "Clanker's Lab […] This is where **Archibald retreated to after being deposed as the King of Deyja by Kastore**."
- `thelazy` trang `Archibald` (văn wiki): "he is **outmaneuvered by Kastore** who eventually seizes power from under him and **redirects the Necromancers towards studies of the Heavenly Forge, instead of necromancy**."
- Fandom (văn wiki): "Finally, the time came when **Kastore asserted his claim to Deyja's throne**. […] Archibald and his few loyalists **bitterly departed Deyja, settling in Clanker's Lab**."

→ Xem `SUSPECTED WIKI-ONLY CLAIMS` #1.

**Chống lưng gián tiếp cho việc Archibald mất quyền cho các Advisor — T4 Lead Designer** (§3.3): Fulton xác nhận "**Archibald's former 'Advisors'** restored production to […] the 'Heavenly Forge'" — chữ **"former"** ngụ ý hắn đã mất họ, và nội dung khớp với "redirects the Necromancers towards […] the Heavenly Forge".

### 1.7 ❌ Câu "deposed lord of Deyja and one of the most hated men in history, offered aid for reasons of his own" — **KHÔNG XÁC MINH ĐƯỢC**

Đã tìm ở **6 chỗ**, tất cả 0 hit:

1. Toàn văn trang 3DO MM7 story (đọc hết 288 dòng) — không có.
2. Fandom `insource:"most hated men in history"` → `{"search":[]}` (Fandom **có** CirrusSearch nên kết quả rỗng là đáng tin).
3. Fandom `insource:"reasons of his own"` → rỗng.
4. thelazy: `Archibald`, `Nimbus`, `Tularea`, `Land of the Giants`, `Succession Wars`, `Lost Lore`, `Frozen Highlands`, `Zog` — đọc thủ công, không có.
5. 7 file `Translation Data` — grep `most hated|deposed lord|reasons of his own` → 0.
6. `WebSearch` cụm nguyên văn → chỉ trả về trang wiki, không có nguồn sơ cấp nào chứa câu đó.

Thử thêm `web.archive.org` cho `3do.com/products/pc/mm8/story/story.htm` (@`20010405231846`) → tải 151.276 byte nhưng **0 hit** `archibald|deposed|most hated` (nghi là trang lỗi/khác nội dung, chưa xác minh); `mm7/characters/characters.htm` → **2.456 byte = trang wrapper rỗng** (đúng như ghi chú access về timestamp).

⚠️ **Khuyến nghị:** coi câu này là **UNVERIFIED, nghi bịa hoặc diễn giải lại**, cho tới khi có ai fetch được nó từ nguồn sơ cấp. **Không đưa vào thân bài.**

---

## PRIORITY 2 — Heroes I và Heroes II

### 2.1 Heroes I — Archibald **KHÔNG** xuất hiện (claim phủ định, đã săn chủ động)

Ba đường xác minh độc lập:

1. Fandom `Morglin Ironfist` (văn wiki): về bốn lãnh chúa HoMM1 — "Lord Ironfist is the leader of the Knight faction in *Heroes I* […] However, **like his three counterparts, he does not appear as a hero during the game at any point, and makes no playable appearance in the series.**" → ngay cả **người cha** cũng không phải hero chơi được. Bốn lãnh chúa HoMM1 = **Lord Ironfist, Queen Lamanda, Lord Slayer, Lord Alamar** (thelazy `Succession Wars`, mục *First War of Enrothian Succession*).
2. Fandom `Archibald Ironfist` (văn wiki): Archibald sinh **sau** HoMM1 — "born […] **sometime after the *Strategic Quest*** (*Heroes I*), between the years of 1127 and 1129 AS".
3. thelazy `Succession Wars`: "**25 years later**, after Morglin Ironfist's death, there was doubt about which of his two sons […] would inherit the throne."

→ **Archibald không phải một trong bốn lãnh chúa chơi được của Heroes I, và không xuất hiện trong Heroes I dưới bất kỳ dạng nào.**

**Phát hiện phụ đáng chú ý:** trang `Morglin Ironfist` trên Fandom đang có tag `{{rename|Jerico Ironfist}}` với lý do: *"It is referred to in the game as 'Jerico'."* Và mục Trivia: "**Lord Ironfist's name being Morglin is not given anywhere in any of the games, and is only implied in the *Heroes I* manual.**" → tên cha của Archibald trong **game** là **Jerico Ironfist**; "Morglin" chỉ có ở manual. Aliases: `Lord Ironfist`, `Old King Ironfist`, `Jerico Ironfist`.

### 2.2 Heroes II — cấu trúc campaign

`Archibald's campaign` (Fandom, infobox — `date = 1151-1154 AS`), 11 scenario:

`First Blood` → `Barbarian Wars` → `Necromancers` → `Slay the Dwarves` → `Turning Point` → `Rebellion` → `Dragon Master` → `Country Lords` → `The Crown` → `Greater Glory` → `Apocalypse`

- Nhân vật người chơi điều khiển **không phải Archibald** mà là **"The Commander"** (`identity = The Commander`). Archibald là **chủ**, giao việc qua "magical amulet".
- Ở scenario 5 `Turning Point`, người chơi **có thể đổi phe sang Roland** → nhảy sang `Betrayal (Roland)` rồi vào campaign của Roland từ scenario 6 `Defender`.
- Phe Archibald: `Necromancer`, `Barbarian`, `Warlock` + `Krashaw`. Phe Roland: `Noraston` + Knights/Sorceresses/Wizards.
- Tướng của Archibald: **Corlagon**, **Brother Brax** (Fandom). Tướng của Roland: **Lord Haart**, **Lord Halton**.

### 2.3 Heroes II — GAME TEXT (briefing / description / epilogue)

⚠️ Phân biệt: trên Fandom, `{{quote|...}}` = **lời thoại briefing trong game**, `{{text|...}}` = **scenario description trong game**. Văn ngoài template = văn wiki.

**`First Blood` — briefing của Archibald (game text):**

> "Thank you for choosing to serve me. You will find I can be a very generous lord to vassals who remain faithful, which is more than I can say for the cowardly lords who refuse to take the oath from me. **I am King! Not Roland. No one can stand before me and refuse to serve.** Go! I have allocated a sum of gold for the purposes of making an example of the lords closest to my castle. Crush them, and report back to me by means of the magical amulet I have sent you."

**`First Blood` — scenario description (game text):** "King Archibald requires you to defeat the three enemies in this region. They are not allied with one another, so they will spend most of their energy fighting amongst themselves."

**`Apocalypse` (scenario 11, cuối campaign Archibald) — briefing (game text):**

> "Our finest hour is upon us! Roland's forces have retreated to the province around his castle, and Roland, the fool, cowers in his summer palace, awaiting our final strike! You have gathered your forces for this final battle, now go! **Crush the rebellion and bring my brother back in chains!**"

**`Apocalypse` — epilogue (game text, Archibald nói với Roland):**

> "Well, Roland, it seems I've won our little contest. But don't worry. Not only have I decided to spare your life, but **I am appointing you monarch of the Western Tower. You will be the ruler of a mighty empire, one who's every crack and crevice you will know... in ten minutes.** Perhaps I will come and visit your splendid court, when you are not entertaining important rats and spiders. (laughs, trailing away)"

**`Final Justice` (scenario 10, cuối campaign Roland) — briefing của Roland (game text):**

> "At last, the war draws to an end. **My brother refuses to surrender in the face of your army, and instead sends his undead armies to continue their war against his own people.** I must redirect the forces you so cleverly led to victory against general Corlagon to the defense of the people. I have decided to put Lord Haart in charge of the defense and you in charge of the attack against my brother's weakened armies. […] Let us bring this civil war to an end!"

**`Final Justice` — epilogue: bản án hóa đá (GAME TEXT, mốc quan trọng nhất của Heroes II):**

> "**Brother Archibald, for your crimes against the kingdom and myself, I give you a mercy you surely would not have shown me: I sentence you to be turned to stone and locked in the west tower until future generations should take pity upon you and restore you to life. If they ever do. In any case, you may rest assured you will never lay eyes upon the crown again.**"

→ Xác nhận **hóa đá là bản án của Roland**, có ràng buộc "until future generations […] restore you to life" — chính điều kiện này được MM6 dùng để giải thoát hắn.

**Ai hóa đá hắn:** Entry 1 của Diaries (T2) nói rõ "**made an insensate stone statue by his pet wizard, Tanir**" → thợ thi hành là **Tanir**, court wizard của Roland. Khớp với thelazy `Archibald` và Fandom.

### 2.4 Kết cục canon Heroes II — **Roland thắng**

- Văn wiki Fandom `Archibald's campaign`: "The two campaigns contradict each other, and **Roland's campaign is the canonically true one.**" — **không dẫn nguồn**.
- **Nhưng có chống lưng T1 thật**, xem §1.4: bio Alamar ("**barely able to escape Enroth following Archibald's defeat**") và bio Gem ("**Shortly after Roland had secured the throne of Enroth**"). Cả hai là string table trích từ game HoMM3.
- **Thêm T1\* từ HoMM3 SoD** — prologue `Clearing the Border` (lời Gem trong video mở màn campaign, thelazy trang `Clearing the Border`):

> "It is hard to believe **a year has passed since Archibald and his Necromancer allies were defeated, ending the Succession Wars**. In that time I have been living a nightmare, for I see the ghosts of the fallen all throughout Enroth. I hope my former teacher, Amanda, is right. I hope moving to a new land, to Antagarich, will still the ghosts of the war."

→ **Ba nguồn game text độc lập** (2× HoMM3 `HeroBios.txt` T1 + 1× SoD prologue T1*) chốt canon: Archibald thua. Câu văn wiki không cần thiết nữa.

### 2.5 Quan hệ gia đình

| Quan hệ | Người | Nguồn |
|---|---|---|
| Cha | **Morglin / Jerico Ironfist**, protagonist HoMM1, chết già **1151** | Fandom `Morglin Ironfist`, thelazy `Succession Wars` |
| Mẹ | không tên (`Morglin Ironfist's wife`) | Fandom infobox — **không nguồn** |
| Anh/em trai | **Roland Ironfist** | Diaries Entry 1 (T2): "my hated brother, Roland Ironfist" |
| Em dâu | **Catherine** (Catherine Gryphonheart / Catherine Ironfist), **vợ Roland**, **con gái Nicolas Gryphonheart** | Diaries Entry 1 + 37 (T2): "his loathsome queen Catherine"; "the lich-king, Nicolas Gryphonheart […] Catherine's father" |
| Cháu trai | **Nicolai** (Nicolai Ironfist) | Diaries Entry 1 (T2): "Their brat, Nicolai, sits on the throne" |
| Họ xa | **Ragnar Ironfist** (em họ của Morglin) | Fandom `Morglin Ironfist` infobox — **không nguồn** |

⚠️ **Chưa xác định được ai là anh, ai là em** giữa Roland và Archibald. Không nguồn nào tôi đọc nói rõ thứ tự sinh. Diaries chỉ dùng "brother". Fandom nói "one of two sons" / "the not-so-good son". Nếu bài Codex cần, phải để **UNVERIFIED**.

### 2.6 Được giải thoát khi nào

Diaries Entry 1 (T2), **11 June 1165**: "the ten years I have been my brother's coat rack" + "**If it wasn't for those fool 'adventurers' I'd still be there now.**"

→ Được giải thoát **trước hoặc ngay quanh 11/06/1165**, sau khoảng **10 năm** hóa đá, **do một nhóm "adventurers"** — tức party MM6 (xem §3.1). Lưu ý: "ten years" là **con số Archibald tự nói**, không phải mốc chính xác; nếu Succession Wars kết thúc 1154 thì 1154 + 10 = 1164, lệch 1 năm so với 1165.

---

## PRIORITY 3 — Might & Magic VI và VII

### 3.1 MM6 — có xuất hiện, vai trò: **tượng đá + người trao spell**

Chỉ có **văn wiki**, không fetch được game text MM6:

- thelazy `Archibald` (văn wiki): "this transformation was **deliberately made reversible**, and during the Kreegan invasion, **adventurers freed him so that they could ask him to give them a powerful spell needed to destroy a Kreegan Hive**. After his liberation, Archibald moved to Antagarich where he joined the Necromancers of Deyja to help Finneas Vilmar's plot."
- Fandom (văn wiki), chi tiết hơn: Archibald ăn cắp **memory crystals** của **Melian**, Guardian của Enroth ở **Freehaven**; party MM6 phục hồi module cho Melian, Melian **ra lệnh** cho họ giải thoát Archibald để lấy spell **`Ritual of the Void`** diệt **The Hive**; party thuyết phục **Nicolai Ironfist** thả hắn; Archibald teleport đi.
- Fandom `Gameplay` (văn wiki): "For the majority of *Might and Magic VI*, Archibald is a **non-interactive stone statue seen in the Library of Castle Ironfist**. However, he is revived during the quest to **Free Archibald** […] Once the player has retrieved the **Third Eye** and entered the Library, Archibald will return to life and provide the party with the **Ritual of the Void scroll** before disappearing."
- Fandom trích **lời trong game MM6** — câu Archibald đang nói dở lúc bị hóa đá: *"Now wait just a minute Tanir, and I'll make it worth your while to let me…"* — Fandom ghi "as revealed in *Might and Magic VI*". **Chưa verify từ file game.**
- Fandom trích lời Archibald sau khi The Hive bị diệt, xem qua crystal ball ở dinh Nimbus: *"Yes, thank you heroes. Thank you for saving my kingdom for me."* **Chưa verify từ file game.**

→ Khớp với Diaries Entry 1 ở hai điểm độc lập: (a) "those fool adventurers", (b) hắn trú tại "the remote estate of my colleague […] Nimbus".

### 3.2 MM7 — vai trò lớn

Văn wiki + bảng quest (Fandom `Path of Darkness`):

- **Path of Darkness (Dark Path)**: "After choosing **Devon Sleen** over **Brandis Fairweather** to replace **Judge Grey**, the party become close allies to the Necromancers of **Deyja** and permanently hostile to the Wizards of **Bracada**. **You are thereafter invited to The Pit by Archibald Ironfist** and tasked with escaping the **Breeding Zone** before becoming fully initiated."
  → ⚠️ **Sửa giả thuyết trong brief:** Archibald **không phải "một trong hai người trao quest Path of Darkness"**. Hai người được chọn giữa là **Sleen** (dark) và **Fairweather** (light); Archibald là người **mời party vào The Pit** *sau khi* đã chọn Sleen. Trang `Enter the Pit` **không tồn tại** trên Fandom (`missingtitle`); quest tương ứng trong bảng là `Navigate the Breeding Zone` (The Pit, 50.000 XP, thưởng **Dark magic**, loại **Main**).
- Vị trí: "situated in the **throne room of Castle Gloaming** for the majority of the game, but relocates to **Clanker's Laboratory** after the quest to **Lower the Shields in Clanker's Lab**."
- **Grandmaster trainer of Dark Magic** (Fandom, mục Gameplay + infobox `occupation`).
- Questgiver cho `Complete the Breeding Zone`; trao **Blaster** cho party khi vào **Land of the Giants** trong quest `Kill Xenofex for Resurrectra` / `Kill Xenofex for Kastore`.
- Quan hệ với **Kastore**: Fandom — tàu `The Lincoln` mắc cạn ở **shoals** phía tây **Spaward** (AvLee); Archibald cho **Lieutenant Piridak** đi điều tra; bốn người Terran được đưa về (**Kastore**, **Maximus**, **Dark Shade**, **Tolberti**) và Archibald **chọn họ làm advisor**. Sau đó Kastore đảo chính.
- Cứu Roland: thelazy `Land of the Giants` (văn wiki) — "**Colony Zod** […] Roland was held captive and tormented here during the events of MM7. **Destroyed by the lords of Harmondale with help from Archibald.**" Fandom thêm: Archibald hộ tống Roland bị thương về **Steadwick**, rồi bị **đưa ra xét xử** trước Catherine và Roland; Catherine muốn xử tử, **Roland xin tha**; Archibald bị **lưu đày vĩnh viễn trên đảo Clanker's Lab**.
- Fandom trích lời chia tay (văn wiki, **chưa verify từ file game**): Roland — *"The score is even now, brother. Farewell."*; Archibald — *"Yes... farewell."*

### 3.3 ⭐ `fulton-names-2023` và các nguồn Lead Designer khác — **T4**

**`Gregory Fulton/On Names in Heroes of Might and Magic III`** (98.499 byte, FETCHED, đọc kỹ):

- **KHÔNG có entry nào cho `Archibald`, `Ironfist`, `Roland`, hay `Catherine`** với nghĩa nguồn gốc tên. `grep -inE "archibald|ironfist|roland|catherine|gryphonheart|deyja"` → chỉ 6 dòng, không dòng nào là entry đặt tên cho họ.
- Chữ "ironfist" duy nhất xuất hiện là **thành ngữ**, không phải tên: dòng 103/673 — "Lord Straker (knight); tough, **ironfist in velvet glove**, in your face to right a wrong."
- **T4 EXPLICIT, giá trị cho `catherine-ironfist`:** dòng 46 — "**Winston Boragus, Gavin Magnus, Finneas Vilmar, Eldrich Parson, Tralossk, Faruk Welnin, Queen Catherine, and Morgan Kendal were not named by me.**"
- **T4** cho `deyja` (đã có trong `deyja-dossier`, ghi lại để đối chiếu): dòng 517–518 — "**Deyja** is derived from **Old Norse meaning 'to die'**. Deyja a barren wasteland, and home of the undead. Deyja is the 'to die' nation, the nation of death."
- **T4** dòng 415: "The initial idea to follow Queen Catherine to Erathia was **Paul's** idea. My contribution was her arriving and seeing her father's kingdom in ruin, and questing to restore it."

→ Với **Archibald**: kết quả **ÂM**, nhưng là "không tìm thấy" **đã săn chủ động trên toàn bộ 98KB**. Hợp lý: essay này về tên do Fulton đặt cho **HoMM3**, còn Archibald là tên có từ HoMM2 (trước thời Fulton).

#### 3.3b 🔴 **PHÁT HIỆN T4 QUAN TRỌNG NHẤT** — Fanstratics Newsletter 5 (Greg Fulton, Lead Designer HoMM3)

URL: `https://heroes.thelazy.net/index.php?title=Greg_Fulton/Fanstratics_Newsletters/5&action=raw` (18.463 byte, FETCHED)

Câu hỏi 24 hỏi thẳng về `Seeds of Discontent` (campaign bí mật của RoE) và về câu "seed of discontent" trong Diaries Entry 143. Người hỏi **suy đoán rằng phiến quân thất bại**. Fulton trả lời (nguyên văn):

> "The purpose of the Seeds of Discontent campaign, aside from being the 'secret' campaign, was to showcase the 'upgrade a town' victory condition. **There was no planned 'official' story conclusion for the campaign.**
>
> So, like many lore threads, we laid down enough story to satisfy the design requirements, then left the various elements to be possibly picked up by someone else at a later time. **This occurred when the MM7 team decided to give Archibald an undefined 'behind the scenes' role in the Seeds of Discontent. So, yes, Archibald did play a role in the Contested Lands becoming independent.**
>
> In my opinion, as to the conclusion of the Seeds of Discontent, upon making Welnin the Capital in the campaign, **the Contested Lands became their own kingdom. Despite the rebels declaring independence, this does not mean Erathia and AvLee acknowledged this reality. It is one thing to declare independence. It is another to remain independent.** As for Faruk Welnin and Ryland, their fates were left unresolved […]"

**Vì sao đây là vàng:**
1. Nó **giải nghĩa** dòng cuối Diaries Entry 143 ("Perhaps my seed of discontent will root in those fertile 'disputed lands?'") — Lead Designer xác nhận đó **không phải** lời khoe suông: Archibald **thực sự** có vai trò trong việc Contested Lands giành độc lập.
2. Nó cho biết **quy trình sáng tác**: vai trò của Archibald do **team MM7 gán vào sau**, "undefined 'behind the scenes'", chứ không có trong thiết kế RoE gốc. Đây là loại metadata canon mà `CANON-POLICY` cần.
3. Nó **phản bác suy đoán của fan** (rằng phiến quân thất bại).
4. Fulton phân biệt rõ đâu là **fact** ("yes, Archibald did play a role") và đâu là **ý kiến cá nhân** ("In my opinion, as to the conclusion…"). Khi gán nhãn phải giữ đúng ranh giới này: câu về Archibald là **T4 EXPLICIT**, câu về Contested Lands thành vương quốc riêng là **T4 nhưng là opinion → INFERENCE**.

#### 3.3c Fanstratics Newsletter 4 + Letter about the Forge's cancellation + Tavern Interview — **T4**

**NL4** (16.301 byte) dòng 64, và **`Gregory Fulton/Tavern of Might and Magic Interview`** (35.730 byte) dòng 110 — **cùng một đoạn**, Fulton kể story của bản AB gốc có Forge:

> "Following M&M7, **Archibald's former 'Advisors'** restored production to an ancient wonder called the '**Heavenly Forge**'. Using the Heavenly Forge, these Advisors could fashion any manner of artifact or technology. Creating a futuristic city (Forge) and an army composed of cybernetically enhanced creatures armed with high tech weaponry, the Advisors set out to conquer the world. Ground zero was Erathia."

**`Gregory Fulton/Letter about the Forge's cancellation`** (7.601 byte) dòng 30:

> "Armageddon's Blade followed a story line set up in the upcoming Might and Magic 7. In the M&M7 story, **Archibald's necromantic Advisors build a machine capable of creating high weaponry.** In the Armageddon's Blade campaign, these Advisors build Forge towns and set out to destroy Erathia. […] In the end, Catherine finds Armageddon's Blade and destroys all remnants of the Forge towns, **concluding the Might and Magic 7 story line**."

**Tavern Interview** dòng 319–321 (**NL6** dòng 102 cùng câu hỏi):

> **XEL:** "Was there any ideas on the future of Deyja and Archibald's advisors (who became its new rulers in MM7) in the light of Forge's cancellation?"
> **GF:** "**Paul Rattner may have had some ideas pertaining to the subject, but we never discussed any such subject.**"

**Tavern Interview** dòng 325–327 — về động cơ của các advisor: "**Simple lust for power and domination**, but I am sure there were plenty of rationalizations."

**Tavern Interview** dòng 78–84 (**NL3** dòng 112, cùng câu hỏi) — **T4 về một mâu thuẫn canon liên quan trực tiếp tới dòng dõi Ironfist:**

> **XEL:** truyện ngắn tiền phát hành HoMM3 viết "like the Ironfists of Enroth, the Gryphonhearts have been the ruling family since before the Silence." Nhưng manual HoMM1 nói Lord Ironfist **đến Enroth từ một thế giới khác**; HoMM2 diễn ra 25 năm sau HoMM1, Roland và Archibald là con Lord Ironfist. "That makes Ironfists ruling from around **1126 A.S.**" Retcon hay lỗi?
> **GF:** "**To me, this looks like a simple mistake.**"

→ Lead Designer **thừa nhận đây là lỗi**, không phải retcon. Lưu ý: con số **1126 AS** là **phép tính của người hỏi (XEL)**, **KHÔNG** phải Fulton phát biểu. Đừng gán 1126 cho Fulton.

**Tavern Interview** dòng 102: "Lore work for HoMM4, and **the idea for 'the Reckoning', did not begin until long after I had left NWC**." → nếu bài Codex muốn nói gì về số phận Archibald sau Reckoning, đây là cảnh báo: Reckoning không thuộc thiết kế thời Fulton.

### 3.4 Kiểm disambiguation — **CÓ Archibald thứ hai** (BH-2)

`allpages&apprefix=Archibald` trên **thelazy**: chỉ **2** trang — `Archibald` (nội dung) và `Archibald Ironfist` (`#REDIRECT [[Archibald]]`, 23 byte).

Trên **Fandom**, trang `Archibald` là **disambiguation** (`{{disambig}}`), nguyên văn:

```
{{disambig}}
* [[Archibald Ironfist]], the evil brother of [[Roland Ironfist|Roland]] that appears in
  ''Heroes II'', ''Might and Magic VI'', and ''Might and Magic VII''.
* [[Archibald Dawnsglow]], the expert [[Light Magic (MM8)|light magic]] trainer in
  ''Might and Magic VIII''.
```

→ ⚠️ **`Archibald Dawnsglow`** — nhân vật MM8 khác hoàn toàn, **expert Light Magic trainer**. Đối xứng thú vị (và có thể là cố ý của NWC): Ironfist là **Grandmaster Dark Magic** trainer ở MM7, Dawnsglow là **expert Light Magic** trainer ở MM8.

→ **Mọi claim dạng "Archibald chỉ có một" hoặc "Archibald không xuất hiện ở game MM RPG nào khác" đều SAI.** Đúng như tiền lệ `Sandro (Xeen)`.

`Archibald (H2)` cũng tồn tại nhưng chỉ là `#REDIRECT [[Archibald Ironfist]]` — không phải entity thứ ba. Search Fandom `Archibald` (25 kết quả) không lộ Archibald nào khác.

---

## PRIORITY 4 — gameplay và phân loại

### 4.1 Heroes II — hero **campaign-exclusive**, class **Warlock**

Fandom `Archibald Ironfist` mục Gameplay (văn wiki, mô tả dữ liệu map):

> "Archibald makes appearances as a hero in **two scenarios** in *Heroes of Might and Magic II*: he is the **main playable hero (red player) in `Apocalypse`**, the final map of his campaign, and is the **main enemy hero (red player) in `Final Justice`**, the last map in Roland's campaign. In both scenarios, Archibald belongs to the **Warlock** hero class."

| | `Apocalypse` (H2, campaign Archibald) | `Final Justice` (H2, campaign Roland) |
|---|---|---|
| Vai | hero chơi được (đỏ) | hero địch chính (đỏ) |
| Level / XP | **6** / **6.000** | **20** / **90.000** |
| Quân khởi đầu | 1× **Green Dragon** | 5× **Black Dragon** |
| Artifact | **Ultimate Crown** *hoặc* quân của **Corlagon** (tùy người chơi đã chơi `The Crown` hay `Greater Glory`) | **Ultimate Shield**, **Arcane Necklace of Magic**, **Foremost Scroll of Knowledge** |
| Secondary skills | Expert Scouting, Expert Leadership, Advanced Wisdom | Expert Wisdom, Expert Luck, Expert Archery, Expert Leadership, Expert Estates |
| Điều kiện | mất Archibald = **thua** | Archibald **không rời được vùng khởi đầu**; phải đánh vào **Warlock castle** của hắn để thắng |

⚠️ **Phạm vi phiên bản:** *Heroes of Might and Magic II: The Succession Wars* (bản gốc). **Chưa kiểm** bản `The Price of Loyalty` hay các port có đổi số hay không. Chưa fetch được số **primary skills** (Attack/Defense/Power/Knowledge) — xem `GAPS`.

### 4.2 Heroes III — **không phải hero**, nhưng **có được nhắc trong game text**

- **Không phải hero HoMM3**: 0 hit trên `HeroBios.txt` và `HeroSpec.txt` (§1.4).
- thelazy `Pumpkin Patch/Archibald` (văn wiki) nói thẳng: "**Archibald does not appear in any of the Heroes III scenarios.**"
- ⚠️ **NHƯNG hắn ĐƯỢC NHẮC trong game text HoMM3 ít nhất 3 lần** — nếu bài Codex viết "không xuất hiện trong HoMM3" mà không phân biệt *appear* vs *mentioned* thì đó là **claim phủ định sai**:
  1. **SoD** `Clearing the Border`, prologue video (lời Gem) — xem §2.4.
  2. **AB** `Return of the King`, timed event **day 33** "Roland's Nightmare" (POV Roland, T1*):
     > "…you peer through eyes swollen shut from fists and see the spectral face of your twisted brother laughing at you. **Archibald's dreamghost points at you and laughs a chilling laugh**, one that angers you beyond your knowing. You have never been so helpless as then. **Not since your banishment during the Succession Wars have you felt so alone.**"
     (cùng event: "**You had been held captive for nearly seven years** and the torture inflicted upon you was unimaginable.")
  3. **AB** `Oblivion's Edge`, timed event **day 33** "Ghosts of Conscience" (T1*) — hồn Khazandar cảnh báo Roland:
     > "I stand before you now, Roland Ironfist, to make you see that you are treading down the dark path, a path that will lead you away from your loving wife and son. Turn back now and all shall be forgiven. **Ignore my warnings and forever shall you be like your brother, Archibald.** Your innocence may be lost, but do not allow your good humor and noble heart go with it."

  → Cả hai event AB đều dùng Archibald làm **cực đạo đức đối lập** của Roland. Đây là chất liệu tốt nhất tìm được cho phần "di sản" của entity.

  ⚠️ **Lưu ý phương pháp — đúng BH-1:** cả hai đoạn này nằm trong `=== Timed events ===`, **KHÔNG** ở prologue/epilogue. Nếu chỉ đọc prologue thì sẽ kết luận sai rằng "AB không nhắc Archibald".

  ⚠️ **Lưu ý phân biệt:** text scenario HoMM3 nằm trong file `.h3m`, **không** nằm trong các `Translation Data/*.txt` mà tôi grep. Nên "0 hit trong string table" và "được nhắc trong scenario" **không mâu thuẫn**.

### 4.3 HotA — changelog **âm**, nhưng **content dương**

`Horn_of_the_Abyss_(Changelog)` (201.529 byte, FETCHED). `grep -inE "archibald|ironfist|roland"` → **0 hit cho Archibald**. Chỉ có:

- dòng 1010: "A bug has been fixed where **Roland's** specialty would affect Crusaders but not Swordsmen" (Roland là hero Knight của HoMM3, **không phải** Archibald).
- dòng 1714 / 1655 / 1661 / 1665: artifact set mới **`Ironfist of the Ogre`** — ghép từ Ogre's Club of Havoc + Targ of the Rampaging Ogre + Crown of the Supreme Magi + Tunic of the Cyclops King; đầu combat cast Bloodlust, Fire Shield, Counterstrike (all Expert) 50 turn cho toàn quân đồng minh. **Introduced HotA v1.3.0**; mặc định **tắt** trên mọi map RoE/AB/SoD và map tạo bằng Editor v1.3.4.

🔴 **NHƯNG — không được dừng ở changelog.** Content HotA **có** Archibald, dưới dạng **rumor game text**:

thelazy `Beyond the Horizon` (map HotA), mục `=== Rumors ===`, trong template `{{Rrow|...}}` = **game text**:

> "**Zog named his powerful artifact in memory of Archibald. The usurper king and the Jackal were allies during the Succession Wars.**"

thelazy `Zog` (văn wiki, mục HotA): "**Ally of Archibald during the Succession Wars.** High Chieftain of the ogres harassing Burton. Owner of the Ironfist of the Ogre." (Zog = **The Jackal**, thủ lĩnh ogre ở Barbarian Fortress, region `Ravage Roaming`, xuất hiện trong MM8.)

→ **HotA bổ sung canon cho Archibald:** (a) artifact `Ironfist of the Ogre` được **đặt tên tưởng nhớ Archibald**; (b) **Zog / The Jackal là đồng minh của Archibald trong Succession Wars**. Cái (b) khớp với việc campaign Archibald có phe **Barbarian** và vùng **Krashaw**.

⭐ **Bài học phương pháp:** quy tắc "dùng changelog cho HotA" là đúng cho **con số gameplay**, nhưng **không đủ** cho **lore**. Ở đây changelog 0 hit mà content 2 hit. Suýt thành claim phủ định sai.

thelazy `Frozen Highlands` (1.599 byte, văn wiki tóm tắt region): "**Krashaw**: A region of frozen wastes, home to the disparate barbarian tribes of northern Enroth. The Krashaw barbarians have remained de-facto independent since the **First War of Enrothian Succession**, with Lord Ironfist neglecting to conquer them, but were **united and brought under Archibald's banner during his war against Roland**." — **văn wiki, không dẫn nguồn**; chưa xác định lấy từ map HotA nào hay từ MM8.

### 4.4 Mod `Pumpkin Patch` — **KHÔNG CANON**, cạm bẫy nhãn

thelazy `Pumpkin Patch/Archibald` (1.830 byte). ⚠️ **Đây là hero của MOD `Pumpkin Patch` cho HoMM3**, không phải nội dung game gốc. Trang ghi rõ: "*Only available with the `Pumpkin Patch` installed.*"

🔴 **Cạm bẫy:** `| biography =` là **tham số template** — theo quy tắc dự án, tham số template thường là game text. **Ở đây KHÔNG**. Đây là text do **modder** viết. **Tuyệt đối không gán `T1*`.** Đề xuất `T6` hoặc tier riêng cho fan content.

Nội dung `| biography =` (mod text):

> "As a result of a series of suspicious deaths among the royal seers, Archibald Ironfist reclaimed the throne of Enroth from his brother, Roland. However, his rule was short-lived; Roland usurped the throne and **encased Archibald in marble**. With the aid of a group of brave adventurers, Archibald was freed and later assumed the throne of Deyja, following the (second) death of Nicolas Gryphonheart."

⚠️ Mod text nói **"marble"** (đá hoa cương) và nói **Roland usurped the throne** — cả hai **lệch với game text gốc**: `Final Justice` nói "turned to stone", và canon là Archibald mới là kẻ tiếm ngôi. Mod cố tình viết từ **góc nhìn thiên vị Archibald**. Không dùng làm nguồn.

Thông số mod (phạm vi: **mod `Pumpkin Patch`, HoMM3**): town **Dungeon**, class **Warlock**, specialty **Tactics** ("Increases the range of the Tactics skill by 2 rows for every level of Tactics after the Basic level"), skills **Basic Wisdom + Basic Tactics**, quân Troglodyte 20–30 / Harpy / Beholder, spell **Curse**, `s_mp = 1560`.

→ Có tuỳ chọn HexSwapper "**Archibald replaces Jeddite**" — liên quan tới entity `jeddite` đã có trong repo.

### 4.5 Bảng phân loại theo game

| Game | Xuất hiện? | Dạng | Class / vai |
|---|---|---|---|
| **Heroes I** (1995) | **KHÔNG** | — | sinh sau sự kiện HoMM1 |
| **Heroes II: The Succession Wars** | **CÓ** | hero **campaign-exclusive**, 2 scenario | **Warlock**; playable ở `Apocalypse`, địch ở `Final Justice` |
| **Might & Magic VI** | **CÓ** | NPC (tượng đá phần lớn game) | questgiver `Free Archibald`, trao `Ritual of the Void` |
| **Might & Magic VII** | **CÓ** | NPC lớn | **Grandmaster trainer of Dark Magic**; Castle Gloaming → Clanker's Lab |
| **Heroes III (RoE/AB/SoD)** | **được NHẮC**, không phải hero | game text scenario | 0 hit trong string table; 3 lần được nhắc trong scenario text |
| **HotA** | **được NHẮC** | rumor game text | artifact `Ironfist of the Ogre` đặt tên tưởng nhớ hắn |
| **MM8** | Fandom ghi "mentioned" | chưa verify | — |
| **Pumpkin Patch (mod)** | có, **không canon** | hero mod | Warlock / Dungeon / Tactics |
| **Heroes VI** | 🔴 xem `GAPS` #7 | ? | Fandom infobox ghi `Reaper (H6)` — **nghi lỗi wiki** |

---

## SOURCE LIST

| # | Source key đề xuất | Tier | Trạng thái | Nội dung một câu |
|---|---|---|---|---|
| 1 | `mm7-manual-diaries-3do` | **T2** | **FETCHED** | Site chính thức 3DO qua Wayback, toàn văn *The Diaries of Archibald* (3 entry) — Archibald tự kể; ngày 1165 / **1167** / **1168**. |
| 2 | `mm7-manual-diaries-thelazy` | **T2\*** | **FETCHED** | thelazy chép lại cùng manual nhưng ngày Entry 37/143 lệch **1 năm** (1166 / 1167) → DISPUTED. |
| 3 | `h3-herobios-alamar` | **T1** | **FETCHED** | `HeroBios.txt` dòng 180: Alamar phục vụ Archibald trong Succession Wars và chạy khỏi Enroth sau khi Archibald thua. |
| 4 | `h3-herobios-gem` | **T1** | **FETCHED** | `HeroBios.txt` dòng 58: Gem phục vụ King Roland Ironfist; Roland "secured the throne of Enroth". |
| 5 | `h3-translation-data-negative` | **T1** | **FETCHED** (âm) | 7 string table HoMM3 (≈630 KB), 0 hit `Archibald` → không phải hero HoMM3. |
| 6 | `sod-clearing-the-border-prologue` | **T1\*** | **FETCHED** | Prologue video SoD, lời Gem: "a year has passed since Archibald and his Necromancer allies were defeated, ending the Succession Wars." |
| 7 | `ab-return-of-the-king-day33` | **T1\*** | **FETCHED** | AB timed event day 33: "Archibald's dreamghost points at you and laughs"; Roland bị giam "nearly seven years". |
| 8 | `ab-oblivions-edge-day33` | **T1\*** | **FETCHED** | AB timed event day 33, hồn Khazandar: "forever shall you be like your brother, Archibald." |
| 9 | `hota-beyond-the-horizon-rumors` | **T1\*** | **FETCHED** | Rumor game text HotA: "Zog named his powerful artifact in memory of Archibald… allies during the Succession Wars." |
| 10 | `hota-changelog` | **T2** | **FETCHED** (âm) | 201 KB, 0 hit Archibald; chỉ có artifact `Ironfist of the Ogre` (HotA v1.3.0). |
| 11 | `h2-first-blood-briefing` | **T1\*** | **FETCHED** (qua Fandom) | Briefing Archibald: "I am King! Not Roland." |
| 12 | `h2-apocalypse-briefing-epilogue` | **T1\*** | **FETCHED** (qua Fandom) | "bring my brother back in chains!" + epilogue "monarch of the Western Tower". |
| 13 | `h2-final-justice-briefing-epilogue` | **T1\*** | **FETCHED** (qua Fandom) | Bản án của Roland: "I sentence you to be turned to stone and locked in the west tower…" |
| 14 | `fulton-fanstratics-nl5` | **T4** | **FETCHED** | Lead Designer: "**yes, Archibald did play a role in the Contested Lands becoming independent**"; vai trò do team MM7 gán vào sau. |
| 15 | `fulton-fanstratics-nl4` | **T4** | **FETCHED** | Story AB gốc: "Archibald's **former** 'Advisors' restored production to… the 'Heavenly Forge'." |
| 16 | `fulton-forge-cancellation-letter` | **T4** | **FETCHED** | "Archibald's necromantic Advisors build a machine capable of creating high weaponry." |
| 17 | `fulton-tavern-interview` | **T4** | **FETCHED** | Mâu thuẫn Ironfist/Gryphonheart "**looks like a simple mistake**"; động cơ advisor = "simple lust for power"; Reckoning có sau thời Fulton. |
| 18 | `fulton-fanstratics-nl3` | **T4** | **FETCHED** | Bản newsletter của cùng câu hỏi Ironfist/Gryphonheart (trùng #17). |
| 19 | `fulton-fanstratics-nl6` | **T4** | **FETCHED** | Bản newsletter của câu hỏi về tương lai Deyja/advisor (trùng #17). |
| 20 | `fulton-names-2023` | **T4** | **FETCHED** (âm cho Archibald) | 98 KB, **không** có entry `Archibald`/`Ironfist`/`Roland`; **có** T4: Catherine "not named by me"; Deyja = Old Norse "to die". |
| 21 | `thelazy-archibald` | **T6** | **FETCHED** | Văn wiki tổng hợp; **gộp sai** Challenge of Dominance với việc lên ngôi Deyja. |
| 22 | `thelazy-nimbus` | **T6** | **FETCHED** | Văn wiki; tách đúng hai sự kiện → **tự mâu thuẫn với `thelazy-archibald`**. |
| 23 | `thelazy-succession-wars` | **T6** | **FETCHED** | Hai cuộc chiến kế vị; Succession Wars "around the 1110s to **1154** AS"; bốn lãnh chúa HoMM1. |
| 24 | `thelazy-tularea` | **T6** | **FETCHED** | Clanker's Lab là nơi Archibald về sau khi bị Kastore phế. |
| 25 | `thelazy-land-of-the-giants` | **T6** | **FETCHED** | Colony Zod bị lords of Harmondale phá "with help from Archibald". |
| 26 | `thelazy-frozen-highlands` | **T6** | **FETCHED** | Krashaw barbarians "united and brought under Archibald's banner" — không dẫn nguồn. |
| 27 | `thelazy-zog` | **T6** | **FETCHED** | Zog = The Jackal, đồng minh Archibald, chủ `Ironfist of the Ogre`. |
| 28 | `thelazy-lost-lore` | **T6** | **FETCHED** | Danh mục lore; xếp *The Diaries of Archibald* là văn bản MM7 do Archibald viết. |
| 29 | `pumpkin-patch-archibald` | **T6** (fan mod) | **FETCHED** | Hero mod HoMM3; ⚠️ `| biography =` là text **modder**, KHÔNG phải game text. |
| 30 | `fandom-archibald-ironfist` | **T6** | **FETCHED** | Bài dài nhất; nhiều số liệu gameplay H2 + trích lời MM6/MM7 chưa verify. |
| 31 | `fandom-archibald-disambig` | **T6** | **FETCHED** | Chứng minh tồn tại **`Archibald Dawnsglow`** (MM8, expert Light Magic trainer). |
| 32 | `fandom-morglin-ironfist` | **T6** | **FETCHED** | Cha; tên in-game là **"Jerico"**, "Morglin" chỉ có ở manual HoMM1; bốn lãnh chúa H1 đều không playable. |
| 33 | `fandom-archibalds-campaign` | **T6** | **FETCHED** | 11 scenario; `date = 1151-1154 AS`; "Roland's campaign is the canonically true one" (không dẫn nguồn). |
| 34 | `fandom-path-of-darkness` | **T6** | **FETCHED** | Bảng quest Dark Path MM7; Archibald **mời** party vào The Pit sau khi chọn Sleen. |
| 35 | `3do-mm8-story-archive` | T2 | **FAILED** | Tải 151 KB nhưng 0 hit `archibald`; nghi trang lỗi/khác nội dung, **chưa xác minh**. |
| 36 | `3do-mm7-characters-archive` | T2 | **FAILED** | 2.456 byte = trang wrapper rỗng (timestamp không khớp snapshot thật). |

**Tổng: 36 source key đề xuất** — trong đó **34 FETCHED** (7 là kết quả âm có giá trị), **2 FAILED**.

---

## GAPS — tìm mà không thấy (kèm nơi đã tìm)

1. **🔴 Câu "deposed lord of Deyja and one of the most hated men in history, offered aid for reasons of his own"** — **KHÔNG XÁC MINH ĐƯỢC**. Đã tìm ở 6 chỗ, chi tiết ở §1.7. **Khuyến nghị coi là nghi bịa; không đưa vào thân bài.**
2. **Ai là anh, ai là em** giữa Roland và Archibald — không nguồn nào nói. Đã đọc: Diaries (cả 3 entry), thelazy `Archibald` / `Succession Wars`, Fandom `Archibald Ironfist` / `Morglin Ironfist`, `HeroBios.txt`. Tất cả chỉ dùng "brother" / "one of two sons".
3. **Primary skills (Attack/Defense/Spell Power/Knowledge) của Archibald ở H2** — Fandom chỉ có level, XP, secondary skills, quân, artifact. Không tìm được bảng primary stat. **Chưa tìm ở:** file `.h2c`/`.h2m` gốc, hay `HEROES2.AGG`.
4. **Text game MM6/MM7 gốc (file game)** — mọi thứ về MM6/MM7 trong dossier này là **văn wiki** hoặc **manual (T2)**. Các câu Fandom trích (*"Now wait just a minute Tanir…"*, *"Thank you for saving my kingdom for me."*, *"The score is even now, brother."*) **chưa verify từ file game**. Liên quan `B-001` trong `BACKLOG.md`. thelazy **không** có `Translation Data` cho MM6/MM7 (chỉ HoMM3 — đã liệt kê đủ 56 file, không file nào là MM6/MM7).
5. **Mốc chính xác Kastore đảo chính** — không có game text, chỉ văn wiki (§1.6). `deyja-dossier` đặt ~1169 dựa trên Fandom.
6. **Manual MM7 bản in giấy** — cần để chốt mâu thuẫn ngày 1167/1168 vs 1166/1167 (§1.5). Chưa tìm scan.
7. **🔴 `Reaper (H6)` trong infobox Fandom** — infobox `Archibald Ironfist` ghi `class = … [[Reaper (H6)|Reaper]] {{Icon-H6}}`, `image = Archibald H6.png`, `status = Unknown (as of the [[Reckoning]])`, **nhưng** `appearances` **không** có H6, và trang disambiguation **không** liệt kê Archibald nào của H6. **Chưa verify.** Nghi lỗi wiki. (H6 = Ashan / New Universe → ngoài phạm vi dự án, nhưng mâu thuẫn nội bộ này nên ghi lại.)
8. **MM8 "mentioned"** — Fandom xếp Archibald vào `Category:Might and Magic VIII characters` và list "mentioned in MM8". **Chưa fetch** nội dung MM8 nào để xác nhận nhắc ở đâu.
9. **`Legends of Might and Magic`** — Fandom xếp vào `Category:Legends characters`. **Chưa kiểm.**
10. **Script thoại H2** — Fandom Trivia trích chỉ dẫn giọng: *"Evil wizard type. Think of Tim Curry, or John Hurt in the role. Cultured, faintly British accent."* và ghi nguồn là "*Heroes II*'s dialogue script". Đây có thể là nguồn **T2/T4 rất giá trị** (tài liệu nội bộ nhà phát triển) nhưng **tôi chưa fetch được bản script gốc** — chỉ có Fandom nhắc lại. **Đáng đào tiếp.**
11. **`Challenge of Dominance`** — chưa fetch trang riêng (nếu có) để xem định nghĩa cơ chế. thelazy `Archibald` chỉ link `[[Challenge of Dominance]]`.
12. **Scenario H2 giữa campaign** — chỉ đọc `First Blood`, `Apocalypse`, `Final Justice`. **Chưa đọc:** `Barbarian Wars`, `Necromancers`, `Slay the Dwarves`, `Turning Point`, `Rebellion`, `Dragon Master`, `Country Lords`, `The Crown`, `Greater Glory`, `Betrayal`. Có thể còn briefing/epilogue nhắc Archibald. **Đây là gap lớn nhất còn lại của PRIORITY 2.**

---

## SUSPECTED WIKI-ONLY CLAIMS

Claim chỉ có văn wiki chống lưng, **không có game text**:

1. **"Archibald bị Kastore phế / đảo chính"** — cả `thelazy` (2 trang) và Fandom đều khẳng định, **không dẫn nguồn**. Chống lưng gián tiếp duy nhất: chữ "**former** Advisors" của Fulton (T4) và việc advisor chuyển hướng sang Heavenly Forge.
2. **"Archibald battles Nimbus for the title of King of Deyja"** — 🔴 **TRÁI game text.** Xem §1.2. Cần viết lại hoàn toàn.
3. **"Deathknell" → dịch thành "Finneas Vilmar"** — cả hai wiki tự thay tên **mà không ghi chú** manual dùng tên khác. Sự đồng nhất hai tên là **INFERENCE**, không EXPLICIT.
4. **"Roland's campaign is the canonically true one"** — Fandom, không dẫn nguồn. **Nhưng có thể nâng cấp** nhờ 3 nguồn game text ở §2.4 → không cần dựa vào văn wiki nữa.
5. **Năm sinh Archibald "between 1127 and 1129 AS" / "~1120s AS"** — Fandom, **không ref**. Số 1126 AS trong phỏng vấn Fulton là **phép tính của người phỏng vấn**, không phải nguồn chính thức, và Fulton gọi cả tiền đề là "a simple mistake".
6. **"Morglin died of old age in 1151"** và **"In 1162, Roland departed"** — Fandom, không ref.
7. **Chi tiết MM6 về Melian / memory crystals / Third Eye / thuyết phục Nicolai** — chỉ Fandom, chưa verify game text.
8. **"Archibald stole Melian's memory crystals out of spite"** — Fandom, không ref; động cơ ("out of spite") là **suy diễn của người viết wiki**.
9. **thelazy `Archibald`: "He allied with… Jadame's pirates"** vs Fandom: "**Regna Island/Regnan** Pirates" — 🔴 **hai wiki nói khác nhau về gốc của cướp biển.** Cả hai không dẫn nguồn. (`Return of the King` T1* có nhắc "the dreaded **Regnan** Pirates' treasure troves" nhưng trong ngữ cảnh khác, không liên quan Archibald.)
10. **thelazy `Frozen Highlands`: Krashaw "brought under Archibald's banner"** — không dẫn nguồn; không rõ từ map HotA hay MM8.
11. **`Pumpkin Patch/Archibald` `| biography =`** — trong tham số template nhưng là **text modder**. ⚠️ Đúng loại lỗi "gán T1\* cho văn không phải game text" mà dự án đã bị bắt một lần.
12. **"Brother Brax rallied to his side"** (Fandom) — không ref.
13. **"eventually attempted to redeem himself for his crimes"** (Fandom, câu mở bài) — **đánh giá của người viết wiki**, không phải claim có nguồn.

---

## TIMELINE

**Lịch:** AS = After the Silence. Ngày **tuyệt đối** (có ngày/tháng) chỉ đến từ *The Diaries of Archibald*.

| Mốc | Sự kiện | Loại | Nguồn | Tier |
|---|---|---|---|---|
| ca. late 1000s AS | Morglin/Jerico Ironfist sinh | tương đối | Fandom infobox | T6 **UNVERIFIED** |
| ~1101–1126 AS | **First War of Enrothian Succession** — Morglin vs Lamanda, Slayer, Alamar (**HoMM1**) | tương đối | thelazy `Succession Wars` | T6 |
| ~1126 AS | Morglin thắng, thống nhất Enroth | tương đối | phép tính của XEL trong phỏng vấn Fulton (**không** phải Fulton nói) | T6 **UNVERIFIED** |
| 1127–1129 AS | **Archibald sinh** (sau HoMM1) | tương đối | Fandom | T6 **UNVERIFIED — không ref** |
| **1151** | **Morglin chết**; Archibald giết 4 royal seer, vu cho Roland, tự lên ngôi | tương đối | Fandom; thelazy `Succession Wars` ("25 years later") | T6 |
| **1151–1154** | **The Succession Wars** (**HoMM2**) | tương đối | Fandom `Archibald's campaign` infobox `date` | T6 |
| **~1154** | Archibald **bị bắt và hóa đá** bởi Tanir, giam ở west tower | tương đối | `Final Justice` epilogue (game text) + thelazy `Succession Wars` ("to 1154 AS") | **T1\*** cho sự kiện, T6 cho năm |
| **~1155** | Gem rời Enroth sang Antagarich, "**a year has passed since Archibald… were defeated**" | tương đối | `Clearing the Border` prologue | **T1\*** |
| **1162** | Roland dẫn quân đánh Kreegan, bị bắt | tương đối | Fandom | T6 **không ref** |
| ~1155–1165 | Archibald bị chuyển vào **Library** của Castle Ironfist | tương đối | Fandom | T6 **không ref** |
| **~01/1165** | Catherine rời Enroth sang Erathia dự tang cha ("**five months ago**" tính từ 11/06/1165) | **tuyệt đối (suy ra)** | Diaries Entry 1 | **T2** |
| **≤ 11/06/1165** | **Archibald được "adventurers" (party MM6) giải thoát** sau ~10 năm hóa đá | tuyệt đối (chặn trên) | Diaries Entry 1 | **T2** |
| **11/06/1165** | **Diaries Entry 1.** Archibald trú tại dinh Nimbus; Nicolai trên ngai, Wilbur Humphrey làm Regent | **TUYỆT ĐỐI** | Diaries Entry 1 | **T2** |
| ~1165–1167 | Deathknell (= Finneas Vilmar, INFERENCE) ám sát Gryphonheart, hồi sinh thành lich, **bị chính lich giết** | tương đối | Diaries Entry 37 | **T2** |
| **23/10/1167** ⚠️ | **Diaries Entry 37.** Archibald lên tàu sang Erathia; thắng **Challenge of Dominance** trước Nimbus, giành quyền chỉ huy đoàn Necromancer Enroth | **TUYỆT ĐỐI** | Diaries Entry 37 (**3DO**) | **T2** |
| *(23/10/**1166**)* | 🔴 **cùng entry, thelazy ghi 1166** — DISPUTED | — | thelazy; khớp với thelazy `Nimbus` ("by 1166 AS") | T2\* |
| **05/08/1168** ⚠️ | **Diaries Entry 143.** Catherine đọc victory speech (kết thúc **RoE**); **Archibald "replaced Gryphonheart"** → Guildmaster of Necromancers + vua Deyja; tuyên "seed of discontent… disputed lands" | **TUYỆT ĐỐI** | Diaries Entry 143 (**3DO**) | **T2** |
| *(05/08/**1167**)* | 🔴 **cùng entry, thelazy ghi 1167** — DISPUTED | — | thelazy | T2\* |
| sau 1168 | Archibald **có vai trò "behind the scenes"** trong **Seeds of Discontent**; Contested Lands tuyên độc lập | tương đối | **Fulton NL5** | **T4 EXPLICIT** (kết luận về Contested Lands là **opinion → INFERENCE**) |
| **MM7** | `The Lincoln` mắc cạn tây Spaward; Piridak đưa 4 Terran (Kastore, Maximus, Dark Shade, Tolberti) về; Archibald **chọn họ làm advisor** | tương đối | Fandom | T6 |
| ~1169 | **Kastore đảo chính**; Archibald + tàn dư về **Clanker's Lab** | tương đối | văn wiki (thelazy ×2, Fandom); `deyja-dossier` đặt 1169 | **T6 — không game text** |
| **MM7 (muộn)** | Archibald giúp **lords of Harmondale** phá **Colony Zod**, cứu Roland (bị giam "**nearly seven years**" → 1162+7 ≈ 1169), hộ tống về **Steadwick** | tương đối | thelazy `Land of the Giants` (T6) + `Return of the King` day 33 (**T1\*** cho "seven years") | T6 / **T1\*** |
| **MM7 (cuối)** | Archibald **bị xét xử** trước Catherine và Roland; Roland xin tha; **lưu đày vĩnh viễn** trên đảo Clanker's Lab; từ bỏ ngai Enroth | tương đối | Fandom | **T6 — không game text** |
| **AB** | `Return of the King` day 33 + `Oblivion's Edge` day 33 — Archibald xuất hiện trong **cơn mê của Roland** như cực đối lập đạo đức | tương đối | game text AB | **T1\*** |
| **AB, sau** | Advisor cũ của Archibald khôi phục **Heavenly Forge**, dựng Forge towns; Catherine dùng Armageddon's Blade diệt sạch → "concluding the Might and Magic 7 story line" | tương đối | Fulton letter + NL4 + Tavern Interview | **T4** (story **bị cắt**, không phải canon shipped) |
| **HotA** | Zog / The Jackal đặt tên artifact **`Ironfist of the Ogre`** "in memory of Archibald"; hai người là đồng minh thời Succession Wars | tương đối | `Beyond the Horizon` rumors | **T1\*** |
| **Reckoning** | Số phận Archibald **không rõ** | — | Fandom `status` | T6; Fulton: ý tưởng Reckoning có **sau** khi ông rời NWC (**T4**) |

### Ba chỗ timeline không khít (cần người viết bài xử lý)

1. **"ten years" vs 1154→1165 = 11 năm.** Diaries Entry 1 nói 10 năm hóa đá. Nếu chiến tranh kết thúc 1154 thì ra 1164. Fandom cũng dùng "the ten years that followed". → dùng **"khoảng mười năm"**, đừng chốt năm giải thoát.
2. **Entry 1 (1165) nói Catherine đi dự tang cha 5 tháng trước** → Gryphonheart chết ~cuối 1164. Nhưng Entry 37 (1167 theo 3DO) mới kể chuyện hồi sinh lich. Khoảng trống ~2,5 năm giữa cái chết và việc Archibald biết tin — **hợp lý** nếu dùng ngày 3DO (1167), **chật hơn** nếu dùng ngày thelazy (1166). → **thêm một điểm cộng nhẹ cho ngày 3DO.**
3. **Roland "held captive for nearly seven years"** (AB, T1*) + "In 1162, Roland departed" (Fandom, không ref) → được cứu ~1169. Khớp với mốc Kastore đảo chính ~1169. Nhưng **1162 chưa có nguồn**, nên đây là chuỗi suy luận dựa trên một khâu UNVERIFIED.

---

## Ghi chú cập nhật cho `access notes` của dự án

1. ⚠️ **thelazy `action=raw` CẦN User-Agent.** Không có `-A` thì trả **0 byte im lặng** — dễ bị hiểu sai thành "trang không tồn tại". Lần gọi đầu cho `Archibald` trả rỗng; thêm `-A "Mozilla/5.0 Research"` thì ra 8.937 byte.
2. ✅ **Fandom CÓ CirrusSearch** — `list=search&srsearch=insource:/.../` **chạy được** (khác thelazy). Đây là cách nhanh nhất để phủ định một cụm nguyên văn.
3. ⚠️ **Quy tắc "HotA → dùng changelog" không đủ cho LORE.** Ở entity này changelog 0 hit mà content (rumor game text trong map `Beyond the Horizon`) có 2 hit. Changelog đúng cho **con số gameplay**, không đúng cho **lore**.
4. ⚠️ **`Translation Data/*.txt` trên thelazy CHỈ có HoMM3** (đã liệt kê đủ 56 file). Không có MM6/MM7. Text scenario HoMM3 nằm trong `.h3m`, **không** trong các `.txt` này — nên "0 hit trong string table" **không** đủ để nói "không được nhắc trong HoMM3".
5. ⚠️ **Không có `python3` trong Bash tool** (Git Bash trên Windows, không phải WSL). Giải JSON của Fandom bằng `sed -e 's/\\n/\n/g' -e 's/\\"/"/g'`.
6. ⚠️ **Đường dẫn:** Bash tool dùng `//wsl.localhost/Ubuntu/home/cuongtv/heroes/...`, **không** dùng `/home/cuongtv/heroes`.
