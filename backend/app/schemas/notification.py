"""
app/schemas/notification.py – Schema Pydantic cho thông báo.

Mục tiêu:
- TelegramConfig: bot_token, chat_id, enabled
- EmailConfig: smtp_host, smtp_port, smtp_user, smtp_password, smtp_from, enabled
- WebhookConfig: url, secret_header?, enabled
- NotificationTestRequest: channel: Literal['telegram', 'email', 'webhook']
- NotificationTestResponse: success: bool, message: str, latency_ms: int?
"""
