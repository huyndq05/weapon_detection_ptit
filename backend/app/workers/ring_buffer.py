"""
app/workers/ring_buffer.py – Bộ đệm vòng lưu khung hình.

Mục tiêu:
- Class RingBuffer:
  + capacity: int – số frame tối đa (tính từ pre_seconds × fps)
  + buffer: collections.deque(maxlen=capacity)
  + push(frame: np.ndarray): thêm frame mới (tự xóa frame cũ nhất khi đầy)
  + get_all() -> List[np.ndarray]: lấy toàn bộ frame theo thứ tự thời gian
  + get_latest() -> np.ndarray | None: frame mới nhất
  + clear(): xóa toàn bộ
- Thread-safe: dùng threading.Lock
- Không sao chép frame (giữ reference) để tiết kiệm RAM
"""
