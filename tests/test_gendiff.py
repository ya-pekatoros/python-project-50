import os
from gendiff import generate_diff
from gendiff import get_data
from gendiff import find_data_differences
from gendiff.scripts.gendiff import parse_args
from gendiff.scripts.gendiff import form_output

def get_fixture_path(file_name):
    current_dir = os.getcwd()
    return current_dir + '/tests/fixtures/' + file_name


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

PARS_FLAT_EXPECT = {
    "host": "hexlet.io", "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False,
}

PARS_NSTED_EXPECT = {
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

DIFF_FLAT_EXPECT = {
    'deleted follow': False,
    'host': 'hexlet.io',
    'deleted proxy': '123.234.53.22',
    'deleted timeout': 50,
    'added timeout': 20,
    'added verbose': True
}

DIFF_NESTED_EXPECT = {
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


CONS_OUT_EXPECT = read(get_fixture_path('expectations_console.txt')).rstrip().split('\n\n\n\n')


def test_get_data_json_flat():
    assert get_data(get_fixture_path('file1.json')) == PARS_FLAT_EXPECT


def test_get_data_yaml_flat():
    assert get_data(get_fixture_path('file1.yml')) == PARS_FLAT_EXPECT


def test_get_data_json_nested():
    assert get_data(get_fixture_path('nested_file1.json')) == PARS_NSTED_EXPECT


def test_get_data_yaml_nested():
    assert get_data(get_fixture_path('nested_file1.yaml')) == PARS_NSTED_EXPECT


def test_find_data_differences_flat():
    data1 = get_data(get_fixture_path('file1.json'))
    data2 = get_data(get_fixture_path('file2.json'))
    
    assert find_data_differences(data1, data2) == DIFF_FLAT_EXPECT

    data1 = get_data(get_fixture_path('file1.yml'))
    data2 = get_data(get_fixture_path('file2.yml'))
    
    assert find_data_differences(data1, data2) == DIFF_FLAT_EXPECT


def test_find_data_differences_nested():
    data1 = get_data(get_fixture_path('nested_file1.json'))
    data2 = get_data(get_fixture_path('nested_file2.json'))
    
    assert find_data_differences(data1, data2) == DIFF_NESTED_EXPECT

    data1 = get_data(get_fixture_path('nested_file1.yaml'))
    data2 = get_data(get_fixture_path('nested_file2.yaml'))
    
    assert find_data_differences(data1, data2) == DIFF_NESTED_EXPECT


def test_gendiff_flat_json():
    assert generate_diff(get_fixture_path('file1.json'), get_fixture_path('file2.json'), 'stylish') == CONS_OUT_EXPECT[0]


def test_gendiff_flat_yaml():
    assert generate_diff(get_fixture_path('file1.yml'), get_fixture_path('file2.yml'), 'stylish') == CONS_OUT_EXPECT[0]


def test_gendiff_nested_json():
    assert generate_diff(get_fixture_path('nested_file1.json'), get_fixture_path('nested_file2.json'), 'stylish') == CONS_OUT_EXPECT[1]
    assert generate_diff(get_fixture_path('nested_file1.json'), get_fixture_path('nested_file2.json'), 'plain') == CONS_OUT_EXPECT[2]
    assert generate_diff(get_fixture_path('nested_file1.json'), get_fixture_path('nested_file2.json'), 'json') == CONS_OUT_EXPECT[3]

def test_gendiff_nested_yaml():
    assert generate_diff(get_fixture_path('nested_file1.yaml'), get_fixture_path('nested_file2.yaml'), 'stylish') == CONS_OUT_EXPECT[1]
    assert generate_diff(get_fixture_path('nested_file1.yaml'), get_fixture_path('nested_file2.yaml'), 'plain') == CONS_OUT_EXPECT[2]
    assert generate_diff(get_fixture_path('nested_file1.yaml'), get_fixture_path('nested_file2.yaml'), 'json') == CONS_OUT_EXPECT[3]


def test_main_ouput():
    expectations = generate_diff(get_fixture_path('nested_file1.json'), get_fixture_path('nested_file2.json'), 'json')
    test = form_output(request=['-fjson', get_fixture_path('nested_file1.json'), get_fixture_path('nested_file2.json')])
    assert test == expectations


def test_parser():
    parser = parse_args(request=['-fplain', get_fixture_path('file1.yml'), get_fixture_path('file2.yml')])
    assert parser.first_file == get_fixture_path('file1.yml')
    assert parser.second_file == get_fixture_path('file2.yml')
    assert parser.format == 'plain'
    assert parse_args(request=['-ftest', get_fixture_path('file1.yml'), get_fixture_path('file2.yml')]) == 'Choose the corrent formatter'
