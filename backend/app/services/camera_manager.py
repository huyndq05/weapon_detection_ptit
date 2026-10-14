"""
app/services/camera_manager.py – Quản lý vòng đời các camera worker.

Mục tiêu:
- Class CameraManager (singleton):
  + workers: Dict[int, CameraWorker] – map camera_id → worker
  + start_worker(camera: Camera): tạo và start CameraWorker trong thread riêng
  + stop_worker(camera_id): dừng worker, join thread
  + restart_worker(camera_id): stop rồi start lại
  + get_status() -> Dict[int, dict]: FPS, trạng thái, frame count
  + start_all(cameras: List[Camera]): khởi động tất cả camera khi app start
  + stop_all(): dừng tất cả khi app shutdown
"""
