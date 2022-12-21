import itertools


def stylish(current_data, depth=0):  # noqa: C901
    replacer = ' '
    spaces_count = 4
    lines = []

    if not isinstance(current_data, dict):
        if current_data is None:
            return 'null'
        if isinstance(current_data, str):
            return current_data
        return str(current_data).lower()

    deep_indent_size = depth + spaces_count
    current_indent = replacer * depth
    lines = []
    for key, value in current_data.items():
        if 'deleted' in key:
            deep_indent = replacer * (deep_indent_size - 2)
            key_output = f'- {key[8:]}'
        elif 'added' in key:
            deep_indent = replacer * (deep_indent_size - 2)
            key_output = f'+ {key[6:]}'
        else:
            deep_indent = replacer * deep_indent_size
            key_output = key
        lines.append(f'{deep_indent}{key_output}: {stylish(value, deep_indent_size)}')
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
