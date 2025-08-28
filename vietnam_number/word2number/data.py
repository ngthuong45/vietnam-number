units = {
    'không': 0,
    'một': 1,
    'mốt': 1,
    'hai': 2,
    'ba': 3,
    'bốn': 4,
    'tư': 4,
    'năm': 5,
    'rưởi': 5,
    'rưỡi': 5,
    'lăm': 5,
    'sáu': 6,
    'bảy': 7,
    'tám': 8,
    'chín': 9,
}

billion_words = frozenset(("tỷ", "tỏi", "tỉ"))
million_words = frozenset(("triệu", "củ", "chai"))
thousand_words = frozenset(("nghìn", "nghàn", "ngàn"))

hundreds_words = frozenset(("trăm", "lít"))
tens_words = frozenset(("mươi", "chục"))

tens_special = ("mười",)
special_word = frozenset(("lẽ", "linh", "lẻ"))

word_multiplier = frozenset().union(
    billion_words,
    million_words,
    thousand_words,
    hundreds_words,
    tens_words,
    tens_special,
    special_word,
)
