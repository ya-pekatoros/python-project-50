import json
import yaml


def get_data(file_path):
    if file_path.endswith(".json"):
        data = json.load(open(file_path))
    elif file_path.endswith(".yaml") or file_path.endswith(".yml"):
        with open(file_path, 'r') as f:
            data = yaml.safe_load(f.read())
    else:
        raise AssertionError(f"wrong file format (file-path = {file_path})")

    return data
