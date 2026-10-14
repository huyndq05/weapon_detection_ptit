@echo off
echo ============================================
echo  ArmGuard - Cai dat moi truong
echo ============================================

REM --- Backend ---
echo [1/4] Tao virtual environment Python...
cd /d "%~dp0..\backend"
python -m venv venv
if %errorlevel% neq 0 ( echo LOI: Khong the tao venv. Kiem tra Python 3.10+ & pause & exit /b 1 )

echo [2/4] Cai dat thu vien Python...
call venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
if %errorlevel% neq 0 ( echo LOI: pip install that bai & pause & exit /b 1 )
call venv\Scripts\deactivate.bat

REM --- Frontend ---
echo [3/4] Cai dat Node modules...
cd /d "%~dp0..\frontend"
npm install
if %errorlevel% neq 0 ( echo LOI: npm install that bai & pause & exit /b 1 )

REM --- .env ---
echo [4/4] Tao file .env...
cd /d "%~dp0.."
if not exist ".env" (
    copy ".env.example" ".env"
    echo Da tao .env tu .env.example. Vui long chinh sua truoc khi chay!
) else (
    echo File .env da ton tai, bo qua.
)

echo.
echo ============================================
echo  Cai dat HOAN THANH!
echo  Tiep theo: scripts\run_all.bat
echo ============================================
pause
