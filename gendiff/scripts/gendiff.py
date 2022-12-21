#! /usr/bin/env python3
import argparse
from pathlib import Path
from gendiff.gendiff_library.make_output import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format", help="set format of output, available formatters: stylish", default='stylish')
    parser.add_argument(
        "first_file",
        type=lambda p: Path(p).absolute()
    )
    parser.add_argument(
        "second_file",
        type=lambda p: Path(p).absolute()
    )
    args = parser.parse_args()

    if args.format != 'stylish':
        return print('Choose the corrent formatter')

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
