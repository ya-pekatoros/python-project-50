import json
import yaml

try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader


def get_data(file_path):
    if str(file_path)[-5:] == '.json':
        data = json.load(open(file_path))

    if str(file_path)[-5:] == '.yaml' or str(file_path)[-4:] == '.yml':
        with open(file_path, 'r') as f:
            data = yaml.load(f.read(), Loader=Loader)

    return data
