// src/App.tsx
// Mục tiêu:
// - Cấu hình React Router v6 (BrowserRouter)
// - Định nghĩa các Route:
//     /login          → LoginPage (public)
//     /               → redirect → /dashboard
//     /dashboard      → DashboardPage (protected)
//     /live           → LiveMonitorPage (protected)
//     /cameras        → CamerasPage (protected)
//     /events         → EventsPage (protected)
//     /analytics      → AnalyticsPage (protected)
//     /settings       → SettingsPage (protected, admin only)
//     *               → NotFoundPage
// - ProtectedRoute component: kiểm tra authStore, redirect /login nếu chưa đăng nhập
// - AppLayout bọc ngoài tất cả protected routes (Sidebar + Topbar)
// - Khởi tạo WebSocket connection khi user đã đăng nhập
