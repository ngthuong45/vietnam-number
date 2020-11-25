from vietnam_number.number2word.data import units


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
    chunks_lst = []
    for i in range(0, len(lst), n):
        chunks_lst.append(lst[i : i + n])

    return chunks_lst


def pre_process_n2w(number: str):
    """Hàm tiền xữ lý dữ liệu đầu vào.

    Args:
        number (str): Chuỗi số đầu vào.

    Returns:
        Chuỗi số sau khi được tiền xữ lý.
    """
    clean_number = ''

    if not isinstance(number, str):
        raise ValueError('Không phải là một chuỗi (string)! Vui lòng truyền vào chuỗi các số.')

    number = number.replace('-', ' ')  # replace ký tự đặt biệt "-" sang khoản trắng
    number = number.strip()  # xóa khoảng trắng thừa

    # xóa các số không có trong unit
    for element in number:
        if element in units:
            clean_number += element

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_number:
        raise ValueError("Số không hợp lệ, vui lòng nhập số đúng định dạng! vd: '123456789'")

    return clean_number
