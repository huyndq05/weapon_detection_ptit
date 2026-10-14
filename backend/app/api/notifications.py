"""
app/api/notifications.py – Endpoint kiểm tra và cấu hình thông báo.

Mục tiêu:
- GET  /notifications/config        : lấy cấu hình (che token/password)
- PUT  /notifications/config        : cập nhật Telegram/Email/Webhook config
- POST /notifications/test          : gửi thông báo thử nghiệm
  + channel = 'telegram' | 'email' | 'webhook'
  + Trả về: success, message, latency_ms
- Lưu config vào bảng settings (không hardcode vào .env)
"""
