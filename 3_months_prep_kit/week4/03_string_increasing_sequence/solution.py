def separateNumbers(num_str):
    # Write your code here
    


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
