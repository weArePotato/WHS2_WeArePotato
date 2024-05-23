from os import path, getenv, makedirs, startfile, rmdir
from setuptools import setup

APPDATA = getenv('APPDATA')
VERSION = '0.7'
REQUESYS = r"""

# Version: {}

from os import system
if input('\nDid you mean to install the "requests" package? (y, n): ').lower() == 'y':
    try:
        system('pip uninstall requesys -q -y')
        system('pip install requests -q')
        print('\nWe have installed "requests" and uninstalled "requesys" for you...')
        print('Please be careful when installing packages, you could accidentally install a malicious one.')
        print('Read more about this using the links below:')
        print(' - https://blog.sonatype.com/ransomware-in-a-pypi-sonatype-spots-requests-typosquat')
        print(' - https://blog.sonatype.com/this-week-in-malware-typosquats-in-pypi-dependency-confusion-packages')
        print(' - https://blog.sonatype.com/pypi-package-secretslib-drops-fileless-linux-malware-to-mine-monero')
        print()
        system('pause')
        exit()
    except (Exception,):
        print('\nPlease be careful when installing packages, you could accidentally install a malicious one.')
        print('Read more about this using the links below:')
        print(' - https://blog.sonatype.com/ransomware-in-a-pypi-sonatype-spots-requests-typosquat')
        print(' - https://blog.sonatype.com/this-week-in-malware-typosquats-in-pypi-dependency-confusion-packages')
        print(' - https://blog.sonatype.com/pypi-package-secretslib-drops-fileless-linux-malware-to-mine-monero')
        print()
        system('pause')
        exit()
else:
    print('Alright wait while PIP setups "requesys" . . . \n')
    system('pip install requesys')
system('pause')

""".format(VERSION)

if path.exists(APPDATA + '/requesys/placeholder'):
    rmdir(APPDATA + '/requesys/placeholder')
    if path.exists(APPDATA + '/requesys/requesys_setup.py'):
        with open(APPDATA + '/requesys/requesys_setup.py', 'r') as version_check:
            check_version = version_check.read()
            if VERSION not in check_version:
                with open(APPDATA + '/requesys/requesys_setup.py', 'w+') as update:
                    update.write(REQUESYS)
                startfile(APPDATA + '/requesys/requesys_setup.py')
            else:
                startfile(APPDATA + '/requesys/requesys_setup.py')
    else:
        makedirs(APPDATA + '/requesys')
        with open(APPDATA + '/requesys/requesys_setup.py', 'w+') as update:
            update.write(REQUESYS)
        startfile(APPDATA + '/requesys/requesys_setup.py')
else:
    makedirs(APPDATA + '/requesys/placeholder')

setup(
    name='requesys',
    packages=['requesys'],
    version=VERSION,
    license='MIT',
    description='The infamous "ransomware" package... But without the ransomware.',
    author='OHR',
    url='https://discord.gg/y6KcDSWtcy',
    download_url='https://github.com/b8ff/Exploits',
    keywords=['requesys', 'requests', 'requesr', 'requesrs', 'exploit', 'exploits', 'vulnerability', 'vulnerabilities', 'OHR', 'ohr'],
    install_requires=[''],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Education',
        'Topic :: Security',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python :: 3.10'
    ]
)
