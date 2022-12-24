def find_data_differences(data1, data2, differences=None):  # noqa: C901

    if differences is None:
        differences = {}

    all_keys = sorted(set(data1.keys()) | (set(data2.keys())))

    for key in all_keys:
        if key not in data2:
            differences.setdefault(f'deleted {key}', data1[key])
        elif key not in data1:
            differences.setdefault(f'added {key}', data2[key])
        elif data1[key] == data2[key]:
            differences.setdefault(key, data2[key])
        else:
            if not isinstance(data1[key], dict) or not isinstance(data2[key], dict):
                differences.setdefault(f'deleted {key}', data1[key])
                differences.setdefault(f'added {key}', data2[key])
            else:
                differences.setdefault(key, find_data_differences(data1[key], data2[key]))

    return differences
