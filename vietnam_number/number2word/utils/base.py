from string import ascii_letters, punctuation, whitespace

CHAR_TO_REMOVE = ascii_letters + punctuation + whitespace
TRANS_TABLE = str.maketrans("", "", CHAR_TO_REMOVE)


def chunk_from_right(numeric_string: str, n: int):
    """
    Split a string into chunks of `n` characters, counting from the right.

    Args:
        numeric_string (str): The input string to split.
        n (int): The chunk size.

    Returns:
        list[str]: A list of substrings (chunks) from right to left.

    Examples:
        >>> chunk_from_right("1_234_567_890", 3)
        ['890', '567', '234', '1']
        >>> chunk_from_right("12_345", 3)
        ['345', '12']
        >>> chunk_from_right("123", 3)
        ['123']
        >>> chunk_from_right("12", 3)
        ['12']
    """
    return (
        numeric_string[max(i - n, 0) : i] for i in range(len(numeric_string), 0, -n)
    )


def pre_process_n2w(number: str):
    """Hàm tiền xữ lý dữ liệu đầu vào.

    Args:
        number (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi số sau khi được tiền xữ lý.
    """

    # xóa các ký tự đặt biệt
    clean_number = number.translate(TRANS_TABLE)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not number.isascii():
        raise ValueError("Số không hợp lệ, vui lòng nhập số đúng định dạng!")

    # Kiểm tra tính hợp lệ của đầu vào
    if not number.isdecimal():
        raise ValueError(
            "Đầu vào không phải là kiểu chuỗi chỉ chứa các ký tự số (0-9)!"
        )

    return clean_number
