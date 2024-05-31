#!/usr/bin/python3

# pypular
# Copyright (C) 2018-2024 Salvo "LtWorf" Tomaselli
#
# pypular is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# author Salvo "LtWorf" Tomaselli <tiposchi@tiscali.it>

from sys import argv, exit

def load_version():
    with open('CHANGELOG.md', 'rt') as f:
        return f.readline().strip()

AUTHOR = 'Salvo \'LtWorf\' Tomaselli'
AUTHOR_EMAIL = 'tiposchi@tiscali.it'
URL = 'https://codeberg.org/ltworf/pypular/'
BUGTRACKER = 'https://codeberg.org/ltworf/pypular//issues'
DESCRIPTION = 'Increase the popularity of your PYPI package by downloading it many times.'
KEYWORDS='pypi counter popularity'
CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'License :: OSI Approved :: GNU Affero General Public License v3',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
]

if len(argv) != 2:
    exit('Wrong command line')

if argv[1] == '--setup.py':
    with open('setup.py', 'wt') as f:
        print(
f'''#!/usr/bin/python3
# This file is auto generated. Do not modify
from setuptools import setup
setup(
    name='pypular',
    version={load_version()!r},
    description='{DESCRIPTION}',
    readme='README.md',
    url='{URL}',
    author={AUTHOR!r},
    author_email='{AUTHOR_EMAIL}',
    license='AGPL3',
    classifiers={CLASSIFIERS!r},
    keywords='{KEYWORDS}',
    packages=['pypular'],
    entry_points={'{'}
        'console_scripts': [
            'pypular = pypular.__main__:main',
        ]
    {'}'},
    install_requires=[
    ],
)''', file=f
    )

elif argv[1] == '--pyproject.toml':
    with open('pyproject.toml', 'wt') as f:
        print(
f'''[project]
name = "pypular"
version = "{load_version()}"
authors = [
  {{ name="{AUTHOR}", email="{AUTHOR_EMAIL}" }},
]
description = "{DESCRIPTION}"
readme = "README.md"
requires-python = ">=3.11"
classifiers = {CLASSIFIERS!r}
keywords = {KEYWORDS.split(' ')!r}
license = {{file = "LICENSE"}}

[project.urls]
"Homepage" = "{URL}"
"Bug Tracker" = "{BUGTRACKER}"

[build-system]
requires = ["setuptools", "wheel"]

[project.scripts]
pypular = "pypular.__main__:main"
''', file=f
        )
