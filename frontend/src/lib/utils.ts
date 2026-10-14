// utils.ts – Tiện ích dùng chung
// Mục tiêu:
// - cn(...classes): merge Tailwind classes (clsx + tailwind-merge)
// - formatDate(date, format): định dạng ngày giờ (date-fns, locale vi)
// - formatConfidence(value: number): '85.3%'
// - formatFileSize(bytes: number): '1.2 MB'
// - getStatusColor(status): trả màu Tailwind class theo trạng thái sự kiện
// - getWeaponIcon(class_name): trả lucide icon component theo loại hung khí