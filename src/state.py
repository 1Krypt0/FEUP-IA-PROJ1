from board import *
from copy import deepcopy
from algo import check_valid, is_solved


class BoardState:
    def __init__(self, pos, board: Board, previousNode=None, next_node=None) -> None:
        self.goal_y, self.goal_x = board.goal
        self.y, self.x = pos
        self.board = board
        self.previousNode = previousNode
        self.next_node = next_node

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BoardState) and self.board == __o.board

    def __repr__(self):
        return f"(x: {self.x}, y: {self.y})"


# Operators


def move_up(state: BoardState) -> BoardState:
    new_pos = (state.y - 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


def move_down(state: BoardState) -> BoardState:
    new_pos = (state.y + 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


def move_left(state: BoardState) -> BoardState:
    new_pos = (state.y, state.x - 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


def move_right(state: BoardState) -> BoardState:
    new_pos = (state.y, state.x + 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


OPERATORS = [move_up, move_down, move_left, move_right]

# Search algorithms


def bfs(start: BoardState) -> list:
    queue = [start]
    solution = None

    while queue:
        current = queue.pop(0)
        if is_solved(
            (current.y, current.x), (current.goal_y, current.goal_x), current.board
        ):
            solution = current
            break
        for op in OPERATORS:
            next = op(current)
            if not next:
                continue
            next.previousNode = current
            queue.append(next)

    path = []
    if solution:
        solution.board.print_board()
        while solution:
            path.append(solution)
            solution = solution.previousNode

    return list(reversed(path))


def dfs(state: BoardState, max_depth: int) -> list:
    if dfs_rec(state, 0, max_depth):
        return get_solution_from_next(state)


def dfs_rec(state: BoardState, current_depth: int, max_depth: int) -> bool:

    if current_depth == max_depth:
        return False

    if is_solved((state.y, state.x), (state.goal_y, state.goal_x), state.board):
        return True

    for op in OPERATORS:
        next = op(state)
        if not next:
            continue
        state.next_node = next
        if dfs_rec(next, current_depth + 1, max_depth):
            return True

    return False

def ids(state: BoardState) -> list:
    depth = 0
    while True:
        if not dfs(state, depth):
            depth += 1
        else:
            return get_solution_from_next(state, False)


def get_solution_from_next(state: BoardState, show=True) -> list:
    path = []
    while state:
        path.append(state)
        state = state.next_node
    if show:
        path[-1].board.print_board()
    return path
