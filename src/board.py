# PROBLEM
#       VISITED IS UPDATING THE VISITED INSIDE THE BOARD CLASS
#           IS THE ONE I'M PASSING JUST A REFERENCE TO THE ACTUAL OBJECT???
#           WE DON'T WANT THAT, WE WANT A COPY (so that changes persist)


class Colors:
    red='\033[31m'
    reset='\033[0m'

class Board:
    def __init__(self, size: int):
        # self.board = generate_board()
        self.board = hardcoded_board()
        self.start = (size-1, 0)
        self.goal = (0,size-1)
        self.visited = [[0 for col in range(size)] for lin in range(size)]
        self.size = size

    # moved implementation to algo.py
    def visit(self, pos):
        self.visited[pos[0]][pos[1]] = 1

    def print_board(self):
        print("_____________")
        for line in range(self.size):
            for col in range(self.size):
                change_color = self.visited
                print("|" + Colors.red * self.visited[line][col] + str(self.board[line][col]) + Colors.reset, end='')
            print("|")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")


def generate_board(size):
    return [[0 for col in range(size)] for lin in range(size)]

def hardcoded_board():
    return [
                [1,1,1,2,2,0],
                [0,3,1,2,4,0],
                [0,3,0,2,4,6],
                [0,3,3,4,4,6],
                [0,5,5,5,6,6],
                [0,0,0,5,0,0]
            ]
