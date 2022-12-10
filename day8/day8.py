import os


def get_max(row, val):
    visible = 0
    idx = len(row)
    idx_lst = [x[0] for x in enumerate(row) if x[1] >= val]
    if idx_lst:
        idx = idx_lst[0] + 1
    if idx == len(row):
        if max(row) < val:
            visible = 1

    return idx, visible


def create_matrix(lines):
    matrix = []
    row = 0
    for line in lines:
        line = line.strip()
        tmp = []
        for height in line:
            tmp.append(int(height))

        matrix.append(tmp)
        row += 1
    return matrix


def main():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day8.txt')) as f:
        lines = f.readlines()
        matrix = create_matrix(lines)

    rows = len(matrix)
    cols = len(matrix[0])
    num_edge_trees = 2*cols + 2*(rows - 2)

    print("The matrix is " + str(rows) + "x" + str(cols))
    print("The number of tree on the edge are " + str(num_edge_trees))

    visible = 0
    scenic_val = 0
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            tree = matrix[r][c]
            idx_upper_col, v_tmp = get_max(
                [i[c] for i in matrix[r-1::-1]], tree)
            visible_tmp = v_tmp
            idx_lower_col, v_tmp = get_max(
                [i[c] for i in matrix[r+1:]], tree)
            visible_tmp += v_tmp
            idx_left, v_tmp = get_max(matrix[r][c-1::-1], tree)
            visible_tmp += v_tmp
            idx_right, v_tmp = get_max(matrix[r][(c+1):], tree)
            visible_tmp += v_tmp

            tmp = idx_upper_col * idx_lower_col * \
                idx_left * idx_right
            if tmp > scenic_val:
                scenic_val = tmp

            if (visible_tmp > 0):
                visible += 1

    print("The number of visible trees are " + str(num_edge_trees + visible))
    print("The highest scenic value is: " + str(scenic_val))


if __name__ == "__main__":
    main()
