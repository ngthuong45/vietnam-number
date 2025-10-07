from vietnam_number.word2number.data import UNITS


def process_units(words: str) -> str:
    """Xữ lý chữ số hàng đơn vị.

    Args:
        words (str): Danh sách chữ số đầu vào.

    Returns:
        Chuổi số hàng đơn vị.

    """
    # nếu str truyền vào là rỗng thì bằng "0"
    return UNITS.get(words, "0")
