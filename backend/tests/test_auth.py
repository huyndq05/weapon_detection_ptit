"""
tests/test_auth.py – Unit test cho authentication endpoints.

Mục tiêu:
- Test POST /api/auth/login thành công: trả access_token hợp lệ
- Test POST /api/auth/login thất bại: sai mật khẩu → 401
- Test POST /api/auth/refresh: làm mới token thành công
- Test GET  /api/auth/me: trả thông tin user hiện tại
- Test POST /api/auth/change-password: đổi mật khẩu thành công
- Dùng pytest-asyncio + httpx AsyncClient
"""
