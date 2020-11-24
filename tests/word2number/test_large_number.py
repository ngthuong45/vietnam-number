import pytest

from vietnam_number.word2number import w2n
from vietnam_number.word2number.large_number import process_large_number


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


@pytest.mark.parametrize(
    'word_number, number_result',
    [
        ([], 0),
        (['một', 'triệu', 'bốn', 'nghìn', 'ba', 'mươi', 'hai'], 1004032),
        (['một', 'trăm', 'hai', 'triệu', 'bốn', 'nghìn', 'ba', 'mươi', 'hai'], 120004032),
        (['bốn', 'nghìn', 'ba', 'mươi', 'hai'], 4032),
        (['triệu', 'nghìn'], 1001000),
        (['hai', 'mươi'], 20),
        (['bốn', 'hai', 'mươi', 'ba'], 423),
        (['một', 'triệu', 'hai', 'trăm', 'nghìn', 'ba', 'trăm'], 1200300),
        (['một'], 1),
        (['tỷ'], 1000000000),
        (['hai', 'nghìn'], 2000),
        (
            ['tỷ', 'hai', 'trăm', 'lẽ', 'ba', 'triệu', 'sáu', 'trăm', 'ba', 'mươi', 'hai', 'nghìn', 'lẽ', 'bốn', 'trăm'],
            1203632400,
        ),
        (['tỷ', 'lẽ', 'hai', 'triệu'], 1002000000),
        (['tỷ', 'rưỡi', 'lẽ', 'chín', 'trăm', 'nghìn'], 1500900000),
        (['triệu', 'rưỡi', 'lẽ', 'chín', 'mươi', 'nghìn'], 1590000),
        (['tỷ', 'lẽ', 'ba', 'mươi', 'hai', 'triệu'], 1032000000),
        (['hai', 'triệu', 'lẽ', 'ba', 'nghìn', 'hai', 'trăm', 'lẽ', 'tám'], 2003208),
        (
            ['tỷ', 'lẽ', 'tám', 'trăm', 'năm', 'mươi', 'hai', 'triệu', 'sáu', 'trăm', 'lẽ', 'ba', 'nghìn', 'hai', 'trăm'],
            1852603200,
        ),
    ],
)
def test_process_large_number(word_number, number_result):
    """Kiểm tra xữ lý chữ số lớn hơn hàng trăm.

    Args:
        word_number (list): Danh sách chữ số đầu vào.
        number_result (str): Số đầu ra.

    """
    assert process_large_number(word_number) == number_result
