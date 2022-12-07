import os


def separate_ruckstack(objects):
    str_sz = len(objects)
    if str_sz % 2 != 0:
        print("ERROR: It is an odd number")
        return [0, 0]

    half_sz = int(str_sz * 0.5)
    return [objects[:half_sz], objects[half_sz:]]


def get_const(character):
    return 38 if character.isupper() else 96


def part1(lines):
    priority = []
    for line in lines:
        [first, second] = separate_ruckstack(line.strip())
        letter = set(first) & set(second)
        priority.append([ord(i) - get_const(i) for i in letter])
    return priority


def part2(lines):
    groups = 3
    total_lines = len(lines)
    if total_lines % groups != 0:
        print("Not divisible by three. Can't complete part 2")
        return
    num_group = int(total_lines / groups)
    priority = []
    x = 0
    for i in range(0, num_group):
        letter = set(lines[x]) & set(lines[x+1]) & set(lines[x+2])
        priority.append([ord(i) - get_const(i) for i in letter])
        x += 3
    return priority


def sum_set(set_var):
    total_sum = 0
    for i in set_var:
        for value in i:
            total_sum += value
    return total_sum


def main():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day3.txt')) as f:
        all_lines = [line.rstrip() for line in f]
        priority_list = part1(all_lines)
        print("Part I:")
        print("The total priority is: " +
              str(sum_set(priority_list)))

        priority_list = part2(all_lines)
        print("Part II:")
        print("The total badge priority is: " +
              str(sum_set(priority_list)))


if __name__ == "__main__":
    main()
