from setuptools import setup


setup(
    name='pycrypterexe',
    version='1.1.0',
    author='PyCryptexe',
    description='Python File Crypter FUD',
    packages=[''],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pycrypterexe = pycrypterexe.__main__:main'
        ]
    }
)

