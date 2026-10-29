import pytest

from vietnam_number.number2word import n2w_large_number
from vietnam_number.number2word.data import ZeroWord


@pytest.mark.parametrize(
    "number_large_number, zero_word, words_result",
    [
        # 1
        ("1", ZeroWord.LE, "một"),
        ("1", ZeroWord.LINH, "một"),
        # 12
        ("12", ZeroWord.LE, "mười hai"),
        ("12", ZeroWord.LINH, "mười hai"),
        # 123
        ("123", ZeroWord.LE, "một trăm hai mươi ba"),
        ("123", ZeroWord.LINH, "một trăm hai mươi ba"),
        # 1_234
        (str(1_234), ZeroWord.LE, "một nghìn hai trăm ba mươi bốn"),
        (str(1_234), ZeroWord.LINH, "một nghìn hai trăm ba mươi bốn"),
        # 12_345
        (str(12_345), ZeroWord.LE, "mười hai nghìn ba trăm bốn mươi lăm"),
        (str(12_345), ZeroWord.LINH, "mười hai nghìn ba trăm bốn mươi lăm"),
        # 1_234_567
        (
            str(1_234_567),
            ZeroWord.LE,
            "một triệu hai trăm ba mươi bốn nghìn năm trăm sáu mươi bảy",
        ),
        (
            str(1_234_567),
            ZeroWord.LINH,
            "một triệu hai trăm ba mươi bốn nghìn năm trăm sáu mươi bảy",
        ),
        # 12_345_678
        (
            str(12_345_678),
            ZeroWord.LE,
            "mười hai triệu ba trăm bốn mươi lăm nghìn sáu trăm bảy mươi tám",
        ),
        (
            str(12_345_678),
            ZeroWord.LINH,
            "mười hai triệu ba trăm bốn mươi lăm nghìn sáu trăm bảy mươi tám",
        ),
        # 123_456_789
        (
            str(123_456_789),
            ZeroWord.LE,
            "một trăm hai mươi ba triệu bốn trăm năm mươi sáu nghìn bảy trăm tám mươi chín",
        ),
        (
            str(123_456_789),
            ZeroWord.LINH,
            "một trăm hai mươi ba triệu bốn trăm năm mươi sáu nghìn bảy trăm tám mươi chín",
        ),
        # 1_234_567_890
        (
            str(1_234_567_890),
            ZeroWord.LE,
            "một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn tám trăm chín mươi",
        ),
        (
            str(1_234_567_890),
            ZeroWord.LINH,
            "một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn tám trăm chín mươi",
        ),
        # 115_205_201_211
        (
            str(115_205_201_211),
            ZeroWord.LE,
            "một trăm mười lăm tỷ hai trăm lẽ năm triệu hai trăm lẽ một nghìn hai trăm mười một",
        ),
        (
            str(115_205_201_211),
            ZeroWord.LINH,
            "một trăm mười lăm tỷ hai trăm linh năm triệu hai trăm linh một nghìn hai trăm mười một",
        ),
        # 1_000_000_000_000
        (str(1_000_000_000_000), ZeroWord.LE, "một nghìn tỷ"),
        (str(1_000_000_000_000), ZeroWord.LINH, "một nghìn tỷ"),
        # 1_000_000_000_000_000
        (
            str(1_000_000_000_000_000),
            ZeroWord.LE,
            "một triệu tỷ",
        ),
        (
            str(1_000_000_000_000_000),
            ZeroWord.LINH,
            "một triệu tỷ",
        ),  # 1_002_000_003
        (
            str(1_002_000_003),
            ZeroWord.LE,
            "một tỷ không trăm lẽ hai triệu không trăm lẽ ba",
        ),
        (
            str(1_002_000_003),
            ZeroWord.LINH,
            "một tỷ không trăm linh hai triệu không trăm linh ba",
        ),
        # 2_345_000_000_000
        (
            str(2_345_000_000_000),
            ZeroWord.LE,
            "hai nghìn tỷ ba trăm bốn mươi lăm tỷ",
        ),
        (
            str(2_345_000_000_000),
            ZeroWord.LINH,
            "hai nghìn tỷ ba trăm bốn mươi lăm tỷ",
        ),  # 123_000_000_000_000
        (
            str(123_000_000_000_000),
            ZeroWord.LE,
            "một trăm hai mươi ba nghìn tỷ",
        ),
        (
            str(123_000_000_000_000),
            ZeroWord.LINH,
            "một trăm hai mươi ba nghìn tỷ",
        ),  # 123_000_000_000_000_000
        (
            str(123_000_000_000_000_000),
            ZeroWord.LE,
            "một trăm hai mươi ba triệu tỷ",
        ),
        (
            str(123_000_000_000_000_000),
            ZeroWord.LINH,
            "một trăm hai mươi ba triệu tỷ",
        ),
        # 123_000_000_000_000_000_000
        (
            str(123_000_000_000_000_000_000),
            ZeroWord.LE,
            "một trăm hai mươi ba tỷ tỷ",
        ),
        (
            str(123_000_000_000_000_000_000),
            ZeroWord.LINH,
            "một trăm hai mươi ba tỷ tỷ",
        ),
        # 1_234_000_000_000_000_000_000
        (
            str(1_234_000_000_000_000_000_000),
            ZeroWord.LE,
            "một nghìn tỷ tỷ hai trăm ba mươi bốn tỷ tỷ",
        ),
        (
            str(1_234_000_000_000_000_000_000),
            ZeroWord.LINH,
            "một nghìn tỷ tỷ hai trăm ba mươi bốn tỷ tỷ",
        ),
        # 123_123_123_000_000
        (
            str(123_123_123_000_000),
            ZeroWord.LE,
            "một trăm hai mươi ba nghìn tỷ một trăm hai mươi ba tỷ một trăm hai mươi ba triệu",
        ),
        (
            str(123_123_123_000_000),
            ZeroWord.LINH,
            "một trăm hai mươi ba nghìn tỷ một trăm hai mươi ba tỷ một trăm hai mươi ba triệu",
        ),
        # 1_234_567_890_000_000
        (
            str(1_234_567_890_000_000),
            ZeroWord.LE,
            "một triệu tỷ hai trăm ba mươi bốn nghìn tỷ năm trăm sáu mươi bảy tỷ tám trăm chín mươi triệu",
        ),
        (
            str(1_234_567_890_000_000),
            ZeroWord.LINH,
            "một triệu tỷ hai trăm ba mươi bốn nghìn tỷ năm trăm sáu mươi bảy tỷ tám trăm chín mươi triệu",
        ),
    ],
)
def test_n2w_large_number(number_large_number, zero_word, words_result):
    """Kiểm tra xữ lý từng số.

    Args:
        number_large_number (str): Chuỗi số đầu vào
        words_result (str): Chuỗi chữ số đầu ra

    """
    assert n2w_large_number(number_large_number, zero_word=zero_word) == words_result
