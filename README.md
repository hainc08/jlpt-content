# jlpt-content

Nội dung dùng chung cho các app JLPT của ManabiHub, phục vụ qua GitHub Pages
(Settings → Pages → Deploy from branch `main`, thư mục `/ (root)`).

| Đường dẫn | Dùng cho |
|---|---|
| `exams/n5/` … `exams/n1/` | App **JLPT Thi Thử** — đề thi, cập nhật không cần build lại app |

Địa chỉ: `https://hainc08.github.io/jlpt-content/exams/<level>/index.json`

Hướng dẫn thêm/sửa/xoá đề: [exams/HUONG_DAN.md](exams/HUONG_DAN.md).
Mỗi lần push, workflow **exams-check** kiểm tra đề (✅/❌).
