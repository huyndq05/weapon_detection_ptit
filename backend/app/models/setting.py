"""
app/models/setting.py – ORM model bảng Settings (cài đặt hệ thống).

Mục tiêu:
- Class Setting(Base): key-value store kiểu EAV
  + id: int (PK)
  + key: str (unique) – tên cài đặt
  + value: str – giá trị dạng string (JSON-serialized nếu phức tạp)
  + description: str (nullable)
  + updated_at: datetime

- Các key mặc định được seed khi init_db():
  + detection.confidence_threshold
  + detection.iou_threshold
  + detection.min_consecutive_frames
  + detection.cooldown_seconds
  + notification.telegram_enabled
  + notification.email_enabled
  + notification.webhook_enabled
  + storage.max_gb
  + storage.retention_days
  + system.auto_cleanup_enabled
"""
