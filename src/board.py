from board_lists import *
import random

RED = "\033[31m"
RESET = "\033[0m"


class Board:
    def __init__(self, difficulty: int) -> None:
        self.board = choose_random_board(difficulty)
        size = len(self.board)
        self.start = (size - 1, 0)
        self.goal = (0, size - 1)
        self.visited = [
            [0 for _ in range(size)] for _ in range(size)
        ]  # TODO: No need to keep track of everything in a Matrix
        self.visited_shapes = set()
        self.all_shapes = determine_shapes(self.board)
        self.size = size
        self.visit(self.start)

    def reset(self):
        self.visited = [
            [0 for _ in range(self.size)] for _ in range(self.size)
        ]  # TODO: No need to keep track of everything in a Matrix

    def visit(self, pos) -> None:
        self.visited_shapes.add(self.board[pos[0]][pos[1]])
        self.visited[pos[0]][pos[1]] = 1

    def unvisit(self, pos) -> None:
        shape = self.board[pos[0]][pos[1]]
        if shape != 0:
            self.visited_shapes.discard(shape)
        self.visited[pos[0]][pos[1]] = 0

    def __repr__(self) -> str:
        final = "\n"
        final += "   0 1 2 3 4 5 "
        final += "\n"
        final += "  _____________\n"
        for line in range(self.size):
            final += str(line) + " "
            for col in range(self.size):
                final += (
                    "|"
                    + RED * self.visited[line][col]
                    + str(self.board[line][col])
                    + RESET
                )
            final += "|\n"
        final += "  ‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
        return final

    def __str__(self) -> str:
        final = "\n"
        final += "   0 1 2 3 4 5 "
        final += "\n"
        final += "  _____________\n"
        for line in range(self.size):
            final += str(line) + " "
            for col in range(self.size):
                final += (
                    "|"
                    + RED * self.visited[line][col]
                    + str(self.board[line][col])
                    + RESET
                )
            final += "|\n"
        final += "  ‾‾‾‾‾‾‾‾‾‾‾‾‾\n"
        return final


def is_complete(pos, goal) -> bool:
    return pos == goal


def visited_all(board: Board) -> bool:
    return board.visited_shapes == board.all_shapes


def is_solved(pos, goal, board: Board) -> bool:
    return is_complete(pos, goal) and visited_all(board)


def check_bounds(board: Board, pos: list) -> bool:
    return not (
        pos[0] < 0 or pos[1] < 0 or pos[0] >= board.size or pos[1] >= board.size
    )


# board  -> board object
# shapes -> array of visited board positions on path
# pos    -> current position on the algorithm, on the maze
# returns the validity of the position
def check_valid(board: Board, pos) -> bool:

    if not check_bounds(board, pos):
        return False

    shape = board.board[pos[0]][pos[1]]

    if board.visited[pos[0]][pos[1]] == 1:
        return False

    if shape in board.visited_shapes and shape != 0:
        return False

    return True


def determine_shapes(board: list[list[int]]) -> set:
    final = set()
    for line in board:
        for num in line:
            if num not in final:
                final.add(num)
    return final


def generate_board(difficulty: int) -> Board:
    return Board(difficulty)


def choose_random_board(difficulty: int) -> list[list[int]]:
    if difficulty == 1:
        return random.choice(EASY_BOARDS_LIST)
    elif difficulty == 2:
        return random.choice(MEDIUM_BOARDS_LIST)
    elif difficulty == 3:
        return random.choice(HARD_BOARDS_LIST)
    elif difficulty == 4:
        return random.choice(EXTREME_BOARDS_LIST)
    else:
        return [[-1]]
