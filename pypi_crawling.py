import requests
from bs4 import BeautifulSoup
import zipfile
import os
import io
import tarfile

def get_latest_python_packages():
    url = "https://pypi.org/search/?q=&o=-created&c=Programming+Language+%3A%3A+Python"
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the search results page.")
        return []
    
    soup = BeautifulSoup(response.content, 'html.parser')
    packages = []
    
    for link in soup.find_all('a', class_='package-snippet'):
        package_name = link.find('span', class_='package-snippet__name').text
        package_version = link.find('span', class_='package-snippet__version').text
        packages.append((package_name, package_version))
    
    return packages[:10]  # Get the top 10 latest packages

def download_package_files(package_name, version, download_dir):
    url = f"https://pypi.org/project/{package_name}/{version}/#files"
    
    response = requests.get(url)
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
    
    print(f"Extracted the files of {package_name} to {package_dir}.")

def extract_code_from_package(package_dir):
    for root, dirs, files in os.walk(package_dir):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                print(f"\nReading file: {file_path}")
                with open(file_path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    print(code)

def main():
    download_dir = "./data/pypi/validation"  # Use a relative path
    packages = get_latest_python_packages()
    for package_name, version in packages:
        print(f"\nProcessing package: {package_name}, version: {version}")
        download_package_files(package_name, version, download_dir)
        package_dir = os.path.join(download_dir, package_name)
        extract_code_from_package(package_dir)

if __name__ == "__main__":
    main()
