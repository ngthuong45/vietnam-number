from vietnam_number.data import million_words, units_words, thousand_words, billion_words, tens_special
from vietnam_number.hundreds import process_hundreds


def process_w2n(word_number: list):
    # Lỗi nếu người dùng nhập hai lần chữ triệu, tỷ, nghìn
    for x, y, z in zip(thousand_words, million_words, billion_words):
        if word_number.count(x) > 1 or word_number.count(y) > 1 or word_number.count(z) > 1:
            raise ValueError('Chữ số bị dư! vui lòng nhập chữ số hợp lệ (eg. bốn trăm năm mươi nghìn)')

    # chuyển các từ mười, chục thành ['một,'mươi']
    for e in word_number:
        if e in tens_special:
            m_index = word_number.index(e)
            word_number[m_index] = 'mươi'
            word_number.insert(m_index, 'một')

    # nếu list truyền vào là rỗng thì bằng 0
    if len(word_number) == 0:
        word_number.append('không')

    # trường hợp văn nói "một triệu hai", "tỷ ba"
    if word_number[len(word_number) - 2] in billion_words:
        if word_number[len(word_number) - 1] in units_words:
            word_number.append('trăm')
            word_number.append('triệu')

    if word_number[len(word_number) - 2] in million_words:
        if word_number[len(word_number) - 1] in units_words:
            word_number.append('trăm')
            word_number.append('nghìn')

    if word_number[len(word_number) - 2] in thousand_words:
        if word_number[len(word_number) - 1] in units_words:
            word_number.append('trăm')

    billion_index = -1
    million_index = -1
    thousand_index = -1

    for e in word_number:
        if e in thousand_words:
            thousand_index = word_number.index(e)

        if e in million_words:
            million_index = word_number.index(e)

        if e in billion_words:
            billion_index = word_number.index(e)

    value_of_billion = []
    value_of_million = []
    value_of_thousand = []
    value_of_hundreds = []

    if billion_index > -1:
        value_of_billion = word_number[:billion_index]

        if not value_of_billion:
            value_of_billion = ['một']

    if million_index > -1:
        if billion_index > -1:
            value_of_million = word_number[billion_index + 1:million_index]
        else:
            value_of_million = word_number[:million_index]

        if not value_of_million:
            value_of_million = ['một']

    if thousand_index > -1:
        if million_index > -1:
            value_of_thousand = word_number[million_index + 1:thousand_index]
        elif billion_index > -1:
            value_of_thousand = word_number[billion_index + 1:thousand_index]
        else:
            value_of_thousand = word_number[:thousand_index]

        if not value_of_thousand:
            value_of_thousand = ['một']

    if thousand_index > -1:
        value_of_hundreds = word_number[thousand_index + 1:]
    elif million_index > -1:
        value_of_hundreds = word_number[million_index + 1:]
    elif billion_index > -1:
        value_of_hundreds = word_number[billion_index + 1:]
    elif thousand_index == -1 and million_index == -1 and billion_index == -1:
        value_of_hundreds = word_number

    return process_hundreds(value_of_billion) + process_hundreds(value_of_million) + process_hundreds(
        value_of_thousand) + process_hundreds(value_of_hundreds)
