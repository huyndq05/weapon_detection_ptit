"""
app/schemas/setting.py – Schema Pydantic cho cài đặt hệ thống.

Mục tiêu:
- SettingOut: key, value, description, updated_at
- SettingUpdate: value: str
- DetectionSettingsSchema: confidence_threshold, iou_threshold, min_frames, cooldown_seconds
- StorageSettingsSchema: max_gb, retention_days, auto_cleanup_enabled
- BulkSettingUpdate: settings: Dict[str, str] – cập nhật nhiều key cùng lúc
"""
