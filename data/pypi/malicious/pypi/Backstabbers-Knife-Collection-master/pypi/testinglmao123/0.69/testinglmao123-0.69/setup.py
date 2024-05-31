from setuptools import find_packages, setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        # do shit here
        print("x")




setup(
  name = 'testinglmao123',
  packages=find_packages(),
  version = '0.69',
  description = ':clown:',
  author = ':clown:',
  install_requires=["sockets","discord.py","aiohttp","Cmake","wheel","requests","gitpython"],
  cmdclass={
    'install': CustomInstallCommand,
  },
  author_email = 'github@gmail.com',
  url = 'https://github.com',
  keywords = [],
  classifiers = [],

)
