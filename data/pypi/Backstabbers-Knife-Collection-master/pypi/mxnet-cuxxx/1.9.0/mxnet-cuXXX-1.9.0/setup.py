

from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        print("Hello world")


setup(name='mxnet-cuXXX', #package name
      version='1.9.0',
      description='AnupamAS01',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
