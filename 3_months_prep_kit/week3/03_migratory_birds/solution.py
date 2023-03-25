def migratoryBirds(birds):
    # Write your code here
    # bird ids are 1,2,3,4,5
    bird_counts = [0] * 6
    for bird in birds:
        bird_counts[bird] += 1

    max_birds = set()
    max_count = 0

    for bird, count in enumerate(bird_counts):
        if count and count == max_count:
            max_birds.add(bird)
        elif count > max_count:
            max_birds = {bird}
            max_count = count

    sorted_birds = sorted(max_birds)
    return sorted_birds[0]


assert migratoryBirds([1, 1, 2, 2, 3]) == 1
assert migratoryBirds([1, 4, 4, 4, 5, 3]) == 4
