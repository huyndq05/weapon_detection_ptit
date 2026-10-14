"""
app/models/user.py – ORM model bảng Users.

Mục tiêu:
- Class User(Base):
  + id: int (PK, autoincrement)
  + username: str (unique, not null)
  + email: str (unique, not null)
  + hashed_password: str
  + full_name: str (nullable)
  + role: Enum('admin', 'operator', 'viewer') – mặc định 'viewer'
  + is_active: bool – mặc định True
  + avatar_url: str (nullable)
  + created_at: datetime
  + updated_at: datetime (auto-update)
  + last_login: datetime (nullable)
- Relationship: cameras (1-n), events (1-n)
"""
