import numpy as np


def flippingMatrix(matrix) -> int:
    # Write your code here
    # og_matrix = np.array(matrix)
    np_matrix = np.array(matrix)

    n = len(np_matrix) // 2
    # swap lower rows
    for i in range(n):
        if sum(np_matrix[i + n][0:n]) > sum(np_matrix[i + n][n:]):
            np_matrix[i + n] = np_matrix[i + n][::-1]
    # swap right cols
    for j in range(n):
        if sum(np_matrix[n:, j + n]) > sum(np_matrix[:n, j + n]):
            np_matrix[:, j + n] = np_matrix[:, j + n][::-1]
    # swap upper rows
    for i in range(n):
        if sum(np_matrix[i][n:]) > sum(np_matrix[i][0:n]):
            np_matrix[i] = np_matrix[i][::-1]

    # get upper left sum
    upper_left_sum = sum(sum(np_matrix[:n, :n]))
    # breakpoint()
    return upper_left_sum


matrix_0 = [[1, 2], [3, 4]]
matrix_1 = [
    [112, 42, 83, 119],
    [56, 125, 56, 49],
    [15, 78, 101, 43],
    [62, 98, 114, 108],
]
matrix_2 = [
    [107, 54, 128, 15],
    [12, 75, 110, 138],
    [100, 96, 34, 85],
    [75, 15, 28, 112],
]

# assert flippingMatrix(matrix_0) == 4
# assert flippingMatrix(matrix_1) == 414
assert flippingMatrix(matrix_2) == 488
