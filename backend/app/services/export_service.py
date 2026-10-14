"""
app/services/export_service.py – Xuất dữ liệu ra file CSV/PDF.

Mục tiêu:
- async export_csv(events: List[Event], filename) -> Path:
  + Tạo file CSV với pandas DataFrame
  + Lưu vào data/exports/{filename}.csv
  + Trả đường dẫn để download
- async export_pdf(events: List[Event], filename) -> Path:
  + Tạo PDF với bảng sự kiện + logo + tiêu đề bằng ReportLab
  + Bao gồm ảnh thumbnail của từng sự kiện (nếu có)
  + Lưu vào data/exports/{filename}.pdf
- Hỗ trợ filter trước khi export (cùng filter với events endpoint)
"""
