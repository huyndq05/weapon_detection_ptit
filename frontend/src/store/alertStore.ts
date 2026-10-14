// alertStore.ts – Zustand store cho cảnh báo realtime
// Mục tiêu:
// - State: alerts: EventAlert[], unreadCount: number
// - Actions:
//   + addAlert(alert): thêm vào đầu danh sách, tăng unreadCount
//   + markAllRead(): đặt unreadCount = 0
//   + clearAlerts(): xóa toàn bộ
// - Giới hạn tối đa 50 alert trong store