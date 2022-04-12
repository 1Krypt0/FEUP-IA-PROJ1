from state import BoardState, OPERATORS
from board import is_solved, check_valid, is_complete, visited_all

# board  -> bidimensional board array
# path   -> array of visited board positions on path
# shapes -> set of visited shape identifiers
# start  -> current position on the algorithm, on the maze
# goal   -> end position, on the maze
def backtracking(board, start, goal) -> bool:  # TODO: Change into a DFS

    startx = start[1]
    starty = start[0]

    board.visit(start)

    if is_complete(start, goal):
        if not visited_all(board):
            board.unvisit(start)
            return False
        board.print_board()
        return True

    # down
    if check_valid(board, (starty + 1, startx)):
        if backtracking(board, (starty + 1, startx), goal):
            return True

    # up
    if check_valid(board, (starty - 1, startx)):
        if backtracking(board, (starty - 1, startx), goal):
            return True

    # right
    if check_valid(board, (starty, startx + 1)):
        if backtracking(board, (starty, startx + 1), goal):
            return True

    # left
    if check_valid(board, (starty, startx - 1)):
        if backtracking(board, (starty, startx - 1), goal):
            return True

    board.unvisit(start)

    return False


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
