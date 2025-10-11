import pytest

from vietnam_number.number2word import n2w_large_number


@pytest.mark.parametrize(
    "number_large_number, words_result",
    [
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
