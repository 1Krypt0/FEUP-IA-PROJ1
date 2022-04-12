def display_menu() -> None:
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


def choose_option(option: int) -> bool:
    if option == 1:
        print("Playing the game!")
        return True
    elif option == 2:
        print("Letting the computer play!")
        return True
    elif option == 3:
        return True
    else:
        print("That's an invalid option! Choose again.")
        return False


def read_option() -> int:
    print("")
    option = input("Enter your option here: ")
    if option.isnumeric():
        return int(option)
    else:
        print("That's an invalid option. Choose again")
        return read_option()
