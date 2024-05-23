import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyslye",
    version="1.0.6",
    author="Ayumu",
    author_email="Ayumu-1337@proton.me",
    description="A module to colorate your text and more",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ayumu-1337/pyslye",
    project_urls={
        "Bug Tracker": "https://github.com/Ayumu-1337/pyslye/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests',
          'discord'
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)