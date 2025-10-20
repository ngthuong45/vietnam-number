UNITS: dict[str, str] = {
    "không": "0",
    "một": "1",
    "mốt": "1",
    "hai": "2",
    "ba": "3",
    "bốn": "4",
    "tư": "4",
    "năm": "5",
    "rưởi": "5",
    "rưỡi": "5",
    "lăm": "5",
    "nhăm": "5",
    "sáu": "6",
    "bảy": "7",
    "tám": "8",
    "chín": "9",
}

BILLION_WORDS = frozenset(("tỷ", "tỏi", "tỉ"))
MILLION_WORDS = frozenset(("triệu", "củ", "chai"))
THOUSAND_WORDS = frozenset(("nghìn", "nghàn", "ngàn", "cành"))

BILLION_MILLION_THOUSAND_WORDS = BILLION_WORDS.union(MILLION_WORDS, THOUSAND_WORDS)

HUNDREDS_WORDS = frozenset(("trăm", "lít", "lốp", "xị"))
TENS_WORDS = frozenset(("mươi", "chục"))

HUNDREDS_TENS_WORDS = HUNDREDS_WORDS.union(TENS_WORDS)

TENS_SPECIAL = ("mười",)
SPECIAL_WORDS = frozenset(("lẽ", "linh", "lẻ"))

WORD_MULTIPLIER = BILLION_MILLION_THOUSAND_WORDS.union(
    HUNDREDS_TENS_WORDS,
    TENS_SPECIAL,
    SPECIAL_WORDS,
)

ALLOW_WORDS = WORD_MULTIPLIER.union(UNITS)
ALLOW_WORDS_EXCLUDING_TENS_SPECIAL = ALLOW_WORDS.difference(TENS_SPECIAL)

KEYWORD_TO_WORDS: dict[str, frozenset[str]] = {
    "tens_index": TENS_WORDS,
    "hundreds_index": HUNDREDS_WORDS,
    "thousand_index": THOUSAND_WORDS,
    "million_index": MILLION_WORDS,
    "billion_index": BILLION_WORDS,
    "special_index": SPECIAL_WORDS,
}

WORD_TO_KEYWORD: dict[str, str] = {
    word: keyword_name
    for keyword_name, words in KEYWORD_TO_WORDS.items()
    for word in words
}
