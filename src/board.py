class Board:
    def __init__(self, size: int):
        # self.board = generate_board()
        self.board = hardcoded_board()
        self.goal = (0,size-1)
        self.start = (size-1, 0)

    def print_board(self):
        print("_____________")
        for line in self.board:
            for col in line:
                print("|" + str(col), end='')
            print("|")
        print("‾‾‾‾‾‾‾‾‾‾‾‾‾")


def generate_board():
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
