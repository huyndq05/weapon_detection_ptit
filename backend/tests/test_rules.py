"""
tests/test_rules.py – Unit test cho DetectionRules.

Mục tiêu:
- Test consecutive frames: 1,2 frame không tạo event; đủ N frame mới tạo
- Test cooldown: không tạo event thứ 2 trong khoảng cooldown
- Test ROI filter: detection ngoài ROI bị lọc bỏ, detection trong ROI giữ lại
- Test skip frame (fps_limit): should_detect() trả False đúng tỷ lệ
"""
