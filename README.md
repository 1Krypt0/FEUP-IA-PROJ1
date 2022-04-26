# Take the L Puzzle

### Requirements

- Python 3.9
- Pygame

### Building and Running

To execute the program, run `python3 main.py`, while being inside the src folder

### How to Play

When starting the application, the user will be asked if he wants to run the application using the pygame gui, or the command line interface.

After making that choice, the user will be able to select whether he wants to play the game himself, see the computer solve the problems, or measure the performance of the algorithms.

If he chooses the computer, he will then be prompted to choose which algorithm to choose and, if applicable, the heuristic as well. The game will show the algorithm trying to figure out a path, and will halt when complete.

If instead the player decides to play, then he can control the direction he wishes to advance to using the WASD keys (and the arrow keys on the pygame gui), or B (Backspace on pygame) to go back one move.

Choosing the performance measurement utility will show the user a few measurements taken after running the different algorithms on the same board
