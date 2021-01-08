from vietnam_number.number2word.large_number import n2w_large_number
from vietnam_number.number2word.single import process_n2w_single
from vietnam_number.number2word.utils.base import pre_process_n2w


def n2w(number):
    # Kiểm tra tính hợp lệ của đầu vào
    if isinstance(number, int):
        number = str(number)

    if not isinstance(number, str):
        raise ValueError('Đầu vào không phải là kiểu dữ liệu dạng số nguyên(int) hoặc kiểu chuỗi (str)!')

    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_number = pre_process_n2w(number)

    return n2w_large_number(clean_number)


def n2w_single(number):
    # Kiểm tra tính hợp lệ của đầu vào
    if isinstance(number, int):
        number = str(number)

    if not isinstance(number, str):
        raise ValueError('Đầu vào không phải là kiểu dữ liệu dạng số nguyên(int) hoặc kiểu chuỗi (str)!')

    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_number = pre_process_n2w(number)

    return process_n2w_single(clean_number)
