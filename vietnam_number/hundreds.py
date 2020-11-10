from vietnam_number.data import hundreds_words, tens_words, tens_special
from vietnam_number.tens import process_tens
from vietnam_number.units import process_units


def process_hundreds(number_hundreds: list):
    # chuyển các từ mười, chục thành ['một,'mươi']
    for e in number_hundreds:
        if e in tens_special:
            m_index = number_hundreds.index(e)
            number_hundreds[m_index] = 'mươi'
            number_hundreds.insert(m_index, 'một')

    # báo lỗi nếu input có nhiều hơn 1 lần các từ trong hundreds_words và tens_words
    for e, i in zip(hundreds_words, tens_words):
        if number_hundreds.count(e) > 1 or number_hundreds.count(i) > 1:
            raise ValueError("Các từ liên kết hàng trăm và hàng chục có nhiều hơn một từ!")

    # nếu list truyền vào là rỗng thì bằng 00
    if len(number_hundreds) == 0:
        number_hundreds.append('không')

    # trường hợp trăm, mươi nằm ở đầu
    if number_hundreds[0] in hundreds_words \
            or number_hundreds[0] in tens_words:
        number_hundreds.insert(0, 'một')

    # trường hợp trăm, mươi nằm ở cuối
    if number_hundreds[len(number_hundreds) - 1] in hundreds_words \
            or number_hundreds[len(number_hundreds) - 1] in tens_words:
        number_hundreds.append('không')

    hundreds_index = -1
    tens_index = -1

    for e in number_hundreds:
        if e in tens_words:
            tens_index = number_hundreds.index(e)

        if e in hundreds_words:
            hundreds_index = number_hundreds.index(e)

    value_of_hundreds = []
    value_of_tens = []

    if hundreds_index > -1:
        value_of_hundreds = number_hundreds[:1]

        if tens_index > -1:
            value_of_tens = number_hundreds[hundreds_index + 1:]
        else:
            try:
                value_of_tens = number_hundreds[hundreds_index + 1:]
                if len(value_of_tens) == 1:
                    value_of_tens.append('không')
            except IndexError:
                value_of_tens = []
    else:
        if tens_index > -1:
            try:
                value_of_tens = number_hundreds[tens_index - 1: tens_index + 2]
            except IndexError:
                value_of_tens = number_hundreds[tens_index - 1:]

            rest_value = list(set(number_hundreds) - set(value_of_tens))

            if len(number_hundreds) <= 3:
                value_of_hundreds = ['không']
                value_of_tens = number_hundreds

            if len(number_hundreds) == 4:
                if tens_index == 1:
                    return process_tens(value_of_tens) + process_units(rest_value)
                if tens_index == 2:
                    return process_units(rest_value) + process_tens(value_of_tens)

        else:
            if len(number_hundreds) <= 2:
                value_of_hundreds = ['không']
                value_of_tens = number_hundreds

            if len(number_hundreds) == 3:
                value_of_hundreds = number_hundreds[:1]
                value_of_tens = number_hundreds[1:]

    return process_units(value_of_hundreds) + process_tens(value_of_tens)

