import pytest

from vietnam_number.word2number import w2n
from vietnam_number.word2number.tens import process_tens


@pytest.mark.parametrize(
    'word_tens, number_result',
    [
        ('mười', 10),
        ('mười không', 10),
        ('mười một', 11),
    ],
)
def test_w2n_tens(word_tens, number_result):
    """Kiểm tra xữ lý chữ số hàng chục.

    Args:
        word_tens (str): Danh sách chữ số đầu vào hàng chục.
        number_result (int): Số đầu ra hàng chục.

    """
    assert w2n(word_tens) == number_result


@pytest.mark.parametrize(
    'word_tens, number_result',
    [
        ([], '00'),
        (['hai'], '02'),
        (['hai', 'sáu'], '26'),
        (['không'], '00'),
        (['mươi', 'bảy'], '17'),
        (['không', 'không'], '00'),
        (['không', 'ba'], '03'),
        (['năm', 'mươi'], '50'),
        (['hai', 'mươi', 'mốt'], '21'),
    ],
)
def test_process_tens(word_tens, number_result):
    """Kiểm tra xữ lý chữ số hàng chục.

    Args:
        word_tens (list): Danh sách chữ số đầu vào hàng chục.
        number_result (str): Số đầu ra hàng chục.

    """
    assert process_tens(word_tens) == number_result
