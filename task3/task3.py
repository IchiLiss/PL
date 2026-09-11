import sys
import json

def load_values(path):
    with open(path, encoding='utf-8') as f:
        data = json.load(f)
    return {item['id']: item['value'] for item in data['values']}

def fill_values(node, values):
    if isinstance(node, dict):
        if 'id' in node and 'value' in node:
            node['value'] = values.get(node['id'], '')
        for key, val in node.items():
            if key != 'value':
                fill_values(val, values)
    elif isinstance(node, list):
        for item in node:
            fill_values(item, values)

def main():
    if len(sys.argv) != 4:
        print("Usage: task3.py values.json tests.json report.json")
        return
    values_path, tests_path, report_path = sys.argv[1:4]
    values = load_values(values_path)
    with open(tests_path, encoding='utf-8') as f:
        tests = json.load(f)
    fill_values(tests, values)
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(tests, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
