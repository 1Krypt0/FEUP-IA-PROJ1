from board import Board
from state import BoardState, bfs, dfs


def main():
    # board = Board(6)
    # solved = backtracking(board, board.start, board.goal)
    # board.print_board()
    board = Board(6)
    state = BoardState(board.start, board)
    dfs(state, 20)


if __name__ == "__main__":
    main()
