
import esprima
import os
import csv
import math
from collections import Counter
from pathlib import Path
from tempfile import NamedTemporaryFile as _ffile
import sys
sys.setrecursionlimit(1500)

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

def check_api_usage(node, api_usage, visited_nodes):
    if isinstance(node, dict):
        node_id = id(node)
        if node_id in visited_nodes:
            return
        visited_nodes.add(node_id)

        node_type = node.get('type')
        if node_type == 'CallExpression':
            callee = node.get('callee')
            process_callee(callee, api_usage)

        for value in node.values():
            if isinstance(value, dict):
                check_api_usage(value, api_usage, visited_nodes)
            elif isinstance(value, list):
                for item in value:
                    check_api_usage(item, api_usage, visited_nodes)

def process_callee(callee, api_usage):
    if isinstance(callee, dict):
        if callee.get('type') == 'MemberExpression':
            process_member_expression(callee, api_usage)
        elif callee.get('type') == 'Identifier' and callee.get('name') in api_list:
            api_usage[callee.get('name')] += 1

def process_member_expression(member_expr, api_usage):
    object_part = member_expr.get('object')
    property_part = member_expr.get('property')
    if isinstance(object_part, dict) and isinstance(property_part, dict):
        object_name = object_part.get('name')
        property_name = property_part.get('name')
        full_name = f"{object_name}.{property_name}"
        if full_name in api_list:
            api_usage[full_name] += 1

def extract_ast_from_js_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            print(file_path)
            ast = esprima.parseScript(content, {'tolerant': True, 'ecmaVersion': 2020})

            return ast, content
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None, None

def traverse_node(node, node_types, api_usage, visited_nodes):
    nodes = []
    max_depth = 0
    stack = [(node, 0)]

    while stack:
        current_node, depth = stack.pop()
        max_depth = max(max_depth, depth)

        node_dict = current_node.toDict() if hasattr(current_node, 'toDict') else current_node

        check_api_usage(node_dict, api_usage, visited_nodes)
        node_type = node_dict.get('type', 'Unknown')
        if node_type in node_types:
            nodes.append(node_type)

        for value in node_dict.values():
            if isinstance(value, (dict, esprima.nodes.Node)):
                stack.append((value, depth + 1))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, (dict, esprima.nodes.Node)):
                        stack.append((item, depth + 1))

    return nodes, max_depth

def get_label_from_folder_path(file_path):

    if 'data/malicious' in file_path:
        return 1
    elif 'data/benign' in file_path:
        return 0
    else:
        return -1

def process_js_file(file_path, node_types, api_list):
    ast, content = extract_ast_from_js_file(file_path)
    if ast is not None and content is not None:
        api_usage = {api: 0 for api in api_list}
        visited_nodes = set()
        node_types_found, max_depth = traverse_node(ast, node_types, api_usage, visited_nodes)
        entropy = calculate_normalized_entropy(content)
        label = get_label_from_folder_path(file_path)
        return Counter(node_types_found), api_usage, entropy, max_depth, label
    else:
        return None

def write_to_csv(data, headers, csv_file):
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

# 노드 유형 및 API 목록 정의
node_types = [
    'ArrayExpression', 'ArrowFunctionExpression',
]

api_list = []
ast_data = []

# js_dataset 대신 downloads 폴더에서 모든 JavaScript 파일을 탐색합니다.
filtered = ['./data/benign/npm/TypeScript/tests/baselines/reference/binderBinaryExpressionStress.js']
for root, dirs, files in os.walk("./data/benign/npm"):
    for file in files:
        if file.endswith(".js"):
            file_path = os.path.join(root, file)
            if file_path in filtered:
                continue
            result = process_js_file(file_path, node_types, api_list)
            if result:
                node_counts, api_usage, entropy, max_depth, label = result
                row = [label, file, entropy, max_depth] + [node_counts[node_type] for node_type in node_types] + [api_usage[api] for api in api_list]
                ast_data.append(row)


csv_file = "js_ast_analysis_benign.csv"
headers = ['Label', 'Filename', 'Entropy', 'MaxDepth'] + node_types + api_list
write_to_csv(ast_data, headers, csv_file)
