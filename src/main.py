from board import Board
from state import BoardState, bfs, dfs, ids


def main():
    board = Board(6)
    state1 = BoardState(board.start, board)
    print("BFS")
    bfs(state1)
    board.reset()
    state2 = BoardState(board.start, board)
    print("DFS, limited at 20")
    dfs(state2, 20)
    state3 = BoardState(board.start, board)
    print("IDS")
    ids(state3)
    


if __name__ == "__main__":
    main()
