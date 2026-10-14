"""
ArmGuard – Điểm khởi chạy chính của FastAPI application.

Mục tiêu:
- Khởi tạo ứng dụng FastAPI với metadata (title, version, docs_url)
- Cấu hình CORS middleware (đọc danh sách origin từ config)
- Mount tất cả API router từ app/api/router.py
- Đăng ký WebSocket endpoint
- Xử lý sự kiện startup: tạo bảng DB, nạp model YOLO, khởi động camera workers
- Xử lý sự kiện shutdown: dừng tất cả workers, đóng kết nối DB
- Phục vụ static files (snapshots) tại /static/snapshots
- Chạy bằng: uvicorn main:app --reload
"""
