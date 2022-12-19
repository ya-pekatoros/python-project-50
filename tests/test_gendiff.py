from pathlib import Path
from gendiff.diff_generation.gendiff import generate_diff

def get_fixture_path(file_name):
    current_dir = Path('.').absolute()
    print(current_dir)
    return current_dir / 'tests/fixtures' / file_name

def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result

expected_data = read(get_fixture_path('expectations.txt')).rstrip()

def test_gendiff():
    assert generate_diff(get_fixture_path('file1.json'), get_fixture_path('file2.json')) == expected_data