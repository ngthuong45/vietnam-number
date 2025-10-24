###########################################################
# METADATA
###########################################################

__author__ = """Nguyen Thuong"""
__email__ = 'ngthuong.lio@gmail.com'

# Version
from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("vietnam_number")
except PackageNotFoundError:
    __version__ = "0.0.0"  # fallback for source installs or testing

###########################################################
# TOP-LEVEL MODULES
###########################################################

from vietnam_number.number2word import n2w, n2w_single
from vietnam_number.word2number import w2n, w2n_couple, w2n_single

__all__ = ['w2n', 'w2n_couple', 'w2n_single', 'n2w', 'n2w_single']
