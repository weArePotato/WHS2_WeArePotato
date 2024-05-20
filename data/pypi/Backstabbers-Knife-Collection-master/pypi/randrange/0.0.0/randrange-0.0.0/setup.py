from setuptools import setup

setup(
    name='randrange',
    version='0.0.0',
    description='Rand range implementation',
    url='https://github.com/randrange/randrange',
    author='0xn3va',
    keywords=['python', 'range'],
    long_description='Rand range implementation',
    long_description_content_type='text/markdown',
    license='Apache-2.0',
    python_requires='>=3.5',
    extras_require={
        'dev': [
            'wheel',
            'twine'
        ]
    },
)
