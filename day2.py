from timeit import Timer

directions = []
with open("input2.txt", "r") as file:
    for item in file.readlines():
        directions.append(item.strip())

commands = {
    "down": 1,
    "up": -1,
}


def part1():
    depth = position = 0
    for instruction in directions:
        command, value = instruction.split(" ")
        if command == "forward":
            position += int(value)
        else:
            depth += commands[command] * int(value)

    result = depth * position
    print(f"Part 1. solution {result}")


def part2():
    depth = position = aim = 0
    for instruction in directions:
        command, value = instruction.split(" ")
        if command == "forward":
            position += int(value)
            depth += int(value) * aim
        else:
            aim += commands[command] * int(value)

    result = depth * position
    print(f"Part 2. solution {result}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
