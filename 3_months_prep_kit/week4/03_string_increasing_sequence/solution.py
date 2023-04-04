# from math import ceil


def separateNumbers(num_str):
    # Write your code here
    if len(num_str) <= 1:
        print("NO")
        return "NO"

    longest_sub_num = len(num_str) // 2
    for sub_num_len in range(1, longest_sub_num + 1):
        first_num = curr_num = int(num_str[:sub_num_len])

        beautiful_num: str = str(curr_num)
        while len(beautiful_num) < len(num_str):
            curr_num += 1
            beautiful_num = beautiful_num + str(curr_num)
            if beautiful_num == num_str:
                print(f"YES {first_num}")
                return f"YES {first_num}"
    print("NO")
    return "NO"


assert separateNumbers("1234") == "YES 1"  # yes 1
assert separateNumbers("91011") == "YES 9"  # yes 9
assert separateNumbers("99100") == "YES 99"  # yes 99
assert separateNumbers("101103") == "NO"  # no
assert separateNumbers("010203") == "NO"  # no
assert separateNumbers("13") == "NO"  # no
assert separateNumbers("1") == "NO"  # no


assert separateNumbers("99910001001") == "YES 999"  # yes 999
assert separateNumbers("7891011") == "YES 7"  # yes 7
assert separateNumbers("9899100") == "YES 98"  # yes 98
assert separateNumbers("999100010001") == "NO"  # no
