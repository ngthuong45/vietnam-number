import pytest
from vietnam_number.units import process_units


@pytest.mark.parametrize('word_units, number_result', [
    ([], '0'),
    (['không'], '0'),
    (['lẽ'], '0'),
    (['lăm'], '5'),
    (['tư'], '4'),
    (['mốt'], '1')
])
def test_process_units(word_units, number_result):
    assert process_units(word_units) == number_result
