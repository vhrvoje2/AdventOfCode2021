from timeit import Timer

heightmap = []
with open("input9.txt", "r") as file:
    for item in file.readlines():
        points = []
        for point in item.strip():
            points.append(int(point))
        heightmap.append(points)


def part1():
    len_y = len(heightmap)
    len_x = len(heightmap[0])
    risk_sum = 0

    for y in range(len_y):
        for x in range(len_x):
            current_point = heightmap[y][x]
            adjecent = {
                "above": -1,
                "below": -1,
                "left": -1,
                "right": -1,
            }

            if y > 0:
                adjecent["above"] = heightmap[y - 1][x]
            if y < len_y - 1:
                adjecent["below"] = heightmap[y + 1][x]
            if x > 0:
                adjecent["left"] = heightmap[y][x - 1]
            if x < len_x - 1:
                adjecent["right"] = heightmap[y][x + 1]

            adjecent_points = [v for k, v in adjecent.items() if v != -1]
            if current_point < min(adjecent_points):
                risk_sum += 1 + current_point

    print(f"Part 1. solution {risk_sum}")


def part2():
    pass
    # print(f"Part 2. solution {}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
