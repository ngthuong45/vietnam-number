from typing import Literal

from vietnam_number.number2word.hundreds import n2w_hundreds
from vietnam_number.number2word.utils.base import chunk_from_right

LABELS: tuple[Literal[""], Literal[" nghìn"], Literal[" triệu"], Literal[" tỷ"]] = (
    "",
    " nghìn",
    " triệu",
    " tỷ",
)


def build_scale_label(group_index: int) -> str:
    """
    Return the Vietnamese scale label for a 3-digit group position.
    Pattern repeats every 3 groups and adds 'tỷ' layers for higher magnitudes.
    Examples:
    | index | label           |
    |-------|-----------------|
    | 0     | ""              |
    | 1     | " nghìn"        |
    | 2     | " triệu"        |
    | 3     | " tỷ"           |
    | 4     | " nghìn tỷ"     |
    | 5     | " triệu tỷ"     |
    | 6     | " tỷ tỷ"        |
    | 7     | " nghìn tỷ tỷ"  |
    | 8     | " triệu tỷ tỷ"  |
    | 9     | " tỷ tỷ tỷ"     |
    """

    # base_label_index: 0 for index=0, else 1..3
    base_label_index: int = group_index and ((group_index - 1) % 3 + 1)

    # Determine label based on position
    # group_index | Calculation of base_label_index   | label assigned
    # ------------+-----------------------------------+---------------
    # 0           | 0                                 | ""
    # 1           | ((1-1)%3 +1) = (0%3 +1) = 1       | "nghìn"
    # 2           | ((2-1)%3 +1) = (1%3 +1) = 2       | "triệu"
    # 3           | ((3-1)%3 +1) = (2%3 +1) = 3       | "tỷ"
    # 4           | ((4-1)%3 +1) = (3%3 +1) = 1       | "nghìn"
    # 5           | ((5-1)%3 +1) = (4%3 +1) = 2       | "triệu"
    # 6           | ((6-1)%3 +1) = (5%3 +1) = 3       | "tỷ"
    # 7           | ((7-1)%3 +1) = (6%3 +1) = 1       | "nghìn"
    # 8           | ((8-1)%3 +1) = (7%3 +1) = 2       | "triệu"
    # 9           | ((9-1)%3 +1) = (8%3 +1) = 3       | "tỷ"

    base_label: str = LABELS[base_label_index]

    # Number of extra 'tỷ' to append:
    #   - Every full block of 3 adds one 'tỷ' layer
    #   - Subtract 1 when the base itself is 'tỷ' (i.e., base_label_index == 3)
    number_of_ty_suffixes: int = (group_index // 3) - (base_label_index // 3)

    return base_label + " tỷ" * number_of_ty_suffixes


def n2w_large_number(numbers: str):
    """Hàm chuyển đổi các số có giá trị lớn.

    Hàm chuyển đổi các số có giá trị lớn từ 999 đến 999.999.999.999

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ số đầu ra.

    """
    # Chúng ta cần duyệt chuổi số đầu vào từ phải sang trái nhằm phân biệt các giá trị từ nhỏ đến lớn.
    # Chia chuỗi số đầu vào thành các nhóm con có 3 phần tử.
    # vì cứ 3 phần tử số lại tạo thành một lớp giá trị, như lớp trăm, lớp nghìn, lớp triệu...
    reversed_large_number = chunk_from_right(numbers, 3)

    total_number = [
        n2w_hundreds(group_value) + build_scale_label(group_index)
        for group_index, group_value in enumerate(reversed_large_number)
        if group_value != "000"
    ]

    total_number.reverse()

    return " ".join(total_number)


if __name__ == '__main__':

    number = '4680000000'
    print(n2w_large_number(number))
    number = '2460125030000'
    print(n2w_large_number(number))
    number = '1000000000000000000'
    print(n2w_large_number(number))
