"""
app/services/detector.py – Dịch vụ suy luận YOLO (AI Engine).

Mục tiêu:
- Class WeaponDetector (singleton):
  + load_model(path): nạp file .pt vào bộ nhớ, chọn device (CPU/CUDA/MPS)
  + detect(frame: np.ndarray) -> List[Detection]: chạy inference, lọc theo confidence
  + warm_up(): chạy inference giả một lần để JIT compile (giảm latency frame đầu)
  + get_model_info() -> dict: tên model, số class, device đang dùng
- Detection = dataclass: class_name, confidence, x1, y1, x2, y2, class_id
- Xử lý lỗi khi model chưa nạp hoặc CUDA OOM
- Thread-safe: dùng threading.Lock khi inference (model không thread-safe)
"""
