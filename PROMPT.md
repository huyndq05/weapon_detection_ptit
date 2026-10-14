# Prompt giao cho Antigravity

## Mục tiêu

Xây dựng hệ thống phát hiện hung khí (dao, súng, ...) từ luồng camera RTSP/webcam sử dụng model YOLOv8 tùy chỉnh (`best.pt`), với giao diện web quản lý đầy đủ tính năng.

## Yêu cầu chức năng

1. **Phát hiện hung khí realtime** từ nhiều camera đồng thời
2. **Quản lý camera**: thêm/sửa/xóa, test kết nối, cấu hình ROI
3. **Ghi nhận sự kiện**: lưu ảnh chụp + video clip trước/sau phát hiện
4. **Thông báo**: Telegram bot, email SMTP, webhook tùy chỉnh
5. **Dashboard**: thống kê, biểu đồ, bản đồ nhiệt theo giờ
6. **Quản lý người dùng**: RBAC (admin / operator / viewer)
7. **Xuất dữ liệu**: CSV, PDF
8. **Đa ngôn ngữ**: Tiếng Việt / English

## Stack kỹ thuật

- **Backend**: Python 3.10, FastAPI, SQLAlchemy, SQLite, WebSocket
- **AI**: Ultralytics YOLOv8 (model: best.pt – YOLOv8m custom)
- **Frontend**: React 18, TypeScript, Vite, Tailwind CSS, shadcn/ui
- **State**: Zustand
- **Charts**: Recharts
- **Auth**: JWT (access + refresh token)

## Ràng buộc

- Không dùng Docker (chạy local bằng script .bat/.sh)
- Database: SQLite (file `data/armguard.db`)
- Video stream qua MJPEG endpoint `/api/stream/{camera_id}`
- WebSocket endpoint `/ws/alerts` để đẩy cảnh báo realtime
