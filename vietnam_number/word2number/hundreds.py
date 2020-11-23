from vietnam_number.word2number.tens import process_tens
from vietnam_number.word2number.units import process_units
from vietnam_number.word2number.utils.hundreds import NumbersOfHundreds


def pre_process_hundreds(words: list) -> NumbersOfHundreds:
    """Tiền xữ lý danh sách chữ số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại danh sách, kiểm tra tính hợp lệ
    của danh sách...

    Args:
        words (list): Danh dách chữ số dùng để tiền xữ lý.

    Returns:
        Trả về một instance sau khi đã được xữ lý
        Nếu có lỗi sẽ trả về lỗi.

    """
    numbers_of_hundreds = NumbersOfHundreds.format_words(words)

    # Kiểm tra tính hợp lệ của danh sách chữ số.
    numbers_of_hundreds.validate()

    return numbers_of_hundreds


def process_hundreds(words: list) -> str:
    """Xữ lý chữ số hàng trăm.

    Args:
        words (list): Danh sách chữ số đầu vào.

    Returns:
        Chuổi số hàng trăm.

    """
    # Tiền xữ lý danh sách chữ số đầu vào.
    numbers_of_hundreds = pre_process_hundreds(words)

    # Xữ lý chữ số hàng trăm.
    clean_words_number = numbers_of_hundreds.words_number

    value_of_hundreds = []
    value_of_tens = []

    # Lấy vị trí index của từ khóa hàng chục
    tens_index = numbers_of_hundreds.get_keyword_index['tens_index']
    hundreds_index = numbers_of_hundreds.get_keyword_index['hundreds_index']

    if hundreds_index:
        value_of_hundreds = clean_words_number[:1]

        try:
            value_of_tens = clean_words_number[hundreds_index + 1 :]
        except IndexError:
            value_of_tens = []

        # Trường hợp ['bốn', 'trăm', 'hai'] == 420
        if len(value_of_tens) == 1:
            value_of_tens.append('không')

    elif tens_index:
        # Lấy giá trị của phần chục.
        try:
            value_of_tens = clean_words_number[tens_index - 1 : tens_index + 2]
        except IndexError:
            value_of_tens = clean_words_number[tens_index - 1 :]

        # Lấy giá trị của phần còn lại.
        remaining = clean_words_number[tens_index + 2 :]
        if not remaining:
            remaining = clean_words_number[: tens_index - 1]

        # Trường hợp cho các số như ['hai','mươi', 'ba'] == 023
        if len(clean_words_number) <= 3:
            value_of_hundreds = ['không']
            value_of_tens = clean_words_number

        if len(clean_words_number) == 4:
            # Trường hợp đặc biệt như ['ba', 'bốn', 'mươi', 'hai'] == 342
            if tens_index == 1:
                return process_tens(value_of_tens) + process_units(remaining)

            # Trường hợp đặc biệt như ['bốn', 'mươi', 'hai', 'ba'] == 423
            if tens_index == 2:
                return process_units(remaining) + process_tens(value_of_tens)

    # Trường hợp ['hai', 'ba'] == 023
    elif len(clean_words_number) <= 2:
        value_of_hundreds = ['không']
        value_of_tens = clean_words_number

    # Trường hợp ['năm', 'sáu', 'hai'] == 562
    elif len(clean_words_number) == 3:
        value_of_hundreds = clean_words_number[:1]
        value_of_tens = clean_words_number[1:]

    return process_units(value_of_hundreds) + process_tens(value_of_tens)
