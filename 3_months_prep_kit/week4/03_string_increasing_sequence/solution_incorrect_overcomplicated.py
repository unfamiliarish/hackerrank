import math

NO = "NO"


def YES(first_num):
    return f"YES {first_num}"


def split_nums(num_str, step):
    length = len(num_str)
    nums = [num_str[i * step : (i + 1) * step] for i in range(length // step)]
    return nums


def separateNumbers(num_str):
    # Write your code here
    str_length = len(num_str)  # len of the numeric string
    if str_length <= 1:
        print(NO)
        return NO

    longest_step = math.ceil(str_length / 2)
    is_beautiful = False

    for step in range(1, longest_step + 1):
        # breakpoint()

        # get individual nums as strings
        # breakpoint()
        if str_length % 2 == 1 and step > 1:
            for num_firsts in range(1, longest_step):
                len_first_steps = (step) * num_firsts  # steps are one size smaller
                remaining_str = num_str[len_first_steps:]
                if (len(remaining_str) - len_first_steps) % step != 0:
                    continue

                first_nums = [
                    num_str[step * count : step * (count + 1)]
                    for count in range(num_firsts)
                ]
                other_nums = split_nums(remaining_str, step)
                nums = first_nums + other_nums
            # first_num = num_str[0 : step - 1]
            # nums = split_nums(num_str[step - 1 :], step)
            # nums.insert(0, first_num)
        else:
            nums = split_nums(num_str, step)

        breakpoint()
        # skip cases where numbers start with 0
        if any([num[0] == "0" for num in nums]):
            continue

        # check for beautiful numbers
        nums = [int(num) for num in nums]
        if all([(nums[i] - nums[i - 1] == 1) for i in range(1, len(nums))]):
            is_beautiful = True
            break

    if is_beautiful:
        print(YES(nums[0]))
        return YES(nums[0])

    print(NO)
    return NO


# separateNumbers("1234")  # yes 1
# separateNumbers("91011")  # yes 9
# separateNumbers("99100")  # yes 99
# separateNumbers("101103")  # no
# separateNumbers("010203")  # no
# separateNumbers("13")  # no
# separateNumbers("1")  # no


separateNumbers("99910001001")  # yes 999
separateNumbers("7891011")  # yes 7
separateNumbers("9899100")  # yes 98
separateNumbers("999100010001")  # no


# assert separateNumbers("1234") == "YES 1"
# assert separateNumbers("91011") == "YES 9"
# assert separateNumbers("99100") == "YES 99"
# assert separateNumbers("101103") == "NO"
# assert separateNumbers("010203") == "NO"
# assert separateNumbers("13") == "NO"
# assert separateNumbers("1") == "NO"


# assert separateNumbers("1") == "NO"  # only 1 number

# assert separateNumbers("1234") == "YES 1"
# assert separateNumbers("1213") == "YES 12"
# assert separateNumbers("91011") == "YES 9"
# assert separateNumbers("99100") == "YES 99"

# assert separateNumbers("321") == "NO"
# assert separateNumbers("10203") == "NO"

# assert separateNumbers("12343") == "NO"
# assert separateNumbers("100010011002") == "YES 1000"
# assert separateNumbers("100010011003") == "NO"
