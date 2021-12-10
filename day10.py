from timeit import Timer
from math import floor

input_lines = []
with open("input10.txt", "r") as file:
    for item in file.readlines():
        input_lines.append(item.strip())


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        top_item = self.stack.pop()
        return top_item

    def top(self):
        last_idx = len(self.stack) - 1
        return self.stack[last_idx]

    def size(self):
        size = len(self.stack)
        return size

    def clear(self):
        self.stack.clear()


scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
count = {")": 0, "]": 0, "}": 0, ">": 0}
points = {"(": 1, "[": 2, "{": 3, "<": 4}


def part1():
    stack = Stack()
    for line in input_lines:
        stack.clear()
        error = False
        idx = 0
        while idx < len(line) and not error:
            bracket = line[idx]
            if bracket in ["(", "[", "{", "<"]:
                stack.push(bracket)
            elif bracket == ")":
                if stack.top() == "(":
                    stack.pop()
                else:
                    error = True
            elif bracket == "]":
                if stack.top() == "[":
                    stack.pop()
                else:
                    error = True
            elif bracket == "}":
                if stack.top() == "{":
                    stack.pop()
                else:
                    error = True
            elif bracket == ">":
                if stack.top() == "<":
                    stack.pop()
                else:
                    error = True
            if error:
                count[bracket] += 1

            idx += 1

    result = sum([scores[bracket] * count[bracket] for bracket in scores.keys()])
    print(f"Part 1. solution {result}")


def part2():
    incomplete_lines = []
    stack = Stack()
    for line in input_lines:
        stack.clear()
        error = False
        idx = 0
        while idx < len(line) and not error:
            bracket = line[idx]
            if bracket in ["(", "[", "{", "<"]:
                stack.push(bracket)
            elif bracket == ")":
                if stack.top() == "(":
                    stack.pop()
                else:
                    error = True
            elif bracket == "]":
                if stack.top() == "[":
                    stack.pop()
                else:
                    error = True
            elif bracket == "}":
                if stack.top() == "{":
                    stack.pop()
                else:
                    error = True
            elif bracket == ">":
                if stack.top() == "<":
                    stack.pop()
                else:
                    error = True

            idx += 1

        if not error:
            incomplete_line_remainder = "".join(stack.stack)
            incomplete_lines.append(incomplete_line_remainder)

    line_scores = []
    for line in incomplete_lines:
        score = 0
        stack.clear()
        for bracket in line:
            stack.push(bracket)

        while stack.size() > 0:
            last_bracket = stack.pop()
            if last_bracket == "(":
                score *= 5
                score += points[last_bracket]
            elif last_bracket == "[":
                score *= 5
                score += points[last_bracket]
            elif last_bracket == "{":
                score *= 5
                score += points[last_bracket]
            elif last_bracket == "<":
                score *= 5
                score += points[last_bracket]

        line_scores.append(score)

    line_scores.sort()
    score_idx = floor(len(line_scores) / 2)
    print(f"Part 2. solution {line_scores[score_idx]}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
