import pygame
from board import generate_board, Board
from state import BoardState
BG_COLOR = (180,180,180)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
CELL_SIZE = 100

def run_game(board_state : BoardState):

    boardSize = len(board_state.board)
    width = boardSize * 100
    height = boardSize * 100

    pygame.init()
    window = pygame.display.set_mode((width, height))
    window.fill(BLACK)
    run = True

    draw_game(window, board_state)

    # while run:
    #     # draw_game(window, board_state.board)
    #     pass

    pygame.time.wait(1000)
    pygame.quit()
        
def draw_game(window, board: BoardState):
    boardSize = len(board.board)

    font = pygame.font.SysFont("Times New Roman", 55)

    start_x = 14
    y = 14
    for row in range(0, boardSize):
        x = start_x
        for col in range(0, boardSize):
            # draw cell
            pygame.draw.rect(window, WHITE, pygame.Rect(x, y, 75, 75),0)

            # get number color
            number_color = RED if (board.visited[row][col]) else BLACK
            # get number and numberpos
            number = font.render(str(board.board[row][col]), True, number_color)
            number_rect = pygame.Rect(x+24, y+6, 55, 55)

            window.blit(number, number_rect)
            x += 100
        y += 100
    pygame.display.update()