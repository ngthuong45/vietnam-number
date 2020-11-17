# vietnam-number
Thư viện xữ lý chữ số dành riêng cho Tiếng Việt. Hỗ trợ chuyển đổi chữ số thành số.

**Tính năng chuyễn chữ số thành số trong Tiếng Việt (word to number):**
- Hỗ trợ cho cả văn nói và văn viết
- Hỗ trợ cho chữ số từ không đến trăm tỷ (0 đến 000.000.000.000)
- Hỗ trợ một số cách đọc chữ số vắn tắt
- Hỗ trợ từ ngữ nhân giang:
    * Tỷ: tỏi
    * Triệu: chai, củ
    * Nghìn: nghàn, ngàn
    * Trăm: lít
    * ...

#### Sử dụng

```
from vietnam_number.main import w2n

# Cách nói vắn tắt
print(w2n('một triệu hai'))
>>> 1200000

# Hỗ trợ số lớn
print(w2n('năm tỷ lẽ hai nghìn ba trăm'))
>>> 5000002300

# Cách nói đặc biệt
print(w2n('ba bốn mươi hai'))
>>> 342

# Cách nói đặc biệt
print(w2n('ba mươi bảy năm'))
>>> 375

# Cách nói nhân gian
print(w2n('bảy củ'))
>>> 7000000

# Cách nói nhân gian
print(w2n('tám triệu tư'))
>>> 8400000

```

#### Những tính năng cần có trong tương lai:

- Chuyển đổi số thành chữ số
- Hỗ trợ chuyển đổi chữ số sang số theo phong cách đọc từng chữ một.
- Hỗ trợ số thập phân
- Hỗ trợ số âm
- ...

_Hãy để lại cho mình một sao nếu thư viện giúp ích được phần nào công việc của bạn._
