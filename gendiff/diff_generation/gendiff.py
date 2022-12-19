import itertools

from gendiff.diff_generation.files_parser import get_data


def generate_diff(file_path1, file_path2):
    data1 = get_data(file_path1)
    data2 = get_data(file_path2)

    replacer = ' '
    spaces_count = 2
    lines = []
    indent = replacer * spaces_count

    all_keys = sorted(set(data1.keys()).union(set(data2.keys())), key=lambda x: x.lower())

    for key in all_keys:
        if key not in data2:
            lines.append(f'{indent}- {key}: {str(data1[key]).lower()}')
        elif key not in data1:
            lines.append(f'{indent}+ {key}: {str(data2[key]).lower()}')
        elif data1[key] == data2[key]:
            lines.append(f'{indent}  {key}: {str(data2[key]).lower()}')
        else:
            lines.append(f'{indent}- {key}: {str(data1[key]).lower()}')
            lines.append(f'{indent}+ {key}: {str(data2[key]).lower()}')

    diff = itertools.chain("{", lines, "}")
    return '\n'.join(diff)
