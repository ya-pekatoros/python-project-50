def get_value_spelling(value):
    if not isinstance(value, dict):
        if value is None:
            value_spelling = 'null'
        elif isinstance(value, str):
            value_spelling = f"'{value}'"
        else:
            value_spelling = str(value).lower()
    else:
        value_spelling = '[complex value]'
    return value_spelling


def plain(current_data, property_path=''):  # noqa: C901
    lines = []
    keys_iter = iter(current_data.items())

    for key, value in keys_iter:
        current_value1 = get_value_spelling(value)

        if 'deleted' in key and f'added {key[8:]}' in current_data.keys():
            key, value = next(keys_iter)
            current_value2 = get_value_spelling(value)
            lines.append(f"Property '{property_path}{key[6:]}' was updated. From {current_value1} to {current_value2}")

        elif 'deleted' in key:
            lines.append(f"Property '{property_path}{key[8:]}' was removed")

        elif 'added' in key:
            lines.append(f"Property '{property_path}{key[6:]}' was added with value: {current_value1}")

        elif current_value1 == '[complex value]':
            new_property_path = property_path + key + '.'
            lines.append(f'{plain(value, new_property_path)}')

    return '\n'.join(lines)
