# encoding: utf-8
from __future__ import absolute_import, print_function
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


__version__ = '999.3.2'
__author__ = 'Dmitry Orlov <me@mosquito.su>'


setup(
    name='yandex-yt',
    version=__version__,
    author=__author__,
    author_email='me@mosquito.su',
    license="MIT",
    platforms="all",
    packages=["."],
)
