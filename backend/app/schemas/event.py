"""
app/schemas/event.py – Schema Pydantic cho sự kiện phát hiện.

Mục tiêu:
- EventOut: tất cả field của bảng events, kèm camera_name
- EventListResponse: items: List[EventOut], total: int, page: int, page_size: int
- EventFilter: camera_id?, weapon_class?, status?, date_from?, date_to?, search?
- EventReviewRequest: status ('confirmed' | 'false_alarm'), note?
- BoundingBox: class_name, confidence, x1, y1, x2, y2
- EventAlertPayload: schema đẩy qua WebSocket khi có sự kiện mới
"""
