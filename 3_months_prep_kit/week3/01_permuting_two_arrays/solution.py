def twoArrays(k, A, B):
    # Write your code here
    sorted_A = sorted(A)[::-1]
    sorted_B = sorted(B)

    sums = []
    for i in range(len(A)):
        sums.append(sorted_A[i] + sorted_B[i])

    breakpoint()
    for sum_ in sums:
        if sum_ < k:
            return "NO"
    return "YES"


a_1 = [2, 1, 3]
b_1 = [7, 8, 9]
a_2 = [1, 2, 2, 1]
b_2 = [3, 3, 3, 4]

assert twoArrays(10, a_1, b_1) == "YES"
assert twoArrays(5, a_2, b_2) == "NO"
