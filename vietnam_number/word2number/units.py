from vietnam_number.word2number.data import units


def process_units(words: list):
    """Xữ lý chữ số hàng đơn vị.

    Args:
        words (list): Danh sách chữ số đầu vào.

    Returns:
        Chuổi số hàng đơn vị.

    Raises:
        ValueError: Danh sách chữ số đầu vào lớn hơn 1.

    """
    # nếu list truyền vào là rỗng thì bằng 0
    # Optimal order: highest frequency first
    if len(words) == 1:
        pass
    elif not words:
        words.append('không')
    else:
        raise ValueError('chữ số vượt quá hàng đơn vị')

    return str(units[words[0]])
