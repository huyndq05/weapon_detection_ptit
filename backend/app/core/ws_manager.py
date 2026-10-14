"""
app/core/ws_manager.py – Quản lý kết nối WebSocket.

Mục tiêu:
- Class ConnectionManager:
  + active_connections: Dict[str, List[WebSocket]] phân theo nhóm (alerts, system)
  + connect(ws, group): chấp nhận kết nối WebSocket và thêm vào nhóm
  + disconnect(ws, group): xóa kết nối khỏi nhóm
  + broadcast(message: dict, group): gửi JSON tới tất cả client trong nhóm
  + send_personal(message: dict, ws): gửi tới một client cụ thể
- Singleton `manager` được import trong websocket endpoint và các service
- Xử lý lỗi khi client đột ngột ngắt kết nối (disconnect/send lỗi)
"""
