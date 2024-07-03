import requests
from bs4 import BeautifulSoup
import zipfile
import os
import io
import tarfile
import mal_preprocessing_pypi
import shutil

def get_latest_python_packages(num):
    cnt = 0
    page = 1
    packages = []
    while cnt < num:
        url = f"https://pypi.org/search/?c=Programming+Language+%3A%3A+Python&o=-created&q=&page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            print("Failed to retrieve the search results page.")
            return []
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        for link in soup.find_all('a', class_='package-snippet'):
            package_name = link.find('span', class_='package-snippet__name').text
            package_version = link.find('span', class_='package-snippet__version').text
            package_url = f"https://pypi.org/project/{package_name}/{package_version}/"
            packages.append((package_name, package_version, package_url))
        
        cnt += len(packages)
        page += 1
    return packages[:num + 1]

def download_package_files(package_name, version, download_dir, package_url, url_map):
    response = requests.get(package_url)
    if response.status_code != 200:
        print(f"Failed to retrieve the package page for {package_name}.")
        return
    
    soup = BeautifulSoup(response.content, 'html.parser')
    file_link = None
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and (href.endswith('.whl') or href.endswith('.tar.gz')):
            file_link = href
            break
    
    if not file_link:
        print(f"Failed to find a .whl or .tar.gz file for {package_name}.")
        return
    
    file_url = file_link
    file_response = requests.get(file_url)
    if file_response.status_code != 200:
        print(f"Failed to download the file for {package_name}.")
        return
    
    file_name = file_url.split('/')[-1]
    package_dir = os.path.join(download_dir, package_name)
    os.makedirs(package_dir, exist_ok=True)
    file_path = os.path.join(package_dir, file_name)
    
    with open(file_path, 'wb') as f:
        f.write(file_response.content)
    
    if file_name.endswith('.zip') or file_name.endswith('.whl'):
        with zipfile.ZipFile(file_path, 'r') as zip_ref:
            zip_ref.extractall(package_dir)
    elif file_name.endswith('.tar.gz'):
        with tarfile.open(file_path, 'r:gz') as tar_ref:
            tar_ref.extractall(package_dir)

    #Save the URL
    for root, dirs, files in os.walk(package_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                url_map[file_path] = package_url

    # print(f"Extracted the files of {package_name} to {package_dir}.")

"""def extract_code_from_package(package_dir):
    for root, dirs, files in os.walk(package_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                # print(f"\nReading file: {file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    # print(code)"""

def download_validation_files(num, dir):
    packages = get_latest_python_packages(num)
    url_map = {}
    for package_name, version, package_url in packages:
        # print(f"\nProcessing package: {package_name}, version: {version}")
        download_package_files(package_name, version, dir, package_url, url_map)
        # package_dir = os.path.join(dir, package_name)
        # extract_code_from_package(package_dir)
    return url_map

def convert_path_to_url(file_path, url_map):
    return url_map.get(file_path, "")


if __name__ == "__main__":
    package_num = 5 
    download_dir = "./data/pypi/validation"
    output_dir = "./preprocessed_data/pypi/pypi_ast_analysis_validation.csv"
    # download_validation_files(package_num, download_dir)
    url_map = download_validation_files(package_num, download_dir)
    mal_preprocessing_pypi.preprocess(download_dir, output_dir, False, url_map)
    shutil.rmtree(download_dir)
