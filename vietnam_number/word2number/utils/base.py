from collections import Counter
from dataclasses import dataclass, field
from string import punctuation

from vietnam_number.word2number.data import (
    TENS_SPECIAL,
    WORD_TO_KEYWORD,
    ALLOW_WORDS_EXCLUDING_TENS_SPECIAL,
)

PUNCTUATION_TO_SPACE_TABLE = str.maketrans(punctuation, " " * len(punctuation))


@dataclass(repr=False, eq=False)
class Numbers:
    """Class xữ lý chữ số đầu vào.
    words_number (list): Danh sách chữ số đầu vào.
    """

    words_number: list[str]
    words_number_counter: Counter[str] = field(init=False)
    keyword_index: dict[str, int] = field(init=False)

    def __post_init__(self) -> None:
        self.words_number_counter = Counter(self.words_number)
        self.keyword_index = self.get_keyword_index()

    def get_keyword_index(self) -> dict[str, int]:
        """Lấy vị trí index của các từ khóa như mười, trăm, nghìn, triệu, tỷ.

        Returns:
            Trả về một dic gồm các keyword và vị trí index của nó.

        """
        return {
            keyword: index_position
            for index_position, word in enumerate(self.words_number)
            if (keyword := WORD_TO_KEYWORD.get(word))
        }


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
        if word in ALLOW_WORDS_EXCLUDING_TENS_SPECIAL:
            new_words.append(word)
        elif word in TENS_SPECIAL:
            new_words.append("một")
            new_words.append("mươi")
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
        words.translate(
            PUNCTUATION_TO_SPACE_TABLE
        )  # replace ký tự đặt biệt punctuation sang khoản trắng
        .lower()  # converting chuổi đầu vào thành chuổi viết thường
        .split()  # xóa khoảng trắng thừa và chia câu thành các từ
    )

    # Chuyển các từ 'mười', 'chục' thành cụm ['một,'mươi']
    clean_numbers = convert_to_tens_word(split_words)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_numbers:
        raise ValueError("không có chữ số hợp lệ! vui lòng nhập chữ số hợp lệ.")

    return clean_numbers
