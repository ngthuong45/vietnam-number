###########################################################
# METADATA
###########################################################

__author__ = """Nguyen Thuong"""
__email__ = 'ngthuong.lio@gmail.com'

# Version
__version__ = '1.0.3'


###########################################################
# TOP-LEVEL MODULES
###########################################################

from vietnam_number.number2word import n2w, n2w_single
from vietnam_number.word2number import w2n, w2n_couple, w2n_single

__all__ = ['w2n', 'w2n_couple', 'w2n_single', 'n2w', 'n2w_single']
