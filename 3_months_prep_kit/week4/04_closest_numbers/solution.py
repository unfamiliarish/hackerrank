def zip_arr(arr):
    # zipped = []
    # for i in range(1, len(arr)):
    #     zipped.append((arr[i - 1], arr[i]))
    # return zipped

    # using a built-in method
    return list(zip(arr[:-1], arr[1:]))


def closestNumbers(arr):
    # Write your code here
    sorted_arr = sorted(arr)
    if len(sorted_arr) == 2:
        return sorted_arr

    smallest = float("inf")  # infinity
    smallest_pairs = []
    for pair in zip_arr(sorted_arr):
        el1, el2 = pair
        difference = abs(el1 - el2)
        if difference == smallest:
            smallest_pairs += [el1, el2]
        if difference < smallest:
            smallest = difference
            smallest_pairs = [el1, el2]

    # flat_pairs = [el for pair in smallest_pairs for el in pair]
    return smallest_pairs


assert zip_arr([1, 2, 3]) == [(1, 2), (2, 3)]


test_array = [
    -20,
    -3916237,
    -357920,
    -3620601,
    7374819,
    -7330761,
    30,
    6246457,
    -6461594,
    266854,
]
test_array_2 = test_array + [-520, -470]

assert closestNumbers([3, 1]) == [1, 3]
assert closestNumbers([5, 2, 3, 4, 1]) == [1, 2, 2, 3, 3, 4, 4, 5]
assert closestNumbers(test_array) == [-20, 30]
assert closestNumbers(test_array_2) == [-520, -470, -20, 30]
