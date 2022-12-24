import json


def json_file_output(current_data, filepath="gendiff_output.json"):  # noqa: C901
    with open(filepath, "w") as output_file:
        output_file.write(json.dumps(current_data, indent=2))
    return
