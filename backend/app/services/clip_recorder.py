"""
app/services/clip_recorder.py – Cắt và lưu video clip quanh thời điểm phát hiện.

Mục tiêu:
- Class ClipRecorder:
  + Nhận ring buffer frame từ camera worker
  + on_detection(camera_id, event_id): bắt đầu lưu clip
    → Lấy N giây trước (từ ring buffer) + tiếp tục ghi N giây sau
  + Lưu file .mp4 vào data/clips/{date}/{event_id}.mp4 bằng cv2.VideoWriter
  + Cập nhật clip_path trong bảng events sau khi ghi xong
  + Giải phóng bộ nhớ sau khi ghi
- Tham số: pre_seconds (default 5), post_seconds (default 10), fps, resolution
"""
