from vietnam_number.number2word.data import UNITS_WITH_TRAILING_SPACE_TABLE


def process_n2w_single(numbers: str):
    """Hàm chuyển đổi số sang chữ số theo từng số một.

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ số đầu ra.
    """
    return numbers.translate(UNITS_WITH_TRAILING_SPACE_TABLE).rstrip()


if __name__ == '__main__':
    number = '0908123456'

    print(process_n2w_single(number))
