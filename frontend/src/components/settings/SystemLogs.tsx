// SystemLogs.tsx
// Mục tiêu:
// - Hiển thị log từ GET /api/system/logs
// - Lọc theo level: ALL, DEBUG, INFO, WARNING, ERROR
// - Tìm kiếm trong log
// - Nút refresh + auto-refresh mỗi 10s
// - Màu theo level: debug=gray, info=blue, warning=yellow, error=red
// - Mono font, cuộn xuống cuối tự động