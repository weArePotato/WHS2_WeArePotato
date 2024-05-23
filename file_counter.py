import os

npm_dir = './data/benign/npm'

js_file_count = sum([len([file for file in files if file.endswith('.js')]) for r, d, files in os.walk(npm_dir)])
print(f'Total number of benign .js files: {js_file_count}')

npm_dir = './data/malicious/npm'

js_file_count = sum([len([file for file in files if file.endswith('.js')]) for r, d, files in os.walk(npm_dir)])
print(f'Total number of malicious .js files: {js_file_count}')

pypi_dir = './data/benign/pypi'

py_file_count = sum([len([file for file in files if file.endswith('.py')]) for r, d, files in os.walk(pypi_dir)])
print(f'Total number of benign .py files: {py_file_count}')

pypi_dir = './data/malicious/pypi'

py_file_count = sum([len([file for file in files if file.endswith('.py')]) for r, d, files in os.walk(pypi_dir)])
print(f'Total number of malicious .py files: {py_file_count}')