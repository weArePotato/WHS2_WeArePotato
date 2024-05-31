from setuptools import setup, find_packages



VERSION = '1.1'
DESCRIPTION = 'fr'
LONG_DESCRIPTION = 'clear console before print then prints printf("nagogy")'
setup(
    name="printf",
    version=VERSION,
    author="dynastyoak",
    author_email="nagogy@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)