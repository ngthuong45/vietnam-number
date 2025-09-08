from functools import cached_property

from vietnam_number.word2number.data import (
    ALLOW_WORDS,
    billion_words,
    hundreds_words,
    million_words,
    special_word,
    tens_special,
    tens_words,
    thousand_words,
)

KEYWORD_INDEX_TEMPLATE = {
    "tens_index": None,
    "hundreds_index": None,
    "thousand_index": None,
    "million_index": None,
    "billion_index": None,
    "special_index": None,
}


class Numbers(object):
    """Class xữ lý chữ số đầu vào."""

    def __init__(self, words_number: list):
        """Khởi tạo instance của lớp Numbers.

        Args:
            words_number (list): Danh sách chữ số đầu vào.
        """
        self.words_number = words_number

    @cached_property
    def get_keyword_index(self):
        """Lấy vị trí index của các từ khóa như mười, trăm, nghìn, triệu, tỷ.

        Returns:
            Trả về một dic gồm các keyword và vị trí index của nó.

        """
        keyword_index = KEYWORD_INDEX_TEMPLATE.copy()

        for index_position, word in enumerate(self.words_number):
            if word in tens_words:
                keyword_index["tens_index"] = index_position

            if word in hundreds_words:
                keyword_index["hundreds_index"] = index_position

            if word in thousand_words:
                keyword_index["thousand_index"] = index_position

            if word in million_words:
                keyword_index["million_index"] = index_position

            if word in billion_words:
                keyword_index["billion_index"] = index_position

            if word in special_word:
                keyword_index["special_index"] = index_position

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
        if word in tens_special:
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
    words = words.replace('-', ' ')  # replace ký tự đặt biệt "-" sang khoản trắng
    words = words.lower()  # converting chuổi đầu vào thành chuổi viết thường

    split_words = words.strip().split()  # xóa khoảng trắng thừa và chia câu thành các từ

    # Chuyển các từ 'mười', 'chục' thành cụm ['một,'mươi']
    clean_numbers = convert_to_tens_word(split_words)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_numbers:
        raise ValueError('không có chử số hợp lệ! vui lòng nhập chữ số hợp lệ.')

    return clean_numbers
