import os


def main():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))

    with open(os.path.join(__location__, 'day8_sample.txt')) as f:
        lines = f.readlines()
        matrix = []
        row = 0
        for line in lines:
            line = line.strip()
            tmp = []
            for height in line:
                tmp.append(int(height))

            matrix.append(tmp)
            row += 1

    rows = len(matrix)
    cols = len(matrix[0])
    num_edge_trees = 2*cols + 2*(rows - 2)

    print("The matrix is " + str(rows) + "x" + str(cols))
    print("The number of tree on the edge are " + str(num_edge_trees))

    for r in range(1, rows-1):
        for c in range(1, cols-1):
            pass


if __name__ == "__main__":
    main()
