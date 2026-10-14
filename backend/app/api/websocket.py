"""
app/api/websocket.py – WebSocket endpoint đẩy cảnh báo realtime.

Mục tiêu:
- WS  /ws/alerts : kết nối WebSocket để nhận cảnh báo khi phát hiện hung khí
  + Client gửi JWT token qua query param ?token= hoặc tin nhắn đầu tiên
  + Server xác thực token, thêm client vào nhóm 'alerts'
  + Khi camera worker phát hiện hung khí → gọi manager.broadcast() → tất cả client nhận
  + Payload JSON: { event_id, camera_id, camera_name, weapon_class, confidence,
                    snapshot_url, detected_at, bounding_boxes }
  + Ping/Pong để giữ kết nối (heartbeat 30s)
  + Xử lý ngắt kết nối đột ngột (WebSocketDisconnect)
"""
