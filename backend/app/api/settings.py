"""
app/api/settings.py – Endpoint cài đặt hệ thống.

Mục tiêu:
- GET  /settings              : trả toàn bộ key-value settings
- GET  /settings/{key}        : trả một setting cụ thể
- PUT  /settings/{key}        : cập nhật một setting
- PUT  /settings              : cập nhật nhiều setting cùng lúc (bulk)
- POST /settings/reset        : đặt lại về giá trị mặc định
- Sau khi cập nhật detection settings → thông báo cho camera workers reload config
- Chỉ admin được ghi, operator/viewer chỉ được đọc
"""
