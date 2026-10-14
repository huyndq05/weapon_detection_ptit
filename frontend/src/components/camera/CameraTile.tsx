// CameraTile.tsx
// Mục tiêu:
// - Hiển thị luồng MJPEG qua thẻ <img src='/api/stream/{id}?token=...'>
// - Overlay: tên camera, địa điểm, FPS badge, trạng thái
// - Khi phát hiện → viền đỏ pulse + icon cảnh báo
// - Click → gọi onEnlarge callback
// - Chỉ báo camera offline (ảnh lỗi → placeholder + 'Mất kết nối')