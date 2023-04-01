def kangaroo_old(closer, closer_rate, farther, farther_rate):
    if closer != farther and closer_rate <= farther_rate:
        return "NO"

    while closer <= farther:
        if closer == farther:
            return "YES"

        farther += farther_rate
        closer += closer_rate

    return "NO"


def kangaroo(closer, closer_rate, farther, farther_rate):
    dist_diff = farther - closer  # total dist to go
    velocity_diff = closer_rate - farther_rate  # velocity to catch up

    if velocity_diff <= 0 or dist_diff % velocity_diff != 0:
        return "NO"
    return "YES"


assert kangaroo(0, 3, 4, 2) == "YES"
assert kangaroo(0, 2, 5, 3) == "NO"
