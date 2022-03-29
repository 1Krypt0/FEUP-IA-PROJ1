from board import Board
from algo import backtracking

def main():
    board = Board(6)
    solved = backtracking(board, board.start, board.goal)

if __name__ == "__main__":
    main()