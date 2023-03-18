import numpy as np


def flippingMatrix(matrix) -> int:
    flattened = [num for row in matrix for num in row]
    sorted_nums = sorted(flattened)

    n = len(matrix) // 2
    max = sum(sorted_nums[n:])

    breakpoint()
    return max


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
