# Bàn giao — jlpt-content (GitHub Pages)

- Repo `hainc08/jlpt-content` (người dùng cần tạo Public, push, bật Pages: main / root).
- `exams/<level>/index.json` liệt kê file đề theo thứ tự hiển thị; mỗi đề một file JSON. App JLPT Thi Thử đọc từ `https://hainc08.github.io/jlpt-content/exams/<level>/`.
- Thêm/sửa/xoá đề: xem `exams/HUONG_DAN.md`. Kiểm tra: `python exams/check_exams.py` (workflow `exams-check` chạy mỗi lần push).
- Nguồn soạn đề nằm ở app thi thử (`tools/content/*.py`); xuất bằng `python tools/build_exams.py --publish ../../content/exams`.
- Không đổi địa chỉ thư mục `exams/<level>/` sau khi app đã phát hành (bản app cũ sẽ không tải được đề).
