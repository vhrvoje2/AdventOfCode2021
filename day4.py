from timeit import Timer

numbers_drawn = []
input_boards = []
with open("input4.txt", "r") as file:
    numbers_drawn = file.readline()
    file.readline()
    for row in file.readlines():
        if row != "\n":
            input_boards.append(row)


class BoardNumber:
    def __init__(self, num):
        self.number = num
        self.marked = False

    def __repr__(self):
        return f"{self.number} - {self.marked}"


def create_board(rows):
    board_rows = []
    for row in rows:
        numbers = row.split(" ")
        new_row = []
        for number in numbers:
            if number != "":
                new_number = int(number)
                number_obj = BoardNumber(new_number)
                new_row.append(number_obj)
        board_rows.append(new_row)

    return board_rows


def mark_on_board(board, number):
    for row in board:
        for num_obj in row:
            if num_obj.number == number:
                num_obj.marked = True
                return


def check_bingo(board, cols=False):
    for i in range(5):
        if (
            board[i][0].marked
            and board[i][1].marked
            and board[i][2].marked
            and board[i][3].marked
            and board[i][4].marked
        ):
            return True
    for j in range(5):
        if (
            board[0][j].marked
            and board[1][j].marked
            and board[2][j].marked
            and board[3][j].marked
            and board[4][j].marked
        ):
            return True
    return False


bingo_boards = []
for n in range(0, len(input_boards), 5):
    current_input_rows = input_boards[n : n + 5]
    new_board = create_board(current_input_rows)
    bingo_boards.append(new_board)


def sum_unmarked_nums(board):
    sum = 0
    for i in range(5):
        for j in range(5):
            if board[i][j].marked == False:
                sum += board[i][j].number
    return sum


def part1():
    for drawn_number in numbers_drawn.split(","):
        for board in bingo_boards:
            drawn_number = int(drawn_number)
            mark_on_board(board, drawn_number)
            bingo_rows = check_bingo(board)
            bingo_cols = check_bingo(board, True)
            if bingo_rows or bingo_cols:
                unmarked_sum = sum_unmarked_nums(board)
                print(f"Part 1. solution {unmarked_sum * drawn_number}")
                return


def part2():
    for drawn_number in numbers_drawn.split(","):
        for x in range(len(bingo_boards) - 1, 0, -1):
            drawn_number = int(drawn_number)
            board = bingo_boards[x]
            mark_on_board(board, drawn_number)
            bingo_rows = check_bingo(board)
            bingo_cols = check_bingo(board, True)
            if bingo_rows or bingo_cols:
                bingo_boards.remove(board)
            if len(bingo_boards) == 1:
                unmarked_sum = sum_unmarked_nums(board)
                print(f"Part 2. solution {unmarked_sum * drawn_number}")
                return


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
