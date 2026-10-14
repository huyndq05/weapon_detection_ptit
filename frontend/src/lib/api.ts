// api.ts – Axios instance với interceptors
// Mục tiêu:
// - Tạo axios instance với baseURL từ import.meta.env.VITE_API_URL
// - Request interceptor: tự động thêm Authorization: Bearer <token> vào header
// - Response interceptor: 
//   + Khi 401 → gọi /auth/refresh, lưu token mới, retry request gốc
//   + Khi refresh thất bại → logout, redirect /login
// - Export các hàm API theo nhóm: authAPI, camerasAPI, eventsAPI, analyticsAPI, settingsAPI, systemAPI