"""
app/schemas/auth.py – Schema Pydantic cho xác thực.

Mục tiêu:
- LoginRequest: username, password
- TokenResponse: access_token, refresh_token, token_type, expires_in
- RefreshRequest: refresh_token
- ChangePasswordRequest: old_password, new_password (min 8 ký tự)
"""
