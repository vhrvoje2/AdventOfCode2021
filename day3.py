from timeit import Timer
from copy import deepcopy

report = []
with open("input3.txt", "r") as file:
    for item in file.readlines():
        report.append(item.strip())


bit_counter = {}


def part1():
    for number in report:
        for idx, bit in enumerate(number):
            if bit == "1":
                if idx in bit_counter:
                    bit_counter[idx] += 1
                else:
                    bit_counter[idx] = 1

    report_length = len(report)
    gamma_rate = ""
    epsilon_rate = ""

    for idx in range(len(number)):
        if bit_counter[idx] > report_length / 2:
            gamma_rate += "1"
            epsilon_rate += "0"
        else:
            gamma_rate += "0"
            epsilon_rate += "1"

    result = int(gamma_rate, 2) * int(epsilon_rate, 2)
    print(f"Part 1. solution {result}")


def part2():
    bit_number = len(report[0])
    number_set = deepcopy(report)
    for n in range(bit_number):
        most_common_one = []
        most_common_zero = []
        one_count = 0
        zero_count = 0
        for number in number_set:
            if number[n] == "1":
                one_count += 1
                most_common_one.append(number)
            else:
                zero_count += 1
                most_common_zero.append(number)
        if len(number_set) == 1:
            break

        if one_count >= zero_count:
            number_set = most_common_one
        else:
            number_set = most_common_zero
    oxygen_generator_rating = int(number_set[0], 2)

    number_set = deepcopy(report)
    for n in range(bit_number):
        most_common_one = []
        most_common_zero = []
        one_count = 0
        zero_count = 0
        for number in number_set:
            if number[n] == "1":
                one_count += 1
                most_common_one.append(number)
            else:
                zero_count += 1
                most_common_zero.append(number)
        if len(number_set) == 1:
            break

        if one_count >= zero_count:
            number_set = most_common_zero
        else:
            number_set = most_common_one
    CO2_scrubber_rating = int(number_set[0], 2)

    result = oxygen_generator_rating * CO2_scrubber_rating
    print(f"Part 2. solution {result}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
