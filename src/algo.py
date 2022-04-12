from state import OPERATORS, BoardState
from board import is_solved

# board  -> bidimensional board array
# path   -> array of visited board positions on path
# shapes -> set of visited shape identifiers
# start  -> current position on the algorithm, on the maze
# goal   -> end position, on the maze
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
        print(solution.board)
        while solution:
            path.append(solution)
            solution = solution.previousNode

    return list(reversed(path))
