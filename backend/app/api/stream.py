"""
app/api/stream.py – Endpoint streaming video MJPEG.

Mục tiêu:
- GET /stream/{camera_id}: StreamingResponse với Content-Type: multipart/x-mixed-replace
  + Lấy frame mới nhất từ ring buffer của camera worker
  + Vẽ bounding boxes lên frame trước khi encode thành JPEG
  + Encode JPEG với quality 75 để cân bằng tốc độ và chất lượng
  + Đẩy frame liên tục dưới dạng MJPEG
  + Dừng khi client ngắt kết nối (GeneratorExit)
- Yêu cầu JWT token (qua query param ?token= hoặc Authorization header)
"""
