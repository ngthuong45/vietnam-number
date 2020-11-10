from vietnam_number.data import tens_words, units_words, tens_special
from vietnam_number.units import process_units


def process_tens(number_tens: list):
    # chuyển các từ mười, chục thành ['một,'mươi']
    for e in number_tens:
        if e in tens_special:
            m_index = number_tens.index(e)
            number_tens[m_index] = 'mươi'
            number_tens.insert(m_index, 'một')

    # nếu list truyền vào là rỗng thì bằng 00
    if len(number_tens) == 0:
        number_tens.append('không')

    # nếu truyền vào 1 ký tự và thuộc vietnam_number thì thêm không
    if len(number_tens) == 1 and number_tens[0] in units_words:
        number_tens.insert(0, 'không')

    tens_index = -1

    for e in number_tens:
        if e in tens_words:
            tens_index = number_tens.index(e)

    value_of_tens = ''
    value_of_units = ''

    if tens_index > -1:
        if tens_index == 0:
            value_of_tens = 'một'
            try:
                value_of_units = number_tens[1]
            except IndexError:
                value_of_units = 'không'
        elif tens_index == 1:
            value_of_tens = number_tens[0]
            try:
                value_of_units = number_tens[2]
            except IndexError:
                value_of_units = 'không'
    else:
        value_of_tens = number_tens[0]
        value_of_units = number_tens[1]

    return process_units([value_of_tens]) + process_units([value_of_units])
