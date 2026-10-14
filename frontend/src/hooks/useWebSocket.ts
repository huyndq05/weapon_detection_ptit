// useWebSocket.ts
// Mục tiêu:
// - Custom hook quản lý kết nối WebSocket tới /ws/alerts
// - Tự động kết nối khi user đã đăng nhập
// - Tự động reconnect khi mất kết nối (exponential backoff)
// - Parse message JSON, dispatch vào alertStore
// - Trả về: { isConnected, lastMessage, send }
// - Cleanup khi component unmount