// AddCameraDialog.tsx
// Mục tiêu:
// - Form thêm / sửa camera (dùng chung)
// - Fields: tên, URL, địa điểm, ngưỡng confidence, giới hạn FPS
// - Nút 'Kiểm tra kết nối' → gọi API test, hiện badge kết quả + độ phân giải
// - Validate URL (RTSP hoặc số webcam)
// - Submit → POST hoặc PUT /api/cameras