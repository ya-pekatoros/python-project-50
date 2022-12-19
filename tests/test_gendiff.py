from pathlib import Path
from gendiff.diff_generation.gendiff import generate_diff
from gendiff.diff_generation.files_parser import get_data

def get_fixture_path(file_name):
    current_dir = Path('.').absolute()
    print(current_dir)
    return current_dir / 'tests/fixtures' / file_name

def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

parsing_file1_results = {
    "host": "hexlet.io", "timeout": 50,
    "proxy": "123.234.53.22",
    "follow": False,
}

expected_data = read(get_fixture_path('expectations.txt')).rstrip()

generate_diff(get_fixture_path('file1.yml'), get_fixture_path('file2.yml'))

def test_get_data():
    assert get_data(get_fixture_path('file1.json')) == parsing_file1_results
    assert get_data(get_fixture_path('file1.yml')) == parsing_file1_results

def test_gendiff():
    assert generate_diff(get_fixture_path('file1.json'), get_fixture_path('file2.json')) == expected_data
    assert generate_diff(get_fixture_path('file1.yml'), get_fixture_path('file2.yml')) == expected_data
