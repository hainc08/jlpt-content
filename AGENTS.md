# Bàn giao — jlpt-content (GitHub Pages)

## Dùng với công cụ nào
- File này (`AGENTS.md`) là **bản gốc** bối cảnh dự án, dùng chung cho Google Antigravity và Claude Code (`CLAUDE.md` chỉ trỏ về đây). Cập nhật mục *Trạng thái* / *Việc tiếp theo* ở đây sau mỗi đợt làm việc.
- Skill dự án: `.agents/skills/<tên>/SKILL.md` (Antigravity đọc trực tiếp). Đây là **bản sao** — bản chính nằm trên tài khoản claude.ai; khi sửa quy trình, sửa ở cả hai nơi.
- Các skill có nhắc công cụ riêng của Claude (device_bash, git bundle, Artifact…): trong IDE chạy trực tiếp trên máy thì bỏ qua phần đồng bộ đó, cứ chạy lệnh `flutter`/`git` bình thường.
- Môi trường: Windows, Flutter tại `C:\Users\admin\develop`, Python có sẵn (in console chỉ dùng ASCII). Bản đồ tổng: `D:\100.JLPT\README.md`.


- Repo `hainc08/jlpt-content` (người dùng cần tạo Public, push, bật Pages: main / root).
- `exams/<level>/index.json` liệt kê file đề theo thứ tự hiển thị; mỗi đề một file JSON. App JLPT Thi Thử đọc từ `https://hainc08.github.io/jlpt-content/exams/<level>/`.
- Thêm/sửa/xoá đề: xem `exams/HUONG_DAN.md`. Kiểm tra: `python exams/check_exams.py` (workflow `exams-check` chạy mỗi lần push).
- Nguồn soạn đề nằm ở app thi thử (`tools/content/*.py`); xuất bằng `python tools/build_exams.py --publish ../../content/exams`.
- Không đổi địa chỉ thư mục `exams/<level>/` sau khi app đã phát hành (bản app cũ sẽ không tải được đề).
- `kanji/<app>.json` (n5, n4, …): dữ liệu app Kanji Flashcard, đọc từ `https://hainc08.github.io/jlpt-content/kanji/<app>.json`. Kiểm tra: `python kanji/check_kanji.py`. Hướng dẫn: `kanji/HUONG_DAN.md`. Xuất từ code: `python tools/export_kanji_json.py ../../content/kanji` (trong repo jlptkanjin5).
