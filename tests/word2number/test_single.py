import pytest

from vietnam_number.word2number import w2n_single
from vietnam_number.word2number.single import process_single


@pytest.mark.parametrize(
    'word_single, number_result',
    [
        (['không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín'], '0123456789'),
    ],
)
def test_process_single(word_single, number_result):
    """Kiểm tra xữ lý từng số.

    Args:
        word_single (list): Danh sách chữ số đầu vào.
        number_result (str): Số đầu ra hàng chục.

    """
    assert process_single(word_single) == number_result


@pytest.mark.parametrize(
    'word_single, number_result',
    [
        ('không một hai ba bốn năm sáu bảy tám chín', '0123456789'),
    ],
)
def test_w2n_single(word_single, number_result):
    """Kiểm tra xữ lý từng số.

    Args:
        word_single (str): Danh sách chữ số đầu vào.
        number_result (str): Số đầu ra hàng chục.

    """
    assert w2n_single(word_single) == number_result
