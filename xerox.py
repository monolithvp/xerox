# coding=utf-8
"""
Xerox.py

Use this script to copy files from source to destination.
You can filter specific file extensions or exclude files.

File patters are regular expressions - use https://regex101.com/ to test your patterns.

For example:

filter single file = --filter 'py'
filter multiple files = --filter 'py|css'
filter by file extension = --filter 'py$|css$'

"""

import argparse
import re
import os
import shutil


def main(args):
    source = args.src
    destination = args.dst
    file_filter = args.filter
    file_exclude = args.exclude
    test = args.test

    try:
        assert source and destination, 'Please mention both source and destination'

        for dirs, folds, files in os.walk(source):
            for f in files:
                file_path = os.path.join(dirs, f)
                source_file_path = None

                if file_filter and re.search(file_filter, f, flags=re.IGNORECASE):
                    source_file_path = file_path

                if file_exclude and re.search(file_exclude, f, flags=re.IGNORECASE):
                    source_file_path = None

                if source_file_path:
                    dest_file_path = source_file_path.replace(source, destination)
                    print source_file_path, '-->', dest_file_path

                    if not test:
                        dest_dir, _ = os.path.split(dest_file_path)

                        if not os.path.exists(dest_dir):
                            os.makedirs(dest_dir)

                        shutil.copy(source_file_path, dest_file_path)

    except Exception as error:
        print 'Error: ', error.message


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Use this script to copy files")

    parser.add_argument('-s', '--src', type=str, help='Source path')
    parser.add_argument('-d', '--dst', type=str, help='Destination path')
    parser.add_argument('-f', '--filter', type=str, help='Filter file pattern', default=None)
    parser.add_argument('-e', '--exclude', type=str, help='Exclude file pattern', default=None)
    parser.add_argument('-t', '--test', type=bool, help='Print only, do not copy', default=False)
    args = parser.parse_args()

    main(args)
