import pygame
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
from pygame_draw import draw_board

def pygame_play(board: BoardState, window):
    while not is_solved((board.x, board.y), (board.goal_x, board.goal_y), board.board):
        draw_board(window, board)
        move = pygame_choose_move()
        dummy = deepcopy(board)
        if move(dummy) is None:
            print("That's an invalid move! I'm staying right where I am")
            continue
        else:
            board = move(board)
    return get_solution_from_previous(board)


def pygame_choose_move() -> Callable[[BoardState], BoardState | None]:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return
                    case pygame.K_UP:
                        return move_up
                    case pygame.K_w:
                        return move_up
                    case pygame.K_LEFT:
                        return move_left
                    case pygame.K_a:
                        return move_left
                    case pygame.K_DOWN:
                        return move_down
                    case pygame.K_s:
                        return move_down
                    case pygame.K_RIGHT:
                        return move_right
                    case pygame.K_d:
                        return move_right
                    case pygame.K_b:
                        return move_back

def play(board: BoardState) -> list:
    """
    Handles the game loop for human plays mode

        Parameters:
            board (BoardState): the board state

        Returns:
            solution (list): the path taken to the goal 
    """
    while not is_solved((board.x, board.y), (board.goal_x, board.goal_y), board.board):
        print(board.board)
        move = choose_move()
        dummy = deepcopy(board)
        if move(dummy) is None:
            print("That's an invalid move! I'm staying right where I am")
            continue
        else:
            board = move(board)
    return get_solution_from_previous(board)


def choose_move() -> Callable[[BoardState], BoardState | None]:
    """
    Reads user input and translates it to one of the valid move functions

        Returns:
            move (function): the function that generates the following state
    """
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
