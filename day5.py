from timeit import Timer

points = []
with open("input5.txt", "r") as file:
    for item in file.readlines():
        points.append(item.strip())


class Line:
    def __init__(self, line):
        self.xmax = 0
        self.ymax = 0
        self.parse_line(line)
        self.set_max()

    def parse_line(self, line):
        points = line.split("->")
        first_point = points[0].split(",")
        second_point = points[1].split(",")

        self.x1 = int(first_point[0])
        self.y1 = int(first_point[1])

        self.x2 = int(second_point[0])
        self.y2 = int(second_point[1])

    def set_max(self):
        if self.x1 > self.xmax:
            self.xmax = self.x1
        elif self.x2 > self.xmax:
            self.xmax = self.x2

        if self.y1 > self.ymax:
            self.ymax = self.y1
        elif self.y2 > self.ymax:
            self.ymax = self.y2

    def __repr__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"


diagram = []
angled_lines = []


def part1():
    lines = [Line(line) for line in points]
    xmax = max([line.xmax for line in lines])
    ymax = max([line.ymax for line in lines])

    range_max = max([xmax, ymax])
    for x in range(range_max + 1):
        new_row = [0 for y in range(range_max + 1)]
        diagram.append(new_row)

    for line in lines:
        if line.x1 == line.x2:
            if line.y1 > line.y2:
                for y in range(line.y2, line.y1 + 1):
                    diagram[y][line.x1] += 1
            else:
                for y in range(line.y1, line.y2 + 1):
                    diagram[y][line.x1] += 1
        elif line.y1 == line.y2:
            if line.x1 > line.x2:
                for x in range(line.x2, line.x1 + 1):
                    diagram[line.y1][x] += 1
            else:
                for x in range(line.x1, line.x2 + 1):
                    diagram[line.y1][x] += 1
        else:
            angled_lines.append(line)

    score = 0
    for line in diagram:
        for cord in line:
            if cord > 1:
                score += 1

    print(f"Part 1. solution {score}")


def mark_coords(xcords, ycords):
    for n in range(len(xcords)):
        diagram[ycords[n]][xcords[n]] += 1


def part2():
    for line in angled_lines:
        if line.x1 < line.x2:
            if line.y1 < line.y2:
                xcords = [x for x in range(line.x1, line.x2 + 1)]
                ycords = [y for y in range(line.y1, line.y2 + 1)]
                mark_coords(xcords, ycords)
            else:
                xcords = [x for x in range(line.x1, line.x2 + 1)]
                ycords = [y for y in range(line.y1, line.y2 - 1, -1)]
                mark_coords(xcords, ycords)
        elif line.x1 > line.x2:
            if line.y1 < line.y2:
                xcords = [x for x in range(line.x1, line.x2 - 1, -1)]
                ycords = [y for y in range(line.y1, line.y2 + 1)]
                mark_coords(xcords, ycords)
            else:
                xcords = [x for x in range(line.x1, line.x2 - 1, -1)]
                ycords = [y for y in range(line.y1, line.y2 - 1, -1)]
                mark_coords(xcords, ycords)

    score = 0
    for line in diagram:
        for cord in line:
            if cord > 1:
                score += 1
    print(f"Part 2. solution {score}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
