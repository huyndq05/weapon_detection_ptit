"""
app/api/auth.py – Endpoint xác thực người dùng.

Mục tiêu:
- POST /auth/login: nhận username+password, trả access_token + refresh_token
- POST /auth/refresh: nhận refresh_token, trả access_token mới
- POST /auth/logout: vô hiệu hóa refresh_token (blacklist hoặc xóa)
- POST /auth/change-password: đổi mật khẩu (yêu cầu đăng nhập)
- GET  /auth/me: lấy thông tin user hiện tại
- Cập nhật last_login khi đăng nhập thành công
"""
