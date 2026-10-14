"""
app/services/event_service.py – Lưu và truy vấn sự kiện phát hiện.

Mục tiêu:
- async create_event(db, camera_id, detections, frame): 
  + Lưu bản ghi Event vào DB
  + Gọi snapshot_service để lưu ảnh
  + Gọi clip_recorder để đánh dấu bắt đầu ghi clip
  + Gọi notification_service để gửi thông báo (chạy background)
  + Broadcast qua WebSocket manager
- async get_events(db, filter): truy vấn có phân trang + filter
- async get_event_by_id(db, event_id): lấy chi tiết một sự kiện
- async review_event(db, event_id, status, note, reviewer_id): xác nhận/báo sai
- async delete_event(db, event_id): xóa DB + file ảnh/clip
"""
