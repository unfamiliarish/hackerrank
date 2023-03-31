def get_triangles(sticks):
    sorted_sticks = sorted(sticks)
    num_sticks = len(sticks)

    triangles = []
    for i in range(num_sticks - 2):
        stick1 = sorted_sticks[i]
        for j in range(i + 1, num_sticks - 1):
            stick2 = sorted_sticks[j]
            for k in range(j + 1, num_sticks):
                stick3 = sorted_sticks[k]
                if stick3 >= stick1 + stick2:
                    continue
                triangles.append((stick1, stick2, stick3))

    return triangles


def maximumPerimeterTriangle(sticks):
    # don't have to worry about pythagorean theorem
    # degenerate - no two sides can equal the third side

    # not all sets of 3 will make a triangle :x
    triangles = get_triangles(sticks)
    if not triangles:
        return [-1]

    last_triangle = triangles[-1]
    reverse_triangles = triangles[-2::-1]

    best_triangle = last_triangle
    max_perim = sum(last_triangle)
    for triangle in reverse_triangles:
        triangle_perim = sum(triangle)
        if triangle_perim < max_perim:
            break

        # going backwards, so automatically will be equal if not neg
        # long side and short side
        if triangle[2] == best_triangle[2] and triangle[0] == best_triangle[0]:
            best_triangle = triangle

    return best_triangle


assert get_triangles([1, 2, 3, 4, 5, 10]) == [(2, 3, 4), (2, 4, 5), (3, 4, 5)]
assert get_triangles([1, 2]) == []
assert maximumPerimeterTriangle([1, 2, 3, 4, 5, 10]) == (3, 4, 5)
assert maximumPerimeterTriangle([1, 1, 1, 3, 3]) == (1, 3, 3)
assert maximumPerimeterTriangle([1, 2, 3]) == [-1]

assert maximumPerimeterTriangle([3, 9, 2, 15, 3]) == (2, 3, 3)
