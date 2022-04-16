from state import BoardState
from math import sqrt


def manhattan_distance(node: BoardState) -> int:
    return abs(node.x - node.goal_x) + abs(node.y - node.goal_y)


def visited_l(node: BoardState) -> int:
    return len(node.board.all_shapes.difference(node.board.visited_shapes))


def euclidian_distance(node: BoardState) -> float:
    return int(sqrt(((node.goal_x - node.x) ** 2) + ((node.goal_y - node.y) ** 2)))
