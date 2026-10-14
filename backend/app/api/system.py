"""
app/api/system.py – Endpoint thông tin sức khỏe hệ thống.

Mục tiêu:
- GET /system/health  : liveness check (trả {"status": "ok"})
- GET /system/metrics : CPU %, RAM %, GPU % (nếu có), disk usage, uptime
- GET /system/logs    : lấy N dòng log gần nhất từ data/logs/app.log
  + query params: lines=100, level=ERROR
- GET /system/cameras-status : FPS thực tế và trạng thái từng camera worker
- Thông tin GPU lấy qua subprocess chạy nvidia-smi hoặc thư viện pynvml
"""
