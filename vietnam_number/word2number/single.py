from vietnam_number.word2number.data import word_multiplier
from vietnam_number.word2number.units import process_units


def pre_process_single(words: list):
    """Tiền xữ lý danh sách chữ số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại danh sách, kiểm tra tính hợp lệ
    của danh sách...

    Args:
        words (list): Danh dách chữ số dùng để tiền xữ lý.

    Returns:
        Trả về danh sách chữ số sau khi đã được xữ lý.

    Raises:
        ValueError: Nếu chữ số đầu vào có từ liên kết.

    """
    for word in words:
        if word in word_multiplier:
            raise ValueError('Chữ số đầu vào có từ liên kết. Vui lòng sử dụng hàm dành riêng cho chữ số có từ liên kết.')

    return words


def process_single(words: list) -> str:
    """Xữ lý chử số từng từ một

    Args:
        words (list): Danh sách chữ số cần xữ lý.

    Returns:
        Chuỗi số sau khi xữ lý xong.
    """
    # Tiền xữ lý dữ liệu chữ số đầu vào.
    clean_number = pre_process_single(words)

    number_total = ''
    for word in clean_number:
        number_total += process_units([word])

    return number_total
