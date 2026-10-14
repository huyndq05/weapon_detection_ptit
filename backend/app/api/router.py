"""
app/api/router.py – Tổng hợp tất cả API routers.

Mục tiêu:
- Tạo api_router = APIRouter(prefix="/api")
- Include tất cả sub-router:
  + /api/auth          → auth.router
  + /api/users         → users.router
  + /api/cameras       → cameras.router
  + /api/stream        → stream.router
  + /api/events        → events.router
  + /api/analytics     → analytics.router
  + /api/settings      → settings.router
  + /api/notifications → notifications.router
  + /api/system        → system.router
- Router này được mount vào FastAPI app trong main.py
"""
