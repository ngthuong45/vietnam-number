from vietnam_number.number2word.data import units


def process_n2w_single(numbers: str):
    """Hàm chuyển đổi số sang chữ số theo từng số một.

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ số đầu ra.
    """
    total_number = ''
    for element in numbers:
        total_number += units[element] + ' '

    return total_number.strip()


if __name__ == '__main__':
    number = '0908123456'

    print(process_n2w_single(number))
