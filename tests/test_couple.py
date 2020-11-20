import pytest

from vietnam_number.word2number import w2n_couple
from vietnam_number.word2number.couple import process_couple


@pytest.mark.parametrize(
    'word_couple, number_result',
    [
        (['hai', 'mươi', 'ba', 'bảy', 'tám', 'mươi', 'tư'], '203784'),
        (['hai', 'mươi', 'ba', 'bảy', 'tám', 'mươi'], '203780'),
        (['năm', 'mươi', 'sáu', 'chín', 'hai', 'ba', 'mươi', 'lăm'], '569235'),
        (['năm', 'mươi', 'sáu', 'chín', 'hai', 'ba', 'mươi'], '569230'),
        (['năm', 'mươi', 'sáu', 'chín', 'hai', 'ba', 'mươi', 'lăm', 'bảy', 'tám'], '56923578'),
    ],
)
def test_process_couple(word_couple, number_result):
    """Kiểm tra xữ lý từng cặp số.
    Args:
        word_couple (list): Danh sách chữ số đầu vào hàng chục.
        number_result (str): Số đầu ra hàng chục.
    """
    assert process_couple(word_couple) == number_result


@pytest.mark.parametrize(
    'word_couple, number_result',
    [
        ('hai mươi ba bảy mười lăm', '203715'),
        ('năm mươi sáu chín hai mười sáu', '569216'),
        ('năm mươi sáu chín hai ba mươi lăm mười', '56923510'),
    ],
)
def test_w2n_couple(word_couple, number_result):
    """Kiểm tra xữ lý từng cặp số.
    Args:
        word_couple (str): Danh sách chữ số đầu vào hàng chục.
        number_result (str): Số đầu ra hàng chục.
    """
    assert w2n_couple(word_couple) == number_result
