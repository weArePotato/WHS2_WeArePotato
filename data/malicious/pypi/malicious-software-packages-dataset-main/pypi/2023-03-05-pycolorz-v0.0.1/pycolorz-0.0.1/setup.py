from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A Python Library'

# Setting up
setup(
    name="pycolorz",
    version=VERSION,
    author="Themonkey094",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)