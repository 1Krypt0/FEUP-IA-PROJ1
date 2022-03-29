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

    def visit(self, pos):
        self.visited[pos[0]][pos[1]] = 1

    def print_board(self):
        print("_____________")
        for line in range(self.size):
            for col in range(self.size):
                if(self.visited[line][col] == 1):
                    print("|" + Colors.red + str(self.board[line][col]) + Colors.reset, end='')
                else:
                    print("|" + str(self.board[line][col]), end='')
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
