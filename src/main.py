from board import Board
from state import BoardState, bfs, dfs, ids


def main():
    # board = Board(6)
    # solved = backtracking(board, board.start, board.goal)
    # board.print_board()
    board = Board(6)
    state = BoardState(board.start, board)
    ids(state)


if __name__ == "__main__":
    main()
