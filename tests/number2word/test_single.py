import pytest

from vietnam_number import n2w_single


@pytest.mark.parametrize(
    'number_single, words_result',
    [
        ('0908123456', 'không chín không tám một hai ba bốn năm sáu'),
        ('+84908123456', 'không chín không tám một hai ba bốn năm sáu'),
    ],
)
def test_n2w_single(number_single, words_result):
    """Kiểm tra xữ lý từng số.

    Args:
        number_single (str): Chuỗi số đầu vào
        words_result (str): Chuỗi chữ số đầu ra

    """
    assert n2w_single(number_single) == words_result
