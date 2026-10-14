// useAlertSound.ts
// Mục tiêu:
// - Hook phát âm thanh cảnh báo khi có sự kiện mới
// - Load file /public/alert.mp3
// - play(): phát âm thanh (debounce 2s để tránh spam)
// - Kiểm tra quyền audio của browser trước khi phát
// - Cho phép tắt âm thanh (lưu vào localStorage)