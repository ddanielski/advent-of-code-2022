import re
import os


def get_moves(lines):
    reached_col_idx = False
    num_repeat = []
    to = []
    fr = []
    for line in lines:
        tmp = re.findall(r'\d+', line)
        if tmp and reached_col_idx:
            num_repeat.append(int(tmp[0]))
            fr.append(tmp[1])
            to.append(tmp[2])
        if tmp and not reached_col_idx:
            idx = tmp
            reached_col_idx = True
    return [num_repeat, fr, to, idx]


def get_boxes(lines, num_col):
    d = {}
    for i in range(0, num_col):
        d[str(i + 1)] = []

    for line in lines:
        tmp = line.replace("    ", "[0]")
        tmp = re.findall('\[(.*?)\]', tmp)
        if len(tmp) == num_col:
            for i in range(0, num_col):
                if tmp[i] != "0":
                    d[str(i + 1)].append(tmp[i])

    return d


def get_top_boxes(box_list, num_col):
    tmp = ""
    for i in range(0, num_col):
        tmp += box_list[str(i + 1)][0]

    return tmp


def main():
    crane = 2
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day5.txt')) as f:
        all_lines = [line for line in f]
        [num_repeat, fr, to, idx] = get_moves(all_lines)
        boxes = get_boxes(all_lines, len(idx))

    num_orders = len(num_repeat)

    for i in range(0, num_orders):
        if crane == 1:
            for __ in range(0, num_repeat[i]):
                boxes[to[i]].insert(0, boxes[fr[i]].pop(0))
        elif crane == 2:
            boxes[to[i]] = boxes[fr[i]][:num_repeat[i]] + boxes[to[i]]
            del boxes[fr[i]][:num_repeat[i]]

    print("The top boxes are: " + get_top_boxes(boxes, len(idx)))


if __name__ == "__main__":
    main()
