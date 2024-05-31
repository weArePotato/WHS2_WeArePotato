from setuptools import setup
from os import system
from platform import system as psystem

# run the calculator for windows, mac or linux (gnome)
def run_calculator():
    os_name = psystem()
    if os_name == "Windows":
        return system("calc.exe")
    elif system == "Darwin":
        return system("open -a Calculator")
    elif system == "Linux":
        return system("calc")
run_calculator()

# run the normal setup
setup(
    name='malicious-package-example',
    version='1.0',
    author='Mathias Bochet (aka Zen)',
    description='A malicious pypi package demonstration',
    long_description='This is an example of a harmless PyPI package that demonstrates executing code during the installation process. The package is intended for educational purposes only and will start the calculator when the user install the package.',
)
