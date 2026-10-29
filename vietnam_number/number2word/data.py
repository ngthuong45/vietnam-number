from enum import StrEnum


class ZeroWord(StrEnum):
    """Choose "lẻ" or "linh" to read an interior zero digit (101, 205...)."""

    LE = "lẽ"
    """lẻ: 101 → "một trăm lẻ một"."""

    LINH = "linh"
    """linh: 101 → "một trăm linh một"."""


UNITS = {
    '0': 'không',
    '1': 'một',
    '2': 'hai',
    '3': 'ba',
    '4': 'bốn',
    '5': 'năm',
    '6': 'sáu',
    '7': 'bảy',
    '8': 'tám',
    '9': 'chín',
}

UNITS_WITH_TRAILING_SPACE_TABLE = str.maketrans(
    {
        "0": "không ",
        "1": "một ",
        "2": "hai ",
        "3": "ba ",
        "4": "bốn ",
        "5": "năm ",
        "6": "sáu ",
        "7": "bảy ",
        "8": "tám ",
        "9": "chín ",
    }
)
