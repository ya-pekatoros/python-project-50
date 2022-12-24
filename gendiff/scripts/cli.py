import argparse
import os
import sys
from gendiff import generate_diff


def parse_args(request):

    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format", help='set format of output, available parameters: [stylish|plain|json]', default='stylish')  # noqa: E501

    parser.add_argument(
        "first_file",
        type=str
    )
    parser.add_argument(
        "second_file",
        type=str
    )
    args = parser.parse_args(request)
    current_dir = os.getcwd()
    available_formats = ['stylish', 'plain', 'json']
    if not args.first_file.startswith('/'):
        args.first_file = current_dir + '/' + args.first_file
    if not args.second_file.startswith('/'):
        args.second_file = current_dir + '/' + args.second_file

    if args.format not in available_formats:
        allert = 'Choose the corrent formatter'
        print(allert)
        return allert

    return args


def form_output(request=''):
    if request == '':
        request = sys.argv[1:]
    parser = parse_args(request)
    diff = generate_diff(parser.first_file, parser.second_file, parser.format)
    print(diff)
    return diff
