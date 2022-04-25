import pygame
from board import generate_board, Board
from state import BoardState

BG_COLOR = (180,180,180)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

WIDTH, HEIGHT = 1000, 1000
BOARD_POS_X, BOARD_POS_Y, BOARD_MAX_SIZE = WIDTH/2, 650, 800
SQUARE_SIZE = 75
CELL_SIZE = 50
FONT_SIZE = CELL_SIZE-20

def run_game(board_state : BoardState):

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.fill(WHITE)
    run = True

    draw_board(window, board_state)

    # while run:
    #     # draw_game(window, board_state.board)
    #     pass

    pygame.time.wait(1000)
    pygame.quit()
        
def draw_board(window, board: BoardState):
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
            font_pos_x, font_pos_y = (x+FONT_SIZE/3, y-FONT_SIZE/6)
            if(board.board[row][col] >= 10):
                font_pos_x -= FONT_SIZE/2

            # draw rectangle and number
            number_rect = pygame.Rect(font_pos_x, font_pos_y, FONT_SIZE, FONT_SIZE)
            window.blit(number, number_rect)

            x += SQUARE_SIZE
        y += SQUARE_SIZE
    pygame.display.update()