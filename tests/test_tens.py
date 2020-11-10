import pytest
from vietnam_number.tens import process_tens


@pytest.mark.parametrize('word_tens, number_result',[
    ([], '00'),
    (['hai'], '02'),
    (['hai', 'sáu'], '26'),
    (['không'], '00'),
    (['mười'], '10'),
    (['mười', 'không'], '10'),
    (['mười', 'một'], '11'),
    (['mươi', 'bảy'], '17'),
    (['không', 'không'], '00'),
    (['không', 'ba'], '03'),
    (['năm', 'mươi'], '50'),
    (['hai', 'mươi', 'mốt'], '21'),
])
def test_process_tens(word_tens, number_result):
    assert process_tens(word_tens) == number_result
