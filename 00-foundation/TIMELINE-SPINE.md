# TIMELINE SPINE

Xương sống thời gian của Old Universe.

---

## 1. Vì sao không dùng năm tuyệt đối làm xương sống

Đây là quyết định thiết kế quan trọng nhất của tài liệu này, nên nói rõ lý do.

Old Universe có **ít nhất ba hệ quy chiếu thời gian không tương thích**:

- Lịch Enroth (dùng trong Heroes I–II và MM6)
- Hệ năm "AS" xuất hiện trong tư liệu Heroes III và MM7–MM8
- Heroes Chronicles gần như **không có mốc năm tuyệt đối nào** cho Tarnum

Nếu dự án đặt mục tiêu "chốt một timeline năm tuyệt đối duy nhất trước khi viết", nó
sẽ không bao giờ ra khỏi Giai đoạn 1. Và tệ hơn: nó sẽ buộc phải **bịa** ra sự chắc
chắn mà tư liệu không có.

Nên:

> **Xương sống là quan hệ tương đối. Năm tuyệt đối là một thuộc tính có nhãn.**

Một sự kiện có thể có `date_certainty: DISPUTED` mà vị trí tương đối của nó vẫn
`EXPLICIT`. Điều này đủ để kể chuyện, và trung thực với tư liệu.

---

## 2. Cấu trúc ba tầng

### Tầng A — Kỷ nguyên (Era)

Đơn vị lớn nhất. Chỉ cần xếp đúng thứ tự, không cần năm.

```
Kỷ Ancients
     ↓
Kỷ Silence
     ↓
Age of Kings (Enroth)
     ↓
Kỷ Antagarich (Heroes III)
     ↓
The Reckoning
     ↓
Kỷ Axeoth (Heroes IV)
```

Đây là tầng ổn định nhất — thứ tự này không có nguồn nào tranh chấp.

### Tầng B — Chuỗi sự kiện (Sequence)

Trong mỗi kỷ nguyên, các sự kiện nối nhau bằng quan hệ `before` / `after` /
`concurrent_with`. **Đây là tầng làm việc chính.**

Ví dụ đã xác lập được từ dữ liệu Sandro:

```
Sandro học dưới Ethric
     ↓ (Sandro chuyển sang necromancy — Ethric nổi giận)
Sandro thu thập artifact qua Gem và Crag Hack
     ↓
Ethric tung tin vị trí Sandro cho kẻ thù
     ↓
Sandro giết Ethric  ·  nhận Vidomina làm học trò
     ↓
Sandro dựng Finneas Vilmar lên ngôi Deyja
     ↓
Bốn anh hùng đánh bại Sandro  ·  Angelic Alliance bị tháo rời
     ↓
Sandro liên minh Kreegan + Nighon
     ↓
Nicolas Gryphonheart bị đầu độc
     ↓
Finneas gài Sandro vào tù
     ↓
Cuộc xâm lược Erathia (Restoration of Erathia bắt đầu)
```

Toàn bộ chuỗi này là `EXPLICIT` về **thứ tự**, dù phần lớn **không có năm**.

### Tầng C — Năm tuyệt đối (Absolute date)

Chỉ gắn khi có nguồn. Mỗi năm mang ba trường:

```yaml
date_absolute: 1164
date_certainty: DISPUTED    # EXPLICIT | INFERENCE | DISPUTED | UNVERIFIED
date_source: h3-manual-timeline
```

**Không được suy ra năm bằng cách cộng trừ** rồi ghi là `EXPLICIT`. Suy ra thì là
`INFERENCE`, và phải ghi rõ suy theo bước nào.

---

## 3. Mốc thời gian tương đối đã xác lập được

Phần này chỉ chứa những gì **đã có nguồn**. Sẽ dày lên khi Codex mở rộng.

### Neo thời gian quan trọng nhất tìm được

Từ dữ liệu Sandro, có một neo dùng được để định vị nhiều thứ khác:

> Sandro thành necromancer **vài thập kỷ** (decades) trước Restoration Wars.

