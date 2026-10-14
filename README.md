# 🔫 ArmGuard – Hệ thống Phát hiện Hung khí Thời gian Thực

> Đồ án PTIT | Python · FastAPI · YOLOv8 · React · TypeScript

---

## 📋 Yêu cầu hệ thống

| Thành phần | Phiên bản tối thiểu |
|---|---|
| Python | 3.10+ |
| Node.js | 18+ |
| CUDA (tùy chọn) | 11.8+ |
| RAM | 8 GB |
| GPU VRAM (tùy chọn) | 4 GB |

---

## 🚀 Cài đặt nhanh

### 1. Clone và chuẩn bị model

```bash
git clone <repo-url>
cd weapon_detection_ptit

# Đặt file model vào thư mục models/
cp /path/to/best.pt models/best.pt
```

### 2. Cấu hình môi trường

```bash
cp .env.example .env
# Mở .env và chỉnh sửa các giá trị phù hợp
```

### 3. Chạy tự động (Windows)

```bat
scripts\run_all.bat
```

### 3. Chạy tự động (Linux/Mac)

```bash
chmod +x scripts/*.sh
./scripts/run_all.sh
```

---

## 🗂️ Cấu trúc dự án

```
weapon_detection_ptit/
├── backend/        FastAPI + YOLO inference + SQLite
├── frontend/       React + Vite + shadcn/ui
├── models/         File .pt (đặt thủ công)
├── data/           Sinh tự động khi chạy
└── scripts/        Script khởi chạy
```

---

## 🔑 Tài khoản mặc định

| Tài khoản | Mật khẩu | Vai trò |
|---|---|---|
| admin | admin123 | Quản trị viên |

> ⚠️ **Đổi mật khẩu ngay sau khi đăng nhập lần đầu!**

---

## 📡 Địa chỉ truy cập

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **Tài liệu API**: http://localhost:8000/docs

---

## 📞 Liên hệ


