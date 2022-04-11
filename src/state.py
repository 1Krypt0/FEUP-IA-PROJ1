from board import *


class BoardState:
    def __init__(self, pos, board: Board, previousNode=None) -> None:
        self.goal_y, self.goal_x = board.goal
        self.y, self.x = pos
        self.board = board
        self.previousNode = previousNode
        self.children = self.calculateChildren()

    def __eq__(self, __o: object) -> bool:
        return isinstance(__o, BoardNode) and self.board == __o.board

    def calculateChildren(self):
        pass


# Operators

def move_up(state):
    if state.x >= state.goal_x or state.board.visited[state.y - 1][state.x]:
        print("Invalid")
        return
    new_pos = (state.y - 1, state.x)
    state.board.visit(new_pos)
    return BoardState(new_pos, state.board)


def move_down(state):
    if state.x <= 0 or state.board.visited[state.y + 1][state.x]:
        print("Invalid")
        return
    new_pos = (state.y + 1, state.x)
    state.board.visit(new_pos)
    return BoardState(new_pos, state.board)


def move_left(state):
    if state.x <= 0 or state.board.visited[state.y][state.x - 1]:
        print("Invalid")
        return
    new_pos = (state.y, state.x - 1)
    state.board.visit(new_pos)
    return BoardState(new_pos, state.board)


def move_right(state):
    if state.x >= state.goal_x or state.board.visited[state.y][state.x + 1]:
        print("Invalid")
        return
    new_pos = (state.y, state.x + 1)
    state.board.visit(new_pos)
    return BoardState(new_pos, state.board)


if __name__ == '__main__':
    pass
