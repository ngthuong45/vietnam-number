from vietnam_number.data import units, word_multiplier
from vietnam_number.w2n.couple import process_couple
from vietnam_number.w2n.large_number import process_w2n
from vietnam_number.w2n.single import process_single


def preprocessing_number(words: str):
    """Tiền xữ lý chuỗi số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại chuỗi số, kiểm tra tính hợp lệ
    của chuỗi số...

    Args:
        words (str): Chuỗi số đầu vào.

    Returns:
        Trả về một instance sau khi đã được xữ lý
        Nếu có lỗi sẽ trả về lỗi.

    Raises:
        ValueError: Nếu đầu vào không phải là một chuỗi.
        ValueError: Nếu đầu vào là chuỗi rỗng.

    """
    clean_numbers = []

    if not isinstance(words, str):
        raise ValueError('Không phải là một chuỗi (string)! Vui lòng truyền vào chuỗi các chữ số.')

    words = words.replace('-', ' ')  # replace ký tự đặt biệt "-" sang khoản trắng
    words = words.lower()  # converting chuổi đầu vào thành chuổi viết thường

    if words.isdigit():  # trả về chuổi số nếu người dùng nhập chuổi số
        return int(words)

    split_words = words.strip().split()  # xóa khoảng trắng thừa và chia câu thành các từ

    # xóa các từ không có trong unit va word_multiplier
    for word in split_words:
        if word in units or word in word_multiplier:
            clean_numbers.append(word)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_numbers:
        raise ValueError('không có chử số hợp lệ! vui lòng nhập chữ số hợp lệ.')

    return clean_numbers


def w2n(number_sentence):
    """Chuyển đổi chữ số sang số.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    """
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_numbers = preprocessing_number(number_sentence)

    return int(process_w2n(clean_numbers))


def w2n_single(number_sentence):
    """Chuyển đổi chữ số sang số từng số một.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    """
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_numbers = preprocessing_number(number_sentence)

    return process_single(clean_numbers)


def w2n_couple(number_sentence):
    """Chuyển đổi chữ số sang số từng cặp số.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    """
    # Tiền xữ lý dữ liệu chuỗi số đầu vào
    clean_numbers = preprocessing_number(number_sentence)

    return process_couple(clean_numbers)


print(w2n_couple('hai mươi ba bảy tám mươi bốn năm bốn chín mươi mốt mười hai bảy năm'))
