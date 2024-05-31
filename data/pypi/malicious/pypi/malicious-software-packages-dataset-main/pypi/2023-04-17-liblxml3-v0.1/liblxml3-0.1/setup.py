from setuptools import setup, find_packages

setup(
    name='liblxml3',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        '': ['*.*']
    },
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'your_package_name=bot.main:main'
        ]
    },
    python_requires='>=3.9'
)
