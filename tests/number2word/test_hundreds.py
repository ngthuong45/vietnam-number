import pytest

from vietnam_number.number2word.data import ZeroWord
from vietnam_number.number2word.hundreds import n2w_hundreds


@pytest.mark.parametrize(
    "number_hundreds, zero_word, words_result",
    [
        ("1", ZeroWord.LE, "một"),
        ("1", ZeroWord.LINH, "một"),
        ("11", ZeroWord.LE, "mười một"),
        ("11", ZeroWord.LINH, "mười một"),
        ("111", ZeroWord.LE, "một trăm mười một"),
        ("111", ZeroWord.LINH, "một trăm mười một"),
        ("215", ZeroWord.LE, "hai trăm mười lăm"),
        ("215", ZeroWord.LINH, "hai trăm mười lăm"),
        ("221", ZeroWord.LE, "hai trăm hai mươi mốt"),
        ("221", ZeroWord.LINH, "hai trăm hai mươi mốt"),
        ("200", ZeroWord.LE, "hai trăm"),
        ("200", ZeroWord.LINH, "hai trăm"),
        ("101", ZeroWord.LE, "một trăm lẽ một"),
        ("101", ZeroWord.LINH, "một trăm linh một"),
        ("121", ZeroWord.LE, "một trăm hai mươi mốt"),
        ("121", ZeroWord.LINH, "một trăm hai mươi mốt"),
        ("815", ZeroWord.LE, "tám trăm mười lăm"),
        ("815", ZeroWord.LINH, "tám trăm mười lăm"),
        ("805", ZeroWord.LE, "tám trăm lẽ năm"),
        ("805", ZeroWord.LINH, "tám trăm linh năm"),
        ("825", ZeroWord.LE, "tám trăm hai mươi lăm"),
        ("825", ZeroWord.LINH, "tám trăm hai mươi lăm"),
    ],
)
def test_n2w_hundreds(number_hundreds, zero_word, words_result):
    """Kiểm tra xữ lý từng số.

    Args:
        number_hundreds (str): Chuỗi số đầu vào
        words_result (str): Chuỗi chữ số đầu ra

    """
    assert n2w_hundreds(number_hundreds, zero_word=zero_word) == words_result
