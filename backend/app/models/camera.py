"""
app/models/camera.py – ORM model bảng Cameras.

Mục tiêu:
- Class Camera(Base):
  + id: int (PK)
  + name: str – tên hiển thị
  + url: str – RTSP URL hoặc số webcam (e.g. '0', 'rtsp://...')
  + location: str – mô tả vị trí đặt camera
  + is_active: bool – bật/tắt xử lý
  + confidence_threshold: float – ghi đè ngưỡng toàn cục (nullable)
  + roi: JSON – danh sách polygon [[x,y],...] (nullable) – vùng quan sát
  + detection_rules: JSON – cấu hình: min_frames, cooldown_seconds
  + resolution_width, resolution_height: int (nullable)
  + fps_limit: int – giới hạn FPS xử lý (mặc định 10)
  + added_by: int FK → users.id
  + created_at: datetime
  + updated_at: datetime
- Relationship: events (1-n)
"""
