import types

# menu text constants
text_num = types.SimpleNamespace()
text_num.BANNER = 0
text_num.MAIN_MENU = 1
text_num.DIFFICULTY = 2
text_num.ALGORITHMS = 3
text_num.HEURISTICS = 4

texts = [
    [
        "",
        "___________       __              __  .__             .____     ",
        "\\__    ___/____  |  | __ ____   _/  |_|  |__   ____   |    |    ",
        "  |    |  \\__  \\ |  |/ // __ \\  \\   __\\  |  \\_/ __ \\  |    |    ",
        "  |    |   / __ \\|    <\\  ___/   |  | |   Y  \\  ___/  |    |___ ",
        "  |____|  (____  /__|_ \\\\___  >  |__| |___|  /\\___  > |_______ \\",
        "               \\/     \\/    \\/             \\/     \\/          \\/"
    ],
    [
        "Please select an option:",
        "1. I want to play!",
        # "2. Let the Computer play!",
        # "3. Run performance test!",
        "Esc - Exit"
    ],
    [
        "Choose your difficulty:",
        "1. Easy",
        "2. Medium",
        "3. Hard",
        "4. Extreme",
        "Esc - Go back"
    ],
    [
        "Choose your algorithm:",
        "1. Depth-First Search ",
        "2. Breadth-First Search",
        "3. Iterative Deepening Search",
        "4. Uniform Cost Search",
        "5. Greedy Search ",
        "6. A* Search",
        "Esc - Go back"
    ],
    [
        "Choose your heuristic:",
        "1. Manhattan Distance",
        "2. Euclidian Distance",
        "3. Number of L Shapes visited",
        "Esc - Go back"
    ]
]