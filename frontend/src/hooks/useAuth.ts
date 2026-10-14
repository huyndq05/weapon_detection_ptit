// useAuth.ts
// Mục tiêu:
// - Hook bọc authStore để dễ dùng trong component
// - Trả về: { user, token, isAuthenticated, login, logout, isLoading }
// - login(username, password): gọi API, lưu token, fetch user profile
// - logout(): xóa token, redirect /login
// - Kiểm tra token expiry, tự refresh khi gần hết hạn