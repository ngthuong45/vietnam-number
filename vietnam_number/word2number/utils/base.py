from collections import Counter
from functools import cached_property

from vietnam_number.word2number.data import (
    ALLOW_WORDS,
    KEYWORD_INDEX_TEMPLATE,
    TENS_SPECIAL,
    WORD_TO_KEYWORD,
)


class Numbers:
    """Class xữ lý chữ số đầu vào."""

    def __init__(self, words_number: list):
        """Khởi tạo instance của lớp Numbers.

        Args:
            words_number (list): Danh sách chữ số đầu vào.
        """
        self.words_number = words_number
        self.words_number_counter = Counter(words_number)

    @cached_property
    def get_keyword_index(self):
        """Lấy vị trí index của các từ khóa như mười, trăm, nghìn, triệu, tỷ.

        Returns:
            Trả về một dic gồm các keyword và vị trí index của nó.

        """
        keyword_index = KEYWORD_INDEX_TEMPLATE.copy()

        for index_position, word in enumerate(self.words_number):
            if keyword := WORD_TO_KEYWORD.get(word):
                keyword_index[keyword] = index_position

        return keyword_index


def convert_to_tens_word(words: list[str]) -> list[str]:
    """Xóa các từ không có trong ALLOW_WORDS và
    chuyển các từ mười, chục thành ['một,'mươi']

    Returns:
        Danh sách mới sau khi chuyển đổi
    """
    # Xóa các từ không có trong ALLOW_WORDS và
    # Chuyển các từ mười, chục thành ['một,'mươi']
    new_words = []
    for word in words:
        if word in TENS_SPECIAL:
            new_words.append("một")
            new_words.append("mươi")
        elif word in ALLOW_WORDS:
            new_words.append(word)
    return new_words


def pre_process_w2n(words: str):
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
    split_words = (
        words.replace("-", " ")  # replace ký tự đặt biệt "-" sang khoản trắng
        .lower()  # converting chuổi đầu vào thành chuổi viết thường
        .split()  # xóa khoảng trắng thừa và chia câu thành các từ
    )

    # Chuyển các từ 'mười', 'chục' thành cụm ['một,'mươi']
    clean_numbers = convert_to_tens_word(split_words)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_numbers:
        raise ValueError('không có chử số hợp lệ! vui lòng nhập chữ số hợp lệ.')

    return clean_numbers
