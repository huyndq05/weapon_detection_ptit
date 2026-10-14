"""
tests/test_cameras.py – Unit test cho camera management endpoints.

Mục tiêu:
- Test GET  /api/cameras: danh sách camera (kết quả rỗng ban đầu)
- Test POST /api/cameras: tạo camera mới thành công
- Test PUT  /api/cameras/{id}: cập nhật camera
- Test DELETE /api/cameras/{id}: xóa camera
- Test POST /api/cameras/test: test kết nối URL (mock cv2.VideoCapture)
- Test phân quyền: viewer không được thêm/xóa camera (403)
"""
