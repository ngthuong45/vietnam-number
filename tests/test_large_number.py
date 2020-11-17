import pytest

from vietnam_number.large_number import process_w2n


@pytest.mark.parametrize(
    'word_number, number_result',
    [
        ([], '000000000000'),
        (['một', 'triệu', 'bốn', 'nghìn', 'ba', 'mươi', 'hai'], '000001004032'),
        (['một', 'trăm', 'hai', 'triệu', 'bốn', 'nghìn', 'ba', 'mươi', 'hai'], '000120004032'),
        (['bốn', 'nghìn', 'ba', 'mươi', 'hai'], '000000004032'),
        (['bốn', 'mười', 'ba', 'tỷ', 'triệu', 'hai'], '413001200000'),
        (['bốn', 'mười', 'ba', 'tỷ', 'triệu'], '413001000000'),
        (['bốn', 'mười', 'ba', 'tỷ', 'triệu', 'nghìn'], '413001001000'),
        (['triệu', 'nghìn'], '000001001000'),
        (['trăm', 'nghìn', 'hai', 'mười', 'ba'], '000000100213'),
        (['hai', 'nghìn', 'hai', 'mười', 'ba'], '000000002213'),
        (['mười', 'nghìn', 'hai', 'mười', 'ba'], '000000010213'),
        (['hai', 'mươi'], '000000000020'),
        (['bốn', 'hai', 'mươi', 'ba'], '000000000423'),
        (['một', 'triệu', 'hai', 'trăm', 'nghìn', 'ba', 'trăm'], '000001200300'),
        (['một'], '000000000001'),
        (['tỷ'], '001000000000'),
        (['hai', 'nghìn'], '000000002000'),
        (['mười'], '000000000010'),
        (['mười', 'không'], '000000000010'),
        (['mười', 'một'], '000000000011'),
    ],
)
def test_process_w2n(word_number, number_result):
    """Kiểm tra xữ lý chữ số lớn hơn hàng trăm.

    Args:
        word_number (list): Danh sách chữ số đầu vào.
        number_result (str): Số đầu ra.

    """
    assert process_w2n(word_number) == number_result
