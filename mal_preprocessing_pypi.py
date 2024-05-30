import ast
import os
import csv

def check_api_usage(func, lib=""):
    return lib in functions.keys() and func in functions[lib]
    

def parse_python_file(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return ast.parse(file_content)


def find_function_calls(node):
    calls = {}
    for lib in functions.keys():
        for func in functions[lib]:
            if lib == "":
                calls[func] = 0
            else :
                calls[lib + "." + func] = 0

    def _find_calls(n):
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute):
            func_name = n.func.attr
            print(func_name)
            lib_name = n.func.value.id
            if check_api_usage(func_name, lib_name):
                calls[lib_name + "." + func_name] += 1
        if isinstance(n, ast.Call) and isinstance(n.func, ast.Name):
            func_name = n.func.id
            if check_api_usage(func_name):
                calls[func_name] += 1
        for child in ast.iter_child_nodes(n):
            _find_calls(child)

    _find_calls(node)
    return calls


def parse_directory(directory_path):
    """
    Parses all Python files in a directory into their ASTs.

    Args:
        directory_path (str): Path to the directory.

    Returns:
        dict: A dictionary where keys are file paths and values are the parsed ASTs.
    """
    asts = {}
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                try:
                    asts[file_path] = parse_python_file(file_path)
                except Exception as e:
                    print(f"Failed to parse {file_path}: {e}")
    return asts


def search_functions_in_directory(directory):
    asts = parse_directory(directory)
    results = {}

    for file_path, tree in asts.items():
        function_calls = find_function_calls(tree)
        results[file_path] = function_calls

    return results

def write_results_to_csv(results, output_file):
    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write the header
        header = ['file name']
        for lib in functions.keys():
            for func in functions[lib]:
                if lib == "":
                    header.append(func)
                else :
                    header.append(lib + "." + func)
        writer.writerow(header)
        
        # Write the data rows
        for file_path, function_calls in results.items():
            for lib in functions.keys():
                for func in functions[lib]:
                    if lib == "":
                        row = [file_path] + [function_calls[func]]
                    else :
                        row = [file_path] + [function_calls[lib + "." + func]]
                    writer.writerow(row)

# Example usage
directory = "./temp"
functions = {"" : ["isinstance", "open", "print"], "os" : ["walk"]}
output_csv = "./temp/function_calls.csv"

search_results = search_functions_in_directory(directory)
print(search_results)
# write_results_to_csv(search_results, output_csv)
# print(f"Results written to {output_csv}")