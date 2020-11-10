from vietnam_number.data import units_words


def process_units(number_units: list):
    # nếu list truyền vào là rỗng thì bằng 0
    if len(number_units) == 0:
        number_units.append('không')

    if len(number_units) > 1:
        raise KeyError('chữ số vượt quá hàng đơn vị')

    return str(units_words[number_units[0]])
