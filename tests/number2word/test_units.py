import pytest

from vietnam_number.number2word.units import n2w_units


@pytest.mark.parametrize(
    'number_units, words_result',
    [
        ('0', 'không'),
        ('1', 'một'),
        ('9', 'chín'),
    ],
)
def test_n2w_units(number_units, words_result):
    """Kiểm tra xữ lý từng số.

    Args:
        number_units (str): Chuỗi số đầu vào
        words_result (str): Chuỗi chữ số đầu ra

    """
    assert n2w_units(number_units) == words_result
