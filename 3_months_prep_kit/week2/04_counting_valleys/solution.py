def countingValleys(steps, path):
    # Write your code here
    height = 0

    in_valley = False
    valley_count = 0
    for step in path:
        if step == 'D':
            height -= 1
            if height == -1:
                in_valley = True
        elif step == 'U':
            height += 1
            if in_valley and height == 0:
                valley_count += 1
                in_valley = False
        else:
            raise ValueError(f"incorrect input: {step}")

    return valley_count


assert countingValleys(0, ['U', 'U', 'D', 'D']) == 0
assert countingValleys(0, ['U', 'U', 'D', 'U', 'D', 'D']) == 0
assert countingValleys(0, ['D', 'U']) == 1
assert countingValleys(0, ['D', 'U', 'U', 'D']) == 1
assert countingValleys(0, ['U', 'D', 'D', 'U']) == 1
assert countingValleys(0, ['D', 'U', 'D', 'U']) == 2
assert countingValleys(0, ['D', 'D', 'U', 'U']) == 1
