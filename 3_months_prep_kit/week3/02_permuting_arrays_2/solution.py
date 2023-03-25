def birthday(squares, day, month):
    # Write your code here
    seg_length = month
    squares_sum = day

    # + 1, inclusive
    num_segments = (len(squares) + 1) - seg_length
    poss_segments = [squares[i : seg_length + i] for i in range(num_segments)]

    sums = [sum(segment) for segment in poss_segments]
    total = sums.count(squares_sum)
    return total


assert birthday([2, 2, 1, 3, 2], 4, 2) == 2
