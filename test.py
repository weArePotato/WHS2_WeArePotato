import os
import requests
import zipfile
import shutil
import csv
import re
import math

# GitHub API URL과 Repository 정보
GITHUB_API_URL = "https://api.github.com/repos/DataDog/malicious-software-packages-dataset/contents/samples/pypi"

# 임시 디렉토리 설정
DOWNLOAD_DIR = "downloads"
EXTRACT_DIR = "extracted"
RESULT_CSV = "results.csv"
ZIP_PASSWORD = "infected"
FEATURES = ['high_entropy_str', 'use_of_crypto', 'network_act', 'external_api_call', 'obfuscation', 'use_of_encoding', 'hidden_file_access']
ADDITIONAL_FIELDS = ['entropy', 'feature_count']

# 다운로드 디렉토리와 압축 해제 디렉토리 생성
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)

# GitHub API에서 zip 파일 목록 가져오기 (상위 200개 파일만)
def get_zip_files(api_url, limit=200):
    response = requests.get(api_url)
    response.raise_for_status()
    files = response.json()
    zip_files = [file['name'] for file in files if file['name'].endswith('.zip')]
    return zip_files[:limit]

# zip 파일 다운로드
def download_zip_file(file_url, download_path):
    response = requests.get(file_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)

# zip 파일 압축 해제
def extract_zip_file(zip_path, extract_to, password):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to, pwd=password.encode())

# 특정 디렉토리의 모든 파일을 재귀적으로 찾기
def find_all_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files

# Shannon 엔트로피 계산 함수
def shannon_entropy(data):
    if not data:
        return 0
    entropy = 0
    for x in set(data):
        p_x = float(data.count(x)) / len(data)
        entropy -= p_x * math.log(p_x, 2)
    return entropy

# 코드 파일을 분석하여 특성을 추출하는 함수
def analyze_code(file_path):
    features = set()
    entropy_value = 0
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            entropy_value = shannon_entropy(content)
            entropy_threshold = 4.0  # 엔트로피 기준값
            if entropy_value > entropy_threshold:
                features.add('high_entropy_str')
            if re.search(r'\bimport\b.*\b(cryptography|Crypto|hashlib|pycryptodome)\b', content):
                features.add('use_of_crypto')
            if re.search(r'\bimport\b.*\b(requests|urllib|http.client|socket)\b', content):
                features.add('network_act')
            if re.search(r'\bimport\b.*\b(os|subprocess|shutil)\b', content):
                features.add('external_api_call')
            if re.search(r'[\x00-\x1F\x7F-\xFF]', content):
                features.add('obfuscation')
            if re.search(r'\bimport\b.*\b(base64|binascii|codecs)\b', content):
                features.add('use_of_encoding')
            if re.search(r'\bimport\b.*\b(os|shutil)\b.*hidden|secret|stealth', content):
                features.add('hidden_file_access')
    except Exception as e:
        print(f"Error analyzing {file_path}: {e}")
    return features, entropy_value

# 메인 스크립트 실행
if __name__ == "__main__":
    zip_files = get_zip_files(GITHUB_API_URL)
    
    print(f"Found {len(zip_files)} zip files.")
    
    with open(RESULT_CSV, mode='w', newline='') as csv_file:
        fieldnames = ['zip_file', 'file_path'] + FEATURES + ADDITIONAL_FIELDS
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for zip_file in zip_files:
            zip_url = f"https://raw.githubusercontent.com/DataDog/malicious-software-packages-dataset/main/samples/pypi/{zip_file}"
            download_path = os.path.join(DOWNLOAD_DIR, zip_file)
            extract_path = os.path.join(EXTRACT_DIR, zip_file.rstrip('.zip'))

            print(f"Downloading {zip_file} from {zip_url}...")
            try:
                download_zip_file(zip_url, download_path)
            except requests.exceptions.HTTPError as e:
                print(f"Failed to download {zip_file}: {e}")
                continue

            print(f"Extracting {zip_file} to {extract_path}...")
            try:
                extract_zip_file(download_path, extract_path, password=ZIP_PASSWORD)
            except (zipfile.BadZipFile, RuntimeError) as e:
                print(f"Failed to extract {zip_file}: {e}")
                continue

            all_files = find_all_files(extract_path)
            print(f"Found {len(all_files)} files in {zip_file}.")

            for file_path in all_files:
                features, entropy_value = analyze_code(file_path)
                feature_dict = {feature: 'Yes' if feature in features else 'No' for feature in FEATURES}
                feature_dict['zip_file'] = zip_file
                feature_dict['file_path'] = file_path
                feature_dict['entropy'] = entropy_value
                feature_dict['feature_count'] = len(features)
                writer.writerow(feature_dict)
                print(f"File: {file_path}, Entropy: {entropy_value}, Features: {features}, Feature Count: {len(features)}")

    # 다운로드 및 압축 해제 파일 정리 (선택 사항)
    shutil.rmtree(DOWNLOAD_DIR)
    shutil.rmtree(EXTRACT_DIR)

    print("All tasks completed.")
