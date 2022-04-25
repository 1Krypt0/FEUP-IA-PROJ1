import types
import pygame
from board import generate_board, Board
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

# menu text constants
text_num = types.SimpleNamespace()
text_num.BANNER = 0
text_num.MAIN_MENU = 1
text_num.DIFFICULTY = 2
text_num.ALGORITHMS = 3
text_num.HEURISTICS = 4

texts = [
    [
        "",
        "___________       __              __  .__             .____     ",
        "\\__    ___/____  |  | __ ____   _/  |_|  |__   ____   |    |    ",
        "  |    |  \\__  \\ |  |/ // __ \\  \\   __\\  |  \\_/ __ \\  |    |    ",
        "  |    |   / __ \\|    <\\  ___/   |  | |   Y  \\  ___/  |    |___ ",
        "  |____|  (____  /__|_ \\\\___  >  |__| |___|  /\\___  > |_______ \\",
        "               \\/     \\/    \\/             \\/     \\/          \\/"
    ],
    [
        "Please select an option:",
        "1. I want to play!",
        "2. Let the Computer play!",
        "3. Run performance test!",
        "Esc - Exit"
    ],
    [
        "Choose your difficulty:",
        "1. Easy",
        "2. Medium",
        "3. Hard",
        "4. Extreme",
        "Esc - Go back"
    ],
    [
        "Choose your algorithm:",
        "1. Depth-First Search ",
        "2. Breadth-First Search",
        "3. Iterative Deepening Search",
        "4. Uniform Cost Search",
        "5. Greedy Search ",
        "6. A* Search",
        "Esc - Go back"
    ],
    [
        "Choose your heuristic:",
        "1. Manhattan Distance",
        "2. Euclidian Distance",
        "3. Number of L Shapes visited",
        "Esc - Go back"
    ]
]

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
    window.fill(BG_COLOR)

    while True:
        handle_main_menu(window)
    pygame.quit()
    

def handle_main_menu(window) -> None:
    draw_menu(window, texts[text_num.MAIN_MENU])
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            match event.key:
                case pygame.K_ESCAPE:
                    pygame.quit()
                case pygame.K_1:
                    handle_difficulty_menu(window, consts.PLAYER)
                case pygame.K_2:
                    handle_algorithms_menu(window)
                case pygame.K_3:
                    run_perf_test()

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
    handle_player(player, board_state, heuristic)
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
                        handle_difficulty_menu(state, manhattan_distance)
                        return
                    case pygame.K_2:
                        handle_difficulty_menu(state, euclidian_distance)
                        return
                    case pygame.K_3:
                        handle_difficulty_menu(state, visited_l)
                        return

def handle_player(player: int, board: BoardState, heuristic=None) -> None:
    match player:
        case consts.PLAYER:
            play(board)
        case consts.DFS:
            dfs(board, 20)
        case consts.BFS:
            bfs(board)
        case consts.IDS:
            ids(board)
        case consts.UCS:
            ucs(board)
        case consts.GREEDY:
            greedy(board, heuristic)
        case consts.A_STAR:
            a_star(board, heuristic)

def play(board: BoardState):
    pass

def draw_menu(window, menu: list) -> None:
    window.fill(BG_COLOR)

    font_title = pygame.font.SysFont("Times New Roman", 30)
    font_option = pygame.font.SysFont("Times New Roman", 20)
    logo_size = 30

    # logo_x, logo_y = 50, 200
    # logo = texts[text_num.BANNER]
    # for part in logo:
    #     part_rect = pygame.Rect(logo_x, logo_y, GAME_FONT_SIZE, GAME_FONT_SIZE)
    #     part_text = font_title.render(part, True, BLACK)
    #     window.blit(part_text, part_rect)
    #     logo_y += logo_size

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

        
def draw_board(window, board: BoardState) -> None:
    window.fill(BG_COLOR)
    board_size = len(board.board)
    board_offset_x = BOARD_POS_X-board_size*SQUARE_SIZE/2
    board_offset_y = BOARD_POS_Y-board_size*SQUARE_SIZE/2

    board_rec = pygame.Rect(0, 0, board_size*SQUARE_SIZE, board_size*SQUARE_SIZE)
    board_rec.center = (BOARD_POS_X, BOARD_POS_Y)
    pygame.draw.rect(window, BLACK, board_rec,0)

    font = pygame.font.SysFont("Times New Roman", 55)

    start_x = board_offset_x + 14
    y = board_offset_y + 14
    for row in range(0, board_size):
        x = start_x
        for col in range(0, board_size):
            # draw cell
            pygame.draw.rect(window, WHITE, pygame.Rect(x, y, CELL_SIZE, CELL_SIZE),0)
            # get number color
            number_color = RED if (board.visited[row][col]) else BLACK
            # get number and numberpos
            number = font.render(str(board.board[row][col]), True, number_color)
            font_pos_x, font_pos_y = (x+GAME_FONT_SIZE/3, y-GAME_FONT_SIZE/6)
            if(board.board[row][col] >= 10):
                font_pos_x -= GAME_FONT_SIZE/2

            # draw rectangle and number
            number_rect = pygame.Rect(font_pos_x, font_pos_y, GAME_FONT_SIZE, GAME_FONT_SIZE)
            window.blit(number, number_rect)

            x += SQUARE_SIZE
        y += SQUARE_SIZE
    pygame.display.update()