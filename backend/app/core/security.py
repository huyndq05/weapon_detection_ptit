"""
app/core/security.py – Xác thực và bảo mật.

Mục tiêu:
- Hàm hash_password(plain: str) -> str: mã hóa mật khẩu bằng bcrypt
- Hàm verify_password(plain: str, hashed: str) -> bool: kiểm tra mật khẩu
- Hàm create_access_token(data: dict, expires_delta: timedelta) -> str: tạo JWT
- Hàm create_refresh_token(data: dict) -> str: tạo refresh JWT (TTL dài hơn)
- Hàm decode_token(token: str) -> dict: giải mã và validate JWT, raise HTTPException nếu hết hạn
- Sử dụng SECRET_KEY và thuật toán HS256 từ settings
"""
