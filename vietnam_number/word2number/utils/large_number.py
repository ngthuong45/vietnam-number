from vietnam_number.word2number.data import billion_words, million_words, thousand_words, units
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
            number_for_format.append('không')

        # Nếu danh sách chữ số truyền vào có 1 chữ số thuộc hàng đơn vị
        # thì thêm 'không' vào đầu của list
        # vd: ['hai'] => ['không', 'hai']
        if len(number_for_format) == 1 and number_for_format[0] in units:
            number_for_format.insert(0, 'không')

        # Trường hợp nghìn, triệu, tỷ nằm ở đầu
        first_number = number_for_format[0]
        if first_number in thousand_words or first_number in million_words or first_number in billion_words:
            number_for_format.insert(0, 'một')

        # Trường hợp văn nói "một triệu hai", "tỷ ba"
        if number_for_format[-2] in billion_words:
            if number_for_format[-1] in units:
                number_for_format.append('trăm')
                number_for_format.append('triệu')

        if number_for_format[-2] in million_words:
            if number_for_format[-1] in units:
                number_for_format.append('trăm')
                number_for_format.append('nghìn')

        if number_for_format[-2] in thousand_words:
            if number_for_format[-1] in units:
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
        for thousand, million, billion in zip(thousand_words, million_words, billion_words):

            if self.words_number.count(thousand) > 1:
                raise ValueError('Chữ số hàng nghìn nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ.')

            if self.words_number.count(million) > 1:
                raise ValueError('Chữ số hàng triệu nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ.')

            if self.words_number.count(billion) > 1:
                raise ValueError('Chữ số hàng tỷ nhiều hơn 1 từ. Vui lòng nhập chữ số hợp lệ.')
