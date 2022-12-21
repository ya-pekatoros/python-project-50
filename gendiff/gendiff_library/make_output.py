from gendiff.gendiff_library.find_difference import find_data_differences
from gendiff.gendiff_library.files_parser import get_data
from gendiff.gendiff_library.output_stylish import stylish


def generate_diff(file_path1, file_path2, formatter):

    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    differences = find_data_differences(data1, data2)

    if formatter == 'stylish':
        formatter = stylish

    return formatter(differences)
