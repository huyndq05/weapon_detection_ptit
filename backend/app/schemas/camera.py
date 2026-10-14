"""
app/schemas/camera.py – Schema Pydantic cho quản lý camera.

Mục tiêu:
- CameraCreate: name, url, location, confidence_threshold?, roi?, fps_limit?, detection_rules?
- CameraUpdate: các field tương tự CameraCreate, tất cả optional
- CameraOut: tất cả field + id, is_active, added_by, created_at
- CameraStatusOut: id, name, is_active, current_fps, last_detection_at
- CameraTestRequest: url – dùng cho endpoint test kết nối
- CameraTestResponse: success: bool, message: str, resolution: str?
"""
