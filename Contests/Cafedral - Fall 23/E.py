n = int(input())
cubes = list(input())

if n % 2 == 0:
    print("Ok")
else:
    counts = {cube: 0 for cube in cubes}
    for cube in cubes:
        counts[cube] += 1

    for cube, count in counts.items():
        if count % 2 == 1:
            print(cube)
