with open("input6.txt", "r") as file:
    for item in file.readlines():
        timers = item.split(",")
        fish_timers = [int(time) for time in timers]

DAYS_P1 = 80
DAYS_P2 = 256


class Lanternfish:
    def __init__(self, timer):
        self.timer = timer


def part1():
    for time in fish_timers:
        lanternfish_list = [Lanternfish(time) for time in fish_timers]

    for day in range(DAYS_P1):
        for n in range(len(lanternfish_list)):
            fish = lanternfish_list[n]
            fish.timer -= 1
            if fish.timer == -1:
                fish.timer = 6
                lanternfish_list.append(Lanternfish(8))

    result = len(lanternfish_list)
    print(f"Part 1. solution {result}")


def part2():
    fish_dict = {x: 0 for x in range(9)}

    for time in fish_timers:
        fish_dict[time] += 1

    for day in range(DAYS_P2):
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
    print(f"Part 2. solution {result}")


part1()
part2()
