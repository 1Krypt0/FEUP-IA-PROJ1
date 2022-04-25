from menu import handle_main_menu
from pygame_game import run_game

def main():
    while True:
        option = int(input("1 - Run game in Pygame\n2 - Run in command line\n0 - Quit\nPlease select an option: "))
        if option == 1:
            run_game()
        elif option == 2:
            handle_main_menu()
        elif option==0:
            return


if __name__ == "__main__":
    main()
