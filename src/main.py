from board import Board
from state import *
from algo import backtracking
# from board_node import *

def main():
    #board = Board(6)
    #solved = backtracking(board, board.start, board.goal)
    #board.print_board()
    board = Board(6)
    state = BoardState(board.start, board)
    bfs(state)


if __name__ == "__main__":
    main()
