// LiveMonitorPage.tsx
// Mục tiêu:
// - CameraGrid hiển thị luồng MJPEG từ tất cả camera
// - LayoutSwitcher cho phép chuyển 1x1 / 2x2 / 3x3 / 4x4
// - Click vào tile → CameraEnlargedView (modal fullscreen)
// - LiveAlertsFeed ở panel bên phải
// - Chỉ báo trực quan khi camera offline
// - Cập nhật trạng thái camera realtime qua WebSocket