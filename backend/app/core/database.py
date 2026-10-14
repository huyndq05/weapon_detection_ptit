"""
app/core/database.py – Kết nối cơ sở dữ liệu SQLite.

Mục tiêu:
- Tạo SQLAlchemy async engine kết nối tới SQLite (đường dẫn từ settings)
- Định nghĩa AsyncSessionLocal factory cho async session
- Cung cấp Base = declarative_base() cho các ORM model kế thừa
- Hàm init_db(): tạo tất cả bảng (CREATE TABLE IF NOT EXISTS)
- Hàm get_db(): async generator trả về DB session, dùng làm FastAPI Depends
"""
