import pytest

from vietnam_number.number2word.hundreds import n2w_hundreds


@pytest.mark.parametrize(
    'number_hundreds, words_result',
    [
        ("1", "một"),
        ("11", "mười một"),
        ("111", "một trăm mười một"),
        ("215", "hai trăm mười lăm"),
        ("221", "hai trăm hai mươi mốt"),
        ("200", "hai trăm"),
        ("101", "một trăm lẽ một"),
        ("121", "một trăm hai mươi mốt"),
        ("815", "tám trăm mười lăm"),
        ("805", "tám trăm lẽ năm"),
        ("825", "tám trăm hai mươi lăm"),
    ],
)
def test_n2w_hundreds(number_hundreds, words_result):
    """Kiểm tra xữ lý từng số.

    Args:
        number_hundreds (str): Chuỗi số đầu vào
        words_result (str): Chuỗi chữ số đầu ra

    """
    assert n2w_hundreds(number_hundreds) == words_result
