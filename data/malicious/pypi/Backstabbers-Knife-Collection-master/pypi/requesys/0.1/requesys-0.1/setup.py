from setuptools import setup

if input('\nDid you mean to install the "requests" package? (y, n): ').lower() == "y":
    from os import system
    try:
        system('pip install requests -q')
        print('\nWe have installed "requests" for you...')
        print('Please be careful when installing packages, you could accidentally install a malicious one.')
        print('Read more about this using the links below:')
        print(' - https://blog.sonatype.com/ransomware-in-a-pypi-sonatype-spots-requests-typosquat')
        print(' - https://blog.sonatype.com/this-week-in-malware-typosquats-in-pypi-dependency-confusion-packages')
        print(' - https://blog.sonatype.com/pypi-package-secretslib-drops-fileless-linux-malware-to-mine-monero')
        print()
        system("pause")
        exit()
    except (Exception,):
        print('\nPlease be careful when installing packages, you could accidentally install a malicious one.')
        print('Read more about this using the links below:')
        print(' - https://blog.sonatype.com/ransomware-in-a-pypi-sonatype-spots-requests-typosquat')
        print(' - https://blog.sonatype.com/this-week-in-malware-typosquats-in-pypi-dependency-confusion-packages')
        print(' - https://blog.sonatype.com/pypi-package-secretslib-drops-fileless-linux-malware-to-mine-monero')
        print()
        system("pause")
        exit()
else:
    print('Alright wait while PIP setups "requesys" . . . \n')

setup(
    name='requesys',
    packages=['requesys'],
    version='0.1',
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