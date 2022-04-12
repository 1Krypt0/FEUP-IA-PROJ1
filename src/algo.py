
# board  -> bidimensional board array
# path   -> array of visited board positions on path
# shapes -> set of visited shape identifiers
# start  -> current position on the algorithm, on the maze
# goal   -> end position, on the maze


def backtracking(board, start, goal) -> bool:

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

# pos  -> current position on the algorithm, on the maze
# goal -> end position, on the maze
def is_complete(pos, goal) -> bool:
    return pos == goal


def visited_all(board) -> bool:
    return board.visited_shapes == board.all_shapes


def is_solved(pos, goal, board):
    return is_complete(pos, goal) and visited_all(board)


def check_bounds(board, pos: list) -> bool:
    return not (
        pos[0] < 0 or pos[1] < 0 or pos[0] >= board.size or pos[1] >= board.size
    )


# board  -> board object
# shapes -> array of visited board positions on path
# pos    -> current position on the algorithm, on the maze
# returns the validity of the position
def check_valid(board, pos) -> bool:

    if not check_bounds(board, pos):
        return False

    shape = board.board[pos[0]][pos[1]]

    if board.visited[pos[0]][pos[1]] == 1:
        return False

    if shape in board.visited_shapes and shape != 0:
        return False

    return True
