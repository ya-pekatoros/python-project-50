from pathlib import Path
from gendiff.gendiff_library.make_output import generate_diff
from gendiff.gendiff_library.files_parser import get_data
from gendiff.gendiff_library.find_difference import find_data_differences

def get_fixture_path(file_name):
    current_dir = Path('.').absolute()
    print(current_dir)
    return current_dir / 'tests/fixtures' / file_name

def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

parsing_file1_flat_results = {
    "host": "hexlet.io", "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False,
}

parsing_file1_nested_results = {
    'common': {
        'setting1': 'Value 1',
        'setting2': 200,
        'setting3': True,
        'setting6': {
            'key': 'value',
            'doge': {
                'wow': ''
            }
        }
    }, 
    'group1': {
        'baz': 'bas',
        'foo': 'bar',
        'nest': {
            'key': 'value'
        }
    },
    'group2': {
        'abc': 12345,
        'deep': {
            'id': 45
        }
    }
}

find_differences_result_flat = {
    'deleted follow': False,
    'host': 'hexlet.io',
    'deleted proxy': '123.234.53.22',
    'deleted timeout': 50,
    'added timeout': 20,
    'added verbose': True
}

find_differences_result_nested = {
    'common': {
        'added follow': False,
        'setting1': 'Value 1',
        'deleted setting2': 200,
        'deleted setting3': True,
        'added setting3': None,
        'added setting4': 'blah blah',
        'added setting5': {
            'key5': 'value5'
        },
        'setting6': {
            'doge': {
                'deleted wow': '',
                'added wow': 'so much'
            },
            'key': 'value',
            'added ops': 'vops'
        }
    },
    'group1': {
        'deleted baz': 'bas',
        'added baz': 'bars',
        'foo': 'bar',
        'deleted nest': {
            'key': 'value'
        },
        'added nest': 'str'
    },
    'deleted group2':{
        'abc': 12345,
        'deep': {
            'id': 45
        }
    },
    'added group3': {
        'deep': {
            'id': {
                'number': 45
            }
        },
        'fee': 100500
    }
}


expected_data_stylish = read(get_fixture_path('expectations_stylish.txt')).rstrip().split('\n\n\n\n')


def test_get_data_json_flat():
    assert get_data(get_fixture_path('file1.json')) == parsing_file1_flat_results


def test_get_data_yaml_flat():
    assert get_data(get_fixture_path('file1.yml')) == parsing_file1_flat_results


def test_get_data_json_nested():
    assert get_data(get_fixture_path('nested_file1.json')) == parsing_file1_nested_results


def test_get_data_yaml_nested():
    assert get_data(get_fixture_path('nested_file1.yaml')) == parsing_file1_nested_results


def test_find_data_differences_flat():
    data1 = get_data(get_fixture_path('file1.json'))
    data2 = get_data(get_fixture_path('file2.json'))
    
    assert find_data_differences(data1, data2) == find_differences_result_flat

    data1 = get_data(get_fixture_path('file1.yml'))
    data2 = get_data(get_fixture_path('file2.yml'))
    
    assert find_data_differences(data1, data2) == find_differences_result_flat


def test_find_data_differences_nested():
    data1 = get_data(get_fixture_path('nested_file1.json'))
    data2 = get_data(get_fixture_path('nested_file2.json'))
    
    assert find_data_differences(data1, data2) == find_differences_result_nested

    data1 = get_data(get_fixture_path('nested_file1.yaml'))
    data2 = get_data(get_fixture_path('nested_file2.yaml'))
    
    assert find_data_differences(data1, data2) == find_differences_result_nested


def test_gendiff_flat_json():
    assert generate_diff(get_fixture_path('file1.json'), get_fixture_path('file2.json'), 'stylish') == expected_data_stylish[0]


def test_gendiff_flat_yaml():
    assert generate_diff(get_fixture_path('file1.yml'), get_fixture_path('file2.yml'), 'stylish') == expected_data_stylish[0]


def test_gendiff_nested_json():
    assert generate_diff(get_fixture_path('nested_file1.json'), get_fixture_path('nested_file2.json'), 'stylish') == expected_data_stylish[1]


def test_gendiff_nested_yaml():
    assert generate_diff(get_fixture_path('nested_file1.yaml'), get_fixture_path('nested_file2.yaml'), 'stylish') == expected_data_stylish[1]


data1 = get_data(get_fixture_path('file1.yml'))
data2 = get_data(get_fixture_path('file2.yml'))
    
print(find_data_differences(data1, data2))

data1 = get_data(get_fixture_path('nested_file1.json'))
data2 = get_data(get_fixture_path('nested_file2.json'))
    
print(find_data_differences(data1, data2))