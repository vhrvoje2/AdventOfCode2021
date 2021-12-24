from timeit import Timer

start_positions = []
with open("input21.txt", "r") as file:
    for item in file.readlines():
        start_positions.append(item.strip())


class Player:
    def __init__(self, name, start_position):
        self.name = name
        self.position = start_position
        self.score = 0

    def move(self, move):
        for n in range(1, move + 1):
            self.position += 1
            if self.position > 10:
                self.position = 1
        self.score += self.position
        print(
            f"{self.name} rolls {move} and moves to space {self.position} for a total score of {self.score}"
        )


def part1():
    position_1 = int(start_positions[0][len(start_positions[0]) - 1])
    position_2 = int(start_positions[1][len(start_positions[1]) - 1])
    player_1 = Player("Player 1", position_1)
    player_2 = Player("Player 2", position_2)

    winner = False
    die = 1
    roll_count = 0
    turn_p1 = True
    loser_score = 0
    while not winner:
        move = 0
        for n in range(die, die + 3):
            move += n
            roll_count += 1
            die += 1
        if turn_p1:
            player_1.move(move)
            turn_p1 = False
        else:
            player_2.move(move)
            turn_p1 = True
        if player_1.score >= 1000:
            winner = True
            loser_score = player_2.score
        elif player_2.score >= 1000:
            winner = True
            loser_score = player_1.score

    result = loser_score * roll_count
    print(f"Part 1. solution {result}")


def part2():
    pass
    # print(f"Part 2. solution {}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
