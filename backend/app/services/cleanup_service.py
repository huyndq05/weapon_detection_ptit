"""
app/services/cleanup_service.py – Tự động dọn dẹp dữ liệu cũ.

Mục tiêu:
- async cleanup_old_events(db): xóa events + file ảnh/clip cũ hơn RETENTION_DAYS ngày
- async cleanup_storage(db): kiểm tra dung lượng, nếu vượt MAX_STORAGE_GB
  → Xóa events cũ nhất cho đến khi đủ dung lượng
- async cleanup_exports(): xóa file export cũ hơn 7 ngày trong data/exports/
- Được lên lịch chạy định kỳ bằng APScheduler (mỗi ngày lúc 3 giờ sáng)
- Ghi log mỗi lần chạy: số event đã xóa, dung lượng giải phóng
"""
