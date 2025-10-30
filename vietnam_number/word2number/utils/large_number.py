from vietnam_number.word2number.data import (
    BILLION_MILLION_THOUSAND_WORDS,
    BILLION_WORDS,
    MILLION_WORDS,
    THOUSAND_WORDS,
    UNITS,
)
from vietnam_number.word2number.utils.base import Numbers


class LargeNumber(Numbers):
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
        # Trường hợp văn nói "một triệu hai", "tỷ ba"
        if len(number_for_format) > 1 and number_for_format[-1] in UNITS:
            second_last_word = number_for_format[-2]

            if second_last_word not in BILLION_MILLION_THOUSAND_WORDS:
                pass

            elif second_last_word in BILLION_WORDS:
                number_for_format.append('trăm')
                number_for_format.append('triệu')

            elif second_last_word in MILLION_WORDS:
                number_for_format.append('trăm')
                number_for_format.append('nghìn')

            elif second_last_word in THOUSAND_WORDS:
                number_for_format.append('trăm')

        return cls(number_for_format)

    def validate(
        self,
        billion_million_thousand_words: frozenset[str] = BILLION_MILLION_THOUSAND_WORDS,
    ):
        """Kiểm tra tính hợp lệ của danh sách chữ số đầu vào.

        Raises:
            ValueError: Nếu danh sách chữ số đầu váo có nhiều hợn 1 từ thuộc các từ trong
                BILLION_MILLION_THOUSAND_WORDS thì báo lỗi.
                vd: bốn trăm trăm bảy mươi hai, bốn trăm bảy mươi mươi hai

        """
        # Lỗi nếu người dùng nhập hai lần chữ triệu, tỷ, nghìn
        for word, count in self.words_number_counter.items():
            if count > 1 and word in billion_million_thousand_words:
                raise ValueError(
                    f"Chữ số {word} nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ."
                )
