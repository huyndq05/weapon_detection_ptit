"""
app/services/analytics_service.py – Tính toán số liệu thống kê.

Mục tiêu:
- async get_dashboard_stats(db, date): KPI: total events, false alarms, avg confidence
- async get_timeline(db, from_date, to_date, granularity): GROUP BY ngày/giờ
- async get_weapon_distribution(db, from_date, to_date, camera_id): COUNT GROUP BY class
- async get_hour_heatmap(db, from_date, to_date): matrix 7×24 (ngày × giờ)
- async get_camera_ranking(db, from_date, to_date, limit): xếp hạng camera
- Tối ưu hóa bằng SQL thuần (SQLAlchemy text()) cho các query phức tạp
"""
