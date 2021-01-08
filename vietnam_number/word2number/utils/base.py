from vietnam_number.word2number.data import (
    billion_words,
    hundreds_words,
    million_words,
    special_word,
    tens_special,
    tens_words,
    thousand_words,
    units,
    word_multiplier,
)


class Numbers(object):
    """Class xữ lý chữ số đầu vào."""

    def __init__(self, words_number: list):
        """Khởi tạo instance của lớp Numbers.

        Args:
            words_number (list): Danh sách chữ số đầu vào.
        """
        self.words_number = words_number

    @property
    def get_keyword_index(self):
        """Lấy vị trí index của các từ khóa như mười, trăm, nghìn, triệu, tỷ.

        Returns:
            Trả về một dic gồm các keyword và vị trí index của nó.

        """
        keyword_index = {
            'tens_index': None,
            'hundreds_index': None,
            'thousand_index': None,
            'million_index': None,
            'billion_index': None,
            'special_index': None,
        }

        for word in self.words_number:
            if word in tens_words:
                keyword_index['tens_index'] = self.words_number.index(word)

            if word in hundreds_words:
                keyword_index['hundreds_index'] = self.words_number.index(word)

            if word in thousand_words:
                keyword_index['thousand_index'] = self.words_number.index(word)

            if word in million_words:
                keyword_index['million_index'] = self.words_number.index(word)

            if word in billion_words:
                keyword_index['billion_index'] = self.words_number.index(word)

            if word in special_word:
                keyword_index['special_index'] = self.words_number.index(word)

        return keyword_index


def convert_to_tens_word(words: list):
    """Chuyển các từ mười, chục thành ['một,'mươi']

    Returns:
        Danh sách mới sau khi chuyển đổi
    """
    # Chuyển các từ mười, chục thành ['một,'mươi']
    for word in words:
        if word in tens_special:
            tens_index = words.index(word)
            words[tens_index] = 'mươi'
            words.insert(tens_index, 'một')

    return words


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
    clean_numbers = []

    words = words.replace('-', ' ')  # replace ký tự đặt biệt "-" sang khoản trắng
    words = words.lower()  # converting chuổi đầu vào thành chuổi viết thường

    split_words = words.strip().split()  # xóa khoảng trắng thừa và chia câu thành các từ

    # xóa các từ không có trong unit va word_multiplier
    for word in split_words:
        if word in units or word in word_multiplier:
            clean_numbers.append(word)

    # Thông báo lỗi nếu người dùng nhập đầu vào không hợp lệ!
    if not clean_numbers:
        raise ValueError('không có chử số hợp lệ! vui lòng nhập chữ số hợp lệ.')

    # Chuyển các từ 'mười', 'chục' thành cụm ['một,'mươi']
    clean_numbers = convert_to_tens_word(clean_numbers)

    return clean_numbers
