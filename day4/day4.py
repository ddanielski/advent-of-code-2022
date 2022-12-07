import re
import os


def main():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day4.txt')) as f:
        num_subsets = 0
        num_contains = 0
        for line in f:
            ids = [int(i) for i in re.findall(r'\d+', line)]
            a = set(range(ids[0], ids[1] + 1))
            b = set(range(ids[2], ids[3] + 1))
            if len(a) >= len(b):
                if b.issubset(a):
                    num_subsets += 1
                if (a & b):
                    num_contains += 1
            else:
                if a.issubset(b):
                    num_subsets += 1
                if (a & b):
                    num_contains += 1

        print("The number of fully contained pairs are: " + str(num_subsets))
        print("The number of pairs that overlap are: " + str(num_contains))


if __name__ == "__main__":
    main()
