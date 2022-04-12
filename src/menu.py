from board import generate_board
from heuristics import euclidian_distance, manhattan_distance, visited_l
from state import BoardState

# Global Constants
PLAYER = 0
DFS = 1
BFS = 2
IDS = 3
UCS = 4
GREEDY = 5
A_STAR = 6


def handle_main_menu() -> None:
    display_main_menu()
    option = read_option([1, 2, 3])
    if option == 1:
        handle_difficulty_menu(PLAYER)
    elif option == 2:
        handle_algo_menu()
    elif option == 3:
        return


def handle_algo_menu() -> None:
    display_algo_menu()
    option = read_option([1, 2, 3, 4, 5, 6, 7])
    if option == 1:
        handle_difficulty_menu(DFS)
    elif option == 2:
        handle_difficulty_menu(BFS)
    elif option == 3:
        handle_difficulty_menu(IDS)
    elif option == 4:
        handle_difficulty_menu(UCS)
    elif option == 5:
        handle_heuristics_menu(GREEDY)
    elif option == 6:
        handle_heuristics_menu(A_STAR)
    elif option == 7:
        handle_main_menu()


def handle_heuristics_menu(state: int) -> None:
    display_heuristics_menu()
    option = read_option([1, 2, 3, 4])
    if option == 1:
        handle_difficulty_menu(state, manhattan_distance)
    elif option == 2:
        handle_difficulty_menu(state, euclidian_distance)
    elif option == 3:
        handle_difficulty_menu(state, visited_l)
    elif option == 4:
        handle_algo_menu()


def handle_difficulty_menu(player: int, heuristic=None) -> None:
    display_difficulty_menu()
    option = read_option([1, 2, 3, 4, 5])
    board = generate_board(option)
    board_state = BoardState(board.start, board)
    handle_player(player, board_state, heuristic)


def handle_player(player: int, board: BoardState, heuristic=None) -> None:
    if player == PLAYER:
        print("Human with", board.board, "Board and heuristic", heuristic)
        pass  # Change to play()
    elif player == DFS:
        print("DFS with", board.board, "Board and heuristic", heuristic)
        pass  # Change to DFS()
    elif player == BFS:
        print("BFS with", board.board, "Board and heuristic", heuristic)
        pass  # Change to BFS()
    elif player == IDS:
        print("IDS with", board.board, "Board and heuristic", heuristic)
        pass  # Change to IDS()
    elif player == UCS:
        print("UCS with", board.board, "Board and heuristic", heuristic)
        pass  # Change to UCS()
    elif player == GREEDY:
        print("GREEDY with", board.board, "Board and heuristic", heuristic)
        pass  # Change to Greedy
    elif player == A_STAR:
        print("A* with", board.board, "Board and heuristic", heuristic)
        pass  # Change to A*


def read_option(acceptable_options: list) -> int:
    print("")
    option = input("Enter your option here: ")
    while not option.isnumeric() or int(option) not in acceptable_options:
        print("That's an invalid option. Choose again")
        option = input("Enter your option here: ")
    return int(option)


def display_banner() -> None:
    print("")
    print("___________       __              __  .__             .____     ")
    print("\\__    ___/____  |  | __ ____   _/  |_|  |__   ____   |    |    ")
    print("  |    |  \\__  \\ |  |/ // __ \\  \\   __\\  |  \\_/ __ \\  |    |    ")
    print("  |    |   / __ \\|    <\\  ___/   |  | |   Y  \\  ___/  |    |___ ")
    print("  |____|  (____  /__|_ \\\\___  >  |__| |___|  /\\___  > |_______ \\")
    print("               \\/     \\/    \\/             \\/     \\/          \\/")
    print("")


def display_main_menu() -> None:
    display_banner()
    print("                    1. I want to play!                            ")
    print("                    2. Let the Computer play!                       ")
    print("                    3. Exit the Game                                ")


def display_difficulty_menu() -> None:
    display_banner()
    print("                    Choose your difficulty:                        ")
    print("                           1. Easy                            ")
    print("                           2. Medium                       ")
    print("                           3. Hard")
    print("                           4. Extreme")
    print("                           5. Go back")


def display_algo_menu() -> None:
    display_banner()
    print("                    Choose your algorithm:                        ")
    print("                    1. Depth-First Search ")
    print("                    2. Breadth-First Search")
    print("                    3. Iterative Deepening Search")
    print("                    4. Uniform Cost Search")
    print("                    5. Greedy Search ")
    print("                    6. A* Search")
    print("                    7. Go back")


def display_heuristics_menu() -> None:
    display_banner()
    print("                    Choose your heuristic:                        ")
    print("                    1. Manhattan Distance")
    print("                    2. Euclidian Distance")
    print("                    3. Number of L Shapes visited")
    print("                    4. Go back")
