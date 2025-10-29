from vietnam_number.word2number.data import TENS_WORDS
from vietnam_number.word2number.utils.base import Numbers


class NumbersOfTens(Numbers):
    """Tiện ích cho xữ lý chữ số hàng chục."""

    @classmethod
    def format_words(cls, number_for_format: list):
        """Định dạng lại danh sách chữ số đầu vào.

        Định dạng lại danh sách chử số đầu vào cho các trường hợp đặc biệt.
        Thông thường là các trường hợp văn nói.

        Args:
            number_for_format (list): Danh sách chữ số đầu vào.

        Returns:
            Đối tượng NumbersOfTens với thuộc tính words_number đã được định dạng.

        """
        return cls(number_for_format)

    def validate(self):
        """Kiểm tra danh sách chữ số đầu vào đã hợp lệ.

        Raises:
            ValueError: Nếu danh sách chữ số đầu vào có nhiều hơn một từ dùng để kết nối hàng chục.
                vd: ba mươi chục tám, năm mươi mươi bảy

        """
        words_number_counter = self.words_number_counter
        for word in TENS_WORDS:
            if words_number_counter[word] > 1:
                raise ValueError(
                    f"Có nhiều hơn một từ {word} dùng để liên kết hàng chục!"
                )
