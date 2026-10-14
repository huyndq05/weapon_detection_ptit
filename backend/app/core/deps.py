"""
app/core/deps.py – FastAPI Dependencies (Depends).

Mục tiêu:
- get_current_user(token: str, db: AsyncSession): giải mã JWT, truy vấn DB, trả về User
- get_current_active_user: xác nhận user chưa bị vô hiệu hóa
- require_admin: kiểm tra role == 'admin', raise 403 nếu không phải
- require_operator: kiểm tra role trong ['admin', 'operator']
- Được dùng làm Depends() trong tất cả protected endpoints
"""
