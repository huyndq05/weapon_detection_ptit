#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "[ArmGuard] Khởi động Backend..."
cd "$SCRIPT_DIR/../backend"
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
