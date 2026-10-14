// HourHeatmap.tsx
// Mục tiêu:
// - Ma trận 7 hàng (thứ 2–CN) × 24 cột (0h–23h)
// - Mỗi ô màu gradient theo cường độ (0 = tối, nhiều sự kiện = đỏ)
// - Tooltip hiển thị số sự kiện khi hover
// - Trục X: giờ trong ngày, trục Y: ngày trong tuần
// - Tự vẽ bằng SVG hoặc thư viện như @nivo/heatmap