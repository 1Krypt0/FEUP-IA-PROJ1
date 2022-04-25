from menu import handle_main_menu
from board import Board
from heuristics import manhattan_distance
from state import BoardState, bfs, dfs, greedy, ids, ucs
from gui import run_game

def main():
    handle_main_menu()


if __name__ == "__main__":
    main()
