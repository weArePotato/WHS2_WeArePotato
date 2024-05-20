from setuptools import setup, find_packages

VERSION = '3.0.0'
DESCRIPTION = "A Python package to encrypt complex data in Python3"
LONG_DESCRIPTION = "A Python package to encrypt complex data in Python3"

# Setting up
setup(
    name="pycryptography",
    version=VERSION,
    author="knwnLegend",
    author_email="nick.faltermeier@gmx.de",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)