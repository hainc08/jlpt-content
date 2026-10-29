# Đề thi thử JLPT — cập nhật không cần build lại app

App **JLPT N5 Thi Thử** tự tải đề từ thư mục này (GitHub Pages):
`https://hainc08.github.io/jlpt-content/exams/n5/`

App kiểm tra đề mới mỗi khi mở (tối đa 3 giờ/lần) hoặc khi người dùng kéo xuống ở màn **Chọn đề thi**.
GitHub Pages cần khoảng 1–10 phút sau khi push để cập nhật.

## Thêm đề
1. Tạo file mới trong `exams/n5/`, ví dụ `n5-03.json` (copy một đề có sẵn rồi sửa).
2. Đổi `"id"` (không trùng đề khác, ví dụ `"n5-03"`), `"title"`, `"titleJa"`.
3. Thêm tên file vào `exams/n5/index.json`:
   ```json
   { "schema": 1, "level": "N5", "exams": ["n5-01.json", "n5-02.json", "n5-03.json"] }
   ```
4. Commit. Workflow **exams-check** sẽ kiểm tra; dấu ✅ là đề hợp lệ.

## Sửa đề
Sửa trực tiếp file `n5-xx.json` rồi commit. Giữ nguyên `"id"` để lịch sử thi của người dùng vẫn khớp.

## Xoá / ẩn đề
Bỏ tên file khỏi `index.json` (có thể giữ file lại). Người dùng không thấy đề nữa,
nhưng kết quả đã thi trước đó vẫn xem lại được.

## Thứ tự hiển thị
Đúng theo thứ tự trong `index.json`.

## Cấu trúc một câu hỏi
```json
{
  "id": "moji-1-1",            // không trùng trong cùng đề
  "no": 1,                      // số thứ tự câu trong phần thi
  "prompt": "あの {山} は とても たかいです。",   // {...} = gạch chân, ［1］ = ô trống đoạn văn
  "options": ["そら", "やま", "かわ", "うみ"],
  "answer": 1,                  // vị trí đáp án đúng, đếm từ 0
  "explanation": "山 đọc là やま ..."
}
```
- Câu nghe (`聴解`) thêm `"script": [["N", "lời dẫn"], ["F", "nữ nói"], ["M", "nam nói"]]`.
- 発話表現 / 即時応答: 3 lựa chọn, thêm `"audioOptions": true` (lựa chọn được đọc, không in ra).
- 発話表現 thêm `"scene": "mô tả tình huống tiếng Việt"`.
- 文の組み立て: `"options"` là 4 thẻ, `"order"` thứ tự đúng (vd `[1,2,0,3]`), `"star"` vị trí ★ (0–3), `"answer"` = `order[star]`.
- Đoạn văn dùng chung cho cả mondai: trường `"passage"` của mondai; bảng thông tin: `"table"`.

## Lỗi thường gặp
Nếu workflow báo ❌, mở log để xem câu nào sai. File lỗi bị app **bỏ qua** (app không hỏng),
người dùng vẫn thấy bản cũ cho đến khi sửa xong.
