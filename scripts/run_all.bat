@echo off
echo ============================================
echo  ArmGuard - Khoi dong toan bo he thong
echo ============================================
echo Backend : http://localhost:8000
echo Frontend: http://localhost:5173
echo API Docs: http://localhost:8000/docs
echo.
echo Nhan Ctrl+C de dung ca hai.
echo ============================================

REM Chay backend trong cua so moi
start "ArmGuard Backend" cmd /k "cd /d %~dp0..\backend && call venv\Scripts\activate.bat && uvicorn main:app --host 0.0.0.0 --port 8000 --reload"

REM Doi 3 giay cho backend khoi dong truoc
timeout /t 3 /nobreak >nul

REM Chay frontend trong cua so moi
start "ArmGuard Frontend" cmd /k "cd /d %~dp0..\frontend && npm run dev"

echo Dang khoi dong... Mo trinh duyet tai http://localhost:5173
pause
