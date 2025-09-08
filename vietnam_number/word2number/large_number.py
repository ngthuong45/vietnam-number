from itertools import groupby

from vietnam_number.word2number.data import hundreds_words, special_word
from vietnam_number.word2number.hundreds import process_hundreds
from vietnam_number.word2number.utils.large_number import LargeNumber


def pre_process_large_number(words: list) -> LargeNumber:
    """Tiền xữ lý danh sách chữ số đầu vào.

    Giúp tiền xữ lý dữ liệu đầu vào bao gồm như định dang lại danh sách, kiểm tra tính hợp lệ
    của danh sách...

    Args:
        words (list): Danh dách chữ số dùng để tiền xữ lý.

    Returns:
        Trả về một instance sau khi đã được xữ lý
        Nếu có lỗi sẽ trả về lỗi.

    """
    large_number = LargeNumber.format_words(words)

    # Kiểm tra tính hợp lệ của danh sách chữ số.
    large_number.validate()

    return large_number


def process_large_number_normal(words: list):
    """Xữ lý chử số lớn.

    Hàm xữ lý chuyển đổi dành cho trường hợp các chữ số lớn hơn
    hàng trăm. Bao gồm các số hàng nghìn, triệu, tỷ

    Args:
        words (list): Danh sách chữ số đầu vào.

    Returns:
        Chuổi số lớn

    """
    # Tiền xữ lý danh sách chữ số đầu vào.
    large_number = pre_process_large_number(words)

    # Xữ lý chữ số hàng trăm.
    clean_words_number = large_number.words_number

    value_of_billion = []
    value_of_million = []
    value_of_thousand = []

    # Lấy vị trí index của từ khóa hàng chục
    billion_index = large_number.get_keyword_index['billion_index']
    million_index = large_number.get_keyword_index['million_index']
    thousand_index = large_number.get_keyword_index['thousand_index']

    if billion_index:
        value_of_billion = clean_words_number[:billion_index]

    if million_index:
        if billion_index:
            value_of_million = clean_words_number[billion_index + 1 : million_index]
        else:
            value_of_million = clean_words_number[:million_index]

        if not value_of_million:
            value_of_million = ['một']

    if thousand_index:
        if million_index:
            value_of_thousand = clean_words_number[million_index + 1 : thousand_index]
        elif billion_index:
            value_of_thousand = clean_words_number[billion_index + 1 : thousand_index]
        else:
            value_of_thousand = clean_words_number[:thousand_index]

        if not value_of_thousand:
            value_of_thousand = ['một']

    if thousand_index:
        value_of_hundreds = clean_words_number[thousand_index + 1 :]
    elif million_index:
        value_of_hundreds = clean_words_number[million_index + 1 :]
    elif billion_index:
        value_of_hundreds = clean_words_number[billion_index + 1 :]
    else:
        value_of_hundreds = clean_words_number

    total_number = (
        process_hundreds(value_of_billion)
        + process_hundreds(value_of_million)
        + process_hundreds(value_of_thousand)
        + process_hundreds(value_of_hundreds)
    )

    return int(total_number)


def process_large_number_special(words: list):
    #   Create sublists of consecutive words that are NOT in `special_word`.
    #   The special word(s) act as split points and are NOT included in the output.
    #
    #   Example:
    #   Input:  ['một', 'trăm', 'lẻ', 'ba'], special_word = {'lẻ'}
    #   Output: [['một', 'trăm'], ['ba']]
    total_number = 0

    for is_special_word, word_group in groupby(
        words, key=lambda word: word in special_word
    ):
        if not is_special_word:
            total_number += int(process_large_number_normal(list(word_group)))

    return total_number


def process_large_number(words: list):
    # Trường hợp có từ khóa đặc biệt 'lẽ'
    # nếu từ 'lẽ' đứng sau từ 'trăm'
    contain_special_word = False

    for index, value in enumerate(words):
        if value in special_word:
            contain_special_word = True
            if words[index - 1] in hundreds_words:
                words[index] = "không"

    if contain_special_word:
        return process_large_number_special(words)
    else:
        return process_large_number_normal(words)


if __name__ == '__main__':
    print(
        process_large_number(
            ['tỷ', 'lẽ', 'tám', 'trăm', 'năm', 'mươi', 'triệu', 'sáu', 'trăm', 'lẽ', 'ba', 'nghìn', 'hai', 'trăm'],
        ),
    )
