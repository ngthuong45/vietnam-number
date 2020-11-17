from vietnam_number.data import billion_words, hundreds_words, million_words, tens_words, thousand_words


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

        return keyword_index
