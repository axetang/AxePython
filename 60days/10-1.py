import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(description='工作目录中文件名后缀修改')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str,
                        nargs=1, help='修改文件名的目录')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str,
                        nargs=1, help='原来的后缀')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str,
                        nargs=1, help='新的后缀')
    return parser


def batch_rename(work_dir, old_ext, new_ext):
    print()
    for file_name in os.listdir(work_dir):
        split_file = os.path.splitext(file_name)
        # print(split_file)
        file_ext = split_file[1]
        if old_ext == file_ext:
            new_file = split_file[0]+new_ext
            os.rename(os.path.join(work_dir, file_name),
                      os.path.join(work_dir, new_file))

    print(os.listdir(work_dir))


def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    print(args)

    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    if old_ext[0] != '.':
        old_ext = "."+old_ext
    new_ext = args['new_ext'][0]
    if new_ext[0] != '.':
        new_ext = "."+new_ext

    batch_rename(work_dir, old_ext, new_ext)


main()
