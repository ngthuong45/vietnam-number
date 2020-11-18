from vietnam_number.data import units, word_multiplier
from vietnam_number.w2n.large_number import process_w2n


def w2n(number_sentence):
    """Chuyển đổi chữ số sang số.

    Args:
        number_sentence (str): Chuổi chữ số đầu vào.

    Returns:
        Số đầu ra

    Raises:
        ValueError: Nếu đầu vào không phải là một chuỗi.
        ValueError: Nếu đầu vào là chuỗi rỗng.

    """
    clean_numbers = []

    if not isinstance(number_sentence, str):
        raise ValueError('Không phải là một chuỗi (string)! Vui lòng truyền vào chuỗi các chữ số.')

    number_sentence = number_sentence.replace('-', ' ')  # replace ký tự đặt biệt "-" sang khoản trắng
    number_sentence = number_sentence.lower()  # converting chuổi đầu vào thành chuổi viết thường

    if number_sentence.isdigit():  # trả về chuổi số nếu người dùng nhập chuổi số
        return int(number_sentence)

    split_words = number_sentence.strip().split()  # xóa khoảng trắng thừa và chia câu thành các từ

    # xóa các từ không có trong vietnam_number_system va muoi, tram, nghin, trieu, ty
    for word in split_words:
        if word in units or word in word_multiplier:
            clean_numbers.append(word)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_numbers:
        raise ValueError('không có chử số hợp lệ! vui lòng nhập chữ số hợp lệ.')

    return int(process_w2n(clean_numbers))
