import os
import re


def get_dir_info(lines):
    dir_tree = {}
    file = {}
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
                if dir_name is not dir_tree:
                    dir_tree[dir_name] = []
                    file[dir_name] = []
                tmp_dir.append(dir_name)
        elif "dir" or "$" not in line:
            file_size = line.split(" ", 1)[0]
            if file_size.isdigit():
                file[tmp_dir[-1]].append(int(file_size))

    print(file)
    print(dir_tree)
    return dir_tree, file


def main():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day7_sample.txt')) as f:
        lines = f.readlines()
        dir_tree, file_sz = get_dir_info(lines)
        dir_sz = {}
        for dir in dir_tree:
            dir_sz[dir] = sum(file_sz[dir])

        delta = 1
        while(delta > 0):
            for dir, sub_dir in dir_tree.items():
                if sub_dir:
                    dir_sz[dir] += sum(dir_sz[sub_dir])
            delta = 0

        print(dir_sz)


if __name__ == "__main__":
    main()
