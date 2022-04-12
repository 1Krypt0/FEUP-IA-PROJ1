RED = "\033[31m"
RESET = "\033[0m"


class Board:
    def __init__(self, size: int) -> None:
        # self.board = generate_board()
        self.board = hardcoded_board()  # TODO: Change to generated board
        self.start = (size - 1, 0)
        self.goal = (0, size - 1)
        self.visited = [
            [0 for _ in range(size)] for _ in range(size)
        ]  # TODO: No need to keep track of everything in a Matrix
        self.visited_shapes = set()
        self.all_shapes = hardcoded_shapes()  # TODO: Change to actual shape identifier
        self.size = size
        self.visit(self.start)

    def visit(self, pos) -> None:
        self.visited_shapes.add(self.board[pos[0]][pos[1]])
        self.visited[pos[0]][pos[1]] = 1

    def unvisit(self, pos) -> None:
        shape = self.board[pos[0]][pos[1]]
        if shape != 0:
            self.visited_shapes.discard(shape)
        self.visited[pos[0]][pos[1]] = 0

    def __repr__(self) -> str:
        final = "   0 1 2 3 4 5 "
        final += "\n"
        final += "  _____________"
        for line in range(self.size):
            print(line, end=" ")
            final += str(line) + " "
            for col in range(self.size):
                final += (
                    "|"
                    + RED * self.visited[line][col]
                    + str(self.board[line][col])
                    + RESET
                )
            final += "|\n"
        final += "  ‾‾‾‾‾‾‾‾‾‾‾‾‾"
        return final

    def __str__(self) -> str:
        final = "   0 1 2 3 4 5 "
        final += "\n"
        final += "  _____________"
        for line in range(self.size):
            print(line, end=" ")
            final += str(line) + " "
            for col in range(self.size):
                final += (
                    "|"
                    + RED * self.visited[line][col]
                    + str(self.board[line][col])
                    + RESET
                )
            final += "|\n"
        final += "  ‾‾‾‾‾‾‾‾‾‾‾‾‾"
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


def generate_board(size) -> list:
    return [[0 for _ in range(size)] for _ in range(size)]


# TODO: Change into list of boards from game
def hardcoded_board() -> list:
    return [
        [0, 0, 0, 6, 6, 0],
        [4, 4, 5, 5, 6, 0],
        [0, 4, 5, 0, 6, 0],
        [0, 4, 5, 0, 3, 2],
        [0, 1, 3, 3, 3, 2],
        [0, 1, 1, 1, 2, 2],
    ]


EASY_BOARD_LIST = [
    [
        [1, 1, 1, 2, 2, 0],
        [0, 3, 1, 2, 4, 0],
        [0, 3, 0, 2, 4, 5],
        [0, 3, 3, 4, 4, 5],
        [0, 6, 6, 6, 5, 5],
        [0, 0, 0, 6, 0, 0],
    ],
    [
        [0, 0, 0, 1, 1, 0],
        [2, 2, 3, 3, 1, 0],
        [0, 2, 3, 0, 1, 0],
        [0, 2, 3, 0, 4, 5],
        [0, 6, 4, 4, 4, 5],
        [0, 6, 6, 6, 5, 5],
    ],
    [
        [1, 0, 2, 2, 2, 0],
        [1, 0, 2, 0, 0, 3],
        [1, 1, 4, 3, 3, 3],
        [5, 0, 4, 4, 4, 0],
        [5, 5, 5, 0, 6, 0],
        [0, 0, 6, 6, 6, 0],
    ],
    [
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 2, 0],
        [0, 1, 2, 2, 2, 3],
        [0, 4, 4, 0, 0, 3],
        [0, 4, 5, 0, 3, 3],
        [0, 4, 5, 5, 5, 0],
    ],
    [
        [1, 1, 2, 3, 0, 0],
        [4, 1, 2, 3, 3, 3],
        [4, 1, 2, 2, 0, 5],
        [4, 4, 6, 0, 0, 5],
        [0, 0, 6, 7, 5, 5],
        [0, 6, 6, 7, 7, 7],
    ],
    [
        [1, 1, 2, 2, 2, 0],
        [0, 1, 2, 0, 3, 4],
        [0, 1, 3, 3, 3, 4],
        [5, 0, 0, 0, 4, 4],
        [5, 5, 5, 6, 6, 6],
        [0, 0, 0, 0, 0, 6],
    ],
    [
        [0, 1, 1, 1, 0, 0],
        [0, 1, 2, 2, 2, 0],
        [3, 3, 2, 4, 4, 4],
        [3, 0, 0, 5, 5, 4],
        [3, 6, 6, 6, 5, 0],
        [0, 6, 0, 0, 5, 0],
    ],
]


def hardcoded_shapes() -> set:
    return {0, 1, 2, 3, 4, 5, 6}
