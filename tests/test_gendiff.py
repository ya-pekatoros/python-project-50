from gendiff.diff_generation.gendiff import generate_diff

link1 = '/home/ypekatoros/python-projects/hexlet/second-project/tests/file1.json'
link2 = '/home/ypekatoros/python-projects/hexlet/second-project/tests/file2.json'

def test_gendiff():
    assert generate_diff(link1, link2) == "{\n  - follow: false\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n  + timeout: 20\n  + verbose: true\n}"