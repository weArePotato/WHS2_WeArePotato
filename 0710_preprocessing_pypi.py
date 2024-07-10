import os
import ast
import math
import csv
import feature_extractor

def calculate_normalized_entropy(text):
    character_freq = {}
    total_characters = len(text)
    for char in text:
        character_freq[char] = character_freq.get(char, 0) + 1

    entropy = 0
    for freq in character_freq.values():
        probability = freq / total_characters
        entropy += -probability * math.log(probability, 2)

    if entropy == 0:
        return 0
    normalized_entropy = entropy / math.log(len(character_freq), 2)
    return normalized_entropy

def calculate_cyclomatic_complexity(node):
    complexity = 0
    if isinstance(node, (ast.If, ast.For, ast.While, ast.And, ast.Or, ast.ExceptHandler)):
        complexity += 1
    for child in ast.iter_child_nodes(node):
        complexity += calculate_cyclomatic_complexity(child)
    return complexity


def get_attribute(node):
    if not isinstance(node, ast.Attribute) :
        return ""
    # print(ast.dump(node))
    attr = node.attr
    val = node.value
    if isinstance(val, ast.Name):
        return val.id
    elif isinstance(val, ast.Attribute):
        return get_attribute(val) + "." + val.attr
    else :
        return ""



def find_function_calls(node, function_names):
    calls = {func: 0 for func in function_names}
    
    # aliased modules
    aliased_lib = {}    # import as
    all_import_lib = [] # from import *
    simple_func = {}    # from import
    aliased_func = {}   # from import as
    
    def _set_alias(n):
        for n in ast.walk(node):
            if isinstance(n, ast.Import):
                for alias in n.names:
                    module_name = alias.name
                    if module_name != None and module_name in calls:
                        calls[module_name] += 1
                    alias_name = alias.asname
                    if alias_name != None:
                        aliased_lib[alias_name] = module_name
            elif isinstance(n, ast.ImportFrom):
                module_name = n.module
                if module_name != None and module_name in calls:
                    calls[module_name] += 1
                for alias in n.names:
                    func_name = alias.name
                    alias_name = alias.asname
                    if module_name == None or func_name == None:
                        continue
                    if func_name == "*":
                        all_import_lib.append(module_name)
                    elif alias_name  != None :
                        aliased_func[alias_name] = module_name + "." + func_name
                    else:
                        simple_func[func_name] = module_name + "." + func_name

    def _find_calls(n):
        # used with package name
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            attr_name = get_attribute(n.func)
            if attr_name in aliased_lib:
                attr_name = aliased_lib[attr_name]
            func_name = n.func.attr
            func_name = attr_name + "." + func_name
            if func_name in calls:
                calls[func_name] += 1
        # used without package name
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            # check import *
            func_name = n.func.id
            for lib in all_import_lib:
                if lib + "." + func_name in calls:
                    calls[lib + "." + func_name] += 1
            # check from import 
            if func_name in simple_func:
                func_name = simple_func[func_name]
            # check from import as
            elif func_name in aliased_func:
                func_name = aliased_func[func_name]
            if func_name in calls:
                calls[func_name] += 1
        for child in ast.iter_child_nodes(n):
            _find_calls(child)

    _set_alias(node)
    # print("aliased lib: ", aliased_lib)
    # print("all import lib: ", all_import_lib)
    # print("simple func: ", simple_func)
    # print("aliased func: ", aliased_func)
    _find_calls(node)
    return calls
  


def extract_metadata(file_content):
    metadata = {}
    try:
        tree = ast.parse(file_content)
        function_count = 0
        total_cc = 0
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_count += 1
                complexity = calculate_cyclomatic_complexity(node)
                total_cc += complexity
            elif isinstance(node, ast.ClassDef):
                metadata['class_count'] = metadata.get('class_count', 0) + 1
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    metadata['imports'] = metadata.get('imports', []) + [alias.name]
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    metadata['imports'] = metadata.get('imports', []) + [node.module + '.' + alias.name]

        metadata['function_count'] = function_count
        metadata['average_cc'] = total_cc / function_count if function_count > 0 else 0
    except Exception as e:
        print(f"Failed to parse metadata: {e}")
    return metadata

