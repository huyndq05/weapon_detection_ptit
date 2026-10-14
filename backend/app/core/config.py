"""
app/core/config.py – Cấu hình ứng dụng.

Mục tiêu:
- Định nghĩa class Settings(BaseSettings) đọc biến từ file .env
- Các nhóm cấu hình: App, Database, JWT, Model, Storage, Telegram, Email, Webhook, CORS
- Cung cấp singleton `settings` để import khắp project
- Validate kiểu dữ liệu (int, bool, List[str], Path) bằng Pydantic
- Tự tạo thư mục data/* nếu chưa tồn tại khi khởi động
"""
