import pytest

from vietnam_number.word2number import w2n
from vietnam_number.word2number.large_number import process_w2n


@pytest.mark.parametrize(
    'word_number, number_result',
    [
        ([], '000000000000'),
        (['một', 'triệu', 'bốn', 'nghìn', 'ba', 'mươi', 'hai'], '000001004032'),
        (['một', 'trăm', 'hai', 'triệu', 'bốn', 'nghìn', 'ba', 'mươi', 'hai'], '000120004032'),
        (['bốn', 'nghìn', 'ba', 'mươi', 'hai'], '000000004032'),
        (['triệu', 'nghìn'], '000001001000'),
        (['hai', 'mươi'], '000000000020'),
        (['bốn', 'hai', 'mươi', 'ba'], '000000000423'),
        (['một', 'triệu', 'hai', 'trăm', 'nghìn', 'ba', 'trăm'], '000001200300'),
        (['một'], '000000000001'),
        (['tỷ'], '001000000000'),
        (['hai', 'nghìn'], '000000002000'),
    ],
)
def test_process_w2n(word_number, number_result):
    """Kiểm tra xữ lý chữ số lớn hơn hàng trăm.

    Args:
        word_number (list): Danh sách chữ số đầu vào.
        number_result (str): Số đầu ra.

    """
    assert process_w2n(word_number) == number_result


@pytest.mark.parametrize(
    'word_number, number_result',
    [
        ('bốn mười ba tỷ triệu hai', 413001200000),
        ('bốn mười ba tỷ triệu', 413001000000),
        ('bốn mười ba tỷ triệu nghìn', 413001001000),
        ('trăm nghìn hai mười ba', 100213),
        ('hai nghìn hai mười ba', 2213),
        ('mười nghìn hai mười ba', 10213),
        ('mười', 10),
        ('mười không', 10),
        ('mười một', 11),
    ],
)
def test_w2n_large_number(word_number, number_result):
    """Kiểm tra xữ lý chữ số lớn hơn hàng trăm.

    Args:
        word_number (str): Danh sách chữ số đầu vào.
        number_result (int): Số đầu ra.

    """
    assert w2n(word_number) == number_result
