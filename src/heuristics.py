from state import BoardState
from math import sqrt


def manhattan_distance(node: BoardState):
    return abs(node.x - node.goal_x) + abs(node.y - node.goal_y)


def visited_l(node: BoardState):
    return len(node.board.all_shapes.difference(node.board.visited_shapes))


def euclidian_distance(node: BoardState):
    return sqrt(((node.goal_x - node.x) ** 2) + ((node.goal_y - node.y) ** 2))
