from collections import defaultdict
import os


def part1(file_sz, const):
    sum_files = 0
    for sz in file_sz.values():
        if sz <= const:
            sum_files += sz
    return sum_files


def part2(file_sz, const):
    files_sz = []
    for sz in file_sz.values():
        if sz >= const:
            files_sz.append(sz)
    return min(files_sz)


def main():
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day7.txt')) as f:
        lines = f.readlines()
        file_sz = defaultdict(int)
        dir = []

        for line in lines:
            line = line.strip()
            if "$ cd" in line:
                # We want the third field.  We can't separate with "cd ", as can be a file name
                dir_name = line.split()[2]
                if ".." in line:
                    dir.pop()
                elif "/" in dir_name:
                    dir.append("/")
                else:
                    dir.append(
                        f"{dir[-1]}{'/' if dir[-1] != '/' else ''}{dir_name}")
            elif "dir" or "$" not in line:
                file_size = line.split(" ", 1)[0]
                if file_size.isdigit():
                    for p in dir:
                        file_sz[p] += int(file_size)

    print("Part I: The sum of all the dir with at most 100k is " +
          str(part1(file_sz, 100000)))
    print("Part II: You need to remove the directory of size " +
          str(part2(file_sz, 30000000 - (70000000 - file_sz['/']))))


if __name__ == "__main__":
    main()
