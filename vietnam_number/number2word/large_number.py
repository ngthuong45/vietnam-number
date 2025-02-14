from vietnam_number.number2word.hundreds import n2w_hundreds
from vietnam_number.number2word.utils.base import chunks


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
    for e in range(0, len(reversed_large_number)):
        number_as_word = ''
        if reversed_large_number[e][::-1] == '000':
            if e >= 3 and (e - 1) % 3 == 2:
                n_of_billions_skipped += 1
            continue
        if e == 0:
            value_of_hundred = reversed_large_number[e][::-1]
            number_as_word = n2w_hundreds(value_of_hundred)

        # Sau khi vượt qua lớp tỷ thì cách đọc sẽ lặp lại từ lớp nghìn
        # một tỷ -> một nghìn (tỷ) -> một triệu (tỷ) -> một tỷ (tỷ)
        # dùng (e - 1) % 3 để tận dụng sự lặp lại này.
        elif e == 1 or (e > 3 and (e - 1) % 3 == 0):
            value_of_thousand = reversed_large_number[e][::-1]
            number_as_word = n2w_hundreds(value_of_thousand) + ' nghìn '
        elif e == 2 or (e > 3 and (e - 1) % 3 == 1):
            value_of_million = reversed_large_number[e][::-1]
            number_as_word = n2w_hundreds(value_of_million) + ' triệu '
        elif e == 3 or (e > 3 and (e - 1) % 3 == 2):
            value_of_billion = reversed_large_number[e][::-1]
            number_as_word = n2w_hundreds(value_of_billion) + ' tỷ '
        while n_of_billions_skipped != 0:
            number_as_word += 'tỷ '
            n_of_billions_skipped -= 1
        total_number.append(number_as_word)

    return ''.join(total_number[::-1]).strip()


if __name__ == '__main__':

    number = '4680000000'
    print(n2w_large_number(number))
    number = '2460125030000'
    print(n2w_large_number(number))
    number = '1000000000000000000'
    print(n2w_large_number(number))
