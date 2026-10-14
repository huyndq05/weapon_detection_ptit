"""
app/models/event.py – ORM model bảng Events (sự kiện phát hiện hung khí).

Mục tiêu:
- Class Event(Base):
  + id: int (PK)
  + camera_id: int FK → cameras.id
  + detected_at: datetime – thời điểm phát hiện
  + weapon_class: str – nhãn phân loại (knife, gun, ...)
  + confidence: float – độ tin cậy cao nhất trong frame
  + snapshot_path: str – đường dẫn tương đối ảnh chụp
  + clip_path: str – đường dẫn clip video (nullable)
  + bounding_boxes: JSON – danh sách [{class, conf, x1, y1, x2, y2}]
  + status: Enum('new', 'confirmed', 'false_alarm') – mặc định 'new'
  + reviewed_by: int FK → users.id (nullable)
  + review_note: str (nullable)
  + notified: bool – đã gửi thông báo chưa
  + created_at: datetime
"""
