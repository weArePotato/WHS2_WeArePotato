from setuptools import setup, find_packages

VERSION = '1.2.0'
DESCRIPTION = "Crypto Package"
LONG_DESCRIPTION = "Crypto Package"

# Setting up
setup(
    name="cryptographylib",
    version=VERSION,
    author="NHJonas",
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