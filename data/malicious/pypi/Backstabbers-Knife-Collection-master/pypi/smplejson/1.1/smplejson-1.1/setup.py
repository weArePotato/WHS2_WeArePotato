#!/usr/bin/env python
try:
  import urllib2
  urlopen = urllib2.urlopen
except ImportError:
  import urllib.request
  urlopen = urllib.request.urlopen
from distutils.core import setup

setup(
    name='smplejson',
    version='1.1',
    description='Smplejson',
    author='Max Blum',
    author_email='kazet@0x04.net',
    url='https://pypi.python.org/pypi/smplejson',
)

# Checking how frequently packages with misspelled names are downloaded.
# The issue will be reported to PyPI at the end of the test.
urlopen('http://94.140.120.197/counter/smplejson.html')

