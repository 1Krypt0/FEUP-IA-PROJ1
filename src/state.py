from board import Board, check_valid
from copy import deepcopy


class BoardState:
    def __init__(self, pos, board: Board, previousNode=None) -> None:
        self.goal_y, self.goal_x = board.goal
        self.y, self.x = pos
        self.board = board
        self.previousNode = previousNode

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BoardState) and self.board == __o.board

    def __repr__(self):
        return f"(x: {self.x}, y: {self.y})"


# Operators


def move_up(state: BoardState) -> BoardState:
    new_pos = (state.y - 1, state.x)
    if not check_valid(state.board, new_pos):
        pass
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


def move_down(state: BoardState) -> BoardState:
    new_pos = (state.y + 1, state.x)
    if not check_valid(state.board, new_pos):
        pass
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


def move_left(state: BoardState) -> BoardState:
    new_pos = (state.y, state.x - 1)
    if not check_valid(state.board, new_pos):
        pass
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


def move_right(state: BoardState) -> BoardState:
    new_pos = (state.y, state.x + 1)
    if not check_valid(state.board, new_pos):
        pass
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


OPERATORS = [move_up, move_down, move_left, move_right]

# Search algorithms
