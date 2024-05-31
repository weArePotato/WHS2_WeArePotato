#!/usr/bin/env python

from distutils.core import setup




class create():
     with open('readme.txt', 'w') as f:
          f.write('Create a new text file!')

setup(name='salamus5',
      version='0.1.4',
      description='Security project that aims to check how many developers install typoed libraries.',
      author='zer0ul',
      author_email='zer0ul@vulnium.com',
      url='https://google.com',
      packages=[],
      cmdclass={
         'install' :  create,
      },

     )
