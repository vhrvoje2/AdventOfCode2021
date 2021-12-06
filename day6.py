from timeit import Timer

with open("input6.txt", "r") as file:
    for item in file.readlines():
        timers = item.split(",")
        fish_timers = [int(time) for time in timers]


def sum_fish(num_days):
    fish_dict = {x: 0 for x in range(9)}

    for time in fish_timers:
        fish_dict[time] += 1

    for day in range(num_days):
        new_fish = fish_dict[0]
        fish_dict[0] = fish_dict[1]
        fish_dict[1] = fish_dict[2]
        fish_dict[2] = fish_dict[3]
        fish_dict[3] = fish_dict[4]
        fish_dict[4] = fish_dict[5]
        fish_dict[5] = fish_dict[6]
        fish_dict[6] = fish_dict[7]
        fish_dict[7] = fish_dict[8]
        fish_dict[8] = new_fish
        fish_dict[6] += new_fish

    result = sum([v for k, v in fish_dict.items()])
    return result


def part1():
    num_days_p1 = 80
    result = sum_fish(num_days_p1)

    print(f"Part 1. solution {result}")


def part2():
    num_days_p2 = 256
    result = sum_fish(num_days_p2)

    print(f"Part 2. solution {result}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
