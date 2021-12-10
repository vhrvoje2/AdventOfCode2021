from timeit import Timer

displays = []
with open("input8.txt", "r") as file:
    for item in file.readlines():
        signals, digits = item.split(" | ")
        inputs = signals.split(" ")
        outputs = digits.split(" ")
        displays.append([inputs, outputs])

# SEGMENTS PER DIGIT
# 0: 6
# 1: 2 UNIQUE
# 2: 5
# 3: 5
# 4: 4 UNIQUE
# 5: 5
# 6: 6
# 7: 3 UNIQUE
# 8: 7 UNIQUE
# 9: 6

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

def part1():
    counter = 0
    for display in displays:
        for output in display[1]:
            if len(output.strip()) in [2, 3, 4, 7]:
                counter += 1

    print(f"Part 1. solution {counter}")


def part2():
    counter = 0
    for display in displays:
        display_map = {}
        for inp in display[0]:
            input_len = len(inp.strip())
            if input_len in [2, 3, 4, 7]:
                if input_len == 2:
                    display_map["c"] = inp[0]
                    display_map["f"] = inp[1]
                elif input_len == 3:
                    display_map["a"] = inp[0]
                    display_map["c"] = inp[1]
                    display_map["f"] = inp[2]
                elif input_len == 4:
                    display_map["b"] = inp[0]
                    display_map["c"] = inp[1]
                    display_map["d"] = inp[2]
                    display_map["f"] = inp[3]
                else:
                    display_map["a"] = inp[0]
                    display_map["b"] = inp[1]
                    display_map["c"] = inp[2]
                    display_map["d"] = inp[3]
                    display_map["e"] = inp[4]
                    display_map["f"] = inp[5]
                    display_map["g"] = inp[6]
    print(f"Part 2. solution {counter}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
