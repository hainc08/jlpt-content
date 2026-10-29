# jlpt-content

Nội dung dùng chung cho các app JLPT của ManabiHub, phục vụ qua GitHub Pages
(Settings → Pages → Deploy from branch `main`, thư mục `/ (root)`).

| Đường dẫn | Dùng cho |
|---|---|
| `exams/n5/` … `exams/n1/` | App **JLPT Thi Thử** — đề thi, cập nhật không cần build lại app |
| `kanji/n5.json`, `kanji/n4.json` … | App **Kanji Flashcard** — bộ chữ Kanji từng cấp |

Địa chỉ: `https://hainc08.github.io/jlpt-content/exams/<level>/index.json`

Hướng dẫn: [exams/HUONG_DAN.md](exams/HUONG_DAN.md) (đề thi), [kanji/HUONG_DAN.md](kanji/HUONG_DAN.md) (Kanji).
Mỗi lần push, workflow **exams-check** kiểm tra đề và dữ liệu Kanji (✅/❌).
