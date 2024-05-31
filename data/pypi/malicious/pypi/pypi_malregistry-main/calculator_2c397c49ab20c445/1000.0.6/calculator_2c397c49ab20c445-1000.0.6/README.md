# PIP Package
## Instructions
1. Replace all <Package_Name> with the desired package name.
2. Create an account on https://pypi.org/
3. Follow Steps Below
```bash
# Prerequisities
sudo apt install twine -y
sudo apt-get install gcc libpq-dev -y
sudo apt-get install python-dev  python-pip -y
sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
pip3 install wheel

# Builing and uploading
python3 setup.py sdist bdist_wheel
twine upload dist/* --verbose
```
## Vulnerability
Using `--extra-index-url`
## Mitigation
Using `--index-url`
