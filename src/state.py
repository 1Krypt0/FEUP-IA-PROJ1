from board import Board, check_valid
from copy import deepcopy
from queue import PriorityQueue
from algo import check_valid, is_solved
from time import sleep

"""

Classes
----------
BoardState


Functions
----------
bfs
dfs
ids
ucs

"""


class BoardState:
    """
    A class to represent a state of the board.

    ...

    Attributes
    ----------
    goal_x : int
        x coordinate of the goal spot
    goal_y : int
        y coordinate of the goal spot
    x : int
        x coordinate of the current spot
    y : int
        y coordinate of the current spot
    board : Board
        current content of the board
    previous_node : BoardState
        the previous state in the path
    next_node : BoardState
        the next state in the path

    Methods
    -------
    """

    def __init__(self, pos, board: Board, previous_node=None, next_node=None) -> None:
        """
        Constructs all the necessary attributes for the BoardState object.

        ...

        Parameters
        ----------
        goal_x : int
            x coordinate of the goal spot
        goal_y : int
            y coordinate of the goal spot
        x : int
            x coordinate of the current spot
        y : int
            y coordinate of the current spot
        board : Board
            current content of the board
        previous_node : BoardState
            the previous state in the path
        next_node : BoardState
            the next state in the path

        """
        self.goal_y, self.goal_x = board.goal
        self.y, self.x = pos
        self.board = board
        self.previous_node = previous_node
        self.next_node = next_node

    def __eq__(self, __o: object) -> bool:
        """
        Checks if two BoardStates are the same

        """
        return isinstance(__o, BoardState) and self.board == __o.board

    def __lt__(self, __o: object) -> bool:
        """
        Compares two BoardStates

        """
        return isinstance(__o, BoardState) and self.x == __o.x

    def __repr__(self):
        """
        Represents a board state by the current position's coordinates

        """
        return f"(x: {self.x}, y: {self.y})"


# Operators


def move_up(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone up by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving up
    """
    new_pos = (state.y - 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_down(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone down by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving down
    """
    new_pos = (state.y + 1, state.x)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_left(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone left by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving left
    """
    new_pos = (state.y, state.x - 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_right(state: BoardState) -> BoardState | None:
    """
    Generate a next state where the player has gone right by one spot

        Parameters:
            state (BoardState): the current state

        Returns:
            new_state (BoardState): the state after moving right
    """
    new_pos = (state.y, state.x + 1)
    if not check_valid(state.board, new_pos):
        return
    new_board = deepcopy(state.board)
    new_board.visit(new_pos)
    newstate = BoardState(new_pos, new_board)
    newstate.previous_node = state
    return newstate


def move_back(state: BoardState) -> BoardState:
    if state.previous_node is None:
        return state
    else:
        return state.previous_node


OPERATORS = {move_up: 1, move_down: 1, move_left: 1, move_right: 1}

# Search algorithms


def bfs(start: BoardState) -> list:
    """
    Run breadth-first search to find a solution to the game.

        Parameters:
            start (BoardState): the starting state

        Returns:
            path (list): the path from the starting state to the final state
    """
    queue = [start]
    solution = None

    while queue:
        current = queue.pop(0)
        sleep(0.1)
        print(current.board)
        if is_solved(
            (current.y, current.x), (current.goal_y, current.goal_x), current.board
        ):
            solution = current
            break
        for op in OPERATORS:
            next = op(current)
            if not next:
                continue
            next.previous_node = current
            queue.append(next)

    return get_solution_from_previous(solution)


def dfs(state: BoardState, max_depth: int) -> list:
    """
    Run depth-first search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state
            max_depth (int): the limit of the depth to explore

        Returns:
            path (list): the path from the starting state to the final state
    """
    if dfs_rec(state, 0, max_depth):
        return get_solution_from_next(state)


def dfs_rec(state: BoardState, current_depth: int, max_depth: int) -> bool:
    """
    Auxiliary function to run depth-first search to find a solution to the game.

        Parameters:
            state (BoardState): the state that is being currently explored
            current_depth (int): the depth of the current state
            max_depth (int): the limit of the depth to explore

        Returns:
            found (bool): whether a solution has been found
    """
    sleep(0.1)
    print(state.board)
    if current_depth == max_depth:
        return False

    if is_solved((state.y, state.x), (state.goal_y, state.goal_x), state.board):
        return True

    for op in OPERATORS:
        next = op(state)
        if not next:
            continue
        state.next_node = next
        if dfs_rec(next, current_depth + 1, max_depth):
            return True

    return False


def ids(state: BoardState) -> list:
    """
    Run iterative deepening search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state

        Returns:
            path (list): the path from the starting state to the final state
    """
    depth = 0
    while True:
        sleep(0.1)
        print(state.board)
        if not dfs(state, depth):
            depth += 1
        else:
            return get_solution_from_next(state, False)


def ucs(start: BoardState) -> list:
    """
    Run uniform cost search to find a solution to the game.

        Parameters:
            state (BoardState): the starting state

        Returns:
            path (list): the path from the starting state to the final state
    """
    queue = PriorityQueue()
    queue.put((0, [start]))

    while queue:
        pair = queue.get()
        current = pair[1][-1]
        sleep(0.1)
        print(current.board)
        if is_solved(
            (current.y, current.x), (current.goal_y, current.goal_x), current.board
        ):
            solution = current
            break
        for op in OPERATORS:
            next = op(current)
            if not next:
                continue
            next.previous_node = current
            queue.put((pair[0] + OPERATORS[op], [next]))

    return get_solution_from_previous(solution)


def get_solution_from_next(state: BoardState, show: bool = True) -> list:
    """
    Calculate the path saved in a state's next attribute

        Parameters:
            state (BoardState): starting state
            show (bool, default: True): whether or not to print the final board

        Returns:
            path (list): the path from the starting state to the final state
    """
    path = []
    while state:
        path.append(state)
        state = state.next_node
    if show:
        print(path[-1].board)
    return path


def get_solution_from_previous(state: BoardState, show=True) -> list:
    """
    Calculate the path saved in a state's previous attribute

        Parameters:
            state (BoardState): final state
            show (bool, default: True): whether or not to print the final board

        Returns:
            path (list): the path from the starting state to the final state
    """
    path = []
    if state:
        if show:
            print(state.board)
        while state:
            path.append(state)
            state = state.previous_node

    return list(reversed(path))
