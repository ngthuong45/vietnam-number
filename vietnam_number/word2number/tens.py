from vietnam_number.word2number.units import process_units
from vietnam_number.word2number.utils.tens import NumbersOfTens


def pre_process_tens(words: list) -> NumbersOfTens:
    """Tiền xữ lý danh sách chữ số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại danh sách, kiểm tra tính hợp lệ
    của danh sách...

    Args:
        words (list): Danh dách chữ số dùng để tiền xữ lý.

    Returns:
        Trả về một instance sau khi đã được xữ lý
        Nếu có lỗi sẽ trả về lỗi.

    """
    numbers_of_tens = NumbersOfTens.format_words(words)

    # Kiểm tra tính hợp lệ của danh sách chữ số.
    numbers_of_tens.validate()

    return numbers_of_tens


def process_tens(words: list) -> str:
    """Xữ lý chữ số hàng chục.

    Args:
        words (list): Danh sách chử số đầu vào.

    Returns:
        Chuổi số hàng chục.

    """
    # Tiền xữ lý danh sách chữ số đầu vào.
    numbers_of_tens = pre_process_tens(words)

    # Xữ lý chữ số hàng chục.
    clean_words_number = numbers_of_tens.words_number
    value_of_tens = ''
    value_of_units = ''

    # Lấy vị trí index của từ khóa hàng chục
    tens_index = numbers_of_tens.get_keyword_index['tens_index']

    if tens_index == 0:
        value_of_tens = 'một'
        try:
            value_of_units = clean_words_number[1]
        except IndexError:
            value_of_units = 'không'

    if tens_index == 1:
        value_of_tens = clean_words_number[0]
        try:
            value_of_units = clean_words_number[2]
        except IndexError:
            value_of_units = 'không'

    if tens_index is None:
        value_of_tens = clean_words_number[0]
        value_of_units = clean_words_number[1]

    return process_units([value_of_tens]) + process_units([value_of_units])
