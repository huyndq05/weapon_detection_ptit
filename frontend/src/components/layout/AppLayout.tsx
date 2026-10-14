// AppLayout.tsx
// Mục tiêu:
// - Layout chính bao gồm: <Sidebar> | <main> | (optional) panel
// - Quản lý trạng thái collapsed của Sidebar (lưu vào uiStore)
// - Responsive: Sidebar thu nhỏ thành icon-only trên màn nhỏ
// - Topbar cố định ở trên (sticky top)
// - Outlet của React Router để render page con