{T1* EXPLICIT: sod-agents-of-vengeance — Ethric nói qua thư gửi Gem: "it had been
decades Sandro was his apprentice"}

Đây là loại neo mà dự án cần nhiều hơn: **khoảng cách tương đối có nguồn**, không phải
năm tuyệt đối.

### Neo dùng để loại trừ

> Sự kiện *Conquest of the Underworld* (Heroes Chronicles) xảy ra **hàng trăm năm**
> trước Restoration Wars.

{T1* INFERENCE: h3wiki-sandro}

Neo này quan trọng vì nó **loại trừ** khả năng Sandro trong Chronicles là cùng một
người — xem `codex/heroes/sandro.md` mục *Điểm tranh chấp*. Timeline không chỉ dùng
để xếp thứ tự, mà còn để phát hiện điều bất khả thi.

### Mốc có năm tuyệt đối

| Sự kiện | Năm | Độ chắc | Nguồn |
|---|---|---|---|
| Ethric bị nhóm nhân vật MM6 giết trên Enroth | ~đầu 1165 AS | `INFERENCE` | `h3wiki-ethric` |
| Nimbus tập hợp tàn dư Necromancer's Guild ở Enroth | ~1166 AS | `INFERENCE` | `h3wiki-nimbus` |

Chỉ hai mốc. Đây là tình trạng thực tế sau đợt research đầu — và chính là lý do
xương sống không thể dựa vào năm.

---

## 4. Quy tắc làm việc

**T1 — Không bịa năm.** Không có nguồn thì để `date_absolute: null`. Một sự kiện
không có năm vẫn định vị được bằng `before` / `after`.

**T2 — Neo tương đối quý hơn năm tuyệt đối.** Một câu như "vài thập kỷ trước
Restoration Wars" có giá trị cấu trúc cao hơn một con năm không nguồn.

**T3 — Timeline dùng để phát hiện điều bất khả thi.** Nếu A được ghi là hệ quả của B
nhưng A lại xảy ra trước B, một trong hai claim sai. Đây là nhiệm vụ Tầng 3 của
`VERIFY-PROTOCOL.md`.

**T4 — Không xếp timeline theo thứ tự campaign.** Campaign là **đơn vị tư liệu**;
sự kiện là **thứ đã xảy ra**. Ví dụ: *Shadow of Death* phát hành **sau**
*Restoration of Erathia* nhưng kể sự kiện **trước** nó. Timeline theo thế giới, không
theo lịch phát hành. Đây là lý do `SCHEMA.md` tách `event` khỏi `campaign`.

**T5 — Mâu thuẫn niên đại là `DISPUTED`, không phải lỗi cần sửa.** Nếu hai nguồn cho
hai năm khác nhau, ghi cả hai.

---

## 5. Bảy Book của Saga xếp trên trục nào

| Book | Nội dung | Neo thời gian |
|---|---|---|
| I | The Ancients | Kỷ Ancients — trước mọi thứ |
| II | Age of Kings | Enroth, Heroes I–II |
| III | Rise of Erathia | Antagarich trước cuộc xâm lược |
| IV | Heroes III | Restoration of Erathia và các expansion |
| V | Heroes Chronicles | **Xuyên nhiều kỷ** — Tarnum sống rất lâu |
| VI | The Reckoning | Kết thúc Enroth |
| VII | Axeoth | Heroes IV |

⚠️ **Book V là vấn đề cấu trúc chưa giải quyết.** Heroes Chronicles không nằm gọn
trong một khoảng thời gian — Tarnum xuất hiện xuyên nhiều kỷ nguyên. Xếp nó thành
Book V (sau Heroes III) là **thứ tự đọc**, không phải thứ tự thời gian.

Cần quyết định sau: kể Chronicles theo thứ tự thời gian (rải vào các Book khác) hay
theo thứ tự đọc (giữ nguyên Book V). Chưa đủ dữ liệu để chốt. Ghi lại để không quên.

Với chuỗi Sandro ở mục 3, phần lớn thuộc **Book IV**, nhưng đoạn đầu (học dưới Ethric,
thời Enroth) thuộc **Book II hoặc III** — chưa định vị được chính xác vì thiếu năm.

---

## 6. Việc cần làm

| Việc | Vì sao |
|---|---|
| Tìm nguồn cho hệ lịch "AS" | Hiện dùng mà chưa biết viết tắt của gì, gốc từ đâu |
| Lập entity `event` cho chuỗi Sandro | Chuỗi ở mục 3 hiện chỉ là văn bản, chưa thành dữ liệu query được |
| Tìm timeline trong manual Heroes III | `h3-manual-timeline` được nhắc nhưng **chưa fetch được** |
| Quyết định cấu trúc Book V | Xem cảnh báo ở mục 5 |
| Xác lập mốc Reckoning | Ranh giới Enroth → Axeoth, hiện chưa có nguồn |

---

## 7. Lịch sử sửa đổi

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 2026-07-31 | Bản đầu | Viết sau khi có dữ liệu Sandro thật, không viết trước — để mốc trong đây là mốc có nguồn, không phải mốc giả định |
