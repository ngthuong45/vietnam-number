from vietnam_number.word2number.data import tens_words
from vietnam_number.word2number.single import process_single
from vietnam_number.word2number.tens import process_tens


def pre_process_couple(words: list):
    """Tiền xữ lý danh sách chữ số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại danh sách, kiểm tra tính hợp lệ
    của danh sách...

    Args:
        words (list): Danh dách chữ số dùng để tiền xữ lý.

    Returns:
        Trả về danh sách chữ số sau khi đã được xữ lý.

    Raises:
        ValueError: Nếu chữ số đầu vào có từ liên kết hàng chục.

    """
    # Trường hợp từ 'mươi' nằm ở cuối cùng.
    if words[-1] in tens_words:
        words.append('không')

    # Trường hợp từ 'mươi' nằm ở đầu.
    if words[0] in tens_words:
        raise ValueError("Từ 'mươi' không thể đặt ở vị trí đầu tiên. Vui lòng nhập dãy chữ số đúng định dạng!")

    return words


def process_couple(words: list) -> str:
    """Xữ lý chử số từng cặp số một.

    Args:
        words (list): Danh sách chữ số cần xữ lý.

    Returns:
        Chuỗi số sau khi xữ lý xong.
    """
    # Tiền xữ lý dữ liệu chữ số đầu vào.
    clean_number = pre_process_couple(words)

    # Lấy tất cả vị trí index của 'mươi'
    all_tens_index = [i for i, value in enumerate(clean_number) if value in tens_words]

    if not all_tens_index:
        return process_single(clean_number)

    value_of_tens = ''
    for i in range(0, len(all_tens_index)):
        first_tens_index = all_tens_index[i]

        try:
            second_tens_index = all_tens_index[i + 1]
            between_two_ten_index = clean_number[first_tens_index + 1 : second_tens_index - 1]

        # Khi duyệt đến vị trí từ 'mươi' cuối cùng.
        except IndexError:
            # Giá trị của phần còn lại tính từ vị trí từ 'mươi' cuối cùng
            between_two_ten_index = clean_number[first_tens_index + 1 :]

        if (len(between_two_ten_index) % 2) == 0:
            value_of_tens += process_tens(clean_number[first_tens_index - 1 : first_tens_index + 1])
            value_of_tens += process_single(between_two_ten_index)
        else:
            value_of_tens += process_tens(clean_number[first_tens_index - 1 : first_tens_index + 2])
            value_of_tens += process_single(between_two_ten_index[1:])

    return value_of_tens
