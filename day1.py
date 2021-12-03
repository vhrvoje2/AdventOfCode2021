measurements = []
with open("input1.txt", "r") as file:
    for item in file.readlines():
        measurements.append(int(item.strip()))


def part1():
    counter = 0
    for idx in range(1, len(measurements)):
        if measurements[idx] > measurements[idx - 1]:
            counter += 1
    print(f"Part 1. solution: {counter}")


def part2():
    counter = 0
    for idx in range(0, len(measurements) - 3):
        current_window = (
            measurements[idx] + measurements[idx + 1] + measurements[idx + 2]
        )
        next_window = (
            measurements[idx + 1] + measurements[idx + 2] + measurements[idx + 3]
        )
        if next_window > current_window:
            counter += 1
    print(f"Part 2. solution: {counter}")


part1()
part2()
