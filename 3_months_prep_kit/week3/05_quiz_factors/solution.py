def get_count_valid_nums(smalls: list, bigs: list):
    smalls = sorted(smalls)
    bigs = sorted(bigs)

    count = 0
    for i in range(smalls[-1], bigs[0] + 1, smalls[-1]):
        multiplies = True
        divides = True

        for num in smalls:
            if i % num != 0:
                multiplies = False

        for num in bigs:
            if num % i != 0:
                divides = False

        if multiplies and divides:
            count += 1

    return count


assert get_count_valid_nums([2, 3, 6], [24, 36]) == 2
