from vietnam_number.number2word.data import units

CHAR_TO_REMOVE = {
    " ": None,
    "-": None,
    ".": None,
    ",": None,
}
TRANS_TABLE = str.maketrans(CHAR_TO_REMOVE)

def chunks(lst, n):
    """Hàm chia nhỏ danh sách đầu vào.

    Hàm dùng chia nhỏ danh sách đầu vào thành các nhóm danh sách con với số lượng các phần tử trong
    nhóm con là n

    Args:
        lst: Danh sách đầu vào.
        n: Số lượng phần tử trong một nhóm con.

    Returns:
        Danh sách các nhóm con có n phần tử.
    """
    return [lst[i : i + n] for i in range(0, len(lst), n)]


def pre_process_n2w(number: str):
    """Hàm tiền xữ lý dữ liệu đầu vào.

    Args:
        number (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi số sau khi được tiền xữ lý.
    """

    # xóa các ký tự đặt biệt
    number = number.translate(TRANS_TABLE)

    # Kiểm tra tính hợp lệ của đầu vào
    if not number.isdigit():
        raise ValueError('Đầu vào không phải là kiểu chuỗi chỉ chứa các ký tự số (isdigit)!')

    # xóa các ký tự số không có trong unit
    clean_number = "".join(element for element in number if element in units)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_number:
        raise ValueError("Số không hợp lệ, vui lòng nhập số đúng định dạng!")

    return clean_number
