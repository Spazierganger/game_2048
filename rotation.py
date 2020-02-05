def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    for i in range(int(len(matrix) / 2)):
        for j in range(i, len(matrix) - i - 1):
            matrix[len(matrix) - 1 - j][i], \
            matrix[len(matrix) - 1 - i][len(matrix) - 1 - j], \
            matrix[j][len(matrix) - 1 - i], \
            matrix[i][j] = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j], \
                           matrix[j][len(matrix) - 1 - i], \
                           matrix[i][j], \
                           matrix[len(matrix) - 1 - j][i]
    return matrix


if __name__ == '__main__':
    mat = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12],
           [13, 14, 15, 16]]

    mat1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
    mat = rotate(mat)
    print(mat)
    # trial
    a, b, c, d = range(0, 4)
    a, b, c, d = d, a, b, c
    print(a, b, c, d)
