"""
Basic
"""
__version__ = '0.1.1'
__author__ = 'Jon Crall'
__author_email__ = 'erotemic@gmail.com'
__url__ = 'https://gitlab.kitware.com/computer-vision/simple_dvc'

__mkinit__ = """
mkinit /home/joncrall/code/simple_dvc/simple_dvc/__init__.py
"""

from .api import SimpleDVC

__all__ = ['SimpleDVC']
