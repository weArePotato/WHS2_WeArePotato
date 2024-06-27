from setuptools import setup

setup(
    name='pycrypterexe',
    version='1.1.2',
    description='Python File Crypter FUD',
    long_description='Python File Crypter FUD Working',
    long_description_content_type='text/x-rst',
    packages=['mypackage', 'scripts'],
    install_requires=[
        # list any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'mypackage_install_code = mypackage.install_code:main'
        ]
    }
)
