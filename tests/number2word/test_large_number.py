import pytest

from vietnam_number.number2word import n2w_large_number


@pytest.mark.parametrize(
    'number_large_number, words_result',
    [
        ('115205201211', 'một trăm mười lăm tỷ hai trăm lẽ năm triệu hai trăm lẽ một nghìn hai trăm mười một'),
    ],
)
def test_n2w_large_number(number_large_number, words_result):
    """Kiểm tra xữ lý từng số.

    Args:
        number_large_number (str): Chuỗi số đầu vào
        words_result (str): Chuỗi chữ số đầu ra

    """
    assert n2w_large_number(number_large_number) == words_result
