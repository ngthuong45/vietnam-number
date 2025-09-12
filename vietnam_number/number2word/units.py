from vietnam_number.number2word.data import units


def n2w_units(numbers: str):
    """Hàm chuyển đổi số sang chữ số cho hàng đơn vị.

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ số đầu ra.

    Raises:
        ValueError: Số đầu vào là rỗng.
        ValueError: Số đầu vào có giá trị lớn hơn 9.

    """
    if len(numbers) == 1:
        return units[numbers]

    elif not numbers:
        raise ValueError('Số rỗng!! vui lòng nhập số đúng định dạng!')

    else:
        raise ValueError('Số vượt quá giá trị của hàng đơn vị!')



if __name__ == '__main__':

    number = '9'
    print(n2w_units(number))
