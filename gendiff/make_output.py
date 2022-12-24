from gendiff.find_difference import find_data_differences
from gendiff.files_parser import get_data
from gendiff.formatters import stylish, plain, output_json_format


def generate_diff(file_path1, file_path2, format_name='stylish'):

    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    differences = find_data_differences(data1, data2)

    if format_name == 'stylish':
        format_name = stylish
    elif format_name == 'plain':
        format_name = plain
    elif format_name == 'json':
        format_name = output_json_format

    return format_name(differences)
