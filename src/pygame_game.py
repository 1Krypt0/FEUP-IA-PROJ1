import pygame
import types
from pygame_texts import texts, text_num
from pygame_draw import draw_menu
from typing import Callable
from board import generate_board
from game import pygame_play
from state import (
    BoardState,
    bfs,
    dfs,
    ids,
    ucs,
    greedy,
    a_star,
    run_perf_test,
    euclidian_distance,
    manhattan_distance,
    visited_l,
)


WIDTH, HEIGHT = 1000, 1000

# difficulty constants
consts = types.SimpleNamespace()
consts.PLAYER = 0
consts.DFS = 1
consts.BFS = 2
consts.IDS = 3
consts.UCS = 4
consts.GREEDY = 5
consts.A_STAR = 6

def run_game():

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    handle_main_menu(window)

    pygame.quit()
    

def handle_main_menu(game_window) -> None:
    while(True):
        draw_menu(game_window, texts[text_num.MAIN_MENU])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        pygame.quit()
                    case pygame.K_1:
                        handle_difficulty_menu(game_window, consts.PLAYER)
                    case pygame.K_2:
                        handle_algorithms_menu(game_window)
                    case pygame.K_3:
                        run_perf_test(pygame_game = True, window=game_window)

def handle_algorithms_menu(window) -> None:
    draw_menu(window, texts[text_num.ALGORITHMS])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return
                    case pygame.K_1:
                        handle_difficulty_menu(window, consts.DFS)
                    case pygame.K_2:
                        handle_difficulty_menu(window, consts.BFS)
                    case pygame.K_3:
                        handle_difficulty_menu(window, consts.IDS)
                    case pygame.K_4:
                        handle_difficulty_menu(window, consts.UCS)
                    case pygame.K_5:
                        handle_heuristics_menu(window, consts.GREEDY)
                    case pygame.K_6:
                        handle_heuristics_menu(window, consts.A_STAR)

def handle_difficulty_menu(window, player: int, heuristic=None) -> None:
    draw_menu(window, texts[text_num.DIFFICULTY])
    loop = True
    while loop:
        option = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return
                    case pygame.K_1:
                        option = 1
                        loop = False 
                    case pygame.K_2:
                        option = 2
                        loop = False 
                    case pygame.K_3:
                        option = 3
                        loop = False 
                    case pygame.K_4:
                        option = 4
                        loop = False
    board = generate_board(option)
    board_state = BoardState(board.start, board)
    handle_player(window, player, board_state, heuristic)
    return

def handle_heuristics_menu(window, state: int) -> None:
    draw_menu(window, texts[text_num.HEURISTICS])
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_ESCAPE:
                        return
                    case pygame.K_1:
                        handle_difficulty_menu(window, state, manhattan_distance)
                        return
                    case pygame.K_2:
                        handle_difficulty_menu(window, state, euclidian_distance)
                        return
                    case pygame.K_3:
                        handle_difficulty_menu(window, state, visited_l)
                        return

def handle_player(game_window, player: int, board: BoardState, heuristic=None) -> None:
    match player:
        case consts.PLAYER:
            pygame_play(board, game_window)
        case consts.DFS:
            dfs(board, 20, pygame_game=True, window=game_window)
        case consts.BFS:
            bfs(board, pygame_game=True, window=game_window)
        case consts.IDS:
            ids(board, pygame_game=True, window=game_window)
        case consts.UCS:
            ucs(board, pygame_game=True, window=game_window)
        case consts.GREEDY:
            greedy(board, heuristic, pygame_game=True, window=game_window)
        case consts.A_STAR:
            a_star(board, heuristic, pygame_game=True, window=game_window)