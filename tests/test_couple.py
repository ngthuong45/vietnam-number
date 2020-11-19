import pytest

from vietnam_number.w2n.couple import process_couple


@pytest.mark.parametrize(
    'word_couple, number_result',
    [
        (
            [
                'hai',
                'mươi',
                'ba',
                'bảy',
                'tám',
                'mươi',
                'bốn',
                'năm',
                'bốn',
                'chín',
                'mươi',
                'mốt',
                'mười',
                'hai',
                'bảy',
                'năm',
            ],
            '20378454911275',
        ),
    ],
)
def test_process_couple(word_couple, number_result):
    """Kiểm tra xữ lý từng cặp số.

    Args:
        word_couple (list): Danh sách chữ số đầu vào hàng chục.
        number_result (str): Số đầu ra hàng chục.

    """
    assert process_couple(word_couple) == number_result
