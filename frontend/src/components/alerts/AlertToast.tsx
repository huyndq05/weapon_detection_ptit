// AlertToast.tsx
// Mục tiêu:
// - Toast notification popup khi có sự kiện mới (nhận từ WebSocket)
// - Hiển thị: tên camera, loại hung khí, confidence, thumbnail nhỏ
// - Auto dismiss sau 8 giây
// - Nút 'Xem chi tiết' → mở EventDetailDrawer
// - Âm thanh cảnh báo khi xuất hiện (useAlertSound hook)
// - Stack nhiều toast, giới hạn 3 toast cùng lúc