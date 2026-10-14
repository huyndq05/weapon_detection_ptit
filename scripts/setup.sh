#!/usr/bin/env bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="$SCRIPT_DIR/.."

echo "============================================"
echo " ArmGuard - Cài đặt môi trường"
echo "============================================"

# Backend
echo "[1/4] Tạo virtual environment Python..."
cd "$ROOT_DIR/backend"
python3 -m venv venv

echo "[2/4] Cài đặt thư viện Python..."
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
deactivate

# Frontend
echo "[3/4] Cài đặt Node modules..."
cd "$ROOT_DIR/frontend"
npm install

# .env
echo "[4/4] Tạo file .env..."
cd "$ROOT_DIR"
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo "Đã tạo .env. Vui lòng chỉnh sửa trước khi chạy!"
else
    echo "File .env đã tồn tại, bỏ qua."
fi

echo ""
echo "============================================"
echo " Cài đặt HOÀN THÀNH!"
echo " Tiếp theo: ./scripts/run_all.sh"
echo "============================================"
