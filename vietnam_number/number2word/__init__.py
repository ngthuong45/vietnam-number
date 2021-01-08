from vietnam_number.number2word.large_number import n2w_large_number
from vietnam_number.number2word.single import process_n2w_single
from vietnam_number.number2word.utils.base import pre_process_n2w


def n2w(number: str):
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_number = pre_process_n2w(number)

    return n2w_large_number(clean_number)


def n2w_single(number: str):
    # Xữ lý đặc thù dành cho số điện thoại
    if number[0:3] == '+84':
        number = number.replace('+84', '0')

    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_number = pre_process_n2w(number)

    return process_n2w_single(clean_number)
