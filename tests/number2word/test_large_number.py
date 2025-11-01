import pytest

from vietnam_number.number2word import n2w_large_number


@pytest.mark.parametrize(
    "number_large_number, words_result",
    [
        ("1", "một"),
        ("12", "mười hai"),
        ("123", "một trăm hai mươi ba"),
        (str(1_234), "một nghìn hai trăm ba mươi bốn"),
        (str(12_345), "mười hai nghìn ba trăm bốn mươi lăm"),
        (str(1_234_567), "một triệu hai trăm ba mươi bốn nghìn năm trăm sáu mươi bảy"),
        (
            str(12_345_678),
            "mười hai triệu ba trăm bốn mươi lăm nghìn sáu trăm bảy mươi tám",
        ),
        (
            str(123_456_789),
            "một trăm hai mươi ba triệu bốn trăm năm mươi sáu nghìn bảy trăm tám mươi chín",
        ),
        (
            str(1_234_567_890),
            "một tỷ hai trăm ba mươi bốn triệu năm trăm sáu mươi bảy nghìn tám trăm chín mươi",
        ),
        (
            "115205201211",
            "một trăm mười lăm tỷ hai trăm lẽ năm triệu hai trăm lẽ một nghìn hai trăm mười một",
        ),
        ("1000000000000", "một nghìn tỷ"),
        ("1000000000000000", "một triệu tỷ"),
        ("1002000003", "một tỷ không trăm lẽ hai triệu không trăm lẽ ba"),
        ("2345000000000", "hai nghìn tỷ ba trăm bốn mươi lăm tỷ"),
        (str(123_000_000_000_000), "một trăm hai mươi ba nghìn tỷ"),
        (str(123_000_000_000_000_000), "một trăm hai mươi ba triệu tỷ"),
        (str(123_000_000_000_000_000_000), "một trăm hai mươi ba tỷ tỷ"),
        (
            str(1_234_000_000_000_000_000_000),
            "một nghìn tỷ tỷ hai trăm ba mươi bốn tỷ tỷ",
        ),
        (
            str(123_123_123_000_000),
            "một trăm hai mươi ba nghìn tỷ một trăm hai mươi ba tỷ một trăm hai mươi ba triệu",
        ),
        (
            str(1_234_567_890_000_000),
            "một triệu tỷ hai trăm ba mươi bốn nghìn tỷ năm trăm sáu mươi bảy tỷ tám trăm chín mươi triệu",
        ),
    ],
)
def test_n2w_large_number(number_large_number, words_result):
    """Kiểm tra xữ lý từng số.

    Args:
        number_large_number (str): Chuỗi số đầu vào
        words_result (str): Chuỗi chữ số đầu ra

    """
    assert n2w_large_number(number_large_number) == words_result
