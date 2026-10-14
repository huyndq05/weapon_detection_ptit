// EventsPage.tsx
// Mục tiêu:
// - EventFilters: lọc theo camera, loại hung khí, trạng thái, khoảng ngày
// - EventTable: bảng sự kiện có phân trang (10/25/50/100 dòng)
// - Click vào hàng → EventDetailDrawer (hiển thị ảnh, bounding boxes, clip)
// - Nút xác nhận (confirmed) / báo sai (false_alarm) ngay trong bảng
// - Nút xuất CSV / PDF
// - Highlight hàng có status = 'new'