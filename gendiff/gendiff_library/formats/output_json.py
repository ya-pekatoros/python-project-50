import json


def json_file_output(current_data):
    return json.dumps(current_data, indent=2)
