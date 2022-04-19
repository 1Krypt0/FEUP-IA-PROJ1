import types
from board import generate_board
from game import play
from heuristics import euclidian_distance, manhattan_distance, visited_l
from state import BoardState, bfs, dfs, ids, ucs, greedy, a_star

# Global Constants
consts = types.SimpleNamespace()
consts.PLAYER = 0
consts.DFS = 1
consts.BFS = 2
consts.IDS = 3
consts.UCS = 4
consts.GREEDY = 5
consts.A_STAR = 6


def handle_main_menu() -> None:
    while True:
        display_main_menu()
        option = read_option([0, 1, 2])
        match option:
            case 0:
                return
            case 1:
                handle_difficulty_menu(consts.PLAYER)
            case 2:
                handle_algo_menu()


def handle_algo_menu() -> None:
    display_algo_menu()
    option = read_option([0, 1, 2, 3, 4, 5, 6])
    match option:
        case 0:
            return
        case 1:
            handle_difficulty_menu(consts.DFS)
        case 2:
            handle_difficulty_menu(consts.BFS)
        case 3:
            handle_difficulty_menu(consts.IDS)
        case 4:
            handle_difficulty_menu(consts.UCS)
        case 5:
            handle_heuristics_menu(consts.GREEDY)
        case 6:
            handle_heuristics_menu(consts.A_STAR)


def handle_heuristics_menu(state: int) -> None:
    display_heuristics_menu()
    option = read_option([0, 1, 2, 3])
    match option:
        case 0:
            return
        case 1:
            handle_difficulty_menu(state, manhattan_distance)
        case 2:
            handle_difficulty_menu(state, euclidian_distance)
        case 3:
            handle_difficulty_menu(state, visited_l)
        case 4:
            handle_algo_menu()


def handle_difficulty_menu(player: int, heuristic=None) -> None:
    display_difficulty_menu()
    option = read_option([0, 1, 2, 3, 4])
    if option == 0:
        return
    board = generate_board(option)
    board_state = BoardState(board.start, board)
    handle_player(player, board_state, heuristic)


def handle_player(player: int, board: BoardState, heuristic=None) -> None:
    match player:
        case consts.PLAYER:
            print("Human with", board.board, "Board and heuristic", heuristic)
            play(board)
        case consts.DFS:
            print("DFS with", board.board, "Board and heuristic", heuristic)
            dfs(board, 20)
        case consts.BFS:
            print("BFS with", board.board, "Board and heuristic", heuristic)
            bfs(board)
        case consts.IDS:
            print("IDS with", board.board, "Board and heuristic", heuristic)
            ids(board)
        case consts.UCS:
            print("UCS with", board.board, "Board and heuristic", heuristic)
            ucs(board)
        case consts.GREEDY:
            print("GREEDY with", board.board, "Board and heuristic", heuristic)
            greedy(board, heuristic)
        case consts.A_STAR:
            print("A* with", board.board, "Board and heuristic", heuristic)
            a_star(board, heuristic)


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
    print("\t\tPlease select an option:")
    print("\t\t\t0. Exit")
    print("\t\t\t1. I want to play!")
    print("\t\t\t2. Let the Computer play!")


def display_difficulty_menu() -> None:
    display_banner()
    print("\t\tChoose your difficulty:")
    print("\t\t\t0. Go back")
    print("\t\t\t1. Easy")
    print("\t\t\t2. Medium")
    print("\t\t\t3. Hard")
    print("\t\t\t4. Extreme")


def display_algo_menu() -> None:
    display_banner()
    print("\t\tChoose your algorithm:")
    print("\t\t\t0. Go back")
    print("\t\t\t1. Depth-First Search ")
    print("\t\t\t2. Breadth-First Search")
    print("\t\t\t3. Iterative Deepening Search")
    print("\t\t\t4. Uniform Cost Search")
    print("\t\t\t5. Greedy Search ")
    print("\t\t\t6. A* Search")


def display_heuristics_menu() -> None:
    display_banner()
    print("\t\tChoose your heuristic:")
    print("\t\t\t0. Go back")
    print("\t\t\t1. Manhattan Distance")
    print("\t\t\t2. Euclidian Distance")
    print("\t\t\t3. Number of L Shapes visited")
