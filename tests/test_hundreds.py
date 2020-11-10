import pytest
from vietnam_number.hundreds import process_hundreds


@pytest.mark.parametrize('word_hundreds, number_result', [
    ([], '000'),
    (['không'], '000'),
    (['trăm'], '100'),
    (['hai'], '002'),
    (['mười'], '010'),

    (['trăm', 'hai'], '120'),
    (['ba', 'trăm'], '300'),
    (['trăm', 'mười'], '110'),
    (['mười', 'lăm'], '015'),
    (['mươi', 'lăm'], '015'),
    (['không', 'ba'], '003'),
    (['hai', 'ba'], '023'),
    (['hai', 'mươi'], '020'),
    (['không', 'không'], '000'),
    (['không', 'mươi'], '000'),
    (['không', 'mười'], '010'),

    (['năm', 'mươi', 'hai'], '052'),
    (['năm', 'sáu', 'hai'], '562'),
    (['ba', 'mười', 'hai'], '312'),
    (['bốn', 'trăm', 'hai'], '420'),
    (['trăm', 'hai', 'ba'], '123'),
    (['trăm', 'mười', 'ba'], '113'),
    (['năm', 'mười', 'bảy'], '517'),
    (['bốn', 'tám', 'mươi'], '480'),

    (['bốn', 'trăm', 'hai', 'ba'], '423'),
    (['trăm', 'hai', 'mươi', 'ba'], '123'),
    (['hai', 'trăm', 'mười', 'ba'], '213'),
    (['không', 'trăm', 'tám', 'mươi'], '080'),
    (['không', 'bảy', 'mươi'], '070'),
    (['ba', 'bốn', 'mươi', 'hai'], '342'),
    (['ba', 'mươi', 'hai', 'bốn'], '324'),

    (['một', 'trăm', 'ba', 'mươi', 'hai'], '132'),
])
def test_process_hundreds(word_hundreds, number_result):
    assert process_hundreds(word_hundreds) == number_result
