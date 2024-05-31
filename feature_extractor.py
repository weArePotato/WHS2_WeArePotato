import csv, re

def read_csv_to_flat_list(file_path):
    flat_list = []
    
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            flat_list.extend(row)
    
    return flat_list

def isBlank(val):
    return val != ""
  
def filter_content(input_list):
    # Regular expression pattern to match content within parentheses including the parentheses
    pattern = re.compile(r'\(.*?\)')
    
    # List comprehension to apply the pattern and remove matches for each string in the list
    cleaned_list = [pattern.sub('', value) for value in input_list]
    cleaned_list = [value.lstrip('· ') for value in cleaned_list]
        
    return cleaned_list

# Example usage:
npm_file_paths = [
    './feature/npm/JavaScript Source Sink Analysis.xlsx - Malicious JavaScript APIs.csv',
    './feature/npm/JavaScript Source Sink Analysis.xlsx - Malicious NodeJS APIs.csv',
    './feature/npm/JavaScript Source Sink Analysis.xlsx - NodeJS Framework API.csv',
    './feature/npm/JavaScript Source Sink Analysis.xlsx - Source Sink List.csv',
    './feature/npm/JavaScript Source Sink Analysis.xlsx - System Calls.csv'
]

pypi_file_paths = [
    './feature/pypi/Python sensitive APIs.xlsx - Framework APIs.csv',
    './feature/pypi/Python sensitive APIs.xlsx - Old Functional Categories.csv',
    './feature/pypi/Python sensitive APIs.xlsx - Old Sources & Sinks.csv',
    './feature/pypi/Python sensitive APIs.xlsx - Source Sink List.csv',
]

def get_feature_list(type) :  
    feature_list = []

    if type == "pypi":
        file_paths = pypi_file_paths
    elif type == "npm":
        file = npm_file_paths
    for file_path in file_paths:
        contents = read_csv_to_flat_list(file_path)
        cleaned_list = list(filter(isBlank, contents))
        cleaned_list = filter_content(cleaned_list)
        feature_list += cleaned_list
    feature_list = list(set(feature_list))

    return feature_list