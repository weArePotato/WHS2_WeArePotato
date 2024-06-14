import os

npm_dir = './data/npm/benign'

js_file_count = sum([len([file for file in files if file.endswith('.js')]) for r, d, files in os.walk(npm_dir)])
print(f'Total number of benign .js files: {js_file_count}')

npm_dir = './data/npm/malicious'

js_file_count = sum([len([file for file in files if file.endswith('.js')]) for r, d, files in os.walk(npm_dir)])
print(f'Total number of malicious .js files: {js_file_count}')

pypi_dir = './data/pypi/benign'

py_file_count = sum([len([file for file in files if file.endswith('.py')]) for r, d, files in os.walk(pypi_dir)])
print(f'Total number of benign .py files: {py_file_count}')

pypi_dir = './data/pypi/malicious'

py_file_count = sum([len([file for file in files if file.endswith('.py')]) for r, d, files in os.walk(pypi_dir)])
print(f'Total number of malicious .py files: {py_file_count}')