def parse_python_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return file_content, ast.parse(file_content)

'''
def parse_directory(directory_path):
    file_contents = {}
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    file_content, tree = parse_python_file(file_path)
                    file_contents[file_path] = (file_content, tree)
                except Exception as e:
                    print(f"Failed to parse {file_path}: {e}")
    return file_contents
'''

def parse_directory(directory_path, isMal):
    asts = {}
    cnt = 0
    
    # for malicious
    if isMal:
        dir_list = []
        # get directory names
        for root, dirs, files in os.walk(directory_path):
            for dir in dirs:
                dir_list.append(root + "/" + dir)
            break
        
        packages = []
        paths = []
        # get package name
        for dir in dir_list:
            for root, dirs, _ in os.walk(dir):
                for package in dirs:
                    if package not in packages:
                        packages.append(package)
                        paths.append(root + "/" + package)
                break
        
        # make ast for all paths
        for path in paths:
            for root, dirs, files in os.walk(path):
                for file in files:
                    if file.endswith('.py'):
                        file_path = os.path.join(root, file)
                        try:
                            asts[file_path] = parse_python_file(file_path)
                            cnt += 1
                        except Exception as e:
                            print(f"Failed to parse {file_path}: {e}")
    # for others
    else:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                # if cnt > 23743:
                #     return asts
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    try:
                        asts[file_path] = parse_python_file(file_path)
                        cnt += 1
                    except Exception as e:
                        print(f"Failed to parse {file_path}: {e}")

    print(cnt)
    return asts



def find_function_calls(node, function_names):
    calls = {func: 0 for func in function_names}
    for n in ast.walk(node):
        if isinstance(n, ast.Call):
            func_name = ""
            if isinstance(n.func, ast.Name):
                func_name = n.func.id
            elif isinstance(n.func, ast.Attribute):
                func_name = n.func.attr
            if func_name in calls:
                calls[func_name] += 1
    return calls

def search_functions_in_directory(directory, function_names, page):
    files = parse_directory(directory, page)
    results = {}
    for file_path, (file_content, tree) in files.items():
        feature_cnt = find_function_calls(tree, set(function_names))
        feature_cnt["entropy"] = calculate_normalized_entropy(file_content)
        feature_cnt.update(extract_metadata(file_content))
        url = f"https://pypi.org/search/?c=Programming+Language+%3A%3A+Python&o=-created&q=&page={page}"
        feature_cnt["url"] = url
        results[file_path] = feature_cnt
    return results

def write_results_to_csv(results, function_names, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ['file name', 'entropy', 'url', 'function_count', 'average_cc', 'class_count', 'imports'] + function_names
        writer.writerow(header)

        for file_path, features in results.items():
            row = [file_path, features["entropy"], features["url"], features.get('function_count', 0), features.get('average_cc', 0), features.get('class_count', 0), ', '.join(features.get('imports', []))] + [features[func] for func in function_names]
            writer.writerow(row)

def preprocess(dir, out, page):
    functions_to_search = ["eval", "exec", "open", "input", "subprocess", "os.system", "requests.get", "requests.post"]  # 예시 함수 목록
    functions_to_search += feature_extractor.get_feature_list("pypi")
    print(functions_to_search)
    search_results = search_functions_in_directory(dir, functions_to_search, page)
    write_results_to_csv(search_results, functions_to_search, out)
    print(f"Results written to {out}")

if __name__ == "__main__":
    # benign
    preprocess("./data/pypi/benign", "./preprocessed_data/pypi/pypi_ast_analysis_benign_modify.csv", False)
    # malicious
    # preprocess("./data/pypi/malicious", "./preprocessed_data/pypi/pypi_ast_analysis_malicious_modify.csv", 1)
