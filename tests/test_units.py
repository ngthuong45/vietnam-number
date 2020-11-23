import pytest

from vietnam_number.word2number import w2n
from vietnam_number.word2number.units import process_units


@pytest.mark.parametrize(
    'word_units, number_result',
    [
        ('không', 0),
        ('lẽ', 0),
        ('lăm', 5),
        ('tư', 4),
        ('mốt', 1),
    ],
)
def test_w2n_units(word_units, number_result):
    """Kiểm tra xữ lý chữ số hàng đơn vị.

    Args:
        word_units (str): Danh sách chử số đầu vào.
        number_result (int): Số đầu ra hàng đơn vị

    """
    assert w2n(word_units) == number_result


@pytest.mark.parametrize(
    'word_units, number_result',
    [
        ([], '0'),
        (['không'], '0'),
        (['lẽ'], '0'),
        (['lăm'], '5'),
        (['tư'], '4'),
        (['mốt'], '1'),
    ],
)
def test_process_units(word_units, number_result):
    """Kiểm tra xữ lý chữ số hàng đơn vị.

    Args:
        word_units (list): Danh sách chử số đầu vào.
        number_result (str): Số đầu ra hàng đơn vị

    """
    assert process_units(word_units) == number_result
