import os
import zipfile
import tarfile

def extract_files(directory, password=None):
    while True:
        files_to_extract = []
        
        # Collect all compressed files first
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(".zip") or file.endswith(".tar.gz") or file.endswith(".tgz"):
                    files_to_extract.append(os.path.join(root, file))

        # If no files to extract, break the loop
        if not files_to_extract:
            break

        # Extract the collected files
        for file_path in files_to_extract:
            # print(file_path)
            if file_path.endswith(".zip"):
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    if password:
                        zip_ref.extractall(os.path.dirname(file_path), pwd=password.encode())
                    else:
                        zip_ref.extractall(os.path.dirname(file_path))
                os.remove(file_path)
            elif file_path.endswith(".tar.gz") or file_path.endswith(".tgz"):
                with tarfile.open(file_path, 'r:gz') as tar_ref:
                    tar_ref.extractall(os.path.dirname(file_path))
                os.remove(file_path)

# Directory to search for compressed files
directory_to_search = "./data/pypi/pypi_malregistry-main"  # Change this to the directory you want to search

# Extract compressed files with a password if needed
extract_files(directory_to_search, password="infected")  