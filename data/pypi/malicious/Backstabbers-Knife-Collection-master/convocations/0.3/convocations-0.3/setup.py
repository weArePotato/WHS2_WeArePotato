#!/usr/bin/env python

# Support setuptools only, distutils has a divergent and more annoying API and
# few folks will lack setuptools.
from setuptools import setup, find_packages
from importlib.resources import open_text
# Version info -- read without importing
_locals = {}

version = '0.3'

# PyYAML ships a split Python 2/3 codebase. Unfortunately, some pip versions
# attempt to interpret both halves of PyYAML, yielding SyntaxErrors. Thus, we
# exclude whichever appears inappropriate for the installing interpreter.
exclude = ["*.yaml2", 'test']

# Frankenstein long_description: version-specific changelog note + README
with open('README.md') as f:
    long_description = f.read()

extras = {}
all_extras = set()
for x in [ 'dev', 'checkpoint', 'onelogin', 'certs', 'aws', 'sharepoint',
           'palo_alto', 'tundra', 'airflow', ]:
    filename = f'{x}.txt'
    with open(filename, 'r') as f:
        st = f.read()
    rg = st.split('\n')
    extras[x] = [ lx for lx in rg if lx ]
    if x != 'dev':
        all_extras |= set(rg)
if all_extras:
    all_extras = list(filter(None, all_extras))
    all_extras.sort()
    extras['all'] = all_extras
print(extras)

setup(
    name='convocations',
    version=version,
    description='convocations',
    license='BSD',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='2ps',
    author_email='pshingavi@gmail.com',
    url='https://github.com/crazy-penguins/convocations',
    package_dir={ '': '.', },
    packages=find_packages(
        where='.',
        exclude=['test', ]),
    package_data={
        'convocations.pypi': [ 'templates/**/*', ],
        'convocations.tundra': [ 'templates/**/*', ],
        'convocations.docker': [ 'templates/**/*', ],
    },
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'jinja2',
        'pyyaml',
        'termcolor',
        'colorama',
        'requests',
        'requests_oauthlib',
        'waddle',
        'halo',
        'python-dateutil',
        'pytz',
    ],
    entry_points={
       'console_scripts': [
           'pypi = convocations.pypi.program:program.run',
           'sharepoint = convocations.sharepoint.program:program.run',
           'dbuy = test.dbuy.program:program.run',
       ]
    },
    extras_require=extras,
)
