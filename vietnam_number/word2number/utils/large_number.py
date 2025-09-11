from vietnam_number.word2number.data import (
    BILLION_MILLION_THOUSAND_WORDS,
    billion_words,
    million_words,
    thousand_words,
    units,
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
        # Nếu list truyền vào là rỗng thì bằng 000000
        if not number_for_format:
            number_for_format.append("không")
            number_for_format.append("không")
            return cls(number_for_format)

        # Nếu danh sách chữ số truyền vào có 1 chữ số thuộc hàng đơn vị
        # thì thêm 'không' vào đầu của list
        # vd: ['hai'] => ['không', 'hai']
        elif len(number_for_format) == 1 and number_for_format[0] in units:
            number_for_format.insert(0, 'không')
            return cls(number_for_format)

        # Trường hợp nghìn, triệu, tỷ nằm ở đầu
        elif number_for_format[0] in BILLION_MILLION_THOUSAND_WORDS:
            number_for_format.insert(0, 'một')

        # Trường hợp văn nói "một triệu hai", "tỷ ba"
        if number_for_format[-1] in units:
            second_last_word = number_for_format[-2]

            if second_last_word in billion_words:
                number_for_format.append('trăm')
                number_for_format.append('triệu')

            elif second_last_word in million_words:
                number_for_format.append('trăm')
                number_for_format.append('nghìn')

            elif second_last_word in thousand_words:
                number_for_format.append('trăm')

        return cls(number_for_format)

    def validate(self):
        """Kiểm tra tính hợp lệ của danh sách chữ số đầu vào.

        Raises:
            ValueError: Nếu danh sách chữ số đầu váo có nhiều hợn 1 từ thuộc các từ trong
                hundreds_words và tens_words thì báo lỗi.
                vd: bốn trăm trăm bảy mươi hai, bốn trăm bảy mươi mươi hai

        """
        # Lỗi nếu người dùng nhập hai lần chữ triệu, tỷ, nghìn
        words_number_counter = self.words_number_counter
        for word in BILLION_MILLION_THOUSAND_WORDS:
            if words_number_counter[word] > 1:
                raise ValueError(
                    f"Chữ số {word} nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ."
                )