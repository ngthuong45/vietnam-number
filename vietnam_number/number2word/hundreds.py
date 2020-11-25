from vietnam_number.number2word.data import units
from vietnam_number.number2word.units import n2w_units


def n2w_hundreds(numbers: str):
    """Hàm chuyển đổi số sang chữ số lớp trăm.

    Hàm chuyển đổi số sang chữ số áp dụng cho các số từ 0 đến 999

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ số đầu ra.

    Raises:
        ValueError: Nếu số đầu vào lớn hơn 999.
        ValueError: Nếu số đầu vào là chuỗi rỗng.

    """
    if len(numbers) > 3:
        raise ValueError('Số vượt quá giá trị của hàng trăm!')

    if len(numbers) == 0:
        raise ValueError('Số vượt quá giá trị của hàng trăm!')

    if len(numbers) <= 1:
        return n2w_units(numbers)

    # Chúng ta cần duyệt danh sách từ phải qua trái nhằm phân biệt các giá trị từ nhỏ đến lớn.
    # Lý giải: giả sử chúng ta có 2 đầu vào: '10' và '123'
    # tại vị trí index đầu tiên của 2 chuỗi điều có giá trị là 1
    # tuy nhiên, chuỗi đầu 1 là giá trị của hàng chục.
    # chuỗi cuối 1 là giá trị của hàng trăm.
    reversed_hundreds = numbers[::-1]

    total_number = []
    for e in range(0, len(reversed_hundreds)):

        if e == 0:
            total_number.append(units[reversed_hundreds[e]])
        elif e == 1:
            total_number.append(units[reversed_hundreds[e]] + ' mươi ')
        elif e == 2:
            total_number.append(units[reversed_hundreds[e]] + ' trăm ')

    # vd: ta có total_number = ['không', 'hai mươi ', 'một trăm ']
    # có nghĩa là ta muốn kết quả cuối cùng là: ['một trăm ', 'hai mươi ', 'không']
    # Các trường hợp đặc biệt:
    #       1. 'hai mươi không' trở thành 'hai mươi'
    #       2. 'ba trăm không mươi hai' trở thành 'ba trăm lẽ hai'
    #       3. 'một mươi một' trở thành 'mười một'
    #       4. 'hai mươi một' trở thành 'hai mươi mốt'
    #       5. 'một mươi năm' trở thành 'mười lăm'
    #       6. 'hai trăm ba mươi năm' trở thành 'hai trăm ba mươi lăm'
    #       7. 'hai trăm không mươi ba' trở thành 'hai trăm lẽ ba'
    for idx, value in enumerate(total_number):
        if idx == 0 and value == 'không':

            if total_number[1] == 'không mươi ':
                total_number[1] = ''

            total_number[idx] = ''

        if idx == 0 and value == 'một':
            if total_number[1] != 'một mươi ' and total_number[1] != 'không mươi ':
                total_number[idx] = 'mốt'

        if idx == 0 and value == 'năm':
            if total_number[1] != 'không mươi ':
                total_number[idx] = 'lăm'

        if value == 'không mươi ':
            total_number[idx] = 'lẽ '

        if value == 'một mươi ':
            total_number[idx] = 'mười '

    return ''.join(total_number[::-1]).strip()


if __name__ == '__main__':

    number = '111'
    print(n2w_hundreds(number))

    number = '200'
    print(n2w_hundreds(number))

    number = '101'
    print(n2w_hundreds(number))

    number = '121'
    print(n2w_hundreds(number))

    number = '815'
    print(n2w_hundreds(number))

    number = '805'
    print(n2w_hundreds(number))

    number = '825'
    print(n2w_hundreds(number))
