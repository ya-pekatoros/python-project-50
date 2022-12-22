from gendiff.gendiff_library.find_difference import find_data_differences
from gendiff.gendiff_library.files_parser import get_data
from gendiff.gendiff_library.formats import stylish, plain


def generate_diff(file_path1, file_path2, format_name):

    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    differences = find_data_differences(data1, data2)

    if format_name == 'stylish':
        format_name = stylish
    elif format_name == 'plain':
        format_name = plain

    return format_name(differences)
