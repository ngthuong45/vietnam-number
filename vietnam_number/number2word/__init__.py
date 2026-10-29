from vietnam_number.number2word.data import ZeroWord
from vietnam_number.number2word.large_number import n2w_large_number
from vietnam_number.number2word.single import process_n2w_single
from vietnam_number.number2word.utils.base import pre_process_n2w


def n2w(number: str, *, zero_word: ZeroWord = ZeroWord.LE):
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    """Convert a numeric string into Vietnamese words.

    Args:
        number: The numeric string to convert.

        zero_word: Selects how an interior zero digit is pronounced:
            ZeroWord.LE uses "lẽ", while ZeroWord.LINH uses "linh".

    Returns:
        The number expressed in Vietnamese words.

    Examples:
        >>> n2w("101")
        'một trăm lẽ một'

        >>> n2w("101", zero_word=ZeroWord.LINH)
        'một trăm linh một'

        >>> n2w("1234")
        'một nghìn hai trăm ba mươi bốn'
    """
    clean_number = pre_process_n2w(number)

    return n2w_large_number(clean_number, zero_word=zero_word)


def n2w_single(number: str):
    # Xữ lý đặc thù dành cho số điện thoại
    if number.startswith("+84"):
        number = number.replace("+84", "0", 1)

    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_number = pre_process_n2w(number)

    return process_n2w_single(clean_number)
