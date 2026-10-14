"""
tests/test_events.py – Unit test cho event management endpoints.

Mục tiêu:
- Test GET  /api/events: danh sách sự kiện với filter
- Test GET  /api/events/{id}: chi tiết sự kiện
- Test PUT  /api/events/{id}/review: xác nhận sự kiện (confirmed/false_alarm)
- Test POST /api/events/export: xuất CSV
- Test phân trang: page, page_size
- Seed dữ liệu test vào DB tạm (SQLite in-memory)
"""
