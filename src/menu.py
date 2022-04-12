AI_GAME = False


def handle_main_menu() -> None:
    display_main_menu()
    option = read_option([1, 2, 3])
    if option == 1:
        handle_difficulty_menu()
    elif option == 2:
        AI_GAME = True
        handle_algo_menu()
    elif option == 3:
        return


def handle_difficulty_menu() -> None:
    display_difficulty_menu()
    option = read_option([1, 2, 3, 4, 5])
    if option == 1:
        print("Choosing easy board (small one)")
    elif option == 2:
        print("Choosing a medium board (meh)")
    elif option == 3:
        print("Choosing a hard board")
    elif option == 4:
        print("Choosing an extreme board. Good luck")
    elif option == 5:
        handle_main_menu()


def handle_algo_menu() -> None:
    display_algo_menu()
    option = read_option([1, 2, 3, 4, 5, 6, 7])
    if option == 1:
        print("Choosing dfs")
    elif option == 2:
        print("Choosing a bfs")
    elif option == 3:
        print("Choosing ids")
    elif option == 4:
        print("Choosing ucs")
    elif option == 5:
        print("Choosing greedy")
    elif option == 6:
        print("Choosing A*")
    elif option == 7:
        handle_main_menu()


def read_option(acceptable_options: list) -> int:
    print("")
    option = input("Enter your option here: ")
    while not option.isnumeric() or int(option) not in acceptable_options:
        print("That's an invalid option. Choose again")
        option = input("Enter your option here: ")
    return int(option)


def display_main_menu() -> None:
    print("___________       __              __  .__             .____     ")
    print("\\__    ___/____  |  | __ ____   _/  |_|  |__   ____   |    |    ")
    print("  |    |  \\__  \\ |  |/ // __ \\  \\   __\\  |  \\_/ __ \\  |    |    ")
    print("  |    |   / __ \\|    <\\  ___/   |  | |   Y  \\  ___/  |    |___ ")
    print("  |____|  (____  /__|_ \\\\___  >  |__| |___|  /\\___  > |_______ \\")
    print("               \\/     \\/    \\/             \\/     \\/          \\/")
    print("")
    print("                    1. I want to play!                            ")
    print("                    2. Let the Computer play!                       ")
    print("                    3. Exit the Game                                ")


def display_difficulty_menu() -> None:
    print("")
    print("___________       __              __  .__             .____     ")
    print("\\__    ___/____  |  | __ ____   _/  |_|  |__   ____   |    |    ")
    print("  |    |  \\__  \\ |  |/ // __ \\  \\   __\\  |  \\_/ __ \\  |    |    ")
    print("  |    |   / __ \\|    <\\  ___/   |  | |   Y  \\  ___/  |    |___ ")
    print("  |____|  (____  /__|_ \\\\___  >  |__| |___|  /\\___  > |_______ \\")
    print("               \\/     \\/    \\/             \\/     \\/          \\/")
    print("")
    print("                    Choose your difficulty:                        ")
    print("                           1. Easy                            ")
    print("                           2. Medium                       ")
    print("                           3. Hard")
    print("                           4. Extreme")
    print("                           5. Go back")


def display_algo_menu() -> None:
    print("")
    print("___________       __              __  .__             .____     ")
    print("\\__    ___/____  |  | __ ____   _/  |_|  |__   ____   |    |    ")
    print("  |    |  \\__  \\ |  |/ // __ \\  \\   __\\  |  \\_/ __ \\  |    |    ")
    print("  |    |   / __ \\|    <\\  ___/   |  | |   Y  \\  ___/  |    |___ ")
    print("  |____|  (____  /__|_ \\\\___  >  |__| |___|  /\\___  > |_______ \\")
    print("               \\/     \\/    \\/             \\/     \\/          \\/")
    print("")
    print("                    Choose your algorithm:                        ")
    print("                    1. Depth-First Search ")
    print("                    2. Breadth-First Search")
    print("                    3. Iterative Deepening Search")
    print("                    4. Uniform Cost Search")
    print("                    5. Greedy Search ")
    print("                    6. A* Search")
    print("                    7. Go back")
