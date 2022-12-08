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

    scenic_score = 0
    temp_score = 0

    for line in lines:
        line = line.strip()

        tree_row = []
        for tree in line:
            tree_row.append(int(tree))

        matrix.append(tree_row)


    for i in range(1, len(matrix) -1):
        for j in range(1, len(matrix[i]) - 1):
            actual = matrix[i][j]

            line_left = matrix[i][:j]

            line_right = matrix[i][j+1:]
            
            column = [matrix[row][j] for row in range(len(matrix))]
            column_top = column[:i]
            column_bottom = column[i+1:]

            left_score = 0
            right_score = 0
            top_score = 0
            bottom_score = 0
            
            for tree in line_left[::-1]:
                left_score += 1
                if tree >= actual:
                    break

            for tree in line_right:
                right_score += 1
                if tree >= actual:
                    break

            for tree in column_top[::-1]:
                top_score += 1
                if tree >= actual:
                    break

            for tree in column_bottom:
                bottom_score += 1
                if tree >= actual:
                    break

            temp_score = left_score * right_score * top_score * bottom_score

            if temp_score > scenic_score:
                scenic_score = temp_score

            temp_score = 0

    print(scenic_score)
