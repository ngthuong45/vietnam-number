from typing import Literal

from vietnam_number.number2word.hundreds import n2w_hundreds
from vietnam_number.number2word.utils.base import chunks

LABELS: tuple[Literal[""], Literal[" nghìn "], Literal[" triệu "], Literal[" tỷ "]] = (
    "",
    " nghìn ",
    " triệu ",
    " tỷ ",
)


def n2w_large_number(numbers: str):
    """Hàm chuyển đổi các số có giá trị lớn.

    Hàm chuyển đổi các số có giá trị lớn từ 999 đến 999.999.999.999

    Args:
        numbers (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi chữ số đầu ra.

    """
    # Chúng ta cần duyệt chuổi số đầu vào từ phải sang trái nhằm phân biệt các giá trị từ nhỏ đến lớn.
    # tương tự như khi chúng ta xữ lý cho hàm n2w_hundreds
    reversed_large_number = numbers[::-1]

    # Chia chuỗi số đầu vào thành các nhóm con có 3 phần tử.
    # vì cứ 3 phần tử số lại tạo thành một lớp giá trị, như lớp trăm, lớp nghìn, lớp triệu...
    reversed_large_number = chunks(reversed_large_number, 3)

    total_number = []

    # Chúng ta đếm số lần vượt qua lớp tỷ để thêm lại chữ 'tỷ' vào chuỗi
    # ví dụ: số 1.000.000.000.000, chunks: ['000', '000', '000', '000', '1']
    # khi e == 3, thuật toán sẽ xem như trở về lại lớp nghìn nên cần phải thêm lại chữ 'tỷ' vào cuối
    # để kết quả chuyển đổi ra là: một nghìn tỷ
    n_of_billions_skipped = 0
    for group_index, reversed_group in enumerate(reversed_large_number):
        group_value = reversed_group[::-1]

        if group_value == "000":
            if group_index >= 3 and group_index % 3 == 0:
                n_of_billions_skipped += 1
            continue

        # Sau khi vượt qua lớp tỷ thì cách đọc sẽ lặp lại từ lớp nghìn
        # một tỷ -> một nghìn (tỷ) -> một triệu (tỷ) -> một tỷ (tỷ)
        # dùng (e - 1) % 3 để tận dụng sự lặp lại này.

        # Determine label based on position
        # group_index | Calculation of label_index        | label assigned
        # ------------+----------------------------------+---------------
        # 0           | 0 (since 0 <= 3)                  | ""
        # 1           | 1 (since 1 <= 3)                  | "nghìn"
        # 2           | 2 (since 2 <= 3)                  | "triệu"
        # 3           | 3 (since 3 <= 3)                  | "tỷ"
        # 4           | ((4-1)%3 +1) = (3%3 +1) = 1       | "nghìn"
        # 5           | ((5-1)%3 +1) = (4%3 +1) = 2       | "triệu"
        # 6           | ((6-1)%3 +1) = (5%3 +1) = 3       | "tỷ"
        # 7           | ((7-1)%3 +1) = (6%3 +1) = 1       | "nghìn"
        # 8           | ((8-1)%3 +1) = (7%3 +1) = 2       | "triệu"
        # 9           | ((9-1)%3 +1) = (8%3 +1) = 3       | "tỷ"

        label_index = group_index if group_index <= 3 else ((group_index - 1) % 3 + 1)
        number_as_word = n2w_hundreds(group_value) + LABELS[label_index]

        if n_of_billions_skipped:
            number_as_word += "tỷ " * n_of_billions_skipped
            n_of_billions_skipped = 0

        total_number.append(number_as_word)

    return ''.join(reversed(total_number)).strip()


if __name__ == '__main__':

    number = '4680000000'
    print(n2w_large_number(number))
    number = '2460125030000'
    print(n2w_large_number(number))
    number = '1000000000000000000'
    print(n2w_large_number(number))
