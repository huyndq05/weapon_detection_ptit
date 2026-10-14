"""
app/api/cameras.py – Endpoint quản lý camera.

Mục tiêu:
- GET    /cameras          : danh sách camera + trạng thái worker (FPS, active)
- POST   /cameras          : thêm camera mới, khởi động worker tương ứng
- GET    /cameras/{id}     : chi tiết camera
- PUT    /cameras/{id}     : sửa thông tin, restart worker nếu cần
- DELETE /cameras/{id}     : xóa camera, dừng worker
- POST   /cameras/{id}/toggle : bật/tắt camera
- POST   /cameras/test     : test kết nối URL (mở cv2.VideoCapture, trả resolution)
- PUT    /cameras/{id}/roi : cập nhật vùng ROI (danh sách polygon)
"""
