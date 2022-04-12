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


def generate_board(size) -> list:
    return [[0 for _ in range(size)] for _ in range(size)]


def hardcoded_board() -> list:
    return [
        [0, 0, 0, 6, 6, 0],
        [4, 4, 5, 5, 6, 0],
        [0, 4, 5, 0, 6, 0],
        [0, 4, 5, 0, 3, 2],
        [0, 1, 3, 3, 3, 2],
        [0, 1, 1, 1, 2, 2],
    ]


def hardcoded_shapes() -> set:
    return {0, 1, 2, 3, 4, 5, 6}
