from timeit import Timer

placeholder = []
with open(".txt", "r") as file:
    for item in file.readlines():
        placeholder.append(item.strip())


def part1():
    pass
    # print(f"Part 1. solution {}")


def part2():
    pass
    # print(f"Part 2. solution {}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
