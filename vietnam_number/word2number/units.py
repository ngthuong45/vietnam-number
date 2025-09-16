from collections.abc import Sequence

from vietnam_number.word2number.data import UNITS


def process_units(words: Sequence[str]) -> str:
    """Xữ lý chữ số hàng đơn vị.

    Args:
        words (Sequence[str]): Danh sách chữ số đầu vào.

    Returns:
        Chuổi số hàng đơn vị.

    Raises:
        ValueError: Danh sách chữ số đầu vào lớn hơn 1.

    """
    # nếu list truyền vào là rỗng thì bằng 0
    # Optimal order: highest frequency first
    if len(words) == 1:
        return str(UNITS[words[0]])
    elif not words:
        return "0"
    else:
        raise ValueError('chữ số vượt quá hàng đơn vị')
