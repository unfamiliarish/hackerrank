from collections import defaultdict
from string import ascii_lowercase as smalls


def pangrams(input_str):
    # Write your code here
    lower_str = input_str.lower()
    for letter in smalls:
        # breakpoint()
        if letter not in lower_str:
            return 'not pangram'

    return 'pangram'


assert (
    pangrams('We promptly judged antique ivory buckles for the next prize') == 'pangram'
)
assert (
    pangrams('We promptly judged antique ivory buckles for the prize') == 'not pangram'
)
