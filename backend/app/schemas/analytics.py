"""
app/schemas/analytics.py – Schema Pydantic cho thống kê.

Mục tiêu:
- DashboardStats: total_events_today, total_cameras_active, total_false_alarms, avg_confidence
- TimeSeriesPoint: timestamp, count
- AlertsOverTime: data: List[TimeSeriesPoint], period: str
- WeaponDistribution: weapon_class: str, count: int, percentage: float
- HourHeatmapCell: hour: int, day_of_week: int, count: int
- CameraRanking: camera_id, camera_name, event_count
"""
