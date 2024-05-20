from setuptools import setup, find_packages
setup(name='otr-utils',
      version='4.1.1',
      description='test',
      author='yaara',
      author_email='no-email@python.net',
      packages=find_packages(),
      package_data={'*': ['**']},
      include_package_data=True
      )