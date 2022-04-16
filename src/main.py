from menu import handle_main_menu
from board import Board
from heuristics import manhattan_distance
from state import BoardState, bfs, dfs, greedy, ids, ucs


def main():
    handle_main_menu()
    '''
    board = Board(6)
    state1 = BoardState(board.start, board)
    print("BFS")
    bfs(state1)
    board.reset()
    state2 = BoardState(board.start, board)
    print("DFS, limited at 20")
    dfs(state2, 20)
    board.reset()
    state3 = BoardState(board.start, board)
    print("IDS")
    ids(state3)
    board.reset()
    print("UCS")
    state4 = BoardState(board.start, board)
    ucs(state4)
    board.reset()
    print("Greedy")
    state5 = BoardState(board.start, board)
    greedy(state5, manhattan_distance)
    print("A*")
    state6 = BoardState(board.start, board)
    greedy(state6, manhattan_distance)
    '''

if __name__ == "__main__":
    main()
