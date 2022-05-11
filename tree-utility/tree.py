import os
import argparse
import sys


def init_parser():
    parser = argparse.ArgumentParser(
        prog='tree',
        description='unix-like tree utility'
    )
    parser.add_argument(
        'dirs',
        action='extend',
        nargs='*',
        help='List of directories to tree'
    )
    return parser


def main():
    arg_parser = init_parser()
    args = arg_parser.parse_args(sys.argv[1:])
    tree(args.dirs)


def tree(dirs):
    if len(dirs) == 0:
        dir_num, files_num, result = list_dir()
        print(result)
        print(str(dir_num) + ' directories, ' + str(files_num) + ' files')

    i = 0
    last_id = len(dirs)
    for directory in dirs:
        dir_num, files_num, result = list_dir(directory)
        print(result + str(dir_num) + ' directories, ' + str(files_num) + ' files')
        if i != last_id - 1:
            print()
        i += 1


def list_dir(current_path='.', depth=0, dir_num=0, files_num=0, result='', prefix=''):
    if current_path[:2] != './' or current_path[:1] != '/':
        current_path = './' + current_path
    dir_list = sorted(os.listdir(current_path))

    i = 0
    last_id = len(dir_list) - 1
    for current_object in dir_list:

        result += prefix
        next_prefix = prefix

        if i != last_id:
            result += '├── '
            next_prefix += '│   '
        else:
            result += '└── '
            next_prefix += '    '

        result += current_object + '\n'

        if '.' not in current_object:
            dir_num += 1
            dir_num, files_num, result = list_dir(
                current_path + '/' + current_object,
                depth + 1,
                dir_num,
                files_num,
                result,
                next_prefix
            )
        else:
            files_num += 1

        i += 1

    return dir_num, files_num, result


if __name__ == '__main__':
    main()
