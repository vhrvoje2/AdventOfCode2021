from timeit import Timer
from math import ceil

dots = []
instructions = []
max_x = 0
max_y = 0
with open("input13.txt", "r") as file:
    for item in file.readlines():
        item = item.strip()
        if len(item) < 9 and item != "":
            xy = item.split(",")
            coords = [int(xy[0]), int(xy[1])]
            dots.append(coords)
            if coords[0] > max_x:
                max_x = coords[0]
            elif coords[1] > max_y:
                max_y = coords[1]
        elif item != "":
            directions = item.split("=")
            axis = directions[0][len(directions[0]) - 1]
            offset = int(directions[1])

            instruction = [axis, offset]
            instructions.append(instruction)


def part1():
    sheet = []
    for y in range(max_y + 1):
        row = ["." for _ in range(max_x + 1)]
        sheet.append(row)

    for x, y in dots:
        sheet[y][x] = "#"

    axis = instructions[0][0]
    offset = instructions[0][1]

    if axis == "y":
        for y in range(offset + 1, max_y + 1):
            for x in range(max_x + 1):
                if sheet[y][x] == "#":
                    new_y = max_y - y
                    sheet[y][x] = "."
                    sheet[new_y][x] = "#"
    else:
        for y in range(max_y + 1):
            for x in range(offset + 1, max_x + 1):
                if sheet[y][x] == "#":
                    new_x = max_x - x
                    sheet[y][x] = "."
                    sheet[y][new_x] = "#"

    result = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if sheet[y][x] == "#":
                result += 1

    print(f"Part 1. solution {result}")


def part2():
    sheet = []
    for y in range(max_y + 1):
        row = ["." for _ in range(max_x + 1)]
        sheet.append(row)

    for x, y in dots:
        sheet[y][x] = "#"

    for instruction in instructions:
        axis = instruction[0]
        offset = instruction[1]

        if axis == "y":
            for y in range(offset + 1, max_y + 1):
                for x in range(max_x + 1):
                    if sheet[y][x] == "#":
                        new_y = max_y - y
                        sheet[y][x] = "."
                        sheet[new_y][x] = "#"
        else:
            for y in range(max_y + 1):
                for x in range(offset + 1, max_x + 1):
                    if sheet[y][x] == "#":
                        new_x = max_x - x
                        sheet[y][x] = "."
                        sheet[y][new_x] = "#"

    print(f"Part 2. solution")

    for y in range(6):
        x_range = ceil((max_x + 1) / 2)
        for x in range(x_range):
            print(sheet[y][x], end="")
        print()


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
