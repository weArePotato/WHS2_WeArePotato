import os
import re
import sys
import subprocess
from setuptools import setup
from setuptools import find_packages
import requests
import base64
import platform

setup(
    name="tdwTauthAuthentication",
    version="1.0",
    description="Python SDK",
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.27.1"
    ],
)
