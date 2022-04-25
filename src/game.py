from copy import deepcopy
from typing import Callable
from state import (
    BoardState,
    get_solution_from_previous,
    move_back,
    move_up,
    move_down,
    move_left,
    move_right,
)
from board import is_solved
from gui import run_game


def play(board: BoardState) -> list:
    while not is_solved((board.x, board.y), (board.goal_x, board.goal_y), board.board):
        print(board.board)
        run_game(board.board)
        move = choose_move()
        dummy = deepcopy(board)
        if move(dummy) is None:
            print("That's an invalid move! I'm staying right where I am")
            continue
        else:
            board = move(board)
    return get_solution_from_previous(board)


def choose_move() -> Callable[[BoardState], BoardState | None]:
    print("")
    option = input(
        "Enter your move here (w - UP, a - LEFT, s - DOWN, d - RIGHT, b - BACK): "
    )
    acceptable = ["w", "a", "s", "d", "b"]
    while option not in acceptable:
        print("That's an invalid option. Choose again")
        option = input(
            "Enter your option here (w - UP, a - LEFT, s - DOWN, d - RIGHT, b - BACK): "
        )
    if option == "w":
        return move_up
    elif option == "a":
        return move_left
    elif option == "s":
        return move_down
    elif option == "d":
        return move_right
    elif option == "b":
        return move_back
    else:
        return lambda board: board
