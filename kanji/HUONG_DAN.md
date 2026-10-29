# Dữ liệu Kanji — cập nhật không cần build lại app

App **Kanji Flashcard** (N5, N4, …) tải `https://hainc08.github.io/jlpt-content/kanji/<app>.json`
(`n5.json`, `n4.json`, …). App kiểm tra khi mở (tối đa 6 giờ/lần) hoặc khi bấm nút ⟳ ở **Cài đặt → Bộ dữ liệu**.

## Sửa / thêm / xoá chữ
Sửa trực tiếp `kanji/n5.json` trên GitHub rồi commit:
```json
{ "char": "毎", "hanViet": "MỖI", "meaning": "mỗi", "on": "マイ", "kun": "" }
```
- Thêm chữ: thêm một dòng như trên vào mảng `"kanji"` (thứ tự trong file = thứ tự trong app).
- Xoá chữ: xoá dòng đó. Sửa: sửa trực tiếp các trường.
- Quy tắc: không trùng chữ, **không trùng nghĩa** (quiz cần 4 đáp án khác nhau), có Hán Việt, nghĩa và ít nhất On hoặc Kun; tối thiểu 20 chữ.
- Workflow **exams-check** kiểm tra mỗi lần push (✅/❌). File sai bị app bỏ qua, người dùng vẫn dùng bộ cũ.

## Khi phát hành bản app mới
Chép nội dung mới vào `lib/data/kanji_<app>.dart` trong repo jlptkanjin5 để bản đóng sẵn trong app cũng mới
(ngược lại, xuất từ .dart sang JSON: `python tools/export_kanji_json.py ../../content/kanji`).
