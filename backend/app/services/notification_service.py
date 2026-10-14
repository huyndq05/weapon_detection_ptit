"""
app/services/notification_service.py – Gửi thông báo qua các kênh.

Mục tiêu:
- async send_telegram(event: Event, snapshot_path): gửi ảnh + caption qua Bot API
- async send_email(event: Event, snapshot_path): gửi email HTML qua SMTP
- async send_webhook(event: Event): POST JSON payload tới webhook URL
- async notify_event(event: Event): gọi cả 3 kênh nếu được bật trong settings
- async test_channel(channel: str) -> TestResult: gửi thử và đo latency
- Xử lý lỗi: retry 3 lần với exponential backoff
- Đọc config Telegram/Email/Webhook từ bảng settings (không hardcode)
"""
