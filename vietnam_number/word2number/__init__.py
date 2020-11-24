from vietnam_number.word2number.couple import process_couple
from vietnam_number.word2number.large_number import process_large_number
from vietnam_number.word2number.single import process_single
from vietnam_number.word2number.utils.base import pre_process_w2n


def w2n(number_sentence):
    """Chuyển đổi chữ số sang số.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    """
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_numbers = pre_process_w2n(number_sentence)

    return process_large_number(clean_numbers)


def w2n_single(number_sentence):
    """Chuyển đổi chữ số sang số từng số một.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    """
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_numbers = pre_process_w2n(number_sentence)

    return process_single(clean_numbers)


def w2n_couple(number_sentence):
    """Chuyển đổi chữ số sang số từng cặp số.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    """
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_numbers = pre_process_w2n(number_sentence)

    return process_couple(clean_numbers)
