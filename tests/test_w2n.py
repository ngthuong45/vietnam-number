import pytest
from vietnam_number.w2n import process_w2n


@pytest.mark.parametrize('word_number, number_result', [
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
])
def test_process_w2n(word_number, number_result):
    assert process_w2n(word_number) == number_result
