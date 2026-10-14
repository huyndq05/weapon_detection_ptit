"""
app/core/logging.py – Cấu hình hệ thống ghi log.

Mục tiêu:
- Thiết lập Python logging với RotatingFileHandler ghi vào data/logs/app.log
- Format: timestamp | level | module | message
- Log level cấu hình từ APP_ENV (DEBUG khi development, INFO khi production)
- Cung cấp hàm get_logger(name: str) -> Logger để dùng trong các module khác
- Tự tạo thư mục data/logs/ nếu chưa tồn tại
"""
