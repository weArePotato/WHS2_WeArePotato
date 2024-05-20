import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setuptools.setup(
    # pip3 1000pip Climber System Free Download
    name="1000pip Climber System Free Download", 
    version="1",
    author="1000pip Climber System Free Download",
    author_email="1000pip@ClimberSystem.com",
    description="1000pip Climber System Free Download",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bfca1bsjtxsz0qao2rakno2q6w.hop.clickbank.net/?tid=pypi",
    project_urls={
        "Bug Tracker": "https://github.com/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=requires,
)
