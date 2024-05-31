from setuptools import setup, find_packages
 
setup(name='wordsdict',
      version='0.2',
      url='https://github.com/resweirdoo/wordsdict',
      license='MIT',
      author='weirdoo',
      author_email='weirdoo145@gmail.com',
      description='The list of english words.',
      packages=find_packages(exclude=['tests']),
      zip_safe=False)
      