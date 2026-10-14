"""
app/api/analytics.py – Endpoint thống kê và phân tích.

Mục tiêu:
- GET /analytics/dashboard    : KPI tổng quan (events hôm nay, camera hoạt động, ...)
- GET /analytics/timeline     : số sự kiện theo thời gian (ngày/tuần/tháng)
- GET /analytics/weapons      : phân bố loại hung khí (pie chart data)
- GET /analytics/heatmap      : ma trận giờ × ngày trong tuần
- GET /analytics/cameras      : xếp hạng camera theo số sự kiện
- Tất cả endpoint hỗ trợ query param: from_date, to_date, camera_id
"""
