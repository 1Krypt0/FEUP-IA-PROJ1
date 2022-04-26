import pygame
from board import Board
import time

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
BG_COLOR = WHITE

# Game constants
WIDTH, HEIGHT = 1000, 1000
BOARD_POS_X, BOARD_POS_Y, BOARD_MAX_SIZE = WIDTH/2, 650, 800
SQUARE_SIZE = 75
CELL_SIZE = 50
GAME_FONT_SIZE = CELL_SIZE-20

# Menu constants
TEXT_BEGIN_X, TEXT_BEGIN_Y, TEXT_OFFSET_Y = 50, 50, 50
OPTION_BEGIN_X = 100

'''
    Functions used for drawing on the pygame application's screen
'''

def draw_logo(window):
    logo = pygame.image.load('logo.png')
    window.blit(logo, (114, 100))

def draw_menu(window, menu: list) -> None:
    window.fill(BG_COLOR)
    font_title = pygame.font.SysFont("Times New Roman", 30)
    font_option = pygame.font.SysFont("Times New Roman", 20)

    draw_logo(window)

    item_num = len(menu)
    y = HEIGHT/2 - item_num/2*50
    for item in menu:
        item_font = font_title if (item == menu[0]) else font_option
        x = 100 if (item == menu[0]) else 150
        menu_rect = pygame.Rect(x, y, WIDTH-2*x, y)
        menu_item = item_font.render(item, True, BLACK)
        window.blit(menu_item, menu_rect)
        y += 50

    pygame.display.update()

def draw_intermediate(window, board: Board, algo, heuristic=None) -> None:
    title = "Calculating path"
    description = [
        "Algorithm: " + algo
    ]
    if not heuristic==None:
        description.append("Heuristic: " + heuristic.__name__)
    draw_board(window, board, title, description)

def draw_final(window, board: Board, duration, node_count, algo, heuristic = None) -> None:
    title = "Solution found."
    heur = "No Heuristic"
    if not heuristic==None:
        heur = "Heuristic: " + heuristic.__name__
    description = [
        "Algorithm: " + algo,
        heur,
        "Board obtained after: " + str(duration) + " seconds",
        "Nodes visited: " + str(node_count)
    ]
    if algo == "Player":
        description = []
    draw_board(window, board, title, description, final=True)
    time.sleep(2)

def draw_player(window, board: Board) -> None:
    title = "Instructions:"
    description = [
        "UP or \'w\' to move up",
        "DOWN or \'s\' to move down",
        "LEFT or \'a\' to move left",
        "RIGHT or \'d\' to move right",
        "\'b\' to move back",
        "ESC to quit"
    ]

    draw_board(window, board, title, description)

def draw_board(window, board: Board, title, description, final=False) -> None:
    window.fill(BG_COLOR)

    desc_title_size = 30
    description_font_size = 20
    desc_title_font = pygame.font.SysFont("Times New Roman", desc_title_size)
    description_font = pygame.font.SysFont("Times New Roman", description_font_size)
    desc_y = 50
    desc_x = 100
    title = desc_title_font.render(title, True, BLACK)
    title_rect = pygame.Rect(desc_x, desc_y, desc_title_size, desc_title_size)
    window.blit(title, title_rect)
    desc_x += 50
    desc_y += 50
    for desc in description:
        desc_text = description_font.render(desc, True, BLACK)
        desc_rect = pygame.Rect(desc_x, desc_y, description_font_size, description_font_size)
        window.blit(desc_text, desc_rect)
        desc_y += description_font_size + 10

    number_font = pygame.font.SysFont("Times New Roman", 55)

    board_size = len(board.board)
    board_offset_x = BOARD_POS_X-board_size*SQUARE_SIZE/2
    board_offset_y = BOARD_POS_Y-board_size*SQUARE_SIZE/2

    board_rec = pygame.Rect(0, 0, board_size*SQUARE_SIZE, board_size*SQUARE_SIZE)
    board_rec.center = (BOARD_POS_X, BOARD_POS_Y)
    pygame.draw.rect(window, BLACK, board_rec,0)

    start_x = board_offset_x + 14
    y = board_offset_y + 14
    for row in range(0, board_size):
        x = start_x
        for col in range(0, board_size):
            # draw cell
            pygame.draw.rect(window, WHITE, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE),0)
            # get number color
            number_color = RED if (board.visited[row][col]) else BLACK
            if final and row == board_size-1 and col == 0:
                number_color = RED
            # get number and numberpos
            number = number_font.render(str(board.board[row][col]), True, number_color)
            font_pos_x, font_pos_y = (x+GAME_FONT_SIZE/3, y-GAME_FONT_SIZE/6)
            if(board.board[row][col] >= 10):
                font_pos_x -= GAME_FONT_SIZE/2

            # draw rectangle and number
            number_rect = pygame.Rect(font_pos_x, font_pos_y, GAME_FONT_SIZE, GAME_FONT_SIZE)
            window.blit(number, number_rect)

            x += SQUARE_SIZE
        y += SQUARE_SIZE

    pygame.display.update()