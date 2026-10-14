#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "============================================"
echo " ArmGuard - Khởi động toàn bộ hệ thống"
echo "============================================"
echo " Backend : http://localhost:8000"
echo " Frontend: http://localhost:5173"
echo " API Docs: http://localhost:8000/docs"
echo " Nhấn Ctrl+C để dừng cả hai."
echo "============================================"

# Hàm dừng tất cả process khi Ctrl+C
cleanup() {
    echo ""
    echo "Đang dừng hệ thống..."
    kill $BACKEND_PID $FRONTEND_PID 2>/dev/null
    exit 0
}
trap cleanup INT TERM

# Chạy backend nền
cd "$SCRIPT_DIR/../backend"
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload &
BACKEND_PID=$!
deactivate

# Đợi backend khởi động
sleep 3

# Chạy frontend nền
cd "$SCRIPT_DIR/../frontend"
npm run dev &
FRONTEND_PID=$!

echo "Hệ thống đã khởi động! PID Backend=$BACKEND_PID | Frontend=$FRONTEND_PID"
wait
