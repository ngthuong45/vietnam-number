====================================
Vietnam Number Toolkit
====================================

.. image:: https://madewithlove.now.sh/vn?heart=true&colorB=%23d5481d
        :target: https://pypi.python.org/pypi/vietnam-number

.. image:: https://img.shields.io/pypi/v/vietnam-number
        :target: https://pypi.python.org/pypi/vietnam-number

.. image:: https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8-blue
        :target: https://pypi.python.org/pypi/vietnam-number

.. image:: https://img.shields.io/badge/license-GPLv3-brightgreen.svg
        :target: https://pypi.python.org/pypi/vietnam-number

.. image:: https://img.shields.io/badge/chat-on%20facebook-informational
        :target: https://www.facebook.com/ng.thuong45/

|

.. image:: https://user-images.githubusercontent.com/66929261/100044430-424d1800-2e42-11eb-8875-3b5abbf25ade.png

**Vietnam-number** là một thư viện Python mã nguồn mở hỗ trợ cho việc xữ lý chữ số trong Tiếng Việt.

+---------------------+------------------------------------------------------------------------------------------------+
|    **Support**      |                           **Description**                                                      |
+---------------------+------------------------------------------------------------------------------------------------+
| Văn nói - Văn viết  | * Hỗ trợ cho cả văn viết và văn nói thông dụng.                                                |
+---------------------+------------------------------------------------------------------------------------------------+
| Số có giá trị lớn   | * Hỗ trợ chuyển đổi chử số từ 0 đến 999.999.999.999                                            |
+---------------------+------------------------------------------------------------------------------------------------+
| Từ ngữ dân gian     | * Hỗ trợ các từ ngữ dân gian, vùng miền:                                                       |
|                     | * Vd: 'tỷ - tỏi', 'triệu - chai, củ', 'nghìn - ngàn', 'trăm - lít' , 'bốn - tư'...             |
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

| **$ pip install vietnam-number**

Tính năng
----------------------------------------

| `1. Chữ số sang số có từ liên kết.`_
| `2. Chữ số sang số không có từ liên kết.`_
| `3. Số sang chữ số có từ liên kết`_
| `4. Số sang chữ số không có từ liên kết`_

****************************************
1. Chữ số sang số có từ liên kết.
****************************************

.. image:: https://img.shields.io/badge/feature-word%20to%20number-orange

| Chuyển đổi **Chữ số** sang **Số** có các từ liên kết ('mươi', 'trăm', 'nghìn', 'triệu', 'tỷ').
| Sử dụng phù hợp trong các tình huống như: đơn vị tiền tệ, số tuổi...

.. code-block:: python

    >>> # -*- coding: utf-8 -*-
    >>> from vietnam_number import w2n
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
2. Chữ số sang số không có từ liên kết.
****************************************

.. image:: https://img.shields.io/badge/feature-word%20to%20number-orange

| Chuyển đổi **Chữ số** sang **Số** không có từ liên kết.
| Sử dụng phù hợp trong các tình huống một dãy nhiều chữ số khác nhau như: số chứng minh thư, số visa, số thẻ ATM, số điện thoại, tài khoản ngân hàng...

.. code-block:: python

    >>> # -*- coding: utf-8 -*-
    >>> from vietnam_number import w2n_single, w2n_couple

    # Văn nói cho cách đọc đơn từng số một.
    >>> text = 'không tám không chín một hai ba bốn năm sáu'

    >>> w2n_single(text)
    0809123456

    # Cách đọc đôi từng cặp số.
    # Bắt buộc số ban đầu phải là số kết hợp bởi từng cặp số,
    # hay nói cách khác số ban đầu phải có số lượng chữ số chia hết cho 2.
    # Trong trường hợp đặt biệt này, dãy số có thể có hoặc không có từ liên kết hàng chục là từ 'mươi'...
    # vd:
    #  032 -> 'không ba mươi hai' -> không được phép (số lượng phần tử số ban đầu lẽ) -> đầu ra không chính xác.
    #  0324 -> 'không ba mươi hai bốn' -> không được phép (không phải cách đọc từng cặp số một) -> đầu ra không chính xác
    #  0324 -> 'không ba hai mươi bốn' -> Ok
    >>> text = 'hai mươi ba bảy tám mươi bốn năm bốn chín mươi mốt mười hai bảy năm'

    >>> w2n_couple(text)
    20378454911275


****************************************
3. Số sang chữ số có từ liên kết
****************************************

.. image:: https://img.shields.io/badge/feature-number%20to%20word-yellow

| Chuyển đổi **Số** sang **Chữ số** cần có các từ liên kết như ('mươi', 'trăm', 'nghìn', 'triệu', 'tỷ').
| Sử dụng phù hợp trong các trường hợp như: giá sản phẩm, đơn vị tiền tệ, số tuổi...,
| Hỗ trợ văn nói cho các từ như 'một - mốt', 'năm - lăm', 'lẽ - linh'...

.. code-block:: python

    >>> # -*- coding: utf-8 -*-
    >>> from vietnam_number import n2w

    >>> number = '115205201211'
    >>> n2w(number)
    'một trăm mười lăm tỷ hai trăm lẽ năm triệu hai trăm lẽ một nghìn hai trăm mười một'


    # hỗ trợ một số trường hợp có cách đọc đặc biệt
    >>> list_number = ['111', '200', '101', '121', '815', '805', '825']
    >>> for element in list_number:
    ...      print(n2w(element))
    ...
    'một trăm mười một'
    'hai trăm'
    'một trăm lẽ một'
    'một trăm hai mươi mốt'
    'tám trăm mười lăm'
    'tám trăm lẽ năm'
    'tám trăm hai mươi lăm'


****************************************
4. Số sang chữ số không có từ liên kết
****************************************

.. image:: https://img.shields.io/badge/feature-number%20to%20word-yellow

| Chuyển đổi **Số** sang **Chữ số** không cần có các từ liên kết.
| Sử dụng phù hợp trong các trường hợp một chuỗi nhiều số khác nhau như: số chứng minh thư, số visa, số thẻ ATM, số điện thoại, tài khoản ngân hàng...

.. code-block:: python

    >>> # -*- coding: utf-8 -*-
    >>> from vietnam_number import n2w_single

    # Chuyển đổi từng số một.
    >>> number = '0908123456'
    >>> n2w_single(number)
    'không chín không tám một hai ba bốn năm sáu'

    # Hỗ trợ cho số có đầu số là '+84'
    >>> number = '+84908123456'
    >>> n2w_single(number)
    'không chín không tám một hai ba bốn năm sáu'


Tính Năng Trong Tương Lai
----------------------------------------

* Hỗ trợ số thập phân.
* Hỗ trợ số âm.
* Chuyển đổi số thứ tự
* Chuyển đổi ngày tháng năm
* Chuyển đổi đơn vị đo khối lượng (g - kg - yến - tạ - tấn)
* Chuyển đổi đơn vị đo độ dài (mm - cm - m - km)

Đóng Góp
----------------------------------------

Thông báo lỗi :beetle: tại https://github.com/ngthuong45/vietnam-number/issues

Nếu bạn phát hiện một lỗi mới, vui lòng thông báo đính kèm các thông tin:

* Thông tin hệ điều hành của bạn.
* Những thiết lập ở local nếu có.
* Các bước chi tiết dẫn đến phát hiện lỗi.

|

*Để lại một sao :star: nếu thư viện giúp ích được phần nào cho công việc của bạn nhé!.*
