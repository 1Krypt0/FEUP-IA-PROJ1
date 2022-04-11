from board import *
from copy import deepcopy
from algo import check_valid, is_solved

class BoardState:
    def __init__(self, pos, board: Board, previousNode=None) -> None:
        self.goal_y, self.goal_x = board.goal
        self.y, self.x = pos
        self.board = board
        self.previousNode = previousNode
        self.children = self.calculateChildren()

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BoardNode) and self.board == __o.board

    def __repr__(self):
        return f'(x: {self.x}, y: {self.y})'

    def calculateChildren(self):
        pass


# Operators

def move_up(state):
    new_pos = (state.y - 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)

def move_down(state):
    new_pos = (state.y + 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)

def move_left(state):
    new_pos = (state.y, state.x - 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)

def move_right(state):
    new_pos = (state.y, state.x + 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    return BoardState(new_pos, new_board)


operators = [move_up, move_down, move_left, move_right]

# Search algorithms


def bfs(start):
    queue = [start]
    solution = None

    while queue:
        current = queue.pop(0)
        if is_solved((current.y, current.x), (current.goal_y, current.goal_x), current.board):
            solution = current
            break
        for op in operators:
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



if __name__ == '__main__':
    pass
