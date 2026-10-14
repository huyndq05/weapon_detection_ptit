"""
app/api/events.py – Endpoint quản lý sự kiện phát hiện hung khí.

Mục tiêu:
- GET    /events               : lịch sử sự kiện, hỗ trợ filter + phân trang
  + Filters: camera_id, weapon_class, status, date_from, date_to
- GET    /events/{id}          : chi tiết sự kiện kèm bounding boxes
- PUT    /events/{id}/review   : xác nhận (confirmed) hoặc đánh dấu false alarm
- GET    /events/{id}/snapshot : trả về ảnh PNG của sự kiện
- GET    /events/{id}/clip     : stream/tải clip video
- DELETE /events/{id}          : xóa sự kiện + file ảnh/clip (chỉ admin)
- POST   /events/export        : xuất CSV/PDF theo filter hiện tại
"""
