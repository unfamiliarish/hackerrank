def pickingNumbers(nums: list[int]):
    if not nums:
        return 0

    nums = sorted(nums)

    max_length = 1
    length = 1
    min = max = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        if abs(num - min) > 1 or abs(num - max) > 1:
            if max_length < length:
                max_length = length
            length = 1
            min = max = num
        else:
            length += 1

        if num < min:
            min = num
        if num > max:
            max = num

    # check for final subarray
    if max_length < length:
        max_length = length

    return max_length


assert pickingNumbers([98, 3, 99, 1, 97, 2]) == 2
assert pickingNumbers([1, 1, 2, 2, 4, 4, 5, 5, 5]) == 5
assert pickingNumbers([1, 3, 4, 4]) == 3
assert pickingNumbers([4, 6, 5, 3, 3, 1]) == 3
assert pickingNumbers([1, 2, 3]) == 2
assert pickingNumbers([3, 2, 1]) == 2
assert pickingNumbers([]) == 0
assert pickingNumbers([1]) == 1
