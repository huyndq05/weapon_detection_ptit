#!/usr/bin/env bash
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
echo "[ArmGuard] Khởi động Frontend..."
cd "$SCRIPT_DIR/../frontend"
npm run dev
