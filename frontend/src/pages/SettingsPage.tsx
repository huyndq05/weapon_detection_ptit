// SettingsPage.tsx
// Mục tiêu:
// - Tabs: Phát hiện | Thông báo | Lưu trữ | Người dùng | Log hệ thống
// - DetectionSettings: ngưỡng confidence, IOU, số frame, cooldown
// - NotificationSettings: cấu hình Telegram/Email/Webhook + nút gửi thử
// - StorageSettings: max dung lượng, số ngày lưu, nút dọn dẹp thủ công
// - UsersSettings: bảng user CRUD (chỉ admin)
// - SystemLogs: hiển thị log cuộn realtime
// - Chỉ admin được truy cập