"""
app/workers/rules.py – Bộ lọc quy tắc phát hiện.

Mục tiêu:
- Class DetectionRules(camera_config):
  + min_consecutive_frames: int – cần N frame liên tiếp có detection mới kích hoạt
  + cooldown_seconds: float – khoảng nghỉ tối thiểu giữa 2 sự kiện (tránh spam)
  + roi_polygons: List[Polygon] – danh sách vùng quan sát (shapely)

  + should_detect(frame_index) -> bool: kiểm tra có nên chạy inference không
    (skip frame dựa theo fps_limit)
  + filter_by_roi(detections) -> List[Detection]:
    Lọc chỉ giữ detection có tâm bbox nằm trong polygon ROI
  + on_detection(detections) -> bool:
    Đếm consecutive frames, kiểm tra cooldown, trả True nếu cần tạo event
  + reset(): reset bộ đếm consecutive frames
"""
