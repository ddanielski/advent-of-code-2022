import os
import re


def main():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day7_sample.txt')) as f:
        lines = f.readlines()
        dir_tree = {}
        files = {}
        tmp_dir = []
        for line in lines:
            if "cd" in line:
                dir_name = line.split("cd ", 1)[1]
                if ".." in dir_name:
                    tmp_dir.pop()
                else:
                    dir_name = dir_name.rstrip()
                    if tmp_dir:
                        dir_tree[tmp_dir[-1]].append(dir_name)
                    tmp_dir.append(dir_name)
                    dir_tree[dir_name] = []
        print(dir_tree)


if __name__ == "__main__":
    main()
