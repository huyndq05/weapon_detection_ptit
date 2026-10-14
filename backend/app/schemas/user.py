"""
app/schemas/user.py – Schema Pydantic cho quản lý người dùng.

Mục tiêu:
- UserBase: username, email, full_name, role
- UserCreate(UserBase): password
- UserUpdate: email?, full_name?, role?, is_active?
- UserOut(UserBase): id, is_active, created_at, last_login (không có password)
- UserListResponse: items: List[UserOut], total: int
"""
