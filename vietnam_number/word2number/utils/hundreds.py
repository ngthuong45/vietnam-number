from vietnam_number.word2number.data import HUNDREDS_TENS_WORDS
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
        return cls(number_for_format)

    def validate(
        self,
        hundreds_tens_words: frozenset[str] = HUNDREDS_TENS_WORDS,
    ):
        """Kiểm tra tính hợp lệ của danh sách chữ số đầu vào.

        Raises:
            ValueError: Nếu danh sách chữ số đầu váo có nhiều hợn 1 từ thuộc các từ trong
                HUNDREDS_TENS_WORDS thì báo lỗi.
                vd: bốn trăm trăm bảy mươi hai, bốn trăm bảy mươi mươi hai

        """
        for word, count in self.words_number_counter.items():
            if count > 1 and word in hundreds_tens_words:
                raise ValueError(
                    f"Chữ số {word} nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ."
                )
