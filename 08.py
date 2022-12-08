def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end="")
        print("")


def sum_column(matrix, column):
    total = 0
    for row in range(len(matrix)):
        total += matrix[row][column]
    return total


with open('input8.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    matrix = []

    for line in lines:
        line = line.strip()

        tree_row = []
        for tree in line:
            tree_row.append(int(tree))

        matrix.append(tree_row)

    visible_trees = 0
    visible_trees += (len(matrix) + len(matrix) + len(matrix[0]) + len(matrix[0]) - 4)

    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            actual = matrix[i][j]

            max_line_left = max(matrix[i][:j])
            max_line_right = max(matrix[i][j+1:])
            
            column = [matrix[row][j] for row in range(len(matrix))]
            max_column_top = max(column[:i])
            max_column_bottom = max(column[i+1:])

            if (actual > max_line_left 
                or actual > max_line_right 
                or actual > max_column_bottom 
                or actual > max_column_top):
                visible_trees += 1

    print(visible_trees)
