"""
app/services/system_monitor.py – Thu thập số liệu tài nguyên hệ thống.

Mục tiêu:
- get_cpu_usage() -> float: CPU % (psutil.cpu_percent)
- get_ram_usage() -> dict: used_gb, total_gb, percent
- get_disk_usage(path) -> dict: used_gb, total_gb, percent cho thư mục data/
- get_gpu_usage() -> dict | None: GPU %, VRAM used/total (dùng pynvml nếu có)
- get_system_uptime() -> str: thời gian hoạt động từ lúc khởi chạy
- get_all_metrics() -> dict: gom tất cả chỉ số trên
- Được gọi từ /api/system/metrics endpoint
"""
