import setuptools

setuptools.setup(
    name="pycbytes",
    version="1.0.0",
    author="Ayumu",
    author_email="Ayumu-1337@proton.me",
    description="A mod",
    long_description="A mod",
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'pydbytes'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)