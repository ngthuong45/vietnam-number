====================================
Vietnam Number Toolkit
====================================


.. image:: https://img.shields.io/pypi/v/underthesea.svg
        :target: https://pypi.python.org/pypi/underthesea

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue
        :target: https://pypi.python.org/pypi/underthesea

.. image:: https://img.shields.io/badge/license-GNU%20General%20Public%20License%20v3-brightgreen.svg
        :target: https://pypi.python.org/pypi/underthesea

.. image:: https://img.shields.io/badge/chat-on%20facebook-informational
    :target: https://www.facebook.com/undertheseanlp/

**Vietnam-number** là một thư viện Python mã nguồn mở hỗ trợ cho việc xữ lý chữ số trong Tiếng Việt.

+---------------------+------------------------------------------------------------------------------------------------+
|    Support          |                           Description                                                          |
+---------------------+------------------------------------------------------------------------------------------------+
| Văn nói - Văn viết  | * Hỗ trợ cho cả văn viết và văn nói thông dụng.                                                |
+---------------------+------------------------------------------------------------------------------------------------+
| Số có giá trị lớn   | * Hỗ trợ chuyễn đổi chử số từ 0 đến 999.999.999.999                                            |
+---------------------+------------------------------------------------------------------------------------------------+
| Từ ngữ dân gian     | * Hỗ trợ các từ ngữ dân gian, vùng miền:                                                       |
|                     | * Vd: 'tỷ = tỏi', 'triệu = chai, củ', 'nghìn = nghàn', 'trăm = lít' , 'bốn = tư'...            |
+---------------------+------------------------------------------------------------------------------------------------+
| Cách đọc đơn        | * Hỗ trợ chuyển đổi văn bản chữ số sang số theo cách đọc từng số:                              |
|                     | * Vd: 'không một hai ba bốn năm sáu bảy tám chín' = 0123456789                                 |
+---------------------+------------------------------------------------------------------------------------------------+
| Cách đọc đôi        | * Hỗ trợ chuyển đổi văn bản chữ số sang số theo cách đọc từng cặp số:                          |
|                     | * Vd: 'không một hai ba bốn mươi lăm sáu mươi bảy tám mươi chín' = 0123456789                  |
+---------------------+------------------------------------------------------------------------------------------------+

Cài đặt
----------------------------------------

Cài đặt vietnam-number bằng lệnh:

.. code-block:: bash

    $ pip install vietnam-number

Tính năng
----------------------------------------

- `Chữ số sang số có từ liên kết.`_
- `Chữ số sang số không có từ liên kết.`_

****************************************
Chữ số sang số có từ liên kết.
****************************************

.. image:: https://img.shields.io/badge/feature-word%20to%20number-orange

.. code-block:: python

    >>> # -*- coding: utf-8 -*-
    >>> from vietnam_number.main import w2n
    >>> text = 'một triệu không trăm tám mươi lăm nghìn ba trăm ba mươi hai'

    >>> w2n(text)
    1085332

    # Văn nói vắn tắt
    >>> text_1 = 'một triệu tư'
    >>> text_2 = 'nghàn hai'

    >>> w2n(text_1)
    1400000

    >>> w2n(text_2)
    1200

    # Hỗ trợ số có giá trị lớn
    >>> text = 'chín trăm năm mươi ba tỷ lẽ tám mươi bảy triệu'

    >>> w2n(text)
    953087000000

    # Văn nói đặt biệt
    # Chỉ áp dụng cho chữ số có từ liên kết.
    # Trường hợp không có từ liên kết chỉ áp dụng cho các số có giá trị từ 0 đến 999
    >>> text_1 = 'ba bốn mươi hai'
    >>> text_2 = 'ba mươi bảy năm'

    >>> w2n(text_1)
    342

    >>> w2n(text_1)
    375

    # Từ ngữ dân gian
    >>> text = 'bảy củ'

    >>> w2n(text)
    7000000

****************************************
Chữ số sang số không có từ liên kết.
****************************************

.. image:: https://img.shields.io/badge/feature-word%20to%20number-orange

.. code-block:: python

    >>> # -*- coding: utf-8 -*-
    >>> from vietnam_number.main import single_w2n

    # Văn nói cho cách đọc từng chữ số một
    # phù hợp trong một số trường hợp cần đọc chính xác từng chữ số một như
    # số điện thoại, số chứng minh nhân nhân, số thẻ ngân hàng...
    >>> text = 'không tám không chín một hai ba bốn năm sáu'

    >>> single_w2n(text)
    0809123456


Tính Năng Sắp Ra Mắt
----------------------------------------

* Hỗ trợ số thập phân.
* Hỗ trợ số âm.

Đóng Góp
----------------------------------------

Thông báo lỗi :beetle: tại https://github.com/undertheseanlp/underthesea/issues.

Nếu bạn thông báo một lỗi mới, vui lòng đính kèm các thông tin:

* Thông tin hệ điều hành của bạn.
* Những thiết lập ở local nếu có.
* Các bước chi tiết dẫn đến phát hiện lỗi.

| *Nhớ để lại một sao :star: nếu thư viện giúp ích được phần nào cho công việc của bạn nhé!.*
