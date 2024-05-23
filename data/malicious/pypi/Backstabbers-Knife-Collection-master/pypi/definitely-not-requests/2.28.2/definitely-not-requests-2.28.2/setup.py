#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 7)


# 'setup.py publish' shortcut.
if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    sys.exit()

requires = [
    "charset_normalizer>=2,<4",
    "idna>=2.5,<4",
    "urllib3>=1.21.1,<1.27",
    "certifi>=2017.4.17",
]
test_requirements = [
    "pytest-httpbin==0.0.7",
    "pytest-cov",
    "pytest-mock",
    "pytest-xdist",
    "PySocks>=1.5.6, !=1.5.7",
    "pytest>=3",
]

with open("README.md", "r", "utf-8") as f:
    readme = f.read()

about = {}
about['__title__'] = "definitely-not-requests"
about['__description__'] = "Python HTTP for Humans."
about['__url__'] = "https://requests.readthedocs.io"
about['__version__'] = "2.28.2"
about['__build__'] = 0x022802
about['__author__'] = "Kenneth Reitz"
about['__author_email__'] = "me@kennethreitz.org"
about['__license__'] = "Apache 2.0"
about['__copyright__'] = "Copyright Kenneth Reitz"
about['__cake__'] = "\u2728 \U0001f370 \u2728"

setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    package_data={"": ["LICENSE", "NOTICE"]},
    url=about["__url__"],
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=requires,
    license=about["__license__"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries",
    ],
    tests_require=test_requirements,
    extras_require={
        "security": [],
        "socks": ["PySocks>=1.5.6, !=1.5.7"],
        "use_chardet_on_py3": ["chardet>=3.0.2,<6"],
    },
    project_urls={
        "Documentation": "https://requests.readthedocs.io",
        "Source": "https://github.com/psf/requests",
    },
)
