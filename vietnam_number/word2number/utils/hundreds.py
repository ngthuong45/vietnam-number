from vietnam_number.word2number.data import hundreds_words, tens_words
from vietnam_number.word2number.utils.base import Numbers


class NumbersOfHundreds(Numbers):
    """Tiện ích cho xữ lý chữ số hàng trăm."""

    @classmethod
    def format_words(cls, number_for_format: list):
        """Định dạng lại danh sách chữ số đầu vào.

        Giúp định dạng lại danh sách chữ số đầu vào cho một số trường hợp đặc biệt.
        Thường được sử dụng nhiều trong văn nói.

        Args:
            number_for_format (list): Danh sách chữ số đầu vào

        Returns:
            Trả về một instance NumbersOfHundreds với thuộc tính kế thừa từ lớp cha (words_number)
            đã được định dạng lại.

        """
        # Trường hợp đầu vào là rỗng thì đầu ra là 000
        if not number_for_format:
            number_for_format.append('không')

        # Trường hợp trăm, mươi nằm ở đầu
        first_number = number_for_format[0]
        if first_number in hundreds_words or first_number in tens_words:
            number_for_format.insert(0, 'một')

        # Trường hợp trăm, mươi nằm ở cuối
        last_number = number_for_format[-1]
        if last_number in hundreds_words or last_number in tens_words:
            number_for_format.append('không')

        return cls(number_for_format)

    def validate(self):
        """Kiểm tra tính hợp lệ của danh sách chữ số đầu vào.

        Raises:
            ValueError: Nếu danh sách chữ số đầu váo có nhiều hợn 1 từ thuộc các từ trong
                hundreds_words và tens_words thì báo lỗi.
                vd: bốn trăm trăm bảy mươi hai, bốn trăm bảy mươi mươi hai

        """
        for hundreds, tens in zip(hundreds_words, tens_words):

            if self.words_number.count(hundreds) > 1:
                raise ValueError('Chữ số hàng trăm nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ.')

            if self.words_number.count(tens) > 1:
                raise ValueError('Chữ số hàng mười nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ.')
