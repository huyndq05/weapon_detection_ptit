// RoiEditor.tsx
// Mục tiêu:
// - Canvas vẽ đè lên ảnh snapshot của camera
// - Cho phép người dùng vẽ polygon (vùng quan sát ROI) bằng click
// - Hiển thị các polygon đã vẽ (có thể xóa từng polygon)
// - Nút Lưu → PUT /api/cameras/{id}/roi
// - Nút Reset xóa toàn bộ ROI