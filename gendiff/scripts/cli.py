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
    args.first_file = current_dir + '/' + args.first_file
    args.second_file = current_dir + '/' + args.second_file
    return args


def form_output():
    parser = parse_args(sys.argv[1:])
    diff = generate_diff(parser.first_file, parser.second_file, parser.format)
    print(diff)
    return diff
