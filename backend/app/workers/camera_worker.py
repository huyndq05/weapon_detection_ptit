"""
app/workers/camera_worker.py – Worker xử lý video cho một camera.

Mục tiêu:
- Class CameraWorker(threading.Thread):
  + camera: Camera object (config)
  + cap: cv2.VideoCapture – kết nối tới RTSP/webcam
  + ring_buffer: RingBuffer – lưu N giây frame gần nhất
  + running: threading.Event – flag điều khiển vòng lặp
  + current_fps: float – FPS thực tế (tính theo EMA)
  + latest_frame: np.ndarray – frame mới nhất để stream

  + run(): vòng lặp chính:
    1. Đọc frame từ camera
    2. Resize nếu cần (fps_limit)
    3. Đẩy frame vào ring_buffer
    4. Gọi rules.should_detect() để quyết định có chạy inference không
    5. Nếu detect: gọi detector.detect(frame)
    6. Nếu có kết quả: gọi rules.on_detection(), event_service.create_event()
    7. Lưu frame vào latest_frame để stream endpoint lấy
  + stop(): dừng vòng lặp, giải phóng cap
  + reconnect(): thử kết nối lại nếu camera mất tín hiệu (retry với backoff)
"""
