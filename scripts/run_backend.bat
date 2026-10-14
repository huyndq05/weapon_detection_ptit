@echo off
echo [ArmGuard] Khoi dong Backend...
cd /d "%~dp0..\backend"
call venv\Scripts\activate.bat
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
