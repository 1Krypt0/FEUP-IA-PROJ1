from board import Board
from state import *
#from algo import backtracking, bfs
# from board_node import *

def main():
    #board = Board(6)
    #solved = backtracking(board, board.start, board.goal)
    board = Board(6)
    board.visit((3,3))
    board.print_board()
    state = BoardState((3,3), board)
    next = move_down(state)
    if next:
        next.board.print_board()


if __name__ == "__main__":
    main()
