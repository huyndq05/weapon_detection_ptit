// ws.ts – WebSocket client wrapper
// Mục tiêu:
// - Class WebSocketClient:
//   + connect(url, token): kết nối WebSocket với token qua query param
//   + disconnect(): đóng kết nối sạch
//   + onMessage(handler): đăng ký callback nhận message
//   + onStatusChange(handler): callback khi trạng thái thay đổi
//   + reconnect(): logic retry với exponential backoff (max 30s)
// - Singleton export để dùng trong useWebSocket hook