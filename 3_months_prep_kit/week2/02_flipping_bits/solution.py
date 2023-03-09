"""
    can use subtraction: (2**32 - 1) - num
    can use xor: (2**32 - 1) ^ num

    since the assignment is to flip bits, i'm going to use 
    the xor operator
"""

max = (2**32) - 1


def flippingBits(num):
    # flip all bits in 32-bit unsigned int
    flipped = num ^ max
    return flipped


assert flippingBits(9) == 4294967286
assert flippingBits(2147483647) == 2147483648
assert flippingBits(1) == 4294967294
assert flippingBits(0) == 4294967295
