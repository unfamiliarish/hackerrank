def diagonalDifference(matrix):
    """
    arr is nxn matrix
    """
    n = len(matrix)
    max_index = n - 1

    primary_sum = secondary_sum = 0
    for i in range(n):
        opp_index = max_index - i

        primary_sum += matrix[i][i]
        secondary_sum += matrix[i][opp_index]

    abs_diff = abs(primary_sum - secondary_sum)
    return abs_diff


matrix = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]

assert diagonalDifference(matrix) == 15
