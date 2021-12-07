from timeit import Timer

with open("input7.txt", "r") as file:
    for item in file.readlines():
        crab_positions = [int(pos) for pos in item.split(",")]


def part1():
    max_move = max(crab_positions)
    min_fuel = float("inf")
    for position in range(max_move):
        fuel_cost = 0
        for crab_pos in crab_positions:
            fuel_cost += abs(crab_pos - position)
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost

    print(f"Part 1. solution {min_fuel}")


def part2():
    max_move = max(crab_positions)
    min_fuel = float("inf")
    for position in range(max_move):
        fuel_cost = 0
        for crab_pos in crab_positions:
            move = abs(crab_pos - position)
            step = 1
            for fuel in range(move):
                fuel_cost += step
                step += 1
        if fuel_cost < min_fuel:
            min_fuel = fuel_cost

    print(f"Part 2. solution {min_fuel}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
