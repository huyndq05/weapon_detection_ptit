"""
app/api/users.py – Endpoint quản lý người dùng (chỉ admin).

Mục tiêu:
- GET    /users        : danh sách người dùng (phân trang, tìm kiếm)
- POST   /users        : tạo người dùng mới
- GET    /users/{id}   : chi tiết người dùng
- PUT    /users/{id}   : cập nhật thông tin (role, is_active, ...)
- DELETE /users/{id}   : xóa mềm (is_active = False) hoặc xóa hẳn
- Tất cả endpoint yêu cầu role == 'admin' (require_admin dependency)
"""
