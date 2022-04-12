from menu import choose_option, display_menu, read_option


def main():
    # board = Board(6)
    # solved = backtracking(board, board.start, board.goal)
    # board.print_board()
    # board = Board(6)
    # state = BoardState(board.start, board)
    # bfs(state)
    display_menu()
    option = read_option()
    while True:
        if choose_option(option):
            break
        else:
            option = read_option()


if __name__ == "__main__":
    main()
