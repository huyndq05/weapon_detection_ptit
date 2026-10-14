// LiveAlertsFeed.tsx
// Mục tiêu:
// - Panel danh sách sự kiện realtime (cuộn ngược - mới nhất lên đầu)
// - Mỗi item: timestamp, camera, loại hung khí, badge confidence
// - Nhận sự kiện từ alertStore (được cập nhật bởi WebSocket)
// - Giới hạn 50 item, xóa item cũ nhất khi đầy
// - Click item → mở EventDetailDrawer