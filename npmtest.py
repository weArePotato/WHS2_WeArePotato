import os
import requests
import zipfile
import shutil
import csv
import re
import math
import subprocess
import json

# GitHub API URL 및 저장소 정보
GITHUB_API_URL = "https://api.github.com/repos/DataDog/malicious-software-packages-dataset/contents/samples/npm"

# 디렉토리 설정
DOWNLOAD_DIR = "downloads"
EXTRACT_DIR = "extracted"
RESULT_CSV = "results.csv"
ZIP_PASSWORD = "infected"

FEATURES = [
    'eval', 
    'WebAssembly.instantiate', 
    'WebAssembly.instantiateStreaming', 
    'WebAssembly.compile', 
    'WebAssembly.compileStreaming', 
    'Reflect', 
    'Proxy'
]
ADDITIONAL_FIELDS = ['entropy', 'feature_count']

# 다운로드 및 압축 해제 디렉토리 생성
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(EXTRACT_DIR, exist_ok=True)

# GitHub API에서 ZIP 파일 목록 가져오기 (최대 200개 파일)
def get_zip_files(api_url, limit=200):
    response = requests.get(api_url)
    response.raise_for_status()
    files = response.json()
    zip_files = [file['name'] for file in files if file['name'].endswith('.zip')]
    return zip_files[:limit]

# ZIP 파일 다운로드
def download_zip_file(file_url, download_path):
    response = requests.get(file_url)
    response.raise_for_status()
    with open(download_path, 'wb') as file:
        file.write(response.content)

# ZIP 파일 압축 해제
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

# 코드 파일을 분석하여 피처를 추출하는 함수
def analyze_code(file_path):
    features = set()
    entropy_value = 0
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            entropy_value = shannon_entropy(content)
            # 제공된 피처에 대한 정규 표현식 검색 추가
            if re.search(r'\beval\b', content):
                features.add('eval')
            if re.search(r'\bWebAssembly\.instantiate\b', content):
                features.add('WebAssembly.instantiate')
            if re.search(r'\bWebAssembly\.instantiateStreaming\b', content):
                features.add('WebAssembly.instantiateStreaming')
            if re.search(r'\bWebAssembly\.compile\b', content):
                features.add('WebAssembly.compile')
            if re.search(r'\bWebAssembly\.compileStreaming\b', content):
                features.add('WebAssembly.compileStreaming')
            if re.search(r'\bReflect\b', content):
                features.add('Reflect')
            if re.search(r'\bProxy\b', content):
                features.add('Proxy')
    except Exception as e:
        print(f"{file_path} 분석 중 오류 발생: {e}")
    return features, entropy_value

# package.json 파일을 분석하여 피처를 추출하는 함수
def analyze_package_json(file_path):
    features = set()
    entropy_value = 0
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            data = json.loads(content)
            scripts = data.get("scripts", {})
            dependencies = data.get("dependencies", {})
            devDependencies = data.get("devDependencies", {})
            all_content = content + " ".join(scripts.values()) + " ".join(dependencies.keys()) + " ".join(devDependencies.keys())
            entropy_value = shannon_entropy(all_content)
            # 제공된 피처에 대한 정규 표현식 검색 추가
            if re.search(r'\beval\b', all_content):
                features.add('eval')
            if re.search(r'\bWebAssembly\.instantiate\b', all_content):
                features.add('WebAssembly.instantiate')
            if re.search(r'\bWebAssembly\.instantiateStreaming\b', all_content):
                features.add('WebAssembly.instantiateStreaming')
            if re.search(r'\bWebAssembly\.compile\b', all_content):
                features.add('WebAssembly.compile')
            if re.search(r'\bWebAssembly\.compileStreaming\b', all_content):
                features.add('WebAssembly.compileStreaming')
            if re.search(r'\bReflect\b', all_content):
                features.add('Reflect')
            if re.search(r'\bProxy\b', all_content):
                features.add('Proxy')
    except Exception as e:
        print(f"{file_path} 분석 중 오류 발생: {e}")
    return features, entropy_value

# 메인 스크립트 실행
if __name__ == "__main__":
    zip_files = get_zip_files(GITHUB_API_URL)
    
    print(f"{len(zip_files)}개의 ZIP 파일을 찾았습니다.")
    
    with open(RESULT_CSV, mode='w', newline='') as csv_file:
        fieldnames = ['zip_file', 'file_path'] + FEATURES + ADDITIONAL_FIELDS
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for zip_file in zip_files:
            zip_url = f"https://raw.githubusercontent.com/DataDog/malicious-software-packages-dataset/main/samples/npm/{zip_file}"
            download_path = os.path.join(DOWNLOAD_DIR, zip_file)
            extract_path = os.path.join(EXTRACT_DIR, zip_file.rstrip('.zip'))

            print(f"{zip_url}에서 {zip_file} 다운로드 중...")
            try:
                download_zip_file(zip_url, download_path)
            except requests.exceptions.HTTPError as e:
                print(f"{zip_file} 다운로드 실패: {e}")
                continue

            print(f"{zip_file} 압축 해제 중...")
            try:
                extract_zip_file(download_path, extract_path, password=ZIP_PASSWORD)
            except (zipfile.BadZipFile, RuntimeError) as e:
                print(f"{zip_file} 압축 해제 실패: {e}")
                continue

            all_files = find_all_files(extract_path)
            print(f"{zip_file}에서 {len(all_files)}개의 파일을 찾았습니다.")

            for file_path in all_files:
                if file_path.endswith('package.json'):
                    features, entropy_value = analyze_package_json(file_path)
                else:
                    features, entropy_value = analyze_code(file_path)
                feature_dict = {feature: 'Yes' if feature in features else 'No' for feature in FEATURES}
                feature_dict['zip_file'] = zip_file
                feature_dict['file_path'] = file_path
                feature_dict['entropy'] = entropy_value
                feature_dict['feature_count'] = len(features)
                writer.writerow(feature_dict)
                print(f"파일: {file_path}, 엔트로피: {entropy_value}, 피처: {features}, 피처 수: {len(features)}")

    # 다운로드 및 압축 해제 파일 정리 (선택 사항)
    shutil.rmtree(DOWNLOAD_DIR)
    shutil.rmtree(EXTRACT_DIR)

    print("모든 작업이 완료되었습니다.")
