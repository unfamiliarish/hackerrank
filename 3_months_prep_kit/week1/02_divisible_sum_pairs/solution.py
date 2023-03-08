from collections import defaultdict
import math


def count_repeat_pairs(total_count: int) -> int:
    return int(total_count * (total_count + 1) / 2)


def recurse_sum_pairs(
    numbers: dict[int, int], remaining_keys: set, divisor: int
) -> int:
    if len(remaining_keys) == 0:
        return 0

    count = 0
    key = remaining_keys.pop()
    if numbers[key] > 1:
        if (key + key) % divisor == 0:
            num_count = numbers[key]
            count += count_repeat_pairs(num_count - 1)

    for r_key in remaining_keys:
        if (key + r_key) % divisor == 0:
            count += numbers[key] * numbers[r_key]

    count += recurse_sum_pairs(numbers, remaining_keys, divisor)

    return count


def remove_zeros(array) -> list[int]:
    return [el for el in array if el != 0]


def divisibleSumPairs_old(arr_len, divisor, array):
    if divisor == 0 or divisor == math.inf:
        return 0

    numbers = defaultdict(int)
    array = remove_zeros(array)

    for val in array:
        numbers[val] += 1

    result = recurse_sum_pairs(numbers, set(numbers.keys()), divisor)
    return result


def divisibleSumPairs(arr_len, divisor, array):
    if divisor == 0 or divisor == math.inf:
        return 0

    count = 0
    for i in range(arr_len):
        for j in range(i + 1, arr_len):
            summand = array[i] + array[j]
            if summand and summand % divisor == 0:
                count += 1

    return count


assert divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6]) == 3
assert divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2]) == 5
assert divisibleSumPairs(3, 1, [0, 0, 0]) == 0
assert divisibleSumPairs(3, 2, [-3, 5, 1, -2]) == 3
assert divisibleSumPairs(2, 0, [3, 2]) == 0
assert divisibleSumPairs(5, math.inf, [1, 2, 3, 4, 5]) == 0
assert divisibleSumPairs(3, 0, []) == 0
assert divisibleSumPairs(2, 3, [3, 3]) == 1
assert divisibleSumPairs(3, 3, [3, 3, 3]) == 3
assert divisibleSumPairs(5, 3, [3, 3, 3, 3, 3]) == 10


assert (
    divisibleSumPairs(
        100,
        22,
        [
            43,
            95,
            51,
            55,
            40,
            86,
            65,
            81,
            51,
            20,
            47,
            50,
            65,
            53,
            23,
            78,
            75,
            75,
            47,
            73,
            25,
            27,
            14,
            8,
            26,
            58,
            95,
            28,
            3,
            23,
            48,
            69,
            26,
            3,
            73,
            52,
            34,
            7,
            40,
            33,
            56,
            98,
            71,
            29,
            70,
            71,
            28,
            12,
            18,
            49,
            19,
            25,
            2,
            18,
            15,
            41,
            51,
            42,
            46,
            19,
            98,
            56,
            54,
            98,
            72,
            25,
            16,
            49,
            34,
            99,
            48,
            93,
            64,
            44,
            50,
            91,
            44,
            17,
            63,
            27,
            3,
            65,
            75,
            19,
            68,
            30,
            43,
            37,
            72,
            54,
            82,
            92,
            37,
            52,
            72,
            62,
            3,
            88,
            82,
            71,
        ],
    )
    == 216
)


assert (
    divisibleSumPairs(
        100,
        40,
        [
            13,
            91,
            5,
            100,
            5,
            12,
            5,
            79,
            99,
            87,
            59,
            65,
            62,
            73,
            93,
            73,
            63,
            65,
            59,
            46,
            67,
            35,
            22,
            55,
            50,
            53,
            38,
            79,
            75,
            44,
            95,
            53,
            5,
            73,
            44,
            94,
            95,
            21,
            60,
            2,
            32,
            48,
            72,
            13,
            91,
            74,
            79,
            99,
            17,
            31,
            53,
            20,
            88,
            17,
            54,
            47,
            56,
            79,
            23,
            49,
            95,
            81,
            9,
            50,
            12,
            20,
            45,
            82,
            44,
            82,
            93,
            15,
            73,
            51,
            65,
            96,
            4,
            77,
            37,
            41,
            30,
            11,
            65,
            100,
            62,
            51,
            64,
            48,
            12,
            11,
            68,
            81,
            46,
            37,
            10,
            46,
            75,
            82,
            21,
            23,
        ],
    )
) == 109
