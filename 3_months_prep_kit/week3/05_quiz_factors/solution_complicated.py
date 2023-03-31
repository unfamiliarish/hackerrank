# from this point, i'm pausing
# this problem is listed as easy, and the way i am approaching it, 
# is far from easy

from collections import defaultdict
from math import ceil, sqrt,


def get_factors(num):
    if num <= 0:
        raise ValueError(f"Invalid number to factor: {num}")
    if num <= 2:
        return [num]

    max_factor = ceil(sqrt(num))
    for n in range(2, max_factor + 1):
        if num % n == 0:
            return [n] + get_factors(num // n)

    return [num]


def get_nums_dict(nums):
    dict = defaultdict(int)
    for num in nums:
        dict[num] += 1
    return dict


import numpy


def get_multiple_and_extras(nums):
    required = defaultdict(int)
    extras = defaultdict(int)

    for num in nums[::-1]:
        factors = get_factors(num)
        factors_dict = get_nums_dict(factors)

        for factor in factors_dict.keys():  # i.e. factors
            factor_count = factors_dict[factor]
            required_count = required[factor]

            diff = required_count - factor_count
            # breakpoint()
            if diff > 0:
                extras[factor] += diff
            elif diff < 0:
                required[factor] += abs(diff)
                extras[factor] += factor_count - abs(diff)
            else:
                extras[factor] += factor_count

    base_num = numpy.prod([k * v for k, v in required.items()])

    extras_all = []
    for k, v in extras.items():
        extras_all += [k] * v

    breakpoint()
    return base_num, extras_all


def requrse_nums(base_num, extras):
    pass


def getTotalX(small_arr, big_arr):
    pass


assert get_factors(12) == [2, 2, 3]
assert get_factors(36) == [2, 2, 3, 3]
assert get_factors(7) == [7]


assert get_multiple_and_extras([2, 3, 7, 21]) == (42, [3, 7])

# assert getTotalX([2, 6], [24, 36]) == 2
