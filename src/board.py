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
        self.visited_shapes = set()
        self.all_shapes = hardcoded_shapes()
        self.size = size

    def visit(self, pos):
        self.visited_shapes.add(self.board[pos[0]][pos[1]])
        self.visited[pos[0]][pos[1]] = 1

    def unvisit(self, pos):
        shape = self.board[pos[0]][pos[1]]
        if shape != 0:
            self.visited_shapes.discard(shape)
        self.visited[pos[0]][pos[1]] = 0

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
def hardcoded_shapes():
    return {0,1,2,3,4,5,6}