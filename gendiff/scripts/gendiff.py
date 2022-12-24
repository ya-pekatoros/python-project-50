#! /usr/bin/env python3
import argparse
import os
import sys
from gendiff.make_output import generate_diff


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
    args.first_file = current_dir + '/' + args.first_file
    args.second_file = current_dir + '/' + args.second_file

    if args.format not in available_formats:
        allert = 'Choose the corrent formatter'
        print(allert)
        return allert

    return parser.parse_args(request)


def main():
    parser = parse_args(sys.argv[1:])

    diff = generate_diff(parser.first_file, parser.second_file, parser.format)

    if parser.format == 'json':
        current_dir = os.getcwd()
        print(f"The result of gendiff in located here: {current_dir}/gendiff_output.json")
    else:
        print(diff)


if __name__ == '__main__':
    main()
