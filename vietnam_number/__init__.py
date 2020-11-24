import sys

# Check python version
try:
    version_info = sys.version_info
    if version_info < (3, 6, 0):
        raise RuntimeError("vietnam-number requires Python 3.6 or later")
except Exception:
    pass

###########################################################
# METADATA
###########################################################

__author__ = """Nguyen Thuong"""
__email__ = 'ngthuong.lio@gmail.com'

# Version
__version__ = '0.1.3'


###########################################################
# TOP-LEVEL MODULES
###########################################################

from vietnam_number.word2number import w2n, w2n_couple, w2n_single

__all__ = [
    'w2n',
    'w2n_couple',
    'w2n_single',
]
