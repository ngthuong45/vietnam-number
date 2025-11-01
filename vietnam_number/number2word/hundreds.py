from typing import Literal

from vietnam_number.number2word.data import UNITS

POSITION_UNITS: tuple[Literal[""], Literal[" mươi "], Literal[" trăm "]] = (
    "",
    " mươi ",
    " trăm ",
)
SPECIAL_TENS: frozenset[Literal["mười ", "lẽ "]] = frozenset(("mười ", "lẽ "))


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
    # Optimal order: highest frequency first
    numbers_length = len(numbers)
    if numbers_length == 3 or numbers_length == 2:
        pass

    elif numbers_length == 1:
        return UNITS[numbers]

    else:
        raise ValueError("Số vượt quá giá trị của hàng trăm!")

    # Chúng ta cần duyệt danh sách từ phải qua trái nhằm phân biệt các giá trị từ nhỏ đến lớn.
    # Lý giải: giả sử chúng ta có 2 đầu vào: '10' và '123'
    # tại vị trí index đầu tiên của 2 chuỗi điều có giá trị là 1
    # tuy nhiên, chuỗi đầu 1 là giá trị của hàng chục.
    # chuỗi cuối 1 là giá trị của hàng trăm.

    # example for numbers = "123"
    # numbers = "123"
    #        |
    #        v
    # reversed_hundreds = "321"
    #        |
    #        v
    # digit_position 0: "3" → "ba"  +   ""     → append → ["ba"]
    # digit_position 1: "2" → "hai" + " mươi " → append → ["ba", "hai mươi "]
    # digit_position 2: "1" → "một" + " trăm " → append → ["ba", "hai mươi ", "một trăm "]
    #        |
    #        v
    # Reverse list for final output: ["một trăm ", "hai mươi ", "ba"]

    reversed_hundreds: str = numbers[:-4:-1]

    total_number = (
        UNITS[digit_character] + POSITION_UNITS[digit_position]
        for digit_position, digit_character in enumerate(reversed_hundreds)
    )

    # vd: ta có total_number = ['không', 'hai mươi ', 'một trăm ']
    # có nghĩa là ta muốn kết quả cuối cùng là: ['một trăm ', 'hai mươi ', 'không']
    # Các trường hợp đặc biệt:
    #       1. 'hai mươi không' trở thành 'hai mươi'
    #       2. 'ba trăm không mươi hai' trở thành 'ba trăm lẽ hai'
    #       3. 'một mươi một' trở thành 'mười một'
    #       4. 'hai mươi một' trở thành 'hai mươi mốt'
    #       5. 'một mươi năm' trở thành 'mười lăm'
    #       6. 'hai trăm ba mươi năm' trở thành 'hai trăm ba mươi lăm'

    # Separate digits
    if numbers_length == 3:
        digit_unit, digit_tens, digits_hundred = total_number
    else:
        digit_unit, digit_tens = total_number
        digits_hundred = ""

    # Adjust tens
    if digit_tens == "không mươi ":
        # Case: tens = 'không mươi '
        # Example list before: ['không', 'không mươi ', 'hai trăm '] (200)

        if digit_unit == "không":
            # Nested case: units = 'không'
            # Example list before: ['không', 'không mươi ', 'hai trăm ']
            digit_tens = ""
            # Example list after assignment: ['không', '', 'hai trăm ']
        else:
            # Nested else: units ≠ 'không'
            # Example list before: ['năm', 'không mươi ', 'hai trăm '] (205)
            digit_tens = "lẽ "
            # Example list after assignment: ['năm', 'lẽ ', 'hai trăm ']
            # case 2. 'ba trăm không mươi hai' trở thành 'ba trăm lẽ hai'

    elif digit_tens == "một mươi ":
        # Case: tens = 'một mươi '
        # Example list before: ['một', 'một mươi ', 'một trăm '] (111)
        digit_tens = "mười "
        # Example list after assignment: ['một', 'mười ', 'một trăm ']
        # case 3. 'một mươi một' trở thành 'mười một'
        # half case 5. 'một mươi năm' trở thành 'mười lăm'

    # Adjust units
    if digit_unit == "không":
        # Case: units = 'không'
        # Example list before: ['không', 'không mươi ', 'hai trăm '] (200)
        digit_unit = ""
        # Example list after assignment: ['', 'không mươi ', 'hai trăm ']
        # case 1. 'hai mươi không' trở thành 'hai mươi'

    elif digit_unit == "một" and digit_tens not in SPECIAL_TENS:
        # Case: units = 'một' AND tens ≠ 'mười ' or 'lẽ '
        # Example list before: ['một', 'hai mươi ', 'hai trăm '] (221)
        digit_unit = "mốt"
        # Example list after assignment: ['mốt', 'hai mươi ', 'hai trăm ']
        # case 4. 'hai mươi một' trở thành 'hai mươi mốt'

    elif digit_unit == "năm" and digit_tens != "lẽ ":
        # Case: units = 'năm' AND tens ≠ 'lẽ '
        # Example list before: ['năm', 'một mươi ', 'hai trăm '] (215)
        digit_unit = "lăm"
        # Example list after assignment: ['lăm', 'một mươi ', 'hai trăm ']
        # half case 5. 'một mươi năm' trở thành 'mười lăm'
        # case 6. 'hai trăm ba mươi năm' trở thành 'hai trăm ba mươi lăm'

    # Combine everything
    return (digits_hundred + digit_tens + digit_unit).rstrip()


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
